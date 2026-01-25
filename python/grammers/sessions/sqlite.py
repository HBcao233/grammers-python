from .session import Session
from .types import (
    DcOption, 
    PeerId, 
    PeerInfo, 
    UpdatesState, 
    UpdateState,
)

from grammers.tl import types


class SqliteSession(Session):
    def __new__(cls, path: str):
        instance = super().__new__(cls)
        instance.path = path
        return instance

    async def home_dc_id(self) -> int:
        pass

    async def set_home_dc_id(self, dc_id: int) -> None:
        pass

    async def dc_option(self, dc_id: int) -> DcOption | None:
        pass

    async def set_dc_option(self, dc_option: DcOption) -> None:
        pass

    async def peer(
        self, peer: int | PeerId | types.InputPeer | types.Peer
    ) -> PeerInfo | None:
        pass

    async def cache_peer(self, peer_info: PeerInfo) -> None:
        pass

    async def updates_state(self) -> UpdatesState:
        pass

    async def set_update_state(self, update: UpdateState) -> None:
        pass
