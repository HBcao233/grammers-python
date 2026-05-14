// Copyright 2020 - developers of the `grammers` project.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

//! Types relating to users, groups and channels.
//!
//! Properties containing raw types are public and will either be called "raw" or prefixed with "raw_".\
//! Keep in mind that **these fields are not part of the semantic versioning guarantees**.

// mod action;
// pub(crate) mod chats;
// mod dialog;
// mod participant;
// pub use action::ActionSender;
mod channel;
mod group;
mod peer;
mod peer_map;
// mod permissions;
mod user;

pub use channel::PyChannel;
// pub use chats::{AdminRightsBuilder, BannedRightsBuilder};
// pub use dialog::Dialog;
pub use group::{PyGroup, GroupRawType};
// pub use participant::{Participant, Role};
pub use peer::PyPeer;
pub use peer_map::PyPeerMap;
// pub use permissions::{Permissions, Restrictions};
pub use user::{PyPlatform, PyRestrictionReason, PyRestrictionReasonWrapper, PyUser};


use pyo3::Python;
use crate::PyClient;
use grammers_session_pyo3::{PyPeerId, PyPeerKind};
use grammers_tl_types as tl;

pub fn convertPeerId2Peer(peer: PyPeerId, client: PyClient) -> tl::enums::Peer {
    match peer.kind() {
        PyPeerKind::User => tl::types::PeerUser {
            user_id: peer.bare_id().unwrap()
        }.into(),
        PyPeerKind::UserSelf => tl::types::PeerUser {
            user_id: Python::attach(|py| 
                client._me().expect("me cache should set").borrow(py).id().bare_id().unwrap()
            )
        }.into(),
        PyPeerKind::Chat => tl::types::PeerChat {
            chat_id: peer.bare_id().unwrap()
        }.into(),
        PyPeerKind::Channel => tl::types::PeerChannel {
            channel_id: peer.bare_id().unwrap()
        }.into(),
    }
}