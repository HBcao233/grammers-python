from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class BoostsList(TLObject):
    """
    [Read `premium.boostsList` docs](https://core.telegram.org/constructor/premium.boostsList).

    Generated from the following TL definition:
    ```tl
    premium.boostsList#86f8613c flags:# count:int boosts:Vector<Boost> next_offset:flags.0?string users:Vector<User> = premium.BoostsList
    ```
    """
    def __new__(
        cls,
        count: int,
        boosts: Sequence[types.Boost],
        next_offset: Optional[str],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MyBoosts(TLObject):
    """
    [Read `premium.myBoosts` docs](https://core.telegram.org/constructor/premium.myBoosts).

    Generated from the following TL definition:
    ```tl
    premium.myBoosts#9ae228e2 my_boosts:Vector<MyBoost> chats:Vector<Chat> users:Vector<User> = premium.MyBoosts
    ```
    """
    def __new__(
        cls,
        my_boosts: Sequence[types.MyBoost],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BoostsStatus(TLObject):
    """
    [Read `premium.boostsStatus` docs](https://core.telegram.org/constructor/premium.boostsStatus).

    Generated from the following TL definition:
    ```tl
    premium.boostsStatus#4959427a flags:# my_boost:flags.2?true level:int current_level_boosts:int boosts:int gift_boosts:flags.4?int next_level_boosts:flags.0?int premium_audience:flags.1?StatsPercentValue boost_url:string prepaid_giveaways:flags.3?Vector<PrepaidGiveaway> my_boost_slots:flags.2?Vector<int> = premium.BoostsStatus
    ```
    """
    def __new__(
        cls,
        my_boost: bool,
        level: int,
        current_level_boosts: int,
        boosts: int,
        gift_boosts: Optional[int],
        next_level_boosts: Optional[int],
        premium_audience: Optional[types.StatsPercentValue],
        boost_url: str,
        prepaid_giveaways: Optional[Sequence[types.PrepaidGiveaway | types.PrepaidStarsGiveaway]],
        my_boost_slots: Optional[Sequence[int]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

