from .rpcbaseerrors import (
    RpcError,
    InvalidDCError,
    BadRequestError,
    UnauthorizedError,
    ForbiddenError,
    NotFoundError,
    AuthKeyError,
    FloodError,
    ServerError,
    TimedOutError,
)

__all__ = [
    'TwoFaConfirmWaitError',
    'AboutTooLongError',
    'AccessTokenExpiredError',
    'AccessTokenInvalidError',
    'ActiveUserRequiredError',
    'AdminsTooMuchError',
    'AdminIdInvalidError',
    'AdminRankEmojiNotAllowedError',
    'AdminRankInvalidError',
    'AlbumPhotosTooManyError',
    'ApiIdInvalidError',
    'ApiIdPublishedFloodError',
    'ArticleTitleEmptyError',
    'AudioContentUrlEmptyError',
    'AudioTitleEmptyError',
    'AuthBytesInvalidError',
    'AuthKeyDuplicatedError',
    'AuthKeyInvalidError',
    'AuthKeyPermEmptyError',
    'AuthKeyUnregisteredError',
    'AuthRestartError',
    'AuthTokenAlreadyAcceptedError',
    'AuthTokenExceptionError',
    'AuthTokenExpiredError',
    'AuthTokenInvalidError',
    'AuthTokenInvalid2Error',
    'AuthTokenInvalidxError',
    'AutoarchiveNotAvailableError',
    'BankCardNumberInvalidError',
    'BannedRightsInvalidError',
    'BasePortLocInvalidError',
    'BotsTooMuchError',
    'BotChannelsNaError',
    'BotCommandDescriptionInvalidError',
    'BotCommandInvalidError',
    'BotDomainInvalidError',
    'BotGamesDisabledError',
    'BotGroupsBlockedError',
    'BotInlineDisabledError',
    'BotInvalidError',
    'BotMethodInvalidError',
    'BotMissingError',
    'BotOnesideNotAvailError',
    'BotPaymentsDisabledError',
    'BotPollsDisabledError',
    'BotResponseTimeoutError',
    'BotScoreNotModifiedError',
    'BroadcastCallsDisabledError',
    'BroadcastForbiddenError',
    'BroadcastIdInvalidError',
    'BroadcastPublicVotersForbiddenError',
    'BroadcastRequiredError',
    'ButtonDataInvalidError',
    'ButtonTextInvalidError',
    'ButtonTypeInvalidError',
    'ButtonUrlInvalidError',
    'ButtonUserPrivacyRestrictedError',
    'CallAlreadyAcceptedError',
    'CallAlreadyDeclinedError',
    'CallOccupyFailedError',
    'CallPeerInvalidError',
    'CallProtocolFlagsInvalidError',
    'CdnMethodInvalidError',
    'CdnUploadTimeoutError',
    'ChannelsAdminLocatedTooMuchError',
    'ChannelsAdminPublicTooMuchError',
    'ChannelsTooMuchError',
    'ChannelBannedError',
    'ChannelForumMissingError',
    'ChannelIdInvalidError',
    'ChannelInvalidError',
    'ChannelParicipantMissingError',
    'ChannelPrivateError',
    'ChannelPublicGroupNaError',
    'ChannelTooBigError',
    'ChannelTooLargeError',
    'ChatAboutNotModifiedError',
    'ChatAboutTooLongError',
    'ChatAdminInviteRequiredError',
    'ChatAdminRequiredError',
    'ChatDiscussionUnallowedError',
    'ChatForbiddenError',
    'ChatForwardsRestrictedError',
    'ChatGetFailedError',
    'ChatGuestSendForbiddenError',
    'ChatIdEmptyError',
    'ChatIdGenerateFailedError',
    'ChatIdInvalidError',
    'ChatInvalidError',
    'ChatInvitePermanentError',
    'ChatLinkExistsError',
    'ChatNotModifiedError',
    'ChatRestrictedError',
    'ChatRevokeDateUnsupportedError',
    'ChatSendGameForbiddenError',
    'ChatSendGifsForbiddenError',
    'ChatSendInlineForbiddenError',
    'ChatSendMediaForbiddenError',
    'ChatSendPollForbiddenError',
    'ChatSendStickersForbiddenError',
    'ChatTitleEmptyError',
    'ChatTooBigError',
    'ChatWriteForbiddenError',
    'ChpCallFailError',
    'CodeEmptyError',
    'CodeHashInvalidError',
    'CodeInvalidError',
    'ConnectionApiIdInvalidError',
    'ConnectionAppVersionEmptyError',
    'ConnectionDeviceModelEmptyError',
    'ConnectionLangPackInvalidError',
    'ConnectionLayerInvalidError',
    'ConnectionNotInitedError',
    'ConnectionSystemEmptyError',
    'ConnectionSystemLangCodeEmptyError',
    'ContactAddMissingError',
    'ContactIdInvalidError',
    'ContactNameEmptyError',
    'ContactReqMissingError',
    'CreateCallFailedError',
    'CurrencyTotalAmountInvalidError',
    'DataInvalidError',
    'DataJsonInvalidError',
    'DataTooLongError',
    'DateEmptyError',
    'DcIdInvalidError',
    'DhGAInvalidError',
    'DocumentInvalidError',
    'EditBotInviteForbiddenError',
    'EmailHashExpiredError',
    'EmailInvalidError',
    'EmailUnconfirmedError',
    'EmailUnconfirmedError',
    'EmailVerifyExpiredError',
    'EmojiInvalidError',
    'EmojiNotModifiedError',
    'EmoticonEmptyError',
    'EmoticonInvalidError',
    'EmoticonStickerpackMissingError',
    'EncryptedMessageInvalidError',
    'EncryptionAlreadyAcceptedError',
    'EncryptionAlreadyDeclinedError',
    'EncryptionDeclinedError',
    'EncryptionIdInvalidError',
    'EncryptionOccupyFailedError',
    'EntitiesTooLongError',
    'EntityBoundsInvalidError',
    'EntityMentionUserInvalidError',
    'ErrorTextEmptyError',
    'ExpireDateInvalidError',
    'ExpireForbiddenError',
    'ExportCardInvalidError',
    'ExternalUrlInvalidError',
    'FieldNameEmptyError',
    'FieldNameInvalidError',
    'FilerefUpgradeNeededError',
    'FileContentTypeInvalidError',
    'FileEmtpyError',
    'FileIdInvalidError',
    'FileMigrateError',
    'FilePartsInvalidError',
    'FilePart0MissingError',
    'FilePartEmptyError',
    'FilePartInvalidError',
    'FilePartLengthInvalidError',
    'FilePartSizeChangedError',
    'FilePartSizeInvalidError',
    'FilePartTooBigError',
    'FilePartMissingError',
    'FileReferenceEmptyError',
    'FileReferenceExpiredError',
    'FileReferenceInvalidError',
    'FileTitleEmptyError',
    'FilterIdInvalidError',
    'FilterIncludeEmptyError',
    'FilterNotSupportedError',
    'FilterTitleEmptyError',
    'FirstNameInvalidError',
    'FloodTestPhoneWaitError',
    'FloodWaitError',
    'FloodPremiumWaitError',
    'FolderIdEmptyError',
    'FolderIdInvalidError',
    'FreshChangeAdminsForbiddenError',
    'FreshChangePhoneForbiddenError',
    'FreshResetAuthorisationForbiddenError',
    'FromMessageBotDisabledError',
    'FromPeerInvalidError',
    'GameBotInvalidError',
    'GeoPointInvalidError',
    'GifContentTypeInvalidError',
    'GifIdInvalidError',
    'GraphExpiredReloadError',
    'GraphInvalidReloadError',
    'GraphOutdatedReloadError',
    'GroupcallAddParticipantsFailedError',
    'GroupcallAlreadyDiscardedError',
    'GroupcallAlreadyStartedError',
    'GroupcallForbiddenError',
    'GroupcallInvalidError',
    'GroupcallJoinMissingError',
    'GroupcallNotModifiedError',
    'GroupcallSsrcDuplicateMuchError',
    'GroupedMediaInvalidError',
    'GroupCallInvalidError',
    'HashInvalidError',
    'HideRequesterMissingError',
    'HistoryGetFailedError',
    'ImageProcessFailedError',
    'ImportFileInvalidError',
    'ImportFormatUnrecognizedError',
    'ImportIdInvalidError',
    'InlineBotRequiredError',
    'InlineResultExpiredError',
    'InputConstructorInvalidError',
    'InputFetchErrorError',
    'InputFetchFailError',
    'InputFilterInvalidError',
    'InputLayerInvalidError',
    'InputMethodInvalidError',
    'InputRequestTooLongError',
    'InputTextEmptyError',
    'InputUserDeactivatedError',
    'InterdcCallErrorError',
    'InterdcCallRichErrorError',
    'InviteForbiddenWithJoinasError',
    'InviteHashEmptyError',
    'InviteHashExpiredError',
    'InviteHashInvalidError',
    'InviteRequestSentError',
    'InviteRevokedMissingError',
    'InvoicePayloadInvalidError',
    'JoinAsPeerInvalidError',
    'LangCodeInvalidError',
    'LangCodeNotSupportedError',
    'LangPackInvalidError',
    'LastnameInvalidError',
    'LimitInvalidError',
    'LinkNotModifiedError',
    'LocationInvalidError',
    'MaxDateInvalidError',
    'MaxIdInvalidError',
    'MaxQtsInvalidError',
    'Md5ChecksumInvalidError',
    'MediaCaptionTooLongError',
    'MediaEmptyError',
    'MediaGroupedInvalidError',
    'MediaInvalidError',
    'MediaNewInvalidError',
    'MediaPrevInvalidError',
    'MediaTtlInvalidError',
    'MegagroupIdInvalidError',
    'MegagroupPrehistoryHiddenError',
    'MegagroupRequiredError',
    'MemberNoLocationError',
    'MemberOccupyPrimaryLocFailedError',
    'MessageAuthorRequiredError',
    'MessageDeleteForbiddenError',
    'MessageEditTimeExpiredError',
    'MessageEmptyError',
    'MessageIdsEmptyError',
    'MessageIdInvalidError',
    'MessageNotModifiedError',
    'MessagePollClosedError',
    'MessageTooLongError',
    'MethodInvalidError',
    'MinDateInvalidError',
    'MsgidDecreaseRetryError',
    'MsgIdInvalidError',
    'MsgTooOldError',
    'MsgWaitFailedError',
    'MtSendQueueTooLongError',
    'MultiMediaTooLongError',
    'NeedChatInvalidError',
    'NeedMemberInvalidError',
    'NetworkMigrateError',
    'NewSaltInvalidError',
    'NewSettingsEmptyError',
    'NewSettingsInvalidError',
    'NextOffsetInvalidError',
    'NotAllowedError',
    'OffsetInvalidError',
    'OffsetPeerIdInvalidError',
    'OptionsTooMuchError',
    'OptionInvalidError',
    'PackShortNameInvalidError',
    'PackShortNameOccupiedError',
    'PackTitleInvalidError',
    'ParticipantsTooFewError',
    'ParticipantCallFailedError',
    'ParticipantIdInvalidError',
    'ParticipantJoinMissingError',
    'ParticipantVersionOutdatedError',
    'PasswordEmptyError',
    'PasswordHashInvalidError',
    'PasswordMissingError',
    'PasswordRecoveryExpiredError',
    'PasswordRecoveryNaError',
    'PasswordRequiredError',
    'PasswordTooFreshError',
    'PaymentProviderInvalidError',
    'PeerFloodError',
    'PeerHistoryEmptyError',
    'PeerIdInvalidError',
    'PeerIdNotSupportedError',
    'PersistentTimestampEmptyError',
    'PersistentTimestampInvalidError',
    'PersistentTimestampOutdatedError',
    'PhoneCodeEmptyError',
    'PhoneCodeExpiredError',
    'PhoneCodeHashEmptyError',
    'PhoneCodeInvalidError',
    'PhoneHashExpiredError',
    'PhoneMigrateError',
    'PhoneNotOccupiedError',
    'PhoneNumberAppSignupForbiddenError',
    'PhoneNumberBannedError',
    'PhoneNumberFloodError',
    'PhoneNumberInvalidError',
    'PhoneNumberOccupiedError',
    'PhoneNumberUnoccupiedError',
    'PhonePasswordFloodError',
    'PhonePasswordProtectedError',
    'PhotoContentTypeInvalidError',
    'PhotoContentUrlEmptyError',
    'PhotoCropFileMissingError',
    'PhotoCropSizeSmallError',
    'PhotoExtInvalidError',
    'PhotoFileMissingError',
    'PhotoIdInvalidError',
    'PhotoInvalidError',
    'PhotoInvalidDimensionsError',
    'PhotoSaveFileInvalidError',
    'PhotoThumbUrlEmptyError',
    'PinnedDialogsTooMuchError',
    'PinRestrictedError',
    'PollAnswersInvalidError',
    'PollAnswerInvalidError',
    'PollOptionDuplicateError',
    'PollOptionInvalidError',
    'PollQuestionInvalidError',
    'PollUnsupportedError',
    'PollVoteRequiredError',
    'PostponedTimeoutError',
    'PremiumAccountRequiredError',
    'PremiumCurrentlyUnavailableError',
    'PreviousChatImportActiveWaitMinError',
    'PrivacyKeyInvalidError',
    'PrivacyTooLongError',
    'PrivacyValueInvalidError',
    'PtsChangeEmptyError',
    'PublicChannelMissingError',
    'PublicKeyRequiredError',
    'QueryIdEmptyError',
    'QueryIdInvalidError',
    'QueryTooShortError',
    'QuizAnswerMissingError',
    'QuizCorrectAnswersEmptyError',
    'QuizCorrectAnswersTooMuchError',
    'QuizCorrectAnswerInvalidError',
    'QuizMultipleInvalidError',
    'RandomIdDuplicateError',
    'RandomIdEmptyError',
    'RandomIdInvalidError',
    'RandomLengthInvalidError',
    'RangesInvalidError',
    'ReactionsTooManyError',
    'ReactionEmptyError',
    'ReactionInvalidError',
    'ReflectorNotAvailableError',
    'RegIdGenerateFailedError',
    'ReplyMarkupBuyEmptyError',
    'ReplyMarkupGameEmptyError',
    'ReplyMarkupInvalidError',
    'ReplyMarkupTooLongError',
    'ResetRequestMissingError',
    'ResultsTooMuchError',
    'ResultIdDuplicateError',
    'ResultIdEmptyError',
    'ResultIdInvalidError',
    'ResultTypeInvalidError',
    'RevoteNotAllowedError',
    'RightsNotModifiedError',
    'RightForbiddenError',
    'RpcCallFailError',
    'RpcMcgetFailError',
    'RsaDecryptFailedError',
    'ScheduleBotNotAllowedError',
    'ScheduleDateInvalidError',
    'ScheduleDateTooLateError',
    'ScheduleStatusPrivateError',
    'ScheduleTooMuchError',
    'ScoreInvalidError',
    'SearchQueryEmptyError',
    'SearchWithLinkNotSupportedError',
    'SecondsInvalidError',
    'SendAsPeerInvalidError',
    'SendCodeUnavailableError',
    'SendMessageMediaInvalidError',
    'SendMessageTypeInvalidError',
    'SensitiveChangeForbiddenError',
    'SessionExpiredError',
    'SessionPasswordNeededError',
    'SessionRevokedError',
    'SessionTooFreshError',
    'SettingsInvalidError',
    'Sha256HashInvalidError',
    'ShortnameOccupyFailedError',
    'ShortNameInvalidError',
    'ShortNameOccupiedError',
    'SignInFailedError',
    'SlowModeMultiMsgsDisabledError',
    'SlowModeWaitError',
    'SmsCodeCreateFailedError',
    'SrpIdInvalidError',
    'SrpPasswordChangedError',
    'StartParamEmptyError',
    'StartParamInvalidError',
    'StartParamTooLongError',
    'StatsMigrateError',
    'StickerpackStickersTooMuchError',
    'StickersetInvalidError',
    'StickersetOwnerAnonymousError',
    'StickersEmptyError',
    'StickersTooMuchError',
    'StickerDocumentInvalidError',
    'StickerEmojiInvalidError',
    'StickerFileInvalidError',
    'StickerGifDimensionsError',
    'StickerIdInvalidError',
    'StickerInvalidError',
    'StickerMimeInvalidError',
    'StickerPngDimensionsError',
    'StickerPngNopngError',
    'StickerTgsNodocError',
    'StickerTgsNotgsError',
    'StickerThumbPngNopngError',
    'StickerThumbTgsNotgsError',
    'StickerVideoBigError',
    'StickerVideoNodocError',
    'StickerVideoNowebmError',
    'StorageCheckFailedError',
    'StoreInvalidScalarTypeError',
    'SwitchPmTextEmptyError',
    'TakeoutInitDelayError',
    'TakeoutInvalidError',
    'TakeoutRequiredError',
    'TempAuthKeyAlreadyBoundError',
    'TempAuthKeyEmptyError',
    'ThemeFileInvalidError',
    'ThemeFormatInvalidError',
    'ThemeInvalidError',
    'ThemeMimeInvalidError',
    'ThemeTitleInvalidError',
    'TimeoutError',
    'TitleInvalidError',
    'TmpPasswordDisabledError',
    'TmpPasswordInvalidError',
    'TokenInvalidError',
    'TopicDeletedError',
    'ToLangInvalidError',
    'TtlDaysInvalidError',
    'TtlMediaInvalidError',
    'TtlPeriodInvalidError',
    'TypesEmptyError',
    'TypeConstructorInvalidError',
    'TimedoutError',
    'TimeoutError',
    'UnknownErrorError',
    'UnknownMethodError',
    'UntilDateInvalidError',
    'UpdateAppToLoginError',
    'UrlInvalidError',
    'UsageLimitInvalidError',
    'UsernameInvalidError',
    'UsernameNotModifiedError',
    'UsernameNotOccupiedError',
    'UsernameOccupiedError',
    'UsernamePurchaseAvailableError',
    'UserpicPrivacyRequiredError',
    'UserpicUploadRequiredError',
    'UsersTooFewError',
    'UsersTooMuchError',
    'UserAdminInvalidError',
    'UserAlreadyInvitedError',
    'UserAlreadyParticipantError',
    'UserBannedInChannelError',
    'UserBlockedError',
    'UserBotError',
    'UserBotInvalidError',
    'UserBotRequiredError',
    'UserChannelsTooMuchError',
    'UserCreatorError',
    'UserDeactivatedError',
    'UserDeactivatedBanError',
    'UserDeletedError',
    'UserIdInvalidError',
    'UserInvalidError',
    'UserIsBlockedError',
    'UserIsBotError',
    'UserKickedError',
    'UserMigrateError',
    'UserNotMutualContactError',
    'UserNotParticipantError',
    'UserPrivacyRestrictedError',
    'UserRestrictedError',
    'UserVolumeInvalidError',
    'VideoContentTypeInvalidError',
    'VideoFileInvalidError',
    'VideoTitleEmptyError',
    'VoiceMessagesForbiddenError',
    'WallpaperFileInvalidError',
    'WallpaperInvalidError',
    'WallpaperMimeInvalidError',
    'WcConvertUrlInvalidError',
    'WebdocumentInvalidError',
    'WebdocumentMimeInvalidError',
    'WebdocumentSizeTooBigError',
    'WebdocumentUrlInvalidError',
    'WebpageCurlFailedError',
    'WebpageMediaEmptyError',
    'WebpushAuthInvalidError',
    'WebpushKeyInvalidError',
    'WebpushTokenInvalidError',
    'WorkerBusyTooLongRetryError',
    'YouBlockedUserError',
    'FrozenMethodInvalidError',
    'FrozenParticipantMissingError',
]

class TwoFaConfirmWaitError(FloodError):
    """
    The account is 2FA protected so it will be deleted in a week. Otherwise it can be reset in {seconds}
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AboutTooLongError(BadRequestError):
    """
    The provided bio is too long
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AccessTokenExpiredError(BadRequestError):
    """
    Bot token expired
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AccessTokenInvalidError(BadRequestError):
    """
    The provided token is not valid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ActiveUserRequiredError(UnauthorizedError):
    """
    The method is only available to already activated users
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AdminsTooMuchError(BadRequestError):
    """
    Too many admins
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AdminIdInvalidError(BadRequestError):
    """
    The specified admin ID is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AdminRankEmojiNotAllowedError(BadRequestError):
    """
    Emoji are not allowed in admin titles or ranks
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AdminRankInvalidError(BadRequestError):
    """
    The given admin title or rank was invalid (possibly larger than 16 characters)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AlbumPhotosTooManyError(BadRequestError):
    """
    Too many photos were included in the album
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ApiIdInvalidError(BadRequestError):
    """
    The api_id/api_hash combination is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ApiIdPublishedFloodError(BadRequestError):
    """
    This API id was published somewhere, you can't use it now
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ArticleTitleEmptyError(BadRequestError):
    """
    The title of the article is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AudioContentUrlEmptyError(BadRequestError):
    """
    The remote URL specified in the content field is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AudioTitleEmptyError(BadRequestError):
    """
    The title attribute of the audio must be non-empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AuthBytesInvalidError(BadRequestError):
    """
    The provided authorization is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AuthKeyDuplicatedError(AuthKeyError):
    """
    The authorization key (session file) was used under two different IP addresses simultaneously, and can no longer be used. Use the same session exclusively, or use different sessions
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AuthKeyInvalidError(UnauthorizedError):
    """
    The key is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AuthKeyPermEmptyError(UnauthorizedError):
    """
    The method is unavailable for temporary authorization key, not bound to permanent
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AuthKeyUnregisteredError(UnauthorizedError):
    """
    The key is not registered in the system
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AuthRestartError(ServerError):
    """
    Restart the authorization process
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AuthTokenAlreadyAcceptedError(BadRequestError):
    """
    The authorization token was already used
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AuthTokenExceptionError(BadRequestError):
    """
    An error occurred while importing the auth token
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AuthTokenExpiredError(BadRequestError):
    """
    The provided authorization token has expired and the updated QR-code must be re-scanned
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AuthTokenInvalidError(BadRequestError):
    """
    An invalid authorization token was provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AuthTokenInvalid2Error(BadRequestError):
    """
    An invalid authorization token was provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AuthTokenInvalidxError(BadRequestError):
    """
    The specified auth token is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class AutoarchiveNotAvailableError(BadRequestError):
    """
    You cannot use this feature yet
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BankCardNumberInvalidError(BadRequestError):
    """
    Incorrect credit card number
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BannedRightsInvalidError(BadRequestError):
    """
    You cannot use that set of permissions in this request, i.e. restricting view_messages as a default
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BasePortLocInvalidError(BadRequestError):
    """
    Base port location invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotsTooMuchError(BadRequestError):
    """
    There are too many bots in this chat/channel
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotChannelsNaError(BadRequestError):
    """
    Bots can't edit admin privileges
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotCommandDescriptionInvalidError(BadRequestError):
    """
    The command description was empty, too long or had invalid characters used
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotCommandInvalidError(BadRequestError):
    """
    The specified command is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotDomainInvalidError(BadRequestError):
    """
    The domain used for the auth button does not match the one configured in @BotFather
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotGamesDisabledError(BadRequestError):
    """
    Bot games cannot be used in this type of chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotGroupsBlockedError(BadRequestError):
    """
    This bot can't be added to groups
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotInlineDisabledError(BadRequestError):
    """
    This bot can't be used in inline mode
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotInvalidError(BadRequestError):
    """
    This is not a valid bot
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotMethodInvalidError(BadRequestError):
    """
    The API access for bot users is restricted. The method you tried to invoke cannot be executed as a bot
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotMissingError(BadRequestError):
    """
    This method can only be run by a bot
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotOnesideNotAvailError(BadRequestError):
    """
    Bots can't pin messages in PM just for themselves
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotPaymentsDisabledError(BadRequestError):
    """
    This method can only be run by a bot
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotPollsDisabledError(BadRequestError):
    """
    You cannot create polls under a bot account
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotResponseTimeoutError(BadRequestError):
    """
    The bot did not answer to the callback query in time
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BotScoreNotModifiedError(BadRequestError):
    """
    The score wasn't modified
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BroadcastCallsDisabledError(BadRequestError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BroadcastForbiddenError(ForbiddenError):
    """
    The request cannot be used in broadcast channels
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BroadcastIdInvalidError(BadRequestError):
    """
    The channel is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BroadcastPublicVotersForbiddenError(BadRequestError):
    """
    You cannot broadcast polls where the voters are public
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class BroadcastRequiredError(BadRequestError):
    """
    The request can only be used with a broadcast channel
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ButtonDataInvalidError(BadRequestError):
    """
    The provided button data is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ButtonTextInvalidError(BadRequestError):
    """
    The specified button text is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ButtonTypeInvalidError(BadRequestError):
    """
    The type of one of the buttons you provided is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ButtonUrlInvalidError(BadRequestError):
    """
    Button URL invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ButtonUserPrivacyRestrictedError(BadRequestError):
    """
    The privacy setting of the user specified in a [inputKeyboardButtonUserProfile](/constructor/inputKeyboardButtonUserProfile) button do not allow creating such a button
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class CallAlreadyAcceptedError(BadRequestError):
    """
    The call was already accepted
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class CallAlreadyDeclinedError(BadRequestError):
    """
    The call was already declined
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class CallOccupyFailedError(ServerError):
    """
    The call failed because the user is already making another call
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class CallPeerInvalidError(BadRequestError):
    """
    The provided call peer object is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class CallProtocolFlagsInvalidError(BadRequestError):
    """
    Call protocol flags invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class CdnMethodInvalidError(BadRequestError):
    """
    This method cannot be invoked on a CDN server. Refer to https://core.telegram.org/cdn#schema for available methods
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class CdnUploadTimeoutError(ServerError):
    """
    A server-side timeout occurred while reuploading the file to the CDN DC
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChannelsAdminLocatedTooMuchError(BadRequestError):
    """
    The user has reached the limit of public geogroups
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChannelsAdminPublicTooMuchError(BadRequestError):
    """
    You're admin of too many public channels, make some channels private to change the username of this channel
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChannelsTooMuchError(BadRequestError):
    """
    You have joined too many channels/supergroups
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChannelBannedError(BadRequestError):
    """
    The channel is banned
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChannelForumMissingError(BadRequestError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChannelIdInvalidError(BadRequestError):
    """
    The specified supergroup ID is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChannelInvalidError(BadRequestError):
    """
    Invalid channel object. Make sure to pass the right types, for instance making sure that the request is designed for channels or otherwise look for a different one more suited
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChannelParicipantMissingError(BadRequestError):
    """
    The current user is not in the channel
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChannelPrivateError(BadRequestError):
    """
    The channel specified is private and you lack permission to access it. Another reason may be that you were banned from it
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChannelPublicGroupNaError(ForbiddenError):
    """
    channel/supergroup not available
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChannelTooBigError(BadRequestError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChannelTooLargeError(BadRequestError):
    """
    Channel is too large to be deleted; this error is issued when trying to delete channels with more than 1000 members (subject to change)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatAboutNotModifiedError(BadRequestError):
    """
    About text has not changed
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatAboutTooLongError(BadRequestError):
    """
    Chat about too long
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatAdminInviteRequiredError(ForbiddenError):
    """
    You do not have the rights to do this
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatAdminRequiredError(BadRequestError):
    """
    Chat admin privileges are required to do that in the specified chat (for example, to send a message in a channel which is not yours), or invalid permissions used for the channel or group
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatDiscussionUnallowedError(BadRequestError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatForbiddenError(ForbiddenError):
    """
    You cannot write in this chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatForwardsRestrictedError(BadRequestError):
    """
    You can't forward messages from a protected chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatGetFailedError(ServerError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatGuestSendForbiddenError(ForbiddenError):
    """
    You join the discussion group before commenting, see [here](/api/discussion#requiring-users-to-join-the-group) for more info
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatIdEmptyError(BadRequestError):
    """
    The provided chat ID is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatIdGenerateFailedError(ServerError):
    """
    Failure while generating the chat ID
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatIdInvalidError(BadRequestError):
    """
    Invalid object ID for a chat. Make sure to pass the right types, for instance making sure that the request is designed for chats (not channels/megagroups) or otherwise look for a different one more suited\\nAn example working with a megagroup and AddChatUserRequest, it will fail because megagroups are channels. Use InviteToChannelRequest instead
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatInvalidError(BadRequestError):
    """
    The chat is invalid for this request
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatInvitePermanentError(BadRequestError):
    """
    You can't set an expiration date on permanent invite links
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatLinkExistsError(BadRequestError):
    """
    The chat is linked to a channel and cannot be used in that request
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatNotModifiedError(BadRequestError):
    """
    The chat or channel wasn't modified (title, invites, username, admins, etc. are the same)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatRestrictedError(BadRequestError):
    """
    The chat is restricted and cannot be used in that request
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatRevokeDateUnsupportedError(BadRequestError):
    """
    `min_date` and `max_date` are not available for using with non-user peers
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatSendGameForbiddenError(ForbiddenError):
    """
    You can't send a game to this chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatSendGifsForbiddenError(ForbiddenError):
    """
    You can't send gifs in this chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatSendInlineForbiddenError(BadRequestError):
    """
    You cannot send inline results in this chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatSendMediaForbiddenError(ForbiddenError):
    """
    You can't send media in this chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatSendPollForbiddenError(ForbiddenError):
    """
    You can't send polls in this chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatSendStickersForbiddenError(ForbiddenError):
    """
    You can't send stickers in this chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatTitleEmptyError(BadRequestError):
    """
    No chat title provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatTooBigError(BadRequestError):
    """
    This method is not available for groups with more than `chat_read_mark_size_threshold` members, [see client configuration](https://core.telegram.org/api/config#client-configuration)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChatWriteForbiddenError(ForbiddenError):
    """
    You can't write in this chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ChpCallFailError(ServerError):
    """
    The statistics cannot be retrieved at this time
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class CodeEmptyError(BadRequestError):
    """
    The provided code is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class CodeHashInvalidError(BadRequestError):
    """
    Code hash invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class CodeInvalidError(BadRequestError):
    """
    Code invalid (i.e. from email)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ConnectionApiIdInvalidError(BadRequestError):
    """
    The provided API id is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ConnectionAppVersionEmptyError(BadRequestError):
    """
    App version is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ConnectionDeviceModelEmptyError(BadRequestError):
    """
    Device model empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ConnectionLangPackInvalidError(BadRequestError):
    """
    The specified language pack is not valid. This is meant to be used by official applications only so far, leave it empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ConnectionLayerInvalidError(BadRequestError):
    """
    The very first request must always be InvokeWithLayerRequest
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ConnectionNotInitedError(BadRequestError):
    """
    Connection not initialized
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ConnectionSystemEmptyError(BadRequestError):
    """
    Connection system empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ConnectionSystemLangCodeEmptyError(BadRequestError):
    """
    The system language string was empty during connection
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ContactAddMissingError(BadRequestError):
    """
    Contact to add is missing
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ContactIdInvalidError(BadRequestError):
    """
    The provided contact ID is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ContactNameEmptyError(BadRequestError):
    """
    The provided contact name cannot be empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ContactReqMissingError(BadRequestError):
    """
    Missing contact request
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class CreateCallFailedError(BadRequestError):
    """
    An error occurred while creating the call
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class CurrencyTotalAmountInvalidError(BadRequestError):
    """
    The total amount of all prices is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class DataInvalidError(BadRequestError):
    """
    Encrypted data invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class DataJsonInvalidError(BadRequestError):
    """
    The provided JSON data is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class DataTooLongError(BadRequestError):
    """
    Data too long
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class DateEmptyError(BadRequestError):
    """
    Date empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class DcIdInvalidError(BadRequestError):
    """
    This occurs when an authorization is tried to be exported for the same data center one is currently connected to
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class DhGAInvalidError(BadRequestError):
    """
    g_a invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class DocumentInvalidError(BadRequestError):
    """
    The document file was invalid and can't be used in inline mode
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EditBotInviteForbiddenError(ForbiddenError):
    """
    Normal users can't edit invites that were created by bots
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EmailHashExpiredError(BadRequestError):
    """
    The email hash expired and cannot be used to verify it
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EmailInvalidError(BadRequestError):
    """
    The given email is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EmailUnconfirmedError(BadRequestError):
    """
    Email unconfirmed
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EmailUnconfirmedError(BadRequestError):
    """
    Email unconfirmed, the length of the code must be {code_length}
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EmailVerifyExpiredError(BadRequestError):
    """
    The verification email has expired
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EmojiInvalidError(BadRequestError):
    """
    The specified theme emoji is valid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EmojiNotModifiedError(BadRequestError):
    """
    The theme wasn't changed
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EmoticonEmptyError(BadRequestError):
    """
    The emoticon field cannot be empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EmoticonInvalidError(BadRequestError):
    """
    The specified emoticon cannot be used or was not a emoticon
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EmoticonStickerpackMissingError(BadRequestError):
    """
    The emoticon sticker pack you are trying to get is missing
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EncryptedMessageInvalidError(BadRequestError):
    """
    Encrypted message invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EncryptionAlreadyAcceptedError(BadRequestError):
    """
    Secret chat already accepted
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EncryptionAlreadyDeclinedError(BadRequestError):
    """
    The secret chat was already declined
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EncryptionDeclinedError(BadRequestError):
    """
    The secret chat was declined
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EncryptionIdInvalidError(BadRequestError):
    """
    The provided secret chat ID is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EncryptionOccupyFailedError(ServerError):
    """
    TDLib developer claimed it is not an error while accepting secret chats and 500 is used instead of 420
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EntitiesTooLongError(BadRequestError):
    """
    It is no longer possible to send such long data inside entity tags (for example inline text URLs)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EntityBoundsInvalidError(BadRequestError):
    """
    Some of provided entities have invalid bounds (length is zero or out of the boundaries of the string)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class EntityMentionUserInvalidError(BadRequestError):
    """
    You can't use this entity
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ErrorTextEmptyError(BadRequestError):
    """
    The provided error message is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ExpireDateInvalidError(BadRequestError):
    """
    The specified expiration date is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ExpireForbiddenError(BadRequestError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ExportCardInvalidError(BadRequestError):
    """
    Provided card is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ExternalUrlInvalidError(BadRequestError):
    """
    External URL invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FieldNameEmptyError(BadRequestError):
    """
    The field with the name FIELD_NAME is missing
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FieldNameInvalidError(BadRequestError):
    """
    The field with the name FIELD_NAME is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilerefUpgradeNeededError(AuthKeyError):
    """
    The file reference needs to be refreshed before being used again
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FileContentTypeInvalidError(BadRequestError):
    """
    File content-type is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FileEmtpyError(BadRequestError):
    """
    An empty file was provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FileIdInvalidError(BadRequestError):
    """
    The provided file id is invalid. Make sure all parameters are present, have the correct type and are not empty (ID, access hash, file reference, thumb size ...)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FileMigrateError(InvalidDCError):
    """
    The file to be accessed is currently stored in DC {new_dc}
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilePartsInvalidError(BadRequestError):
    """
    The number of file parts is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilePart0MissingError(BadRequestError):
    """
    File part 0 missing
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilePartEmptyError(BadRequestError):
    """
    The provided file part is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilePartInvalidError(BadRequestError):
    """
    The file part number is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilePartLengthInvalidError(BadRequestError):
    """
    The length of a file part is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilePartSizeChangedError(BadRequestError):
    """
    The file part size (chunk size) cannot change during upload
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilePartSizeInvalidError(BadRequestError):
    """
    The provided file part size is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilePartTooBigError(BadRequestError):
    """
    The uploaded file part is too big
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilePartMissingError(BadRequestError):
    """
    Part {which} of the file is missing from storage
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FileReferenceEmptyError(BadRequestError):
    """
    The file reference must exist to access the media and it cannot be empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FileReferenceExpiredError(BadRequestError):
    """
    The file reference has expired and is no longer valid or it belongs to self-destructing media and cannot be resent
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FileReferenceInvalidError(BadRequestError):
    """
    The file reference is invalid or you can't do that operation on such message
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FileTitleEmptyError(BadRequestError):
    """
    An empty file title was specified
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilterIdInvalidError(BadRequestError):
    """
    The specified filter ID is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilterIncludeEmptyError(BadRequestError):
    """
    The include_peers vector of the filter is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilterNotSupportedError(BadRequestError):
    """
    The specified filter cannot be used in this context
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FilterTitleEmptyError(BadRequestError):
    """
    The title field of the filter is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FirstNameInvalidError(BadRequestError):
    """
    The first name is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FloodTestPhoneWaitError(FloodError):
    """
    A wait of {seconds} seconds is required in the test servers
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FloodWaitError(FloodError):
    """
    A wait of {seconds} seconds is required
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FloodPremiumWaitError(FloodError):
    """
    A wait of {seconds} seconds is required in non-premium accounts
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FolderIdEmptyError(BadRequestError):
    """
    The folder you tried to delete was already empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FolderIdInvalidError(BadRequestError):
    """
    The folder you tried to use was not valid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FreshChangeAdminsForbiddenError(BadRequestError):
    """
    Recently logged-in users cannot add or change admins
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FreshChangePhoneForbiddenError(AuthKeyError):
    """
    Recently logged-in users cannot use this request
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FreshResetAuthorisationForbiddenError(AuthKeyError):
    """
    The current session is too new and cannot be used to reset other authorisations yet
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FromMessageBotDisabledError(BadRequestError):
    """
    Bots can't use fromMessage min constructors
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FromPeerInvalidError(BadRequestError):
    """
    The given from_user peer cannot be used for the parameter
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GameBotInvalidError(BadRequestError):
    """
    You cannot send that game with the current bot
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GeoPointInvalidError(BadRequestError):
    """
    Invalid geoposition provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GifContentTypeInvalidError(BadRequestError):
    """
    GIF content-type invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GifIdInvalidError(BadRequestError):
    """
    The provided GIF ID is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GraphExpiredReloadError(BadRequestError):
    """
    This graph has expired, please obtain a new graph token
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GraphInvalidReloadError(BadRequestError):
    """
    Invalid graph token provided, please reload the stats and provide the updated token
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GraphOutdatedReloadError(BadRequestError):
    """
    Data can't be used for the channel statistics, graphs outdated
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GroupcallAddParticipantsFailedError(ServerError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GroupcallAlreadyDiscardedError(BadRequestError):
    """
    The group call was already discarded
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GroupcallAlreadyStartedError(ForbiddenError):
    """
    The groupcall has already started, you can join directly using [phone.joinGroupCall](https://core.telegram.org/method/phone.joinGroupCall)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GroupcallForbiddenError(ForbiddenError):
    """
    The group call has already ended
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GroupcallInvalidError(BadRequestError):
    """
    The specified group call is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GroupcallJoinMissingError(BadRequestError):
    """
    You haven't joined this group call
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GroupcallNotModifiedError(BadRequestError):
    """
    Group call settings weren't modified
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GroupcallSsrcDuplicateMuchError(BadRequestError):
    """
    The app needs to retry joining the group call with a new SSRC value
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GroupedMediaInvalidError(BadRequestError):
    """
    Invalid grouped media
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class GroupCallInvalidError(BadRequestError):
    """
    Group call invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class HashInvalidError(BadRequestError):
    """
    The provided hash is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class HideRequesterMissingError(BadRequestError):
    """
    The join request was missing or was already handled
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class HistoryGetFailedError(ServerError):
    """
    Fetching of history failed
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ImageProcessFailedError(BadRequestError):
    """
    Failure while processing image
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ImportFileInvalidError(BadRequestError):
    """
    The file is too large to be imported
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ImportFormatUnrecognizedError(BadRequestError):
    """
    Unknown import format
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ImportIdInvalidError(BadRequestError):
    """
    The specified import ID is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InlineBotRequiredError(ForbiddenError):
    """
    The action must be performed through an inline bot callback
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InlineResultExpiredError(BadRequestError):
    """
    The inline query expired
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InputConstructorInvalidError(BadRequestError):
    """
    The provided constructor is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InputFetchErrorError(BadRequestError):
    """
    An error occurred while deserializing TL parameters
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InputFetchFailError(BadRequestError):
    """
    Failed deserializing TL payload
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InputFilterInvalidError(BadRequestError):
    """
    The search query filter is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InputLayerInvalidError(BadRequestError):
    """
    The provided layer is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InputMethodInvalidError(BadRequestError):
    """
    The invoked method does not exist anymore or has never existed
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InputRequestTooLongError(BadRequestError):
    """
    The input request was too long. This may be a bug in the library as it can occur when serializing more bytes than it should (like appending the vector constructor code at the end of a message)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InputTextEmptyError(BadRequestError):
    """
    The specified text is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InputUserDeactivatedError(BadRequestError):
    """
    The specified user was deleted
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InterdcCallErrorError(ServerError):
    """
    An error occurred while communicating with DC {dc}
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InterdcCallRichErrorError(ServerError):
    """
    A rich error occurred while communicating with DC {dc}
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InviteForbiddenWithJoinasError(BadRequestError):
    """
    If the user has anonymously joined a group call as a channel, they can't invite other users to the group call because that would cause deanonymization, because the invite would be sent using the original user ID, not the anonymized channel ID
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InviteHashEmptyError(BadRequestError):
    """
    The invite hash is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InviteHashExpiredError(BadRequestError):
    """
    The chat the user tried to join has expired and is not valid anymore
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InviteHashInvalidError(BadRequestError):
    """
    The invite hash is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InviteRequestSentError(BadRequestError):
    """
    You have successfully requested to join this chat or channel
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InviteRevokedMissingError(BadRequestError):
    """
    The specified invite link was already revoked or is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class InvoicePayloadInvalidError(BadRequestError):
    """
    The specified invoice payload is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class JoinAsPeerInvalidError(BadRequestError):
    """
    The specified peer cannot be used to join a group call
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class LangCodeInvalidError(BadRequestError):
    """
    The specified language code is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class LangCodeNotSupportedError(BadRequestError):
    """
    The specified language code is not supported
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class LangPackInvalidError(BadRequestError):
    """
    The provided language pack is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class LastnameInvalidError(BadRequestError):
    """
    The last name is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class LimitInvalidError(BadRequestError):
    """
    An invalid limit was provided. See https://core.telegram.org/api/files#downloading-files
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class LinkNotModifiedError(BadRequestError):
    """
    The channel is already linked to this group
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class LocationInvalidError(BadRequestError):
    """
    The location given for a file was invalid. See https://core.telegram.org/api/files#downloading-files
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MaxDateInvalidError(BadRequestError):
    """
    The specified maximum date is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MaxIdInvalidError(BadRequestError):
    """
    The provided max ID is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MaxQtsInvalidError(BadRequestError):
    """
    The provided QTS were invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class Md5ChecksumInvalidError(BadRequestError):
    """
    The MD5 check-sums do not match
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MediaCaptionTooLongError(BadRequestError):
    """
    The caption is too long
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MediaEmptyError(BadRequestError):
    """
    The provided media object is invalid or the current account may not be able to send it (such as games as users)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MediaGroupedInvalidError(BadRequestError):
    """
    You tried to send media of different types in an album
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MediaInvalidError(BadRequestError):
    """
    Media invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MediaNewInvalidError(BadRequestError):
    """
    The new media to edit the message with is invalid (such as stickers or voice notes)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MediaPrevInvalidError(BadRequestError):
    """
    The old media cannot be edited with anything else (such as stickers or voice notes)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MediaTtlInvalidError(BadRequestError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MegagroupIdInvalidError(BadRequestError):
    """
    The group is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MegagroupPrehistoryHiddenError(BadRequestError):
    """
    You can't set this discussion group because it's history is hidden
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MegagroupRequiredError(BadRequestError):
    """
    The request can only be used with a megagroup channel
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MemberNoLocationError(ServerError):
    """
    An internal failure occurred while fetching user info (couldn't find location)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MemberOccupyPrimaryLocFailedError(ServerError):
    """
    Occupation of primary member location failed
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MessageAuthorRequiredError(ForbiddenError):
    """
    Message author required
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MessageDeleteForbiddenError(ForbiddenError):
    """
    You can't delete one of the messages you tried to delete, most likely because it is a service message.
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MessageEditTimeExpiredError(BadRequestError):
    """
    You can't edit this message anymore, too much time has passed since its creation.
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MessageEmptyError(BadRequestError):
    """
    Empty or invalid UTF-8 message was sent
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MessageIdsEmptyError(BadRequestError):
    """
    No message ids were provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MessageIdInvalidError(BadRequestError):
    """
    The specified message ID is invalid or you can't do that operation on such message
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MessageNotModifiedError(BadRequestError):
    """
    Content of the message was not modified
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MessagePollClosedError(BadRequestError):
    """
    The poll was closed and can no longer be voted on
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MessageTooLongError(BadRequestError):
    """
    Message was too long
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MethodInvalidError(BadRequestError):
    """
    The API method is invalid and cannot be used
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MinDateInvalidError(BadRequestError):
    """
    The specified minimum date is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MsgidDecreaseRetryError(ServerError):
    """
    The request should be retried with a lower message ID
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MsgIdInvalidError(BadRequestError):
    """
    The message ID used in the peer was invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MsgTooOldError(BadRequestError):
    """
    [`chat_read_mark_expire_period` seconds](https://core.telegram.org/api/config#chat-read-mark-expire-period) have passed since the message was sent, read receipts were deleted
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MsgWaitFailedError(BadRequestError):
    """
    A waiting call returned an error
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MtSendQueueTooLongError(ServerError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class MultiMediaTooLongError(BadRequestError):
    """
    Too many media files were included in the same album
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class NeedChatInvalidError(ServerError):
    """
    The provided chat is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class NeedMemberInvalidError(ServerError):
    """
    The provided member is invalid or does not exist (for example a thumb size)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class NetworkMigrateError(InvalidDCError):
    """
    The source IP address is associated with DC {new_dc}
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class NewSaltInvalidError(BadRequestError):
    """
    The new salt is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class NewSettingsEmptyError(BadRequestError):
    """
    No password is set on the current account, and no new password was specified in `new_settings`
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class NewSettingsInvalidError(BadRequestError):
    """
    The new settings are invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class NextOffsetInvalidError(BadRequestError):
    """
    The value for next_offset is invalid. Check that it has normal characters and is not too long
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class NotAllowedError(ForbiddenError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class OffsetInvalidError(BadRequestError):
    """
    The given offset was invalid, it must be divisible by 1KB. See https://core.telegram.org/api/files#downloading-files
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class OffsetPeerIdInvalidError(BadRequestError):
    """
    The provided offset peer is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class OptionsTooMuchError(BadRequestError):
    """
    You defined too many options for the poll
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class OptionInvalidError(BadRequestError):
    """
    The option specified is invalid and does not exist in the target poll
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PackShortNameInvalidError(BadRequestError):
    """
    Invalid sticker pack name. It must begin with a letter, can\'t contain consecutive underscores and must end in "_by_<bot username>".
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PackShortNameOccupiedError(BadRequestError):
    """
    A stickerpack with this name already exists
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PackTitleInvalidError(BadRequestError):
    """
    The stickerpack title is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ParticipantsTooFewError(BadRequestError):
    """
    Not enough participants
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ParticipantCallFailedError(ServerError):
    """
    Failure while making call
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ParticipantIdInvalidError(BadRequestError):
    """
    The specified participant ID is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ParticipantJoinMissingError(BadRequestError):
    """
    Trying to enable a presentation, when the user hasn't joined the Video Chat with [phone.joinGroupCall](https://core.telegram.org/method/phone.joinGroupCall)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ParticipantVersionOutdatedError(BadRequestError):
    """
    The other participant does not use an up to date telegram client with support for calls
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PasswordEmptyError(BadRequestError):
    """
    The provided password is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PasswordHashInvalidError(BadRequestError):
    """
    The password (and thus its hash value) you entered is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PasswordMissingError(BadRequestError):
    """
    The account must have 2-factor authentication enabled (a password) before this method can be used
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PasswordRecoveryExpiredError(BadRequestError):
    """
    The recovery code has expired
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PasswordRecoveryNaError(BadRequestError):
    """
    No email was set, can't recover password via email
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PasswordRequiredError(BadRequestError):
    """
    The account must have 2-factor authentication enabled (a password) before this method can be used
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PasswordTooFreshError(BadRequestError):
    """
    The password was added too recently and {seconds} seconds must pass before using the method
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PaymentProviderInvalidError(BadRequestError):
    """
    The payment provider was not recognised or its token was invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PeerFloodError(BadRequestError):
    """
    Too many requests
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PeerHistoryEmptyError(BadRequestError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PeerIdInvalidError(BadRequestError):
    """
    An invalid Peer was used. Make sure to pass the right peer type and that the value is valid (for instance, bots cannot start conversations)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PeerIdNotSupportedError(BadRequestError):
    """
    The provided peer ID is not supported
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PersistentTimestampEmptyError(BadRequestError):
    """
    Persistent timestamp empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PersistentTimestampInvalidError(BadRequestError):
    """
    Persistent timestamp invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PersistentTimestampOutdatedError(ServerError):
    """
    Persistent timestamp outdated
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneCodeEmptyError(BadRequestError):
    """
    The phone code is missing
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneCodeExpiredError(BadRequestError):
    """
    The confirmation code has expired
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneCodeHashEmptyError(BadRequestError):
    """
    The phone code hash is missing
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneCodeInvalidError(BadRequestError):
    """
    The phone code entered was invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneHashExpiredError(BadRequestError):
    """
    An invalid or expired `phone_code_hash` was provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneMigrateError(InvalidDCError):
    """
    The phone number a user is trying to use for authorization is associated with DC {new_dc}
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneNotOccupiedError(BadRequestError):
    """
    No user is associated to the specified phone number
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneNumberAppSignupForbiddenError(BadRequestError):
    """
    You can't sign up using this app
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneNumberBannedError(BadRequestError):
    """
    The used phone number has been banned from Telegram and cannot be used anymore. Maybe check https://www.telegram.org/faq_spam
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneNumberFloodError(BadRequestError):
    """
    You asked for the code too many times.
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneNumberInvalidError(BadRequestError):
    """
    The phone number is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneNumberOccupiedError(BadRequestError):
    """
    The phone number is already in use
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhoneNumberUnoccupiedError(BadRequestError):
    """
    The phone number is not yet being used
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhonePasswordFloodError(AuthKeyError):
    """
    You have tried logging in too many times
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhonePasswordProtectedError(BadRequestError):
    """
    This phone is password protected
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhotoContentTypeInvalidError(BadRequestError):
    """
    Photo mime-type invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhotoContentUrlEmptyError(BadRequestError):
    """
    The content from the URL used as a photo appears to be empty or has caused another HTTP error
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhotoCropFileMissingError(BadRequestError):
    """
    Photo crop file missing
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhotoCropSizeSmallError(BadRequestError):
    """
    Photo is too small
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhotoExtInvalidError(BadRequestError):
    """
    The extension of the photo is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhotoFileMissingError(BadRequestError):
    """
    Profile photo file missing
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhotoIdInvalidError(BadRequestError):
    """
    Photo id is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhotoInvalidError(BadRequestError):
    """
    Photo invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhotoInvalidDimensionsError(BadRequestError):
    """
    The photo dimensions are invalid (hint: `pip install pillow` for `send_file` to resize images)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhotoSaveFileInvalidError(BadRequestError):
    """
    The photo you tried to send cannot be saved by Telegram. A reason may be that it exceeds 10MB. Try resizing it locally
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PhotoThumbUrlEmptyError(BadRequestError):
    """
    The URL used as a thumbnail appears to be empty or has caused another HTTP error
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PinnedDialogsTooMuchError(BadRequestError):
    """
    Too many pinned dialogs
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PinRestrictedError(BadRequestError):
    """
    You can't pin messages in private chats with other people
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PollAnswersInvalidError(BadRequestError):
    """
    The poll did not have enough answers or had too many
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PollAnswerInvalidError(BadRequestError):
    """
    One of the poll answers is not acceptable
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PollOptionDuplicateError(BadRequestError):
    """
    A duplicate option was sent in the same poll
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PollOptionInvalidError(BadRequestError):
    """
    A poll option used invalid data (the data may be too long)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PollQuestionInvalidError(BadRequestError):
    """
    The poll question was either empty or too long
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PollUnsupportedError(BadRequestError):
    """
    This layer does not support polls in the issued method
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PollVoteRequiredError(ForbiddenError):
    """
    Cast a vote in the poll before calling this method
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PostponedTimeoutError(ServerError):
    """
    The postponed call has timed out
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PremiumAccountRequiredError(ForbiddenError):
    """
    A premium account is required to execute this action
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PremiumCurrentlyUnavailableError(AuthKeyError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PreviousChatImportActiveWaitMinError(AuthKeyError):
    """
    Similar to a flood wait, must wait {minutes} minutes
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PrivacyKeyInvalidError(BadRequestError):
    """
    The privacy key is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PrivacyTooLongError(BadRequestError):
    """
    Cannot add that many entities in a single request
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PrivacyValueInvalidError(BadRequestError):
    """
    The privacy value is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PtsChangeEmptyError(ServerError):
    """
    No PTS change
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PublicChannelMissingError(ForbiddenError):
    """
    You can only export group call invite links for public chats or channels
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class PublicKeyRequiredError(BadRequestError):
    """
    A public key is required
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class QueryIdEmptyError(BadRequestError):
    """
    The query ID is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class QueryIdInvalidError(BadRequestError):
    """
    The query ID is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class QueryTooShortError(BadRequestError):
    """
    The query string is too short
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class QuizAnswerMissingError(BadRequestError):
    """
    You can forward a quiz while hiding the original author only after choosing an option in the quiz
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class QuizCorrectAnswersEmptyError(BadRequestError):
    """
    A quiz must specify one correct answer
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class QuizCorrectAnswersTooMuchError(BadRequestError):
    """
    There can only be one correct answer
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class QuizCorrectAnswerInvalidError(BadRequestError):
    """
    The correct answer is not an existing answer
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class QuizMultipleInvalidError(BadRequestError):
    """
    A poll cannot be both multiple choice and quiz
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class RandomIdDuplicateError(ServerError):
    """
    You provided a random ID that was already used
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class RandomIdEmptyError(BadRequestError):
    """
    Random ID empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class RandomIdInvalidError(BadRequestError):
    """
    A provided random ID is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class RandomLengthInvalidError(BadRequestError):
    """
    Random length invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class RangesInvalidError(BadRequestError):
    """
    Invalid range provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ReactionsTooManyError(BadRequestError):
    """
    The message already has exactly `reactions_uniq_max` reaction emojis, you can't react with a new emoji, see [the docs for more info](/api/config#client-configuration)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ReactionEmptyError(BadRequestError):
    """
    No reaction provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ReactionInvalidError(BadRequestError):
    """
    Invalid reaction provided (only emoji are allowed)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ReflectorNotAvailableError(BadRequestError):
    """
    Invalid call reflector server
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class RegIdGenerateFailedError(ServerError):
    """
    Failure while generating registration ID
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ReplyMarkupBuyEmptyError(BadRequestError):
    """
    Reply markup for buy button empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ReplyMarkupGameEmptyError(BadRequestError):
    """
    The provided reply markup for the game is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ReplyMarkupInvalidError(BadRequestError):
    """
    The provided reply markup is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ReplyMarkupTooLongError(BadRequestError):
    """
    The data embedded in the reply markup buttons was too much
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ResetRequestMissingError(BadRequestError):
    """
    No password reset is in progress
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ResultsTooMuchError(BadRequestError):
    """
    You sent too many results, see https://core.telegram.org/bots/api#answerinlinequery for the current limit
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ResultIdDuplicateError(BadRequestError):
    """
    Duplicated IDs on the sent results. Make sure to use unique IDs
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ResultIdEmptyError(BadRequestError):
    """
    Result ID empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ResultIdInvalidError(BadRequestError):
    """
    The given result cannot be used to send the selection to the bot
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ResultTypeInvalidError(BadRequestError):
    """
    Result type invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class RevoteNotAllowedError(BadRequestError):
    """
    You cannot change your vote
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class RightsNotModifiedError(BadRequestError):
    """
    The new admin rights are equal to the old rights, no change was made
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class RightForbiddenError(ForbiddenError):
    """
    Either your admin rights do not allow you to do this or you passed the wrong rights combination (some rights only apply to channels and vice versa)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class RpcCallFailError(ServerError):
    """
    Telegram is having internal issues, please try again later.
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class RpcMcgetFailError(ServerError):
    """
    Telegram is having internal issues, please try again later.
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class RsaDecryptFailedError(BadRequestError):
    """
    Internal RSA decryption failed
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ScheduleBotNotAllowedError(BadRequestError):
    """
    Bots are not allowed to schedule messages
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ScheduleDateInvalidError(BadRequestError):
    """
    Invalid schedule date provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ScheduleDateTooLateError(BadRequestError):
    """
    The date you tried to schedule is too far in the future (last known limit of 1 year and a few hours)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ScheduleStatusPrivateError(BadRequestError):
    """
    You cannot schedule a message until the person comes online if their privacy does not show this information
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ScheduleTooMuchError(BadRequestError):
    """
    You cannot schedule more messages in this chat (last known limit of 100 per chat)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ScoreInvalidError(BadRequestError):
    """
    The specified game score is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SearchQueryEmptyError(BadRequestError):
    """
    The search query is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SearchWithLinkNotSupportedError(BadRequestError):
    """
    You cannot provide a search query and an invite link at the same time
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SecondsInvalidError(BadRequestError):
    """
    Slow mode only supports certain values (e.g. 0, 10s, 30s, 1m, 5m, 15m and 1h)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SendAsPeerInvalidError(BadRequestError):
    """
    You can't send messages as the specified peer
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SendCodeUnavailableError(AuthKeyError):
    """
    Returned when all available options for this type of number were already used (e.g. flash-call, then SMS, then this error might be returned to trigger a second resend)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SendMessageMediaInvalidError(BadRequestError):
    """
    The message media was invalid or not specified
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SendMessageTypeInvalidError(BadRequestError):
    """
    The message type is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SensitiveChangeForbiddenError(ForbiddenError):
    """
    Your sensitive content settings cannot be changed at this time
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SessionExpiredError(UnauthorizedError):
    """
    The authorization has expired
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SessionPasswordNeededError(UnauthorizedError):
    """
    Two-steps verification is enabled and a password is required
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SessionRevokedError(UnauthorizedError):
    """
    The authorization has been invalidated, because of the user terminating all sessions
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SessionTooFreshError(BadRequestError):
    """
    The session logged in too recently and {seconds} seconds must pass before calling the method
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SettingsInvalidError(BadRequestError):
    """
    Invalid settings were provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class Sha256HashInvalidError(BadRequestError):
    """
    The provided SHA256 hash is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ShortnameOccupyFailedError(BadRequestError):
    """
    An error occurred when trying to register the short-name used for the sticker pack. Try a different name
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ShortNameInvalidError(BadRequestError):
    """
    The specified short name is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ShortNameOccupiedError(BadRequestError):
    """
    The specified short name is already in use
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SignInFailedError(ServerError):
    """
    Failure while signing in
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SlowModeMultiMsgsDisabledError(BadRequestError):
    """
    Slowmode is enabled, you cannot forward multiple messages to this group
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SlowModeWaitError(FloodError):
    """
    A wait of {seconds} seconds is required before sending another message in this chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SmsCodeCreateFailedError(BadRequestError):
    """
    An error occurred while creating the SMS code
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SrpIdInvalidError(BadRequestError):
    """
    Invalid SRP ID provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SrpPasswordChangedError(BadRequestError):
    """
    Password has changed
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StartParamEmptyError(BadRequestError):
    """
    The start parameter is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StartParamInvalidError(BadRequestError):
    """
    Start parameter invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StartParamTooLongError(BadRequestError):
    """
    Start parameter is too long
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StatsMigrateError(InvalidDCError):
    """
    The channel statistics must be fetched from DC {dc}
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerpackStickersTooMuchError(BadRequestError):
    """
    There are too many stickers in this stickerpack, you can't add any more
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickersetInvalidError(BadRequestError):
    """
    The provided sticker set is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickersetOwnerAnonymousError(AuthKeyError):
    """
    This sticker set can't be used as the group's official stickers because it was created by one of its anonymous admins
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickersEmptyError(BadRequestError):
    """
    No sticker provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickersTooMuchError(BadRequestError):
    """
    There are too many stickers in this stickerpack, you can't add any more
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerDocumentInvalidError(BadRequestError):
    """
    The sticker file was invalid (this file has failed Telegram internal checks, make sure to use the correct format and comply with https://core.telegram.org/animated_stickers)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerEmojiInvalidError(BadRequestError):
    """
    Sticker emoji invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerFileInvalidError(BadRequestError):
    """
    Sticker file invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerGifDimensionsError(BadRequestError):
    """
    The specified video sticker has invalid dimensions
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerIdInvalidError(BadRequestError):
    """
    The provided sticker ID is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerInvalidError(BadRequestError):
    """
    The provided sticker is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerMimeInvalidError(BadRequestError):
    """
    Make sure to pass a valid image file for the right InputFile parameter
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerPngDimensionsError(BadRequestError):
    """
    Sticker png dimensions invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerPngNopngError(BadRequestError):
    """
    Stickers must be a png file but the used image was not a png
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerTgsNodocError(BadRequestError):
    """
    You must send the animated sticker as a document
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerTgsNotgsError(BadRequestError):
    """
    Stickers must be a tgs file but the used file was not a tgs
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerThumbPngNopngError(BadRequestError):
    """
    Stickerset thumb must be a png file but the used file was not png
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerThumbTgsNotgsError(BadRequestError):
    """
    Stickerset thumb must be a tgs file but the used file was not tgs
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerVideoBigError(BadRequestError):
    """
    The specified video sticker is too big
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerVideoNodocError(BadRequestError):
    """
    You must send the video sticker as a document
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StickerVideoNowebmError(BadRequestError):
    """
    The specified video sticker is not in webm format
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StorageCheckFailedError(ServerError):
    """
    Server storage check failed
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class StoreInvalidScalarTypeError(ServerError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class SwitchPmTextEmptyError(BadRequestError):
    """
    The switch_pm.text field was empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TakeoutInitDelayError(FloodError):
    """
    A wait of {seconds} seconds is required before being able to initiate the takeout
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TakeoutInvalidError(BadRequestError):
    """
    The takeout session has been invalidated by another data export session
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TakeoutRequiredError(BadRequestError):
    """
    You must initialize a takeout request first
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TempAuthKeyAlreadyBoundError(BadRequestError):
    """
    The passed temporary key is already bound to another **perm_auth_key_id**
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TempAuthKeyEmptyError(BadRequestError):
    """
    No temporary auth key provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ThemeFileInvalidError(BadRequestError):
    """
    Invalid theme file provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ThemeFormatInvalidError(BadRequestError):
    """
    Invalid theme format provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ThemeInvalidError(BadRequestError):
    """
    Theme invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ThemeMimeInvalidError(BadRequestError):
    """
    You cannot create this theme, the mime-type is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ThemeTitleInvalidError(BadRequestError):
    """
    The specified theme title is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TimeoutError(ServerError):
    """
    A timeout occurred while fetching data from the worker
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TitleInvalidError(BadRequestError):
    """
    The specified stickerpack title is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TmpPasswordDisabledError(BadRequestError):
    """
    The temporary password is disabled
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TmpPasswordInvalidError(BadRequestError):
    """
    Password auth needs to be regenerated
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TokenInvalidError(BadRequestError):
    """
    The provided token is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TopicDeletedError(BadRequestError):
    """
    The topic was deleted
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class ToLangInvalidError(BadRequestError):
    """
    The specified destination language is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TtlDaysInvalidError(BadRequestError):
    """
    The provided TTL is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TtlMediaInvalidError(BadRequestError):
    """
    The provided media cannot be used with a TTL
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TtlPeriodInvalidError(BadRequestError):
    """
    The provided TTL Period is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TypesEmptyError(BadRequestError):
    """
    The types field is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TypeConstructorInvalidError(BadRequestError):
    """
    The type constructor is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TimedoutError(TimedOutError):
    """
    Timeout while fetching data
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class TimeoutError(TimedOutError):
    """
    Timeout while fetching data
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UnknownErrorError(BadRequestError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UnknownMethodError(ServerError):
    """
    The method you tried to call cannot be called on non-CDN DCs
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UntilDateInvalidError(BadRequestError):
    """
    That date cannot be specified in this request (try using None)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UpdateAppToLoginError(AuthKeyError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UrlInvalidError(BadRequestError):
    """
    The URL used was invalid (e.g. when answering a callback with a URL that's not t.me/yourbot or your game's URL)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UsageLimitInvalidError(BadRequestError):
    """
    The specified usage limit is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UsernameInvalidError(BadRequestError):
    """
    Nobody is using this username, or the username is unacceptable. If the latter, it must match r"[a-zA-Z][\\w\\d]{3,30}[a-zA-Z\\d]
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UsernameNotModifiedError(BadRequestError):
    """
    The username is not different from the current username
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UsernameNotOccupiedError(BadRequestError):
    """
    The username is not in use by anyone else yet
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UsernameOccupiedError(BadRequestError):
    """
    The username is already taken
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UsernamePurchaseAvailableError(BadRequestError):
    """
    
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserpicPrivacyRequiredError(AuthKeyError):
    """
    You need to disable privacy settings for your profile picture in order to make your geolocation public
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserpicUploadRequiredError(BadRequestError):
    """
    You must have a profile picture before using this method
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UsersTooFewError(BadRequestError):
    """
    Not enough users (to create a chat, for example)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UsersTooMuchError(BadRequestError):
    """
    The maximum number of users has been exceeded (to create a chat, for example)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserAdminInvalidError(BadRequestError):
    """
    Either you're not an admin or you tried to ban an admin that you didn't promote
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserAlreadyInvitedError(BadRequestError):
    """
    You have already invited this user
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserAlreadyParticipantError(BadRequestError):
    """
    The authenticated user is already a participant of the chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserBannedInChannelError(BadRequestError):
    """
    You're banned from sending messages in supergroups/channels
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserBlockedError(BadRequestError):
    """
    User blocked
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserBotError(BadRequestError):
    """
    Bots can only be admins in channels.
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserBotInvalidError(BadRequestError):
    """
    This method can only be called by a bot
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserBotRequiredError(BadRequestError):
    """
    This method can only be called by a bot
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserChannelsTooMuchError(BadRequestError):
    """
    One of the users you tried to add is already in too many channels/supergroups
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserCreatorError(BadRequestError):
    """
    You can't leave this channel, because you're its creator
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserDeactivatedError(UnauthorizedError):
    """
    The user has been deleted/deactivated
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserDeactivatedBanError(UnauthorizedError):
    """
    The user has been deleted/deactivated
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserDeletedError(ForbiddenError):
    """
    You can't send this secret message because the other participant deleted their account
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserIdInvalidError(BadRequestError):
    """
    Invalid object ID for a user. Make sure to pass the right types, for instance making sure that the request is designed for users or otherwise look for a different one more suited
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserInvalidError(BadRequestError):
    """
    The given user was invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserIsBlockedError(BadRequestError):
    """
    User is blocked
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserIsBotError(BadRequestError):
    """
    Bots can't send messages to other bots
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserKickedError(BadRequestError):
    """
    This user was kicked from this supergroup/channel
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserMigrateError(InvalidDCError):
    """
    The user whose identity is being used to execute queries is associated with DC {new_dc}
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserNotMutualContactError(BadRequestError):
    """
    The provided user is not a mutual contact
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserNotParticipantError(BadRequestError):
    """
    The target user is not a member of the specified megagroup or channel
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserPrivacyRestrictedError(ForbiddenError):
    """
    The user's privacy settings do not allow you to do this
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserRestrictedError(ForbiddenError):
    """
    You're spamreported, you can't create channels or chats.
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class UserVolumeInvalidError(BadRequestError):
    """
    The specified user volume is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class VideoContentTypeInvalidError(BadRequestError):
    """
    The video content type is not supported with the given parameters (i.e. supports_streaming)
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class VideoFileInvalidError(BadRequestError):
    """
    The given video cannot be used
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class VideoTitleEmptyError(BadRequestError):
    """
    The specified video title is empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class VoiceMessagesForbiddenError(BadRequestError):
    """
    This user's privacy settings forbid you from sending voice messages
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WallpaperFileInvalidError(BadRequestError):
    """
    The given file cannot be used as a wallpaper
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WallpaperInvalidError(BadRequestError):
    """
    The input wallpaper was not valid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WallpaperMimeInvalidError(BadRequestError):
    """
    The specified wallpaper MIME type is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WcConvertUrlInvalidError(BadRequestError):
    """
    WC convert URL invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WebdocumentInvalidError(BadRequestError):
    """
    Invalid webdocument URL provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WebdocumentMimeInvalidError(BadRequestError):
    """
    Invalid webdocument mime type provided
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WebdocumentSizeTooBigError(BadRequestError):
    """
    Webdocument is too big!
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WebdocumentUrlInvalidError(BadRequestError):
    """
    The given URL cannot be used
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WebpageCurlFailedError(BadRequestError):
    """
    Failure while fetching the webpage with cURL
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WebpageMediaEmptyError(BadRequestError):
    """
    Webpage media empty
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WebpushAuthInvalidError(BadRequestError):
    """
    The specified web push authentication secret is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WebpushKeyInvalidError(BadRequestError):
    """
    The specified web push elliptic curve Diffie-Hellman public key is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WebpushTokenInvalidError(BadRequestError):
    """
    The specified web push token is invalid
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class WorkerBusyTooLongRetryError(ServerError):
    """
    Telegram workers are too busy to respond immediately
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class YouBlockedUserError(BadRequestError):
    """
    You blocked this user
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FrozenMethodInvalidError(FloodError):
    """
    You tried to use a method that is not available for frozen accounts
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

class FrozenParticipantMissingError(BadRequestError):
    """
    Your account is frozen and can't access the chat
    """
    def __new__(cls, name: String, value: int | None = None, caused_by: int | None = None): ...

