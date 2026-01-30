from typing import final, Self
from grammers.tl import TLObject

@final
class CollectibleInfo(TLObject):
    """
    [Read `fragment.collectibleInfo` docs](https://core.telegram.org/constructor/fragment.collectibleInfo).

    Generated from the following TL definition:
    ```tl
    fragment.collectibleInfo#6ebdff91 purchase_date:int currency:string amount:long crypto_currency:string crypto_amount:long url:string = fragment.CollectibleInfo
    ```
    """
    def __new__(
        cls,
        purchase_date: int,
        currency: str,
        amount: int,
        crypto_currency: str,
        crypto_amount: int,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

