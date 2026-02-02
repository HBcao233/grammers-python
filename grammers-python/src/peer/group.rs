// Copyright 2020 - developers of the `grammers` project.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

use pyo3::exceptions::PyTypeError;
use pyo3::prelude::*;
use pyo3::types::{PyDateTime, PyDict};

use grammers_session_pyo3::{PeerInfoLike, PyChannelKind, PyPeerAuth, PyPeerId, PyPeerRef};
use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

use super::{PyRestrictionReason, PyRestrictionReasonWrapper};
use crate::PyClient;
use crate::utils::PyDateTimeWrapper;

#[derive(Clone)]
#[pyclass]
pub enum GroupRawType {
    ChatEmpty,
    Chat,
    ChatForbidden,
    Channel,
    ChannelForbidden,
}
#[pymethods]
impl GroupRawType {
    fn __repr__(&self) -> String {
        match self {
            Self::ChatEmpty => "GroupRawType.ChatEmpty",
            Self::Chat => "GroupRawType.Chat",
            Self::ChatForbidden => "GroupRawType.ChatForbidden",
            Self::Channel => "GroupRawType.Channel",
            Self::ChannelForbidden => "GroupRawType.ChannelForbidden",
        }
        .to_string()
    }
}

/// A group chat.
///
/// Telegram's API internally distinguishes between "small group chats" and "megagroups", also
/// known as "supergroups" in the UI of Telegram applications.
///
/// Small group chats are the default, and offer less features than megagroups, but you can
/// join more of them. Certain actions in official clients, like setting a chat's username,
/// silently upgrade the chat to a megagroup.
#[derive(Clone)]
#[pyclass(name = "Group", module = "grammers.client", extends = pytl::TLObject, dict)]
pub struct PyGroup {
    #[pyo3(get)]
    pub raw_type: GroupRawType,
    pub(crate) client: PyClient,

    /// Return the unique identifier for this group.
    ///
    /// Note that if this group is migrated to a megagroup, both this group and the new one will
    /// exist as separate chats, with different identifiers.
    #[pyo3(get)]
    id: PyPeerId,

    /// Return the title of this group.
    ///
    /// The title may be the empty string if the group is not accessible.
    #[pyo3(get, set)]
    pub title: Option<String>,

    /// Date when the user joined the supergroup/channel, or if the user isn't a member, its creation date
    #[pyo3(get)]
    pub date: Option<PyDateTimeWrapper>,
    #[pyo3(get)]
    pub date_timestamp: Option<i32>,

    #[pyo3(get, set)]
    pub access_hash: Option<PyPeerAuth>,

    /// Is this a channel, always false.
    #[pyo3(get, set)]
    pub broadcast: Option<bool>,

    /// Whether this is a supergroup, always true.
    #[pyo3(get, set)]
    pub megagroup: Option<bool>,

    /// The ban is valid until the specified date.
    #[pyo3(get)]
    pub until_date: Option<PyDateTimeWrapper>,
    #[pyo3(get)]
    pub until_date_timestamp: Option<i32>,

    /// Whether the current user is the creator of this channel.
    #[pyo3(get, set)]
    pub creator: Option<bool>,

    /// Whether the current user has left or is not a member of this channel.
    #[pyo3(get, set)]
    pub left: Option<bool>,

    #[pyo3(get, set)]
    pub deactivated: Option<bool>,

    #[pyo3(get, set)]
    pub call_active: Option<bool>,

    #[pyo3(get, set)]
    pub call_not_empty: Option<bool>,

    /// Whether this channel or group is protected, thus does not allow forwarding messages from it.
    #[pyo3(get, set)]
    pub noforwards: Option<bool>,

    // Return photo of this group, if any.
    #[pyo3(get, set)]
    pub photo: Option<pytl::enums::PyChatPhoto>,

    #[pyo3(get, set)]
    pub participants_count: Option<i32>,

    #[pyo3(get, set)]
    pub version: Option<i32>,

    #[pyo3(get, set)]
    pub migrated_to: Option<pytl::enums::PyInputChannel>,

    /// Return the permissions of the logged-in user in this channel.
    #[pyo3(get, set)]
    pub admin_rights: Option<pytl::enums::PyChatAdminRights>,

    #[pyo3(get, set)]
    pub default_banned_rights: Option<pytl::enums::PyChatBannedRights>,

    /// Whether this channel is verified by telegram.
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
    pub fake: Option<bool>,

    /// Whether this supergroup is a gigagroup.
    #[pyo3(get, set)]
    pub gigagroup: Option<bool>,

    /// Whether a user needs to join the supergroup before they can send messages:
    /// can be false only for discussion groups.
    /// toggle using `channels.toggleJoinToSend`
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

    /// Return the public @username of this group, if any.
    ///
    /// The returned username does not contain the "@" prefix.
    ///
    /// Outside of the application, people may link to this user with one of Telegram's URLs, such
    /// as https://t.me/username.
    #[pyo3(get, set)]
    pub username: Option<String>,

    #[pyo3(get, set)]
    pub restriction_reason: Vec<PyRestrictionReasonWrapper>,

    #[pyo3(get, set)]
    pub banned_rights: Option<pytl::enums::PyChatBannedRights>,

    /// Return collectible usernames of this group, if any.
    ///
    /// The returned usernames do not contain the "@" prefix.
    ///
    /// Outside of the application, people may link to this user with one of its username, such
    /// as https://t.me/username.
    #[pyo3(get, set)]
    pub usernames: Vec<pytl::enums::PyUsername>,

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

    /// Expiration date of the Telegram Star subscription
    /// the current user has bought to gain access to this channel.
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

// use to Default::default() eliminate so much None
#[derive(Default)]
struct GroupData {
    pub title: Option<String>,
    pub date: Option<PyDateTimeWrapper>,
    pub date_timestamp: Option<i32>,
    pub access_hash: Option<PyPeerAuth>,
    pub broadcast: Option<bool>,
    pub megagroup: Option<bool>,
    pub until_date: Option<PyDateTimeWrapper>,
    pub until_date_timestamp: Option<i32>,
    pub username: Option<String>,
    pub usernames: Vec<pytl::enums::PyUsername>,
    pub photo: Option<pytl::enums::PyChatPhoto>,

    pub creator: Option<bool>,
    pub left: Option<bool>,
    pub deactivated: Option<bool>,
    pub call_active: Option<bool>,
    pub call_not_empty: Option<bool>,
    pub noforwards: Option<bool>,
    pub participants_count: Option<i32>,
    pub version: Option<i32>,
    pub migrated_to: Option<pytl::enums::PyInputChannel>,
    pub admin_rights: Option<pytl::enums::PyChatAdminRights>,
    pub default_banned_rights: Option<pytl::enums::PyChatBannedRights>,
    pub verified: Option<bool>,
    pub restricted: Option<bool>,
    pub signatures: Option<bool>,
    pub min: Option<bool>,
    pub scam: Option<bool>,
    pub has_link: Option<bool>,
    pub has_geo: Option<bool>,
    pub slowmode_enabled: Option<bool>,
    pub fake: Option<bool>,
    pub gigagroup: Option<bool>,
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
    pub banned_rights: Option<pytl::enums::PyChatBannedRights>,
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

// TODO it might be desirable to manually merge all the properties of the chat to avoid endless matching

impl PyGroup {
    pub fn from_raw(
        client: &PyClient,
        chat: tl::enums::Chat,
    ) -> PyResult<PyClassInitializer<Self>> {
        use tl::enums::Chat as C;

        let (id, raw_type, data) = match chat {
            C::Empty(x) => (
                PyPeerId::chat(x.id).unwrap(),
                GroupRawType::ChatEmpty,
                GroupData::default(),
            ),
            C::Chat(x) => (
                PyPeerId::chat(x.id).unwrap(),
                GroupRawType::Chat,
                GroupData {
                    creator: Some(x.creator),
                    left: Some(x.left),
                    deactivated: Some(x.deactivated),
                    call_active: Some(x.call_active),
                    call_not_empty: Some(x.call_not_empty),
                    noforwards: Some(x.noforwards),
                    title: Some(x.title),
                    photo: {
                        let x = x.photo.into();
                        match x {
                            pytl::enums::PyChatPhoto::Photo(_) => Some(x),
                            _ => None,
                        }
                    },
                    participants_count: Some(x.participants_count),
                    date: Some(Python::attach(|py| {
                        PyDateTime::from_timestamp(py, x.date as f64, None)
                            .map(|x| x.unbind().into())
                    })?),
                    date_timestamp: Some(x.date),
                    version: Some(x.version),
                    migrated_to: x.migrated_to.map(Into::into),
                    admin_rights: x.admin_rights.map(Into::into),
                    default_banned_rights: x.default_banned_rights.map(Into::into),
                    ..Default::default()
                },
            ),
            C::Forbidden(x) => (
                PyPeerId::chat(x.id).unwrap(),
                GroupRawType::ChatForbidden,
                GroupData {
                    title: Some(x.title),
                    ..Default::default()
                },
            ),
            C::Channel(x) if x.broadcast => {
                return Err(PyTypeError::new_err(
                    "tried to create group from broadcast channel",
                ));
            }
            C::ChannelForbidden(x) if x.broadcast => {
                return Err(PyTypeError::new_err(
                    "tried to create group from broadcast channel",
                ));
            }
            C::Channel(x) => (
                PyPeerId::channel(x.id).unwrap(),
                GroupRawType::Channel,
                GroupData {
                    creator: Some(x.creator),
                    left: Some(x.left),
                    broadcast: Some(false),
                    verified: Some(x.verified),
                    megagroup: Some(x.megagroup),
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
                    access_hash: x.access_hash.map(PyPeerAuth::new),
                    title: Some(x.title),
                    username: x.username,
                    photo: {
                        let x = x.photo.into();
                        match x {
                            pytl::enums::PyChatPhoto::Photo(_) => Some(x),
                            _ => None,
                        }
                    },
                    date: Some(Python::attach(|py| {
                        PyDateTime::from_timestamp(py, x.date as f64, None)
                            .map(|x| x.unbind().into())
                    })?),
                    date_timestamp: Some(x.date),
                    restriction_reason: x
                        .restriction_reason
                        .unwrap_or_default()
                        .into_iter()
                        .map(|x| PyRestrictionReason::from_raw(&x).into())
                        .collect(),
                    admin_rights: match x.admin_rights {
                        Some(x) => Some(x.into()),
                        None if x.creator => Some(
                            pytl::types::PyChatAdminRights {
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
                            }
                            .into(),
                        ),
                        None => None,
                    },
                    banned_rights: x.banned_rights.map(Into::into),
                    default_banned_rights: x.default_banned_rights.map(Into::into),
                    participants_count: x.participants_count,
                    usernames: x
                        .usernames
                        .unwrap_or(Vec::new())
                        .into_iter()
                        .map(Into::into)
                        .collect(),
                    stories_max_id: x.stories_max_id.map(Into::into),
                    color: x.color.map(Into::into),
                    profile_color: x.profile_color.map(Into::into),
                    emoji_status: x.emoji_status.map(Into::into),
                    level: x.level,
                    subscription_until_date: match x.subscription_until_date {
                        None => None,
                        Some(x) => Some(Python::attach(|py| {
                            PyDateTime::from_timestamp(py, x as f64, None)
                                .map(|x| x.unbind().into())
                        })?),
                    },
                    subscription_until_date_timestamp: x.subscription_until_date,
                    bot_verification_icon: x.bot_verification_icon,
                    send_paid_messages_stars: x.send_paid_messages_stars,
                    linked_monoforum_id: x.linked_monoforum_id,
                    ..Default::default()
                },
            ),
            C::ChannelForbidden(x) => (
                PyPeerId::channel(x.id).unwrap(),
                GroupRawType::ChannelForbidden,
                GroupData {
                    access_hash: Some(PyPeerAuth::new(x.access_hash)),
                    title: Some(x.title),
                    broadcast: Some(false),
                    megagroup: Some(x.megagroup),
                    until_date: match x.until_date {
                        None => None,
                        Some(x) => Some(Python::attach(|py| {
                            PyDateTime::from_timestamp(py, x as f64, None)
                                .map(|x| x.unbind().into())
                        })?),
                    },
                    until_date_timestamp: x.until_date,
                    ..Default::default()
                },
            ),
        };
        let GroupData {
            title,
            date,
            date_timestamp,
            access_hash,
            broadcast,
            megagroup,
            until_date,
            until_date_timestamp,
            creator,
            left,
            deactivated,
            call_active,
            call_not_empty,
            noforwards,
            photo,
            participants_count,
            version,
            migrated_to,
            admin_rights,
            default_banned_rights,
            verified,
            restricted,
            signatures,
            min,
            scam,
            has_link,
            has_geo,
            slowmode_enabled,
            fake,
            gigagroup,
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
            username,
            restriction_reason,
            banned_rights,
            usernames,
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
            raw_type,
            client: client.clone(),
            id,
            title,
            date,
            date_timestamp,
            access_hash,
            broadcast,
            megagroup,
            until_date,
            until_date_timestamp,
            creator,
            left,
            deactivated,
            call_active,
            call_not_empty,
            noforwards,
            photo,
            participants_count,
            version,
            migrated_to,
            admin_rights,
            default_banned_rights,
            verified,
            restricted,
            signatures,
            min,
            scam,
            has_link,
            has_geo,
            slowmode_enabled,
            fake,
            gigagroup,
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
            username,
            restriction_reason,
            banned_rights,
            usernames,
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

    pub fn info(&self) -> PeerInfoLike {
        match self.raw_type {
            GroupRawType::ChatEmpty | GroupRawType::Chat | GroupRawType::ChatForbidden => {
                PeerInfoLike::Chat {
                    id: self.id.bare_id().unwrap(),
                }
            }
            GroupRawType::Channel | GroupRawType::ChannelForbidden => PeerInfoLike::Channel {
                id: self.id.bare_id().unwrap(),
                auth: self.auth(),
                kind: self.kind(),
            },
        }
    }

    pub fn into_dict(self) -> PyResult<Py<PyDict>> {
        let PyGroup {
            id,
            title,
            date,
            access_hash,
            broadcast,
            megagroup,
            photo,
            until_date,
            username,
            usernames,
            creator,
            left,
            deactivated,
            call_active,
            call_not_empty,
            noforwards,
            participants_count,
            version,
            migrated_to,
            admin_rights,
            default_banned_rights,
            verified,
            restricted,
            signatures,
            min,
            scam,
            has_link,
            has_geo,
            slowmode_enabled,
            fake,
            gigagroup,
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
            banned_rights,
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
            dict.set_item("_", "Group")?;
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
            dict.set_item("deactivated", deactivated)?;
            dict.set_item("call_active", call_active)?;
            dict.set_item("call_not_empty", call_not_empty)?;
            dict.set_item("noforwards", noforwards)?;
            dict.set_item("participants_count", participants_count)?;
            dict.set_item("version", version)?;
            dict.set_item("migrated_to", migrated_to)?;
            dict.set_item("admin_rights", admin_rights)?;
            dict.set_item("default_banned_rights", default_banned_rights)?;
            dict.set_item("verified", verified)?;
            dict.set_item("restricted", restricted)?;
            dict.set_item("signatures", signatures)?;
            dict.set_item("min", min)?;
            dict.set_item("scam", scam)?;
            dict.set_item("has_link", has_link)?;
            dict.set_item("has_geo", has_geo)?;
            dict.set_item("slowmode_enabled", slowmode_enabled)?;
            dict.set_item("fake", fake)?;
            dict.set_item("gigagroup", gigagroup)?;
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
            dict.set_item("banned_rights", banned_rights)?;
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
impl PyGroup {
    #[new]
    fn new(client: &PyClient, chat: pytl::enums::PyChat) -> PyResult<PyClassInitializer<Self>> {
        Self::from_raw(client, chat.into())
    }

    fn to_bytes(&self) -> PyResult<Vec<u8>> {
        Err(PyTypeError::new_err(
            "grammers.client.Group can't to_bytes()",
        ))
    }

    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        self.clone().into_dict()
    }

    /// Non-min auth stored in the group, if any.
    #[getter]
    pub fn auth(&self) -> Option<PyPeerAuth> {
        self.access_hash.clone()
    }

    #[getter]
    pub fn kind(&self) -> Option<PyChannelKind> {
        if self.is_gigagroup() {
            Some(PyChannelKind::Gigagroup)
        } else if self.is_megagroup() {
            Some(PyChannelKind::Megagroup)
        } else {
            None
        }
    }

    /// Convert the group to its reference.
    ///
    /// This is only possible if the peer would be usable on all methods or if it is in the session cache.
    pub async fn to_ref(&self) -> PyResult<Option<PyPeerRef>> {
        let id = self.id();
        let session = self.client.session();
        Ok(match self.auth() {
            Some(auth) => Some(PyPeerRef { id, auth }),
            None => session.peer_ref(id).await?,
        })
    }

    /// Returns true if this group is a megagroup (also known as supergroups).
    ///
    /// In case inner type of group is Channel, that means it's a megagroup.
    #[getter]
    pub fn is_megagroup(&self) -> bool {
        matches!(self.megagroup, Some(true))
    }

    #[getter]
    fn is_broadcast(&self) -> bool {
        false
    }

    #[getter]
    fn is_gigagroup(&self) -> bool {
        matches!(self.gigagroup, Some(true))
    }
}
