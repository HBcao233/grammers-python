use pyo3::prelude::*;
use grammers_session::{Session, PackedChat, UpdateState};
use grammers_tl_types as tl;

#[pyclass(name = "Session", session = "grammers.sessions")]
pub struct PySession {
  inner: Box<dyn Session>,
}

#[pymethods]
impl PySession {
  #[pyo3(signature = "class")]
  pub fn new(session: PySession) -> Self {
    Self { handler }
  }
}

impl Session for PySession {
  
}