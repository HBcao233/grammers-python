use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;

use super::PyClient;
use crate::peer::PyUser;
// use crate::runtime::RUNTIME;

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

        self._start_event_pool().await?;

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

    /// Block until the event pool finishes or a termination signal is
    /// received (SIGINT / SIGTERM).
    #[pyo3(signature = ())]
    async fn idle(&self) -> PyResult<()> {
        let inner = self.inner.clone();

        let res = pyo3_async_runtimes::tokio::get_runtime()
            .spawn(async move {
                tokio::select! {
                    biased;
                    // 1. Event pool finished (connection lost, error, quit, …)
                    _ = inner.event_pool_done.notified() => {
                        Ok::<_, PyErr>(())
                    }
                    // 2. Ctrl-C  (SIGINT) / SIGTERM
                    _ = tokio::signal::ctrl_c() => {
                        Ok::<_, PyErr>(())
                    }
                }
            })
            .await
            .map_err(|_| PyRuntimeError::new_err("JoinHandle fail"))?;

        res?;

        if self._is_event_pool_running() {
            self._stop_event_pool().await?;
        }

        Ok(())
    }
}
