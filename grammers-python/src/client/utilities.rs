use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;

use super::{PyClient, UpdatesConfiguration};

#[pymethods]
impl PyClient {
    /// Start login in to telegram
    #[pyo3(signature = ())]
    async fn start(&mut self) -> PyResult<Py<PyUser>> {
        let authorized = self.is_authorized().await?;
        let user = if !authorized {
            self.authorize().await?
        } else {
            self.get_me().await?
        };
        self.set_me(user);

        self._me().expect("me setup")
    }

    /// Stop client
    /// Calling clent's methods after stopping will raise ClientStoppedError.
    #[pyo3(signature = ())]
    async fn stop(&mut self) -> PyResult<()> {
        let inner = self.inner.clone();
        let stream_updates = inner.stream_updates.lock().unwrap().take();
        if let Some(s) = stream_updates {
            s.sync_update_state().await?;
        }
        self.disconnect();

        // session close
        let session = self.session();
        session.close().await?;

        let task = inner.pool_task.lock().unwrap().take();
        if let Some(task) = task {
            let _ = task.await;
        }
        Ok(())
    }
}
