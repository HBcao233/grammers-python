use pyo3::prelude::*;
use pyo3::{PyClassInitializer, PyErr};

use super::{PyRpcError, PyInvalidDCError};

#[pyclass(name = "UserMigrateError", module = "grammers.errors", extends = PyInvalidDCError)]
pub struct PyUserMigrateError {
    #[pyo3(get)]
    pub new_dc: u32,
}

impl PyUserMigrateError {
    pub fn new_err(
        value: Option<u32>,
        caused_by: Option<u32>,
    ) -> PyErr {
        PyErr::new::<PyRpcError, _>((value, caused_by))
    }
}

#[pymethods]
impl PyUserMigrateError {
    #[new]
    #[pyo3(signature = (value = None, caused_by = None))]
    fn new(value: Option<u32>, caused_by: Option<u32>) -> PyClassInitializer<Self> {
        let message = format!(
            "The user whose identity is being used to execute queries is associated with DC {}",
            value.unwrap(),
        );
        PyClassInitializer::from(
            PyRpcError {
                code: 303,
                name: "USER_MIGRATE".to_string(),
                value,
                caused_by,
                message: Some(message),
            })
            .add_subclass(PyInvalidDCError {})
            .add_subclass(PyUserMigrateError {
                new_dc: value.unwrap(),
            })
    }
}
