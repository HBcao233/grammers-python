use pyo3::PyErr;
use pyo3::exceptions::PyException;
use pyo3::prelude::*;

use grammers_tl_types as tl;

#[pyclass(name = "RpcError", module = "grammers.errors", extends = PyException, subclass)]
pub struct PyRpcError {
    #[pyo3(get)]
    pub code: i32,
    #[pyo3(get)]
    pub name: String,
    #[pyo3(get)]
    pub value: Option<u32>,
    #[pyo3(get)]
    pub caused_by: Option<u32>,
    #[pyo3(get)]
    pub message: Option<String>,
}

impl PyRpcError {
    pub fn new_err(
        code: i32,
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> PyErr {
        PyErr::new::<PyRpcError, _>((code, name, value, caused_by, message))
    }
}

#[pymethods]
impl PyRpcError {
    #[new]
    #[pyo3(signature = (code, name, value, caused_by=None, message=None))]
    fn new(
        code: i32,
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> Self {
        Self {
            code,
            name,
            value,
            caused_by,
            message,
        }
    }

    fn __str__(&self) -> PyResult<String> {
        let message = match &self.message {
            None => "".to_string(),
            Some(x) => format!(" {}", x),
        };

        let caused_by = match self.caused_by {
            None => "".to_string(),
            Some(x) => format!("caused by {}", tl::name_for_id(x)),
        };
        let value = match self.value {
            None => "".to_string(),
            Some(x) => format!("with value: {}", x),
        };
        let more = vec![self.name.clone(), caused_by, value].join(", ");
        let more = if more.is_empty() {
            "".to_string()
        } else {
            format!("({})", more)
        };
        Ok(format!("{}:{}{}", self.code, message, more))
    }

    fn __repr__(&self) -> PyResult<String> {
        let value = match self.value {
            Some(x) => x.to_string(),
            None => "None".to_string(),
        };
        let caused_by = match self.caused_by {
            Some(x) => tl::name_for_id(x),
            None => "None",
        };
        let message = match &self.message {
            Some(x) => x,
            None => &"".to_string(),
        };
        Ok(format!(
            "RpcError(\n  code={},\n  name={},\n  value={},\n  caused_by={},\n  message={},\n)",
            self.code, self.name, value, caused_by, message,
        ))
    }
}

#[pyclass(name = "InvalidDCError", module = "grammers.errors", extends = PyRpcError, subclass)]
pub struct PyInvalidDCError {}

impl PyInvalidDCError {
    pub fn new_err(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> PyErr {
        PyErr::new::<PyInvalidDCError, _>((name, value, caused_by, message))
    }
}

#[pymethods]
impl PyInvalidDCError {
    #[new]
    #[pyo3(signature = (name, value=None, caused_by=None, message=None))]
    fn new(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> (Self, PyRpcError) {
        (
            PyInvalidDCError {},
            PyRpcError {
                code: 303,
                name: name,
                value: value,
                caused_by: caused_by,
                message: Some(message.unwrap_or("ERROR_SEE_OTHER".to_string())),
            },
        )
    }

    #[getter]
    fn new_dc(slf: &Bound<'_, Self>) -> PyResult<Option<u32>> {
        let res = slf.getattr("value")?;
        Ok(if res.is_none() {
            None
        } else {
            Some(res.extract::<u32>()?)
        })
    }
}

/// The query contains errors. In the event that a request was created
/// using a form and contains user generated data, the user should be
/// notified that the data must be corrected before the query is repeated.
#[pyclass(name = "BadRequestError", module = "grammers.errors", extends = PyRpcError, subclass)]
pub struct PyBadRequestError {}

impl PyBadRequestError {
    pub fn new_err(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> PyErr {
        PyErr::new::<PyBadRequestError, _>((name, value, caused_by, message))
    }
}

#[pymethods]
impl PyBadRequestError {
    #[new]
    #[pyo3(signature = (name, value=None, caused_by=None, message=None))]
    fn new(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> (Self, PyRpcError) {
        (
            PyBadRequestError {},
            PyRpcError {
                code: 400,
                name: name,
                value: value,
                caused_by: caused_by,
                message: Some(message.unwrap_or("BAD_REQUEST".to_string())),
            },
        )
    }
}

#[pyclass(name = "UnauthorizedError", module = "grammers.errors", extends = PyRpcError, subclass)]
pub struct PyUnauthorizedError {}

impl PyUnauthorizedError {
    pub fn new_err(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> PyErr {
        PyErr::new::<PyUnauthorizedError, _>((name, value, caused_by, message))
    }
}

#[pymethods]
impl PyUnauthorizedError {
    #[new]
    #[pyo3(signature = (name, value=None, caused_by=None, message=None))]
    fn new(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> (Self, PyRpcError) {
        (
            PyUnauthorizedError {},
            PyRpcError {
                code: 401,
                name: name,
                value: value,
                caused_by: caused_by,
                message: Some(message.unwrap_or("UNAUTHORIZED".to_string())),
            },
        )
    }
}

#[pyclass(name = "ForbiddenError", module = "grammers.errors", extends = PyRpcError, subclass)]
pub struct PyForbiddenError {}

impl PyForbiddenError {
    pub fn new_err(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> PyErr {
        PyErr::new::<PyForbiddenError, _>((name, value, caused_by, message))
    }
}

#[pymethods]
impl PyForbiddenError {
    #[new]
    #[pyo3(signature = (name, value=None, caused_by=None, message=None))]
    fn new(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> (Self, PyRpcError) {
        (
            PyForbiddenError {},
            PyRpcError {
                code: 403,
                name: name,
                value: value,
                caused_by: caused_by,
                message: Some(message.unwrap_or("FORBIDDEN".to_string())),
            },
        )
    }
}

#[pyclass(name = "NotFoundError", module = "grammers.errors", extends = PyRpcError, subclass)]
pub struct PyNotFoundError {}

impl PyNotFoundError {
    pub fn new_err(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> PyErr {
        PyErr::new::<PyNotFoundError, _>((name, value, caused_by, message))
    }
}

#[pymethods]
impl PyNotFoundError {
    #[new]
    #[pyo3(signature = (name, value=None, caused_by=None, message=None))]
    fn new(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> (Self, PyRpcError) {
        (
            PyNotFoundError {},
            PyRpcError {
                code: 404,
                name: name,
                value: value,
                caused_by: caused_by,
                message: Some(message.unwrap_or("NOT_FOUND".to_string())),
            },
        )
    }
}

#[pyclass(name = "AuthKeyError", module = "grammers.errors", extends = PyRpcError, subclass)]
pub struct PyAuthKeyError {}

impl PyAuthKeyError {
    pub fn new_err(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> PyErr {
        PyErr::new::<PyAuthKeyError, _>((name, value, caused_by, message))
    }
}

#[pymethods]
impl PyAuthKeyError {
    #[new]
    #[pyo3(signature = (name, value=None, caused_by=None, message=None))]
    fn new(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> (Self, PyRpcError) {
        (
            PyAuthKeyError {},
            PyRpcError {
                code: 406,
                name: name,
                value: value,
                caused_by: caused_by,
                message: Some(message.unwrap_or("AUTH_KEY".to_string())),
            },
        )
    }
}

#[pyclass(name = "FloodError", module = "grammers.errors", extends = PyRpcError, subclass)]
pub struct PyFloodError {}

impl PyFloodError {
    pub fn new_err(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> PyErr {
        PyErr::new::<PyFloodError, _>((name, value, caused_by, message))
    }
}

#[pymethods]
impl PyFloodError {
    #[new]
    #[pyo3(signature = (name, value=None, caused_by=None, message=None))]
    fn new(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> (Self, PyRpcError) {
        (
            PyFloodError {},
            PyRpcError {
                code: 420,
                name: name,
                value: value,
                caused_by: caused_by,
                message: Some(message.unwrap_or("FLOOD".to_string())),
            },
        )
    }

    #[getter]
    fn seconds(slf: &Bound<'_, Self>) -> PyResult<Option<u32>> {
        let res = slf.getattr("value")?;
        Ok(if res.is_none() {
            None
        } else {
            Some(res.extract::<u32>()?)
        })
    }
}

#[pyclass(name = "ServerError", module = "grammers.errors", extends = PyRpcError, subclass)]
pub struct PyServerError {}

impl PyServerError {
    pub fn new_err(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> PyErr {
        PyErr::new::<PyServerError, _>((name, value, caused_by, message))
    }
}

#[pymethods]
impl PyServerError {
    #[new]
    #[pyo3(signature = (name, value=None, caused_by=None, message=None))]
    fn new(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> (Self, PyRpcError) {
        (
            PyServerError {},
            PyRpcError {
                code: 500,
                name: name,
                value: value,
                caused_by: caused_by,
                message: Some(message.unwrap_or("INTERNAL".to_string())),
            },
        )
    }
}

#[pyclass(name = "TimedOutError", module = "grammers.errors", extends = PyRpcError, subclass)]
pub struct PyTimedOutError {}

impl PyTimedOutError {
    pub fn new_err(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> PyErr {
        PyErr::new::<PyTimedOutError, _>((name, value, caused_by, message))
    }
}

#[pymethods]
impl PyTimedOutError {
    #[new]
    #[pyo3(signature = (name, value=None, caused_by=None, message=None))]
    fn new(
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: Option<String>,
    ) -> (Self, PyRpcError) {
        (
            PyTimedOutError {},
            PyRpcError {
                code: 503,
                name: name,
                value: value,
                caused_by: caused_by,
                message: Some(message.unwrap_or("Timeout".to_string())),
            },
        )
    }
}
