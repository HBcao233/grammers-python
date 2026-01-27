// Copyright 2020 - developers of the `grammers` project.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

use pyo3::PyResult;

use std::collections::HashMap;
use std::sync::Arc;

use grammers_session_pyo3::{PyPeerId, PyPeerRef};

use crate::PyClient;
use crate::peer::Peer;
// use crate::peer::User;

/// Helper structure to efficiently retrieve peers via their peer.
///
/// A lot of responses include the peers related to them in the form of a list of users
/// and peers, making it annoying to extract a specific peer. This structure lets you
/// save those separate vectors in a single place and query them by using a `Peer`.
///
/// While this type derives `Clone` for convenience, it is recommended to use
/// [`PeerMap::handle`] instead to signal that it is a cheap clone.
#[derive(Clone)]
pub struct PeerMap {
    pub(crate) map: Arc<HashMap<PyPeerId, Peer>>,
    pub(crate) client: PyClient,
}

impl PeerMap {
    /// Retrieve the full `Peer` object given its `PeerId`.
    pub fn get(&self, peer: PyPeerId) -> Option<&Peer> {
        self.map.get(&peer)
    }

    /// Retrieve a non-min `PeerRef` from either the in-memory cache or the session.
    pub async fn get_ref(&self, peer: PyPeerId) -> PyResult<Option<PyPeerRef>> {
        let session = self.client.inner.lock().unwrap().session.clone();
        match self.map.get(&peer) {
            Some(peer) => peer.to_ref().await,
            None => session.peer_ref(peer).await,
        }
    }

    /// Take the full `Peer` object given its `PeerId`.
    ///
    /// The peer will be removed from the map if there are no other strong references to it.
    pub fn take(&mut self, peer: PyPeerId) -> Option<Peer> {
        match Arc::get_mut(&mut self.map) {
            Some(map) => map.remove(&peer),
            None => self.get(peer).cloned(),
        }
    }

    /*
    pub(crate) fn take_user(&mut self, user_id: i64) -> Option<User> {
        let peer = PyPeerId::user(user_id).unwrap();
        self.take(peer).map(|peer| match peer {
            Peer::User(user) => user,
            _ => unreachable!(),
        })
    }
    */

    /// Iterate over the peers and peers in the map.
    pub fn iter(&self) -> impl Iterator<Item = (PyPeerId, &Peer)> {
        self.map.iter().map(|(k, v)| (*k, v))
    }

    /// Iterate over the peers in the map.
    pub fn iter_peers(&self) -> impl Iterator<Item = &Peer> {
        self.map.values()
    }

    /// Return a new strong reference to the map and session contained within.
    pub fn handle(&self) -> Self {
        Self {
            map: Arc::clone(&self.map),
            client: self.client.clone(),
        }
    }
}
