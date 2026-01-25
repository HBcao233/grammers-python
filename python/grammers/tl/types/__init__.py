from grammers._rs.tl.types import *

InputPeer = (
    InputPeerEmpty
    | InputPeerSelf
    | InputPeerChat
    | InputPeerUser
    | InputPeerChannel
    | InputPeerUserFromMessage
    | InputPeerChannelFromMessage
)

Peer = PeerUser | PeerChat | PeerChannel
