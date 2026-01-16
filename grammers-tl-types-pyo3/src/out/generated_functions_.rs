#[pyo3::pymodule(name = "functions")]
pub mod functions_ {
  #[pymodule_export]
  use crate::functions::PyPing;
}