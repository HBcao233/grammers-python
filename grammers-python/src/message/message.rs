// Copyright 2020 - developers of the `grammers` project.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

use pyo3::exceptions::PyTypeError;
use pyo3::prelude::*;
use pyo3::types::{PyDateTime, PyDict};

use grammers_session_pyo3::{PyPeerId, PyPeerKind};
use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

use crate::PyClient;
use crate::utils::PyDateTimeWrapper;
// use crate::media::{InputMedia, Media, Photo};
// #[cfg(any(feature = "markdown", feature = "html"))]
// use crate::parsers;
use crate::peer::{PyPeer, PyPeerMap};

// use to Default::default() eliminate so much None
#[derive(Default)]
struct MessageData {
    pub out: Option<bool>,
    pub mentioned: Option<bool>,
    pub media_unread: Option<bool>,
    // MessageService only
    pub reactions_are_possible: Option<bool>,
    pub silent: Option<bool>,
    pub post: Option<bool>,
    pub from_scheduled: Option<bool>,
    pub legacy: Option<bool>,
    pub edit_hide: Option<bool>,
    pub pinned: Option<bool>,
    pub noforwards: Option<bool>,
    pub invert_media: Option<bool>,
    pub offline: Option<bool>,
    pub video_processing_pending: Option<bool>,
    pub paid_suggested_post_stars: Option<bool>,
    pub paid_suggested_post_ton: Option<bool>,
    pub from_id: Option<PyPeerId>,
    pub from_boosts_applied: Option<i32>,
    pub saved_peer_id: Option<PyPeerId>,
    pub fwd_from: Option<pytl::enums::PyMessageFwdHeader>,
    pub via_bot_id: Option<i64>,
    pub via_business_bot_id: Option<i64>,
    pub reply_to: Option<pytl::enums::PyMessageReplyHeader>,
    pub date: Option<PyDateTimeWrapper>,
    pub date_timestamp: Option<i32>,
    // MessageService only
    pub action: Option<pytl::enums::PyMessageAction>,
    pub message: Option<String>,
    pub media: Option<pytl::enums::PyMessageMedia>,
    pub reply_markup: Option<pytl::enums::PyReplyMarkup>,
    pub entities: Vec<pytl::enums::PyMessageEntity>,
    pub views: Option<i32>,
    pub forwards: Option<i32>,
    pub replies: Option<pytl::enums::PyMessageReplies>,
    pub edit_date: Option<i32>,
    pub post_author: Option<String>,
    pub grouped_id: Option<i64>,
    pub reactions: Option<pytl::enums::PyMessageReactions>,
    pub restriction_reason: Vec<pytl::enums::PyRestrictionReason>,
    pub ttl_period: Option<i32>,
    pub quick_reply_shortcut_id: Option<i32>,
    pub effect: Option<i64>,
    pub factcheck: Option<pytl::enums::PyFactCheck>,
    pub report_delivery_until_date: Option<i32>,
    pub paid_message_stars: Option<i64>,
    pub suggested_post: Option<pytl::enums::PySuggestedPost>,
    pub schedule_repeat_period: Option<i32>,
    pub summary_from_language: Option<String>,
}

/// Represents a Telegram message, which includes text messages, messages with media, and service
/// messages.
///
/// This message should be treated as a snapshot in time, that is, if the message is edited while
/// using this object, those changes won't alter this structure.
#[derive(Clone)]
#[pyclass(name = "Message", module = "grammers.client", extends = pytl::TLObject)]
pub struct PyMessage {
    #[pyo3(get)]
    pub(crate) client: PyClient,

    // When fetching messages or receiving updates, a set of peers will be present. A single
    // server response contains a lot of peers, and some might be related to deep layers of
    // a message action for instance. Keeping the entire set like this allows for cheaper clones
    // and moves, and saves us from worrying about picking out all the peers we care about.
    pub(crate) peers: PyPeerMap,

    /// The ID of this message.
    ///
    /// Message identifiers are counters that start at 1 and grow by 1 for each message produced.
    ///
    /// Every channel has its own unique message counter. This counter is the same for all users,
    /// but unique to each channel.
    ///
    /// Every account has another unique message counter which is used for private conversations
    /// and small group chats. This means different accounts will likely have different message
    /// identifiers for the same message in a private conversation or small group chat. This also
    /// implies that the message identifier alone is enough to uniquely identify the message,
    /// without the need to know the chat ID.
    ///
    /// **You cannot use the message ID of User A when running as User B**, unless this message
    /// belongs to a megagroup or broadcast channel. Beware of this when using methods like
    /// [`Client::delete_messages`], which **cannot** validate the peer where the message
    /// should be deleted for those cases.
    #[pyo3(get)]
    pub id: i32,

    /// The [`Self::peer`]'s identifier.
    #[pyo3(get)]
    pub peer_id: Option<PyPeerId>,

    /// Whether the message is outgoing (i.e. you sent this message to some other peer) or
    /// incoming (i.e. someone else sent it to you or the peer).
    #[pyo3(get, set)]
    pub out: Option<bool>,

    /// Whether you were mentioned in this message or not.
    ///
    /// This includes @username mentions, text mentions, and messages replying to one of your
    /// previous messages (even if it contains no mention in the message text).
    #[pyo3(get, set)]
    pub mentioned: Option<bool>,

    /// Whether you have read the media in this message or not.
    ///
    /// Most commonly, these are voice notes that you have not played yet.
    #[pyo3(get, set)]
    pub media_unread: Option<bool>,

    /// Whether you can react to this message.
    ///
    /// MessageService only.
    #[pyo3(get, set)]
    pub reactions_are_possible: Option<bool>,

    /// Whether the message should notify people with sound or not.
    #[pyo3(get, set)]
    pub silent: Option<bool>,

    /// Whether this message is a post in a broadcast channel or not.
    #[pyo3(get, set)]
    pub post: Option<bool>,

    /// Whether this message was originated from a previously-scheduled message or not.
    #[pyo3(get, set)]
    pub from_scheduled: Option<bool>,

    /// Whether this is a legacy message: it has to be refetched with the new layer.
    #[pyo3(get, set)]
    pub legacy: Option<bool>,

    /// Whether the edited mark of this message is edited should be hidden (e.g. in GUI clients)
    /// or shown.
    #[pyo3(get, set)]
    pub edit_hide: Option<bool>,

    /// Whether this message is currently pinned or not.
    #[pyo3(get, set)]
    pub pinned: Option<bool>,

    /// Whether this message is protected and thus cannot be forwarded; clients should also
    /// prevent users from saving attached media (i.e. videos should only be streamed,
    /// photos should be kept in RAM, et cetera).
    #[pyo3(get, set)]
    pub noforwards: Option<bool>,

    /// If set, any eventual webpage preview will be shown on top of the message instead of at the bottom.
    #[pyo3(get, set)]
    pub invert_media: Option<bool>,

    /// If set, the message was sent because of a scheduled action by the message sender,
    /// for example, as away, or a greeting service message.
    #[pyo3(get, set)]
    pub offline: Option<bool>,

    /// The video contained in the message is currently being processed by the server
    /// (i.e. to generate alternative qualities, that will be contained in the final messageMediaDocument.alt_document)
    #[pyo3(get, set)]
    pub video_processing_pending: Option<bool>,

    /// Set if this is a suggested channel post that was paid using Telegram Stars.
    #[pyo3(get, set)]
    pub paid_suggested_post_stars: Option<bool>,

    /// Set if this is a suggested channel post that was paid using Toncoins.
    #[pyo3(get, set)]
    pub paid_suggested_post_ton: Option<bool>,

    /// Raw from_id, generally use `sender_id` instead.
    #[pyo3(get, set)]
    pub from_id: Option<PyPeerId>,

    /// Supergroups only, contains the number of boosts this user has given the current supergroup.
    #[pyo3(get, set)]
    pub from_boosts_applied: Option<i32>,

    #[pyo3(get, set)]
    pub saved_peer_id: Option<PyPeerId>,

    /// Info about forwarded messages.
    #[pyo3(get, set)]
    pub fwd_from: Option<pytl::enums::PyMessageFwdHeader>,

    /// If this message was sent @via some inline bot, return the bot's user identifier.
    #[pyo3(get, set)]
    pub via_bot_id: Option<i64>,

    #[pyo3(get, set)]
    pub via_business_bot_id: Option<i64>,

    /// If this message is replying to a previous message, return the header with information
    /// about that reply.
    #[pyo3(get, set)]
    pub reply_to: Option<pytl::enums::PyMessageReplyHeader>,

    /// The date when this message was produced.
    #[pyo3(get)]
    pub date: Option<PyDateTimeWrapper>,

    #[pyo3(get)]
    pub date_timestamp: Option<i32>,

    /// Event connected with the service message.
    ///
    /// MessageService only.
    #[pyo3(get, set)]
    pub action: Option<pytl::enums::PyMessageAction>,

    /// The message's text.
    ///
    /// For service or empty messages, this will be None.
    ///
    /// If the message has media, this text is the caption commonly displayed underneath it.
    #[pyo3(get, set)]
    pub message: Option<String>,

    /// The media displayed by this message, if any.
    ///
    /// This not only includes photos or videos, but also contacts, polls, documents, locations
    /// and many other types.
    #[pyo3(get, set)]
    pub media: Option<pytl::enums::PyMessageMedia>,

    /// If the message has a reply markup (which can happen for messages produced by bots),
    /// returns said markup.
    #[pyo3(get, set)]
    pub reply_markup: Option<pytl::enums::PyReplyMarkup>,

    #[pyo3(get, set)]
    pub entities: Vec<pytl::enums::PyMessageEntity>,

    /// How many views does this message have, when applicable.
    ///
    /// The same user account can contribute to increment this counter indefinitedly, however
    /// there is a server-side cooldown limitting how fast it can happen (several hours).
    #[pyo3(get, set)]
    pub views: Option<i32>,

    /// How many times has this message been forwarded, when applicable.
    #[pyo3(get, set)]
    pub forwards: Option<i32>,

    /// How many replies does this message have, when applicable.
    #[pyo3(get, set)]
    pub replies: Option<pytl::enums::PyMessageReplies>,

    /// The date when this message was last edited.
    #[pyo3(get, set)]
    pub edit_date: Option<i32>,

    /// If this message was sent to a channel, return the name used by the author to post it.
    #[pyo3(get, set)]
    pub post_author: Option<String>,

    /// If this message belongs to a group of messages, return the unique identifier for that
    /// group.
    ///
    /// This applies to albums of media, such as multiple photos grouped together.
    ///
    /// Note that there may be messages sent in between the messages forming a group.
    #[pyo3(get, set)]
    pub grouped_id: Option<i64>,

    #[pyo3(get, set)]
    pub reactions: Option<pytl::enums::PyMessageReactions>,

    /// A list of reasons on why this message is restricted.
    ///
    /// The message is not restricted if the return value is `None`.
    #[pyo3(get, set)]
    pub restriction_reason: Vec<pytl::enums::PyRestrictionReason>,

    #[pyo3(get, set)]
    pub ttl_period: Option<i32>,

    #[pyo3(get, set)]
    pub quick_reply_shortcut_id: Option<i32>,
    #[pyo3(get, set)]
    pub effect: Option<i64>,
    #[pyo3(get, set)]
    pub factcheck: Option<pytl::enums::PyFactCheck>,
    #[pyo3(get, set)]
    pub report_delivery_until_date: Option<i32>,
    #[pyo3(get, set)]
    pub paid_message_stars: Option<i64>,
    #[pyo3(get, set)]
    pub suggested_post: Option<pytl::enums::PySuggestedPost>,
    #[pyo3(get, set)]
    pub schedule_repeat_period: Option<i32>,
    #[pyo3(get, set)]
    pub summary_from_language: Option<String>,
}

impl PyMessage {
    pub fn from_raw(
        client: &PyClient,
        message: tl::enums::Message,
        peers: PyPeerMap,
    ) -> PyResult<PyClassInitializer<Self>> {
        use tl::enums::Message as M;

        let (id, peer_id, data) = match message {
            M::Empty(x) => (x.id, x.peer_id.map(PyPeerId::from), MessageData::default()),
            M::Message(x) => {
                let tl::types::Message {
                    id,
                    peer_id,
                    out,
                    mentioned,
                    media_unread,
                    silent,
                    post,
                    from_scheduled,
                    legacy,
                    edit_hide,
                    pinned,
                    noforwards,
                    invert_media,
                    offline,
                    video_processing_pending,
                    paid_suggested_post_stars,
                    paid_suggested_post_ton,
                    from_id,
                    from_boosts_applied,
                    saved_peer_id,
                    fwd_from,
                    via_bot_id,
                    via_business_bot_id,
                    reply_to,
                    date,
                    message,
                    media,
                    reply_markup,
                    entities,
                    views,
                    forwards,
                    replies,
                    edit_date,
                    post_author,
                    grouped_id,
                    reactions,
                    restriction_reason,
                    ttl_period,
                    quick_reply_shortcut_id,
                    effect,
                    factcheck,
                    report_delivery_until_date,
                    paid_message_stars,
                    suggested_post,
                    schedule_repeat_period,
                    summary_from_language,
                } = x;
                (
                    id,
                    Some(PyPeerId::from(peer_id)),
                    MessageData {
                        out: Some(out),
                        mentioned: Some(mentioned),
                        media_unread: Some(media_unread),
                        silent: Some(silent),
                        post: Some(post),
                        from_scheduled: Some(from_scheduled),
                        legacy: Some(legacy),
                        edit_hide: Some(edit_hide),
                        pinned: Some(pinned),
                        noforwards: Some(noforwards),
                        invert_media: Some(invert_media),
                        offline: Some(offline),
                        video_processing_pending: Some(video_processing_pending),
                        paid_suggested_post_stars: Some(paid_suggested_post_stars),
                        paid_suggested_post_ton: Some(paid_suggested_post_ton),
                        from_id: from_id.map(Into::into),
                        from_boosts_applied: from_boosts_applied,
                        saved_peer_id: saved_peer_id.map(Into::into),
                        fwd_from: fwd_from.map(Into::into),
                        via_bot_id: via_bot_id,
                        via_business_bot_id: via_business_bot_id,
                        reply_to: reply_to.map(Into::into),
                        date: Some(Python::attach(|py| {
                            PyDateTime::from_timestamp(py, date as f64, None)
                                .map(|x| x.unbind().into())
                        })?),
                        date_timestamp: Some(date),
                        message: Some(message),
                        media: media.map(Into::into),
                        reply_markup: reply_markup.map(Into::into),
                        entities: entities
                            .unwrap_or_default()
                            .into_iter()
                            .map(Into::into)
                            .collect(),
                        views: views,
                        forwards: forwards,
                        replies: replies.map(Into::into),
                        edit_date: edit_date,
                        post_author: post_author,
                        grouped_id: grouped_id,
                        reactions: reactions.map(Into::into), // Option<pytl::enums::PyMessageReactions>,
                        restriction_reason: restriction_reason
                            .unwrap_or_default()
                            .into_iter()
                            .map(Into::into)
                            .collect(), // Option<Vec<pytl::enums::PyRestrictionReason>>,
                        ttl_period: ttl_period,               // Option<i32>,
                        quick_reply_shortcut_id: quick_reply_shortcut_id, // Option<i32>,
                        effect: effect,                       // Option<i64>,
                        factcheck: factcheck.map(Into::into), // Option<pytl::enums::PyFactCheck>,
                        report_delivery_until_date: report_delivery_until_date, // Option<i32>,
                        paid_message_stars: paid_message_stars, // Option<i64>,
                        suggested_post: suggested_post.map(Into::into), // Option<pytl::enums::PySuggestedPost>,
                        schedule_repeat_period: schedule_repeat_period, // Option<i32>,
                        summary_from_language: summary_from_language,   // Option<String>,
                        ..Default::default()
                    },
                )
            }
            M::Service(x) => {
                let tl::types::MessageService {
                    id,
                    peer_id,
                    out,
                    mentioned,
                    media_unread,
                    reactions_are_possible,
                    silent,
                    post,
                    legacy,
                    from_id,
                    saved_peer_id,
                    reply_to,
                    date,
                    action,
                    reactions,
                    ttl_period,
                } = x;
                (
                    id,
                    Some(PyPeerId::from(peer_id)),
                    MessageData {
                        out: Some(out),
                        mentioned: Some(mentioned),
                        media_unread: Some(media_unread),
                        reactions_are_possible: Some(reactions_are_possible),
                        silent: Some(silent),
                        post: Some(post),
                        legacy: Some(legacy),
                        from_id: from_id.map(Into::into),
                        saved_peer_id: saved_peer_id.map(Into::into),
                        reply_to: reply_to.map(Into::into),
                        date: Some(Python::attach(|py| {
                            PyDateTime::from_timestamp(py, date as f64, None)
                                .map(|x| x.unbind().into())
                        })?),
                        date_timestamp: Some(date),
                        action: Some(action.into()),
                        reactions: reactions.map(Into::into),
                        ttl_period: ttl_period,
                        ..Default::default()
                    },
                )
            }
        };
        let MessageData {
            out,
            mentioned,
            media_unread,
            reactions_are_possible,
            silent,
            post,
            from_scheduled,
            legacy,
            edit_hide,
            pinned,
            noforwards,
            invert_media,
            offline,
            video_processing_pending,
            paid_suggested_post_stars,
            paid_suggested_post_ton,
            from_id,
            from_boosts_applied,
            saved_peer_id,
            fwd_from,
            via_bot_id,
            via_business_bot_id,
            reply_to,
            date,
            date_timestamp,
            action,
            message,
            media,
            reply_markup,
            entities,
            views,
            forwards,
            replies,
            edit_date,
            post_author,
            grouped_id,
            reactions,
            restriction_reason,
            ttl_period,
            quick_reply_shortcut_id,
            effect,
            factcheck,
            report_delivery_until_date,
            paid_message_stars,
            suggested_post,
            schedule_repeat_period,
            summary_from_language,
        } = data;
        let base = PyClassInitializer::from(pytl::TLObject {});
        let sub = Self {
            client: client.clone(),
            peers,
            id,
            peer_id,
            out,
            mentioned,
            media_unread,
            reactions_are_possible,
            silent,
            post,
            from_scheduled,
            legacy,
            edit_hide,
            pinned,
            noforwards,
            invert_media,
            offline,
            video_processing_pending,
            paid_suggested_post_stars,
            paid_suggested_post_ton,
            from_id,
            from_boosts_applied,
            saved_peer_id,
            fwd_from,
            via_bot_id,
            via_business_bot_id,
            reply_to,
            date,
            date_timestamp,
            action,
            message,
            media,
            reply_markup,
            entities,
            views,
            forwards,
            replies,
            edit_date,
            post_author,
            grouped_id,
            reactions,
            restriction_reason,
            ttl_period,
            quick_reply_shortcut_id,
            effect,
            factcheck,
            report_delivery_until_date,
            paid_message_stars,
            suggested_post,
            schedule_repeat_period,
            summary_from_language,
        };
        Ok(base.add_subclass(sub))
    }

    /*pub fn from_raw_short_updates(
        client: &PyClient,
        updates: tl::types::UpdateShortSentMessage,
        input: InputMessage,
        peer: PeerRef,
    ) -> Self {
        Self {
            raw: tl::enums::Message::Message(tl::types::Message {
                out: updates.out,
                mentioned: false,
                media_unread: false,
                silent: input.silent,
                post: false, // TODO true if sent to broadcast channel
                from_scheduled: false,
                legacy: false,
                edit_hide: false,
                pinned: false,
                noforwards: false, // TODO true if channel has noforwads?
                video_processing_pending: false,
                paid_suggested_post_stars: false,
                invert_media: input.invert_media,
                id: updates.id,
                from_id: None, // TODO self
                from_boosts_applied: None,
                peer_id: peer.id.into(),
                saved_peer_id: None,
                fwd_from: None,
                via_bot_id: None,
                reply_to: input.reply_to.map(|reply_to_msg_id| {
                    tl::types::MessageReplyHeader {
                        reply_to_scheduled: false,
                        forum_topic: false,
                        quote: false,
                        reply_to_msg_id: Some(reply_to_msg_id),
                        reply_to_peer_id: None,
                        reply_from: None,
                        reply_media: None,
                        reply_to_top_id: None,
                        quote_text: None,
                        quote_entities: None,
                        quote_offset: None,
                        todo_item_id: None,
                    }
                    .into()
                }),
                date: updates.date,
                message: input.text,
                media: updates.media,
                reply_markup: input.reply_markup,
                entities: updates.entities,
                views: None,
                forwards: None,
                replies: None,
                edit_date: None,
                post_author: None,
                grouped_id: None,
                restriction_reason: None,
                ttl_period: updates.ttl_period,
                reactions: None,
                quick_reply_shortcut_id: None,
                via_business_bot_id: None,
                offline: false,
                effect: None,
                factcheck: None,
                report_delivery_until_date: None,
                paid_message_stars: None,
                paid_suggested_post_ton: false,
                suggested_post: None,
                schedule_repeat_period: None,
                summary_from_language: None,
            }),
            fetched_in: Some(peer),
            client: client.clone(),
            peers: client.empty_peer_map(),
        }
    }*/

    pub fn into_dict(self) -> PyResult<Py<PyDict>> {
        let peer = self.peer();
        let sender = self.sender();
        let PyMessage {
            client: _,
            peers: _,
            id,
            peer_id: _,
            out,
            mentioned,
            media_unread,
            reactions_are_possible,
            silent,
            post,
            from_scheduled,
            legacy,
            edit_hide,
            pinned,
            noforwards,
            invert_media,
            offline,
            video_processing_pending,
            paid_suggested_post_stars,
            paid_suggested_post_ton,
            from_id: _,
            from_boosts_applied,
            saved_peer_id,
            fwd_from,
            via_bot_id,
            via_business_bot_id,
            reply_to,
            date,
            date_timestamp: _,
            action,
            message,
            media,
            reply_markup,
            entities,
            views,
            forwards,
            replies,
            edit_date,
            post_author,
            grouped_id,
            reactions,
            restriction_reason,
            ttl_period,
            quick_reply_shortcut_id,
            effect,
            factcheck,
            report_delivery_until_date,
            paid_message_stars,
            suggested_post,
            schedule_repeat_period,
            summary_from_language,
        } = self;
        Python::attach(|py| {
            let dict = PyDict::new(py);
            dict.set_item("_", "Message")?;
            dict.set_item("id", id)?;
            dict.set_item("peer", peer)?;
            dict.set_item("sender", sender)?;
            dict.set_item("out", out)?;
            dict.set_item("mentioned", mentioned)?;
            dict.set_item("media_unread", media_unread)?;
            dict.set_item("reactions_are_possible", reactions_are_possible)?;
            dict.set_item("silent", silent)?;
            dict.set_item("post", post)?;
            dict.set_item("from_scheduled", from_scheduled)?;
            dict.set_item("legacy", legacy)?;
            dict.set_item("edit_hide", edit_hide)?;
            dict.set_item("pinned", pinned)?;
            dict.set_item("noforwards", noforwards)?;
            dict.set_item("invert_media", invert_media)?;
            dict.set_item("offline", offline)?;
            dict.set_item("video_processing_pending", video_processing_pending)?;
            dict.set_item("paid_suggested_post_stars", paid_suggested_post_stars)?;
            dict.set_item("paid_suggested_post_ton", paid_suggested_post_ton)?;
            // dict.set_item("from_id", from_id)?;
            dict.set_item("from_boosts_applied", from_boosts_applied)?;
            dict.set_item("saved_peer_id", saved_peer_id)?;
            dict.set_item("fwd_from", fwd_from)?;
            dict.set_item("via_bot_id", via_bot_id)?;
            dict.set_item("via_business_bot_id", via_business_bot_id)?;
            dict.set_item("reply_to", reply_to)?;
            dict.set_item("date", date)?;
            dict.set_item("action", action)?;
            dict.set_item("message", message)?;
            dict.set_item("media", media)?;
            dict.set_item("reply_markup", reply_markup)?;
            dict.set_item("entities", entities)?;
            dict.set_item("views", views)?;
            dict.set_item("forwards", forwards)?;
            dict.set_item("replies", replies)?;
            dict.set_item("edit_date", edit_date)?;
            dict.set_item("post_author", post_author)?;
            dict.set_item("grouped_id", grouped_id)?;
            dict.set_item("reactions", reactions)?;
            dict.set_item("restriction_reason", restriction_reason)?;
            dict.set_item("ttl_period", ttl_period)?;
            dict.set_item("quick_reply_shortcut_id", quick_reply_shortcut_id)?;
            dict.set_item("effect", effect)?;
            dict.set_item("factcheck", factcheck)?;
            dict.set_item("report_delivery_until_date", report_delivery_until_date)?;
            dict.set_item("paid_message_stars", paid_message_stars)?;
            dict.set_item("suggested_post", suggested_post)?;
            dict.set_item("schedule_repeat_period", schedule_repeat_period)?;
            dict.set_item("summary_from_language", summary_from_language)?;
            Ok(dict.unbind())
        })
    }
}

#[pymethods]
impl PyMessage {
    #[new]
    fn new(
        client: &PyClient,
        message: pytl::enums::PyMessage,
        peers: PyPeerMap,
    ) -> PyResult<PyClassInitializer<Self>> {
        PyMessage::from_raw(client, message.into(), peers)
    }

    fn to_bytes(&self) -> PyResult<Vec<u8>> {
        Err(PyTypeError::new_err(
            "grammers.custom.Message can't to_bytes()",
        ))
    }

    fn to_dict(&self) -> PyResult<Py<PyDict>> {
        self.clone().into_dict()
    }

    /// The peer where this message was sent to.
    ///
    /// This might be the user you're talking to for private conversations, or the group or
    /// channel where the message was sent.
    #[getter]
    pub fn peer(&self) -> Option<PyPeer> {
        self.peers.get(self.peer_id?).cloned()
    }

    /// The [`Self::sender`]'s identifier, if there is a sender.
    #[getter]
    pub fn sender_id(&self) -> Option<PyPeerId> {
        self.from_id.or_else(|| {
            // Incoming messages in private conversations don't include `from_id` since
            // layer 119, but the sender can only be the peer we're in.
            let peer_id = self.peer_id?;
            if matches!(peer_id.kind(), PyPeerKind::User | PyPeerKind::UserSelf) {
                if self.out.unwrap_or(false) {
                    Some(PyPeerId::self_user().expect("self_user"))
                } else {
                    Some(peer_id)
                }
            } else {
                None
            }
        })
    }

    /// The sender of this message, if there is a sender **and** the sender is in cache.
    #[getter]
    pub fn sender(&self) -> Option<PyPeer> {
        self.peers.get(self.sender_id()?).cloned()
    }

    // ====================
    //       Methods
    // ====================

    /// Fetch the message that this message is replying to, or `None` if this message is not a
    /// reply to a previous message.
    ///
    /// Shorthand for `Client.get_reply_to_message`.
    pub async fn get_reply_to(&self) -> PyResult<Option<Py<PyMessage>>> {
        /*self.client
        .get_reply_to_message(self)
        .await*/
        Err(PyTypeError::new_err("TODO!"))
    }

    /*
    /// React to this message.
    ///
    /// # Examples
    ///
    /// ```
    /// # async fn f(message: grammers_client::message::Message, client: grammers_client::Client) -> Result<(), Box<dyn std::error::Error>> {
    /// message.react("👍").await?;
    /// # Ok(())
    /// # }
    /// ```
    ///
    /// Make animation big & Add to recent
    ///
    /// ```
    /// # async fn f(message: grammers_client::message::Message, client: grammers_client::Client) -> Result<(), Box<dyn std::error::Error>> {
    /// use grammers_client::message::InputReactions;
    ///
    /// let reactions = InputReactions::emoticon("🤯").big().add_to_recent();
    ///
    /// message.react(reactions).await?;
    /// # Ok(())
    /// # }
    /// ```
    ///
    /// Remove reactions
    ///
    /// ```
    /// # async fn f(message: grammers_client::message::Message, client: grammers_client::Client) -> Result<(), Box<dyn std::error::Error>> {
    /// use grammers_client::message::InputReactions;
    ///
    /// message.react(InputReactions::remove()).await?;
    /// # Ok(())
    /// # }
    /// ```
    pub async fn react(
        &self,
        reactions: InputReactionsLike,
    ) -> Result<(), InvocationError> {
        self.client
            .send_reactions(
                self.peer_ref().await.ok_or(InvocationError::Dropped)?,
                self.id(),
                reactions,
            )
            .await?;
        Ok(())
    }
    */

    /*
    /// Respond to this message by sending a new message to the same peer, but without directly
    /// replying to it.
    ///
    /// Shorthand for `Client::send_message`.
    pub async fn respond(
        &self,
        message: InputMessageLike,
    ) -> PyResult<Self> {
        self.client
            .send_message(
                self.peer_ref().await.ok_or(InvocationError::Dropped)?,
                message,
            )
            .await
            .map_err(PyInvocationError::new)
    }
    */

    /*
    /// Respond to this message by sending a album in the same peer, but without directly
    /// replying to it.
    ///
    /// Shorthand for `Client::send_album`.
    pub async fn respond_album(
        &self,
        medias: Vec<InputMedia>,
    ) -> Result<Vec<Option<Self>>, InvocationError> {
        self.client
            .send_album(
                self.peer_ref().await.ok_or(InvocationError::Dropped)?,
                medias,
            )
            .await
    }
    */

    /*
    /// Directly reply to this message by sending a new message to the same peer that replies to
    /// it. This methods overrides the `reply_to` on the `InputMessage` to point to `self`.
    ///
    /// Shorthand for `Client::send_message`.
    pub async fn reply<M: Into<InputMessage>>(&self, message: M) -> Result<Self, InvocationError> {
        let message = message.into();
        self.client
            .send_message(
                self.peer_ref().await.ok_or(InvocationError::Dropped)?,
                message.reply_to(Some(self.id())),
            )
            .await
    }
    */

    /*
    /// Directly reply to this message by sending a album to the same peer that replies to
    /// it. This methods overrides the `reply_to` on the first `InputMedia` to point to `self`.
    ///
    /// Shorthand for `Client::send_album`.
    pub async fn reply_album(
        &self,
        mut medias: Vec<InputMedia>,
    ) -> Result<Vec<Option<Self>>, InvocationError> {
        medias.first_mut().unwrap().reply_to = Some(self.id());
        self.client
            .send_album(
                self.peer_ref().await.ok_or(InvocationError::Dropped)?,
                medias,
            )
            .await
    }
    */

    /*
    /// Forward this message to another (or the same) peer.
    ///
    /// Shorthand for `Client::forward_messages`. If you need to forward multiple messages
    /// at once, consider using that method instead.
    pub async fn forward_to<C: Into<PeerRef>>(&self, chat: C) -> Result<Self, InvocationError> {
        // TODO return `Message`
        // When forwarding a single message, if it fails, Telegram should respond with RPC error.
        // If it succeeds we will have the single forwarded message present which we can unwrap.
        self.client
            .forward_messages(
                chat,
                &[self.id()],
                self.peer_ref().await.ok_or(InvocationError::Dropped)?,
            )
            .await
            .map(|mut msgs| msgs.pop().unwrap().unwrap())
    }
    */

    /*
    /// Edit this message to change its text or media.
    ///
    /// Shorthand for `Client::edit_message`.
    pub async fn edit<M: Into<InputMessage>>(&self, new_message: M) -> Result<(), InvocationError> {
        self.client
            .edit_message(
                self.peer_ref().await.ok_or(InvocationError::Dropped)?,
                self.id(),
                new_message,
            )
            .await
    }
    */

    /*
    /// Delete this message for everyone.
    ///
    /// Shorthand for `Client::delete_messages`. If you need to delete multiple messages
    /// at once, consider using that method instead.
    pub async fn delete(&self) -> Result<(), InvocationError> {
        self.client
            .delete_messages(
                self.peer_ref().await.ok_or(InvocationError::Dropped)?,
                &[self.id()],
            )
            .await
            .map(drop)
    }
    */

    /*
    /// Mark this message and all messages above it as read.
    ///
    /// Unlike `Client::mark_as_read`, this method only will mark the conversation as read up to
    /// this message, not the entire conversation.
    pub async fn mark_as_read(&self) -> Result<(), InvocationError> {
        let peer = self.peer_ref().await.ok_or(InvocationError::Dropped)?;
        if peer.id.kind() == PeerKind::Channel {
            self.client
                .invoke(&tl::functions::channels::ReadHistory {
                    channel: peer.into(),
                    max_id: self.id(),
                })
                .await
                .map(drop)
        } else {
            self.client
                .invoke(&tl::functions::messages::ReadHistory {
                    peer: peer.into(),
                    max_id: self.id(),
                })
                .await
                .map(drop)
        }
    }
    */

    /*
    /// Pin this message in the conversation.
    ///
    /// Shorthand for `Client::pin_message`.
    pub async fn pin(&self) -> Result<(), InvocationError> {
        self.client
            .pin_message(
                self.peer_ref().await.ok_or(InvocationError::Dropped)?,
                self.id(),
            )
            .await
    }
    */

    /*
    /// Unpin this message from the conversation.
    ///
    /// Shorthand for `Client::unpin_message`.
    pub async fn unpin(&self) -> Result<(), InvocationError> {
        self.client
            .unpin_message(
                self.peer_ref().await.ok_or(InvocationError::Dropped)?,
                self.id(),
            )
            .await
    }
    */

    /*
    /// Refetch this message, mutating all of its properties in-place.
    ///
    /// No changes will be made to the message if it fails to be fetched.
    ///
    /// Shorthand for `Client::get_messages_by_id`.
    pub async fn refetch(&self) -> Result<(), InvocationError> {
        // When fetching a single message, if it fails, Telegram should respond with RPC error.
        // If it succeeds we will have the single message present which we can unwrap.
        self.client
            .get_messages_by_id(
                self.peer_ref().await.ok_or(InvocationError::Dropped)?,
                &[self.id()],
            )
            .await?
            .pop()
            .unwrap()
            .unwrap();
        todo!("actually mutate self after get_messages_by_id returns `Message`")
    }
    */

    /*
    /// Download the message media in this message if applicable.
    ///
    /// Returns `true` if there was media to download, or `false` otherwise.
    ///
    /// Shorthand for `Client::download_media`.
    #[cfg(feature = "fs")]
    pub async fn download_media<P: AsRef<Path>>(&self, path: P) -> Result<bool, io::Error> {
        // TODO probably encode failed download in error
        if let Some(media) = self.media() {
            self.client.download_media(&media, path).await.map(|_| true)
        } else {
            Ok(false)
        }
    }
    */

    /*
    /// Get photo attached to the message if any.
    pub fn photo(&self) -> Option<Photo> {
        if let Media::Photo(photo) = self.media()? {
            return Some(photo);
        }

        None
    }
    */
}
