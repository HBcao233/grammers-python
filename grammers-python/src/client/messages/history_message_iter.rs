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
pub type HistoryMessageIter = IterBuffer<tl::functions::messages::GetHistory, Py<PyMessage>>;

impl HistoryMessageIter {
    pub(crate) fn new(
        client: &PyClient,
        peer: tl::enums::InputPeer,
        offset_id: i32,
        offset_date: i32,
        add_offset: i32,
        limit: Option<usize>,
        page_limit: i32,
        max_id: i32,
        min_id: i32,
    ) -> Self {
        Self::from_request(
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
        )
    }

    pub async fn total(&mut self) -> PyResult<usize> {
        self.request.limit = 1;
        self.get_total().await
    }

    pub async fn next(&mut self) -> PyResult<Option<Py<PyMessage>>> {
        if let Some(result) = self.next_raw() {
            return result.map_err(PyInvocationError::new);
        }

        self.request.limit = self.determine_limit(MAX_LIMIT);
        self.fill_buffer(self.request.limit).await?;

        // Don't bother updating offsets if this is the last time stuff has to be fetched.
        if !self.last_chunk && !self.buffer.is_empty() {
            let last = &self.buffer[self.buffer.len() - 1];
            let (id, date_timestamp) = Python::attach(|py| {
                let borrowed = last.borrow(py);
                (borrowed.id, borrowed.date_timestamp.unwrap_or(0))
            });
            self.request.offset_id = id;
            self.request.offset_date = date_timestamp;
        }

        Ok(self.pop_item())
    }
}

#[derive(Clone)]
#[pyclass(name = "HistoryMessageIter", module = "grammers.client")]
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
        *,
        offset_id=0,
        offset_date=0,
        add_offset=0,
        limit=None,
        page_limit=0,
        max_id=0,
        min_id=0,
    ))]
    pub(crate) fn new(
        client: PyClient,
        peer: InputPeerLike,
        offset_id: i32,
        offset_date: i32,
        add_offset: i32,
        limit: Option<usize>,
        page_limit: i32,
        max_id: i32,
        min_id: i32,
    ) -> Self {
        Self {
            peer: Some(peer),
            iter: Arc::new(Mutex::new(HistoryMessageIter::new(
                &client,
                tl::types::InputPeerEmpty {}.into(),
                offset_id,
                offset_date,
                add_offset,
                limit,
                page_limit,
                max_id,
                min_id,
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
            let peer = iter.client.resolve_peer_ref(p).await?.ok_or_else(|| {
                PyValueError::new_err(format!("peer {} can't resolve to PeerRef.", peer_string))
            })?;
            iter.request.peer = peer.into();
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
