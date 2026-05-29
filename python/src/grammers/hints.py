from grammers import custom
from grammers.tl import types, enums
from grammers.sessions import PeerIdLike

from typing import TypeAlias

Phone: TypeAlias = str
Username: TypeAlias = str
InviteLink: TypeAlias = str
InputPeerLike: TypeAlias = Phone | Username | enums.InputPeer | PeerIdLike
Peer: TypeAlias = custom.User | custom.Group | custom.Channel

MsgId: TypeAlias = int
InputReplyToLike: TypeAlias = MsgId | enums.InputReplyTo
InputMessageLike: TypeAlias = str | custom.Message

Downloadable: TypeAlias = (
    enums.Photo | types.MessageMediaPhoto | enums.Document | types.MessageMediaDocument
)
