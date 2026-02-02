use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;

use super::{PyClient, UpdatesConfiguration};

#[pymethods]
impl PyClient {
    /// Start login in to telegram
    #[pyo3(signature = ())]
    async fn start(&mut self) -> PyResult<()> {
        let authorized = self.is_authorized().await?;
        self.me = Some(if !authorized {
            self.authorize().await?
        } else {
            self.get_me().await?
        }.into());

        self._start().await
    }

    /// Stop client
    /// Calling clent's methods after stopping will raise ClientStoppedError.
    #[pyo3(signature = ())]
    async fn stop(&mut self) -> PyResult<()> {
        let stream_updates = self.inner.lock().unwrap().stream_updates.take();
        if let Some(s) = stream_updates {
            s.sync_update_state().await?;
        }
        self.disconnect();
        let task = self.inner.lock().unwrap().pool_task.take();
        if let Some(task) = task {
            let _ = task.await;
        }
        Ok(())
    }
}

impl PyClient {
    async fn _start(&self) -> PyResult<()> {
        let updates = self
            .inner
            .lock()
            .unwrap()
            .updates
            .take()
            .ok_or(PyRuntimeError::new_err("Client fail to initialize."))?;
        let stream_updates = self
            .stream_updates(
                updates,
                UpdatesConfiguration {
                    catch_up: true,
                    update_queue_limit: Some(100),
                },
            )
            .await?;
        self.inner.lock().unwrap().stream_updates = Some(stream_updates);
        Ok(())
    }
}
