// Copyright 2020 - developers of the `grammers` project.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

use pyo3::exceptions::PyTypeError;
use pyo3::prelude::*;
use pyo3::types::PyDict;

use grammers_session_pyo3::{PeerInfo, PyPeerAuth, PyPeerId, PyPeerRef};
use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

use crate::PyClient;

/// Platform Identifier referenced only by [`RestrictionReason`].
#[non_exhaustive]
#[derive(Clone)]
#[pyclass(name = "Platform", module = "grammers.custom")]
pub enum PyPlatform {
    All(),
    Android(),
    Ios(),
    WindowsPhone(),
    Other(String),
}

#[pymethods]
impl PyPlatform {
    fn __repr__(&self) -> String {
        match self {
            Self::All() => "Platform.All".to_string(),
            Self::Android() => "Platform.Android".to_string(),
            Self::Ios() => "Platform.IOS".to_string(),
            Self::WindowsPhone() => "Platform.WindowsPhone".to_string(),
            Self::Other(x) => format!("Platform.Other('{}')", x),
        }
    }
}

/// Reason why a user is globally restricted.
#[derive(Clone)]
#[pyclass(name = "RestrictionReason", module = "grammers.custom")]
pub struct PyRestrictionReason {
    pub platforms: Vec<PyPlatform>,
    pub reason: String,
    pub text: String,
}

impl PyRestrictionReason {
    pub fn from_raw(reason: &tl::enums::RestrictionReason) -> Self {
        let tl::enums::RestrictionReason::Reason(reason) = reason;
        Self {
            platforms: reason
                .platform
                .split('-')
                .map(|p| match p {
                    // Taken from https://core.telegram.org/constructor/restrictionReason
                    "all" => PyPlatform::All(),
                    "android" => PyPlatform::Android(),
                    "ios" => PyPlatform::Ios(),
                    "wp" => PyPlatform::WindowsPhone(),
                    o => PyPlatform::Other(o.to_string()),
                })
                .collect(),
            reason: reason.reason.to_string(),
            text: reason.text.to_string(),
        }
    }
}

#[pymethods]
impl PyRestrictionReason {
    #[new]
    fn new(reason: pytl::enums::PyRestrictionReason) -> Self {
        Self::from_raw(&reason.into())
    }

    fn __repr__(&self) -> String {
        let platforms = "[".to_owned()
            + &self
                .platforms
                .iter()
                .map(|x| "        \n".to_owned() + &x.__repr__())
                .collect::<Vec<String>>()
                .join(",")
            + "\n    ]";

        format!(
            "RestrictionReason(\n    platforms={},\n    reason={},    text={},\n)",
            platforms, self.reason, self.text,
        )
    }
}

#[derive(IntoPyObject, FromPyObject)]
pub struct PyRestrictionReasonWrapper(pub Py<PyRestrictionReason>);
impl Clone for PyRestrictionReasonWrapper {
    fn clone(&self) -> Self {
        Python::attach(|py| Self(self.0.bind(py).clone().unbind()))
    }
}
impl From<PyRestrictionReason> for PyRestrictionReasonWrapper {
    fn from(x: PyRestrictionReason) -> Self {
        PyRestrictionReasonWrapper(Python::attach(|py| Py::new(py, x).expect("init")))
    }
}

// use to Default::default() eliminate so much None
#[derive(Default)]
struct UserData {
    pub access_hash: Option<PyPeerAuth>,
    pub bot: Option<bool>,
    pub is_self: Option<bool>,
    pub restriction_reason: Vec<PyRestrictionReasonWrapper>,
    pub contact: Option<bool>,
    pub mutual_contact: Option<bool>,
    pub deleted: Option<bool>,
    pub bot_chat_history: Option<bool>,
    pub bot_nochats: Option<bool>,
    pub verified: Option<bool>,
    pub restricted: Option<bool>,
    pub min: Option<bool>,
    pub bot_inline_geo: Option<bool>,
    pub support: Option<bool>,
    pub scam: Option<bool>,
    pub apply_min_photo: Option<bool>,
    pub fake: Option<bool>,
    pub bot_attach_menu: Option<bool>,
    pub premium: Option<bool>,
    pub attach_menu_enabled: Option<bool>,
    pub bot_can_edit: Option<bool>,
    pub close_friend: Option<bool>,
    pub stories_hidden: Option<bool>,
    pub stories_unavailable: Option<bool>,
    pub contact_require_premium: Option<bool>,
    pub bot_business: Option<bool>,
    pub bot_has_main_app: Option<bool>,
    pub bot_forum_view: Option<bool>,
    pub first_name: Option<String>,
    pub last_name: Option<String>,
    pub username: Option<String>,
    pub phone: Option<String>,
    pub photo: Option<pytl::enums::PyUserProfilePhoto>,
    pub status: Option<pytl::enums::PyUserStatus>,
    pub bot_info_version: Option<i32>,
    pub bot_inline_placeholder: Option<String>,
    pub lang_code: Option<String>,
    pub emoji_status: Option<pytl::enums::PyEmojiStatus>,
    pub usernames: Vec<pytl::enums::PyUsername>,
    pub stories_max_id: Option<pytl::enums::PyRecentStory>,
    pub color: Option<pytl::enums::PyPeerColor>,
    pub profile_color: Option<pytl::enums::PyPeerColor>,
    pub bot_active_users: Option<i32>,
    pub bot_verification_icon: Option<i64>,
    pub send_paid_messages_stars: Option<i64>,
}

/// A user.
///
/// Users include your contacts, members of a group, bot accounts created by [@BotFather], or
/// anyone with a Telegram account.
///
/// A "normal" (non-bot) user may also behave like a "bot" without actually being one, for
/// example, when controlled with a program as opposed to being controlled by a human through
/// a Telegram application. These are commonly known as "userbots", and some people use them
/// to enhance their Telegram experience (for example, creating "commands" so that the program
/// automatically reacts to them, like translating messages).
///
/// [@BotFather]: https://t.me/BotFather
#[derive(Clone)]
#[pyclass(name = "User", module = "grammers.custom", extends = pytl::TLObject)]
pub struct PyUser {
    #[pyo3(get)]
    pub(crate) client: PyClient,

    #[pyo3(get)]
    pub id: PyPeerId,
    #[pyo3(get, set)]
    pub access_hash: Option<PyPeerAuth>,
    #[pyo3(get, set)]
    pub bot: Option<bool>,
    #[pyo3(get, set)]
    pub is_self: Option<bool>,
    #[pyo3(get, set)]
    pub restriction_reason: Vec<PyRestrictionReasonWrapper>,

    #[pyo3(get, set)]
    pub contact: Option<bool>,
    #[pyo3(get, set)]
    pub mutual_contact: Option<bool>,
    #[pyo3(get, set)]
    pub deleted: Option<bool>,
    #[pyo3(get, set)]
    pub bot_chat_history: Option<bool>,
    #[pyo3(get, set)]
    pub bot_nochats: Option<bool>,
    #[pyo3(get, set)]
    pub verified: Option<bool>,
    #[pyo3(get, set)]
    pub restricted: Option<bool>,
    #[pyo3(get, set)]
    pub min: Option<bool>,
    #[pyo3(get, set)]
    pub bot_inline_geo: Option<bool>,
    #[pyo3(get, set)]
    pub support: Option<bool>,
    #[pyo3(get, set)]
    pub scam: Option<bool>,
    #[pyo3(get, set)]
    pub apply_min_photo: Option<bool>,
    #[pyo3(get, set)]
    pub fake: Option<bool>,
    #[pyo3(get, set)]
    pub bot_attach_menu: Option<bool>,
    #[pyo3(get, set)]
    pub premium: Option<bool>,
    #[pyo3(get, set)]
    pub attach_menu_enabled: Option<bool>,
    #[pyo3(get, set)]
    pub bot_can_edit: Option<bool>,
    #[pyo3(get, set)]
    pub close_friend: Option<bool>,
    #[pyo3(get, set)]
    pub stories_hidden: Option<bool>,
    #[pyo3(get, set)]
    pub stories_unavailable: Option<bool>,
    #[pyo3(get, set)]
    pub contact_require_premium: Option<bool>,
    #[pyo3(get, set)]
    pub bot_business: Option<bool>,
    #[pyo3(get, set)]
    pub bot_has_main_app: Option<bool>,
    #[pyo3(get, set)]
    pub bot_forum_view: Option<bool>,
    
    #[pyo3(get, set)]
    pub first_name: Option<String>,
    #[pyo3(get, set)]
    pub last_name: Option<String>,
    #[pyo3(get, set)]
    pub username: Option<String>,
    #[pyo3(get, set)]
    pub phone: Option<String>,
    #[pyo3(get, set)]
    pub photo: Option<pytl::enums::PyUserProfilePhoto>,
    #[pyo3(get, set)]
    pub status: Option<pytl::enums::PyUserStatus>,
    #[pyo3(get, set)]
    pub bot_info_version: Option<i32>,
    #[pyo3(get, set)]
    pub bot_inline_placeholder: Option<String>,
    #[pyo3(get, set)]
    pub lang_code: Option<String>,
    #[pyo3(get, set)]
    pub emoji_status: Option<pytl::enums::PyEmojiStatus>,
    #[pyo3(get, set)]
    pub usernames: Vec<pytl::enums::PyUsername>,
    #[pyo3(get, set)]
    pub stories_max_id: Option<pytl::enums::PyRecentStory>,
    #[pyo3(get, set)]
    pub color: Option<pytl::enums::PyPeerColor>,
    #[pyo3(get, set)]
    pub profile_color: Option<pytl::enums::PyPeerColor>,
    #[pyo3(get, set)]
    pub bot_active_users: Option<i32>,
    #[pyo3(get, set)]
    pub bot_verification_icon: Option<i64>,
    #[pyo3(get, set)]
    pub send_paid_messages_stars: Option<i64>,
}

impl PyUser {
    pub fn from_raw(client: &PyClient, user: tl::enums::User) -> PyClassInitializer<Self> {
        let (id, data) = match user {
            tl::enums::User::Empty(x) => (
                PyPeerId::user(x.id).unwrap(),
                UserData::default(),
            ),
            tl::enums::User::User(x) => (
                PyPeerId::user(x.id).unwrap(),
                UserData {
                    access_hash: x.access_hash.map(PyPeerAuth::new),
                    bot: Some(x.bot),
                    is_self: Some(x.is_self),
                    restriction_reason: x.restriction_reason.map_or(Vec::new(), |x| {
                        x.into_iter()
                            .map(|x| PyRestrictionReason::from_raw(&x).into())
                            .collect()
                    }),
                    contact: Some(x.contact),
                    mutual_contact: Some(x.mutual_contact),
                    deleted: Some(x.deleted),
                    bot_chat_history: Some(x.bot_chat_history),
                    bot_nochats: Some(x.bot_nochats),
                    verified: Some(x.verified),
                    restricted: Some(x.restricted),
                    min: Some(x.min),
                    bot_inline_geo: Some(x.bot_inline_geo),
                    support: Some(x.support),
                    scam: Some(x.scam),
                    apply_min_photo: Some(x.apply_min_photo),
                    fake: Some(x.fake),
                    bot_attach_menu: Some(x.bot_attach_menu),
                    premium: Some(x.premium),
                    attach_menu_enabled: Some(x.attach_menu_enabled),
                    bot_can_edit: Some(x.bot_can_edit),
                    close_friend: Some(x.close_friend),
                    stories_hidden: Some(x.stories_hidden),
                    stories_unavailable: Some(x.stories_unavailable),
                    contact_require_premium: Some(x.contact_require_premium),
                    bot_business: Some(x.bot_business),
                    bot_has_main_app: Some(x.bot_has_main_app),
                    bot_forum_view: Some(x.bot_forum_view),
                    first_name: x.first_name,
                    last_name: x.last_name,
                    username: x.username,
                    phone: x.phone,
                    photo: x.photo.map(Into::into),
                    status: x.status.map(Into::into),
                    bot_info_version: x.bot_info_version,
                    bot_inline_placeholder: x.bot_inline_placeholder,
                    lang_code: x.lang_code,
                    emoji_status: x.emoji_status.map(Into::into),
                    usernames: x.usernames
                        .unwrap_or(Vec::new())
                        .into_iter()
                        .map(Into::into)
                        .collect(),
                    stories_max_id: x.stories_max_id.map(Into::into),
                    color: x.color.map(Into::into),
                    profile_color: x.profile_color.map(Into::into),
                    bot_active_users: x.bot_active_users,
                    bot_verification_icon: x.bot_verification_icon,
                    send_paid_messages_stars: x.send_paid_messages_stars,
                }
            ),
        };
        let UserData {
            access_hash,
            bot,
            is_self,
            restriction_reason,
            contact,
            mutual_contact,
            deleted,
            bot_chat_history,
            bot_nochats,
            verified,
            restricted,
            min,
            bot_inline_geo,
            support,
            scam,
            apply_min_photo,
            fake,
            bot_attach_menu,
            premium,
            attach_menu_enabled,
            bot_can_edit,
            close_friend,
            stories_hidden,
            stories_unavailable,
            contact_require_premium,
            bot_business,
            bot_has_main_app,
            bot_forum_view,
            first_name,
            last_name,
            username,
            phone,
            photo,
            status,
            bot_info_version,
            bot_inline_placeholder,
            lang_code,
            emoji_status,
            usernames,
            stories_max_id,
            color,
            profile_color,
            bot_active_users,
            bot_verification_icon,
            send_paid_messages_stars,
        } = data;
        PyClassInitializer::from(pytl::TLObject {}).add_subclass(Self {
            client: client.clone(),
            id,
            access_hash,
            bot,
            is_self,
            restriction_reason,
            contact,
            mutual_contact,
            deleted,
            bot_chat_history,
            bot_nochats,
            verified,
            restricted,
            min,
            bot_inline_geo,
            support,
            scam,
            apply_min_photo,
            fake,
            bot_attach_menu,
            premium,
            attach_menu_enabled,
            bot_can_edit,
            close_friend,
            stories_hidden,
            stories_unavailable,
            contact_require_premium,
            bot_business,
            bot_has_main_app,
            bot_forum_view,
            first_name,
            last_name,
            username,
            phone,
            photo,
            status,
            bot_info_version,
            bot_inline_placeholder,
            lang_code,
            emoji_status,
            usernames,
            stories_max_id,
            color,
            profile_color,
            bot_active_users,
            bot_verification_icon,
            send_paid_messages_stars,
        })
    }

    pub fn id(&self) -> PyPeerId {
        self.id
    }

    pub fn auth(&self) -> Option<PyPeerAuth> {
        self.access_hash
    }

    pub fn info(&self) -> PeerInfo {
        PeerInfo::User {
            id: self.id.bare_id().unwrap(),
            auth: self.auth(),
            bot: self.bot,
            is_self: self.is_self,
        }
    }

    fn into_dict(self) -> PyResult<Py<PyDict>> {
        let PyUser {
            id,
            access_hash,
            bot,
            is_self,
            restriction_reason,
            contact,
            mutual_contact,
            deleted,
            bot_chat_history,
            bot_nochats,
            verified,
            restricted,
            min,
            bot_inline_geo,
            support,
            scam,
            apply_min_photo,
            fake,
            bot_attach_menu,
            premium,
            attach_menu_enabled,
            bot_can_edit,
            close_friend,
            stories_hidden,
            stories_unavailable,
            contact_require_premium,
            bot_business,
            bot_has_main_app,
            bot_forum_view,
            first_name,
            last_name,
            username,
            phone,
            photo,
            status,
            bot_info_version,
            bot_inline_placeholder,
            lang_code,
            emoji_status,
            usernames,
            stories_max_id,
            color,
            profile_color,
            bot_active_users,
            bot_verification_icon,
            send_paid_messages_stars,
            ..
        } = self;
        Python::attach(|py| {
            let dict = PyDict::new(py);
            dict.set_item("_", "User")?;
            dict.set_item("id", id)?;
            dict.set_item("access_hash", access_hash)?;
            dict.set_item("bot", bot)?;
            dict.set_item("is_self", is_self)?;
            dict.set_item("restriction_reason", restriction_reason)?;
            dict.set_item("first_name", first_name)?;
            dict.set_item("last_name", last_name)?;
            dict.set_item("username", username)?;
            dict.set_item("usernames", usernames)?;
            dict.set_item("contact", contact)?;
            dict.set_item("mutual_contact", mutual_contact)?;
            dict.set_item("deleted", deleted)?;
            dict.set_item("bot_chat_history", bot_chat_history)?;
            dict.set_item("bot_nochats", bot_nochats)?;
            dict.set_item("verified", verified)?;
            dict.set_item("restricted", restricted)?;
            dict.set_item("min", min)?;
            dict.set_item("bot_inline_geo", bot_inline_geo)?;
            dict.set_item("support", support)?;
            dict.set_item("scam", scam)?;
            dict.set_item("apply_min_photo", apply_min_photo)?;
            dict.set_item("fake", fake)?;
            dict.set_item("bot_attach_menu", bot_attach_menu)?;
            dict.set_item("premium", premium)?;
            dict.set_item("attach_menu_enabled", attach_menu_enabled)?;
            dict.set_item("bot_can_edit", bot_can_edit)?;
            dict.set_item("close_friend", close_friend)?;
            dict.set_item("stories_hidden", stories_hidden)?;
            dict.set_item("stories_unavailable", stories_unavailable)?;
            dict.set_item("contact_require_premium", contact_require_premium)?;
            dict.set_item("bot_business", bot_business)?;
            dict.set_item("bot_has_main_app", bot_has_main_app)?;
            dict.set_item("bot_forum_view", bot_forum_view)?;
            dict.set_item("phone", phone)?;
            dict.set_item("photo", photo)?;
            dict.set_item("status", status)?;
            dict.set_item("bot_info_version", bot_info_version)?;
            dict.set_item("bot_inline_placeholder", bot_inline_placeholder)?;
            dict.set_item("lang_code", lang_code)?;
            dict.set_item("emoji_status", emoji_status)?;
            dict.set_item("stories_max_id", stories_max_id)?;
            dict.set_item("color", color)?;
            dict.set_item("profile_color", profile_color)?;
            dict.set_item("bot_active_users", bot_active_users)?;
            dict.set_item("bot_verification_icon", bot_verification_icon)?;
            dict.set_item("send_paid_messages_stars", send_paid_messages_stars)?;
            Ok(dict.unbind())
        })
    }
}

// TODO: photo
#[pymethods]
impl PyUser {
    #[new]
    pub fn new(client: &PyClient, user: pytl::enums::PyUser) -> PyClassInitializer<Self> {
        let user: tl::enums::User = user.into();
        PyUser::from_raw(client, user)
    }

    fn to_bytes(&self) -> PyResult<Vec<u8>> {
        Err(PyTypeError::new_err(
            "grammers.client.Group can't to_bytes()",
        ))
    }

    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        self.clone().into_dict()
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
    
    #[getter]
    pub fn full_name(&self) -> String {
        match (self.first_name.clone(), self.last_name.clone()) {
            (Some(f), Some(l)) => format!("{} {}", f, l),
            (Some(f), None) => f,
            (None, Some(l)) => l,
            (None, None) => String::new(),
        }
    }
}
