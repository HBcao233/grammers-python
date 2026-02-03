use pyo3::exceptions::{PyTypeError, PyValueError};
use pyo3::types::{PyAnyMethods, PyTypeMethods};
use pyo3::{Borrowed, FromPyObject, PyAny, PyErr, PyResult};

use crate::utils::parse_peer_string;
use grammers_session_pyo3::{PeerIdLike, PyPeerId, PyPeerKind};
use grammers_tl_types_pyo3 as pytl;

pub enum InputPeerLike {
    Phone(String),
    Username(String),
    InputPeer(pytl::enums::PyInputPeer),
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
        let cls_name = ob.get_type().qualname()?;
        Err(PyTypeError::new_err(format!(
            "expected a phone, username, int, or InputPeer, got '{}'",
            cls_name,
        )))
    }
}
