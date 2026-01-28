from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class RegisterDevice(TLRequest):
    """
    [Read `account.registerDevice` docs](https://core.telegram.org/method/account.registerDevice).

    Generated from the following TL definition:
    ```tl
    account.registerDevice#ec86017a flags:# no_muted:flags.0?true token_type:int token:string app_sandbox:Bool secret:bytes other_uids:Vector<long> = Bool
    ```
    """
    def __new__(
        cls,
        no_muted: bool,
        token_type: int,
        token: str,
        app_sandbox: bool,
        secret: bytes,
        other_uids: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UnregisterDevice(TLRequest):
    """
    [Read `account.unregisterDevice` docs](https://core.telegram.org/method/account.unregisterDevice).

    Generated from the following TL definition:
    ```tl
    account.unregisterDevice#6a0d3206 token_type:int token:string other_uids:Vector<long> = Bool
    ```
    """
    def __new__(
        cls,
        token_type: int,
        token: str,
        other_uids: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateNotifySettings(TLRequest):
    """
    [Read `account.updateNotifySettings` docs](https://core.telegram.org/method/account.updateNotifySettings).

    Generated from the following TL definition:
    ```tl
    account.updateNotifySettings#84be5b93 peer:InputNotifyPeer settings:InputPeerNotifySettings = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputNotifyPeer | types.InputNotifyUsers | types.InputNotifyChats | types.InputNotifyBroadcasts | types.InputNotifyForumTopic,
        settings: types.InputPeerNotifySettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetNotifySettings(TLRequest):
    """
    [Read `account.getNotifySettings` docs](https://core.telegram.org/method/account.getNotifySettings).

    Generated from the following TL definition:
    ```tl
    account.getNotifySettings#12b3ad31 peer:InputNotifyPeer = PeerNotifySettings
    ```
    """
    def __new__(
        cls,
        peer: types.InputNotifyPeer | types.InputNotifyUsers | types.InputNotifyChats | types.InputNotifyBroadcasts | types.InputNotifyForumTopic,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetNotifySettings(TLRequest):
    """
    [Read `account.resetNotifySettings` docs](https://core.telegram.org/method/account.resetNotifySettings).

    Generated from the following TL definition:
    ```tl
    account.resetNotifySettings#db7e1747 = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateProfile(TLRequest):
    """
    [Read `account.updateProfile` docs](https://core.telegram.org/method/account.updateProfile).

    Generated from the following TL definition:
    ```tl
    account.updateProfile#78515775 flags:# first_name:flags.0?string last_name:flags.1?string about:flags.2?string = User
    ```
    """
    def __new__(
        cls,
        first_name: Optional[str],
        last_name: Optional[str],
        about: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStatus(TLRequest):
    """
    [Read `account.updateStatus` docs](https://core.telegram.org/method/account.updateStatus).

    Generated from the following TL definition:
    ```tl
    account.updateStatus#6628562c offline:Bool = Bool
    ```
    """
    def __new__(
        cls,
        offline: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetWallPapers(TLRequest):
    """
    [Read `account.getWallPapers` docs](https://core.telegram.org/method/account.getWallPapers).

    Generated from the following TL definition:
    ```tl
    account.getWallPapers#7967d36 hash:long = account.WallPapers
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportPeer(TLRequest):
    """
    [Read `account.reportPeer` docs](https://core.telegram.org/method/account.reportPeer).

    Generated from the following TL definition:
    ```tl
    account.reportPeer#c5ba3d86 peer:InputPeer reason:ReportReason message:string = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        reason: types.InputReportReasonSpam | types.InputReportReasonViolence | types.InputReportReasonPornography | types.InputReportReasonChildAbuse | types.InputReportReasonOther | types.InputReportReasonCopyright | types.InputReportReasonGeoIrrelevant | types.InputReportReasonFake | types.InputReportReasonIllegalDrugs | types.InputReportReasonPersonalDetails,
        message: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckUsername(TLRequest):
    """
    [Read `account.checkUsername` docs](https://core.telegram.org/method/account.checkUsername).

    Generated from the following TL definition:
    ```tl
    account.checkUsername#2714d86c username:string = Bool
    ```
    """
    def __new__(
        cls,
        username: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateUsername(TLRequest):
    """
    [Read `account.updateUsername` docs](https://core.telegram.org/method/account.updateUsername).

    Generated from the following TL definition:
    ```tl
    account.updateUsername#3e0bdd7c username:string = User
    ```
    """
    def __new__(
        cls,
        username: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPrivacy(TLRequest):
    """
    [Read `account.getPrivacy` docs](https://core.telegram.org/method/account.getPrivacy).

    Generated from the following TL definition:
    ```tl
    account.getPrivacy#dadbc950 key:InputPrivacyKey = account.PrivacyRules
    ```
    """
    def __new__(
        cls,
        key: types.InputPrivacyKeyStatusTimestamp | types.InputPrivacyKeyChatInvite | types.InputPrivacyKeyPhoneCall | types.InputPrivacyKeyPhoneP2P | types.InputPrivacyKeyForwards | types.InputPrivacyKeyProfilePhoto | types.InputPrivacyKeyPhoneNumber | types.InputPrivacyKeyAddedByPhone | types.InputPrivacyKeyVoiceMessages | types.InputPrivacyKeyAbout | types.InputPrivacyKeyBirthday | types.InputPrivacyKeyStarGiftsAutoSave | types.InputPrivacyKeyNoPaidMessages | types.InputPrivacyKeySavedMusic,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetPrivacy(TLRequest):
    """
    [Read `account.setPrivacy` docs](https://core.telegram.org/method/account.setPrivacy).

    Generated from the following TL definition:
    ```tl
    account.setPrivacy#c9f81ce8 key:InputPrivacyKey rules:Vector<InputPrivacyRule> = account.PrivacyRules
    ```
    """
    def __new__(
        cls,
        key: types.InputPrivacyKeyStatusTimestamp | types.InputPrivacyKeyChatInvite | types.InputPrivacyKeyPhoneCall | types.InputPrivacyKeyPhoneP2P | types.InputPrivacyKeyForwards | types.InputPrivacyKeyProfilePhoto | types.InputPrivacyKeyPhoneNumber | types.InputPrivacyKeyAddedByPhone | types.InputPrivacyKeyVoiceMessages | types.InputPrivacyKeyAbout | types.InputPrivacyKeyBirthday | types.InputPrivacyKeyStarGiftsAutoSave | types.InputPrivacyKeyNoPaidMessages | types.InputPrivacyKeySavedMusic,
        rules: Sequence[types.InputPrivacyValueAllowContacts | types.InputPrivacyValueAllowAll | types.InputPrivacyValueAllowUsers | types.InputPrivacyValueDisallowContacts | types.InputPrivacyValueDisallowAll | types.InputPrivacyValueDisallowUsers | types.InputPrivacyValueAllowChatParticipants | types.InputPrivacyValueDisallowChatParticipants | types.InputPrivacyValueAllowCloseFriends | types.InputPrivacyValueAllowPremium | types.InputPrivacyValueAllowBots | types.InputPrivacyValueDisallowBots],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteAccount(TLRequest):
    """
    [Read `account.deleteAccount` docs](https://core.telegram.org/method/account.deleteAccount).

    Generated from the following TL definition:
    ```tl
    account.deleteAccount#a2c0cf74 flags:# reason:string password:flags.0?InputCheckPasswordSRP = Bool
    ```
    """
    def __new__(
        cls,
        reason: str,
        password: Optional[types.InputCheckPasswordEmpty | types.InputCheckPasswordSrp],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAccountTtl(TLRequest):
    """
    [Read `account.getAccountTTL` docs](https://core.telegram.org/method/account.getAccountTTL).

    Generated from the following TL definition:
    ```tl
    account.getAccountTTL#8fc711d = AccountDaysTTL
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetAccountTtl(TLRequest):
    """
    [Read `account.setAccountTTL` docs](https://core.telegram.org/method/account.setAccountTTL).

    Generated from the following TL definition:
    ```tl
    account.setAccountTTL#2442485e ttl:AccountDaysTTL = Bool
    ```
    """
    def __new__(
        cls,
        ttl: types.AccountDaysTtl,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendChangePhoneCode(TLRequest):
    """
    [Read `account.sendChangePhoneCode` docs](https://core.telegram.org/method/account.sendChangePhoneCode).

    Generated from the following TL definition:
    ```tl
    account.sendChangePhoneCode#82574ae5 phone_number:string settings:CodeSettings = auth.SentCode
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        settings: types.CodeSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChangePhone(TLRequest):
    """
    [Read `account.changePhone` docs](https://core.telegram.org/method/account.changePhone).

    Generated from the following TL definition:
    ```tl
    account.changePhone#70c32edb phone_number:string phone_code_hash:string phone_code:string = User
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        phone_code_hash: str,
        phone_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDeviceLocked(TLRequest):
    """
    [Read `account.updateDeviceLocked` docs](https://core.telegram.org/method/account.updateDeviceLocked).

    Generated from the following TL definition:
    ```tl
    account.updateDeviceLocked#38df3532 period:int = Bool
    ```
    """
    def __new__(
        cls,
        period: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAuthorizations(TLRequest):
    """
    [Read `account.getAuthorizations` docs](https://core.telegram.org/method/account.getAuthorizations).

    Generated from the following TL definition:
    ```tl
    account.getAuthorizations#e320c158 = account.Authorizations
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetAuthorization(TLRequest):
    """
    [Read `account.resetAuthorization` docs](https://core.telegram.org/method/account.resetAuthorization).

    Generated from the following TL definition:
    ```tl
    account.resetAuthorization#df77f3bc hash:long = Bool
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPassword(TLRequest):
    """
    [Read `account.getPassword` docs](https://core.telegram.org/method/account.getPassword).

    Generated from the following TL definition:
    ```tl
    account.getPassword#548a30f5 = account.Password
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPasswordSettings(TLRequest):
    """
    [Read `account.getPasswordSettings` docs](https://core.telegram.org/method/account.getPasswordSettings).

    Generated from the following TL definition:
    ```tl
    account.getPasswordSettings#9cd4eaf9 password:InputCheckPasswordSRP = account.PasswordSettings
    ```
    """
    def __new__(
        cls,
        password: types.InputCheckPasswordEmpty | types.InputCheckPasswordSrp,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePasswordSettings(TLRequest):
    """
    [Read `account.updatePasswordSettings` docs](https://core.telegram.org/method/account.updatePasswordSettings).

    Generated from the following TL definition:
    ```tl
    account.updatePasswordSettings#a59b102f password:InputCheckPasswordSRP new_settings:account.PasswordInputSettings = Bool
    ```
    """
    def __new__(
        cls,
        password: types.InputCheckPasswordEmpty | types.InputCheckPasswordSrp,
        new_settings: types.account.PasswordInputSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendConfirmPhoneCode(TLRequest):
    """
    [Read `account.sendConfirmPhoneCode` docs](https://core.telegram.org/method/account.sendConfirmPhoneCode).

    Generated from the following TL definition:
    ```tl
    account.sendConfirmPhoneCode#1b3faa88 hash:string settings:CodeSettings = auth.SentCode
    ```
    """
    def __new__(
        cls,
        hash: str,
        settings: types.CodeSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ConfirmPhone(TLRequest):
    """
    [Read `account.confirmPhone` docs](https://core.telegram.org/method/account.confirmPhone).

    Generated from the following TL definition:
    ```tl
    account.confirmPhone#5f2178c3 phone_code_hash:string phone_code:string = Bool
    ```
    """
    def __new__(
        cls,
        phone_code_hash: str,
        phone_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetTmpPassword(TLRequest):
    """
    [Read `account.getTmpPassword` docs](https://core.telegram.org/method/account.getTmpPassword).

    Generated from the following TL definition:
    ```tl
    account.getTmpPassword#449e0b51 password:InputCheckPasswordSRP period:int = account.TmpPassword
    ```
    """
    def __new__(
        cls,
        password: types.InputCheckPasswordEmpty | types.InputCheckPasswordSrp,
        period: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetWebAuthorizations(TLRequest):
    """
    [Read `account.getWebAuthorizations` docs](https://core.telegram.org/method/account.getWebAuthorizations).

    Generated from the following TL definition:
    ```tl
    account.getWebAuthorizations#182e6d6f = account.WebAuthorizations
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetWebAuthorization(TLRequest):
    """
    [Read `account.resetWebAuthorization` docs](https://core.telegram.org/method/account.resetWebAuthorization).

    Generated from the following TL definition:
    ```tl
    account.resetWebAuthorization#2d01b9ef hash:long = Bool
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetWebAuthorizations(TLRequest):
    """
    [Read `account.resetWebAuthorizations` docs](https://core.telegram.org/method/account.resetWebAuthorizations).

    Generated from the following TL definition:
    ```tl
    account.resetWebAuthorizations#682d2594 = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAllSecureValues(TLRequest):
    """
    [Read `account.getAllSecureValues` docs](https://core.telegram.org/method/account.getAllSecureValues).

    Generated from the following TL definition:
    ```tl
    account.getAllSecureValues#b288bc7d = Vector<SecureValue>
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSecureValue(TLRequest):
    """
    [Read `account.getSecureValue` docs](https://core.telegram.org/method/account.getSecureValue).

    Generated from the following TL definition:
    ```tl
    account.getSecureValue#73665bc2 types:Vector<SecureValueType> = Vector<SecureValue>
    ```
    """
    def __new__(
        cls,
        types: Sequence[types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveSecureValue(TLRequest):
    """
    [Read `account.saveSecureValue` docs](https://core.telegram.org/method/account.saveSecureValue).

    Generated from the following TL definition:
    ```tl
    account.saveSecureValue#899fe31d value:InputSecureValue secure_secret_id:long = SecureValue
    ```
    """
    def __new__(
        cls,
        value: types.InputSecureValue,
        secure_secret_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteSecureValue(TLRequest):
    """
    [Read `account.deleteSecureValue` docs](https://core.telegram.org/method/account.deleteSecureValue).

    Generated from the following TL definition:
    ```tl
    account.deleteSecureValue#b880bc4b types:Vector<SecureValueType> = Bool
    ```
    """
    def __new__(
        cls,
        types: Sequence[types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAuthorizationForm(TLRequest):
    """
    [Read `account.getAuthorizationForm` docs](https://core.telegram.org/method/account.getAuthorizationForm).

    Generated from the following TL definition:
    ```tl
    account.getAuthorizationForm#a929597a bot_id:long scope:string public_key:string = account.AuthorizationForm
    ```
    """
    def __new__(
        cls,
        bot_id: int,
        scope: str,
        public_key: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AcceptAuthorization(TLRequest):
    """
    [Read `account.acceptAuthorization` docs](https://core.telegram.org/method/account.acceptAuthorization).

    Generated from the following TL definition:
    ```tl
    account.acceptAuthorization#f3ed4c73 bot_id:long scope:string public_key:string value_hashes:Vector<SecureValueHash> credentials:SecureCredentialsEncrypted = Bool
    ```
    """
    def __new__(
        cls,
        bot_id: int,
        scope: str,
        public_key: str,
        value_hashes: Sequence[types.SecureValueHash],
        credentials: types.SecureCredentialsEncrypted,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendVerifyPhoneCode(TLRequest):
    """
    [Read `account.sendVerifyPhoneCode` docs](https://core.telegram.org/method/account.sendVerifyPhoneCode).

    Generated from the following TL definition:
    ```tl
    account.sendVerifyPhoneCode#a5a356f9 phone_number:string settings:CodeSettings = auth.SentCode
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        settings: types.CodeSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class VerifyPhone(TLRequest):
    """
    [Read `account.verifyPhone` docs](https://core.telegram.org/method/account.verifyPhone).

    Generated from the following TL definition:
    ```tl
    account.verifyPhone#4dd3a7f6 phone_number:string phone_code_hash:string phone_code:string = Bool
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        phone_code_hash: str,
        phone_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendVerifyEmailCode(TLRequest):
    """
    [Read `account.sendVerifyEmailCode` docs](https://core.telegram.org/method/account.sendVerifyEmailCode).

    Generated from the following TL definition:
    ```tl
    account.sendVerifyEmailCode#98e037bb purpose:EmailVerifyPurpose email:string = account.SentEmailCode
    ```
    """
    def __new__(
        cls,
        purpose: types.EmailVerifyPurposeLoginSetup | types.EmailVerifyPurposeLoginChange | types.EmailVerifyPurposePassport,
        email: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class VerifyEmail(TLRequest):
    """
    [Read `account.verifyEmail` docs](https://core.telegram.org/method/account.verifyEmail).

    Generated from the following TL definition:
    ```tl
    account.verifyEmail#32da4cf purpose:EmailVerifyPurpose verification:EmailVerification = account.EmailVerified
    ```
    """
    def __new__(
        cls,
        purpose: types.EmailVerifyPurposeLoginSetup | types.EmailVerifyPurposeLoginChange | types.EmailVerifyPurposePassport,
        verification: types.EmailVerificationCode | types.EmailVerificationGoogle | types.EmailVerificationApple,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InitTakeoutSession(TLRequest):
    """
    [Read `account.initTakeoutSession` docs](https://core.telegram.org/method/account.initTakeoutSession).

    Generated from the following TL definition:
    ```tl
    account.initTakeoutSession#8ef3eab0 flags:# contacts:flags.0?true message_users:flags.1?true message_chats:flags.2?true message_megagroups:flags.3?true message_channels:flags.4?true files:flags.5?true file_max_size:flags.5?long = account.Takeout
    ```
    """
    def __new__(
        cls,
        contacts: bool,
        message_users: bool,
        message_chats: bool,
        message_megagroups: bool,
        message_channels: bool,
        files: bool,
        file_max_size: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FinishTakeoutSession(TLRequest):
    """
    [Read `account.finishTakeoutSession` docs](https://core.telegram.org/method/account.finishTakeoutSession).

    Generated from the following TL definition:
    ```tl
    account.finishTakeoutSession#1d2652ee flags:# success:flags.0?true = Bool
    ```
    """
    def __new__(
        cls,
        success: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ConfirmPasswordEmail(TLRequest):
    """
    [Read `account.confirmPasswordEmail` docs](https://core.telegram.org/method/account.confirmPasswordEmail).

    Generated from the following TL definition:
    ```tl
    account.confirmPasswordEmail#8fdf1920 code:string = Bool
    ```
    """
    def __new__(
        cls,
        code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResendPasswordEmail(TLRequest):
    """
    [Read `account.resendPasswordEmail` docs](https://core.telegram.org/method/account.resendPasswordEmail).

    Generated from the following TL definition:
    ```tl
    account.resendPasswordEmail#7a7f2a15 = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CancelPasswordEmail(TLRequest):
    """
    [Read `account.cancelPasswordEmail` docs](https://core.telegram.org/method/account.cancelPasswordEmail).

    Generated from the following TL definition:
    ```tl
    account.cancelPasswordEmail#c1cbd5b6 = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetContactSignUpNotification(TLRequest):
    """
    [Read `account.getContactSignUpNotification` docs](https://core.telegram.org/method/account.getContactSignUpNotification).

    Generated from the following TL definition:
    ```tl
    account.getContactSignUpNotification#9f07c728 = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetContactSignUpNotification(TLRequest):
    """
    [Read `account.setContactSignUpNotification` docs](https://core.telegram.org/method/account.setContactSignUpNotification).

    Generated from the following TL definition:
    ```tl
    account.setContactSignUpNotification#cff43f61 silent:Bool = Bool
    ```
    """
    def __new__(
        cls,
        silent: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetNotifyExceptions(TLRequest):
    """
    [Read `account.getNotifyExceptions` docs](https://core.telegram.org/method/account.getNotifyExceptions).

    Generated from the following TL definition:
    ```tl
    account.getNotifyExceptions#53577479 flags:# compare_sound:flags.1?true compare_stories:flags.2?true peer:flags.0?InputNotifyPeer = Updates
    ```
    """
    def __new__(
        cls,
        compare_sound: bool,
        compare_stories: bool,
        peer: Optional[types.InputNotifyPeer | types.InputNotifyUsers | types.InputNotifyChats | types.InputNotifyBroadcasts | types.InputNotifyForumTopic],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetWallPaper(TLRequest):
    """
    [Read `account.getWallPaper` docs](https://core.telegram.org/method/account.getWallPaper).

    Generated from the following TL definition:
    ```tl
    account.getWallPaper#fc8ddbea wallpaper:InputWallPaper = WallPaper
    ```
    """
    def __new__(
        cls,
        wallpaper: types.InputWallPaper | types.InputWallPaperSlug | types.InputWallPaperNoFile,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UploadWallPaper(TLRequest):
    """
    [Read `account.uploadWallPaper` docs](https://core.telegram.org/method/account.uploadWallPaper).

    Generated from the following TL definition:
    ```tl
    account.uploadWallPaper#e39a8f03 flags:# for_chat:flags.0?true file:InputFile mime_type:string settings:WallPaperSettings = WallPaper
    ```
    """
    def __new__(
        cls,
        for_chat: bool,
        file: types.InputFile | types.InputFileBig | types.InputFileStoryDocument,
        mime_type: str,
        settings: types.WallPaperSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveWallPaper(TLRequest):
    """
    [Read `account.saveWallPaper` docs](https://core.telegram.org/method/account.saveWallPaper).

    Generated from the following TL definition:
    ```tl
    account.saveWallPaper#6c5a5b37 wallpaper:InputWallPaper unsave:Bool settings:WallPaperSettings = Bool
    ```
    """
    def __new__(
        cls,
        wallpaper: types.InputWallPaper | types.InputWallPaperSlug | types.InputWallPaperNoFile,
        unsave: bool,
        settings: types.WallPaperSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InstallWallPaper(TLRequest):
    """
    [Read `account.installWallPaper` docs](https://core.telegram.org/method/account.installWallPaper).

    Generated from the following TL definition:
    ```tl
    account.installWallPaper#feed5769 wallpaper:InputWallPaper settings:WallPaperSettings = Bool
    ```
    """
    def __new__(
        cls,
        wallpaper: types.InputWallPaper | types.InputWallPaperSlug | types.InputWallPaperNoFile,
        settings: types.WallPaperSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetWallPapers(TLRequest):
    """
    [Read `account.resetWallPapers` docs](https://core.telegram.org/method/account.resetWallPapers).

    Generated from the following TL definition:
    ```tl
    account.resetWallPapers#bb3b9804 = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAutoDownloadSettings(TLRequest):
    """
    [Read `account.getAutoDownloadSettings` docs](https://core.telegram.org/method/account.getAutoDownloadSettings).

    Generated from the following TL definition:
    ```tl
    account.getAutoDownloadSettings#56da0b3f = account.AutoDownloadSettings
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveAutoDownloadSettings(TLRequest):
    """
    [Read `account.saveAutoDownloadSettings` docs](https://core.telegram.org/method/account.saveAutoDownloadSettings).

    Generated from the following TL definition:
    ```tl
    account.saveAutoDownloadSettings#76f36233 flags:# low:flags.0?true high:flags.1?true settings:AutoDownloadSettings = Bool
    ```
    """
    def __new__(
        cls,
        low: bool,
        high: bool,
        settings: types.AutoDownloadSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UploadTheme(TLRequest):
    """
    [Read `account.uploadTheme` docs](https://core.telegram.org/method/account.uploadTheme).

    Generated from the following TL definition:
    ```tl
    account.uploadTheme#1c3db333 flags:# file:InputFile thumb:flags.0?InputFile file_name:string mime_type:string = Document
    ```
    """
    def __new__(
        cls,
        file: types.InputFile | types.InputFileBig | types.InputFileStoryDocument,
        thumb: Optional[types.InputFile | types.InputFileBig | types.InputFileStoryDocument],
        file_name: str,
        mime_type: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CreateTheme(TLRequest):
    """
    [Read `account.createTheme` docs](https://core.telegram.org/method/account.createTheme).

    Generated from the following TL definition:
    ```tl
    account.createTheme#652e4400 flags:# slug:string title:string document:flags.2?InputDocument settings:flags.3?Vector<InputThemeSettings> = Theme
    ```
    """
    def __new__(
        cls,
        slug: str,
        title: str,
        document: Optional[types.InputDocumentEmpty | types.InputDocument],
        settings: Optional[Sequence[types.InputThemeSettings]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateTheme(TLRequest):
    """
    [Read `account.updateTheme` docs](https://core.telegram.org/method/account.updateTheme).

    Generated from the following TL definition:
    ```tl
    account.updateTheme#2bf40ccc flags:# format:string theme:InputTheme slug:flags.0?string title:flags.1?string document:flags.2?InputDocument settings:flags.3?Vector<InputThemeSettings> = Theme
    ```
    """
    def __new__(
        cls,
        format: str,
        theme: types.InputTheme | types.InputThemeSlug,
        slug: Optional[str],
        title: Optional[str],
        document: Optional[types.InputDocumentEmpty | types.InputDocument],
        settings: Optional[Sequence[types.InputThemeSettings]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveTheme(TLRequest):
    """
    [Read `account.saveTheme` docs](https://core.telegram.org/method/account.saveTheme).

    Generated from the following TL definition:
    ```tl
    account.saveTheme#f257106c theme:InputTheme unsave:Bool = Bool
    ```
    """
    def __new__(
        cls,
        theme: types.InputTheme | types.InputThemeSlug,
        unsave: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InstallTheme(TLRequest):
    """
    [Read `account.installTheme` docs](https://core.telegram.org/method/account.installTheme).

    Generated from the following TL definition:
    ```tl
    account.installTheme#c727bb3b flags:# dark:flags.0?true theme:flags.1?InputTheme format:flags.2?string base_theme:flags.3?BaseTheme = Bool
    ```
    """
    def __new__(
        cls,
        dark: bool,
        theme: Optional[types.InputTheme | types.InputThemeSlug],
        format: Optional[str],
        base_theme: Optional[types.BaseThemeClassic | types.BaseThemeDay | types.BaseThemeNight | types.BaseThemeTinted | types.BaseThemeArctic],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetTheme(TLRequest):
    """
    [Read `account.getTheme` docs](https://core.telegram.org/method/account.getTheme).

    Generated from the following TL definition:
    ```tl
    account.getTheme#3a5869ec format:string theme:InputTheme = Theme
    ```
    """
    def __new__(
        cls,
        format: str,
        theme: types.InputTheme | types.InputThemeSlug,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetThemes(TLRequest):
    """
    [Read `account.getThemes` docs](https://core.telegram.org/method/account.getThemes).

    Generated from the following TL definition:
    ```tl
    account.getThemes#7206e458 format:string hash:long = account.Themes
    ```
    """
    def __new__(
        cls,
        format: str,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetContentSettings(TLRequest):
    """
    [Read `account.setContentSettings` docs](https://core.telegram.org/method/account.setContentSettings).

    Generated from the following TL definition:
    ```tl
    account.setContentSettings#b574b16b flags:# sensitive_enabled:flags.0?true = Bool
    ```
    """
    def __new__(
        cls,
        sensitive_enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetContentSettings(TLRequest):
    """
    [Read `account.getContentSettings` docs](https://core.telegram.org/method/account.getContentSettings).

    Generated from the following TL definition:
    ```tl
    account.getContentSettings#8b9b4dae = account.ContentSettings
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMultiWallPapers(TLRequest):
    """
    [Read `account.getMultiWallPapers` docs](https://core.telegram.org/method/account.getMultiWallPapers).

    Generated from the following TL definition:
    ```tl
    account.getMultiWallPapers#65ad71dc wallpapers:Vector<InputWallPaper> = Vector<WallPaper>
    ```
    """
    def __new__(
        cls,
        wallpapers: Sequence[types.InputWallPaper | types.InputWallPaperSlug | types.InputWallPaperNoFile],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetGlobalPrivacySettings(TLRequest):
    """
    [Read `account.getGlobalPrivacySettings` docs](https://core.telegram.org/method/account.getGlobalPrivacySettings).

    Generated from the following TL definition:
    ```tl
    account.getGlobalPrivacySettings#eb2b4cf6 = GlobalPrivacySettings
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetGlobalPrivacySettings(TLRequest):
    """
    [Read `account.setGlobalPrivacySettings` docs](https://core.telegram.org/method/account.setGlobalPrivacySettings).

    Generated from the following TL definition:
    ```tl
    account.setGlobalPrivacySettings#1edaaac2 settings:GlobalPrivacySettings = GlobalPrivacySettings
    ```
    """
    def __new__(
        cls,
        settings: types.GlobalPrivacySettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportProfilePhoto(TLRequest):
    """
    [Read `account.reportProfilePhoto` docs](https://core.telegram.org/method/account.reportProfilePhoto).

    Generated from the following TL definition:
    ```tl
    account.reportProfilePhoto#fa8cc6f5 peer:InputPeer photo_id:InputPhoto reason:ReportReason message:string = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        photo_id: types.InputPhotoEmpty | types.InputPhoto,
        reason: types.InputReportReasonSpam | types.InputReportReasonViolence | types.InputReportReasonPornography | types.InputReportReasonChildAbuse | types.InputReportReasonOther | types.InputReportReasonCopyright | types.InputReportReasonGeoIrrelevant | types.InputReportReasonFake | types.InputReportReasonIllegalDrugs | types.InputReportReasonPersonalDetails,
        message: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetPassword(TLRequest):
    """
    [Read `account.resetPassword` docs](https://core.telegram.org/method/account.resetPassword).

    Generated from the following TL definition:
    ```tl
    account.resetPassword#9308ce1b = account.ResetPasswordResult
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeclinePasswordReset(TLRequest):
    """
    [Read `account.declinePasswordReset` docs](https://core.telegram.org/method/account.declinePasswordReset).

    Generated from the following TL definition:
    ```tl
    account.declinePasswordReset#4c9409f6 = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetChatThemes(TLRequest):
    """
    [Read `account.getChatThemes` docs](https://core.telegram.org/method/account.getChatThemes).

    Generated from the following TL definition:
    ```tl
    account.getChatThemes#d638de89 hash:long = account.Themes
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetAuthorizationTtl(TLRequest):
    """
    [Read `account.setAuthorizationTTL` docs](https://core.telegram.org/method/account.setAuthorizationTTL).

    Generated from the following TL definition:
    ```tl
    account.setAuthorizationTTL#bf899aa0 authorization_ttl_days:int = Bool
    ```
    """
    def __new__(
        cls,
        authorization_ttl_days: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChangeAuthorizationSettings(TLRequest):
    """
    [Read `account.changeAuthorizationSettings` docs](https://core.telegram.org/method/account.changeAuthorizationSettings).

    Generated from the following TL definition:
    ```tl
    account.changeAuthorizationSettings#40f48462 flags:# confirmed:flags.3?true hash:long encrypted_requests_disabled:flags.0?Bool call_requests_disabled:flags.1?Bool = Bool
    ```
    """
    def __new__(
        cls,
        confirmed: bool,
        hash: int,
        encrypted_requests_disabled: Optional[bool],
        call_requests_disabled: Optional[bool],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSavedRingtones(TLRequest):
    """
    [Read `account.getSavedRingtones` docs](https://core.telegram.org/method/account.getSavedRingtones).

    Generated from the following TL definition:
    ```tl
    account.getSavedRingtones#e1902288 hash:long = account.SavedRingtones
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveRingtone(TLRequest):
    """
    [Read `account.saveRingtone` docs](https://core.telegram.org/method/account.saveRingtone).

    Generated from the following TL definition:
    ```tl
    account.saveRingtone#3dea5b03 id:InputDocument unsave:Bool = account.SavedRingtone
    ```
    """
    def __new__(
        cls,
        id: types.InputDocumentEmpty | types.InputDocument,
        unsave: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UploadRingtone(TLRequest):
    """
    [Read `account.uploadRingtone` docs](https://core.telegram.org/method/account.uploadRingtone).

    Generated from the following TL definition:
    ```tl
    account.uploadRingtone#831a83a2 file:InputFile file_name:string mime_type:string = Document
    ```
    """
    def __new__(
        cls,
        file: types.InputFile | types.InputFileBig | types.InputFileStoryDocument,
        file_name: str,
        mime_type: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateEmojiStatus(TLRequest):
    """
    [Read `account.updateEmojiStatus` docs](https://core.telegram.org/method/account.updateEmojiStatus).

    Generated from the following TL definition:
    ```tl
    account.updateEmojiStatus#fbd3de6b emoji_status:EmojiStatus = Bool
    ```
    """
    def __new__(
        cls,
        emoji_status: types.EmojiStatusEmpty | types.EmojiStatus | types.EmojiStatusCollectible | types.InputEmojiStatusCollectible,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDefaultEmojiStatuses(TLRequest):
    """
    [Read `account.getDefaultEmojiStatuses` docs](https://core.telegram.org/method/account.getDefaultEmojiStatuses).

    Generated from the following TL definition:
    ```tl
    account.getDefaultEmojiStatuses#d6753386 hash:long = account.EmojiStatuses
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetRecentEmojiStatuses(TLRequest):
    """
    [Read `account.getRecentEmojiStatuses` docs](https://core.telegram.org/method/account.getRecentEmojiStatuses).

    Generated from the following TL definition:
    ```tl
    account.getRecentEmojiStatuses#f578105 hash:long = account.EmojiStatuses
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ClearRecentEmojiStatuses(TLRequest):
    """
    [Read `account.clearRecentEmojiStatuses` docs](https://core.telegram.org/method/account.clearRecentEmojiStatuses).

    Generated from the following TL definition:
    ```tl
    account.clearRecentEmojiStatuses#18201aae = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReorderUsernames(TLRequest):
    """
    [Read `account.reorderUsernames` docs](https://core.telegram.org/method/account.reorderUsernames).

    Generated from the following TL definition:
    ```tl
    account.reorderUsernames#ef500eab order:Vector<string> = Bool
    ```
    """
    def __new__(
        cls,
        order: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleUsername(TLRequest):
    """
    [Read `account.toggleUsername` docs](https://core.telegram.org/method/account.toggleUsername).

    Generated from the following TL definition:
    ```tl
    account.toggleUsername#58d6b376 username:string active:Bool = Bool
    ```
    """
    def __new__(
        cls,
        username: str,
        active: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDefaultProfilePhotoEmojis(TLRequest):
    """
    [Read `account.getDefaultProfilePhotoEmojis` docs](https://core.telegram.org/method/account.getDefaultProfilePhotoEmojis).

    Generated from the following TL definition:
    ```tl
    account.getDefaultProfilePhotoEmojis#e2750328 hash:long = EmojiList
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDefaultGroupPhotoEmojis(TLRequest):
    """
    [Read `account.getDefaultGroupPhotoEmojis` docs](https://core.telegram.org/method/account.getDefaultGroupPhotoEmojis).

    Generated from the following TL definition:
    ```tl
    account.getDefaultGroupPhotoEmojis#915860ae hash:long = EmojiList
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAutoSaveSettings(TLRequest):
    """
    [Read `account.getAutoSaveSettings` docs](https://core.telegram.org/method/account.getAutoSaveSettings).

    Generated from the following TL definition:
    ```tl
    account.getAutoSaveSettings#adcbbcda = account.AutoSaveSettings
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveAutoSaveSettings(TLRequest):
    """
    [Read `account.saveAutoSaveSettings` docs](https://core.telegram.org/method/account.saveAutoSaveSettings).

    Generated from the following TL definition:
    ```tl
    account.saveAutoSaveSettings#d69b8361 flags:# users:flags.0?true chats:flags.1?true broadcasts:flags.2?true peer:flags.3?InputPeer settings:AutoSaveSettings = Bool
    ```
    """
    def __new__(
        cls,
        users: bool,
        chats: bool,
        broadcasts: bool,
        peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        settings: types.AutoSaveSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteAutoSaveExceptions(TLRequest):
    """
    [Read `account.deleteAutoSaveExceptions` docs](https://core.telegram.org/method/account.deleteAutoSaveExceptions).

    Generated from the following TL definition:
    ```tl
    account.deleteAutoSaveExceptions#53bc0020 = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InvalidateSignInCodes(TLRequest):
    """
    [Read `account.invalidateSignInCodes` docs](https://core.telegram.org/method/account.invalidateSignInCodes).

    Generated from the following TL definition:
    ```tl
    account.invalidateSignInCodes#ca8ae8ba codes:Vector<string> = Bool
    ```
    """
    def __new__(
        cls,
        codes: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateColor(TLRequest):
    """
    [Read `account.updateColor` docs](https://core.telegram.org/method/account.updateColor).

    Generated from the following TL definition:
    ```tl
    account.updateColor#684d214e flags:# for_profile:flags.1?true color:flags.2?PeerColor = Bool
    ```
    """
    def __new__(
        cls,
        for_profile: bool,
        color: Optional[types.PeerColor | types.PeerColorCollectible | types.InputPeerColorCollectible],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDefaultBackgroundEmojis(TLRequest):
    """
    [Read `account.getDefaultBackgroundEmojis` docs](https://core.telegram.org/method/account.getDefaultBackgroundEmojis).

    Generated from the following TL definition:
    ```tl
    account.getDefaultBackgroundEmojis#a60ab9ce hash:long = EmojiList
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetChannelDefaultEmojiStatuses(TLRequest):
    """
    [Read `account.getChannelDefaultEmojiStatuses` docs](https://core.telegram.org/method/account.getChannelDefaultEmojiStatuses).

    Generated from the following TL definition:
    ```tl
    account.getChannelDefaultEmojiStatuses#7727a7d5 hash:long = account.EmojiStatuses
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetChannelRestrictedStatusEmojis(TLRequest):
    """
    [Read `account.getChannelRestrictedStatusEmojis` docs](https://core.telegram.org/method/account.getChannelRestrictedStatusEmojis).

    Generated from the following TL definition:
    ```tl
    account.getChannelRestrictedStatusEmojis#35a9e0d5 hash:long = EmojiList
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBusinessWorkHours(TLRequest):
    """
    [Read `account.updateBusinessWorkHours` docs](https://core.telegram.org/method/account.updateBusinessWorkHours).

    Generated from the following TL definition:
    ```tl
    account.updateBusinessWorkHours#4b00e066 flags:# business_work_hours:flags.0?BusinessWorkHours = Bool
    ```
    """
    def __new__(
        cls,
        business_work_hours: Optional[types.BusinessWorkHours],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBusinessLocation(TLRequest):
    """
    [Read `account.updateBusinessLocation` docs](https://core.telegram.org/method/account.updateBusinessLocation).

    Generated from the following TL definition:
    ```tl
    account.updateBusinessLocation#9e6b131a flags:# geo_point:flags.1?InputGeoPoint address:flags.0?string = Bool
    ```
    """
    def __new__(
        cls,
        geo_point: Optional[types.InputGeoPointEmpty | types.InputGeoPoint],
        address: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBusinessGreetingMessage(TLRequest):
    """
    [Read `account.updateBusinessGreetingMessage` docs](https://core.telegram.org/method/account.updateBusinessGreetingMessage).

    Generated from the following TL definition:
    ```tl
    account.updateBusinessGreetingMessage#66cdafc4 flags:# message:flags.0?InputBusinessGreetingMessage = Bool
    ```
    """
    def __new__(
        cls,
        message: Optional[types.InputBusinessGreetingMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBusinessAwayMessage(TLRequest):
    """
    [Read `account.updateBusinessAwayMessage` docs](https://core.telegram.org/method/account.updateBusinessAwayMessage).

    Generated from the following TL definition:
    ```tl
    account.updateBusinessAwayMessage#a26a7fa5 flags:# message:flags.0?InputBusinessAwayMessage = Bool
    ```
    """
    def __new__(
        cls,
        message: Optional[types.InputBusinessAwayMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateConnectedBot(TLRequest):
    """
    [Read `account.updateConnectedBot` docs](https://core.telegram.org/method/account.updateConnectedBot).

    Generated from the following TL definition:
    ```tl
    account.updateConnectedBot#66a08c7e flags:# deleted:flags.1?true rights:flags.0?BusinessBotRights bot:InputUser recipients:InputBusinessBotRecipients = Updates
    ```
    """
    def __new__(
        cls,
        deleted: bool,
        rights: Optional[types.BusinessBotRights],
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        recipients: types.InputBusinessBotRecipients,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetConnectedBots(TLRequest):
    """
    [Read `account.getConnectedBots` docs](https://core.telegram.org/method/account.getConnectedBots).

    Generated from the following TL definition:
    ```tl
    account.getConnectedBots#4ea4c80f = account.ConnectedBots
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetBotBusinessConnection(TLRequest):
    """
    [Read `account.getBotBusinessConnection` docs](https://core.telegram.org/method/account.getBotBusinessConnection).

    Generated from the following TL definition:
    ```tl
    account.getBotBusinessConnection#76a86270 connection_id:string = Updates
    ```
    """
    def __new__(
        cls,
        connection_id: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBusinessIntro(TLRequest):
    """
    [Read `account.updateBusinessIntro` docs](https://core.telegram.org/method/account.updateBusinessIntro).

    Generated from the following TL definition:
    ```tl
    account.updateBusinessIntro#a614d034 flags:# intro:flags.0?InputBusinessIntro = Bool
    ```
    """
    def __new__(
        cls,
        intro: Optional[types.InputBusinessIntro],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleConnectedBotPaused(TLRequest):
    """
    [Read `account.toggleConnectedBotPaused` docs](https://core.telegram.org/method/account.toggleConnectedBotPaused).

    Generated from the following TL definition:
    ```tl
    account.toggleConnectedBotPaused#646e1097 peer:InputPeer paused:Bool = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        paused: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DisablePeerConnectedBot(TLRequest):
    """
    [Read `account.disablePeerConnectedBot` docs](https://core.telegram.org/method/account.disablePeerConnectedBot).

    Generated from the following TL definition:
    ```tl
    account.disablePeerConnectedBot#5e437ed9 peer:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBirthday(TLRequest):
    """
    [Read `account.updateBirthday` docs](https://core.telegram.org/method/account.updateBirthday).

    Generated from the following TL definition:
    ```tl
    account.updateBirthday#cc6e0c11 flags:# birthday:flags.0?Birthday = Bool
    ```
    """
    def __new__(
        cls,
        birthday: Optional[types.Birthday],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CreateBusinessChatLink(TLRequest):
    """
    [Read `account.createBusinessChatLink` docs](https://core.telegram.org/method/account.createBusinessChatLink).

    Generated from the following TL definition:
    ```tl
    account.createBusinessChatLink#8851e68e link:InputBusinessChatLink = BusinessChatLink
    ```
    """
    def __new__(
        cls,
        link: types.InputBusinessChatLink,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditBusinessChatLink(TLRequest):
    """
    [Read `account.editBusinessChatLink` docs](https://core.telegram.org/method/account.editBusinessChatLink).

    Generated from the following TL definition:
    ```tl
    account.editBusinessChatLink#8c3410af slug:string link:InputBusinessChatLink = BusinessChatLink
    ```
    """
    def __new__(
        cls,
        slug: str,
        link: types.InputBusinessChatLink,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteBusinessChatLink(TLRequest):
    """
    [Read `account.deleteBusinessChatLink` docs](https://core.telegram.org/method/account.deleteBusinessChatLink).

    Generated from the following TL definition:
    ```tl
    account.deleteBusinessChatLink#60073674 slug:string = Bool
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetBusinessChatLinks(TLRequest):
    """
    [Read `account.getBusinessChatLinks` docs](https://core.telegram.org/method/account.getBusinessChatLinks).

    Generated from the following TL definition:
    ```tl
    account.getBusinessChatLinks#6f70dde1 = account.BusinessChatLinks
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResolveBusinessChatLink(TLRequest):
    """
    [Read `account.resolveBusinessChatLink` docs](https://core.telegram.org/method/account.resolveBusinessChatLink).

    Generated from the following TL definition:
    ```tl
    account.resolveBusinessChatLink#5492e5ee slug:string = account.ResolvedBusinessChatLinks
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePersonalChannel(TLRequest):
    """
    [Read `account.updatePersonalChannel` docs](https://core.telegram.org/method/account.updatePersonalChannel).

    Generated from the following TL definition:
    ```tl
    account.updatePersonalChannel#d94305e0 channel:InputChannel = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleSponsoredMessages(TLRequest):
    """
    [Read `account.toggleSponsoredMessages` docs](https://core.telegram.org/method/account.toggleSponsoredMessages).

    Generated from the following TL definition:
    ```tl
    account.toggleSponsoredMessages#b9d9a38d enabled:Bool = Bool
    ```
    """
    def __new__(
        cls,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetReactionsNotifySettings(TLRequest):
    """
    [Read `account.getReactionsNotifySettings` docs](https://core.telegram.org/method/account.getReactionsNotifySettings).

    Generated from the following TL definition:
    ```tl
    account.getReactionsNotifySettings#6dd654c = ReactionsNotifySettings
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetReactionsNotifySettings(TLRequest):
    """
    [Read `account.setReactionsNotifySettings` docs](https://core.telegram.org/method/account.setReactionsNotifySettings).

    Generated from the following TL definition:
    ```tl
    account.setReactionsNotifySettings#316ce548 settings:ReactionsNotifySettings = ReactionsNotifySettings
    ```
    """
    def __new__(
        cls,
        settings: types.ReactionsNotifySettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetCollectibleEmojiStatuses(TLRequest):
    """
    [Read `account.getCollectibleEmojiStatuses` docs](https://core.telegram.org/method/account.getCollectibleEmojiStatuses).

    Generated from the following TL definition:
    ```tl
    account.getCollectibleEmojiStatuses#2e7b4543 hash:long = account.EmojiStatuses
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPaidMessagesRevenue(TLRequest):
    """
    [Read `account.getPaidMessagesRevenue` docs](https://core.telegram.org/method/account.getPaidMessagesRevenue).

    Generated from the following TL definition:
    ```tl
    account.getPaidMessagesRevenue#19ba4a67 flags:# parent_peer:flags.0?InputPeer user_id:InputUser = account.PaidMessagesRevenue
    ```
    """
    def __new__(
        cls,
        parent_peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleNoPaidMessagesException(TLRequest):
    """
    [Read `account.toggleNoPaidMessagesException` docs](https://core.telegram.org/method/account.toggleNoPaidMessagesException).

    Generated from the following TL definition:
    ```tl
    account.toggleNoPaidMessagesException#fe2eda76 flags:# refund_charged:flags.0?true require_payment:flags.2?true parent_peer:flags.1?InputPeer user_id:InputUser = Bool
    ```
    """
    def __new__(
        cls,
        refund_charged: bool,
        require_payment: bool,
        parent_peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetMainProfileTab(TLRequest):
    """
    [Read `account.setMainProfileTab` docs](https://core.telegram.org/method/account.setMainProfileTab).

    Generated from the following TL definition:
    ```tl
    account.setMainProfileTab#5dee78b0 tab:ProfileTab = Bool
    ```
    """
    def __new__(
        cls,
        tab: types.ProfileTabPosts | types.ProfileTabGifts | types.ProfileTabMedia | types.ProfileTabFiles | types.ProfileTabMusic | types.ProfileTabVoice | types.ProfileTabLinks | types.ProfileTabGifs,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveMusic(TLRequest):
    """
    [Read `account.saveMusic` docs](https://core.telegram.org/method/account.saveMusic).

    Generated from the following TL definition:
    ```tl
    account.saveMusic#b26732a9 flags:# unsave:flags.0?true id:InputDocument after_id:flags.1?InputDocument = Bool
    ```
    """
    def __new__(
        cls,
        unsave: bool,
        id: types.InputDocumentEmpty | types.InputDocument,
        after_id: Optional[types.InputDocumentEmpty | types.InputDocument],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSavedMusicIds(TLRequest):
    """
    [Read `account.getSavedMusicIds` docs](https://core.telegram.org/method/account.getSavedMusicIds).

    Generated from the following TL definition:
    ```tl
    account.getSavedMusicIds#e09d5faf hash:long = account.SavedMusicIds
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetUniqueGiftChatThemes(TLRequest):
    """
    [Read `account.getUniqueGiftChatThemes` docs](https://core.telegram.org/method/account.getUniqueGiftChatThemes).

    Generated from the following TL definition:
    ```tl
    account.getUniqueGiftChatThemes#e42ce9c9 offset:string limit:int hash:long = account.ChatThemes
    ```
    """
    def __new__(
        cls,
        offset: str,
        limit: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InitPasskeyRegistration(TLRequest):
    """
    [Read `account.initPasskeyRegistration` docs](https://core.telegram.org/method/account.initPasskeyRegistration).

    Generated from the following TL definition:
    ```tl
    account.initPasskeyRegistration#429547e8 = account.PasskeyRegistrationOptions
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RegisterPasskey(TLRequest):
    """
    [Read `account.registerPasskey` docs](https://core.telegram.org/method/account.registerPasskey).

    Generated from the following TL definition:
    ```tl
    account.registerPasskey#55b41fd6 credential:InputPasskeyCredential = Passkey
    ```
    """
    def __new__(
        cls,
        credential: types.InputPasskeyCredentialPublicKey | types.InputPasskeyCredentialFirebasePnv,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPasskeys(TLRequest):
    """
    [Read `account.getPasskeys` docs](https://core.telegram.org/method/account.getPasskeys).

    Generated from the following TL definition:
    ```tl
    account.getPasskeys#ea1f0c52 = account.Passkeys
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeletePasskey(TLRequest):
    """
    [Read `account.deletePasskey` docs](https://core.telegram.org/method/account.deletePasskey).

    Generated from the following TL definition:
    ```tl
    account.deletePasskey#f5b5563f id:string = Bool
    ```
    """
    def __new__(
        cls,
        id: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

