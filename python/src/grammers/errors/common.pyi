class DroppedError(Exception): ...
class DeserializeError(Exception): ...
class TransportError(Exception): ...

class SignInError(Exception):
    """
    Login-related errors.
    """

    ...

class PaymentRequiredError(SignInError):
    """
    Indicating that due to the high cost of SMS verification codes for the user's country/provider,
    the user must purchase a Telegram Premium subscription in order to proceed with the login/signup.
    """

    ...

class SignUpRequiredError(SignInError):
    """
    Sign-up with an official client is required.
    (Third-party applications cannot be used to register new accounts.)
    """

    ...

class PasswordRequiredError(SignInError):
    """
    The account has 2FA enabled, and the password is required.
    """

    ...

class InvalidCodeError(SignInError):
    """
    The code used to complete login was not valid.
    """

    ...

class InvalidPasswordError(SignInError):
    """
    The 2FA password used to complete login was not valid.
    """

    ...
