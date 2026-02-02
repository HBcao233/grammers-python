// Copyright 2020 - developers of the `grammers` project.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

use pyo3::prelude::*;
use pyo3::types::PyDict;

use std::fmt;

use grammers_session_pyo3::{PyChannelKind, PyPeerAuth, PyPeerId, PyPeerInfo, PyPeerRef};
use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

use crate::PyClient;

/// A broadcast channel.
///
/// In a broadcast channel, only administrators can broadcast messages to all the subscribers.
/// The rest of users can only join and see messages.
///
/// Broadcast channels and megagroups both are treated as "channels" by Telegram's API, but
/// this variant will always represent a broadcast channel. The only difference between a
/// broadcast channel and a megagroup are the permissions (default, and available).
#[derive(Clone)]
#[pyclass(name = "Channel", module = "grammers.client", extends = pytl::TLObject)]
pub struct PyChannel {
    pub raw: tl::types::Channel,
    pub(crate) client: PyClient,
}

impl fmt::Debug for PyChannel {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        self.raw.fmt(f)
    }
}

impl PyChannel {
    pub fn from_raw(client: &PyClient, chat: tl::enums::Chat) -> Self {
        use tl::enums::Chat as C;

        match chat {
            C::Empty(_) | C::Chat(_) | C::Forbidden(_) => panic!("cannot create from group chat"),
            C::Channel(channel) => {
                if channel.broadcast {
                    Self {
                        raw: channel,
                        client: client.clone(),
                    }
                } else {
                    panic!("tried to create broadcast channel from megagroup");
                }
            }
            C::ChannelForbidden(channel) => {
                if channel.broadcast {
                    // TODO store until_date
                    Self {
                        raw: tl::types::Channel {
                            creator: false,
                            left: false,
                            broadcast: channel.broadcast,
                            verified: false,
                            megagroup: channel.megagroup,
                            restricted: false,
                            signatures: false,
                            min: false,
                            scam: false,
                            has_link: false,
                            has_geo: false,
                            slowmode_enabled: false,
                            call_active: false,
                            call_not_empty: false,
                            fake: false,
                            gigagroup: false,
                            noforwards: false,
                            join_request: false,
                            forum: false,
                            stories_hidden: false,
                            stories_hidden_min: false,
                            stories_unavailable: true,
                            signature_profiles: false,
                            autotranslation: false,
                            broadcast_messages_allowed: false,
                            monoforum: false,
                            join_to_send: false,
                            id: channel.id,
                            access_hash: Some(channel.access_hash),
                            title: channel.title,
                            username: None,
                            photo: tl::enums::ChatPhoto::Empty,
                            date: 0,
                            restriction_reason: None,
                            admin_rights: None,
                            banned_rights: None,
                            default_banned_rights: None,
                            participants_count: None,
                            usernames: None,
                            stories_max_id: None,
                            color: None,
                            profile_color: None,
                            emoji_status: None,
                            level: None,
                            subscription_until_date: None,
                            bot_verification_icon: None,
                            send_paid_messages_stars: None,
                            forum_tabs: false,
                            linked_monoforum_id: None,
                        },
                        client: client.clone(),
                    }
                } else {
                    panic!("tried to create broadcast channel from megagroup");
                }
            }
        }
    }
    
    /// Non-min auth stored in the channel, if any.
    pub(crate) fn auth(&self) -> Option<PyPeerAuth> {
        self.raw
            .access_hash
            .filter(|_| !self.raw.min)
            .map(PyPeerAuth::new)
    }
}

#[pymethods]
impl PyChannel {
    #[new]
    pub fn new(client: &PyClient, chat: pytl::enums::PyChat) -> (Self, pytl::TLObject) {
        (PyChannel::from_raw(client, chat.into()), pytl::TLObject {})
    }
    
    fn to_bytes(&self) -> Vec<u8> {
        let raw: pytl::types::PyChannel = self.raw.clone().into();
        raw.py_to_bytes()
    }
    
    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        let raw: pytl::types::PyChannel = self.raw.clone().into();
        raw.into_dict()
    }

    /// Return the unique identifier for this channel.
    #[getter]
    pub fn id(&self) -> PyPeerId {
        PyPeerId::channel(self.raw.id).unwrap()
    }

    /// Convert the channel to its reference.
    ///
    /// This is only possible if the peer would be usable on all methods or if it is in the session cache.
    pub async fn to_ref(&self) -> PyResult<Option<PyPeerRef>> {
        let id = self.id();
        let session = self.client.inner.lock().unwrap().session.clone();
        Ok(match self.auth() {
            Some(auth) => Some(PyPeerRef { id, auth }),
            None => session.peer_ref(id).await?,
        })
    }

    /// Additional information about this channel.
    #[getter]
    pub fn kind(&self) -> Option<PyChannelKind> {
        match <PyChannelKind as TryFrom<&PyChannel>>::try_from(self) {
            Ok(channel_kind) => Some(channel_kind),
            Err(()) => None,
        }
    }

    /// Return the title of this channel.
    #[getter]
    pub fn title(&self) -> String {
        self.raw.title.clone()
    }

    /// Return the public @username of this channel, if any.
    ///
    /// The returned username does not contain the "@" prefix.
    ///
    /// Outside of the application, people may link to this user with one of Telegram's URLs, such
    /// as https://t.me/username.
    #[getter]
    pub fn username(&self) -> Option<String> {
        self.raw.username.clone()
    }

    /// Return collectible usernames of this channel, if any.
    ///
    /// The returned usernames do not contain the "@" prefix.
    ///
    /// Outside of the application, people may link to this user with one of its username, such
    /// as https://t.me/username.
    #[getter]
    pub fn usernames(&self) -> Vec<String> {
        self.raw
            .usernames
            .as_deref()
            .map_or(Vec::new(), |usernames| {
                usernames
                    .iter()
                    .map(|username| match username {
                        tl::enums::Username::Username(username) => username.username.clone(),
                    })
                    .collect()
            })
    }

    /// Return the photo of this channel, if any.
    #[getter]
    pub fn photo(&self) -> Option<Py<pytl::types::PyChatPhoto>> {
        match &self.raw.photo {
            tl::enums::ChatPhoto::Empty => None,
            tl::enums::ChatPhoto::Photo(photo) => {
                let x: pytl::types::PyChatPhoto = photo.clone().into();
                let x: pytl::types::PyChatPhotoWrapper = x.into();
                Some(x.0)
            },
        }
    }

    /// Return the permissions of the logged-in user in this channel.
    #[getter]
    pub fn admin_rights(&self) -> Option<Py<pytl::types::PyChatAdminRights>> {
        match &self.raw.admin_rights {
            Some(tl::enums::ChatAdminRights::Rights(rights)) => Some(rights.clone().into()),
            None if self.raw.creator => Some(pytl::types::PyChatAdminRights {
                add_admins: true,
                other: true,
                change_info: true,
                post_messages: true,
                anonymous: false,
                ban_users: true,
                delete_messages: true,
                edit_messages: true,
                invite_users: true,
                manage_call: true,
                pin_messages: true,
                manage_topics: true,
                post_stories: true,
                edit_stories: true,
                delete_stories: true,
                manage_direct_messages: true,
            }),
            None => None,
        }.map(|x| Into::<pytl::types::PyChatAdminRightsWrapper>::into(x).0)
    }
}

impl PyChannel {
    pub fn info(&self) -> PyPeerInfo {
        self.raw.clone().into()
    }
}

impl TryFrom<PyChannel> for PyChannelKind {
    type Error = <Self as TryFrom<&'static PyChannel>>::Error;

    #[inline]
    fn try_from(channel: PyChannel) -> Result<Self, Self::Error> {
        <Self as TryFrom<&PyChannel>>::try_from(&channel)
    }
}
impl<'a> TryFrom<&'a PyChannel> for PyChannelKind {
    type Error = <Self as TryFrom<&'a tl::types::Channel>>::Error;

    #[inline]
    fn try_from(channel: &'a PyChannel) -> Result<Self, Self::Error> {
        <Self as TryFrom<&'a tl::types::Channel>>::try_from(&channel.raw)
    }
}
