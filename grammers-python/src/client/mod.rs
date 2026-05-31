mod auth;
mod chats;
mod client;
mod events;
mod files;
mod iter_buffer;
mod messages;
mod net;
mod updates;
mod utilities;

pub(crate) use auth::{
    InvalidCodeError, InvalidPasswordError, PasswordRequiredError, PaymentRequiredError,
    PyLoginToken, SignInError, SignUpRequiredError,
};
pub use client::PyClient;
pub(crate) use files::{PyDownloadIter, PyProgressUpdate};
use iter_buffer::IterBuffer;
pub(crate) use messages::PyHistoryMessageIter;
pub(crate) use updates::UpdateStream;
use updates::UpdatesConfiguration;

#[pyo3::pymodule(name = "client")]
pub(crate) mod client_ {
    #[pymodule_export]
    use super::PyClient;
}
