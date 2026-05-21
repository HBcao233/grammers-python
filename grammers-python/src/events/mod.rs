mod common;
mod event;
mod handler;
mod pool;

pub(crate) use common::{EventBuilder, EventKind};
pub use common::{PyError, PyEventBuilder, PyEventKind, PyLogined, PyRawUpdate};
pub(crate) use event::Event;
pub use event::{PyErrorEvent, PyEventCommon, PyLoginedEvent, PyRawUpdateEvent};
pub(crate) use handler::EventHandlersManager;
pub(crate) use pool::EventPool;

#[pyo3::pymodule]
pub(crate) mod events_ {
    #[pymodule_export]
    use super::PyEventKind;

    #[pymodule_export]
    use super::PyEventBuilder;

    #[pymodule_export]
    use super::PyLogined;

    #[pymodule_export]
    use super::PyError;

    #[pymodule_export]
    use super::PyRawUpdate;

    #[pymodule_export]
    use super::PyEventCommon;

    #[pymodule_export]
    use super::PyLoginedEvent;

    #[pymodule_export]
    use super::PyErrorEvent;

    #[pymodule_export]
    use super::PyRawUpdateEvent;
}
