mod peer;
mod session;
mod types;
// mod utils;
// mod runtime;

pub use peer::{
    PeerIdLike, PeerInfo, PyChannelKind, PyPeerAuth, PyPeerId, PyPeerInfo, PyPeerKind, PyPeerRef,
};
// pub use utils::into_future;
// pub use runtime::{asyncio, event_loop, into_future};
pub use session::{PySession, Session};
pub use types::{
    PyChannelState, PyDcOption, PySocketAddrV4, PySocketAddrV6, PyUpdateState, PyUpdatesState,
    UpdateStateLike,
};

use pyo3::sync::PyOnceLock;
use pyo3::{Py, PyAny, PyResult, Python};
use pyo3_async_runtimes::tokio::get_current_locals;
use pyo3_async_runtimes::{TaskLocals, into_future_with_locals};

static LOCALS: PyOnceLock<TaskLocals> = PyOnceLock::new();

fn get_locals<'py>(py: Python<'py>) -> PyResult<TaskLocals> {
    LOCALS
        .get_or_try_init(py, || Ok(get_current_locals(py)?))
        .cloned()
}

pub fn into_future(awaitable: Py<PyAny>) -> impl Future<Output = PyResult<Py<PyAny>>> + Send {
    async move {
        Python::attach(|py| {
            let locals = get_locals(py)?;
            into_future_with_locals(&locals, awaitable.into_bound(py))
        })?
        .await
    }
}

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
    use super::PyPeerRef;

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
