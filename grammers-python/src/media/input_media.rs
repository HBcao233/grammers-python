use pyo3::PyResult;
use pyo3::exceptions::PyTypeError;

use grammers_tl_types as tl;
use grammers_session_pyo3::PyPeerKind;

use crate::PyClient;


pub fn convertPhoto2InputPhoto(photo: Option<tl::enums::Photo>) -> tl::enums::InputPhoto {
    match photo {
        None => tl::enums::InputPhoto::Empty,
        Some(x) => match x {
            tl::enums::Photo::Empty(_) => tl::enums::InputPhoto::Empty,
            tl::enums::Photo::Photo(x) => tl::types::InputPhoto {
                id: x.id,
                access_hash: x.access_hash,
                file_reference: x.file_reference,
            }.into(),
        },
    }
}

pub fn convertDocument2InputDocument(document: Option<tl::enums::Document>) -> tl::enums::InputDocument {
    match document {
        None => tl::enums::InputDocument::Empty,
        Some(x) => match x {
            tl::enums::Document::Empty(_) => tl::enums::InputDocument::Empty,
            tl::enums::Document::Document(x) => tl::types::InputDocument {
                id: x.id,
                access_hash: x.access_hash,
                file_reference: x.file_reference,
            }.into(),
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
        }.into(),
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

pub async fn convertPeer2InputPeer(client: PyClient, peer: tl::enums::Peer) -> PyResult<tl::enums::InputPeer> {
    let peer_id = PyPeerId::from(peer);
    let session = client.session();
    let peer_ref = session.peer_ref(peer_id).await?;
    let mut access_hash = 0;
    if let Some(p) = peer_ref {
        access_hash = p.auth().0;
    }
    let input_peer = match peer_id.kind() {
        PyPeerKind::User => tl::types::InputPeerUser {
            user_id: peer_id.bare_id(),
            access_hash,
        }.into(),
        PyPeerKind::Chat => tl::types::InputPeerUser {
            chat_id: peer_id.bare_id(),
        }.into(),
        PyPeerKind::Channel => tl::types::InputPeerUser {
            channel_id: peer_id.bare_id(),
            access_hash,
        }.into(),
    };
    let access_hash = client.resolve_input_peer(input_peer).await
        .ok()
        .map(|peer| Python::attach(|py| peer.borrow(py).auth().hash()));
    match peer_id.kind() {
        PyPeerKind::User => tl::types::InputPeerUser {
            user_id: peer_id.bare_id(),
            access_hash,
        }.into(),
        PyPeerKind::Chat => tl::types::InputPeerUser {
            chat_id: peer_id.bare_id(),
        }.into(),
        PyPeerKind::Channel => tl::types::InputPeerUser {
            channel_id: peer_id.bare_id(),
            access_hash,
        }.into(),
    }
}

pub async fn convertMessageMedia2InputMedia(client: PyClient, media: tl::enums::MessageMedia) -> PyResult<Option<tl::enums::InputMedia>> {
    use tl::enums::MessageMedia as M;
    Ok(Some(match media {
        M::Empty => None,
        M::Photo(media_photo) => tl::types::InputMediaPhoto {
            spoiler: media_photo.spoiler,
            id: convertPhoto2InputPhoto(media_photo.photo),
            ttl_seconds: media_photo.ttl_seconds,
            live_photo: false,
            video: None,
        }.into(),
        M::Geo(media_geo) => tl::types::InputMediaGeoPoint {
            geo_point: convertGeoPoint2InputGeoPoint(media_geo.geo),
        }.into(),
        M::Contact(media_contact) => tl::types::InputMediaContact {
            phone_number: media_contact.phone_number,
            first_name: media_contact.first_name,
            last_name: media_contact.last_name,
            vcard: media_contact.vcard,
        }.into(),
        M::Unsupported => return Err(PyTypeError::new_err("MessageMediaUnsupported can't cast to InputMedia.")),
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
        }.into(),
        M::WebPage(media_webpage) => tl::types::InputMediaWebPage {
            force_large_media: media_webpage.force_large_media,
            force_small_media: media_webpage.force_small_media,
            optional: true,
            url: convertWebPage2Url(media_webpage.webpage),
        }.into(),
        M::Venue(media_venue) => tl::types::InputMediaVenue {
            geo_point: convertGeoPoint2InputGeoPoint(media_venue.geo),
            title: media_venue.title,
            address: media_venue.address,
            provider: media_venue.provider,
            venue_id: media_venue.venue_id,
            venue_type: media_venue.venue_type,
        }.into(),
        M::Game(media_game) => {
            let (id, access_hash) = match media_game.game {
                tl::enums::Game::Game(x) => (x.id, x.access_hash),
            };
            tl::types::InputMediaGame {
                id: tl::types::InputGameId {
                    id,
                    access_hash,
                }.into(),
            }.into()
        },
        M::Invoice(media_invoice) => return Err(PyTypeError::new_err("MessageMediaInvoice can't cast to InputMedia.")),
        M::GeoLive(media_geolive) => tl::types::InputMediaGeoLive {
            stopped: false,
            geo_point: convertGeoPoint2InputGeoPoint(media_geolive.geo),
            heading: media_geolive.heading,
            period: Some(media_geolive.period),
            proximity_notification_radius: media_geolive.proximity_notification_radius,
        }.into(),
        // Not a lossless conversion
        M::Poll(media_poll) => {
            let (
                solution,
                solution_entities,
                solution_media,
            ) = match media_poll.results {
                tl::enums::PollResults::Results(x) => (
                    x.solution,
                    x.solution_entities,
                    x.solution_media,
                ),
            };
            tl::types::InputMediaPoll {
                poll: media_poll.poll,
                correct_answers: None,
                solution,
                solution_entities,
                attached_media: match media_poll.attached_media {
                    None => None,
                    Some(x) => convertMessageMedia2InputMedia(client, x).await?,
                },
                solution_media: match solution_media {
                    None => None,
                    Some(x) => convertMessageMedia2InputMedia(client, x).await?,
                },
            }.into()
        },
        M::Dice(media_dice) => tl::types::InputMediaDice {
            emoticon: media_dice.emoticon,
        }.into(),
        M::Story(media_story) => tl::types::InputMediaStory {
            peer: convertPeer2InputPeer(client, media_story.peer).await?,
            id: media_story.id,
        }.into(),
        M::Giveaway(_) => return Err(PyTypeError::new_err("MessageMediaGiveaway can't cast to InputMedia.")),
        M::GiveawayResults(_) => return Err(PyTypeError::new_err("MessageMediaGiveawayResults can't cast to InputMedia.")),
        M::PaidMedia(media_paid_media) => {
            let extended_media = Vec::with_capacity(media_paid_media.extended_media.len());
            for media in media_paid_media.extended_media {
                let item = convertMessageExtendedMedia2InputMedia(client, media).await.map_err(|_|
                    PyTypeError::new_err("MessageMediaPaidMedia which is not yet purchased can't case to InputMedia.")
                )?;
                extended_media.push(item);
            }
            tl::types::InputMediaPaidMedia {
                stars_amount: media_paid_media.stars_amount,
                extended_media,
                payload: None,
            }.into()
        },
        M::ToDo(media_todo) => tl::types::InputMediaTodo {
            todo: media_todo.todo,
        }.into(),
        M::VideoStream(media_video_stream) => return Err(PyTypeError::new_err("MessageMediaVideoStream can't cast to InputMedia.")),
    }))
}

pub async fn convertMessageExtendedMedia2InputMedia(client: PyClient, media: tl::enums::MessageExtendedMedia) -> PyResult<tl::enums::InputMedia> {
    match media {
        tl::enums::MessageExtendedMedia::Preview(_) => Err(PyTypeError::new_err("MessageExtendedMediaPreview can't cast to InputMedia.")),
        tl::enums::MessageExtendedMedia::Media(x) => convertMessageMedia2InputMedia(client, x.media).await,
    }
}
