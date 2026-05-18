use pyo3::prelude::*;

use std::sync::Arc;

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[pyclass(name = "EventKind", module = "grammers.events")]
pub enum PyEventKind {
    Logined = -1,  // When account is logined.
    Error = -2,    // When error occurred.
    RawUpdate = 0, // When received a raw Update.
}

#[pymethods]
impl PyEventKind {
    pub fn __str__(&self) -> String {
        format!("EventKind.{}", self.name())
    }
}

impl PyEventKind {
    pub fn name(&self) -> String {
        match self {
            PyEventKind::Logined => "Logined".to_string(),
            PyEventKind::Error => "Error".to_string(),
            PyEventKind::RawUpdate => "RawUpdate".to_string(),
        }
    }
}

pub struct EventBuilder {
    pub kind: PyEventKind,
    pub filter: Option<Py<PyAny>>,
}

impl<'a, 'py> FromPyObject<'a, 'py> for EventBuilder {
    type Error = PyErr;

    fn extract(ob: Borrowed<'a, 'py, PyAny>) -> Result<Self, Self::Error> {
        let ob = match ob.extract::<PyType>() {
            Err(_) => ob,
            Ok(ty) => ty.call0()?.borrow();
        };
        
        if let Ok(kind) = ob.extract::<PyEventKind>() {
            return Ok(Self { kind, filter: None });
        }
        if let Ok(v) = ob.extract::<PyConnected>() {
            return Ok(Self {
                kind: PyEventKind::Connected,
                filter: v.filter,
            });
        }
        if let Ok(v) = ob.extract::<PyLogined>() {
            return Ok(Self {
                kind: PyEventKind::Logined,
                filter: v.filter,
            });
        }
        if let Ok(v) = ob.extract::<PyRawUpdate>() {
            return Ok(Self {
                kind: PyEventKind::RawUpdate,
                filter: v.filter,
            });
        }

        Err(PyTypeError::new_err("need a EventBuilder or EventKind"))
    }
}

#[pyclass(name = "EventBuilder", module = "grammers.event", subclass)]
pub struct PyEventBuilder {};

#[pymethods]
impl PyEventBuilder {
    #[classattr]
    fn Logined() -> Py<PyType> {
        PyLogined.type_object().unbind()
    }
    
    #[classattr]
    fn Error() -> Py<PyType> {
        PyError.type_object().unbind()
    }
    
    #[classattr]
    fn RawUpdate() -> Py<PyType> {
        PyRawUpdate.type_object().unbind()
    }
}

#[pyclass(name = "Logined", module = "grammers.events")]
pub struct PyLogined {
    pub filter: Option<Py<PyAny>>,
}

#[pymethods]
impl PyLogined {
    #[new]
    #[pyo3(signature = (filter=None))]
    fn new(filter: Option<Py<PyAny>>) -> Self {
        Self {
            filter,
        }
    }
    
    fn __str__(&self) -> PyResult<String> {
        let filter = match {
            Some(x) => x.repr()?,
            None => "None".to_string(),
        };
        format!("EventBuilder.Logined(filter={})", filter)
    }
}

#[pyclass(name = "Error", module = "grammers.events")]
pub struct PyError {
    pub filter: Option<Py<PyAny>>,
}

#[pymethods]
impl PyError {
    #[new]
    #[pyo3(signature = (filter=None))]
    fn new(filter: Option<Py<PyAny>>) -> Self {
        Self {
            filter,
        }
    }
    
    fn __str__(&self) -> PyResult<String> {
        let filter = match {
            Some(x) => x.repr()?,
            None => "None".to_string(),
        };
        format!("EventBuilder.Error(filter={})", filter)
    }
}

#[pyclass(name = "RawUpdate", module = "grammers.events")]
pub struct PyRawUpdate {
    pub filter: Option<Py<PyAny>>,
}

#[pymethods]
impl PyRawUpdate {
    #[new]
    #[pyo3(signature = (filter=None))]
    fn new(filter: Option<Py<PyAny>>) -> Self {
        Self {
            filter,
        }
    }
    
    fn __str__(&self) -> PyResult<String> {
        let filter = match self.filter {
            Some(x) => x.repr()?.extract(),
            None => "None".to_string(),
        };
        format!("EventBuilder.RawUpdate(filter={})", filter)
    }
}
