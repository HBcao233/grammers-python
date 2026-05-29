use std::sync::Arc;
use tokio::sync::Mutex;

use pyo3::exceptions::{PyStopAsyncIteration, PyValueError};
use pyo3::prelude::*;

use grammers_tl_types as tl;

use super::MAX_LIMIT;
use crate::client::{IterBuffer, PyClient};
use crate::errors::PyInvocationError;
use crate::hints::InputPeerLike;
use crate::message::PyMessage;

/// Iterator returned by [`Client::iter_history_messages`].
pub struct HistoryMessageIter {
    inner: IterBuffer<tl::functions::messages::GetHistory, Py<PyMessage>>,
    reverse: bool,
}

impl HistoryMessageIter {
    pub(crate) fn new(
        client: &PyClient,
        peer: tl::enums::InputPeer,
        limit: Option<usize>,
        offset_id: i32,
        offset_date: i32,
        add_offset: i32,
        page_limit: i32,
        max_id: i32,
        min_id: i32,
        reverse: bool,
    ) -> Self {
        let inner = IterBuffer::from_request(
            client,
            MAX_LIMIT,
            limit,
            tl::functions::messages::GetHistory {
                peer,
                offset_id,
                offset_date,
                add_offset,
                limit: page_limit,
                max_id,
                min_id,
                hash: 0,
            },
        );
        Self { inner, reverse }
    }

    pub async fn total(&mut self) -> PyResult<usize> {
        self.inner.request.limit = 1;
        self.inner.get_total().await
    }

    pub async fn next(&mut self) -> PyResult<Option<Py<PyMessage>>> {
        if let Some(result) = self.inner.next_raw() {
            return result.map_err(PyInvocationError::new);
        }

        self.inner.request.limit = self.inner.determine_limit(MAX_LIMIT);
        let request = &mut self.inner.request;
        if self.reverse {
            request.add_offset = -request.limit;
            request.min_id = request.offset_id;
            if request.offset_id == 0 && request.offset_date == 0 {
                // With no explicit offset, start from the oldest available page.
                request.offset_id = 1;
                request.add_offset = -request.limit + 1; // +1 to include the first message (ID=1)
            }
        }
        self.inner
            .fill_buffer(self.inner.request.limit, self.reverse)
            .await?;

        // Don't bother updating offsets if this is the last time stuff has to be fetched.
        if !self.inner.last_chunk && !self.inner.buffer.is_empty() {
            let last = &self.inner.buffer[self.inner.buffer.len() - 1];
            let (id, date_timestamp) = Python::attach(|py| {
                let borrowed = last.borrow(py);
                (borrowed.id, borrowed.date_timestamp.unwrap_or(0))
            });
            self.inner.request.offset_id = id;
            self.inner.request.offset_date = date_timestamp;
        }

        Ok(self.inner.pop_item())
    }
}

#[derive(Clone)]
#[pyclass(
    skip_from_py_object,
    name = "HistoryMessageIter",
    module = "grammers.custom"
)]
pub struct PyHistoryMessageIter {
    pub(crate) peer: Option<InputPeerLike>,
    pub(crate) iter: Arc<Mutex<HistoryMessageIter>>,
}

#[pymethods]
impl PyHistoryMessageIter {
    #[new]
    #[pyo3(signature = (
        client,
        peer,
        limit=None,
        *,
        offset_id=0,
        offset_date=0,
        add_offset=0,
        page_limit=0,
        max_id=0,
        min_id=0,
        reverse=false,
    ))]
    pub(crate) fn new(
        client: PyClient,
        peer: InputPeerLike,
        limit: Option<usize>,
        offset_id: i32,
        offset_date: i32,
        add_offset: i32,
        page_limit: i32,
        max_id: i32,
        min_id: i32,
        reverse: bool,
    ) -> Self {
        Self {
            peer: Some(peer),
            iter: Arc::new(Mutex::new(HistoryMessageIter::new(
                &client,
                tl::types::InputPeerEmpty {}.into(),
                limit,
                offset_id,
                offset_date,
                add_offset,
                page_limit,
                max_id,
                min_id,
                reverse,
            ))),
        }
    }

    fn __aiter__(slf: PyRef<'_, Self>) -> PyRef<'_, Self> {
        slf
    }

    fn __anext__(slf: Bound<'_, Self>) -> PyResult<Py<PyAny>> {
        slf.call_method0("next").map(|x| x.unbind())
    }

    async fn init(&mut self) -> PyResult<()> {
        let mut iter = self.iter.lock().await;
        if let Some(p) = self.peer.take() {
            let peer_string = p.stringify()?;
            let peer = iter
                .inner
                .client
                .resolve_peer_ref(p)
                .await?
                .ok_or_else(|| {
                    PyValueError::new_err(format!("peer {} can't resolve to PeerRef.", peer_string))
                })?;
            iter.inner.request.peer = peer.into();
        }
        Ok(())
    }

    /// Determines how many messages there are in total.
    ///
    /// This only performs a network call if `next` has not been called before.
    async fn total(&mut self) -> PyResult<usize> {
        self.init().await?;
        let mut iter = self.iter.lock().await;
        iter.total().await
    }

    /// Returns the next `Message` from the internal buffer, filling the buffer previously if it's
    /// empty.
    ///
    /// Returns `None` if the `limit` is reached or there are no messages left.
    async fn next(&mut self) -> PyResult<Py<PyMessage>> {
        self.init().await?;
        let mut iter = self.iter.lock().await;
        match iter.next().await? {
            None => Err(PyStopAsyncIteration::new_err(())),
            Some(m) => Ok(m),
        }
    }
}
