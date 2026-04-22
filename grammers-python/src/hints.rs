use pyo3::exceptions::{PyTypeError, PyValueError};
use pyo3::prelude::*;
use pyo3::types::{PyAnyMethods, PyTypeMethods};

use crate::peer::PyPeer;
use crate::utils::parse_peer_string;
use grammers_session_pyo3::{PeerIdLike, PyPeerId, PyPeerKind};
use grammers_tl_types_pyo3 as pytl;

pub enum InputPeerLike {
    Phone(String),
    Username(String),
    InputPeer(pytl::enums::PyInputPeer),
    Peer(PyPeer),
}
impl<'a, 'py> FromPyObject<'a, 'py> for InputPeerLike {
    type Error = PyErr;
    fn extract(ob: Borrowed<'a, 'py, PyAny>) -> PyResult<Self> {
        if let Ok(s) = ob.extract::<String>() {
            return parse_peer_string(&s).ok_or(PyValueError::new_err("Invalid phone or username"));
        }
        if let Ok(x) = ob.extract::<PeerIdLike>() {
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
        if let Ok(x) = ob.extract::<pytl::enums::PyInputPeer>() {
            return Ok(Self::InputPeer(x));
        }
        if let Ok(x) = ob.extract::<PyPeer>() {
            return Ok(Self::Peer(x));
        }

        let cls_name = ob.get_type().qualname()?;
        Err(PyTypeError::new_err(format!(
            "expected a phone, username, int, InputPeer or Peer, got '{}'",
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
                Ok::<_, PyErr>(
                    x.clone()
                        .into_pyobject(py)?
                        .call_method0("__str__")?
                        .extract::<String>()?,
                )
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
