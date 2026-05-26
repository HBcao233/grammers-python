use pyo3::prelude::*;

use super::PyClient;
use crate::peer::PyUser;

#[pymethods]
impl PyClient {
    /// Start login in to telegram
    #[pyo3(signature = ())]
    async fn start(&mut self) -> PyResult<Py<PyUser>> {
        let authorized = self.is_authorized().await?;
        let user = if !authorized || self.bot_token().is_some() {
            self.authorize().await?
        } else {
            self.get_me().await?
        };
        self.set_me(user);

        Ok(self._me().expect("me setup"))
    }

    /// Stop client
    /// Calling clent's methods after stopping will raise ClientStoppedError.
    #[pyo3(signature = ())]
    async fn stop(&mut self) -> PyResult<()> {
        let inner = self.inner.clone();
        if self._is_event_pool_running() {
            self._stop_event_pool().await?;
        }

        self.disconnect();

        // session close
        inner.session.close().await?;

        let task = inner.pool_task.lock().unwrap().take();
        if let Some(task) = task {
            let _ = task.await;
        }
        Ok(())
    }
}
