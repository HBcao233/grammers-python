from grammers._rs.client import (
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
)

Peer = User | Group | Channel

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
]
