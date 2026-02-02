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
pub use group::PyGroup;
// pub use participant::{Participant, Role};
pub use peer::Peer;
pub use peer_map::PyPeerMap;
// pub use permissions::{Permissions, Restrictions};
pub use user::{PyPlatform, PyRestrictionReason, PyRestrictionReasonWrapper, PyUser};
