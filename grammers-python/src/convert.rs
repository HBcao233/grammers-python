#![allow(non_snake_case)]

use pyo3::PyResult;
use pyo3::exceptions::{PyTypeError, PyValueError};

use grammers_session_pyo3::{PyPeerId, PyPeerKind};
use grammers_tl_types as tl;

use crate::PyClient;

pub(crate) fn convertInputPeer2PeerId(
    peer: tl::enums::InputPeer,
    client: PyClient,
) -> PyResult<PyPeerId> {
    use tl::enums::InputPeer as E;
    Ok(match peer {
        E::Empty => {
            return Err(PyValueError::new_err(
                "InputReplyToStory.peer: InputPeerEmpty can't cast to PeerId.",
            ));
        }
        tl::enums::InputPeer::PeerSelf => client.me_ref()?.id(),
        tl::enums::InputPeer::Chat(x) => PyPeerId::chat(x.chat_id).unwrap(),
        tl::enums::InputPeer::User(x) => PyPeerId::user(x.user_id).unwrap(),
        tl::enums::InputPeer::Channel(x) => PyPeerId::channel(x.channel_id).unwrap(),
        tl::enums::InputPeer::UserFromMessage(x) => PyPeerId::user(x.user_id).unwrap(),
        tl::enums::InputPeer::ChannelFromMessage(x) => PyPeerId::channel(x.channel_id).unwrap(),
    })
}

pub(crate) fn convertPeerId2Peer(peer: PyPeerId, client: PyClient) -> PyResult<tl::enums::Peer> {
    Ok(match peer.kind() {
        PyPeerKind::User => tl::types::PeerUser {
            user_id: peer.bare_id().unwrap(),
        }
        .into(),
        PyPeerKind::UserSelf => tl::types::PeerUser {
            user_id: client.me_ref()?.id().bare_id().unwrap(),
        }
        .into(),
        PyPeerKind::Chat => tl::types::PeerChat {
            chat_id: peer.bare_id().unwrap(),
        }
        .into(),
        PyPeerKind::Channel => tl::types::PeerChannel {
            channel_id: peer.bare_id().unwrap(),
        }
        .into(),
    })
}

pub(crate) fn convertInputReplyTo2MessageReplyHeader(
    x: tl::enums::InputReplyTo,
    client: PyClient,
) -> PyResult<tl::enums::MessageReplyHeader> {
    Ok(match x {
        tl::enums::InputReplyTo::Message(x) => {
            let reply_to_peer_id = match x.reply_to_peer_id {
                Some(p) => {
                    let p = convertInputPeer2PeerId(p, client.clone())?;
                    Some(convertPeerId2Peer(p, client.clone())?)
                }
                None => None,
            };
            tl::types::MessageReplyHeader {
                reply_to_scheduled: false,
                forum_topic: false,
                quote: false,
                reply_to_msg_id: Some(x.reply_to_msg_id),
                reply_to_peer_id,
                reply_from: None,
                reply_media: None,
                reply_to_top_id: x.top_msg_id,
                quote_text: x.quote_text,
                quote_entities: x.quote_entities,
                quote_offset: x.quote_offset,
                todo_item_id: x.todo_item_id,
                poll_option: x.poll_option,
            }
            .into()
        }
        tl::enums::InputReplyTo::Story(x) => {
            let peer = convertInputPeer2PeerId(x.peer, client.clone())?;
            tl::types::MessageReplyStoryHeader {
                peer: convertPeerId2Peer(peer, client.clone())?,
                story_id: x.story_id,
            }
            .into()
        }
        tl::enums::InputReplyTo::MonoForum(_) => todo!(),
    })
}

pub fn convertPhoto2InputPhoto(photo: Option<tl::enums::Photo>) -> tl::enums::InputPhoto {
    match photo {
        None => tl::enums::InputPhoto::Empty,
        Some(x) => match x {
            tl::enums::Photo::Empty(_) => tl::enums::InputPhoto::Empty,
            tl::enums::Photo::Photo(x) => tl::types::InputPhoto {
                id: x.id,
                access_hash: x.access_hash,
                file_reference: x.file_reference,
            }
            .into(),
        },
    }
}

pub fn convertDocument2InputDocument(
    document: Option<tl::enums::Document>,
) -> tl::enums::InputDocument {
    match document {
        None => tl::enums::InputDocument::Empty,
        Some(x) => match x {
            tl::enums::Document::Empty(_) => tl::enums::InputDocument::Empty,
            tl::enums::Document::Document(x) => tl::types::InputDocument {
                id: x.id,
                access_hash: x.access_hash,
                file_reference: x.file_reference,
            }
            .into(),
        },
    }
}

pub fn convertGeoPoint2InputGeoPoint(geo_point: tl::enums::GeoPoint) -> tl::enums::InputGeoPoint {
    match geo_point {
        tl::enums::GeoPoint::Empty => tl::enums::InputGeoPoint::Empty,
        tl::enums::GeoPoint::Point(x) => tl::types::InputGeoPoint {
            lat: x.lat,
            long: x.long,
            accuracy_radius: x.accuracy_radius,
        }
        .into(),
    }
}

fn convertWebPage2Url(web_page: tl::enums::WebPage) -> String {
    match web_page {
        tl::enums::WebPage::Empty(x) => x.url.unwrap_or_default(),
        tl::enums::WebPage::Pending(x) => x.url.unwrap_or_default(),
        tl::enums::WebPage::Page(x) => x.url,
        tl::enums::WebPage::NotModified(_) => String::default(),
    }
}

pub async fn convertPeer2InputPeer(
    client: PyClient,
    peer: tl::enums::Peer,
) -> PyResult<tl::enums::InputPeer> {
    let peer_id = PyPeerId::from(peer);
    let inner = client.inner.clone();
    let peer_ref = inner.session.peer_ref(peer_id).await?;
    let mut access_hash = 0;
    if let Some(p) = peer_ref {
        access_hash = p.auth().0;
    }
    let input_peer: tl::enums::InputPeer = match peer_id.kind() {
        PyPeerKind::UserSelf => client.me_ref()?.into(),
        PyPeerKind::User => tl::types::InputPeerUser {
            user_id: peer_id.bare_id()?,
            access_hash,
        }
        .into(),
        PyPeerKind::Chat => tl::types::InputPeerChat {
            chat_id: peer_id.bare_id()?,
        }
        .into(),
        PyPeerKind::Channel => tl::types::InputPeerChannel {
            channel_id: peer_id.bare_id()?,
            access_hash,
        }
        .into(),
    };
    let access_hash = client
        .resolve_input_peer(input_peer.into())
        .await?
        .and_then(|peer| peer.auth())
        .map(|auth| auth.0)
        .unwrap_or(0);
    Ok(match peer_id.kind() {
        PyPeerKind::UserSelf => client.me_ref()?.into(),
        PyPeerKind::User => tl::types::InputPeerUser {
            user_id: peer_id.bare_id()?,
            access_hash,
        }
        .into(),
        PyPeerKind::Chat => tl::types::InputPeerChat {
            chat_id: peer_id.bare_id()?,
        }
        .into(),
        PyPeerKind::Channel => tl::types::InputPeerChannel {
            channel_id: peer_id.bare_id()?,
            access_hash,
        }
        .into(),
    })
}

pub async fn convertMessageMedia2InputMedia(
    client: PyClient,
    media: tl::enums::MessageMedia,
) -> PyResult<Option<tl::enums::InputMedia>> {
    use tl::enums::MessageMedia as M;
    Ok(Some(match media {
        M::Empty => return Ok(None),
        M::Photo(media_photo) => tl::types::InputMediaPhoto {
            spoiler: media_photo.spoiler,
            id: convertPhoto2InputPhoto(media_photo.photo),
            ttl_seconds: media_photo.ttl_seconds,
            live_photo: false,
            video: None,
        }
        .into(),
        M::Geo(media_geo) => tl::types::InputMediaGeoPoint {
            geo_point: convertGeoPoint2InputGeoPoint(media_geo.geo),
        }
        .into(),
        M::Contact(media_contact) => tl::types::InputMediaContact {
            phone_number: media_contact.phone_number,
            first_name: media_contact.first_name,
            last_name: media_contact.last_name,
            vcard: media_contact.vcard,
        }
        .into(),
        M::Unsupported => {
            return Err(PyTypeError::new_err(
                "MessageMediaUnsupported can't cast to InputMedia.",
            ));
        }
        M::Document(media_document) => tl::types::InputMediaDocument {
            spoiler: media_document.spoiler,
            id: convertDocument2InputDocument(media_document.document),
            video_cover: match convertPhoto2InputPhoto(media_document.video_cover) {
                tl::enums::InputPhoto::Empty => None,
                tl::enums::InputPhoto::Photo(x) => Some(tl::enums::InputPhoto::Photo(x)),
            },
            video_timestamp: media_document.video_timestamp,
            ttl_seconds: media_document.ttl_seconds,
            query: None,
        }
        .into(),
        M::WebPage(media_webpage) => tl::types::InputMediaWebPage {
            force_large_media: media_webpage.force_large_media,
            force_small_media: media_webpage.force_small_media,
            optional: true,
            url: convertWebPage2Url(media_webpage.webpage),
        }
        .into(),
        M::Venue(media_venue) => tl::types::InputMediaVenue {
            geo_point: convertGeoPoint2InputGeoPoint(media_venue.geo),
            title: media_venue.title,
            address: media_venue.address,
            provider: media_venue.provider,
            venue_id: media_venue.venue_id,
            venue_type: media_venue.venue_type,
        }
        .into(),
        M::Game(media_game) => {
            let (id, access_hash) = match media_game.game {
                tl::enums::Game::Game(x) => (x.id, x.access_hash),
            };
            tl::types::InputMediaGame {
                id: tl::types::InputGameId { id, access_hash }.into(),
            }
            .into()
        }
        M::Invoice(_media_invoice) => {
            return Err(PyTypeError::new_err(
                "MessageMediaInvoice can't cast to InputMedia.",
            ));
        }
        M::GeoLive(media_geolive) => tl::types::InputMediaGeoLive {
            stopped: false,
            geo_point: convertGeoPoint2InputGeoPoint(media_geolive.geo),
            heading: media_geolive.heading,
            period: Some(media_geolive.period),
            proximity_notification_radius: media_geolive.proximity_notification_radius,
        }
        .into(),
        // Not a lossless conversion
        M::Poll(media_poll) => {
            let (solution, solution_entities, solution_media) = match media_poll.results {
                tl::enums::PollResults::Results(x) => {
                    (x.solution, x.solution_entities, x.solution_media)
                }
            };
            tl::types::InputMediaPoll {
                poll: media_poll.poll,
                correct_answers: None,
                solution,
                solution_entities,
                attached_media: match media_poll.attached_media {
                    None => None,
                    Some(x) => Box::pin(convertMessageMedia2InputMedia(client.clone(), x)).await?,
                },
                solution_media: match solution_media {
                    None => None,
                    Some(x) => Box::pin(convertMessageMedia2InputMedia(client.clone(), x)).await?,
                },
            }
            .into()
        }
        M::Dice(media_dice) => tl::types::InputMediaDice {
            emoticon: media_dice.emoticon,
        }
        .into(),
        M::Story(media_story) => tl::types::InputMediaStory {
            peer: convertPeer2InputPeer(client, media_story.peer).await?,
            id: media_story.id,
        }
        .into(),
        M::Giveaway(_) => {
            return Err(PyTypeError::new_err(
                "MessageMediaGiveaway can't cast to InputMedia.",
            ));
        }
        M::GiveawayResults(_) => {
            return Err(PyTypeError::new_err(
                "MessageMediaGiveawayResults can't cast to InputMedia.",
            ));
        }
        M::PaidMedia(media_paid_media) => {
            let mut extended_media = Vec::with_capacity(media_paid_media.extended_media.len());
            for media in media_paid_media.extended_media {
                let item = convertMessageExtendedMedia2InputMedia(client.clone(), media).await.map_err(|_|
                    PyTypeError::new_err("MessageMediaPaidMedia which is not yet purchased can't case to InputMedia.")
                )?;
                if let Some(x) = item {
                    extended_media.push(x);
                }
            }
            tl::types::InputMediaPaidMedia {
                stars_amount: media_paid_media.stars_amount,
                extended_media,
                payload: None,
            }
            .into()
        }
        M::ToDo(media_todo) => tl::types::InputMediaTodo {
            todo: media_todo.todo,
        }
        .into(),
        M::VideoStream(_media_video_stream) => {
            return Err(PyTypeError::new_err(
                "MessageMediaVideoStream can't cast to InputMedia.",
            ));
        }
    }))
}

pub async fn convertMessageExtendedMedia2InputMedia(
    client: PyClient,
    media: tl::enums::MessageExtendedMedia,
) -> PyResult<Option<tl::enums::InputMedia>> {
    match media {
        tl::enums::MessageExtendedMedia::Preview(_) => Err(PyTypeError::new_err(
            "MessageExtendedMediaPreview can't cast to InputMedia.",
        )),
        tl::enums::MessageExtendedMedia::Media(x) => {
            Box::pin(convertMessageMedia2InputMedia(client.clone(), x.media)).await
        }
    }
}
