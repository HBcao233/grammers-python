from grammers._rs.sessions import (
    PeerId,
    PeerAuth,
    PeerInfo,
    PeerKind,
    PeerRef,
    ChannelKind,
    DcOption,
    ChannelState,
    UpdatesState,
    UpdateState,
)
from grammers.tl import enums
from typing import TypeAlias

PeerIdLike: TypeAlias = int | PeerId | enums.InputPeer | enums.Peer

__all__ = [
    'PeerId',
    'PeerIdLike',
    'PeerAuth',
    'PeerInfo',
    'PeerKind',
    'PeerRef',
    'ChannelKind',
    'DcOption',
    'ChannelState',
    'UpdatesState',
    'UpdateState',
]
