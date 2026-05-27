use pyo3::PyTypeInfo;
use pyo3::exceptions::{PyTypeError, PyValueError};
use pyo3::prelude::*;
use pyo3::types::PyType;

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[pyclass(from_py_object, name = "EventKind", module = "grammers.events")]
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

impl EventBuilder {
    pub fn clone_ref(&self, py: Python<'_>) -> Self {
        Self {
            kind: self.kind,
            filter: match &self.filter {
                Some(x) => Some(x.clone_ref(py)),
                None => None,
            },
        }
    }
}

impl<'a, 'py> FromPyObject<'a, 'py> for EventBuilder {
    type Error = PyErr;

    fn extract(ob: Borrowed<'a, 'py, PyAny>) -> Result<Self, Self::Error> {
        let obj;
        let ob = if ob.is_instance_of::<PyType>() {
            obj = ob.call0()?;
            obj.as_borrowed()
        } else {
            ob
        };

        if let Ok(kind) = ob.extract::<PyEventKind>() {
            return Ok(Self { kind, filter: None });
        }
        let py = ob.py();
        if let Ok(v) = ob.cast::<PyLogined>() {
            return Ok(Self {
                kind: PyEventKind::Logined,
                filter: match &v.borrow().filter {
                    Some(x) => Some(x.clone_ref(py)),
                    None => None,
                },
            });
        }
        if let Ok(v) = ob.cast::<PyError>() {
            return Ok(Self {
                kind: PyEventKind::Error,
                filter: match &v.borrow().filter {
                    Some(x) => Some(x.clone_ref(py)),
                    None => None,
                },
            });
        }
        if let Ok(v) = ob.cast::<PyRawUpdate>() {
            return Ok(Self {
                kind: PyEventKind::RawUpdate,
                filter: match &v.borrow().filter {
                    Some(x) => Some(x.clone_ref(py)),
                    None => None,
                },
            });
        }

        Err(PyTypeError::new_err("need a EventBuilder or EventKind"))
    }
}

impl<'py> IntoPyObject<'py> for EventBuilder {
    type Target = PyAny;
    type Output = Bound<'py, PyAny>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> PyResult<Bound<'py, PyAny>> {
        match self.kind {
            PyEventKind::Logined => Bound::new(
                py,
                PyLogined {
                    filter: self.filter,
                },
            )
            .map(|x| x.into_any()),
            PyEventKind::Error => Bound::new(
                py,
                PyError {
                    filter: self.filter,
                },
            )
            .map(|x| x.into_any()),
            PyEventKind::RawUpdate => Bound::new(
                py,
                PyRawUpdate {
                    filter: self.filter,
                },
            )
            .map(|x| x.into_any()),
        }
    }
}

#[pyclass(name = "EventBuilder", module = "grammers.event", subclass)]
pub struct PyEventBuilder {}

#[pymethods]
impl PyEventBuilder {
    #[allow(non_snake_case)]
    #[classattr]
    fn Logined(py: Python<'_>) -> Py<PyType> {
        PyLogined::type_object(py).unbind()
    }

    #[allow(non_snake_case)]
    #[classattr]
    fn Error(py: Python<'_>) -> Py<PyType> {
        PyError::type_object(py).unbind()
    }

    #[allow(non_snake_case)]
    #[classattr]
    fn RawUpdate(py: Python<'_>) -> Py<PyType> {
        PyRawUpdate::type_object(py).unbind()
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
    fn new(filter: Option<Py<PyAny>>) -> PyResult<Self> {
        let is_callable = match filter {
            None => true,
            Some(ref x) => Python::attach(|py| x.bind(py).is_callable()),
        };
        if !is_callable {
            Err(PyValueError::new_err("filter must be a callable or None."))
        } else {
            Ok(Self { filter })
        }
    }

    fn __str__(&self, py: Python<'_>) -> PyResult<String> {
        let filter = match &self.filter {
            Some(x) => x.bind(py).repr()?.extract()?,
            None => "None".to_string(),
        };
        Ok(format!("EventBuilder.Logined(filter={})", filter))
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
    fn new(filter: Option<Py<PyAny>>) -> PyResult<Self> {
        let is_callable = match filter {
            None => true,
            Some(ref x) => Python::attach(|py| x.bind(py).is_callable()),
        };
        if !is_callable {
            Err(PyValueError::new_err("filter must be a callable or None."))
        } else {
            Ok(Self { filter })
        }
    }

    fn __str__(&self, py: Python<'_>) -> PyResult<String> {
        let filter = match &self.filter {
            Some(x) => x.bind(py).repr()?.extract()?,
            None => "None".to_string(),
        };
        Ok(format!("EventBuilder.Error(filter={})", filter))
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
    fn new(filter: Option<Py<PyAny>>) -> PyResult<Self> {
        let is_callable = match filter {
            None => true,
            Some(ref x) => Python::attach(|py| x.bind(py).is_callable()),
        };
        if !is_callable {
            Err(PyValueError::new_err("filter must be a callable or None."))
        } else {
            Ok(Self { filter })
        }
    }

    fn __str__(&self, py: Python<'_>) -> PyResult<String> {
        let filter = match &self.filter {
            Some(x) => x.bind(py).repr()?.extract()?,
            None => "None".to_string(),
        };
        Ok(format!("EventBuilder.RawUpdate(filter={})", filter))
    }
}
