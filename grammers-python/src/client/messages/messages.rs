use std::collections::HashMap;

use pyo3::exceptions::{PyRuntimeError, PyValueError};
use pyo3::prelude::*;

use grammers_session_pyo3::PyPeerKind;
use grammers_tl_types as tl;

use super::PyHistoryMessageIter;
use crate::client::PyClient;
use crate::errors::PyInvocationError;
use crate::hints::InputPeerLike;
use crate::message::PyMessage;

#[pymethods]
impl PyClient {
    /// Get messages by id
    ///
    /// Both users and bots can use this method.
    ///
    /// Example
    ///     .. code-block:: python
    ///
    ///         messages = await client.get_messages_by_id(peer, [123])
    pub async fn get_messages_by_id(
        &self,
        peer: InputPeerLike,
        message_ids: Vec<i32>,
    ) -> PyResult<Vec<Option<Py<PyMessage>>>> {
        let peer_string = peer.stringify()?;
        let peer = self.resolve_peer_ref(peer).await?.ok_or_else(|| {
            PyValueError::new_err(format!("peer {} can't resolve to PeerRef.", peer_string))
        })?;
        let id = message_ids
            .iter()
            .map(|&id| tl::enums::InputMessage::Id(tl::types::InputMessageId { id }))
            .collect();

        let peer_id = peer.id();
        let access_hash = peer.auth().0;
        let result = if peer_id.kind() == PyPeerKind::Channel {
            self.invoke(&tl::functions::channels::GetMessages {
                channel: tl::types::InputChannel {
                    channel_id: peer_id.bare_id()?,
                    access_hash,
                }
                .into(),
                id,
            })
            .await
        } else {
            self.invoke(&tl::functions::messages::GetMessages { id })
                .await
        }
        .map_err(PyInvocationError::new)?;

        let (messages, users, chats) = match result {
            tl::enums::messages::Messages::Messages(m) => (m.messages, m.users, m.chats),
            tl::enums::messages::Messages::Slice(m) => (m.messages, m.users, m.chats),
            tl::enums::messages::Messages::ChannelMessages(m) => (m.messages, m.users, m.chats),
            tl::enums::messages::Messages::NotModified(_) => {
                return Err(PyRuntimeError::new_err(
                    "API returned Messages::NotModified even though GetMessages was used",
                ));
            }
        };

        let peers = self.build_peer_map(users, chats).await?;
        let mut map = Python::attach(|py| {
            Ok::<_, PyErr>(
                messages
                    .into_iter()
                    .map(|m| Py::new(py, PyMessage::from_raw(self, m, peers.handle())?))
                    .collect::<Result<Vec<_>, _>>()?
                    .into_iter()
                    .filter(|m| m.borrow(py).peer_id == Some(peer.id()))
                    .map(|m| {
                        let id = m.borrow(py).id;
                        (id, m)
                    })
                    .collect::<HashMap<_, _>>(),
            )
        })?;

        Ok(message_ids.iter().map(|id| map.remove(id)).collect())
    }

    /// Returns the conversation history with one interlocutor / within a chat
    ///
    /// Only users can use this method
    ///
    /// Example
    ///     .. code-block:: python
    ///
    ///         # Get the latest message of Telegram.
    ///         async for m in client.iter_history_messages(777000, limit=1)
    ///             print(m.date)
    ///             print(m.message)
    ///
    ///         # Or without using async for
    ///         iterator = client.iter_history_messages(
    ///             777000,
    ///             limit=None,
    ///         )
    ///         # Determines how many messages there are in total.
    ///         print(await iterator.total())
    ///         # Get the next `Message`.
    ///         print(await iterator.next())  # or await anext(iterator)
    #[pyo3(signature = (
        peer,
        limit=None,
        *,
        offset_id=0,
        offset_date=0,
        add_offset=0,
        page_limit=0,
        max_id=0,
        min_id=0,
    ))]
    pub fn iter_history_messages(
        &self,
        peer: InputPeerLike,
        limit: Option<usize>,
        offset_id: i32,
        offset_date: i32,
        add_offset: i32,
        page_limit: i32,
        max_id: i32,
        min_id: i32,
    ) -> PyResult<Py<PyHistoryMessageIter>> {
        let res = PyHistoryMessageIter::new(
            self.clone(),
            peer,
            limit,
            offset_id,
            offset_date,
            add_offset,
            page_limit,
            max_id,
            min_id,
        );
        Python::attach(|py| Py::new(py, res))
    }

    /*pub fn send_messages(
        &self,
        entity: EntityLike,
        message: InputMessageLike,
    ) -> pytl::types::PyMessage {

    }*/

    // edit_message
    // delete_messages
    // forward_messages
    // get_reply_to_message
}
