// Copyright 2020 - developers of the `grammers` project.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

use pyo3::prelude::*;
use pyo3::types::{PyDict, PyDateTime};
use pyo3::exceptions::PyTypeError;

use grammers_session_pyo3::{PyChannelKind, PyPeerAuth, PyPeerId, PeerInfoLike, PyPeerRef};
use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

use super::{PyRestrictionReason, PyRestrictionReasonWrapper};
use crate::PyClient;
use crate::utils::PyDateTimeWrapper;

// use to Default::default() eliminate so much None
#[derive(Default)]
struct ChannelData {
    pub title: String,
    pub access_hash: Option<PyPeerAuth>,
    pub username: Option<String>,
    pub usernames: Vec<String>,
    pub photo: Option<pytl::enums::PyChatPhoto>,
    pub date: Option<PyDateTimeWrapper>,
    pub date_timestamp: Option<i32>,
    pub broadcast: bool,
    pub megagroup: bool,
    pub until_date: Option<PyDateTimeWrapper>,
    pub until_date_timestamp: Option<i32>,

    pub creator: Option<bool>,
    pub left: Option<bool>,
    pub verified: Option<bool>,
    pub restricted: Option<bool>,
    pub signatures: Option<bool>,
    pub min: Option<bool>,
    pub scam: Option<bool>,
    pub has_link: Option<bool>,
    pub has_geo: Option<bool>,
    pub slowmode_enabled: Option<bool>,
    pub call_active: Option<bool>,
    pub call_not_empty: Option<bool>,
    pub fake: Option<bool>,
    pub gigagroup: Option<bool>,
    pub noforwards: Option<bool>,
    pub join_to_send: Option<bool>,
    pub join_request: Option<bool>,
    pub forum: Option<bool>,
    pub stories_hidden: Option<bool>,
    pub stories_hidden_min: Option<bool>,
    pub stories_unavailable: Option<bool>,
    pub signature_profiles: Option<bool>,
    pub autotranslation: Option<bool>,
    pub broadcast_messages_allowed: Option<bool>,
    pub monoforum: Option<bool>,
    pub forum_tabs: Option<bool>,
    pub restriction_reason: Vec<PyRestrictionReasonWrapper>,
    pub admin_rights: Option<pytl::enums::PyChatAdminRights>,
    pub banned_rights: Option<pytl::enums::PyChatBannedRights>,
    pub default_banned_rights: Option<pytl::enums::PyChatBannedRights>,
    pub participants_count: Option<i32>,
    pub stories_max_id: Option<pytl::enums::PyRecentStory>,
    pub color: Option<pytl::enums::PyPeerColor>,
    pub profile_color: Option<pytl::enums::PyPeerColor>,
    pub emoji_status: Option<pytl::enums::PyEmojiStatus>,
    pub level: Option<i32>,
    pub subscription_until_date: Option<PyDateTimeWrapper>,
    pub subscription_until_date_timestamp: Option<i32>,
    pub bot_verification_icon: Option<i64>,
    pub send_paid_messages_stars: Option<i64>,
    pub linked_monoforum_id: Option<i64>,
}

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
    pub(crate) client: PyClient,
    
    /// Return the unique identifier for this channel.
    #[pyo3(get)]
    pub id: PyPeerId,
    
    /// Return the title of this channel.
    #[pyo3(get, set)]
    pub title: String,
    
    #[pyo3(get, set)]
    pub access_hash: Option<PyPeerAuth>,
    
    /// Return the public @username of this channel, if any.
    ///
    /// The returned username does not contain the "@" prefix.
    ///
    /// Outside of the application, people may link to this user with one of Telegram's URLs, such
    /// as https://t.me/username.
    #[pyo3(get, set)]
    pub username: Option<String>,
    
    /// Return collectible usernames of this channel, if any.
    ///
    /// The returned usernames do not contain the "@" prefix.
    ///
    /// Outside of the application, people may link to this user with one of its username, such
    /// as https://t.me/username.
    #[pyo3(get, set)]
    pub usernames: Vec<String>,
    
    /// Return the photo of this channel, if any.
    #[pyo3(get, set)]
    pub photo: Option<pytl::enums::PyChatPhoto>,
    
    #[pyo3(get)]
    pub date: Option<PyDateTimeWrapper>,
    #[pyo3(get)]
    pub date_timestamp: Option<i32>,
    #[pyo3(get)]
    pub until_date: Option<PyDateTimeWrapper>,
    #[pyo3(get)]
    pub until_date_timestamp: Option<i32>,
    
    #[pyo3(get, set)]
    pub broadcast: bool,
    #[pyo3(get, set)]
    pub megagroup: bool,
    
    #[pyo3(get, set)]
    pub creator: Option<bool>,
    #[pyo3(get, set)]
    pub left: Option<bool>,
    #[pyo3(get, set)]
    pub verified: Option<bool>,
    #[pyo3(get, set)]
    pub restricted: Option<bool>,
    #[pyo3(get, set)]
    pub signatures: Option<bool>,
    #[pyo3(get, set)]
    pub min: Option<bool>,
    #[pyo3(get, set)]
    pub scam: Option<bool>,
    #[pyo3(get, set)]
    pub has_link: Option<bool>,
    #[pyo3(get, set)]
    pub has_geo: Option<bool>,
    #[pyo3(get, set)]
    pub slowmode_enabled: Option<bool>,
    #[pyo3(get, set)]
    pub call_active: Option<bool>,
    #[pyo3(get, set)]
    pub call_not_empty: Option<bool>,
    #[pyo3(get, set)]
    pub fake: Option<bool>,
    #[pyo3(get, set)]
    pub gigagroup: Option<bool>,
    #[pyo3(get, set)]
    pub noforwards: Option<bool>,
    #[pyo3(get, set)]
    pub join_to_send: Option<bool>,
    #[pyo3(get, set)]
    pub join_request: Option<bool>,
    #[pyo3(get, set)]
    pub forum: Option<bool>,
    #[pyo3(get, set)]
    pub stories_hidden: Option<bool>,
    #[pyo3(get, set)]
    pub stories_hidden_min: Option<bool>,
    #[pyo3(get, set)]
    pub stories_unavailable: Option<bool>,
    #[pyo3(get, set)]
    pub signature_profiles: Option<bool>,
    #[pyo3(get, set)]
    pub autotranslation: Option<bool>,
    #[pyo3(get, set)]
    pub broadcast_messages_allowed: Option<bool>,
    #[pyo3(get, set)]
    pub monoforum: Option<bool>,
    #[pyo3(get, set)]
    pub forum_tabs: Option<bool>,
    #[pyo3(get, set)]
    pub restriction_reason: Vec<PyRestrictionReasonWrapper>,
    #[pyo3(get, set)]
    pub admin_rights: Option<pytl::enums::PyChatAdminRights>,
    #[pyo3(get, set)]
    pub banned_rights: Option<pytl::enums::PyChatBannedRights>,
    #[pyo3(get, set)]
    pub default_banned_rights: Option<pytl::enums::PyChatBannedRights>,
    #[pyo3(get, set)]
    pub participants_count: Option<i32>,
    #[pyo3(get, set)]
    pub stories_max_id: Option<pytl::enums::PyRecentStory>,
    #[pyo3(get, set)]
    pub color: Option<pytl::enums::PyPeerColor>,
    #[pyo3(get, set)]
    pub profile_color: Option<pytl::enums::PyPeerColor>,
    #[pyo3(get, set)]
    pub emoji_status: Option<pytl::enums::PyEmojiStatus>,
    #[pyo3(get, set)]
    pub level: Option<i32>,
    #[pyo3(get)]
    pub subscription_until_date: Option<PyDateTimeWrapper>,
    #[pyo3(get)]
    pub subscription_until_date_timestamp: Option<i32>,
    #[pyo3(get, set)]
    pub bot_verification_icon: Option<i64>,
    #[pyo3(get, set)]
    pub send_paid_messages_stars: Option<i64>,
    #[pyo3(get, set)]
    pub linked_monoforum_id: Option<i64>,
}

impl PyChannel {
    pub fn from_raw(client: &PyClient, chat: tl::enums::Chat) -> PyResult<PyClassInitializer<Self>> {
        use tl::enums::Chat as C;

        let (id, data) = match chat {
            C::Empty(_) | C::Chat(_) | C::Forbidden(_) => return Err(PyTypeError::new_err(
                "cannot create from group chat"
            )),
            C::Channel(x) if !x.broadcast => return Err(PyTypeError::new_err(
                "tried to create broadcast channel from megagroup"
            )),
            C::ChannelForbidden(x) if !x.broadcast => return Err(PyTypeError::new_err(
                "tried to create broadcast channel from megagroup"
            )),
            C::Channel(x) => (
                PyPeerId::channel(x.id).unwrap(),
                ChannelData {
                    creator: Some(x.creator),
                    left: Some(x.left),
                    broadcast: false,
                    verified: Some(x.verified),
                    megagroup: x.megagroup,
                    restricted: Some(x.restricted),
                    signatures: Some(x.signatures),
                    min: Some(x.min),
                    scam: Some(x.scam),
                    has_link: Some(x.has_link),
                    has_geo: Some(x.has_geo),
                    slowmode_enabled: Some(x.slowmode_enabled),
                    call_active: Some(x.call_active),
                    call_not_empty: Some(x.call_not_empty),
                    fake: Some(x.fake),
                    gigagroup: Some(x.gigagroup),
                    noforwards: Some(x.noforwards),
                    join_to_send: Some(x.join_to_send),
                    join_request: Some(x.join_request),
                    forum: Some(x.forum),
                    stories_hidden: Some(x.stories_hidden),
                    stories_hidden_min: Some(x.stories_hidden_min),
                    stories_unavailable: Some(x.stories_unavailable),
                    signature_profiles: Some(x.signature_profiles),
                    autotranslation: Some(x.autotranslation),
                    broadcast_messages_allowed: Some(x.broadcast_messages_allowed),
                    monoforum: Some(x.monoforum),
                    forum_tabs: Some(x.forum_tabs),
                    access_hash: if x.min {
                        None
                    } else {
                        x.access_hash.map(PyPeerAuth::new)
                    },
                    title: x.title,
                    username: x.username,
                    photo: {
                        let x = x.photo.into();
                        match x {
                            pytl::enums::PyChatPhoto::Photo(_) => Some(x),
                            _ => None
                        }
                    },
                    date: Some(Python::attach(|py|
                        PyDateTime::from_timestamp(py, x.date as f64, None)
                            .map(|x| x.unbind().into())
                    )?),
                    date_timestamp: Some(x.date),
                    restriction_reason: x.restriction_reason
                        .unwrap_or_default()
                        .into_iter()
                        .map(|x| PyRestrictionReason::from_raw(&x).into())
                        .collect(),
                    admin_rights: match x.admin_rights {
                        Some(y) => Some(y.into()),
                        None if x.creator => Some(pytl::types::PyChatAdminRights {
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
                        }.into()),
                        None => None,
                    },
                    banned_rights: x.banned_rights.map(Into::into),
                    default_banned_rights: x.default_banned_rights.map(Into::into),
                    participants_count: x.participants_count,
                    usernames: x.usernames.as_deref()
                        .map_or(Vec::new(), |usernames| {
                            usernames
                                .iter()
                                .map(|username| match username {
                                    tl::enums::Username::Username(username) => {
                                        username.username.clone()
                                    }
                                })
                                .collect()
                        }),
                    stories_max_id: x.stories_max_id.map(Into::into),
                    color: x.color.map(Into::into),
                    profile_color: x.profile_color.map(Into::into),
                    emoji_status: x.emoji_status.map(Into::into),
                    level: x.level,
                    subscription_until_date: match x.subscription_until_date {
                        None => None,
                        Some(x) => Some(Python::attach(|py|
                            PyDateTime::from_timestamp(py, x as f64, None)
                            .map(|x| x.unbind().into())
                        )?),
                    },
                    subscription_until_date_timestamp: x.subscription_until_date,
                    bot_verification_icon: x.bot_verification_icon,
                    send_paid_messages_stars: x.send_paid_messages_stars,
                    linked_monoforum_id: x.linked_monoforum_id,
                    ..Default::default()
                }
            ),
            C::ChannelForbidden(x) => (
                PyPeerId::channel(x.id).unwrap(),
                ChannelData {
                    access_hash: Some(PyPeerAuth::new(x.access_hash)),
                    title: x.title,
                    broadcast: false,
                    megagroup: x.megagroup,
                    until_date: match x.until_date {
                        None => None,
                        Some(x) => Some(Python::attach(|py|
                            PyDateTime::from_timestamp(py, x as f64, None)
                                .map(|x| x.unbind().into())
                        )?),
                    },
                    ..Default::default()
                } 
            ),
        };
        let ChannelData {
            title,
            access_hash,
            username,
            usernames,
            photo,
            date,
            date_timestamp,
            broadcast,
            megagroup,
            until_date,
            until_date_timestamp,
            creator,
            left,
            verified,
            restricted,
            signatures,
            min,
            scam,
            has_link,
            has_geo,
            slowmode_enabled,
            call_active,
            call_not_empty,
            fake,
            gigagroup,
            noforwards,
            join_to_send,
            join_request,
            forum,
            stories_hidden,
            stories_hidden_min,
            stories_unavailable,
            signature_profiles,
            autotranslation,
            broadcast_messages_allowed,
            monoforum,
            forum_tabs,
            restriction_reason,
            admin_rights,
            banned_rights,
            default_banned_rights,
            participants_count,
            stories_max_id,
            color,
            profile_color,
            emoji_status,
            level,
            subscription_until_date,
            subscription_until_date_timestamp,
            bot_verification_icon,
            send_paid_messages_stars,
            linked_monoforum_id,
        } = data;
        let base = PyClassInitializer::from(pytl::TLObject {});
        let sub = Self {
            client: client.clone(),
            id,
            title,
            access_hash,
            username,
            usernames,
            photo,
            date,
            date_timestamp,
            broadcast,
            megagroup,
            until_date,
            until_date_timestamp,
            creator,
            left,
            verified,
            restricted,
            signatures,
            min,
            scam,
            has_link,
            has_geo,
            slowmode_enabled,
            call_active,
            call_not_empty,
            fake,
            gigagroup,
            noforwards,
            join_to_send,
            join_request,
            forum,
            stories_hidden,
            stories_hidden_min,
            stories_unavailable,
            signature_profiles,
            autotranslation,
            broadcast_messages_allowed,
            monoforum,
            forum_tabs,
            restriction_reason,
            admin_rights,
            banned_rights,
            default_banned_rights,
            participants_count,
            stories_max_id,
            color,
            profile_color,
            emoji_status,
            level,
            subscription_until_date,
            subscription_until_date_timestamp,
            bot_verification_icon,
            send_paid_messages_stars,
            linked_monoforum_id,
        };
        Ok(base.add_subclass(sub))
    }
    
    pub fn id(&self) -> PyPeerId {
        self.id
    }
    
    /// Non-min auth stored in the channel, if any.
    pub fn auth(&self) -> Option<PyPeerAuth> {
        self.access_hash
    }
    
    pub fn info(&self) -> PeerInfoLike {
        PeerInfoLike::Channel {
            id: self.id.bare_id().unwrap(),
            auth: self.auth(),
            kind: self.kind(),
        }
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
    
    pub fn into_dict(self) -> PyResult<Py<PyDict>> {
        let PyChannel {
            id,
            title,
            access_hash,
            username,
            usernames,
            photo,
            date,
            broadcast,
            megagroup,
            until_date,
            creator,
            left,
            verified,
            restricted,
            signatures,
            min,
            scam,
            has_link,
            has_geo,
            slowmode_enabled,
            call_active,
            call_not_empty,
            fake,
            gigagroup,
            noforwards,
            join_to_send,
            join_request,
            forum,
            stories_hidden,
            stories_hidden_min,
            stories_unavailable,
            signature_profiles,
            autotranslation,
            broadcast_messages_allowed,
            monoforum,
            forum_tabs,
            restriction_reason,
            admin_rights,
            banned_rights,
            default_banned_rights,
            participants_count,
            stories_max_id,
            color,
            profile_color,
            emoji_status,
            level,
            subscription_until_date,
            bot_verification_icon,
            send_paid_messages_stars,
            linked_monoforum_id,
            ..
        } = self;
        Python::attach(|py| {
            let dict = PyDict::new(py);
            dict.set_item("_", "Channel")?;
            dict.set_item("id", id)?;
            dict.set_item("title", title)?;
            dict.set_item("access_hash", access_hash)?;
            dict.set_item("username", username)?;
            dict.set_item("usernames", usernames)?;
            dict.set_item("photo", photo)?;
            dict.set_item("date", date)?;
            dict.set_item("broadcast", broadcast)?;
            dict.set_item("megagroup", megagroup)?;
            dict.set_item("until_date", until_date)?;
            dict.set_item("creator", creator)?;
            dict.set_item("left", left)?;
            dict.set_item("verified", verified)?;
            dict.set_item("restricted", restricted)?;
            dict.set_item("signatures", signatures)?;
            dict.set_item("min", min)?;
            dict.set_item("scam", scam)?;
            dict.set_item("has_link", has_link)?;
            dict.set_item("has_geo", has_geo)?;
            dict.set_item("slowmode_enabled", slowmode_enabled)?;
            dict.set_item("call_active", call_active)?;
            dict.set_item("call_not_empty", call_not_empty)?;
            dict.set_item("fake", fake)?;
            dict.set_item("gigagroup", gigagroup)?;
            dict.set_item("noforwards", noforwards)?;
            dict.set_item("join_to_send", join_to_send)?;
            dict.set_item("join_request", join_request)?;
            dict.set_item("forum", forum)?;
            dict.set_item("stories_hidden", stories_hidden)?;
            dict.set_item("stories_hidden_min", stories_hidden_min)?;
            dict.set_item("stories_unavailable", stories_unavailable)?;
            dict.set_item("signature_profiles", signature_profiles)?;
            dict.set_item("autotranslation", autotranslation)?;
            dict.set_item("broadcast_messages_allowed", broadcast_messages_allowed)?;
            dict.set_item("monoforum", monoforum)?;
            dict.set_item("forum_tabs", forum_tabs)?;
            dict.set_item("restriction_reason", restriction_reason)?;
            dict.set_item("admin_rights", admin_rights)?;
            dict.set_item("banned_rights", banned_rights)?;
            dict.set_item("default_banned_rights", default_banned_rights)?;
            dict.set_item("participants_count", participants_count)?;
            dict.set_item("stories_max_id", stories_max_id)?;
            dict.set_item("color", color)?;
            dict.set_item("profile_color", profile_color)?;
            dict.set_item("emoji_status", emoji_status)?;
            dict.set_item("level", level)?;
            dict.set_item("subscription_until_date", subscription_until_date)?;
            dict.set_item("bot_verification_icon", bot_verification_icon)?;
            dict.set_item("send_paid_messages_stars", send_paid_messages_stars)?;
            dict.set_item("linked_monoforum_id", linked_monoforum_id)?;
            Ok(dict.unbind())
        })
    }
}

#[pymethods]
impl PyChannel {
    #[new]
    fn new(client: &PyClient, chat: pytl::enums::PyChat) -> PyResult<PyClassInitializer<Self>> {
        PyChannel::from_raw(client, chat.into())
    }
    
    fn to_bytes(&self) -> PyResult<Vec<u8>> {
        Err(PyTypeError::new_err("grammers.client.Group can't to_bytes()"))
    }
    
    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        self.clone().into_dict()
    }

    /// Additional information about this channel.
    #[getter]
    pub fn kind(&self) -> Option<PyChannelKind> {
        if self.is_gigagroup() {
            Some(PyChannelKind::Gigagroup)
        } else if self.is_megagroup() {
            Some(PyChannelKind::Megagroup)
        } else {
            Some(PyChannelKind::Broadcast)
        }
    }
    
    #[getter]
    pub fn is_megagroup(&self) -> bool {
        self.megagroup
    }
    
    #[getter]
    pub fn is_gigagroup(&self) -> bool {
        matches!(self.gigagroup, Some(true))
    }
}
