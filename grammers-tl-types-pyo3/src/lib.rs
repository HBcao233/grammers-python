mod common;
mod generated;
pub use common::{TLObject, TLRequest, PyRawVec, PyTLObjectWrapper};
pub use generated::{PyTLRequest, PyTLObject, types, functions, enums};
use generated::{types_, functions_, enums_};

pub type Buffer<'a, 'b> = &'a mut grammers_tl_types::deserialize::Cursor<'b>;

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
  
  #[pymodule_export]
  use crate::enums_;
}