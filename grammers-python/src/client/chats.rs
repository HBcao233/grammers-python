use pyo3::exceptions::{PyIndexError, PyTypeError, PyValueError};
use pyo3::prelude::*;

use std::collections::HashMap;
use std::sync::Arc;

use super::PyClient;
use crate::errors::PyInvocationError;
use crate::hints::InputPeerLike;
use crate::peer::{Peer, PyPeerMap, PyUser};
use crate::utils::{parse_phone, parse_username};

use grammers_session_pyo3::PyPeerId;
use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

fn updates_to_chat(
    client: &PyClient,
    id: Option<i64>,
    updates: tl::enums::Updates,
) -> PyResult<Option<Peer>> {
    use tl::enums::Updates;

    let chats = match updates {
        Updates::Combined(updates) => Some(updates.chats),
        Updates::Updates(updates) => Some(updates.chats),
        _ => None,
    };

    let chat = match chats {
        Some(chats) => match id {
            Some(id) => chats.into_iter().find(|chat| chat.id() == id),
            None => chats.into_iter().next(),
        },
        None => None,
    };
    Ok(match chat {
        None => None,
        Some(x) => Some(Peer::from_raw(client, x)?),
    })
}

#[pymethods]
impl PyClient {
    /// Fetch information about the currently logged-in user.
    ///
    /// Although this method is cheap to call, you might want to
    /// use the `Client.me` attribute which automatically cached by `Client.start()` method.
    ///
    /// Both users and bots can use this method.
    ///
    /// # Examples
    ///
    /// ```ignore
    /// await client.get_me()
    /// ```
    pub async fn get_me(&self) -> PyResult<Py<PyUser>> {
        let mut res = self
            .invoke(&pytl::functions::users::PyGetUsers {
                id: vec![pytl::types::PyInputUserSelf {}.into()],
            })
            .await
            .map_err(PyInvocationError::new)?;

        match res.pop() {
            Some(user) => Python::attach(|py| Py::new(py, PyUser::new(self, user))),
            None => Err(PyIndexError::new_err("list index out of range")),
        }
    }

    /// Resolves a username (not prefix with '@') into the peer that owns it, if any.
    ///
    /// Note that this method is expensive to call, and can quickly cause long flood waits.
    ///
    /// Both users and bots can use this method.
    ///
    /// # Examples
    ///
    /// ```ignore
    /// if peer := await client.resolve_username("username"):
    ///     print("Found peer!: {:?}", peer.name)
    /// ```
    pub async fn resolve_username(&self, username: String) -> PyResult<Option<Peer>> {
        let username = match parse_username(&username) {
            Some(x) => x,
            None => return Err(PyValueError::new_err("Invalid username.")),
        };
        let request = tl::functions::contacts::ResolveUsername {
            username,
            referer: None,
        };
        let tl::types::contacts::ResolvedPeer { peer, users, chats } =
            match self.invoke(&request).await {
                Ok(tl::enums::contacts::ResolvedPeer::Peer(p)) => p,
                Err(err) if err.is("USERNAME_NOT_OCCUPIED") => return Ok(None),
                Err(err) => return Err(PyInvocationError::new(err)),
            };

        let res = match peer {
            tl::enums::Peer::User(tl::types::PeerUser { user_id }) => users
                .into_iter()
                .map(|user| Peer::from_user(self, user.into()))
                .collect::<PyResult<Vec<_>>>()?
                .into_iter()
                .find(|peer| peer.id() == PyPeerId::user(user_id).unwrap()),
            tl::enums::Peer::Chat(tl::types::PeerChat { chat_id }) => chats
                .into_iter()
                .map(|chat| Peer::from_raw(self, chat))
                .collect::<PyResult<Vec<_>>>()?
                .into_iter()
                .find(|peer| peer.id() == PyPeerId::chat(chat_id).unwrap()),
            tl::enums::Peer::Channel(tl::types::PeerChannel { channel_id }) => chats
                .into_iter()
                .map(|chat| Peer::from_raw(self, chat))
                .collect::<PyResult<Vec<_>>>()?
                .into_iter()
                .find(|peer| peer.id() == PyPeerId::channel(channel_id).unwrap()),
        };
        Ok(res)
    }

    /// Resolves a phone to a User.
    ///
    /// Both users and bots can use this method
    pub async fn resolve_phone(&self, phone: String) -> PyResult<Option<Py<PyUser>>> {
        let phone = match parse_phone(&phone) {
            Some(x) => x,
            None => return Err(PyValueError::new_err("Invalid phone.")),
        };
        let mut users = match self
            .invoke(&tl::functions::contacts::ResolvePhone { phone })
            .await
            .map_err(PyInvocationError::new)?
        {
            tl::enums::contacts::ResolvedPeer::Peer(x) => x.users,
        };

        Ok(match users.pop() {
            Some(x) => Some(Python::attach(|py| Py::new(py, PyUser::from_raw(self, x)))?),
            None => None,
        })
    }

    /// Resolves a InputPeer into a Peer.
    ///
    /// Both users and bots can use this method.
    pub async fn resolve_input_peer(
        &self,
        peer: pytl::enums::PyInputPeer,
    ) -> PyResult<Option<Peer>> {
        Ok(match peer {
            pytl::enums::PyInputPeer::Empty(_) => {
                return Err(PyTypeError::new_err(
                    "InputPeerEmpty can't resolve to any peer.",
                ));
            }
            pytl::enums::PyInputPeer::PeerSelf(_) => Some(Peer::User(self.get_me().await?)),
            pytl::enums::PyInputPeer::User(x) => {
                let (user_id, access_hash) = Python::attach(|py| {
                    let x = x.0.borrow(py);
                    (x.user_id, x.access_hash)
                });
                let mut res = self
                    .invoke(&tl::functions::users::GetUsers {
                        id: vec![
                            tl::types::InputUser {
                                user_id: user_id,
                                access_hash: access_hash,
                            }
                            .into(),
                        ],
                    })
                    .await
                    .map_err(PyInvocationError::new)?;
                match res.pop() {
                    Some(x) => Some(Peer::from_user(self, x)?),
                    None => None,
                }
            }
            pytl::enums::PyInputPeer::Chat(x) => {
                let chat_id = Python::attach(|py| x.0.borrow(py).chat_id);
                let mut res = match self
                    .invoke(&tl::functions::messages::GetChats { id: vec![chat_id] })
                    .await
                    .map_err(PyInvocationError::new)?
                {
                    tl::enums::messages::Chats::Chats(chats) => chats.chats,
                    tl::enums::messages::Chats::Slice(chat_slice) => chat_slice.chats,
                };
                match res.pop() {
                    Some(x) => Some(Peer::from_raw(self, x)?),
                    None => None,
                }
            }
            pytl::enums::PyInputPeer::Channel(x) => {
                let (channel_id, access_hash) = Python::attach(|py| {
                    let x = x.0.borrow(py);
                    (x.channel_id, x.access_hash)
                });
                let mut res = match self
                    .invoke(&tl::functions::channels::GetChannels {
                        id: vec![
                            tl::types::InputChannel {
                                channel_id: channel_id,
                                access_hash: access_hash,
                            }
                            .into(),
                        ],
                    })
                    .await
                    .map_err(PyInvocationError::new)?
                {
                    tl::enums::messages::Chats::Chats(chats) => chats.chats,
                    tl::enums::messages::Chats::Slice(chat_slice) => chat_slice.chats,
                };
                match res.pop() {
                    Some(x) => Some(Peer::from_raw(self, x)?),
                    None => None,
                }
            }
            pytl::enums::PyInputPeer::UserFromMessage(x) => {
                let (peer, msg_id, user_id) = Python::attach(|py| {
                    let x = x.0.borrow(py);
                    (x.peer.clone(), x.msg_id, x.user_id)
                });
                let mut res = self
                    .invoke(&tl::functions::users::GetUsers {
                        id: vec![
                            tl::types::InputUserFromMessage {
                                peer: peer.into(),
                                msg_id: msg_id,
                                user_id: user_id,
                            }
                            .into(),
                        ],
                    })
                    .await
                    .map_err(PyInvocationError::new)?;
                match res.pop() {
                    Some(x) => Some(Peer::from_user(self, x)?),
                    None => None,
                }
            }
            pytl::enums::PyInputPeer::ChannelFromMessage(x) => {
                let (peer, msg_id, channel_id) = Python::attach(|py| {
                    let x = x.0.borrow(py);
                    (x.peer.clone(), x.msg_id, x.channel_id)
                });
                let mut res = match self
                    .invoke(&tl::functions::channels::GetChannels {
                        id: vec![
                            tl::types::InputChannelFromMessage {
                                peer: peer.into(),
                                msg_id: msg_id,
                                channel_id: channel_id,
                            }
                            .into(),
                        ],
                    })
                    .await
                    .map_err(PyInvocationError::new)?
                {
                    tl::enums::messages::Chats::Chats(chats) => chats.chats,
                    tl::enums::messages::Chats::Slice(chat_slice) => chat_slice.chats,
                };
                match res.pop() {
                    Some(x) => Some(Peer::from_raw(self, x)?),
                    None => None,
                }
            }
        })
    }

    #[staticmethod]
    pub fn parse_invite_link(invite_link: String) -> Option<String> {
        let pattern = regex::Regex::new("^+?([a-zA-Z0-9_-]+)$").unwrap();
        if let Some(x) = pattern.captures(&invite_link) {
            return Some(x[1].to_string());
        }

        let invite_link = if !invite_link.contains("://") {
            "http://".to_owned() + &invite_link
        } else {
            invite_link
        };
        let res = url::Url::parse(&invite_link);
        if res.is_err() {
            return None;
        }

        let url_parse = res.unwrap();
        let scheme = url_parse.scheme();
        let path = url_parse.path();
        if url_parse.host_str().is_none() || !vec!["https", "http"].contains(&scheme) {
            return None;
        }

        let host = url_parse.host_str().unwrap();
        let hosts = [
            "t.me",
            "telegram.me",
            "telegram.dog",
            "tg.dev",
            "telegram.me",
            "telesco.pe",
        ];

        if !hosts.contains(&host) {
            return None;
        }
        let paths = path.split("/").skip(1).collect::<Vec<&str>>();

        if paths.len() == 1 {
            if paths[0].starts_with("+") {
                return Some(paths[0].replace("+", ""));
            }

            return None;
        }

        if paths.len() > 1 {
            if paths[0].starts_with("joinchat") {
                return Some(paths[1].to_string());
            }
            if paths[0].starts_with("+") {
                return Some(paths[0].replace("+", ""));
            }

            return None;
        }

        None
    }

    /// Resolves any InputPeerLike to a Peer.
    ///
    /// Both users and bots can use this method.
    pub async fn resolve_peer(&self, peer: InputPeerLike) -> PyResult<Option<Peer>> {
        match peer {
            InputPeerLike::Phone(x) => Ok(self.resolve_phone(x).await?.map(Peer::User)),
            InputPeerLike::Username(x) => self.resolve_username(x).await,
            InputPeerLike::InputPeer(x) => self.resolve_input_peer(x).await,
        }
    }

    /// Check the validity of a chat invite link and get basic info about it.
    ///
    /// Only users can use this method.
    pub async fn check_invite_link(
        &self,
        invite_link: String,
    ) -> PyResult<pytl::enums::PyChatInvite> {
        match Self::parse_invite_link(invite_link) {
            Some(hash) => self
                .invoke(&pytl::functions::messages::PyCheckChatInvite { hash })
                .await
                .map_err(PyInvocationError::new),
            None => Err(PyValueError::new_err("Invalid invite link.")),
        }
    }

    /// Import a chat invite and join a private chat/supergroup/channel.
    ///
    /// Only users can use this method.
    pub async fn accept_invite_link(&self, invite_link: String) -> PyResult<Option<Peer>> {
        match Self::parse_invite_link(invite_link) {
            Some(hash) => updates_to_chat(
                self,
                None,
                self.invoke(&tl::functions::messages::ImportChatInvite { hash })
                    .await
                    .map_err(PyInvocationError::new)?,
            ),
            None => Err(PyValueError::new_err("Invalid invite link.")),
        }
    }
}

impl PyClient {
    pub async fn build_peer_map(
        &self,
        users: Vec<tl::enums::User>,
        chats: Vec<tl::enums::Chat>,
    ) -> PyResult<PyPeerMap> {
        let session = self.inner.lock().unwrap().session.clone();
        let users = users
            .into_iter()
            .map(|user| Peer::from_user(self, user))
            .collect::<PyResult<Vec<_>>>()?;
        let chats = chats
            .into_iter()
            .map(|chat| Peer::from_raw(self, chat))
            .collect::<PyResult<Vec<_>>>()?;
        let map = users
            .into_iter()
            .chain(chats)
            .map(|peer| (peer.id(), peer))
            .collect::<HashMap<_, _>>();

        for peer in map.values() {
            if peer.auth().is_some() {
                session.cache_peer(peer.info()).await?;
            }
        }

        Ok(PyPeerMap {
            map: Arc::new(map),
            client: self.clone(),
        })
    }
}
