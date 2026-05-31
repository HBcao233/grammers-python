from grammers._rs.custom import (
    LoginToken,
    SignInError,
    PaymentRequiredError,
    SignUpRequiredError,
    PasswordRequiredError,
    InvalidCodeError,
    InvalidPasswordError,
    User,
    Group,
    Channel,
    PeerMap,
    Platform,
    RestrictionReason,
    Message,
    HistoryMessageIter,
    DownloadIter,
    ProgressUpdate,
)

MIN_CHUNK_SIZE: int = 4 * 1024
MAX_CHUNK_SIZE: int = 512 * 1024

__all__ = [
    'LoginToken',
    'SignInError',
    'PaymentRequiredError',
    'SignUpRequiredError',
    'PasswordRequiredError',
    'InvalidCodeError',
    'InvalidPasswordError',
    'User',
    'Group',
    'Channel',
    'PeerMap',
    'Platform',
    'RestrictionReason',
    'Message',
    'HistoryMessageIter',
    'DownloadIter',
    'ProgressUpdate',
]
