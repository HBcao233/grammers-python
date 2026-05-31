use tokio::fs;
use tokio::io::AsyncWriteExt;

use pyo3::exceptions::{PyIOError, PyRuntimeError, PyValueError};
use pyo3::prelude::*;

use super::{DownloadIter, DownloadIterVariant, PyDownloadIter};
use crate::client::PyClient;
use crate::media::Downloadable;

pub const MIN_CHUNK_SIZE: i32 = 4 * 1024;
pub const MAX_CHUNK_SIZE: i32 = 512 * 1024;

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

    pub async fn download_media(&self, downloadable: Downloadable, path: String) -> PyResult<()> {
        let dc_id = downloadable.dc_id();
        let size = downloadable.size();

        if let Some(location) = downloadable.into_raw_input_location() {
            let mut iter = DownloadIter::new(
                self.clone(),
                DownloadIterVariant::Request(location),
                MAX_CHUNK_SIZE,
                0,
                0,
                dc_id,
                size,
            );

            let res: PyResult<()> = pyo3_async_runtimes::tokio::get_runtime()
                .spawn(async move {
                    let mut file = fs::File::create(path).await?;
                    while let Some(chunk) = iter
                        .next()
                        .await
                        .map_err(|e| PyIOError::new_err(e.to_string()))?
                    {
                        file.write_all(&chunk).await?;
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
