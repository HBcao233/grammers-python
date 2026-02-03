from .tl import types
from .sessions import PeerIdLike

Phone = str
Username = str
InviteLink = str
InputPeerLike = Phone | Username | types.InputPeer | PeerIdLike
