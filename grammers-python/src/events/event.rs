use pyo3::exceptions::{PyBaseException, PyNotImplementedError};
use pyo3::prelude::*;
use pyo3::types::{PyAnyMethods, PyDict};

use grammers_tl_types_pyo3 as pytl;
use grammers_tl_types_pyo3::TLObject;

use super::PyEventKind;
use crate::PyClient;
use crate::peer::PyUser;

#[derive(FromPyObject, IntoPyObject)]
pub enum Event {
    Logined(Py<PyLoginedEvent>),
    Error_(Py<PyErrorEvent>),
    RawUpdate(Py<PyRawUpdateEvent>),
}

impl Event {
    pub fn logined(py: Python<'_>, client: Py<PyClient>, user: Py<PyUser>) -> PyResult<Self> {
        Ok(Self::Logined(Py::new(
            py,
            PyLoginedEvent::new(client, user),
        )?))
    }

    pub fn error(py: Python<'_>, client: Py<PyClient>, error: PyErr) -> PyResult<Self> {
        Ok(Self::Error_(Py::new(
            py,
            PyErrorEvent::new(client, error.into_value(py)),
        )?))
    }

    pub fn raw_update(
        py: Python<'_>,
        client: Py<PyClient>,
        update: pytl::enums::PyUpdate,
    ) -> PyResult<Self> {
        Ok(Self::RawUpdate(Py::new(
            py,
            PyRawUpdateEvent::new(client, update),
        )?))
    }

    pub fn kind(&self) -> PyEventKind {
        match self {
            Event::Logined(_) => PyEventKind::Logined,
            Event::Error_(_) => PyEventKind::Error,
            Event::RawUpdate(_) => PyEventKind::RawUpdate,
        }
    }

    pub fn client(&self, py: Python<'_>) -> PyResult<Py<PyClient>> {
        Ok(match self {
            Event::Logined(x) => x.bind(py).as_super().borrow().client(py),
            Event::Error_(x) => x.bind(py).as_super().borrow().client(py),
            Event::RawUpdate(x) => x.bind(py).as_super().borrow().client(py),
        })
    }

    pub fn clone_ref(&self, py: Python<'_>) -> Event {
        match self {
            Event::Logined(x) => Event::Logined(x.clone_ref(py)),
            Event::Error_(x) => Event::Error_(x.clone_ref(py)),
            Event::RawUpdate(x) => Event::RawUpdate(x.clone_ref(py)),
        }
    }
}

#[pyclass(name = "EventCommon", module = "grammers.events", subclass, dict)]
pub struct PyEventCommon {
    client: Py<PyClient>,
}

#[pymethods]
impl PyEventCommon {
    #[new]
    pub fn new(client: Py<PyClient>) -> Self {
        Self { client }
    }

    #[getter]
    fn kind(&self) -> PyResult<PyEventKind> {
        Err(PyNotImplementedError::new_err(()))
    }

    #[getter]
    fn client(&self, py: Python<'_>) -> Py<PyClient> {
        self.client.clone_ref(py)
    }

    fn to_dict(slf: Bound<'_, Self>) -> PyResult<Py<PyDict>> {
        let kind: Bound<'_, PyEventKind> = slf.getattr("kind")?.extract()?;
        let event_name = format!("{}Event", kind.borrow().name());
        let dict: Bound<'_, PyDict> = slf.into_any().getattr("__dict__")?.extract()?;
        dict.set_item("_", event_name)?;
        Ok(dict.unbind())
    }

    fn __repr__(slf: Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(&slf, None)
    }

    fn __str__(slf: Bound<'_, Self>) -> PyResult<String> {
        TLObject::pretty_format(&slf, Some(0))
    }
}

#[pyclass(name = "LoginedEvent", module = "grammers.events", extends = PyEventCommon)]
pub struct PyLoginedEvent {
    // logined user.
    #[pyo3(get)]
    user: Py<PyUser>,
}

#[pymethods]
impl PyLoginedEvent {
    #[classattr]
    fn kind() -> PyEventKind {
        PyEventKind::Logined
    }

    #[new]
    fn new(client: Py<PyClient>, user: Py<PyUser>) -> PyClassInitializer<Self> {
        PyClassInitializer::from(PyEventCommon::new(client)).add_subclass(Self { user })
    }

    #[getter]
    fn user(&self, py: Python<'_>) -> Py<PyUser> {
        self.user.clone_ref(py)
    }

    fn to_dict(slf: Bound<'_, Self>) -> PyResult<Py<PyDict>> {
        let py = slf.py();
        let borrowed = slf.borrow();
        let kind = PyLoginedEvent::kind();
        let user = borrowed.user(py);

        let dict = PyDict::new(py);
        dict.set_item("_", "LoginedEvent")?;
        dict.set_item("kind", kind)?;
        dict.set_item("user", user)?;
        Ok(dict.unbind())
    }
}

#[pyclass(name = "ErrorEvent", module = "grammers.events", extends = PyEventCommon)]
pub struct PyErrorEvent {
    // The error occurred when run handler.
    #[pyo3(get)]
    error: Py<PyBaseException>,
}

#[pymethods]
impl PyErrorEvent {
    #[classattr]
    fn kind() -> PyEventKind {
        PyEventKind::Error
    }

    #[new]
    fn new(client: Py<PyClient>, error: Py<PyBaseException>) -> PyClassInitializer<Self> {
        PyClassInitializer::from(PyEventCommon::new(client)).add_subclass(Self { error })
    }

    #[getter]
    fn error(&self, py: Python<'_>) -> Py<PyBaseException> {
        self.error.clone_ref(py)
    }
    
    fn to_dict(slf: Bound<'_, Self>) -> PyResult<Py<PyDict>> {
        let py = slf.py();
        let borrowed = slf.borrow();
        let kind = PyErrorEvent::kind();
        let error = borrowed.error(py);

        let dict = PyDict::new(py);
        dict.set_item("_", "ErrorEvent")?;
        dict.set_item("kind", kind)?;
        dict.set_item("error", error)?;
        Ok(dict.unbind())
    }
}

#[pyclass(name = "RawUpdateEvent", module = "grammers.events", extends = PyEventCommon)]
pub struct PyRawUpdateEvent {
    // logined user.
    #[pyo3(get)]
    update: pytl::enums::PyUpdate,
}

#[pymethods]
impl PyRawUpdateEvent {
    #[classattr]
    fn kind() -> PyEventKind {
        PyEventKind::RawUpdate
    }

    #[new]
    pub fn new(client: Py<PyClient>, update: pytl::enums::PyUpdate) -> PyClassInitializer<Self> {
        PyClassInitializer::from(PyEventCommon::new(client)).add_subclass(Self { update })
    }

    #[getter]
    fn update(&self, _py: Python<'_>) -> pytl::enums::PyUpdate {
        self.update.clone()
    }
    
    fn to_dict(slf: Bound<'_, Self>) -> PyResult<Py<PyDict>> {
        let py = slf.py();
        let borrowed = slf.borrow();
        let kind = PyRawUpdateEvent::kind();
        let update = borrowed.update(py);

        let dict = PyDict::new(py);
        dict.set_item("_", "RawUpdateEvent")?;
        dict.set_item("kind", kind)?;
        dict.set_item("update", update)?;
        Ok(dict.unbind())
    }
}
