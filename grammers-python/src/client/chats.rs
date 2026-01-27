use pyo3::prelude::*;

use std::collections::HashMap;
use std::sync::Arc;

use crate::peer::Peer;
use crate::peer::PeerMap;
// use crate::peer::User;

use super::PyClient;
use grammers_tl_types as tl;

#[pymethods]
impl PyClient {
    /*fn get_me<'py>(
      &self,
    ) -> PyResult<Bound<'py, PyAny>> {

    }*/
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
