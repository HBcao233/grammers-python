use pyo3::exceptions::{PyTypeError, PyValueError};
use pyo3::prelude::*;

use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

/// Sentinel value used to represent the self-user
/// when its true `PeerId` is unknown.
///
/// Per <https://core.telegram.org/api/bots/ids>:
/// > a bot API dialog ID ranges from -4000000000000 to 1099511627775
///
/// This value is not intended to be visible or persisted,
/// so it can be changed as needed in the future.
pub const SELF_USER_ID: i64 = 1 << 40;

/// Sentinel value used to represent empty chats.
///
/// Per <https://core.telegram.org/api/bots/ids>:
/// > \[…] transformed range for bot API chat dialog IDs is -999999999999 to -1 inclusively
/// >
/// > \[…] transformed range for bot API channel dialog IDs is -1997852516352 to -1000000000001 inclusively
///
/// `chat_id` parameters are in Telegram's API use the bare identifier,
/// so there's no empty constructor,
/// but it can be mimicked by picking the value in the correct range hole.
/// This value is closer to "channel with ID 0" than "chat with ID 0",
/// but there's no distinct `-0` integer,
/// and channels have a proper constructor for empty already.
// const EMPTY_CHAT_ID: i64 = -1000000000000;

#[repr(transparent)]
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[pyclass(name = "PeerId", module = "grammers.sessions")]
pub struct PyPeerId(pub i64);

#[pymethods]
impl PyPeerId {
    #[new]
    fn new(id: PeerIdLike) -> PyResult<Self> {
        let id = id.0;
        if (1 <= id && id <= 0xffffffffff)
            || id == SELF_USER_ID
            || (-999999999999 <= id && id <= -1)
            || (-1997852516352 <= id && id <= -1000000000001)
            || (-4000000000000 <= id && id <= -2002147483649)
        {
            Ok(Self(id))
        } else {
            Err(PyValueError::new_err("Invalid peer id"))
        }
    }

    /// Creates a peer identity for the currently-logged-in user or bot account.
    ///
    /// Internally, this will use a special sentinel value outside of any valid Bot API Dialog ID range.
    #[staticmethod]
    pub fn self_user() -> PyResult<Self> {
        Ok(Self(SELF_USER_ID))
    }

    /// Creates a peer identity for a user or bot account.
    #[staticmethod]
    pub fn user(id: i64) -> PyResult<Self> {
        if !(1 <= id && id <= 0xffffffffff) {
            Err(PyValueError::new_err("user ID out of range"))
        } else {
            Ok(Self(id))
        }
    }

    /// Creates a peer identity for a small group chat.
    #[staticmethod]
    pub fn chat(id: i64) -> PyResult<Self> {
        // https://core.telegram.org/api/bots/ids#chat-ids
        if !(1 <= id && id <= 999999999999) {
            Err(PyValueError::new_err("chat ID out of range"))
        } else {
            Ok(Self(-id))
        }
    }

    /// Creates a peer identity for a broadcast channel, megagroup, gigagroup or monoforum.
    #[staticmethod]
    pub fn channel(id: i64) -> PyResult<Self> {
        // https://core.telegram.org/api/bots/ids#supergroup-channel-ids and #monoforum-ids
        if !((1 <= id && id <= 997852516352) || (1002147483649 <= id && id <= 3000000000000)) {
            Err(PyValueError::new_err("channel ID out of range"))
        } else {
            Ok(Self(-(1000000000000 + id)))
        }
    }

    fn __repr__(&self) -> String {
        format!("PeerId({})", self.0)
    }

    /// Peer kind.
    #[getter]
    pub fn kind(&self) -> PyPeerKind {
        if 1 <= self.0 && self.0 <= 0xffffffffff {
            PyPeerKind::User
        } else if self.0 == SELF_USER_ID {
            PyPeerKind::UserSelf
        } else if -999999999999 <= self.0 && self.0 <= -1 {
            PyPeerKind::Chat
        } else if -1997852516352 <= self.0 && self.0 <= -1000000000001
            || (-4000000000000 <= self.0 && self.0 <= -2002147483649)
        {
            PyPeerKind::Channel
        } else {
            unreachable!()
        }
    }

    /// Returns the identity using the Bot API Dialog ID format.
    ///
    /// Will return an arbitrary value if [`Self::kind`] is [`PeerKind::UserSelf`].
    /// This value should not be relied on and may change between releases.
    #[getter]
    pub fn bot_api_dialog_id(&self) -> i64 {
        self.0
    }

    fn __int__(&self) -> i64 {
        self.0
    }

    /// Unpacked peer identifier. Panics if [`Self::kind`] is [`PeerKind::UserSelf`].
    #[getter]
    pub fn bare_id(&self) -> PyResult<i64> {
        Ok(match self.kind() {
            PyPeerKind::User => self.0,
            PyPeerKind::UserSelf => return Err(PyValueError::new_err("self-user ID not known")),
            PyPeerKind::Chat => -self.0,
            PyPeerKind::Channel => -self.0 - 1000000000000,
        })
    }

    fn __eq__(&self, other: &Bound<'_, PyAny>) -> PyResult<bool> {
        if let Ok(other_peer) = other.cast::<PyPeerId>() {
            return Ok(self.0 == other_peer.borrow().0);
        }
        if let Ok(other_int) = other.extract::<i64>() {
            return Ok(self.0 == other_int);
        }
        Ok(false)
    }

    fn __hash__(&self) -> i64 {
        self.0
    }
}

#[repr(transparent)]
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub struct PeerIdLike(pub i64);
impl<'a, 'py> FromPyObject<'a, 'py> for PeerIdLike {
    type Error = PyErr;

    fn extract(ob: Borrowed<'a, 'py, PyAny>) -> Result<Self, Self::Error> {
        if let Ok(v) = ob.extract::<i64>() {
            return Ok(Self(v));
        }
        if let Ok(v) = ob.extract::<PyPeerId>() {
            return Ok(Self(v.0));
        }
        // Peer
        if let Ok(v) = ob.extract::<pytl::types::PyPeerUser>() {
            return Ok(Self(PyPeerId::user(v.user_id)?.0));
        }
        if let Ok(v) = ob.extract::<pytl::types::PyPeerChat>() {
            return Ok(Self(PyPeerId::chat(v.chat_id)?.0));
        }
        if let Ok(v) = ob.extract::<pytl::types::PyPeerChannel>() {
            return Ok(Self(PyPeerId::channel(v.channel_id)?.0));
        }
        // InputPeer
        if let Ok(_) = ob.extract::<pytl::types::PyInputPeerSelf>() {
            return Ok(Self(PyPeerId::self_user()?.0));
        }
        if let Ok(v) = ob.extract::<pytl::types::PyInputPeerUser>() {
            return Ok(Self(PyPeerId::user(v.user_id)?.0));
        }
        if let Ok(v) = ob.extract::<pytl::types::PyInputPeerChat>() {
            return Ok(Self(PyPeerId::chat(v.chat_id)?.0));
        }
        if let Ok(v) = ob.extract::<pytl::types::PyInputPeerChannel>() {
            return Ok(Self(PyPeerId::channel(v.channel_id)?.0));
        }
        // Entity
        if let Ok(v) = ob.extract::<pytl::types::PyUserEmpty>() {
            return Ok(Self(PyPeerId::user(v.id)?.0));
        }
        if let Ok(v) = ob.extract::<pytl::types::PyUser>() {
            return Ok(Self(PyPeerId::user(v.id)?.0));
        }
        if let Ok(v) = ob.extract::<pytl::types::PyChatEmpty>() {
            return Ok(Self(PyPeerId::chat(v.id)?.0));
        }
        if let Ok(v) = ob.extract::<pytl::types::PyChat>() {
            return Ok(Self(PyPeerId::chat(v.id)?.0));
        }
        if let Ok(v) = ob.extract::<pytl::types::PyChatForbidden>() {
            return Ok(Self(PyPeerId::chat(v.id)?.0));
        }
        if let Ok(v) = ob.extract::<pytl::types::PyChannel>() {
            return Ok(Self(PyPeerId::channel(v.id)?.0));
        }
        if let Ok(v) = ob.extract::<pytl::types::PyChannelForbidden>() {
            return Ok(Self(PyPeerId::channel(v.id)?.0));
        }
        // FullEntity
        if let Ok(v) = ob.extract::<pytl::types::PyUserFull>() {
             return Ok(Self(PyPeerId::user(v.id)?.0))
        }
        if let Ok(v) = ob.extract::<pytl::types::messages::PyChatFull>() {
            let py = ob.py();
            return Ok(Self(match v.full_chat {
                pytl::enums::PyChatFull::Full(x) => PyPeerId::chat(x.0.borrow(py).id)?.0,
                pytl::enums::PyChatFull::ChannelFull(x) => PyPeerId::channel(x.0.borrow(py).id)?.0,
            }))
        }
        if let Ok(v) = ob.extract::<pytl::types::PyChatFull>() {
             return Ok(Self(PyPeerId::chat(v.id)?.0))
        }
        if let Ok(v) = ob.extract::<pytl::types::PyChannelFull>() {
             return Ok(Self(PyPeerId::channel(v.id)?.0))
        }
        let cls_name = ob.get_type().qualname()?;
        Err(PyTypeError::new_err(
            format!("expected PeerIdLike, got '{}'", cls_name)
        ))
    }
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[pyclass(
    name = "PeerKind",
    module = "grammers.sessions",
    eq,
    eq_int,
    frozen,
    hash
)]
pub enum PyPeerKind {
    /// The peer identity belongs to a [`tl.types.User`]. May also represent [`PeerKind.UserSelf`].
    User,
    /// The peer identity belongs to a user with its [`tl.types.User.is_self`] flag set to `true`.
    UserSelf,
    /// The peer identity belongs to a [`tl.types.Chat`] or one of its derivatives.
    Chat,
    /// The peer identity belongs to a [`tl.types.Channel`] or one of its derivatives.
    Channel,
}

#[pymethods]
impl PyPeerKind {
    fn __repr__(&self) -> String {
        match self {
            Self::User => "PeerKind.User",
            Self::UserSelf => "PeerKind.UserSelf",
            Self::Chat => "PeerKind.Chat",
            Self::Channel => "PeerKind.Channel",
        }
        .to_string()
    }

    fn __int__(&self) -> i64 {
        *self as i64
    }
}

#[repr(transparent)]
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[pyclass(name = "PeerAuth", module = "grammers.sessions", eq, frozen, hash)]
pub struct PyPeerAuth(i64);

#[pymethods]
impl PyPeerAuth {
    #[new]
    pub fn new(access_hash: i64) -> Self {
        Self(access_hash)
    }

    #[getter]
    pub fn hash(&self) -> i64 {
        self.0
    }

    fn __repr__(&self) -> String {
        format!("PeerAuth({})", self.0)
    }

    fn __int__(&self) -> i64 {
        self.hash()
    }
}

impl Default for PyPeerAuth {
    /// Returns the ambient authority to authorize peers only when Telegram considers it valid.
    ///
    /// The internal representation uses `0` to signal the ambient authority,
    /// although this might happen to be the actual witness used by some peers.
    fn default() -> Self {
        Self(0)
    }
}

#[repr(transparent)]
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub struct PeerAuthLike(pub PyPeerAuth);
impl std::ops::Deref for PeerAuthLike {
    type Target = PyPeerAuth;
    fn deref(&self) -> &Self::Target {
        &self.0
    }
}
impl<'a, 'py> FromPyObject<'a, 'py> for PeerAuthLike {
    type Error = PyErr;

    fn extract(ob: Borrowed<'a, 'py, PyAny>) -> Result<Self, Self::Error> {
        if let Ok(v) = ob.extract::<i64>() {
            return Ok(Self(PyPeerAuth(v)));
        }
        let cls_name = ob.get_type().qualname()?;
        Err(PyTypeError::new_err(format!(
            "peer_auth expected an int or PeerAuth, got '{}'",
            cls_name
        )))
    }
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[pyclass(
    name = "ChannelKind",
    module = "grammers.sessions",
    eq,
    eq_int,
    frozen,
    hash
)]
pub enum PyChannelKind {
    /// Value used for a channel with its [`tl.types.Channel.broadcast`] flag set to `true`.
    Broadcast = 1,
    /// Value used for a channel with its [`tl.types.Channel.megagroup`] flag set to `true`.
    Megagroup,
    /// Value used for a channel with its [`tl.types.Channel.gigagroup`] flag set to `true`.
    Gigagroup,
}

#[pymethods]
impl PyChannelKind {
    fn __repr__(&self) -> String {
        match self {
            Self::Broadcast => "ChannelKind.Broadcast",
            Self::Megagroup => "ChannelKind.Megagroup",
            Self::Gigagroup => "ChannelKind.Gigagroup",
        }
        .to_string()
    }

    fn __int__(&self) -> i64 {
        *self as i64
    }
}

/// An exploded peer reference along with any known useful information about the peer.
#[derive(Clone, Debug, PartialEq, Eq)]
#[pyclass(name = "PeerInfo", module = "grammers.sessions", eq)]
pub enum PyPeerInfo {
    User {
        /// Bare user identifier.
        ///
        /// Despite being `i64`, Telegram only uses strictly positive values.
        id: i64,
        /// Non-ambient authority bound to both the user itself and the session.
        auth: Option<PyPeerAuth>,
        /// Whether this user represents a bot or not.
        bot: Option<bool>,
        /// Whether this user represents the logged-in user authorized by this session or not.
        is_self: Option<bool>,
    },
    Chat {
        /// Bare chat identifier.
        ///
        /// Note that the HTTP Bot API negates this identifier to signal that it is a chat,
        /// but the true value used by Telegram's API is always strictly-positive.
        id: i64,
    },
    Channel {
        /// Bare channel identifier.
        ///
        /// Note that the HTTP Bot API prefixes this identifier with `-100` to signal that it is a channel,
        /// but the true value used by Telegram's API is always strictly-positive.
        id: i64,
        /// Non-ambient authority bound to both the user itself and the session.
        auth: Option<PyPeerAuth>,
        /// Channel kind, useful to determine what the possible permissions on it are.
        kind: Option<PyChannelKind>,
    },
}

#[pymethods]
impl PyPeerInfo {
    #[staticmethod]
    #[pyo3(signature = (id, auth=None, bot=None, is_self=None))]
    fn user(
        id: i64,
        auth: Option<PeerAuthLike>,
        bot: Option<bool>,
        is_self: Option<bool>,
    ) -> PyResult<Self> {
        let _ = PyPeerId::user(id)?;
        Ok(Self::User {
            id,
            auth: auth.map(|x| x.0),
            bot,
            is_self,
        })
    }

    #[staticmethod]
    #[pyo3(signature = (id))]
    fn chat(id: i64) -> PyResult<Self> {
        let _ = PyPeerId::chat(id)?;
        Ok(Self::Chat { id })
    }

    #[staticmethod]
    #[pyo3(signature = (id, auth=None, kind=None))]
    fn channel(id: i64, auth: Option<PeerAuthLike>, kind: Option<PyChannelKind>) -> PyResult<Self> {
        let _ = PyPeerId::channel(id)?;
        Ok(Self::Channel {
            id,
            auth: auth.map(|x| x.0),
            kind,
        })
    }

    /// Returns the `PeerId` represented by this info.
    ///
    /// The returned [`PeerId::kind()`] will never be [`PeerKind::UserSelf`].
    #[getter]
    pub fn id(&self) -> PyResult<PyPeerId> {
        Ok(match self {
            PyPeerInfo::User { id, .. } => PyPeerId::user(*id)?,
            PyPeerInfo::Chat { id } => PyPeerId::chat(*id)?,
            PyPeerInfo::Channel { id, .. } => PyPeerId::channel(*id)?,
        })
    }

    #[getter]
    pub fn bot_api_dialog_id(&self) -> PyResult<i64> {
        Ok(self.id()?.bot_api_dialog_id())
    }

    /// Returns the `PeerAuth` stored in this info.
    #[getter]
    pub fn auth(&self) -> Option<PyPeerAuth> {
        match self {
            PyPeerInfo::User { auth, .. } => *auth,
            PyPeerInfo::Chat { .. } => Some(PyPeerAuth::default()),
            PyPeerInfo::Channel { auth, .. } => *auth,
        }
    }
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[pyclass(name = "PeerRef", module = "grammers.sessions")]
pub struct PyPeerRef {
    /// The peer identity.
    pub id: PyPeerId,
    /// The authority bound to both the sibling identity and the session of the logged-in user.
    pub auth: PyPeerAuth,
}

#[pymethods]
impl PyPeerRef {
    #[new]
    fn new(id: PeerIdLike, auth: PeerAuthLike) -> Self {
        Self {
            id: PyPeerId(id.0),
            auth: auth.0,
        }
    }
}

impl From<tl::enums::Peer> for PyPeerId {
    #[inline]
    fn from(peer: tl::enums::Peer) -> Self {
        <Self as From<&tl::enums::Peer>>::from(&peer)
    }
}
impl<'a> From<&'a tl::enums::Peer> for PyPeerId {
    fn from(peer: &'a tl::enums::Peer) -> Self {
        use tl::enums::Peer;
        match peer {
            Peer::User(user) => Self::from(user),
            Peer::Chat(chat) => Self::from(chat),
            Peer::Channel(channel) => Self::from(channel),
        }
    }
}

impl From<tl::types::PeerUser> for PyPeerId {
    #[inline]
    fn from(user: tl::types::PeerUser) -> Self {
        <Self as From<&tl::types::PeerUser>>::from(&user)
    }
}
impl<'a> From<&'a tl::types::PeerUser> for PyPeerId {
    fn from(user: &'a tl::types::PeerUser) -> Self {
        Self::user(user.user_id).unwrap()
    }
}

impl From<tl::types::PeerChat> for PyPeerId {
    #[inline]
    fn from(user: tl::types::PeerChat) -> Self {
        <Self as From<&tl::types::PeerChat>>::from(&user)
    }
}
impl<'a> From<&'a tl::types::PeerChat> for PyPeerId {
    fn from(chat: &'a tl::types::PeerChat) -> Self {
        Self::chat(chat.chat_id).unwrap()
    }
}

impl From<tl::types::PeerChannel> for PyPeerId {
    #[inline]
    fn from(channel: tl::types::PeerChannel) -> Self {
        <Self as From<&tl::types::PeerChannel>>::from(&channel)
    }
}
impl<'a> From<&'a tl::types::PeerChannel> for PyPeerId {
    fn from(channel: &'a tl::types::PeerChannel) -> Self {
        Self::channel(channel.channel_id).unwrap()
    }
}

impl From<tl::enums::Chat> for PyPeerInfo {
    #[inline]
    fn from(chat: tl::enums::Chat) -> Self {
        <Self as From<&tl::enums::Chat>>::from(&chat)
    }
}
impl<'a> From<&'a tl::enums::Chat> for PyPeerInfo {
    fn from(chat: &'a tl::enums::Chat) -> Self {
        match chat {
            tl::enums::Chat::Chat(chat) => <Self as From<&tl::types::Chat>>::from(&chat),
            tl::enums::Chat::Empty(chat) => <Self as From<&tl::types::ChatEmpty>>::from(&chat),
            tl::enums::Chat::Forbidden(chat) => {
                <Self as From<&tl::types::ChatForbidden>>::from(&chat)
            }
            tl::enums::Chat::Channel(channel) => {
                <Self as From<&tl::types::Channel>>::from(&channel)
            }
            tl::enums::Chat::ChannelForbidden(channel) => {
                <Self as From<&tl::types::ChannelForbidden>>::from(&channel)
            }
        }
    }
}

impl From<tl::enums::User> for PyPeerInfo {
    #[inline]
    fn from(user: tl::enums::User) -> Self {
        <Self as From<&tl::enums::User>>::from(&user)
    }
}
impl<'a> From<&'a tl::enums::User> for PyPeerInfo {
    fn from(user: &'a tl::enums::User) -> Self {
        match user {
            tl::enums::User::User(user) => <Self as From<&tl::types::User>>::from(&user),
            tl::enums::User::Empty(user) => <Self as From<&tl::types::UserEmpty>>::from(&user),
        }
    }
}

impl From<tl::types::User> for PyPeerInfo {
    #[inline]
    fn from(user: tl::types::User) -> Self {
        <Self as From<&tl::types::User>>::from(&user)
    }
}
impl<'a> From<&'a tl::types::User> for PyPeerInfo {
    fn from(user: &'a tl::types::User) -> Self {
        Self::User {
            id: user.id,
            auth: user.access_hash.map(PyPeerAuth),
            bot: Some(user.bot),
            is_self: Some(user.is_self),
        }
    }
}

impl From<tl::types::UserEmpty> for PyPeerInfo {
    #[inline]
    fn from(user: tl::types::UserEmpty) -> Self {
        <Self as From<&tl::types::UserEmpty>>::from(&user)
    }
}
impl<'a> From<&'a tl::types::UserEmpty> for PyPeerInfo {
    fn from(user: &'a tl::types::UserEmpty) -> Self {
        Self::User {
            id: user.id,
            auth: None,
            bot: None,
            is_self: None,
        }
    }
}

impl From<tl::types::Chat> for PyPeerInfo {
    #[inline]
    fn from(chat: tl::types::Chat) -> Self {
        <Self as From<&tl::types::Chat>>::from(&chat)
    }
}
impl<'a> From<&'a tl::types::Chat> for PyPeerInfo {
    fn from(chat: &'a tl::types::Chat) -> Self {
        Self::Chat { id: chat.id }
    }
}

impl From<tl::types::ChatEmpty> for PyPeerInfo {
    #[inline]
    fn from(chat: tl::types::ChatEmpty) -> Self {
        <Self as From<&tl::types::ChatEmpty>>::from(&chat)
    }
}
impl<'a> From<&'a tl::types::ChatEmpty> for PyPeerInfo {
    fn from(chat: &'a tl::types::ChatEmpty) -> Self {
        Self::Chat { id: chat.id }
    }
}

impl From<tl::types::ChatForbidden> for PyPeerInfo {
    #[inline]
    fn from(chat: tl::types::ChatForbidden) -> Self {
        <Self as From<&tl::types::ChatForbidden>>::from(&chat)
    }
}
impl<'a> From<&'a tl::types::ChatForbidden> for PyPeerInfo {
    fn from(chat: &'a tl::types::ChatForbidden) -> Self {
        Self::Chat { id: chat.id }
    }
}

impl From<tl::types::Channel> for PyPeerInfo {
    #[inline]
    fn from(channel: tl::types::Channel) -> Self {
        <Self as From<&tl::types::Channel>>::from(&channel)
    }
}
impl<'a> From<&'a tl::types::Channel> for PyPeerInfo {
    fn from(channel: &'a tl::types::Channel) -> Self {
        Self::Channel {
            id: channel.id,
            auth: channel.access_hash.map(PyPeerAuth),
            kind: <PyChannelKind as TryFrom<&'a tl::types::Channel>>::try_from(channel).ok(),
        }
    }
}

impl From<tl::types::ChannelForbidden> for PyPeerInfo {
    #[inline]
    fn from(channel: tl::types::ChannelForbidden) -> Self {
        <Self as From<&tl::types::ChannelForbidden>>::from(&channel)
    }
}
impl<'a> From<&'a tl::types::ChannelForbidden> for PyPeerInfo {
    fn from(channel: &'a tl::types::ChannelForbidden) -> Self {
        Self::Channel {
            id: channel.id,
            auth: Some(PyPeerAuth(channel.access_hash)),
            kind: <PyChannelKind as TryFrom<&'a tl::types::ChannelForbidden>>::try_from(channel)
                .ok(),
        }
    }
}

impl TryFrom<tl::types::Channel> for PyChannelKind {
    type Error = <PyChannelKind as TryFrom<&'static tl::types::Channel>>::Error;

    #[inline]
    fn try_from(channel: tl::types::Channel) -> Result<Self, Self::Error> {
        <PyChannelKind as TryFrom<&tl::types::Channel>>::try_from(&channel)
    }
}
impl<'a> TryFrom<&'a tl::types::Channel> for PyChannelKind {
    type Error = ();

    fn try_from(channel: &'a tl::types::Channel) -> Result<Self, Self::Error> {
        match channel {
            channel if channel.gigagroup => Ok(Self::Gigagroup),
            channel if channel.broadcast => Ok(Self::Broadcast),
            channel if channel.megagroup => Ok(Self::Megagroup),
            _channel => Err(()),
        }
    }
}

impl TryFrom<tl::types::ChannelForbidden> for PyChannelKind {
    type Error = <PyChannelKind as TryFrom<&'static tl::types::ChannelForbidden>>::Error;

    #[inline]
    fn try_from(channel: tl::types::ChannelForbidden) -> Result<Self, Self::Error> {
        <PyChannelKind as TryFrom<&tl::types::ChannelForbidden>>::try_from(&channel)
    }
}
impl<'a> TryFrom<&'a tl::types::ChannelForbidden> for PyChannelKind {
    type Error = ();

    fn try_from(channel: &'a tl::types::ChannelForbidden) -> Result<Self, Self::Error> {
        match channel {
            // channel if channel.gigagroup => Ok(Self::Gigagroup),
            channel if channel.broadcast => Ok(Self::Broadcast),
            channel if channel.megagroup => Ok(Self::Megagroup),
            _channel => Err(()),
        }
    }
}
