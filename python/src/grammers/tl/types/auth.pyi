from typing import final, Self, Optional
from grammers.tl import TLObject, types

@final
class SentCode(TLObject):
    """
    [Read `auth.sentCode` docs](https://core.telegram.org/constructor/auth.sentCode).

    Generated from the following TL definition:
    ```tl
    auth.sentCode#5e002502 flags:# type:auth.SentCodeType phone_code_hash:string next_type:flags.1?auth.CodeType timeout:flags.2?int = auth.SentCode
    ```
    """
    def __new__(
        cls,
        type: types.auth.SentCodeTypeApp | types.auth.SentCodeTypeSms | types.auth.SentCodeTypeCall | types.auth.SentCodeTypeFlashCall | types.auth.SentCodeTypeMissedCall | types.auth.SentCodeTypeEmailCode | types.auth.SentCodeTypeSetUpEmailRequired | types.auth.SentCodeTypeFragmentSms | types.auth.SentCodeTypeFirebaseSms | types.auth.SentCodeTypeSmsWord | types.auth.SentCodeTypeSmsPhrase,
        phone_code_hash: str,
        next_type: Optional[types.auth.CodeTypeSms | types.auth.CodeTypeCall | types.auth.CodeTypeFlashCall | types.auth.CodeTypeMissedCall | types.auth.CodeTypeFragmentSms],
        timeout: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodeSuccess(TLObject):
    """
    [Read `auth.sentCodeSuccess` docs](https://core.telegram.org/constructor/auth.sentCodeSuccess).

    Generated from the following TL definition:
    ```tl
    auth.sentCodeSuccess#2390fe44 authorization:auth.Authorization = auth.SentCode
    ```
    """
    def __new__(
        cls,
        authorization: types.auth.Authorization | types.auth.AuthorizationSignUpRequired,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodePaymentRequired(TLObject):
    """
    [Read `auth.sentCodePaymentRequired` docs](https://core.telegram.org/constructor/auth.sentCodePaymentRequired).

    Generated from the following TL definition:
    ```tl
    auth.sentCodePaymentRequired#e0955a3c store_product:string phone_code_hash:string support_email_address:string support_email_subject:string currency:string amount:long = auth.SentCode
    ```
    """
    def __new__(
        cls,
        store_product: str,
        phone_code_hash: str,
        support_email_address: str,
        support_email_subject: str,
        currency: str,
        amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Authorization(TLObject):
    """
    [Read `auth.authorization` docs](https://core.telegram.org/constructor/auth.authorization).

    Generated from the following TL definition:
    ```tl
    auth.authorization#2ea2c0d4 flags:# setup_password_required:flags.1?true otherwise_relogin_days:flags.1?int tmp_sessions:flags.0?int future_auth_token:flags.2?bytes user:User = auth.Authorization
    ```
    """
    def __new__(
        cls,
        setup_password_required: bool,
        otherwise_relogin_days: Optional[int],
        tmp_sessions: Optional[int],
        future_auth_token: Optional[bytes],
        user: types.UserEmpty | types.User,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AuthorizationSignUpRequired(TLObject):
    """
    [Read `auth.authorizationSignUpRequired` docs](https://core.telegram.org/constructor/auth.authorizationSignUpRequired).

    Generated from the following TL definition:
    ```tl
    auth.authorizationSignUpRequired#44747e9a flags:# terms_of_service:flags.0?help.TermsOfService = auth.Authorization
    ```
    """
    def __new__(
        cls,
        terms_of_service: Optional[types.help.TermsOfService],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportedAuthorization(TLObject):
    """
    [Read `auth.exportedAuthorization` docs](https://core.telegram.org/constructor/auth.exportedAuthorization).

    Generated from the following TL definition:
    ```tl
    auth.exportedAuthorization#b434e2b8 id:long bytes:bytes = auth.ExportedAuthorization
    ```
    """
    def __new__(
        cls,
        id: int,
        bytes: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PasswordRecovery(TLObject):
    """
    [Read `auth.passwordRecovery` docs](https://core.telegram.org/constructor/auth.passwordRecovery).

    Generated from the following TL definition:
    ```tl
    auth.passwordRecovery#137948a5 email_pattern:string = auth.PasswordRecovery
    ```
    """
    def __new__(
        cls,
        email_pattern: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CodeTypeSms(TLObject):
    """
    [Read `auth.codeTypeSms` docs](https://core.telegram.org/constructor/auth.codeTypeSms).

    Generated from the following TL definition:
    ```tl
    auth.codeTypeSms#72a3158c = auth.CodeType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CodeTypeCall(TLObject):
    """
    [Read `auth.codeTypeCall` docs](https://core.telegram.org/constructor/auth.codeTypeCall).

    Generated from the following TL definition:
    ```tl
    auth.codeTypeCall#741cd3e3 = auth.CodeType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CodeTypeFlashCall(TLObject):
    """
    [Read `auth.codeTypeFlashCall` docs](https://core.telegram.org/constructor/auth.codeTypeFlashCall).

    Generated from the following TL definition:
    ```tl
    auth.codeTypeFlashCall#226ccefb = auth.CodeType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CodeTypeMissedCall(TLObject):
    """
    [Read `auth.codeTypeMissedCall` docs](https://core.telegram.org/constructor/auth.codeTypeMissedCall).

    Generated from the following TL definition:
    ```tl
    auth.codeTypeMissedCall#d61ad6ee = auth.CodeType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CodeTypeFragmentSms(TLObject):
    """
    [Read `auth.codeTypeFragmentSms` docs](https://core.telegram.org/constructor/auth.codeTypeFragmentSms).

    Generated from the following TL definition:
    ```tl
    auth.codeTypeFragmentSms#6ed998c = auth.CodeType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodeTypeApp(TLObject):
    """
    [Read `auth.sentCodeTypeApp` docs](https://core.telegram.org/constructor/auth.sentCodeTypeApp).

    Generated from the following TL definition:
    ```tl
    auth.sentCodeTypeApp#3dbb5986 length:int = auth.SentCodeType
    ```
    """
    def __new__(
        cls,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodeTypeSms(TLObject):
    """
    [Read `auth.sentCodeTypeSms` docs](https://core.telegram.org/constructor/auth.sentCodeTypeSms).

    Generated from the following TL definition:
    ```tl
    auth.sentCodeTypeSms#c000bba2 length:int = auth.SentCodeType
    ```
    """
    def __new__(
        cls,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodeTypeCall(TLObject):
    """
    [Read `auth.sentCodeTypeCall` docs](https://core.telegram.org/constructor/auth.sentCodeTypeCall).

    Generated from the following TL definition:
    ```tl
    auth.sentCodeTypeCall#5353e5a7 length:int = auth.SentCodeType
    ```
    """
    def __new__(
        cls,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodeTypeFlashCall(TLObject):
    """
    [Read `auth.sentCodeTypeFlashCall` docs](https://core.telegram.org/constructor/auth.sentCodeTypeFlashCall).

    Generated from the following TL definition:
    ```tl
    auth.sentCodeTypeFlashCall#ab03c6d9 pattern:string = auth.SentCodeType
    ```
    """
    def __new__(
        cls,
        pattern: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodeTypeMissedCall(TLObject):
    """
    [Read `auth.sentCodeTypeMissedCall` docs](https://core.telegram.org/constructor/auth.sentCodeTypeMissedCall).

    Generated from the following TL definition:
    ```tl
    auth.sentCodeTypeMissedCall#82006484 prefix:string length:int = auth.SentCodeType
    ```
    """
    def __new__(
        cls,
        prefix: str,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodeTypeEmailCode(TLObject):
    """
    [Read `auth.sentCodeTypeEmailCode` docs](https://core.telegram.org/constructor/auth.sentCodeTypeEmailCode).

    Generated from the following TL definition:
    ```tl
    auth.sentCodeTypeEmailCode#f450f59b flags:# apple_signin_allowed:flags.0?true google_signin_allowed:flags.1?true email_pattern:string length:int reset_available_period:flags.3?int reset_pending_date:flags.4?int = auth.SentCodeType
    ```
    """
    def __new__(
        cls,
        apple_signin_allowed: bool,
        google_signin_allowed: bool,
        email_pattern: str,
        length: int,
        reset_available_period: Optional[int],
        reset_pending_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodeTypeSetUpEmailRequired(TLObject):
    """
    [Read `auth.sentCodeTypeSetUpEmailRequired` docs](https://core.telegram.org/constructor/auth.sentCodeTypeSetUpEmailRequired).

    Generated from the following TL definition:
    ```tl
    auth.sentCodeTypeSetUpEmailRequired#a5491dea flags:# apple_signin_allowed:flags.0?true google_signin_allowed:flags.1?true = auth.SentCodeType
    ```
    """
    def __new__(
        cls,
        apple_signin_allowed: bool,
        google_signin_allowed: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodeTypeFragmentSms(TLObject):
    """
    [Read `auth.sentCodeTypeFragmentSms` docs](https://core.telegram.org/constructor/auth.sentCodeTypeFragmentSms).

    Generated from the following TL definition:
    ```tl
    auth.sentCodeTypeFragmentSms#d9565c39 url:string length:int = auth.SentCodeType
    ```
    """
    def __new__(
        cls,
        url: str,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodeTypeFirebaseSms(TLObject):
    """
    [Read `auth.sentCodeTypeFirebaseSms` docs](https://core.telegram.org/constructor/auth.sentCodeTypeFirebaseSms).

    Generated from the following TL definition:
    ```tl
    auth.sentCodeTypeFirebaseSms#9fd736 flags:# nonce:flags.0?bytes play_integrity_project_id:flags.2?long play_integrity_nonce:flags.2?bytes receipt:flags.1?string push_timeout:flags.1?int length:int = auth.SentCodeType
    ```
    """
    def __new__(
        cls,
        nonce: Optional[bytes],
        play_integrity_project_id: Optional[int],
        play_integrity_nonce: Optional[bytes],
        receipt: Optional[str],
        push_timeout: Optional[int],
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodeTypeSmsWord(TLObject):
    """
    [Read `auth.sentCodeTypeSmsWord` docs](https://core.telegram.org/constructor/auth.sentCodeTypeSmsWord).

    Generated from the following TL definition:
    ```tl
    auth.sentCodeTypeSmsWord#a416ac81 flags:# beginning:flags.0?string = auth.SentCodeType
    ```
    """
    def __new__(
        cls,
        beginning: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentCodeTypeSmsPhrase(TLObject):
    """
    [Read `auth.sentCodeTypeSmsPhrase` docs](https://core.telegram.org/constructor/auth.sentCodeTypeSmsPhrase).

    Generated from the following TL definition:
    ```tl
    auth.sentCodeTypeSmsPhrase#b37794af flags:# beginning:flags.0?string = auth.SentCodeType
    ```
    """
    def __new__(
        cls,
        beginning: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LoginToken(TLObject):
    """
    [Read `auth.loginToken` docs](https://core.telegram.org/constructor/auth.loginToken).

    Generated from the following TL definition:
    ```tl
    auth.loginToken#629f1980 expires:int token:bytes = auth.LoginToken
    ```
    """
    def __new__(
        cls,
        expires: int,
        token: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LoginTokenMigrateTo(TLObject):
    """
    [Read `auth.loginTokenMigrateTo` docs](https://core.telegram.org/constructor/auth.loginTokenMigrateTo).

    Generated from the following TL definition:
    ```tl
    auth.loginTokenMigrateTo#68e9916 dc_id:int token:bytes = auth.LoginToken
    ```
    """
    def __new__(
        cls,
        dc_id: int,
        token: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LoginTokenSuccess(TLObject):
    """
    [Read `auth.loginTokenSuccess` docs](https://core.telegram.org/constructor/auth.loginTokenSuccess).

    Generated from the following TL definition:
    ```tl
    auth.loginTokenSuccess#390d5c5e authorization:auth.Authorization = auth.LoginToken
    ```
    """
    def __new__(
        cls,
        authorization: types.auth.Authorization | types.auth.AuthorizationSignUpRequired,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LoggedOut(TLObject):
    """
    [Read `auth.loggedOut` docs](https://core.telegram.org/constructor/auth.loggedOut).

    Generated from the following TL definition:
    ```tl
    auth.loggedOut#c3a2835f flags:# future_auth_token:flags.0?bytes = auth.LoggedOut
    ```
    """
    def __new__(
        cls,
        future_auth_token: Optional[bytes],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PasskeyLoginOptions(TLObject):
    """
    [Read `auth.passkeyLoginOptions` docs](https://core.telegram.org/constructor/auth.passkeyLoginOptions).

    Generated from the following TL definition:
    ```tl
    auth.passkeyLoginOptions#e2037789 options:DataJSON = auth.PasskeyLoginOptions
    ```
    """
    def __new__(
        cls,
        options: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

