use pyo3::{PyResult, Python};

use grammers_tl_types as tl;

use super::PyMessage;
use crate::convert::convertMessageMedia2InputMedia;
use crate::hints::{InputPeerLike, InputReplyToLike};

#[derive(Default, Clone)]
pub struct InputMessage {
    /// Set this flag to disable generation of the webpage preview
    pub no_webpage: bool,

    pub silent: bool,

    pub background: bool,

    pub clear_draft: bool,

    pub noforwards: bool,

    pub update_stickersets_order: bool,

    pub invert_media: bool,

    pub allow_paid_floodskip: bool,

    pub reply_to: Option<InputReplyToLike>,

    pub message: String,

    pub media: Option<tl::enums::InputMedia>,

    pub reply_markup: Option<tl::enums::ReplyMarkup>,

    pub entities: Vec<tl::enums::MessageEntity>,

    pub schedule_date: Option<i32>,

    /// Send this message as the specified peer
    pub send_as: Option<InputPeerLike>,

    pub quick_reply_shortcut: Option<tl::enums::InputQuickReplyShortcut>,

    pub effect: Option<i64>,

    pub allow_paid_stars: Option<i64>,

    pub suggested_post: Option<tl::enums::SuggestedPost>,
}

impl InputMessage {
    pub async fn from_py_message(msg: PyMessage) -> PyResult<Self> {
        let sender = msg.sender();
        let PyMessage {
            message,
            media,
            entities,
            reply_to: _,
            reply_markup,
            silent,
            noforwards: _,
            invert_media,
            effect,
            suggested_post,
            ref client,
            peers: _,
            id: _,
            peer_id: _,
            out: _,
            mentioned: _,
            media_unread: _,
            reactions_are_possible: _,
            post: _,
            from_scheduled: _,
            legacy: _,
            edit_hide: _,
            pinned: _,
            offline: _,
            video_processing_pending: _,
            paid_suggested_post_stars: _,
            paid_suggested_post_ton: _,
            from_id: _,
            from_boosts_applied: _,
            from_rank: _,
            saved_peer_id: _,
            fwd_from: _,
            via_bot_id: _,
            via_business_bot_id: _,
            guestchat_via_from_id: _,
            date: _,
            date_timestamp: _,
            action: _,
            views: _,
            forwards: _,
            replies: _,
            edit_date: _,
            post_author: _,
            grouped_id: _,
            reactions: _,
            restriction_reason: _,
            ttl_period: _,
            quick_reply_shortcut_id: _,
            factcheck: _,
            report_delivery_until_date: _,
            paid_message_stars: _,
            schedule_repeat_period: _,
            summary_from_language: _,
        } = msg;
        let me = client._me().expect("me must be cached, but not found.");
        let me_id = Python::attach(|py| me.borrow(py).id());

        let mut send_as = None;
        if let Some(sender) = sender {
            if me_id != sender.id() {
                send_as = Some(sender.to_ref().await?.unwrap());
            }
        }
        Ok(Self {
            message: message.unwrap_or_default(),
            media: match media {
                Some(m) => convertMessageMedia2InputMedia(client.clone(), m.into()).await?,
                None => None,
            },
            entities: entities.into_iter().map(Into::into).collect(),
            reply_to: None,
            reply_markup: reply_markup.map(Into::into),
            schedule_date: None,
            send_as: send_as.map(|x| InputPeerLike::PeerRef(x)),
            no_webpage: false,
            silent,
            background: false,
            clear_draft: false,
            noforwards: false,
            update_stickersets_order: false,
            invert_media,
            allow_paid_floodskip: false,
            quick_reply_shortcut: None,
            effect,
            allow_paid_stars: None,
            suggested_post: suggested_post.map(Into::into),
        })
    }
}
