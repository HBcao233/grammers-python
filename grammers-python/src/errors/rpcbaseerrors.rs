use pyo3::prelude::*;
use pyo3::PyErr;
use pyo3::exceptions::PyException;

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
        let caused_by = match self.caused_by {
            None => "".to_string(),
            Some(x) => format!(" (caused by {})", tl::name_for_id(x)),
        };
        let value = match self.value {
            None => "".to_string(),
            Some(x) => format!(" (with value: {})", x),
        };
        let message = match &self.message {
            Some(x) => x,
            None => &"".to_string()
        };
        Ok(format!(
            "RpcError {}{}: {}{}{}",
            self.code, 
            self.name,
            message, 
            caused_by,
            value,
        ))
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
            None => &"".to_string()
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
        PyErr::new::<PyRpcError, _>((name, value, caused_by, message))
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
        message: Option<String>
    ) -> (Self, PyRpcError) {
        (
            PyInvalidDCError { },
            PyRpcError {
                code: 303,
                name: name,
                value: value,
                caused_by: caused_by,
                message: Some(message.unwrap_or("ERROR_SEE_OTHER".to_string())),
            },
        )
    }
}
