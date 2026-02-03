use pyo3::exceptions::{PyIndexError, PyTypeError};
use pyo3::prelude::*;

use std::collections::HashMap;
use std::sync::Arc;

use super::PyClient;
use crate::peer::{Peer, PyPeerMap, PyUser};
use crate::errors::PyInvocationError;

use grammers_session_pyo3::PyPeerId;
use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

#[pymethods]
impl PyClient {
    /// Fetch information about the currently logged-in user.
    ///
    /// Although this method is cheap to call, you might want to cache the results somewhere.
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
    /// # Examples
    ///
    /// ```ignore
    /// if peer := await client.resolve_username("username"):
    ///     print("Found peer!: {:?}", peer.name)
    /// ```
    pub async fn resolve_username(&self, username: String) -> PyResult<Option<Peer>> {
        let request = tl::functions::contacts::ResolveUsername {
            username: username.into(),
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
    
    /// Resolves a PeerIdLike or InputPeer into a Peer
    pub async fn resolve_peer(&self, peer: pytl::enums::PyInputPeer) -> PyResult<Option<Peer>> {
        Ok(match peer {
            pytl::enums::PyInputPeer::Empty(_) => return Err(PyTypeError::new_err(
                "InputPeerEmpty can't resolve to any peer."
            )),
            pytl::enums::PyInputPeer::PeerSelf(_) => Some(Peer::User(self.get_me().await?)),
            pytl::enums::PyInputPeer::User(x) => {
                let (user_id, access_hash) = Python::attach(|py| {
                    let x = x.0.borrow(py);
                    (x.user_id, x.access_hash)
                });
                let mut res = self
                    .invoke(&tl::functions::users::GetUsers {
                        id: vec![tl::types::InputUser {
                            user_id: user_id,
                            access_hash: access_hash,
                        }.into()],
                    })
                    .await
                    .map_err(PyInvocationError::new)?;
                match res.pop() {
                    Some(x) => Some(Peer::from_user(self, x)?),
                    None => None,
                }
            },
            pytl::enums::PyInputPeer::Chat(x) => {
                let chat_id = Python::attach(|py| {
                    x.0.borrow(py).chat_id
                });
                let mut res = match self
                    .invoke(&tl::functions::messages::GetChats {
                        id: vec![chat_id],
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
            },
            pytl::enums::PyInputPeer::Channel(x) => {
                let (channel_id, access_hash) = Python::attach(|py| {
                    let x = x.0.borrow(py);
                    (x.channel_id, x.access_hash)
                });
                let mut res = match self
                    .invoke(&tl::functions::channels::GetChannels {
                        id: vec![tl::types::InputChannel {
                            channel_id: channel_id,
                            access_hash: access_hash,
                        }.into()],
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
            },
            pytl::enums::PyInputPeer::UserFromMessage(x) => {
                let (peer, msg_id, user_id) = Python::attach(|py| {
                    let x = x.0.borrow(py);
                    (x.peer.clone(), x.msg_id, x.user_id)
                });
                let mut res = self
                    .invoke(&tl::functions::users::GetUsers {
                        id: vec![tl::types::InputUserFromMessage {
                            peer: peer.into(),
                            msg_id: msg_id,
                            user_id: user_id,
                        }.into()],
                    })
                    .await
                    .map_err(PyInvocationError::new)?;
                match res.pop() {
                    Some(x) => Some(Peer::from_user(self, x)?),
                    None => None,
                }
            },
            pytl::enums::PyInputPeer::ChannelFromMessage(x) => {
                let (peer, msg_id, channel_id) = Python::attach(|py| {
                    let x = x.0.borrow(py);
                    (x.peer.clone(), x.msg_id, x.channel_id)
                });
                let mut res = match self
                    .invoke(&tl::functions::channels::GetChannels {
                        id: vec![tl::types::InputChannelFromMessage {
                            peer: peer.into(),
                            msg_id: msg_id,
                            channel_id: channel_id,
                        }.into()],
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
            },
        })
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
