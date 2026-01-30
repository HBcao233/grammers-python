use pyo3::exceptions::PyIndexError;
use pyo3::prelude::*;

use std::collections::HashMap;
use std::sync::Arc;

use crate::peer::Peer;
use crate::peer::PeerMap;

use super::PyClient;
use crate::errors::PyInvocationError;
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
    /// ```
    /// await client.get_me()
    /// ```
    pub async fn get_me(&self) -> PyResult<pytl::enums::PyUser> {
        let mut res = self
            .invoke_tl(&tl::functions::users::GetUsers {
                id: vec![tl::enums::InputUser::UserSelf],
            })
            .await
            .map_err(PyInvocationError::new)?;

        match res.pop() {
            Some(x) => Ok(x.into()),
            None => Err(PyIndexError::new_err("list index out of range")),
        }
    }
}

impl PyClient {
    pub async fn build_peer_map(
        &self,
        users: Vec<tl::enums::User>,
        chats: Vec<tl::enums::Chat>,
    ) -> PyResult<PeerMap> {
        let session = self.inner.lock().unwrap().session.clone();
        let map = users
            .into_iter()
            .map(|user| Peer::from_user(self, user))
            .chain(chats.into_iter().map(|chat| Peer::from_raw(self, chat)))
            .map(|peer| (peer.id(), peer))
            .collect::<HashMap<_, _>>();

        for peer in map.values() {
            if peer.auth().is_some() {
                session.cache_peer(peer.into()).await?;
            }
        }

        Ok(PeerMap {
            map: Arc::new(map),
            client: self.clone(),
        })
    }
}
