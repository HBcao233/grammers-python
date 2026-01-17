use pyo3::prelude::*;
use grammers_tl_types_pyo3 as tlpy;
// use grammers_mtsender::InvocationError;

use super::PyClient;
use crate::errors::InvocationErrorConverter;

#[cfg(feature = "stub-gen")]
use pyo3_stub_gen::derive::*;


#[cfg_attr(feature = "stub-gen", gen_stub_pymethods)]
#[pymethods]
impl PyClient {
  pub async fn invoke<'py>(
    &self, 
    request: tlpy::PyTLRequest,
  ) -> PyResult<tlpy::PyTLObject> {
    let result = self.inner.invoke(&request).await;
    let result = result.map_err(|e| InvocationErrorConverter(e))?;
    Ok(result)
  }
}