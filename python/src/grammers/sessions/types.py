from grammers._rs.sessions import (
    PeerId,
    PeerAuth,
    PeerInfo,
    PeerKind,
    ChannelKind,
    DcOption,
    ChannelState,
    UpdatesState,
    UpdateState,
)
from grammers.tl import types

PeerIdLike = (
    int
    | PeerId
    | types.InputPeerSelf
    | types.InputPeerChat
    | types.InputPeerUser
    | types.InputPeerChannel
    | types.Peer
    | types.Entity
    | types.FullEntity
)

__all__ = [
    'PeerId',
    'PeerIdLike',
    'PeerAuth',
    'PeerInfo',
    'PeerKind',
    'ChannelKind',
    'DcOption',
    'ChannelState',
    'UpdatesState',
    'UpdateState',
]
