use pyo3::exceptions::{PyTypeError, PyValueError};
use pyo3::prelude::*;
use pyo3::types::{PyAnyMethods, PyTypeMethods};

use grammers_session_pyo3::{PeerIdLike, PyPeerId, PyPeerKind, PyPeerRef};
use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

use crate::PyClient;
use crate::message::{PyMessage, InputMessage};
use crate::peer::{convertPeerId2Peer, PyPeer};
use crate::utils::parse_peer_string;


#[derive(Clone, IntoPyObject)]
pub enum InputPeerLike {
    Phone(String),
    Username(String),
    InputPeer(pytl::enums::PyInputPeer),
    Peer(PyPeer),
    PeerRef(PyPeerRef),
}
impl<'a, 'py> FromPyObject<'a, 'py> for InputPeerLike {
    type Error = PyErr;
    fn extract(obj: Borrowed<'a, 'py, PyAny>) -> PyResult<Self> {
        if let Ok(s) = obj.extract::<String>() {
            return parse_peer_string(&s).ok_or(PyValueError::new_err("Invalid phone or username"));
        }
        if let Ok(x) = obj.extract::<PeerIdLike>() {
            let x = PyPeerId::new(x)?;
            return Ok(match x.kind() {
                PyPeerKind::UserSelf => Self::InputPeer(pytl::types::PyInputPeerSelf {}.into()),
                PyPeerKind::User => Self::InputPeer(
                    pytl::types::PyInputPeerUser {
                        user_id: x.bare_id()?,
                        access_hash: 0,
                    }
                    .into(),
                ),
                PyPeerKind::Chat => Self::InputPeer(
                    pytl::types::PyInputPeerChat {
                        chat_id: x.bare_id()?,
                    }
                    .into(),
                ),
                PyPeerKind::Channel => Self::InputPeer(
                    pytl::types::PyInputPeerChannel {
                        channel_id: x.bare_id()?,
                        access_hash: 0,
                    }
                    .into(),
                ),
            });
        }
        if let Ok(x) = obj.extract::<pytl::enums::PyInputPeer>() {
            return Ok(Self::InputPeer(x));
        }
        if let Ok(x) = obj.extract::<PyPeer>() {
            return Ok(Self::Peer(x));
        }
        if let Ok(x) = obj.extract::<PyPeerRef>() {
            return Ok(Self::PeerRef(x));
        }

        let cls_name = obj.get_type().qualname()?;
        Err(PyTypeError::new_err(format!(
            "expected a phone, username, int, InputPeer, Peer or PeerRef, got '{}'",
            cls_name,
        )))
    }
}

impl InputPeerLike {
    pub fn stringify(&self) -> PyResult<String> {
        Ok(match self {
            InputPeerLike::Phone(x) => format!("Phone({})", x),
            InputPeerLike::Username(x) => format!("Username({})", x),
            InputPeerLike::InputPeer(x) => Python::attach(|py| {
                Ok::<_, PyErr>(
                    x.clone()
                        .into_pyobject(py)?
                        .call_method0("__str__")?
                        .extract::<String>()?,
                )
            })?,
            InputPeerLike::Peer(x) => Python::attach(|py| {
                x.clone()
                    .into_pyobject(py)?
                    .call_method0("__str__")?
                    .extract::<String>()
            })?,
            InputPeerLike::PeerRef(x) => Python::attach(|py| {
                x.clone()
                    .into_pyobject(py)?
                    .call_method0("__repr__")?
                    .extract::<String>()
            })?,
            /*match x {
                pytl::enums::PyInputPeer::Empty(_) => write!(f, "InputPeerEmpty()"),
                pytl::enums::PyInputPeer::PeerSelf(_) => write!(f, "InputPeerSelf()"),
                pytl::enums::PyInputPeer::Chat(x) => Python::attach(|py| {
                    write!(f, "InputPeerChat({})", x.0.borrow(py).chat_id)
                }),
                pytl::enums::PyInputPeer::User(x) => Python::attach(|py| {
                    write!(f, "InputPeerUser({})", x.0.borrow(py).user_id)
                }),
                pytl::enums::PyInputPeer::Channel(x) => Python::attach(|py| {
                    write!(f, "InputPeerChannel({})", x.0.borrow(py).channel_id)
                }),
                pytl::enums::PyInputPeer::UserFromMessage(x) => Python::attach(|py| {
                    let borrowed = x.0.borrow(py);
                    write!(
                        f,
                        "InputPeerUserFromMessage(peer={}, msg_id={}, user_id={})",
                        borrowed.peer,
                        borrowed.msg_id,
                        borrowed.user_id
                    )
                }),
                pytl::enums::PyInputPeer::ChannelFromMessage(x) => Python::attach(|py| {
                    let borrowed = x.0.borrow(py);
                    write!(
                        f,
                        "InputPeerChannelFromMessage(peer={}, msg_id={}, channel_id={})",
                        borrowed.peer,
                        borrowed.msg_id,
                        borrowed.channel_id
                    )
                }),
            },*/
        })
    }
}

#[derive(Clone, FromPyObject)]
pub enum InputReplyToLike {
    MsgId(i32),
    InputReplyTo(pytl::enums::PyInputReplyTo),
}
impl InputReplyToLike {
    fn toMessageReplyHeader(&self, client: &PyClient) -> tl::enums::MessageReplyHeader {
        let x = tl::enums::InputReplyTo::from(self);
        match x {
            tl::enums::InputReplyTo::Message(x) => tl::types::MessageReplyHeader {
                reply_to_scheduled: false,
                forum_topic: false,
                quote: false,
                reply_to_msg_id: Some(x.reply_to_msg_id),
                reply_to_peer_id: PyPeerId::from(x.reply_to_peer_id).into(),
                reply_from: None,
                reply_media: None,
                reply_to_top_id: x.top_msg_id,
                quote_text: x.quote_text,
                quote_entities: x.quote_entities,
                quote_offset: x.quote_offset,
                todo_item_id: x.todo_item_id,
                poll_option: x.poll_option,
            }.into(),
            tl::enums::InputReplyTo::Story(x) => tl::types::MessageReplyStoryHeader {
                peer: convertPeerId2Peer(PyPeerId::from(x.peer), client),
                story_id: x.story_id,
            }.into(),
            tl::enums::InputReplyTo::MonoForum(_) => todo!(),
        }
    }
    
    fn toPyMessageReplyHeader(&self, client: &PyClient) -> pytl::enums::PyMessageReplyHeader {
        self.toMessageReplyHeader(client).into()
    }
}
impl From<InputReplyToLike> for tl::enums::InputReplyTo {
    fn from(x: InputReplyToLike) -> Self {
        match x {
            InputReplyToLike::MsgId(reply_to_msg_id) => tl::types::InputReplyToMessage {
                reply_to_msg_id,
                top_msg_id: None,
                reply_to_peer_id: None,
                quote_text: None,
                quote_entities: None,
                quote_offset: None,
                monoforum_peer_id: None,
                todo_item_id: None,
                poll_option: None,
            }.into(),
            InputReplyToLike::InputReplyTo(x) => x.into(),
        }
    }
}
impl From<InputReplyToLike> for pytl::enums::PyInputReplyTo {
    fn from(x: InputReplyToLike) -> Self {
        tl::enums::InputReplyTo::from(x).into()
    }
}


#[derive(Clone, FromPyObject)]
pub enum InputMessageLike {
    Str(String),
    Message(PyMessage),
}
impl InputMessageLike {
    pub async fn into_input_message(self) -> InputMessage {
        match self {
            InputMessageLike::Str(message) => InputMessage {
                message,
                ..Self::default()
            },
            InputMessageLike::Message(x) => InputMessage::from_py_message(x),
        }
    }
}
