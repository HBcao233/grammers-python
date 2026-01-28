from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class SendCode(TLRequest):
    """
    [Read `auth.sendCode` docs](https://core.telegram.org/method/auth.sendCode).

    Generated from the following TL definition:
    ```tl
    auth.sendCode#a677244f phone_number:string api_id:int api_hash:string settings:CodeSettings = auth.SentCode
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        api_id: int,
        api_hash: str,
        settings: types.CodeSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SignUp(TLRequest):
    """
    [Read `auth.signUp` docs](https://core.telegram.org/method/auth.signUp).

    Generated from the following TL definition:
    ```tl
    auth.signUp#aac7b717 flags:# no_joined_notifications:flags.0?true phone_number:string phone_code_hash:string first_name:string last_name:string = auth.Authorization
    ```
    """
    def __new__(
        cls,
        no_joined_notifications: bool,
        phone_number: str,
        phone_code_hash: str,
        first_name: str,
        last_name: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SignIn(TLRequest):
    """
    [Read `auth.signIn` docs](https://core.telegram.org/method/auth.signIn).

    Generated from the following TL definition:
    ```tl
    auth.signIn#8d52a951 flags:# phone_number:string phone_code_hash:string phone_code:flags.0?string email_verification:flags.1?EmailVerification = auth.Authorization
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        phone_code_hash: str,
        phone_code: Optional[str],
        email_verification: Optional[types.EmailVerificationCode | types.EmailVerificationGoogle | types.EmailVerificationApple],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LogOut(TLRequest):
    """
    [Read `auth.logOut` docs](https://core.telegram.org/method/auth.logOut).

    Generated from the following TL definition:
    ```tl
    auth.logOut#3e72ba19 = auth.LoggedOut
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetAuthorizations(TLRequest):
    """
    [Read `auth.resetAuthorizations` docs](https://core.telegram.org/method/auth.resetAuthorizations).

    Generated from the following TL definition:
    ```tl
    auth.resetAuthorizations#9fab0d1a = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportAuthorization(TLRequest):
    """
    [Read `auth.exportAuthorization` docs](https://core.telegram.org/method/auth.exportAuthorization).

    Generated from the following TL definition:
    ```tl
    auth.exportAuthorization#e5bfffcd dc_id:int = auth.ExportedAuthorization
    ```
    """
    def __new__(
        cls,
        dc_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ImportAuthorization(TLRequest):
    """
    [Read `auth.importAuthorization` docs](https://core.telegram.org/method/auth.importAuthorization).

    Generated from the following TL definition:
    ```tl
    auth.importAuthorization#a57a7dad id:long bytes:bytes = auth.Authorization
    ```
    """
    def __new__(
        cls,
        id: int,
        bytes: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BindTempAuthKey(TLRequest):
    """
    [Read `auth.bindTempAuthKey` docs](https://core.telegram.org/method/auth.bindTempAuthKey).

    Generated from the following TL definition:
    ```tl
    auth.bindTempAuthKey#cdd42a05 perm_auth_key_id:long nonce:long expires_at:int encrypted_message:bytes = Bool
    ```
    """
    def __new__(
        cls,
        perm_auth_key_id: int,
        nonce: int,
        expires_at: int,
        encrypted_message: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ImportBotAuthorization(TLRequest):
    """
    [Read `auth.importBotAuthorization` docs](https://core.telegram.org/method/auth.importBotAuthorization).

    Generated from the following TL definition:
    ```tl
    auth.importBotAuthorization#67a3ff2c flags:int api_id:int api_hash:string bot_auth_token:string = auth.Authorization
    ```
    """
    def __new__(
        cls,
        flags: int,
        api_id: int,
        api_hash: str,
        bot_auth_token: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckPassword(TLRequest):
    """
    [Read `auth.checkPassword` docs](https://core.telegram.org/method/auth.checkPassword).

    Generated from the following TL definition:
    ```tl
    auth.checkPassword#d18b4d16 password:InputCheckPasswordSRP = auth.Authorization
    ```
    """
    def __new__(
        cls,
        password: types.InputCheckPasswordEmpty | types.InputCheckPasswordSrp,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestPasswordRecovery(TLRequest):
    """
    [Read `auth.requestPasswordRecovery` docs](https://core.telegram.org/method/auth.requestPasswordRecovery).

    Generated from the following TL definition:
    ```tl
    auth.requestPasswordRecovery#d897bc66 = auth.PasswordRecovery
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RecoverPassword(TLRequest):
    """
    [Read `auth.recoverPassword` docs](https://core.telegram.org/method/auth.recoverPassword).

    Generated from the following TL definition:
    ```tl
    auth.recoverPassword#37096c70 flags:# code:string new_settings:flags.0?account.PasswordInputSettings = auth.Authorization
    ```
    """
    def __new__(
        cls,
        code: str,
        new_settings: Optional[types.account.PasswordInputSettings],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResendCode(TLRequest):
    """
    [Read `auth.resendCode` docs](https://core.telegram.org/method/auth.resendCode).

    Generated from the following TL definition:
    ```tl
    auth.resendCode#cae47523 flags:# phone_number:string phone_code_hash:string reason:flags.0?string = auth.SentCode
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        phone_code_hash: str,
        reason: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CancelCode(TLRequest):
    """
    [Read `auth.cancelCode` docs](https://core.telegram.org/method/auth.cancelCode).

    Generated from the following TL definition:
    ```tl
    auth.cancelCode#1f040578 phone_number:string phone_code_hash:string = Bool
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        phone_code_hash: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DropTempAuthKeys(TLRequest):
    """
    [Read `auth.dropTempAuthKeys` docs](https://core.telegram.org/method/auth.dropTempAuthKeys).

    Generated from the following TL definition:
    ```tl
    auth.dropTempAuthKeys#8e48a188 except_auth_keys:Vector<long> = Bool
    ```
    """
    def __new__(
        cls,
        except_auth_keys: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportLoginToken(TLRequest):
    """
    [Read `auth.exportLoginToken` docs](https://core.telegram.org/method/auth.exportLoginToken).

    Generated from the following TL definition:
    ```tl
    auth.exportLoginToken#b7e085fe api_id:int api_hash:string except_ids:Vector<long> = auth.LoginToken
    ```
    """
    def __new__(
        cls,
        api_id: int,
        api_hash: str,
        except_ids: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ImportLoginToken(TLRequest):
    """
    [Read `auth.importLoginToken` docs](https://core.telegram.org/method/auth.importLoginToken).

    Generated from the following TL definition:
    ```tl
    auth.importLoginToken#95ac5ce4 token:bytes = auth.LoginToken
    ```
    """
    def __new__(
        cls,
        token: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AcceptLoginToken(TLRequest):
    """
    [Read `auth.acceptLoginToken` docs](https://core.telegram.org/method/auth.acceptLoginToken).

    Generated from the following TL definition:
    ```tl
    auth.acceptLoginToken#e894ad4d token:bytes = Authorization
    ```
    """
    def __new__(
        cls,
        token: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckRecoveryPassword(TLRequest):
    """
    [Read `auth.checkRecoveryPassword` docs](https://core.telegram.org/method/auth.checkRecoveryPassword).

    Generated from the following TL definition:
    ```tl
    auth.checkRecoveryPassword#d36bf79 code:string = Bool
    ```
    """
    def __new__(
        cls,
        code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ImportWebTokenAuthorization(TLRequest):
    """
    [Read `auth.importWebTokenAuthorization` docs](https://core.telegram.org/method/auth.importWebTokenAuthorization).

    Generated from the following TL definition:
    ```tl
    auth.importWebTokenAuthorization#2db873a9 api_id:int api_hash:string web_auth_token:string = auth.Authorization
    ```
    """
    def __new__(
        cls,
        api_id: int,
        api_hash: str,
        web_auth_token: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestFirebaseSms(TLRequest):
    """
    [Read `auth.requestFirebaseSms` docs](https://core.telegram.org/method/auth.requestFirebaseSms).

    Generated from the following TL definition:
    ```tl
    auth.requestFirebaseSms#8e39261e flags:# phone_number:string phone_code_hash:string safety_net_token:flags.0?string play_integrity_token:flags.2?string ios_push_secret:flags.1?string = Bool
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        phone_code_hash: str,
        safety_net_token: Optional[str],
        play_integrity_token: Optional[str],
        ios_push_secret: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetLoginEmail(TLRequest):
    """
    [Read `auth.resetLoginEmail` docs](https://core.telegram.org/method/auth.resetLoginEmail).

    Generated from the following TL definition:
    ```tl
    auth.resetLoginEmail#7e960193 phone_number:string phone_code_hash:string = auth.SentCode
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        phone_code_hash: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportMissingCode(TLRequest):
    """
    [Read `auth.reportMissingCode` docs](https://core.telegram.org/method/auth.reportMissingCode).

    Generated from the following TL definition:
    ```tl
    auth.reportMissingCode#cb9deff6 phone_number:string phone_code_hash:string mnc:string = Bool
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        phone_code_hash: str,
        mnc: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckPaidAuth(TLRequest):
    """
    [Read `auth.checkPaidAuth` docs](https://core.telegram.org/method/auth.checkPaidAuth).

    Generated from the following TL definition:
    ```tl
    auth.checkPaidAuth#56e59f9c phone_number:string phone_code_hash:string form_id:long = auth.SentCode
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        phone_code_hash: str,
        form_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InitPasskeyLogin(TLRequest):
    """
    [Read `auth.initPasskeyLogin` docs](https://core.telegram.org/method/auth.initPasskeyLogin).

    Generated from the following TL definition:
    ```tl
    auth.initPasskeyLogin#518ad0b7 api_id:int api_hash:string = auth.PasskeyLoginOptions
    ```
    """
    def __new__(
        cls,
        api_id: int,
        api_hash: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FinishPasskeyLogin(TLRequest):
    """
    [Read `auth.finishPasskeyLogin` docs](https://core.telegram.org/method/auth.finishPasskeyLogin).

    Generated from the following TL definition:
    ```tl
    auth.finishPasskeyLogin#9857ad07 flags:# credential:InputPasskeyCredential from_dc_id:flags.0?int from_auth_key_id:flags.0?long = auth.Authorization
    ```
    """
    def __new__(
        cls,
        credential: types.InputPasskeyCredentialPublicKey | types.InputPasskeyCredentialFirebasePnv,
        from_dc_id: Optional[int],
        from_auth_key_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

