use super::PyClient;
use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;
// use pyo3_async_runtimes::tokio::get_runtime;
use grammers_client::client::UpdatesConfiguration;

#[cfg(feature = "stub-gen")]
use pyo3_stub_gen::derive::*;

#[cfg_attr(feature = "stub-gen", gen_stub_pymethods)]
#[pymethods]
impl PyClient {
    /// Start login in to telegram
    #[pyo3(signature = ())]
    async fn start(&mut self) -> PyResult<()> {
        let _authorized = self.authorize().await?;
        let updates = self
            .updates
            .take()
            .ok_or(PyRuntimeError::new_err("Client fail to initialize."))?;
        let inner = self.inner.clone();
        let stream_updates = inner
            .stream_updates(
                updates,
                UpdatesConfiguration {
                    catch_up: true,
                    ..Default::default()
                },
            )
            .await;
        self.stream_updates = Some(stream_updates);

        Ok(())
    }

    /// Stop connection
    /// Calling clent's methods after stopping will raise ClientStoppedError.
    #[pyo3(signature = ())]
    async fn stop(&mut self) -> PyResult<()> {
        if let Some(stream_updates) = self.stream_updates.take() {
            stream_updates.sync_update_state().await;
        }
        self.handle.quit();
        if let Some(task) = self.pool_task.take() {
            let _ = task.await;
        }
        Ok(())
    }
}
