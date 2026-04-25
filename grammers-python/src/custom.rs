#[pyo3::pymodule(name = "custom")]
pub(crate) mod custom_ {
    #[pymodule_export]
    use crate::client::PyLoginToken;

    #[pymodule_export]
    use crate::client::SignInError;

    #[pymodule_export]
    use crate::client::PaymentRequiredError;

    #[pymodule_export]
    use crate::client::SignUpRequiredError;

    #[pymodule_export]
    use crate::client::PasswordRequiredError;

    #[pymodule_export]
    use crate::client::InvalidCodeError;

    #[pymodule_export]
    use crate::client::InvalidPasswordError;

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
    use crate::client::PyHistoryMessageIter;
}
