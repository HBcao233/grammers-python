use pyo3::exceptions::{PyException, PyIOError, PyTypeError};
use pyo3::{PyErr, create_exception};

use grammers_mtsender_pyo3::InvocationError;

use super::{PyInvalidDCError, PyRpcError, PyUserMigrateError};

create_exception!("grammers.errors", ClientStoppedError, PyException);

pub struct InvocationErrorConverter(pub InvocationError);

impl From<InvocationError> for InvocationErrorConverter {
    fn from(x: InvocationError) -> Self {
        InvocationErrorConverter(x)
    }
}
impl From<InvocationErrorConverter> for PyErr {
    fn from(err: InvocationErrorConverter) -> PyErr {
        match err.0 {
            InvocationError::Rpc(e) => match e.code {
                303 => match e.name.as_ref() {
                    "" => PyUserMigrateError::new_err(e.value, e.caused_by),
                    _ => PyInvalidDCError::new_err(e.name, e.value, e.caused_by, None),
                },
                _ => PyRpcError::new_err(e.code, e.name, e.value, e.caused_by, None),
            },
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
            InvocationError::PyErr(e) => e,
        }
    }
}
