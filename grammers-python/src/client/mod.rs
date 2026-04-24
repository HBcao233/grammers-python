mod auth;
mod chats;
mod client;
mod iter_buffer;
mod messages;
mod net;
mod updates;
mod utilities;

pub use client::PyClient;
use iter_buffer::IterBuffer;
use updates::{UpdateStream, UpdatesConfiguration};

#[pyo3::pymodule(name = "client")]
pub(crate) mod client_ {
    #[pymodule_export]
    use super::auth::PyLoginToken;

    #[pymodule_export]
    use super::PyClient;

    #[pymodule_export]
    use super::auth::SignInError;

    #[pymodule_export]
    use super::auth::PaymentRequiredError;

    #[pymodule_export]
    use super::auth::SignUpRequiredError;

    #[pymodule_export]
    use super::auth::PasswordRequiredError;

    #[pymodule_export]
    use super::auth::InvalidCodeError;

    #[pymodule_export]
    use super::auth::InvalidPasswordError;

    #[pymodule_export]
    use crate::peer::PyUser;

    #[pymodule_export]
    use crate::peer::PyGroup;

    #[pymodule_export]
    use crate::peer::PyChannel;

    #[pymodule_export]
    use crate::peer::PyPlatform;

    #[pymodule_export]
    use crate::peer::PyRestrictionReason;

    #[pymodule_export]
    use crate::peer::PyPeerMap;

    #[pymodule_export]
    use crate::message::PyMessage;

    #[pymodule_export]
    use crate::client::messages::PyHistoryMessageIter;
}
