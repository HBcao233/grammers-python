use grammers_mtsender::InvocationError;
use grammers_tl_types as tl;
use pyo3::exceptions::{PyException, PyIOError, PyTypeError};
use pyo3::prelude::*;
use pyo3::{PyErr, create_exception};

#[pymodule(name = "errors")]
pub mod _errors {
    use pyo3::prelude::*;

    #[pymodule_export]
    #[allow(non_upper_case_globals)]
    const __package__: &str = &"grammers";

    #[pymodule_export]
    use super::PyRpcError;

    #[pymodule_init]
    fn init(_m: &Bound<'_, PyModule>) -> PyResult<()> {
        // m.add("RpcError", m.py().get_type::<PyRpcError>())?;
        Ok(())
    }
}

create_exception!(errors, ClientStoppedError, PyException);

// #[repr(transparent)]
#[pyclass(name = "RpcError", module = "grammers.errors", extends = PyException)]
pub struct PyRpcError {
    #[pyo3(get)]
    code: i32,
    #[pyo3(get)]
    name: String,
    #[pyo3(get)]
    value: Option<u32>,
    #[pyo3(get)]
    caused_by: Option<u32>,
    #[pyo3(get)]
    message: String,
}

impl PyRpcError {
    fn new_err(
        code: i32,
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: String,
    ) -> PyErr {
        PyErr::new::<PyRpcError, _>((code, name, value, caused_by, message))
    }
}

#[pymethods]
impl PyRpcError {
    #[new]
    fn new(
        code: i32,
        name: String,
        value: Option<u32>,
        caused_by: Option<u32>,
        message: String,
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
        Ok(format!(
            "RpcError {}: {}{}",
            self.code, self.message, caused_by
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
        Ok(format!(
            "RpcError(\n  code={},\n  name={},\n  value={},\n  caused_by={},\n  message={},\n)",
            self.code, self.name, value, caused_by, self.message,
        ))
    }
}

pub struct InvocationErrorConverter(pub InvocationError);

impl From<InvocationErrorConverter> for PyErr {
    fn from(err: InvocationErrorConverter) -> PyErr {
        match err.0 {
            InvocationError::Rpc(e) => {
                PyRpcError::new_err(e.code, e.name, e.value, e.caused_by, "".to_string())
            }
            InvocationError::Io(e) => PyIOError::new_err(format!("{}", e)),
            InvocationError::Deserialize(e) => PyTypeError::new_err(format!("Deserialize: {}", e)),
            InvocationError::Transport(e) => PyTypeError::new_err(format!("Transport: {}", e)),
            InvocationError::Dropped => ClientStoppedError::new_err(
                "Client runner not start. Pleace re-create Client() to restart.".to_string(),
            ),
            InvocationError::InvalidDc => PyTypeError::new_err("InvalidDc".to_string()),
            InvocationError::Authentication(e) => {
                PyTypeError::new_err(format!("Authentication: {}", e))
            }
        }
    }
}
