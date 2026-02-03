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

PeerIdLike = int | PeerId

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
