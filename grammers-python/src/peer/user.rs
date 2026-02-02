// Copyright 2020 - developers of the `grammers` project.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

use pyo3::prelude::*;

use grammers_session_pyo3::{PyPeerId, PyPeerAuth, PeerInfoLike};
use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

use crate::PyClient;

/// Platform Identifier referenced only by [`RestrictionReason`].
#[non_exhaustive]
#[derive(Clone)]
#[pyclass(name = "Platform", module = "grammers.client")]
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
#[pyclass(name = "RestrictionReason", module = "grammers.client")]
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
        let platforms = "[".to_owned() + &self.platforms
            .iter()
            .map(|x| "        \n".to_owned() + &x.__repr__())
            .collect::<Vec<String>>()
            .join(",") + "\n    ]";

        format!(
            "RestrictionReason(\n    platforms={},\n    reason={},    text={},\n)",
            platforms,
            self.reason,
            self.text,
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
#[pyclass(name = "User", module = "grammers.client", extends = pytl::types::PyUser)]
pub struct PyUser {
    id: PyPeerId,
    auth: Option<PyPeerAuth>,
    bot: Option<bool>,
    is_self: Option<bool>,
    restriction_reason: Vec<PyRestrictionReasonWrapper>,
    pub(crate) client: PyClient,
}

impl PyUser {
    pub fn from_raw(client: &PyClient, user: tl::enums::User) -> PyClassInitializer<Self> {
        let (user, id, auth, bot, is_self, restriction_reason) = match user {
            tl::enums::User::Empty(x) => (
                pytl::types::PyUser {
                    id: x.id,
                    is_self: false,
                    contact: false,
                    mutual_contact: false,
                    deleted: false,
                    bot: false,
                    bot_chat_history: false,
                    bot_nochats: false,
                    verified: false,
                    restricted: false,
                    min: false,
                    bot_inline_geo: false,
                    support: false,
                    scam: false,
                    apply_min_photo: false,
                    fake: false,
                    bot_attach_menu: false,
                    premium: false,
                    attach_menu_enabled: false,
                    bot_can_edit: false,
                    close_friend: false,
                    stories_hidden: false,
                    stories_unavailable: false,
                    contact_require_premium: false,
                    bot_business: false,
                    bot_has_main_app: false,
                    bot_forum_view: false,
                    access_hash: None,
                    first_name: None,
                    last_name: None,
                    username: None,
                    phone: None,
                    photo: None,
                    status: None,
                    bot_info_version: None,
                    restriction_reason: None,
                    bot_inline_placeholder: None,
                    lang_code: None,
                    emoji_status: None,
                    usernames: None,
                    stories_max_id: None,
                    color: None,
                    profile_color: None,
                    bot_active_users: None,
                    bot_verification_icon: None,
                    send_paid_messages_stars: None,
                },
                PyPeerId::user(x.id).unwrap(),
                Some(PyPeerAuth::default()),
                None,
                None,
                Vec::new()
            ),
            tl::enums::User::User(x) => (
                x.clone().into(),
                PyPeerId::user(x.id).unwrap(),
                x.access_hash.map(PyPeerAuth::new),
                Some(x.bot),
                Some(x.is_self),
                x.restriction_reason
                    .map_or(Vec::new(), |x| 
                        x.into_iter()
                        .map(|x| PyRestrictionReason::from_raw(&x).into())
                        .collect()
                    )
            ),
        };
        PyClassInitializer::from(pytl::TLObject {})
            .add_subclass(user)
            .add_subclass(Self {
                id,
                auth,
                bot,
                is_self,
                restriction_reason,
                client: client.clone(),
            })
    }
    
    pub fn id(&self) -> PyPeerId {
        self.id
    }

    pub fn auth(&self) -> Option<PyPeerAuth> {
        self.auth
    }

    pub fn info(&self) -> PeerInfoLike {
        PeerInfoLike::User {
            id: self.id.bare_id().unwrap(),
            auth: self.auth,
            bot: self.bot,
            is_self: self.is_self,
        }
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
    
    #[getter]
    fn restriction_reason(&self) -> Vec<PyRestrictionReasonWrapper> {
        self.restriction_reason.clone()
    }
}
