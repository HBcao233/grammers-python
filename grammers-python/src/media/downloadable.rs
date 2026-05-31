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
    pub fn dc_id(&self) -> Option<i32> {
        Python::attach(|py| match self {
            Self::Photo(x) => get_photo_dc_id(py, x),
            Self::MessageMediaPhoto(x) => x
                .borrow(py)
                .photo
                .as_ref()
                .and_then(|p| get_photo_dc_id(py, p)),
            Self::Document(x) => get_document_dc_id(py, x),
            Self::MessageMediaDocument(x) => x
                .borrow(py)
                .document
                .as_ref()
                .and_then(|d| get_document_dc_id(py, d)),
        })
    }

    pub fn size(&self) -> Option<i64> {
        Python::attach(|py| match self {
            Self::Photo(_) => None,
            Self::MessageMediaPhoto(_) => None,
            Self::Document(x) => get_document_size(py, x),
            Self::MessageMediaDocument(x) => x
                .borrow(py)
                .document
                .as_ref()
                .and_then(|d| get_document_size(py, d)),
        })
    }

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

fn get_photo_dc_id(py: Python<'_>, x: &pytl::enums::PyPhoto) -> Option<i32> {
    use pytl::enums::PyPhoto as P;

    match x {
        P::Empty(_) => None,
        P::Photo(photo) => Some(photo.0.borrow(py).dc_id),
    }
}

fn get_document_dc_id(py: Python<'_>, x: &pytl::enums::PyDocument) -> Option<i32> {
    use pytl::enums::PyDocument as D;

    match x {
        D::Empty(_) => None,
        D::Document(document) => Some(document.0.borrow(py).dc_id),
    }
}

fn get_document_size(py: Python<'_>, x: &pytl::enums::PyDocument) -> Option<i64> {
    use pytl::enums::PyDocument as D;

    match x {
        D::Empty(_) => None,
        D::Document(document) => Some(document.0.borrow(py).size),
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
