use pyo3::prelude::*;

use super::PyClient;

#[pymethods]
impl PyClient {
    /// Start login in to telegram
    #[pyo3(signature = ())]
    async fn start(&mut self) -> PyResult<()> {
        let _authorized = self.authorize().await?;
        /*let updates = self
            .updates
            .take()
            .ok_or(PyRuntimeError::new_err("Client fail to initialize."))?;
        let stream_updates = self
            .stream_updates(
                updates,
                UpdatesConfiguration {
                    catch_up: true,
                    ..Default::default()
                },
            )
            .await;
        self.stream_updates = Some(stream_updates);*/

        Ok(())
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
            if let Ok(res) = task.await {
                res?;
            }
        }
        Ok(())
    }
}
