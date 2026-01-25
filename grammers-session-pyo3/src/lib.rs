mod peer;
mod types;
mod session;
// mod dc_options;
// mod storages;

pub use peer::{PyPeerId, PeerIdLike, PyPeerAuth, PyPeerInfo, PyPeerKind, PyChannelKind, PyPeerRef};
pub use types::{PyDcOption, PyUpdatesState, PyUpdateState};
pub use session::{PySession, Session};

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
    use super::PySession;
    
    // #[pymodule_export]
    // use super::PyMemorySession;
}