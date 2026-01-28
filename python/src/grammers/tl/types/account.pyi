from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class PrivacyRules(TLObject):
    """
    [Read `account.privacyRules` docs](https://core.telegram.org/constructor/account.privacyRules).

    Generated from the following TL definition:
    ```tl
    account.privacyRules#50a04e45 rules:Vector<PrivacyRule> chats:Vector<Chat> users:Vector<User> = account.PrivacyRules
    ```
    """
    def __new__(
        cls,
        rules: Sequence[types.PrivacyValueAllowContacts | types.PrivacyValueAllowAll | types.PrivacyValueAllowUsers | types.PrivacyValueDisallowContacts | types.PrivacyValueDisallowAll | types.PrivacyValueDisallowUsers | types.PrivacyValueAllowChatParticipants | types.PrivacyValueDisallowChatParticipants | types.PrivacyValueAllowCloseFriends | types.PrivacyValueAllowPremium | types.PrivacyValueAllowBots | types.PrivacyValueDisallowBots],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Authorizations(TLObject):
    """
    [Read `account.authorizations` docs](https://core.telegram.org/constructor/account.authorizations).

    Generated from the following TL definition:
    ```tl
    account.authorizations#4bff8ea0 authorization_ttl_days:int authorizations:Vector<Authorization> = account.Authorizations
    ```
    """
    def __new__(
        cls,
        authorization_ttl_days: int,
        authorizations: Sequence[types.Authorization],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Password(TLObject):
    """
    [Read `account.password` docs](https://core.telegram.org/constructor/account.password).

    Generated from the following TL definition:
    ```tl
    account.password#957b50fb flags:# has_recovery:flags.0?true has_secure_values:flags.1?true has_password:flags.2?true current_algo:flags.2?PasswordKdfAlgo srp_B:flags.2?bytes srp_id:flags.2?long hint:flags.3?string email_unconfirmed_pattern:flags.4?string new_algo:PasswordKdfAlgo new_secure_algo:SecurePasswordKdfAlgo secure_random:bytes pending_reset_date:flags.5?int login_email_pattern:flags.6?string = account.Password
    ```
    """
    def __new__(
        cls,
        has_recovery: bool,
        has_secure_values: bool,
        has_password: bool,
        current_algo: Optional[types.PasswordKdfAlgoUnknown | types.PasswordKdfAlgoSha256Sha256Pbkdf2Hmacsha512iter100000Sha256ModPow],
        srp_b: Optional[bytes],
        srp_id: Optional[int],
        hint: Optional[str],
        email_unconfirmed_pattern: Optional[str],
        new_algo: types.PasswordKdfAlgoUnknown | types.PasswordKdfAlgoSha256Sha256Pbkdf2Hmacsha512iter100000Sha256ModPow,
        new_secure_algo: types.SecurePasswordKdfAlgoUnknown | types.SecurePasswordKdfAlgoPbkdf2Hmacsha512iter100000 | types.SecurePasswordKdfAlgoSha512,
        secure_random: bytes,
        pending_reset_date: Optional[int],
        login_email_pattern: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PasswordSettings(TLObject):
    """
    [Read `account.passwordSettings` docs](https://core.telegram.org/constructor/account.passwordSettings).

    Generated from the following TL definition:
    ```tl
    account.passwordSettings#9a5c33e5 flags:# email:flags.0?string secure_settings:flags.1?SecureSecretSettings = account.PasswordSettings
    ```
    """
    def __new__(
        cls,
        email: Optional[str],
        secure_settings: Optional[types.SecureSecretSettings],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PasswordInputSettings(TLObject):
    """
    [Read `account.passwordInputSettings` docs](https://core.telegram.org/constructor/account.passwordInputSettings).

    Generated from the following TL definition:
    ```tl
    account.passwordInputSettings#c23727c9 flags:# new_algo:flags.0?PasswordKdfAlgo new_password_hash:flags.0?bytes hint:flags.0?string email:flags.1?string new_secure_settings:flags.2?SecureSecretSettings = account.PasswordInputSettings
    ```
    """
    def __new__(
        cls,
        new_algo: Optional[types.PasswordKdfAlgoUnknown | types.PasswordKdfAlgoSha256Sha256Pbkdf2Hmacsha512iter100000Sha256ModPow],
        new_password_hash: Optional[bytes],
        hint: Optional[str],
        email: Optional[str],
        new_secure_settings: Optional[types.SecureSecretSettings],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TmpPassword(TLObject):
    """
    [Read `account.tmpPassword` docs](https://core.telegram.org/constructor/account.tmpPassword).

    Generated from the following TL definition:
    ```tl
    account.tmpPassword#db64fd34 tmp_password:bytes valid_until:int = account.TmpPassword
    ```
    """
    def __new__(
        cls,
        tmp_password: bytes,
        valid_until: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebAuthorizations(TLObject):
    """
    [Read `account.webAuthorizations` docs](https://core.telegram.org/constructor/account.webAuthorizations).

    Generated from the following TL definition:
    ```tl
    account.webAuthorizations#ed56c9fc authorizations:Vector<WebAuthorization> users:Vector<User> = account.WebAuthorizations
    ```
    """
    def __new__(
        cls,
        authorizations: Sequence[types.WebAuthorization],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AuthorizationForm(TLObject):
    """
    [Read `account.authorizationForm` docs](https://core.telegram.org/constructor/account.authorizationForm).

    Generated from the following TL definition:
    ```tl
    account.authorizationForm#ad2e1cd8 flags:# required_types:Vector<SecureRequiredType> values:Vector<SecureValue> errors:Vector<SecureValueError> users:Vector<User> privacy_policy_url:flags.0?string = account.AuthorizationForm
    ```
    """
    def __new__(
        cls,
        required_types: Sequence[types.SecureRequiredType | types.SecureRequiredTypeOneOf],
        values: Sequence[types.SecureValue],
        errors: Sequence[types.SecureValueErrorData | types.SecureValueErrorFrontSide | types.SecureValueErrorReverseSide | types.SecureValueErrorSelfie | types.SecureValueErrorFile | types.SecureValueErrorFiles | types.SecureValueError | types.SecureValueErrorTranslationFile | types.SecureValueErrorTranslationFiles],
        users: Sequence[types.UserEmpty | types.User],
        privacy_policy_url: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentEmailCode(TLObject):
    """
    [Read `account.sentEmailCode` docs](https://core.telegram.org/constructor/account.sentEmailCode).

    Generated from the following TL definition:
    ```tl
    account.sentEmailCode#811f854f email_pattern:string length:int = account.SentEmailCode
    ```
    """
    def __new__(
        cls,
        email_pattern: str,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Takeout(TLObject):
    """
    [Read `account.takeout` docs](https://core.telegram.org/constructor/account.takeout).

    Generated from the following TL definition:
    ```tl
    account.takeout#4dba4501 id:long = account.Takeout
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WallPapersNotModified(TLObject):
    """
    [Read `account.wallPapersNotModified` docs](https://core.telegram.org/constructor/account.wallPapersNotModified).

    Generated from the following TL definition:
    ```tl
    account.wallPapersNotModified#1c199183 = account.WallPapers
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WallPapers(TLObject):
    """
    [Read `account.wallPapers` docs](https://core.telegram.org/constructor/account.wallPapers).

    Generated from the following TL definition:
    ```tl
    account.wallPapers#cdc3858c hash:long wallpapers:Vector<WallPaper> = account.WallPapers
    ```
    """
    def __new__(
        cls,
        hash: int,
        wallpapers: Sequence[types.WallPaper | types.WallPaperNoFile],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AutoDownloadSettings(TLObject):
    """
    [Read `account.autoDownloadSettings` docs](https://core.telegram.org/constructor/account.autoDownloadSettings).

    Generated from the following TL definition:
    ```tl
    account.autoDownloadSettings#63cacf26 low:AutoDownloadSettings medium:AutoDownloadSettings high:AutoDownloadSettings = account.AutoDownloadSettings
    ```
    """
    def __new__(
        cls,
        low: types.AutoDownloadSettings,
        medium: types.AutoDownloadSettings,
        high: types.AutoDownloadSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ThemesNotModified(TLObject):
    """
    [Read `account.themesNotModified` docs](https://core.telegram.org/constructor/account.themesNotModified).

    Generated from the following TL definition:
    ```tl
    account.themesNotModified#f41eb622 = account.Themes
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Themes(TLObject):
    """
    [Read `account.themes` docs](https://core.telegram.org/constructor/account.themes).

    Generated from the following TL definition:
    ```tl
    account.themes#9a3d8c6d hash:long themes:Vector<Theme> = account.Themes
    ```
    """
    def __new__(
        cls,
        hash: int,
        themes: Sequence[types.Theme],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ContentSettings(TLObject):
    """
    [Read `account.contentSettings` docs](https://core.telegram.org/constructor/account.contentSettings).

    Generated from the following TL definition:
    ```tl
    account.contentSettings#57e28221 flags:# sensitive_enabled:flags.0?true sensitive_can_change:flags.1?true = account.ContentSettings
    ```
    """
    def __new__(
        cls,
        sensitive_enabled: bool,
        sensitive_can_change: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetPasswordFailedWait(TLObject):
    """
    [Read `account.resetPasswordFailedWait` docs](https://core.telegram.org/constructor/account.resetPasswordFailedWait).

    Generated from the following TL definition:
    ```tl
    account.resetPasswordFailedWait#e3779861 retry_date:int = account.ResetPasswordResult
    ```
    """
    def __new__(
        cls,
        retry_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetPasswordRequestedWait(TLObject):
    """
    [Read `account.resetPasswordRequestedWait` docs](https://core.telegram.org/constructor/account.resetPasswordRequestedWait).

    Generated from the following TL definition:
    ```tl
    account.resetPasswordRequestedWait#e9effc7d until_date:int = account.ResetPasswordResult
    ```
    """
    def __new__(
        cls,
        until_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetPasswordOk(TLObject):
    """
    [Read `account.resetPasswordOk` docs](https://core.telegram.org/constructor/account.resetPasswordOk).

    Generated from the following TL definition:
    ```tl
    account.resetPasswordOk#e926d63e = account.ResetPasswordResult
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatThemesNotModified(TLObject):
    """
    [Read `account.chatThemesNotModified` docs](https://core.telegram.org/constructor/account.chatThemesNotModified).

    Generated from the following TL definition:
    ```tl
    account.chatThemesNotModified#e011e1c4 = account.ChatThemes
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatThemes(TLObject):
    """
    [Read `account.chatThemes` docs](https://core.telegram.org/constructor/account.chatThemes).

    Generated from the following TL definition:
    ```tl
    account.chatThemes#be098173 flags:# hash:long themes:Vector<ChatTheme> chats:Vector<Chat> users:Vector<User> next_offset:flags.0?string = account.ChatThemes
    ```
    """
    def __new__(
        cls,
        hash: int,
        themes: Sequence[types.ChatTheme | types.ChatThemeUniqueGift],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
        next_offset: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedRingtonesNotModified(TLObject):
    """
    [Read `account.savedRingtonesNotModified` docs](https://core.telegram.org/constructor/account.savedRingtonesNotModified).

    Generated from the following TL definition:
    ```tl
    account.savedRingtonesNotModified#fbf6e8b1 = account.SavedRingtones
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedRingtones(TLObject):
    """
    [Read `account.savedRingtones` docs](https://core.telegram.org/constructor/account.savedRingtones).

    Generated from the following TL definition:
    ```tl
    account.savedRingtones#c1e92cc5 hash:long ringtones:Vector<Document> = account.SavedRingtones
    ```
    """
    def __new__(
        cls,
        hash: int,
        ringtones: Sequence[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedRingtone(TLObject):
    """
    [Read `account.savedRingtone` docs](https://core.telegram.org/constructor/account.savedRingtone).

    Generated from the following TL definition:
    ```tl
    account.savedRingtone#b7263f6d = account.SavedRingtone
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedRingtoneConverted(TLObject):
    """
    [Read `account.savedRingtoneConverted` docs](https://core.telegram.org/constructor/account.savedRingtoneConverted).

    Generated from the following TL definition:
    ```tl
    account.savedRingtoneConverted#1f307eb7 document:Document = account.SavedRingtone
    ```
    """
    def __new__(
        cls,
        document: types.DocumentEmpty | types.Document,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiStatusesNotModified(TLObject):
    """
    [Read `account.emojiStatusesNotModified` docs](https://core.telegram.org/constructor/account.emojiStatusesNotModified).

    Generated from the following TL definition:
    ```tl
    account.emojiStatusesNotModified#d08ce645 = account.EmojiStatuses
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiStatuses(TLObject):
    """
    [Read `account.emojiStatuses` docs](https://core.telegram.org/constructor/account.emojiStatuses).

    Generated from the following TL definition:
    ```tl
    account.emojiStatuses#90c467d1 hash:long statuses:Vector<EmojiStatus> = account.EmojiStatuses
    ```
    """
    def __new__(
        cls,
        hash: int,
        statuses: Sequence[types.EmojiStatusEmpty | types.EmojiStatus | types.EmojiStatusCollectible | types.InputEmojiStatusCollectible],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmailVerified(TLObject):
    """
    [Read `account.emailVerified` docs](https://core.telegram.org/constructor/account.emailVerified).

    Generated from the following TL definition:
    ```tl
    account.emailVerified#2b96cd1b email:string = account.EmailVerified
    ```
    """
    def __new__(
        cls,
        email: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmailVerifiedLogin(TLObject):
    """
    [Read `account.emailVerifiedLogin` docs](https://core.telegram.org/constructor/account.emailVerifiedLogin).

    Generated from the following TL definition:
    ```tl
    account.emailVerifiedLogin#e1bb0d61 email:string sent_code:auth.SentCode = account.EmailVerified
    ```
    """
    def __new__(
        cls,
        email: str,
        sent_code: types.auth.SentCode | types.auth.SentCodeSuccess | types.auth.SentCodePaymentRequired,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AutoSaveSettings(TLObject):
    """
    [Read `account.autoSaveSettings` docs](https://core.telegram.org/constructor/account.autoSaveSettings).

    Generated from the following TL definition:
    ```tl
    account.autoSaveSettings#4c3e069d users_settings:AutoSaveSettings chats_settings:AutoSaveSettings broadcasts_settings:AutoSaveSettings exceptions:Vector<AutoSaveException> chats:Vector<Chat> users:Vector<User> = account.AutoSaveSettings
    ```
    """
    def __new__(
        cls,
        users_settings: types.AutoSaveSettings,
        chats_settings: types.AutoSaveSettings,
        broadcasts_settings: types.AutoSaveSettings,
        exceptions: Sequence[types.AutoSaveException],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ConnectedBots(TLObject):
    """
    [Read `account.connectedBots` docs](https://core.telegram.org/constructor/account.connectedBots).

    Generated from the following TL definition:
    ```tl
    account.connectedBots#17d7f87b connected_bots:Vector<ConnectedBot> users:Vector<User> = account.ConnectedBots
    ```
    """
    def __new__(
        cls,
        connected_bots: Sequence[types.ConnectedBot],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessChatLinks(TLObject):
    """
    [Read `account.businessChatLinks` docs](https://core.telegram.org/constructor/account.businessChatLinks).

    Generated from the following TL definition:
    ```tl
    account.businessChatLinks#ec43a2d1 links:Vector<BusinessChatLink> chats:Vector<Chat> users:Vector<User> = account.BusinessChatLinks
    ```
    """
    def __new__(
        cls,
        links: Sequence[types.BusinessChatLink],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResolvedBusinessChatLinks(TLObject):
    """
    [Read `account.resolvedBusinessChatLinks` docs](https://core.telegram.org/constructor/account.resolvedBusinessChatLinks).

    Generated from the following TL definition:
    ```tl
    account.resolvedBusinessChatLinks#9a23af21 flags:# peer:Peer message:string entities:flags.0?Vector<MessageEntity> chats:Vector<Chat> users:Vector<User> = account.ResolvedBusinessChatLinks
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaidMessagesRevenue(TLObject):
    """
    [Read `account.paidMessagesRevenue` docs](https://core.telegram.org/constructor/account.paidMessagesRevenue).

    Generated from the following TL definition:
    ```tl
    account.paidMessagesRevenue#1e109708 stars_amount:long = account.PaidMessagesRevenue
    ```
    """
    def __new__(
        cls,
        stars_amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedMusicIdsNotModified(TLObject):
    """
    [Read `account.savedMusicIdsNotModified` docs](https://core.telegram.org/constructor/account.savedMusicIdsNotModified).

    Generated from the following TL definition:
    ```tl
    account.savedMusicIdsNotModified#4fc81d6e = account.SavedMusicIds
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedMusicIds(TLObject):
    """
    [Read `account.savedMusicIds` docs](https://core.telegram.org/constructor/account.savedMusicIds).

    Generated from the following TL definition:
    ```tl
    account.savedMusicIds#998d6636 ids:Vector<long> = account.SavedMusicIds
    ```
    """
    def __new__(
        cls,
        ids: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Passkeys(TLObject):
    """
    [Read `account.passkeys` docs](https://core.telegram.org/constructor/account.passkeys).

    Generated from the following TL definition:
    ```tl
    account.passkeys#f8e0aa1c passkeys:Vector<Passkey> = account.Passkeys
    ```
    """
    def __new__(
        cls,
        passkeys: Sequence[types.Passkey],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PasskeyRegistrationOptions(TLObject):
    """
    [Read `account.passkeyRegistrationOptions` docs](https://core.telegram.org/constructor/account.passkeyRegistrationOptions).

    Generated from the following TL definition:
    ```tl
    account.passkeyRegistrationOptions#e16b5ce1 options:DataJSON = account.PasskeyRegistrationOptions
    ```
    """
    def __new__(
        cls,
        options: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

