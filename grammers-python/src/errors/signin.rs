use pyo3::PyErr;
use pyo3::create_exception;
use pyo3::exceptions::PyException;

create_exception!(
    grammers.errors,
    SignInError,
    PyException,
    "Login-related errors."
);
create_exception!(
    grammers.errors,
    PaymentRequiredError,
    SignInError,
    "Indicating that due to the high cost of SMS verification codes for the user's country/provider, the user must purchase a Telegram Premium subscription in order to proceed with the login/signup."
);
create_exception!(
    grammers.errors,
    SignUpRequiredError,
    SignInError,
    "Sign-up with an official client is required. (Third-party applications cannot be used to register new accounts.)"
);
create_exception!(
    grammers.errors,
    PasswordRequiredError,
    SignInError,
    "The account has 2FA enabled, and the password is required."
);
create_exception!(
    grammers.errors,
    InvalidCodeError,
    SignInError,
    "The code used to complete login was not valid."
);
create_exception!(
    grammers.errors,
    InvalidPasswordError,
    SignInError,
    "The 2FA password used to complete login was not valid."
);

pub struct PyPaymentRequiredError {}
impl PyPaymentRequiredError {
    pub fn new() -> PyErr {
        PaymentRequiredError::new_err(
            "Indicating that due to the high cost of SMS verification codes for the user's country/provider, the user must purchase a Telegram Premium subscription in order to proceed with the login/signup.",
        )
    }
}

pub struct PySignUpRequiredError {}
impl PySignUpRequiredError {
    pub fn new() -> PyErr {
        SignUpRequiredError::new_err(
            "Sign-up with an official client is required. (Third-party applications cannot be used to register new accounts.)",
        )
    }
}

pub struct PyPasswordRequiredError {}
impl PyPasswordRequiredError {
    pub fn new() -> PyErr {
        PasswordRequiredError::new_err("The account has 2FA enabled, and the password is required.")
    }
}

pub struct PyInvalidCodeError {}
impl PyInvalidCodeError {
    pub fn new() -> PyErr {
        InvalidCodeError::new_err("The code used to complete login was not valid.")
    }
}

pub struct PyInvalidPasswordError {}
impl PyInvalidPasswordError {
    pub fn new() -> PyErr {
        InvalidPasswordError::new_err("The 2FA password used to complete login was not valid.")
    }
}
