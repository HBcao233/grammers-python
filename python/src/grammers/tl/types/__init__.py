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

_Peer = PeerUser | PeerChat | PeerChannel

Entity = (
    UserEmpty | User | ChatEmpty | Chat | ChatForbidden | Channel | ChannelForbidden
)
FullEntity = UserFull | messages.ChatFull | ChatFull | ChannelFull
