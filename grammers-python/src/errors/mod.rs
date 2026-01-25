use pyo3::prelude::*;

mod common;
mod rpcbaseerrors;
mod rpcerrorlist;

pub use common::{ClientStoppedError, InvocationErrorConverter};
pub use rpcbaseerrors::{PyRpcError, PyInvalidDCError};
pub use rpcerrorlist::PyUserMigrateError;

#[pymodule(name = "errors")]
pub mod _errors {
    use pyo3::prelude::*;

    #[pymodule_export]
    #[allow(non_upper_case_globals)]
    const __package__: &str = &"grammers";

    #[pymodule_export]
    use super::ClientStoppedError;
    
    #[pymodule_export]
    use super::PyRpcError;
    
    #[pymodule_export]
    use super::PyInvalidDCError;
    
    #[pymodule_export]
    use super::PyUserMigrateError;

    #[pymodule_init]
    fn init(_m: &Bound<'_, PyModule>) -> PyResult<()> {
        Ok(())
    }
}
