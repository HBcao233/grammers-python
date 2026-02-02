use pyo3::exceptions::PyIndexError;
use pyo3::prelude::*;

use std::collections::HashMap;
use std::sync::Arc;

use crate::peer::Peer;
use crate::peer::PyPeerMap;
use crate::peer::PyUser;

use super::PyClient;
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

    /// Resolves a username into the peer that owns it, if any.
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
