use pyo3::prelude::*;

use super::PyClient;
//use grammers_tl_types as tl;
//use grammers_tl_types_pyo3 as pytl;

// use crate::message::PyMessage;

#[derive(Clone)]
#[pyclass(name = "HistoryMessageIter", module = "grammers.client")]
pub struct PyHistoryMessageIter {}

#[pymethods]
impl PyHistoryMessageIter {
    #[new]
    fn new() -> Self {
        Self {}
    }

    fn __aiter__(slf: PyRef<'_, Self>) -> PyRef<'_, Self> {
        slf
    }

    fn __anext__(slf: &Bound<'_, Self>) -> PyResult<Py<PyAny>> {
        Ok(slf.getattr("next")?.unbind())
    }

    async fn next(&self) -> PyResult<Py<PyAny>> {
        todo!()
    }
}

#[pymethods]
impl PyClient {
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

    /*pub async fn get_messages(
        &self,
        entity: EntityLike,
        message_ids: Vec<i32>,
    ) -> PyResult<Vec<Option<PyMessage>>> {
        let peer = peer.into();
        let id = message_ids
            .iter()
            .map(|&id| tl::enums::InputMessage::Id(tl::types::InputMessageId { id }))
            .collect();

        let result = if peer.id.kind() == PeerKind::Channel {
            self.invoke(&tl::functions::channels::GetMessages {
                channel: peer.into(),
                id,
            })
            .await
        } else {
            self.invoke(&tl::functions::messages::GetMessages { id })
                .await
        }?;

        let (messages, users, chats) = match result {
            tl::enums::messages::Messages::Messages(m) => (m.messages, m.users, m.chats),
            tl::enums::messages::Messages::Slice(m) => (m.messages, m.users, m.chats),
            tl::enums::messages::Messages::ChannelMessages(m) => (m.messages, m.users, m.chats),
            tl::enums::messages::Messages::NotModified(_) => {
                return Err(PyValueError::new_err("API returned types.messages.MessagesNotModified even though GetMessages was used"))
            }
        };

        let peers = self.build_peer_map(users, chats).await?;
        let mut map = messages
            .into_iter()
            .map(|m| PyMessage::from_raw(self, m, Some(peer.into()), peers.handle()))
            .filter(|m| m.peer_id() == peer.id)
            .map(|m| (m.id(), m))
            .collect::<HashMap<_, _>>();

        Ok(message_ids.iter().map(|id| map.remove(id)).collect())
    }*/

    /*
    pub fn iter_history_messages(
        &self,
        entity: EntityLike,
        offset_id: usize,
        offset_date: usize,
        add_offset: usize,
        limit: usize,
        max_id: usize,
        min_id: usize,
        hash: usize,
    ) -> {

    }*/
}
