use futures::stream::{self, BoxStream, StreamExt};
use std::convert::TryInto;
use std::mem;
use std::sync::Arc;
use tokio::sync::Mutex;

use pyo3::exceptions::{PyRuntimeError, PyStopAsyncIteration, PyValueError};
use pyo3::prelude::*;
use pyo3::types::{PyByteArray, PyByteArrayMethods};

use grammers_mtsender_pyo3::InvocationError;
use grammers_tl_types as tl;

use super::{MAX_CHUNK_SIZE, MIN_CHUNK_SIZE};
use crate::client::PyClient;
use crate::errors::PyInvocationError;
use crate::media::Downloadable;

const FILE_MIGRATE_ERROR: i32 = 303;
const CONCURRENCY: usize = 2;

struct ChunkResult {
    data: Option<Vec<u8>>,
    done: bool,
    dc_id: i32,
}

/// Iterator returned by [`Client::iter_download`].
pub struct DownloadIter {
    client: PyClient,
    done: bool,
    variant: DownloadIterVariant,
    chunk_size: i32,
    skip_chunks: i32,
    limit: i32,

    dc_id: Option<i32>,
    size: Option<i64>,
    stream: Option<BoxStream<'static, PyResult<ChunkResult>>>,
}

pub enum DownloadIterVariant {
    Request(tl::enums::InputFileLocation),
    PreDownloaded(Vec<u8>),
    Empty,
}

async fn download_single_chunk(
    client: PyClient,
    mut dc_id: i32,
    location: tl::enums::InputFileLocation,
    chunk_size: i32,
    index: i64,
) -> PyResult<ChunkResult> {
    let request = tl::functions::upload::GetFile {
        precise: false,
        cdn_supported: false,
        location,
        offset: chunk_size as i64 * (index as i64),
        limit: chunk_size,
    };

    use tl::enums::upload::File;

    // TODO handle maybe FILEREF_UPGRADE_NEEDED
    loop {
        break match client.invoke_in_dc(dc_id, &request).await {
            Ok(File::File(f)) => {
                if f.bytes.len() < request.limit as usize {
                    if f.bytes.is_empty() {
                        break Ok(ChunkResult {
                            data: None,
                            done: true,
                            dc_id,
                        });
                    }
                }

                Ok(ChunkResult {
                    data: Some(f.bytes),
                    done: false,
                    dc_id,
                })
            }
            Ok(File::CdnRedirect(_)) => Err(PyRuntimeError::new_err(
                "API returned File::CdnRedirect even though cdn_supported = false",
            )),
            Err(InvocationError::Rpc(err)) if &err.name == "AUTH_KEY_UNREGISTERED" => {
                match client.copy_auth_to_dc(dc_id).await {
                    Ok(_) => continue,
                    Err(e) => Err(PyInvocationError::new(e)),
                }
            }
            Err(InvocationError::Rpc(err)) if err.code == FILE_MIGRATE_ERROR => {
                dc_id = err.value.ok_or_else(|| {
                    PyRuntimeError::new_err("got FILE_MIGRATE_ERROR, but no dc_id received.")
                })? as i32;
                continue;
            }
            Err(e) => Err(PyInvocationError::new(e)),
        };
    }
}

impl DownloadIter {
    pub fn new(
        client: PyClient,
        variant: DownloadIterVariant,
        chunk_size: i32,
        skip_chunks: i32,
        limit: i32,
        dc_id: Option<i32>,
        size: Option<i64>,
    ) -> Self {
        Self {
            client,
            done: false,
            variant,
            chunk_size,
            skip_chunks,
            limit,
            dc_id,
            size,
            stream: None,
        }
    }

    /// Fetch and return the next chunk.
    pub async fn next(&mut self) -> PyResult<Option<Vec<u8>>> {
        if self.done {
            return Ok(None);
        }

        match &mut self.stream {
            None => {
                let variant = mem::replace(&mut self.variant, DownloadIterVariant::Empty);

                let location = match variant {
                    DownloadIterVariant::Request(l) => l,
                    DownloadIterVariant::PreDownloaded(data) => {
                        self.done = true;
                        return Ok(Some(data));
                    }
                    DownloadIterVariant::Empty => return Ok(None),
                };

                let home_dc_id = self.client.inner.session.home_dc_id().await?;
                let dc_id = self.dc_id.unwrap_or(home_dc_id);
                if dc_id != home_dc_id {
                    self.client
                        .copy_auth_to_dc(dc_id)
                        .await
                        .map_err(PyInvocationError::new)?;
                }

                let index = self.skip_chunks as i64;
                let ChunkResult {
                    data,
                    mut done,
                    dc_id,
                } = download_single_chunk(
                    self.client.clone(),
                    dc_id,
                    location.clone(),
                    self.chunk_size,
                    index,
                )
                .await?;
                if self.limit == 1 {
                    done = true;
                }
                self.done = done;
                self.dc_id = Some(dc_id);

                if !done {
                    let limit_i64 = self.limit as i64;
                    let range: Box<dyn Iterator<Item = i64> + Send> = if limit_i64 > 0 {
                        Box::new((index + 1)..(index + limit_i64))
                    } else if let Some(size) = self.size {
                        // let limit = size.div_ceil(self.chunk_size);
                        let limit = if size == 0 {
                            0
                        } else {
                            (size - 1) / (self.chunk_size as i64) + 1
                        };
                        Box::new((index + 1)..(index + limit))
                    } else {
                        Box::new((index + 1)..)
                    };
                    let client = self.client.clone();
                    let chunk_size = self.chunk_size;
                    self.stream = Some(
                        stream::iter(range)
                            .map(move |index| {
                                download_single_chunk(
                                    client.clone(),
                                    dc_id,
                                    location.clone(),
                                    chunk_size,
                                    index,
                                )
                            })
                            .buffered(CONCURRENCY)
                            .boxed(),
                    );
                }

                return Ok(data);
            }
            &mut Some(ref mut stream) => match stream.next().await {
                Some(x) => {
                    let ChunkResult { data, done, dc_id } = x?;
                    self.done = done;
                    self.dc_id = Some(dc_id);
                    Ok(data)
                }
                None => Ok(None),
            },
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
        limit=0,
    ))]
    pub(crate) fn new(
        client: PyClient,
        downloadable: Downloadable,
        chunk_size: i32,
        skip_chunks: i32,
        limit: i32,
    ) -> PyResult<Self> {
        if !((MIN_CHUNK_SIZE..=MAX_CHUNK_SIZE).contains(&chunk_size)
            && chunk_size % MIN_CHUNK_SIZE == 0)
        {
            return Err(PyValueError::new_err(
                "chunk_size must be between [4 * 1024, 512 * 1024] and divisible by 4 * 1024.",
            ));
        }
        if skip_chunks < 0 {
            return Err(PyValueError::new_err("skip_chunks must be >= 0."));
        }
        if limit < 0 {
            return Err(PyValueError::new_err("limit must be >= 0."));
        }

        let dc_id = downloadable.dc_id();
        let size = downloadable.size();

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
                iter: Arc::new(Mutex::new(DownloadIter::new(
                    client,
                    DownloadIterVariant::Request(location),
                    chunk_size,
                    skip_chunks,
                    limit,
                    dc_id,
                    size,
                ))),
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
        match iter.next().await? {
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
