mod peer;
mod session;
mod types;
pub mod utils;

pub use peer::{
    PeerIdLike, PyChannelKind, PyPeerAuth, PyPeerId, PyPeerInfo, PyPeerKind, PyPeerRef,
};
pub use session::{PySession, Session};
pub use types::{PyChannelState, PyDcOption, PySocketAddrV4, PySocketAddrV6, PyUpdateState, PyUpdatesState};

#[pyo3::pymodule(name = "sessions")]
pub mod sessions_ {
    // #[pymodule_export]
    // use super::KNOWN_DC_OPTIONS;

    #[pymodule_export]
    use super::PyPeerId;

    #[pymodule_export]
    use super::PyPeerAuth;

    #[pymodule_export]
    use super::PyPeerInfo;

    #[pymodule_export]
    use super::PyPeerKind;

    #[pymodule_export]
    use super::PyChannelKind;

    #[pymodule_export]
    use super::PyDcOption;
    
    #[pymodule_export]
    use super::PySocketAddrV4;
    
    #[pymodule_export]
    use super::PySocketAddrV6;

    #[pymodule_export]
    use super::PyChannelState;

    #[pymodule_export]
    use super::PySession;

    #[pymodule_export]
    use super::PyUpdatesState;

    #[pymodule_export]
    use super::PyUpdateState;
}
