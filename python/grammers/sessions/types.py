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

PeerIdLike = int | PeerId | types.InputPeer | types.Peer
