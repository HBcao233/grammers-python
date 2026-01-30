from typing import final, Self, Optional
from grammers.tl import TLRequest, types

@final
class GetState(TLRequest):
    """
    [Read `updates.getState` docs](https://core.telegram.org/method/updates.getState).

    Generated from the following TL definition:
    ```tl
    updates.getState#edd4882a = updates.State
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDifference(TLRequest):
    """
    [Read `updates.getDifference` docs](https://core.telegram.org/method/updates.getDifference).

    Generated from the following TL definition:
    ```tl
    updates.getDifference#19c2f763 flags:# pts:int pts_limit:flags.1?int pts_total_limit:flags.0?int date:int qts:int qts_limit:flags.2?int = updates.Difference
    ```
    """
    def __new__(
        cls,
        pts: int,
        pts_limit: Optional[int],
        pts_total_limit: Optional[int],
        date: int,
        qts: int,
        qts_limit: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetChannelDifference(TLRequest):
    """
    [Read `updates.getChannelDifference` docs](https://core.telegram.org/method/updates.getChannelDifference).

    Generated from the following TL definition:
    ```tl
    updates.getChannelDifference#3173d78 flags:# force:flags.0?true channel:InputChannel filter:ChannelMessagesFilter pts:int limit:int = updates.ChannelDifference
    ```
    """
    def __new__(
        cls,
        force: bool,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        filter: types.ChannelMessagesFilterEmpty | types.ChannelMessagesFilter,
        pts: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

