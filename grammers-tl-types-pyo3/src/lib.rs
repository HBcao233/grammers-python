mod common;
mod generated;
pub use common::{Buffer, TLObject, TLRequest, PyRawVec, PyTLObjectWrapper, PyTLRequestWrapper};
pub use generated::{PyTLRequest, PyTLObject, types, functions, enums};
use generated::{types_, functions_};


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