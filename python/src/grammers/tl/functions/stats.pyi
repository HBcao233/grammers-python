from typing import final, Self, Optional
from grammers.tl import TLRequest, types

@final
class GetBroadcastStats(TLRequest):
    """
    [Read `stats.getBroadcastStats` docs](https://core.telegram.org/method/stats.getBroadcastStats).

    Generated from the following TL definition:
    ```tl
    stats.getBroadcastStats#ab42441a flags:# dark:flags.0?true channel:InputChannel = stats.BroadcastStats
    ```
    """
    def __new__(
        cls,
        dark: bool,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LoadAsyncGraph(TLRequest):
    """
    [Read `stats.loadAsyncGraph` docs](https://core.telegram.org/method/stats.loadAsyncGraph).

    Generated from the following TL definition:
    ```tl
    stats.loadAsyncGraph#621d5fa0 flags:# token:string x:flags.0?long = StatsGraph
    ```
    """
    def __new__(
        cls,
        token: str,
        x: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMegagroupStats(TLRequest):
    """
    [Read `stats.getMegagroupStats` docs](https://core.telegram.org/method/stats.getMegagroupStats).

    Generated from the following TL definition:
    ```tl
    stats.getMegagroupStats#dcdf8607 flags:# dark:flags.0?true channel:InputChannel = stats.MegagroupStats
    ```
    """
    def __new__(
        cls,
        dark: bool,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMessagePublicForwards(TLRequest):
    """
    [Read `stats.getMessagePublicForwards` docs](https://core.telegram.org/method/stats.getMessagePublicForwards).

    Generated from the following TL definition:
    ```tl
    stats.getMessagePublicForwards#5f150144 channel:InputChannel msg_id:int offset:string limit:int = stats.PublicForwards
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        msg_id: int,
        offset: str,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMessageStats(TLRequest):
    """
    [Read `stats.getMessageStats` docs](https://core.telegram.org/method/stats.getMessageStats).

    Generated from the following TL definition:
    ```tl
    stats.getMessageStats#b6e0a3f5 flags:# dark:flags.0?true channel:InputChannel msg_id:int = stats.MessageStats
    ```
    """
    def __new__(
        cls,
        dark: bool,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStoryStats(TLRequest):
    """
    [Read `stats.getStoryStats` docs](https://core.telegram.org/method/stats.getStoryStats).

    Generated from the following TL definition:
    ```tl
    stats.getStoryStats#374fef40 flags:# dark:flags.0?true peer:InputPeer id:int = stats.StoryStats
    ```
    """
    def __new__(
        cls,
        dark: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStoryPublicForwards(TLRequest):
    """
    [Read `stats.getStoryPublicForwards` docs](https://core.telegram.org/method/stats.getStoryPublicForwards).

    Generated from the following TL definition:
    ```tl
    stats.getStoryPublicForwards#a6437ef6 peer:InputPeer id:int offset:string limit:int = stats.PublicForwards
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
        offset: str,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

