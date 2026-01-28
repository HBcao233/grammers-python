from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class GetBoostsList(TLRequest):
    """
    [Read `premium.getBoostsList` docs](https://core.telegram.org/method/premium.getBoostsList).

    Generated from the following TL definition:
    ```tl
    premium.getBoostsList#60f67660 flags:# gifts:flags.0?true peer:InputPeer offset:string limit:int = premium.BoostsList
    ```
    """
    def __new__(
        cls,
        gifts: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        offset: str,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMyBoosts(TLRequest):
    """
    [Read `premium.getMyBoosts` docs](https://core.telegram.org/method/premium.getMyBoosts).

    Generated from the following TL definition:
    ```tl
    premium.getMyBoosts#be77b4a = premium.MyBoosts
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ApplyBoost(TLRequest):
    """
    [Read `premium.applyBoost` docs](https://core.telegram.org/method/premium.applyBoost).

    Generated from the following TL definition:
    ```tl
    premium.applyBoost#6b7da746 flags:# slots:flags.0?Vector<int> peer:InputPeer = premium.MyBoosts
    ```
    """
    def __new__(
        cls,
        slots: Optional[Sequence[int]],
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetBoostsStatus(TLRequest):
    """
    [Read `premium.getBoostsStatus` docs](https://core.telegram.org/method/premium.getBoostsStatus).

    Generated from the following TL definition:
    ```tl
    premium.getBoostsStatus#42f1f61 peer:InputPeer = premium.BoostsStatus
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetUserBoosts(TLRequest):
    """
    [Read `premium.getUserBoosts` docs](https://core.telegram.org/method/premium.getUserBoosts).

    Generated from the following TL definition:
    ```tl
    premium.getUserBoosts#39854d1f peer:InputPeer user_id:InputUser = premium.BoostsList
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

