from .types import (
    DcOption,
    PeerId,
    PeerInfo,
    UpdatesState,
    UpdateState,
)
from grammers.tl import types, enums
from abc import ABC, abstractmethod

class Session(ABC):
    def __new__(cls): ...
    @abstractmethod
    async def home_dc_id(self) -> int:
        raise NotImplementedError('Session subclasses must implement home_dc_id()')

    @abstractmethod
    async def set_home_dc_id(self, dc_id: int) -> None:
        raise NotImplementedError('Session subclasses must implement set_home_dc_id()')

    @abstractmethod
    async def dc_option(self, dc_id: int) -> DcOption | None:
        raise NotImplementedError('Session subclasses must implement dc_option()')

    @abstractmethod
    async def set_dc_option(self, dc_option: DcOption) -> None:
        raise NotImplementedError('Session subclasses must implement set_dc_option()')

    @abstractmethod
    async def peer(
        self, peer: int | PeerId | enums.InputPeer | enums.Peer
    ) -> PeerInfo | None:
        raise NotImplementedError('Session subclasses must implement peer()')

    @abstractmethod
    async def cache_peer(
        self, peer_info: PeerInfo.User | PeerInfo.Chat | PeerInfo.Channel
    ) -> None:
        raise NotImplementedError('Session subclasses must implement cache_peer()')

    @abstractmethod
    async def updates_state(self) -> UpdatesState:
        raise NotImplementedError('Session subclasses must implement updates_state()')

    @abstractmethod
    async def set_update_state(
        self,
        update: UpdateState.All
        | UpdateState.Primary
        | UpdateState.Secondary
        | UpdateState.Channel,
    ) -> None:
        raise NotImplementedError(
            'Session subclasses must implement set_update_state()'
        )
