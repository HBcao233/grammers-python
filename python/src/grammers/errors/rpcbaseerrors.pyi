from typing import Self

class RpcError(Exception):
    """
    Base class for all Remote Procedure Call errors.
    """
    def __new__(
        cls,
        code: int,
        name: str,
        value: int | None = None,
        caused_by: int | None = None,
        message: str | None = None,
    ) -> Self: ...
    @property
    def code(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int | None: ...
    @property
    def caused_by(self) -> int | None: ...
    @property
    def message(self) -> str | None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class InvalidDCError(RpcError):
    """
    The request must be repeated, but directed to a different data center.
    """

    code = 303
    message = 'ERROR_SEE_OTHER'
    @property
    def new_dc(self) -> int | None: ...
    def __new__(
        cls,
        name: str,
        value: int | None = None,
        caused_by: int | None = None,
        message: str | None = None,
    ) -> Self: ...

class BadRequestError(RpcError):
    """
    The query contains errors. In the event that a request was created
    using a form and contains user generated data, the user should be
    notified that the data must be corrected before the query is repeated.
    """

    code = 400
    message = 'BAD_REQUEST'
    def __new__(
        cls,
        name: str,
        value: int | None = None,
        caused_by: int | None = None,
        message: str | None = None,
    ) -> Self: ...

class UnauthorizedError(RpcError):
    """
    There was an unauthorized attempt to use functionality available only
    to authorized users.
    """

    code = 401
    message = 'UNAUTHORIZED'
    def __new__(
        cls,
        name: str,
        value: int | None = None,
        caused_by: int | None = None,
        message: str | None = None,
    ) -> Self: ...

class ForbiddenError(RpcError):
    """
    Privacy violation. For example, an attempt to write a message to
    someone who has blacklisted the current user.
    """

    code = 403
    message = 'FORBIDDEN'
    def __new__(
        cls,
        name: str,
        value: int | None = None,
        caused_by: int | None = None,
        message: str | None = None,
    ) -> Self: ...

class NotFoundError(RpcError):
    """
    An attempt to invoke a non-existent object, such as a method.
    """

    code = 404
    message = 'NOT_FOUND'
    def __new__(
        cls,
        name: str,
        value: int | None = None,
        caused_by: int | None = None,
        message: str | None = None,
    ) -> Self: ...

class AuthKeyError(RpcError):
    """
    Errors related to invalid authorization key, like
    AUTH_KEY_DUPLICATED which can cause the connection to fail.
    """

    code = 406
    message = 'AUTH_KEY'
    def __new__(
        cls,
        name: str,
        value: int | None = None,
        caused_by: int | None = None,
        message: str | None = None,
    ) -> Self: ...

class FloodError(RpcError):
    """
    The maximum allowed number of attempts to invoke the given method
    with the given input parameters has been exceeded. For example, in an
    attempt to request a large number of text messages (SMS) for the same
    phone number.
    """

    code = 420
    message = 'FLOOD'
    @property
    def seconds(self) -> int | None: ...
    def __new__(
        cls,
        name: str,
        value: int | None = None,
        caused_by: int | None = None,
        message: str | None = None,
    ) -> Self: ...

class ServerError(RpcError):
    """
    An internal server error occurred while a request was being processed
    for example, there was a disruption while accessing a database or file
    storage.
    """

    code = 500  # Also witnessed as -500
    message = 'INTERNAL'
    def __new__(
        cls,
        name: str,
        value: int | None = None,
        caused_by: int | None = None,
        message: str | None = None,
    ) -> Self: ...

class TimedOutError(RpcError):
    """
    Clicking the inline buttons of bots that never (or take to long to)
    call ``answerCallbackQuery`` will result in this "special" RpcError.
    """

    code = 503  # Only witnessed as -503
    message = 'Timeout'
    def __new__(
        cls,
        name: str,
        value: int | None = None,
        caused_by: int | None = None,
        message: str | None = None,
    ) -> Self: ...
