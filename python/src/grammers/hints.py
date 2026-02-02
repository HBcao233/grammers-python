from .tl import types
from .sessions import PeerIdLike

Phone = str
Username = str
EntityLike = (
    Phone
    | Username
    | PeerIdLike
    | types.InputPeerEmpty
    | types.InputPeerUserFromMessage
    | types.InputPeerChannelFromMessage
)
