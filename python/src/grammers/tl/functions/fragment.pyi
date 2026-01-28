from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class GetCollectibleInfo(TLRequest):
    """
    [Read `fragment.getCollectibleInfo` docs](https://core.telegram.org/method/fragment.getCollectibleInfo).

    Generated from the following TL definition:
    ```tl
    fragment.getCollectibleInfo#be1e85ba collectible:InputCollectible = fragment.CollectibleInfo
    ```
    """
    def __new__(
        cls,
        collectible: types.InputCollectibleUsername | types.InputCollectiblePhone,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

