use pyo3::FromPyObject;
use grammers_session_pyo3::PeerIdLike;
use grammers_tl_types_pyo3 as pytl;

#[derive(FromPyObject)]
pub enum InputPeerLike {
    InputPeerUserFromMessage(pytl::types::InputPeerUserFromMessage),
    InputPeerChannelFromMessage(pytl::types::InputPeerChannelFromMessage),
}
