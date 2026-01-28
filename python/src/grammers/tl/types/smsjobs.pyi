from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class EligibleToJoin(TLObject):
    """
    [Read `smsjobs.eligibleToJoin` docs](https://core.telegram.org/constructor/smsjobs.eligibleToJoin).

    Generated from the following TL definition:
    ```tl
    smsjobs.eligibleToJoin#dc8b44cf terms_url:string monthly_sent_sms:int = smsjobs.EligibilityToJoin
    ```
    """
    def __new__(
        cls,
        terms_url: str,
        monthly_sent_sms: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Status(TLObject):
    """
    [Read `smsjobs.status` docs](https://core.telegram.org/constructor/smsjobs.status).

    Generated from the following TL definition:
    ```tl
    smsjobs.status#2aee9191 flags:# allow_international:flags.0?true recent_sent:int recent_since:int recent_remains:int total_sent:int total_since:int last_gift_slug:flags.1?string terms_url:string = smsjobs.Status
    ```
    """
    def __new__(
        cls,
        allow_international: bool,
        recent_sent: int,
        recent_since: int,
        recent_remains: int,
        total_sent: int,
        total_since: int,
        last_gift_slug: Optional[str],
        terms_url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

