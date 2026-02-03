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

Peer = UserEmpty | User | ChatEmpty | Chat | ChatForbidden | Channel | ChannelForbidden
PeerFull = UserFull | messages.ChatFull | ChatFull | ChannelFull
