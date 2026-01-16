#[pyo3::pymodule(name = "types")]
pub mod types_ {
  #[pymodule_export]
  use crate::types::PyPong;
}