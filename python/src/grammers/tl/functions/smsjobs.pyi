from typing import final, Self, Optional
from grammers.tl import TLRequest

@final
class IsEligibleToJoin(TLRequest):
    """
    [Read `smsjobs.isEligibleToJoin` docs](https://core.telegram.org/method/smsjobs.isEligibleToJoin).

    Generated from the following TL definition:
    ```tl
    smsjobs.isEligibleToJoin#edc39d0 = smsjobs.EligibilityToJoin
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Join(TLRequest):
    """
    [Read `smsjobs.join` docs](https://core.telegram.org/method/smsjobs.join).

    Generated from the following TL definition:
    ```tl
    smsjobs.join#a74ece2d = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Leave(TLRequest):
    """
    [Read `smsjobs.leave` docs](https://core.telegram.org/method/smsjobs.leave).

    Generated from the following TL definition:
    ```tl
    smsjobs.leave#9898ad73 = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateSettings(TLRequest):
    """
    [Read `smsjobs.updateSettings` docs](https://core.telegram.org/method/smsjobs.updateSettings).

    Generated from the following TL definition:
    ```tl
    smsjobs.updateSettings#93fa0bf flags:# allow_international:flags.0?true = Bool
    ```
    """
    def __new__(
        cls,
        allow_international: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStatus(TLRequest):
    """
    [Read `smsjobs.getStatus` docs](https://core.telegram.org/method/smsjobs.getStatus).

    Generated from the following TL definition:
    ```tl
    smsjobs.getStatus#10a698e8 = smsjobs.Status
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSmsJob(TLRequest):
    """
    [Read `smsjobs.getSmsJob` docs](https://core.telegram.org/method/smsjobs.getSmsJob).

    Generated from the following TL definition:
    ```tl
    smsjobs.getSmsJob#778d902f job_id:string = SmsJob
    ```
    """
    def __new__(
        cls,
        job_id: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FinishJob(TLRequest):
    """
    [Read `smsjobs.finishJob` docs](https://core.telegram.org/method/smsjobs.finishJob).

    Generated from the following TL definition:
    ```tl
    smsjobs.finishJob#4f1ebf24 flags:# job_id:string error:flags.0?string = Bool
    ```
    """
    def __new__(
        cls,
        job_id: str,
        error: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

