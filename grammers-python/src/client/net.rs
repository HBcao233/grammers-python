use pyo3::prelude::*;

use super::PyClient;
use crate::errors::InvocationErrorConverter;

use grammers_mtsender_pyo3::InvocationError;
use grammers_tl_types_pyo3::{PyTLObject, PyTLRequest};

use grammers_tl_types::{Deserializable, Serializable, RemoteCall};

#[pymethods]
impl PyClient {
    pub async fn invoke(&self, request: PyTLRequest) -> PyResult<PyTLObject> {
        self.invoke_raw(request)
            .await
            .map_err(|e| InvocationErrorConverter(e).into())
    }

    pub async fn invoke_in_dc(&self, dc_id: i32, request: PyTLRequest) -> PyResult<PyTLObject> {
        self.invoke_raw_in_dc(dc_id, request)
            .await
            .map_err(|e| InvocationErrorConverter(e).into())
    }
}

impl PyClient {
    pub async fn invoke_raw_in_dc(
        &self,
        dc_id: i32,
        request: PyTLRequest,
    ) -> Result<PyTLObject, InvocationError> {
        let response = self.do_invoke_in_dc(dc_id, request.to_bytes()).await?;
        PyTLObject::from_bytes(&response).map_err(Into::into)
    }

    pub async fn invoke_raw(&self, request: PyTLRequest) -> Result<PyTLObject, InvocationError> {
        let session = self.inner.lock().unwrap().session.clone();
        let dc_id = session
            .home_dc_id()
            .await
            .map_err(|e| InvocationError::PyErr(e))?;
        self.invoke_raw_in_dc(dc_id, request).await
    }

    pub async fn invoke_tl_in_dc<R: RemoteCall>(
        &self,
        dc_id: i32,
        request: &R,
    ) -> Result<R::Return, InvocationError> {
        let response = self.do_invoke_in_dc(dc_id, request.to_bytes()).await?;
        R::Return::from_bytes(&response).map_err(Into::into)
    }

    pub async fn invoke_tl<R: RemoteCall>(
        &self,
        request: &R,
    ) -> Result<R::Return, InvocationError> {
        let session = &self.inner.lock().unwrap().session;
        let dc_id = session
            .home_dc_id()
            .await
            .map_err(|e| InvocationError::PyErr(e))?;
        self.invoke_tl_in_dc(dc_id, request).await
    }

    async fn do_invoke_in_dc(
        &self,
        dc_id: i32,
        request_body: Vec<u8>,
    ) -> Result<Vec<u8>, InvocationError> {
        let handle = self.inner.lock().unwrap().handle.clone();
        handle.invoke_in_dc(dc_id, request_body.clone()).await
    }
}
