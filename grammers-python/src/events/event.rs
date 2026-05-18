use pyo3::prelude::*;
use pyo3::exceptions::PyNotImplementedError;

use grammers_tl_types_pyo3 as pytl;
use grammers_tl_types_pyo3::TLObject;

use crate::PyClient;
use crate::peer::PyUser;
use super::PyEventKind;

pub(crate) enum Event {
    Logined(Py<PyLoginedEvent>),
    Error(Py<PyErrorEvent>),
    RawUpdate(Py<PyRawUpdateEvent>),
}

impl Event {
    pub fn logined(client: &PyClient, user: Py<PyUser>) -> PyResult<Self> {
        Self::Logined(Py::new(py, PyLoginedEvent::new(client.clone(), user)))
    }
    
    pub fn error(client: &PyClient, error: PyErr) -> PyResult<Self> {
        Self::Error(Py::new(py, PyErrorEvent::new(client.clone(), error)))
    }
    
    pub fn raw_update(client: &PyClient, update: pytl::enums::PyUpdate) -> PyResult<Self> {
        Self::RawUpdate(Py::new(py, PyRawUpdateEvent::new(client.clone(), update)))
    }

    pub fn kind(&self) -> PyEventKind {
        match self {
            Event::Logined(_) => PyEventKind::Logined,
            Event::Error(_) => PyEventKind::Error,
            Event::RawUpdate(_) => PyEventKind::RawUpdate,
        }
    }
    
    pub fn client(&self, py: Python<'_>) -> PyClient {
        match self {
            Event::Logined(x) => x.borrow(py).clone(),
            Event::Error(x) => x.borrow(py).clone(),
            Event::RawUpdate(x) => x.borrow(py).clone(),
        }
    }
    
    pub fn clone_ref(&self, py: Python<'_>) -> Event {
        match self {
            Event::Logined(x) => Event::Logined(x.clone_ref(py)),
            Event::Error(x) => Event::Error(x.clone_ref(py)),
            Event::RawUpdate(x) => Event::RawUpdate(x.clone_ref(py)),
        }
    }
}

#[pyclass(name = "EventCommon", module = "grammers.events", subclass, dict)]
pub struct PyEventCommon {
    client: Py<PyClient>,
}

impl PyEventCommon {
    #[new]
    pub fn new(client: PyClient) -> Self {
        Self {
            client
        }
    }
    
    #[classattr]
    fn kind() -> PyResult<PyEventKind> {
        Err(PyNotImplementedError::new_err(()))
    }
    
    #[getter]
    fn client(self, py: Python<'_>) -> Py<PyClient> {
        self.client.clone_ref(py)
    }
    
    fn to_dict(slf: Bound<'_, Self>) -> PyResult<Py<PyDict>> {
        let event_name = format!("{}Event", slf.borrow(py).kind().name());
        let dict = slf.into_any().dict()?;
        dict.set_item("_", event_name)?;
        Ok(dict.unbind())
    }
    
    fn __repr__(slf: &Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(slf, None)
    }
    
    fn __str__(slf: &Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(slf, Some(0))
    }
}

#[pyclass(name = "LoginedEvent", module = "grammers.events", extends = PyEventCommon)]
pub struct PyLoginedEvent {
    // logined user.
    #[pyo3(get)]
    user: Py<PyUser>,
}

impl PyLoginedEvent {
    #[classattr]
    fn kind() -> PyEventKind {
        PyEventKind::Logined
    }
    
    #[new]
    fn new(client: PyClient, user: Py<PyUser>) -> PyClassInitializer<Self> {
        PyClassInitializer::from(PyEventCommon::new(client))
            .add_subclass(Self {
                user,
            })
    }
}

#[pyclass(name = "ErrorEvent", module = "grammers.events", extends = PyEventCommon)]
pub struct PyErrorEvent {
    // The error occurred when run handler.
    #[pyo3(get)]
    error: PyErr,
}

impl PyErrorEvent {
    #[classattr]
    fn kind() -> PyEventKind {
        PyEventKind::Error
    }
    
    #[new]
    fn new(client: PyClient, error: PyErr) -> PyClassInitializer<Self> {
        PyClassInitializer::from(PyEventCommon::new(client))
            .add_subclass(Self {
                error,
            })
    }
}

#[pyclass(name = "LoginedEvent", module = "grammers.events", extends = PyEventCommon)]
pub struct PyRawUpdateEvent {
    // logined user.
    #[pyo3(get)]
    update: pytl::enums::PyUpdate,
}

impl PyRawUpdateEvent {
    #[classattr]
    fn kind() -> PyEventKind {
        PyEventKind::RawUpdate
    }
    
    #[new]
    pub fn new(client: PyClient, update: pytl::enums::PyUpdate) -> PyClassInitializer<Self> {
        PyClassInitializer::from(PyEventCommon::new(client))
            .add_subclass(Self {
                update,
            })
    }
}
