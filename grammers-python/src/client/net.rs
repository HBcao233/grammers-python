use pyo3::prelude::*;

use grammers_mtsender_pyo3::InvocationError;
use grammers_tl_types_pyo3::{TLObjectLike, TLRequestLike};

use grammers_tl_types::{Deserializable, RemoteCall, Serializable};

use super::PyClient;
use crate::errors::PyInvocationError;

#[pymethods]
impl PyClient {
    /// Invoke a raw API call. This directly sends the request to Telegram's servers.
    ///
    /// Using function definitions corresponding to a different layer is likely to cause the
    /// responses to the request to not be understood.
    ///
    /// <div class="warning">
    ///
    /// This method is **not** part of the stability guarantees of semantic
    /// versioning. It **may** break during *minor* version changes (but not on patch version
    /// changes). Use with care.
    ///
    /// </div>
    ///
    /// Examples
    ///
    /// ```ignore
    /// await client.invoke(functions.Ping(ping_id=0))
    /// ```
    #[pyo3(name = "invoke")]
    async fn py_invoke(&self, request: TLRequestLike) -> PyResult<TLObjectLike> {
        let dc_id = self.session().home_dc_id().await?;
        self.py_invoke_in_dc(dc_id, request).await
    }

    #[pyo3(name = "invoke_in_dc")]
    async fn py_invoke_in_dc(&self, dc_id: i32, request: TLRequestLike) -> PyResult<TLObjectLike> {
        let response = self
            .do_invoke_in_dc(dc_id, request.to_bytes())
            .await
            .map_err(PyInvocationError::new)?;
        TLObjectLike::from_bytes(&response)
            .map_err(Into::into)
            .map_err(PyInvocationError::new)
    }
    
    #[pyo3(name = "invoke_raw")]
    async fn py_invoke_raw(&self, request_body: Vec<u8>) -> PyResult<Vec<u8>> {
        let dc_id = self.session().home_dc_id().await?;
        self.py_invoke_raw_in_dc(dc_id, request_body).await
    }
    
    #[pyo3(name = "invoke_raw_in_dc")]
    async fn py_invoke_raw_in_dc(&self, dc_id: i32, request_body: Vec<u8>) -> PyResult<Vec<u8>> {
        self
            .do_invoke_in_dc(dc_id, request_body)
            .await
            .map_err(PyInvocationError::new)
    }
}

impl PyClient {
    pub async fn invoke_in_dc<R: RemoteCall>(
        &self,
        dc_id: i32,
        request: &R,
    ) -> Result<R::Return, InvocationError> {
        let response = self.do_invoke_in_dc(dc_id, request.to_bytes()).await?;
        R::Return::from_bytes(&response).map_err(Into::into)
    }

    pub async fn invoke<R: RemoteCall>(&self, request: &R) -> Result<R::Return, InvocationError> {
        let dc_id = self
            .session()
            .home_dc_id()
            .await
            .map_err(|e| InvocationError::PyErr(e))?;
        self.invoke_in_dc(dc_id, request).await
    }

    async fn do_invoke_in_dc(
        &self,
        dc_id: i32,
        request_body: Vec<u8>,
    ) -> Result<Vec<u8>, InvocationError> {
        self.handle()
            .invoke_in_dc(dc_id, request_body.clone())
            .await
    }
}
