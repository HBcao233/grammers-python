use pyo3::exceptions::{PyTypeError, PyValueError, PyNotImplementedError};
use pyo3::prelude::*;
use pyo3::PyTypeInfo;
use pyo3::types::{PyDict, PyDictMethods, PyType};

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

    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        Python::attach(|py| {
            let dict = PyDict::new(py);
            dict.set_item("_", "PeerId")?;
            dict.set_item("bot_api_dialog_id", self.bot_api_dialog_id())?;
            dict.set_item("kind", self.kind())?;
            dict.set_item("bare_id", self.bare_id()?)?;
            Ok(dict.unbind())
        })
    }
    
    fn __repr__(slf: &Bound<'_, Self>) -> PyResult<String> {
        pytl::TLObject::pretty_format(&slf.call_method0("to_dict")?, None)
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
    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        Python::attach(|py| {
            let dict = PyDict::new(py);
            dict.set_item("_", self.__repr__())?;
            Ok(dict.unbind())
        })
    }
    
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

    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        Python::attach(|py| {
            let dict = PyDict::new(py);
            dict.set_item("_", "PeerAuth")?;
            dict.set_item("hash", self.0)?;
            Ok(dict.unbind())
        })
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
    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        Python::attach(|py| {
            let dict = PyDict::new(py);
            dict.set_item("_", self.__repr__())?;
            Ok(dict.unbind())
        })
    }
    
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


pub enum PeerInfoLike {
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
    }
}

impl<'a, 'py> FromPyObject<'a, 'py> for PeerInfoLike {
    type Error = PyErr;
    fn extract(ob: Borrowed<'a, 'py, PyAny>) -> PyResult<Self> {
        if let Ok(x) = ob.extract::<PyPeerInfoUser>() {
            return Ok(Self::User {
                id: x.id,
                auth: x.auth,
                bot: x.bot,
                is_self: x.is_self,
            });
        }
        if let Ok(x) = ob.extract::<PyPeerInfoChat>() {
            return Ok(Self::Chat {
                id: x.id,
            });
        }
        if let Ok(x) = ob.extract::<PyPeerInfoChannel>() {
            return Ok(Self::Channel {
                id: x.id,
                auth: x.auth,
                kind: x.kind,
            });
        }
        let cls_name = ob.get_type().qualname()?;
        Err(PyTypeError::new_err(
            format!("expected PeerInfo, got '{}'.", cls_name)
        ))
    }
}

impl<'py> IntoPyObject<'py> for PeerInfoLike {
    type Target = PyPeerInfo;
    type Output = Bound<'py, PyPeerInfo>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> PyResult<Bound<'py, PyPeerInfo>> {
        match self {
            Self::User { id, auth, bot, is_self } => Ok(Bound::new(
                py,
                PyPeerInfoUser::new(id, auth.map(PeerAuthLike), bot, is_self)?
            )?.into_super()),
            Self::Chat { id } => Ok(Bound::new(
                py,
                PyPeerInfoChat::new(id)?
            )?.into_super()),
            Self::Channel { id, auth, kind } => Ok(Bound::new(
                py,
                PyPeerInfoChannel::new(id, auth.map(PeerAuthLike), kind)?
            )?.into_super()),
        }
    }
}

impl PeerInfoLike {
    pub fn id(&self) -> PyPeerId {
        match self {
            Self::User { id, .. } => PyPeerId::user(*id).unwrap(),
            Self::Chat { id } => PyPeerId::chat(*id).unwrap(),
            Self::Channel { id, .. } => PyPeerId::channel(*id).unwrap(),
        }
    }
    
    pub fn auth(&self) -> Option<PyPeerAuth> {
        match self {
            Self::User { auth, .. } => *auth,
            Self::Chat { .. } => None,
            Self::Channel { auth, .. } => *auth,
        }
    }
}

/// An exploded peer reference along with any known useful information about the peer.
#[derive(Clone, Debug)]
#[pyclass(name = "PeerInfo", module = "grammers.sessions", subclass)]
pub struct PyPeerInfo {}

#[pymethods]
impl PyPeerInfo {
    #[classattr]
    #[pyo3(name = "User")]
    fn user(py: Python<'_>) -> Py<PyType> {
        PyPeerInfoUser::type_object(py).unbind()
    }
    
    #[classattr]
    #[pyo3(name = "Chat")]
    fn chat(py: Python<'_>) -> Py<PyType> {
        PyPeerInfoChat::type_object(py).unbind()
    }
    
    #[classattr]
    #[pyo3(name = "Channel")]
    fn channel(py: Python<'_>) -> Py<PyType> {
        PyPeerInfoChannel::type_object(py).unbind()
    }

    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        Err(PyNotImplementedError::new_err(
            "PeerInfo subclasses must implement to_dict()",
        ))
    }
    
    fn __repr__(slf: &Bound<'_, Self>) -> PyResult<String> {
        pytl::TLObject::pretty_format(&slf.call_method0("to_dict")?, None)
    }
}

#[derive(Clone, PartialEq, Eq)]
#[pyclass(name = "PeerInfoUser", module = "grammers.sessions", extends = PyPeerInfo, eq)]
pub struct PyPeerInfoUser {
    /// Bare user identifier.
    ///
    /// Despite being `i64`, Telegram only uses strictly positive values.
    id: i64,
    /// Non-ambient authority bound to both the user itself and the session.
    #[pyo3(get, set)]
    auth: Option<PyPeerAuth>,
    /// Whether this user represents a bot or not.
    #[pyo3(get, set)]
    bot: Option<bool>,
    /// Whether this user represents the logged-in user authorized by this session or not.
    #[pyo3(get, set)]
    is_self: Option<bool>,
}

#[pymethods]
impl PyPeerInfoUser {
    #[new]
    #[pyo3(signature = (id, auth=None, bot=None, is_self=None))]
    fn new(
        id: i64,
        auth: Option<PeerAuthLike>,
        bot: Option<bool>,
        is_self: Option<bool>,
    ) -> PyResult<PyClassInitializer<Self>> {
        let _ = PyPeerId::user(id)?;
        let base = PyClassInitializer::from(PyPeerInfo {});
        let x = Self {
            id,
            auth: auth.map(|x| x.0),
            bot,
            is_self,
        };
        Ok(base.add_subclass(x))
    }
    
    #[getter]
    fn id(&self) -> PyPeerId {
        PyPeerId::user(self.id).unwrap()
    }
    
    #[setter(id)]
    fn set_id(&mut self, id: PeerIdLike) -> PyResult<()> {
        let _ = PyPeerId::user(id.0)?;
        self.id = id.0;
        Ok(())
    }
    
    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        Python::attach(|py| {
            let dict = PyDict::new(py);
            dict.set_item("_", "PeerInfo.User")?;
            dict.set_item("id", self.id())?;
            dict.set_item("auth", self.auth)?;
            dict.set_item("bot", self.bot)?;
            dict.set_item("is_self", self.is_self)?;
            Ok(dict.unbind())
        })
    }
}

#[derive(Clone, PartialEq, Eq)]
#[pyclass(name = "PeerInfoChat", module = "grammers.sessions", extends = PyPeerInfo, eq)]
pub struct PyPeerInfoChat {
    id: i64,
}

#[pymethods]
impl PyPeerInfoChat {
    #[new]
    fn new(id: i64) -> PyResult<PyClassInitializer<Self>> {
        let _ = PyPeerId::chat(id)?;
        let base = PyClassInitializer::from(PyPeerInfo {});
        Ok(base.add_subclass(Self { id }))
    }
    
    #[getter]
    fn id(&self) -> PyPeerId {
        PyPeerId::chat(self.id).unwrap()
    }
    
    #[setter(id)]
    fn set_id(&mut self, id: PeerIdLike) -> PyResult<()> {
        let _ = PyPeerId::chat(id.0)?;
        self.id = id.0;
        Ok(())
    }
    
    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        Python::attach(|py| {
            let dict = PyDict::new(py);
            dict.set_item("_", "PeerInfo.Chat")?;
            dict.set_item("id", self.id())?;
            Ok(dict.unbind())
        })
    }
}

#[derive(Clone, PartialEq, Eq)]
#[pyclass(name = "PeerInfoChannel", module = "grammers.sessions", extends = PyPeerInfo, eq)]
pub struct PyPeerInfoChannel {
    /// Bare channel identifier.
    ///
    /// Note that the HTTP Bot API prefixes this identifier with `-100` to signal that it is a channel,
    /// but the true value used by Telegram's API is always strictly-positive.
    #[pyo3(get, set)]
    id: i64,
    /// Non-ambient authority bound to both the user itself and the session.
    #[pyo3(get, set)]
    auth: Option<PyPeerAuth>,
    /// Channel kind, useful to determine what the possible permissions on it are.
    #[pyo3(get, set)]
    kind: Option<PyChannelKind>,
}

#[pymethods]
impl PyPeerInfoChannel {
    #[new]
    #[pyo3(signature = (id, auth=None, kind=None))]
    fn new(
        id: i64,
        auth: Option<PeerAuthLike>,
        kind: Option<PyChannelKind>,
    ) -> PyResult<PyClassInitializer<Self>> {
        let _ = PyPeerId::channel(id)?;
        let base = PyClassInitializer::from(PyPeerInfo {});
        let x = Self {
            id,
            auth: auth.map(|x| x.0),
            kind,
        };
        Ok(base.add_subclass(x))
    }
    
    #[getter]
    fn id(&self) -> PyPeerId {
        PyPeerId::channel(self.id).unwrap()
    }
    
    #[setter(id)]
    fn set_id(&mut self, id: PeerIdLike) -> PyResult<()> {
        let _ = PyPeerId::channel(id.0)?;
        self.id = id.0;
        Ok(())
    }
    
    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        Python::attach(|py| {
            let dict = PyDict::new(py);
            dict.set_item("_", "PeerInfo.Channel")?;
            dict.set_item("id", self.id())?;
            dict.set_item("auth", self.auth)?;
            dict.set_item("kind", self.kind)?;
            Ok(dict.unbind())
        })
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
