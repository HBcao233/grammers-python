from typing import final, Self
from grammers.tl import TLObject

@final
class SuggestedShortName(TLObject):
    """
    [Read `stickers.suggestedShortName` docs](https://core.telegram.org/constructor/stickers.suggestedShortName).

    Generated from the following TL definition:
    ```tl
    stickers.suggestedShortName#85fea03f short_name:string = stickers.SuggestedShortName
    ```
    """
    def __new__(
        cls,
        short_name: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

