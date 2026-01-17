use pyo3::prelude::*;
use crate::client::PyClient;
use crate::errors::InvocationErrorConverter;
//use grammers_mtsender::InvocationError;

#[cfg(feature = "stub-gen")]
use pyo3_stub_gen::derive::*;

#[cfg_attr(feature = "stub-gen", gen_stub_pymethods)]
#[pymethods]
impl PyClient {
  pub async fn is_authorized(&self) -> PyResult<bool> {
    match self.inner.is_authorized().await {
      Ok(b) => Ok(b),
      Err(err) => Err(InvocationErrorConverter(err).into()),
    }
  }
  
  pub async fn authorize(&self) -> PyResult<bool> {
    
    
    Ok(true)
  }
}