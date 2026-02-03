from .tl import types
from .sessions import PeerIdLike

Phone = str
Username = str
PeerIdLikeExtend = (
    PeerIdLike
    | types.InputPeerUserFromMessage
    | types.InputPeerChannelFromMessage
)
EntityLike = (
    Phone
    | Username
    | PeerIdLikeExtend
)
