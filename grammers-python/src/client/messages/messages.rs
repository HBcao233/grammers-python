use std::collections::HashMap;

use pyo3::exceptions::{PyRuntimeError, PyValueError};
use pyo3::prelude::*;

use grammers_session_pyo3::PyPeerKind;
use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

use super::{PyHistoryMessageIter, parse_mention_entities};
use crate::client::PyClient;
use crate::errors::PyInvocationError;
use crate::hints::{InputPeerLike, InputMessageLike, InputReplyToLike};
use crate::message::{PyMessage, InputMessage};
use crate::peer::{PyPeer, PyPeerMap};


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

    #[pyo3(signature = (
        peer,
        message,
        *,
        media=None,
        entities=vec![],
        reply_to=None,
        reply_markup=None,
        schedule_date=None,
        send_as=None,
        no_webpage=None,
        silent=None,
        background=None,
        clear_draft=None,
        noforwards=None,
        update_stickersets_order=None,
        invert_media=None,
        allow_paid_floodskip=None,
        quick_reply_shortcut=None,
        effect=None,
        allow_paid_stars=None,
        suggested_post=None,
    ))]
    pub async fn send_message(
        &self,
        peer: InputPeerLike,
        message: InputMessageLike,
        media: Option<pytl::enums::PyInputMedia>,
        entities: Vec<pytl::enums::PyMessageEntity>,
        reply_to: Option<InputReplyToLike>,
        reply_markup: Option<pytl::enums::PyReplyMarkup>,
        schedule_date: Option<i32>,
        send_as: Option<InputPeerLike>,
        no_webpage: Option<bool>,
        silent: Option<bool>,
        background: Option<bool>,
        clear_draft: Option<bool>,
        noforwards: Option<bool>,
        update_stickersets_order: Option<bool>,
        invert_media: Option<bool>,
        allow_paid_floodskip: Option<bool>,
        quick_reply_shortcut: Option<pytl::enums::PyInputQuickReplyShortcut>,
        effect: Option<i64>,
        allow_paid_stars: Option<i64>,
        suggested_post: Option<pytl::enums::PySuggestedPost>,
    ) -> PyResult<Option<Py<PyMessage>>> {
        let x: InputMessage = message.into_input_message().await;
        let media: Option<tl::enums::InputMedia> = media.map(Into::into);
        let reply_markup: Option<tl::enums::ReplyMarkup> = reply_markup.map(Into::into);
        let quick_reply_shortcut: Option<tl::enums::InputQuickReplyShortcut> = quick_reply_shortcut.map(Into::into);
        let suggested_post: Option<tl::enums::SuggestedPost> = suggested_post.map(Into::into);
        let (
            message,
            media,
            entities,
            reply_to,
            reply_markup,
            schedule_date,
            send_as,
            no_webpage,
            silent,
            background,
            clear_draft,
            noforwards,
            update_stickersets_order,
            invert_media,
            allow_paid_floodskip,
            quick_reply_shortcut,
            effect,
            allow_paid_stars,
            suggested_post,
        ) = (
            x.message,
            media.or(x.media),
            if entities.is_empty() {
                x.entities
            } else {
                entities.into_iter().map(Into::into).collect()
            },
            reply_to.or(x.reply_to.map(Into::into)),
            reply_markup.or(x.reply_markup),
            schedule_date.or(x.schedule_date),
            send_as.or(x.send_as),
            no_webpage.unwrap_or(x.no_webpage),
            silent.unwrap_or(x.silent),
            background.unwrap_or(x.background),
            clear_draft.unwrap_or(x.clear_draft),
            noforwards.unwrap_or(x.noforwards),
            update_stickersets_order.unwrap_or(x.update_stickersets_order),
            invert_media.unwrap_or(x.invert_media),
            allow_paid_floodskip.unwrap_or(x.allow_paid_floodskip),
            quick_reply_shortcut.or(x.quick_reply_shortcut),
            effect.or(x.effect),
            allow_paid_stars.or(x.allow_paid_stars),
            suggested_post.or(x.suggested_post),
        );
        let input_message = InputMessage {
            message,
            media,
            entities,
            reply_to,
            reply_markup,
            schedule_date,
            send_as,
            no_webpage,
            silent,
            background,
            clear_draft,
            noforwards,
            update_stickersets_order,
            invert_media,
            allow_paid_floodskip,
            quick_reply_shortcut,
            effect,
            allow_paid_stars,
            suggested_post,
        };
        self._send_input_message(peer, input_message).await
    }

    // edit_message
    // delete_messages
    // forward_messages
    // get_reply_to_message
}

impl PyClient {
    async fn map_random_ids_to_messages(
        &self,
        peer: PyPeer,
        peers: PyPeerMap,
        random_ids: &[i64],
        updates: tl::enums::Updates,
    ) -> PyResult<Vec<Option<PyClassInitializer<PyMessage>>>> {
        Ok(match updates {
            tl::enums::Updates::Updates(tl::types::Updates {
                updates,
                users,
                chats,
                date: _,
                seq: _,
            }) => {
                let peers = self.build_peer_map(users, chats).await?;
    
                let rnd_to_id = updates
                    .iter()
                    .filter_map(|update| match update {
                        tl::enums::Update::MessageId(u) => Some((u.random_id, u.id)),
                        _ => None,
                    })
                    .collect::<HashMap<_, _>>();
    
                // TODO ideally this would use the same UpdateIter mechanism to make sure we don't
                //      accidentally miss variants
                let mut id_to_msg = updates
                    .into_iter()
                    .filter_map(|update| match update {
                        tl::enums::Update::NewMessage(tl::types::UpdateNewMessage {
                            message, ..
                        }) => Some(message),
                        tl::enums::Update::NewChannelMessage(tl::types::UpdateNewChannelMessage {
                            message,
                            ..
                        }) => Some(message),
                        tl::enums::Update::NewScheduledMessage(
                            tl::types::UpdateNewScheduledMessage { message, .. },
                        ) => Some(message),
                        _ => None,
                    })
                    .map(|message| Python::attach(|py|
                        Py::new(py, PyMessage::from_raw(self, message, peers.handle())?)
                    ))
                    .collect::<Result<Vec<_>, _>>()?
                    .into_iter()
                    .map(|message| Python::attach(|py| {
                        let id = message.borrow(py).id();
                        (id, message)
                    }))
                    .collect::<HashMap<_, _>>();
    
                random_ids
                    .iter()
                    .map(|rnd| {
                        rnd_to_id
                            .get(rnd)
                            .and_then(|id| id_to_msg.remove(id))
                            .or_else(|| {
                                if id_to_msg.len() == 1 {
                                    // If there's no random_id to map from, in the common case a single message
                                    // should've been produced regardless, so try to recover by returning that.
                                    id_to_msg.drain().next().map(|(_, m)| m)
                                } else {
                                    None
                                }
                            })
                    })
                    .collect()
            }
            _ => return Err(PyRuntimeError::new_err("API returned something other than Updates so messages can't be mapped")),
        })
    }
    
    async fn _send_input_message(
        &self,
        peer: InputPeerLike,
        input_message: InputMessage,
    ) -> PyResult<Option<Py<PyMessage>>> {
        let peer_string = peer.stringify()?;
        let peer = self.resolve_peer(peer).await?.ok_or_else(|| {
            PyValueError::new_err(format!("peer {} can't resolve to PeerRef.", peer_string))
        })?;
        
        let random_id = crate::utils::generate_random_id();
        let InputMessage {
            media,
            message,
            entities,
            reply_to,
            reply_markup,
            schedule_date,
            send_as,
            no_webpage,
            silent,
            background,
            clear_draft,
            noforwards,
            update_stickersets_order,
            invert_media,
            allow_paid_floodskip,
            quick_reply_shortcut,
            effect,
            allow_paid_stars,
            suggested_post,
        } = input_message.clone();
        let media = media.map(Into::into);
        let entities = parse_mention_entities(self, entities.into_iter().map(Into::into).collect()).await;
        let reply_to = reply_to.map(Into::into);
        let reply_markup = reply_markup.map(Into::into);
        let send_as_string = match send_as {
            Some(x) => x.stringify()?,
            None => String::new(),
        };
        let send_as: Option<PyPeer> = self.resolve_peer(peer).await?.ok_or_else(|| {
            PyValueError::new_err(format!("send_as {} can't resolve to PeerRef.", peer_string))
        })?;
        let quick_reply_shortcut = quick_reply_shortcut.map(Into::into);
        let suggested_post = suggested_post.map(Into::into);
        
        let updates = if let Some(media) = media {
            self.invoke(&tl::functions::messages::SendMedia {
                peer: peer.into(),
                random_id,
                media,
                message,
                entities,
                reply_to,
                reply_markup,
                schedule_date,
                send_as,
                no_webpage,
                silent,
                background,
                clear_draft,
                noforwards,
                update_stickersets_order,
                invert_media,
                allow_paid_floodskip,
                quick_reply_shortcut,
                effect,
                allow_paid_stars,
                suggested_post,
            }).await?
        } else {
            self.invoke(&tl::functions::messages::SendMessage {
                peer: peer.into(),
                random_id,
                message,
                entities,
                reply_to,
                reply_markup,
                schedule_date,
                send_as,
                no_webpage,
                silent,
                background,
                clear_draft,
                noforwards,
                update_stickersets_order,
                invert_media,
                allow_paid_floodskip,
                quick_reply_shortcut,
                effect,
                allow_paid_stars,
                suggested_post,
            }).await.map_err(PyInvocationError::new)?
        };
        
        let peers = self.build_peer_map_from_peer(peer).await?;
        let res = match updates {
            tl::enums::Updates::UpdateShortSentMessage(updates) => {
                PyMessage::from_raw_short_updates(self, updates, peer, input_message, peers, send_as).await
            }
            updates => {
                let updates_debug = if log::log_enabled!(log::Level::Warn) {
                    Some(updates.clone())
                } else {
                    None
                };

                match self.map_random_ids_to_messages(peer, peers, &[random_id], updates)
                    .await
                    .pop()
                    .flatten()
                {
                    Some(message) => message,
                    None => {
                        if let Some(updates) = updates_debug {
                            log::warn!(
                                "failed to find just-sent message in response updates; please report this:"
                            );
                            log::warn!("{:#?}", updates);
                        }
                        PyMessage::from_raw(
                            self,
                            tl::enums::Message::Empty(tl::types::MessageEmpty {
                                id: 0,
                                peer_id: Some(peer.id.into()),
                            }),
                            peers,
                        )
                    }
                }
            }
        };
        res.map(|x| Python::attach(|py| Py::new(py, x)))
    }
}