from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class BotInfo(TLObject):
    """
    [Read `bots.botInfo` docs](https://core.telegram.org/constructor/bots.botInfo).

    Generated from the following TL definition:
    ```tl
    bots.botInfo#e8a775b0 name:string about:string description:string = bots.BotInfo
    ```
    """
    def __new__(
        cls,
        name: str,
        about: str,
        description: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PopularAppBots(TLObject):
    """
    [Read `bots.popularAppBots` docs](https://core.telegram.org/constructor/bots.popularAppBots).

    Generated from the following TL definition:
    ```tl
    bots.popularAppBots#1991b13b flags:# next_offset:flags.0?string users:Vector<User> = bots.PopularAppBots
    ```
    """
    def __new__(
        cls,
        next_offset: Optional[str],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PreviewInfo(TLObject):
    """
    [Read `bots.previewInfo` docs](https://core.telegram.org/constructor/bots.previewInfo).

    Generated from the following TL definition:
    ```tl
    bots.previewInfo#ca71d64 media:Vector<BotPreviewMedia> lang_codes:Vector<string> = bots.PreviewInfo
    ```
    """
    def __new__(
        cls,
        media: Sequence[types.BotPreviewMedia],
        lang_codes: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

