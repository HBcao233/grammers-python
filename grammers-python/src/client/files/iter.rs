use std::convert::TryInto;
use std::mem;
use std::sync::Arc;
use tokio::sync::Mutex;

use pyo3::exceptions::{PyStopAsyncIteration, PyValueError};
use pyo3::prelude::*;
use pyo3::types::{PyByteArray, PyByteArrayMethods};

use grammers_mtsender_pyo3::InvocationError;
use grammers_tl_types as tl;

use super::{MAX_CHUNK_SIZE, MIN_CHUNK_SIZE};
use crate::client::PyClient;
use crate::errors::PyInvocationError;
use crate::media::Downloadable;

const FILE_MIGRATE_ERROR: i32 = 303;

/// Iterator returned by [`Client::iter_download`].
pub struct DownloadIter {
    pub client: PyClient,
    pub done: bool,
    pub variant: DownloadIterVariant,
}

pub enum DownloadIterVariant {
    Request(tl::functions::upload::GetFile),
    PreDownloaded(Vec<u8>),
    Empty,
}

impl DownloadIter {
    /// Fetch and return the next chunk.
    pub async fn next(&mut self) -> Result<Option<Vec<u8>>, InvocationError> {
        if self.done {
            return Ok(None);
        }

        let variant = mem::replace(&mut self.variant, DownloadIterVariant::Empty);

        let mut request = match variant {
            DownloadIterVariant::Request(r) => r,
            DownloadIterVariant::PreDownloaded(data) => {
                self.done = true;
                return Ok(Some(data.clone()));
            }
            DownloadIterVariant::Empty => return Ok(None),
        };

        use tl::enums::upload::File;

        // TODO handle maybe FILEREF_UPGRADE_NEEDED
        let inner = self.client.inner.clone();
        let mut dc = inner
            .session
            .home_dc_id()
            .await
            .map_err(InvocationError::PyErr)?;
        loop {
            break match self.client.invoke_in_dc(dc, &request).await {
                Ok(File::File(f)) => {
                    if f.bytes.len() < request.limit as usize {
                        self.done = true;
                        if f.bytes.is_empty() {
                            break Ok(None);
                        }
                    }

                    request.offset += request.limit as i64;
                    self.variant = DownloadIterVariant::Request(request);

                    Ok(Some(f.bytes))
                }
                Ok(File::CdnRedirect(_)) => {
                    panic!("API returned File::CdnRedirect even though cdn_supported = false");
                }
                Err(InvocationError::Rpc(err)) if &err.name == "AUTH_KEY_UNREGISTERED" => {
                    match self.client.copy_auth_to_dc(dc).await {
                        Ok(_) => continue,
                        Err(e) => Err(e),
                    }
                }
                Err(InvocationError::Rpc(err)) if err.code == FILE_MIGRATE_ERROR => {
                    dc = err.value.unwrap() as _;
                    continue;
                }
                Err(e) => Err(e),
            };
        }
    }
}

#[pyclass(skip_from_py_object, name = "DownloadIter", module = "grammers.custom")]
pub struct PyDownloadIter {
    pub(crate) iter: Arc<Mutex<DownloadIter>>,
    buf: Py<PyByteArray>,
}

#[pymethods]
impl PyDownloadIter {
    #[new]
    #[pyo3(signature = (
        client,
        downloadable,
        *,
        chunk_size=MAX_CHUNK_SIZE,
        skip_chunks=0,
    ))]
    pub(crate) fn new(
        client: PyClient,
        downloadable: Downloadable,
        chunk_size: i32,
        skip_chunks: i32,
    ) -> PyResult<Self> {
        if !((MIN_CHUNK_SIZE..=MAX_CHUNK_SIZE).contains(&chunk_size)
            && chunk_size % MIN_CHUNK_SIZE == 0)
        {
            return Err(PyValueError::new_err(
                "chunk_size must be between [4 * 1024, 512 * 1024] and divisible by 4 * 1024.",
            ));
        }

        if let Some(location) = downloadable.into_raw_input_location() {
            let buf = Python::attach(|py| {
                Ok::<_, PyErr>(
                    PyByteArray::new(
                        py,
                        &vec![
                            0;
                            chunk_size
                                .try_into()
                                .map_err(|e: std::num::TryFromIntError| PyValueError::new_err(
                                    e.to_string()
                                ))?
                        ],
                    )
                    .unbind(),
                )
            })?;
            Ok(PyDownloadIter {
                iter: Arc::new(Mutex::new(DownloadIter {
                    client,
                    done: false,
                    variant: DownloadIterVariant::Request(tl::functions::upload::GetFile {
                        precise: false,
                        cdn_supported: false,
                        location,
                        offset: chunk_size as i64 * (skip_chunks as i64),
                        limit: chunk_size,
                    }),
                })),
                buf,
            })
        } else {
            Err(PyValueError::new_err("this media not downloadable."))
        }
    }

    fn __aiter__(slf: PyRef<'_, Self>) -> PyRef<'_, Self> {
        slf
    }

    fn __anext__(slf: Bound<'_, Self>) -> PyResult<Py<PyAny>> {
        slf.call_method0("next").map(|x| x.unbind())
    }

    /// Returns the next `Message` from the internal buffer, filling the buffer previously if it's
    /// empty.
    ///
    /// Returns `None` if the `limit` is reached or there are no messages left.
    async fn next(&mut self) -> PyResult<Py<PyByteArray>> {
        let mut iter = self.iter.lock().await;
        match iter.next().await.map_err(PyInvocationError::new)? {
            None => Err(PyStopAsyncIteration::new_err(())),
            Some(data) => {
                let buf = Python::attach(|py| {
                    let buf = self.buf.bind(py);
                    if buf.len() != data.len() {
                        buf.resize(data.len())?;
                    }
                    unsafe {
                        let buf_slice = buf.as_bytes_mut();
                        buf_slice.copy_from_slice(&data);
                    }
                    Ok::<_, PyErr>(buf.clone().unbind())
                })?;
                Ok(buf)
            }
        }
    }
}
