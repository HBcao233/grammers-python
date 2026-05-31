use std::sync::Arc;
use tokio::fs;
use tokio::io::AsyncWriteExt;
use tokio::sync::{Mutex, mpsc};

use pyo3::exceptions::{PyIOError, PyRuntimeError, PyValueError};
use pyo3::prelude::*;
use pyo3_async_runtimes::tokio::get_runtime;

use super::{DownloadIter, DownloadIterVariant, PyDownloadIter};
use crate::client::PyClient;
use crate::media::Downloadable;
use crate::utils::maybe_await;

pub const MIN_CHUNK_SIZE: i32 = 4 * 1024;
pub const MAX_CHUNK_SIZE: i32 = 512 * 1024;

#[pyclass(
    skip_from_py_object,
    name = "ProgressUpdate",
    module = "grammers.custom"
)]
pub struct PyProgressUpdate {
    #[pyo3(get, set)]
    downloaded: i64,
    #[pyo3(get, set)]
    total: Option<i64>,
}

#[pymethods]
impl PyProgressUpdate {
    #[new]
    #[pyo3(signature = (downloaded, total=None))]
    pub fn new(downloaded: i64, total: Option<i64>) -> Self {
        Self { downloaded, total }
    }

    pub fn __repr__(&self) -> String {
        let total = match self.total {
            None => "None".to_string(),
            Some(x) => x.to_string(),
        };
        format!(
            "ProgressUpdate(downloaded={}, total={})",
            self.downloaded, total
        )
    }
}

#[pymethods]
impl PyClient {
    #[pyo3(signature = (
        downloadable,
        *,
        chunk_size=MAX_CHUNK_SIZE,
        skip_chunks=0,
        limit=0
    ))]
    pub async fn iter_download(
        &self,
        downloadable: Downloadable,
        chunk_size: i32,
        skip_chunks: i32,
        limit: i32,
    ) -> PyResult<Py<PyDownloadIter>> {
        let iter = PyDownloadIter::new(self.clone(), downloadable, chunk_size, skip_chunks, limit)?;
        Python::attach(|py| Py::new(py, iter))
    }

    #[pyo3(signature = (
        downloadable,
        path,
        *,
        chunk_size=MAX_CHUNK_SIZE,
        progress_callback=None,
    ))]
    pub async fn download_media(
        &self,
        downloadable: Downloadable,
        path: String,
        chunk_size: i32,
        progress_callback: Option<Py<PyAny>>,
    ) -> PyResult<()> {
        if !((MIN_CHUNK_SIZE..=MAX_CHUNK_SIZE).contains(&chunk_size)
            && chunk_size % MIN_CHUNK_SIZE == 0)
        {
            return Err(PyValueError::new_err(
                "chunk_size must be between [4 * 1024, 512 * 1024] and divisible by 4 * 1024.",
            ));
        }
        if let Some(ref p) = progress_callback {
            let is_callable = Python::attach(|py| p.bind(py).is_callable());
            if !is_callable {
                return Err(PyValueError::new_err(
                    "progress_callback must be a callable or None.",
                ));
            }
        }

        let dc_id = downloadable.dc_id();
        let size = downloadable.size();

        if let Some(location) = downloadable.into_raw_input_location() {
            let mut iter = DownloadIter::new(
                self.clone(),
                DownloadIterVariant::Request(location),
                chunk_size,
                0,
                0,
                dc_id,
                size,
            );
            let mut downloaded: i64 = 0;
            let progress_callback_provided = progress_callback.is_some();
            let mut last_update = std::time::Instant::now();
            let (tx, mut rx) = mpsc::channel(1);
            let shared_error = Arc::new(Mutex::new(None::<PyErr>));
            let shared_error_for_bg = Arc::clone(&shared_error);

            if let Some(p) = progress_callback {
                get_runtime().spawn(async move {
                    while let Some((downloaded, total)) = rx.recv().await {
                        let res: PyResult<()> = async {
                            let res = Python::attach(|py| {
                                let update = PyProgressUpdate { downloaded, total };
                                let update = Py::new(py, update)?;
                                Ok::<_, PyErr>(p.bind(py).call1((update,))?.unbind())
                            })?;
                            maybe_await(res).await?;
                            Ok(())
                        }
                        .await;

                        if let Err(e) = res {
                            let mut guard = shared_error_for_bg.lock().await;
                            *guard = Some(e);
                            break;
                        }
                    }
                });
            }

            let res: PyResult<()> = get_runtime()
                .spawn(async move {
                    let mut file = fs::File::create(path).await?;
                    while let Some(chunk) = iter
                        .next()
                        .await
                        .map_err(|e| PyIOError::new_err(e.to_string()))?
                    {
                        if let Some(err) = shared_error.lock().await.take() {
                            return Err(err);
                        }

                        file.write_all(&chunk).await?;
                        downloaded += chunk.len() as i64;

                        if progress_callback_provided {
                            if last_update.elapsed().as_millis() > 100 {
                                if let Ok(_) = tx.try_send((downloaded, size)) {
                                    last_update = std::time::Instant::now();
                                }
                            }
                        }
                    }
                    Ok(())
                })
                .await
                .map_err(|_| PyRuntimeError::new_err("JoinHandle fail"))?;
            res?;

            Ok(())
        } else {
            Err(PyValueError::new_err("this media not downloadable."))
        }
    }
}
