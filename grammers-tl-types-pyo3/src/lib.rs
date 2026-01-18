mod common;
mod generated;
pub use common::{Buffer, PyRawVec, PyTLObjectWrapper, PyTLRequestWrapper, TLObject, TLRequest};
pub use generated::{PyTLObject, PyTLRequest, enums, functions, types};
use generated::{functions_, types_};

#[pyo3::pymodule(name = "tl", module = "grammers")]
pub mod tl {
    #[pymodule_export]
    use crate::TLObject;

    #[pymodule_export]
    use crate::TLRequest;

    #[pymodule_export]
    use crate::types_;

    #[pymodule_export]
    use crate::functions_;
}
