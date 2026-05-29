use pyo3::{FromPyObject, Py, Python};

use grammers_tl_types as tl;
use grammers_tl_types_pyo3 as pytl;

use super::PhotoSize;

#[derive(FromPyObject)]
pub enum Downloadable {
    Photo(pytl::enums::PyPhoto),
    MessageMediaPhoto(Py<pytl::types::PyMessageMediaPhoto>),
    Document(pytl::enums::PyDocument),
    MessageMediaDocument(Py<pytl::types::PyMessageMediaDocument>),
}

impl Downloadable {
    pub fn into_raw_input_location(self) -> Option<tl::enums::InputFileLocation> {
        match self {
            Self::Photo(x) => convertPhoto2InputFileLocation(x.into()),
            Self::MessageMediaPhoto(x) => Python::attach(|py| x.borrow(py).photo.clone())
                .and_then(|x| convertPhoto2InputFileLocation(x.into())),
            Self::Document(x) => convertDocument2InputFileLocation(x.into()),
            Self::MessageMediaDocument(x) => Python::attach(|py| x.borrow(py).document.clone())
                .and_then(|x| convertDocument2InputFileLocation(x.into())),
        }
    }
}

fn convertPhoto2InputFileLocation(photo: tl::enums::Photo) -> Option<tl::enums::InputFileLocation> {
    use tl::enums::Photo as P;
    match &photo {
        P::Empty(_) => None,
        P::Photo(photo) => Some(
            tl::types::InputPhotoFileLocation {
                id: photo.id,
                access_hash: photo.access_hash,
                file_reference: photo.file_reference.clone(),
                thumb_size: photo
                    .sizes
                    .iter()
                    .map(|x| PhotoSize::make_from(x, photo))
                    .max_by_key(|x| x.size())
                    .map(|ps| ps.photo_type())
                    .unwrap_or(String::from("w")),
            }
            .into(),
        ),
    }
}

fn convertDocument2InputFileLocation(
    document: tl::enums::Document,
) -> Option<tl::enums::InputFileLocation> {
    use tl::enums::Document as D;

    match document {
        D::Empty(_) => None,
        D::Document(document) => Some(
            tl::types::InputDocumentFileLocation {
                id: document.id,
                access_hash: document.access_hash,
                file_reference: document.file_reference.clone(),
                thumb_size: String::new(),
            }
            .into(),
        ),
    }
}
