use pyo3::exceptions::PyRuntimeError;
use pyo3::{Py, PyErr, PyResult, Python};

use grammers_tl_types as tl;

use crate::client::IterBuffer;
use crate::errors::PyInvocationError;
use crate::message::PyMessage;

pub const MAX_LIMIT: usize = 100;

impl<R: tl::RemoteCall<Return = tl::enums::messages::Messages>> IterBuffer<R, Py<PyMessage>> {
    /// Fetches the total unless cached.
    ///
    /// The `request.limit` should be set to the right value before calling this method.
    pub(crate) async fn get_total(&mut self) -> PyResult<usize> {
        if let Some(total) = self.total {
            return Ok(total);
        }

        use tl::enums::messages::Messages;

        let total = match self
            .client
            .invoke(&self.request)
            .await
            .map_err(PyInvocationError::new)?
        {
            Messages::Messages(messages) => messages.messages.len(),
            Messages::Slice(messages) => messages.count as usize,
            Messages::ChannelMessages(messages) => messages.count as usize,
            Messages::NotModified(messages) => messages.count as usize,
        };
        self.total = Some(total);
        Ok(total)
    }

    /// Performs the network call, fills the buffer, and returns the `offset_rate` if any.
    ///
    /// The `request.limit` should be set to the right value before calling this method.
    pub(crate) async fn fill_buffer(&mut self, limit: i32) -> PyResult<Option<i32>> {
        use tl::enums::messages::Messages;

        let (messages, users, chats, rate) = match self
            .client
            .invoke(&self.request)
            .await
            .map_err(PyInvocationError::new)?
        {
            Messages::Messages(m) => {
                self.last_chunk = true;
                self.total = Some(m.messages.len());
                (m.messages, m.users, m.chats, None)
            }
            Messages::Slice(m) => {
                // Can't rely on `count(messages) < limit` as the stop condition.
                // See https://github.com/LonamiWebs/Telethon/issues/3949 for more.
                //
                // If the highest fetched message ID is lower than or equal to the limit,
                // there can't be more messages after (highest ID - limit), because the
                // absolute lowest message ID is 1.
                self.last_chunk = m.messages.is_empty() || m.messages[0].id() <= limit;
                self.total = Some(m.count as usize);
                (m.messages, m.users, m.chats, m.next_rate)
            }
            Messages::ChannelMessages(m) => {
                self.last_chunk = m.messages.is_empty() || m.messages[0].id() <= limit;
                self.total = Some(m.count as usize);
                (m.messages, m.users, m.chats, None)
            }
            Messages::NotModified(_) => {
                return Err(PyRuntimeError::new_err(
                    "API returned Messages::NotModified even though hash = 0",
                ));
            }
        };

        let peers = self.client.build_peer_map(users, chats).await?;

        let client = self.client.clone();
        Python::attach(|py| {
            self.buffer.extend(
                messages
                    .into_iter()
                    .map(|message| {
                        Py::new(py, PyMessage::from_raw(&client, message, peers.handle())?)
                    })
                    .collect::<Result<Vec<_>, _>>()?,
            );
            Ok::<_, PyErr>(())
        })?;

        Ok(rate)
    }
}
