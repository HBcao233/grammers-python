mod auth;
mod chats;
mod client;
mod net;
mod updates;
mod utilities;
mod messages;

pub use client::PyClient;
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
}