use super::macros::{
    createAuthKeyError, createBadRequestError, createFloodError, createForbiddenError,
    createInvalidDCError, createServerError, createUnauthorizedError,
};
use super::*;
use pyo3::PyClassInitializer;
use pyo3::prelude::*;

// ========== InvalidDCError ==========

createInvalidDCError!(
    PyUserMigrateError,
    "UserMigrateError",
    "The user whose identity is being used to execute queries is associated with DC {}"
);
createInvalidDCError!(
    PyFileMigrateError,
    "FileMigrateError",
    "The file to be accessed is currently stored in DC {}"
);
createInvalidDCError!(
    PyNetworkMigrateError,
    "NetworkMigrateError",
    "The source IP address is associated with DC {}"
);
createInvalidDCError!(
    PyPhoneMigrateError,
    "PhoneMigrateError",
    "The phone number a user is trying to use for authorization is associated with DC {}"
);
createInvalidDCError!(
    PyStatsMigrateError,
    "StatsMigrateError",
    "The channel statistics must be fetched from DC {}"
);

// ========== BadRequestError ==========

createBadRequestError!(
    PyAboutTooLongError,
    "AboutTooLongError",
    "The provided bio is too long"
);
createBadRequestError!(
    PyAccessTokenExpiredError,
    "AccessTokenExpiredError",
    "Bot token expired"
);
createBadRequestError!(
    PyAccessTokenInvalidError,
    "AccessTokenInvalidError",
    "The provided token is not valid"
);
createBadRequestError!(
    PyAdminsTooMuchError,
    "AdminsTooMuchError",
    "Too many admins"
);
createBadRequestError!(
    PyAdminIdInvalidError,
    "AdminIdInvalidError",
    "The specified admin ID is invalid"
);
createBadRequestError!(
    PyAdminRankEmojiNotAllowedError,
    "AdminRankEmojiNotAllowedError",
    "Emoji are not allowed in admin titles or ranks"
);
createBadRequestError!(
    PyAdminRankInvalidError,
    "AdminRankInvalidError",
    "The given admin title or rank was invalid (possibly larger than 16 characters)"
);
createBadRequestError!(
    PyAlbumPhotosTooManyError,
    "AlbumPhotosTooManyError",
    "Too many photos were included in the album"
);
createBadRequestError!(
    PyApiIdInvalidError,
    "ApiIdInvalidError",
    "The api_id/api_hash combination is invalid"
);
createBadRequestError!(
    PyApiIdPublishedFloodError,
    "ApiIdPublishedFloodError",
    "This API id was published somewhere, you can't use it now"
);
createBadRequestError!(
    PyArticleTitleEmptyError,
    "ArticleTitleEmptyError",
    "The title of the article is empty"
);
createBadRequestError!(
    PyAudioContentUrlEmptyError,
    "AudioContentUrlEmptyError",
    "The remote URL specified in the content field is empty"
);
createBadRequestError!(
    PyAudioTitleEmptyError,
    "AudioTitleEmptyError",
    "The title attribute of the audio must be non-empty"
);
createBadRequestError!(
    PyAuthBytesInvalidError,
    "AuthBytesInvalidError",
    "The provided authorization is invalid"
);
createBadRequestError!(
    PyAuthTokenAlreadyAcceptedError,
    "AuthTokenAlreadyAcceptedError",
    "The authorization token was already used"
);
createBadRequestError!(
    PyAuthTokenExceptionError,
    "AuthTokenExceptionError",
    "An error occurred while importing the auth token"
);
createBadRequestError!(
    PyAuthTokenExpiredError,
    "AuthTokenExpiredError",
    "The provided authorization token has expired and the updated QR-code must be re-scanned"
);
createBadRequestError!(
    PyAuthTokenInvalidError,
    "AuthTokenInvalidError",
    "An invalid authorization token was provided"
);
createBadRequestError!(
    PyAuthTokenInvalid2Error,
    "AuthTokenInvalid2Error",
    "An invalid authorization token was provided"
);
createBadRequestError!(
    PyAuthTokenInvalidxError,
    "AuthTokenInvalidxError",
    "The specified auth token is invalid"
);
createBadRequestError!(
    PyAutoarchiveNotAvailableError,
    "AutoarchiveNotAvailableError",
    "You cannot use this feature yet"
);
createBadRequestError!(
    PyBankCardNumberInvalidError,
    "BankCardNumberInvalidError",
    "Incorrect credit card number"
);
createBadRequestError!(
    PyBannedRightsInvalidError,
    "BannedRightsInvalidError",
    "You cannot use that set of permissions in this request, i.e. restricting view_messages as a default"
);
createBadRequestError!(
    PyBasePortLocInvalidError,
    "BasePortLocInvalidError",
    "Base port location invalid"
);
createBadRequestError!(
    PyBotsTooMuchError,
    "BotsTooMuchError",
    "There are too many bots in this chat/channel"
);
createBadRequestError!(
    PyBotChannelsNaError,
    "BotChannelsNaError",
    "Bots can't edit admin privileges"
);
createBadRequestError!(
    PyBotCommandDescriptionInvalidError,
    "BotCommandDescriptionInvalidError",
    "The command description was empty, too long or had invalid characters used"
);
createBadRequestError!(
    PyBotCommandInvalidError,
    "BotCommandInvalidError",
    "The specified command is invalid"
);
createBadRequestError!(
    PyBotDomainInvalidError,
    "BotDomainInvalidError",
    "The domain used for the auth button does not match the one configured in @BotFather"
);
createBadRequestError!(
    PyBotGamesDisabledError,
    "BotGamesDisabledError",
    "Bot games cannot be used in this type of chat"
);
createBadRequestError!(
    PyBotGroupsBlockedError,
    "BotGroupsBlockedError",
    "This bot can't be added to groups"
);
createBadRequestError!(
    PyBotInlineDisabledError,
    "BotInlineDisabledError",
    "This bot can't be used in inline mode"
);
createBadRequestError!(
    PyBotInvalidError,
    "BotInvalidError",
    "This is not a valid bot"
);
createBadRequestError!(
    PyBotMethodInvalidError,
    "BotMethodInvalidError",
    "The API access for bot users is restricted. The method you tried to invoke cannot be executed as a bot"
);
createBadRequestError!(
    PyBotMissingError,
    "BotMissingError",
    "This method can only be run by a bot"
);
createBadRequestError!(
    PyBotOnesideNotAvailError,
    "BotOnesideNotAvailError",
    "Bots can't pin messages in PM just for themselves"
);
createBadRequestError!(
    PyBotPaymentsDisabledError,
    "BotPaymentsDisabledError",
    "This method can only be run by a bot"
);
createBadRequestError!(
    PyBotPollsDisabledError,
    "BotPollsDisabledError",
    "You cannot create polls under a bot account"
);
createBadRequestError!(
    PyBotResponseTimeoutError,
    "BotResponseTimeoutError",
    "The bot did not answer to the callback query in time"
);
createBadRequestError!(
    PyBotScoreNotModifiedError,
    "BotScoreNotModifiedError",
    "The score wasn't modified"
);
createBadRequestError!(
    PyBroadcastCallsDisabledError,
    "BroadcastCallsDisabledError",
    ""
);
createBadRequestError!(
    PyBroadcastIdInvalidError,
    "BroadcastIdInvalidError",
    "The channel is invalid"
);
createBadRequestError!(
    PyBroadcastPublicVotersForbiddenError,
    "BroadcastPublicVotersForbiddenError",
    "You cannot broadcast polls where the voters are public"
);
createBadRequestError!(
    PyBroadcastRequiredError,
    "BroadcastRequiredError",
    "The request can only be used with a broadcast channel"
);
createBadRequestError!(
    PyButtonDataInvalidError,
    "ButtonDataInvalidError",
    "The provided button data is invalid"
);
createBadRequestError!(
    PyButtonTextInvalidError,
    "ButtonTextInvalidError",
    "The specified button text is invalid"
);
createBadRequestError!(
    PyButtonTypeInvalidError,
    "ButtonTypeInvalidError",
    "The type of one of the buttons you provided is invalid"
);
createBadRequestError!(
    PyButtonUrlInvalidError,
    "ButtonUrlInvalidError",
    "Button URL invalid"
);
createBadRequestError!(
    PyButtonUserPrivacyRestrictedError,
    "ButtonUserPrivacyRestrictedError",
    "The privacy setting of the user specified in a [inputKeyboardButtonUserProfile](/constructor/inputKeyboardButtonUserProfile) button do not allow creating such a button"
);
createBadRequestError!(
    PyCallAlreadyAcceptedError,
    "CallAlreadyAcceptedError",
    "The call was already accepted"
);
createBadRequestError!(
    PyCallAlreadyDeclinedError,
    "CallAlreadyDeclinedError",
    "The call was already declined"
);
createBadRequestError!(
    PyCallPeerInvalidError,
    "CallPeerInvalidError",
    "The provided call peer object is invalid"
);
createBadRequestError!(
    PyCallProtocolFlagsInvalidError,
    "CallProtocolFlagsInvalidError",
    "Call protocol flags invalid"
);
createBadRequestError!(
    PyCdnMethodInvalidError,
    "CdnMethodInvalidError",
    "This method cannot be invoked on a CDN server. Refer to https://core.telegram.org/cdn#schema for available methods"
);
createBadRequestError!(
    PyChannelsAdminLocatedTooMuchError,
    "ChannelsAdminLocatedTooMuchError",
    "The user has reached the limit of public geogroups"
);
createBadRequestError!(
    PyChannelsAdminPublicTooMuchError,
    "ChannelsAdminPublicTooMuchError",
    "You're admin of too many public channels, make some channels private to change the username of this channel"
);
createBadRequestError!(
    PyChannelsTooMuchError,
    "ChannelsTooMuchError",
    "You have joined too many channels/supergroups"
);
createBadRequestError!(
    PyChannelBannedError,
    "ChannelBannedError",
    "The channel is banned"
);
createBadRequestError!(PyChannelForumMissingError, "ChannelForumMissingError", "");
createBadRequestError!(
    PyChannelIdInvalidError,
    "ChannelIdInvalidError",
    "The specified supergroup ID is invalid"
);
createBadRequestError!(
    PyChannelInvalidError,
    "ChannelInvalidError",
    "Invalid channel object. Make sure to pass the right types, for instance making sure that the request is designed for channels or otherwise look for a different one more suited"
);
createBadRequestError!(
    PyChannelParicipantMissingError,
    "ChannelParicipantMissingError",
    "The current user is not in the channel"
);
createBadRequestError!(
    PyChannelPrivateError,
    "ChannelPrivateError",
    "The channel specified is private and you lack permission to access it. Another reason may be that you were banned from it"
);
createBadRequestError!(PyChannelTooBigError, "ChannelTooBigError", "");
createBadRequestError!(
    PyChannelTooLargeError,
    "ChannelTooLargeError",
    "Channel is too large to be deleted; this error is issued when trying to delete channels with more than 1000 members (subject to change)"
);
createBadRequestError!(
    PyChatAboutNotModifiedError,
    "ChatAboutNotModifiedError",
    "About text has not changed"
);
createBadRequestError!(
    PyChatAboutTooLongError,
    "ChatAboutTooLongError",
    "Chat about too long"
);
createBadRequestError!(
    PyChatAdminRequiredError,
    "ChatAdminRequiredError",
    "Chat admin privileges are required to do that in the specified chat (for example, to send a message in a channel which is not yours), or invalid permissions used for the channel or group"
);
createBadRequestError!(
    PyChatDiscussionUnallowedError,
    "ChatDiscussionUnallowedError",
    ""
);
createBadRequestError!(
    PyChatForwardsRestrictedError,
    "ChatForwardsRestrictedError",
    "You can't forward messages from a protected chat"
);
createBadRequestError!(
    PyChatIdEmptyError,
    "ChatIdEmptyError",
    "The provided chat ID is empty"
);
createBadRequestError!(
    PyChatIdInvalidError,
    "ChatIdInvalidError",
    "Invalid object ID for a chat. Make sure to pass the right types, for instance making sure that the request is designed for chats (not channels/megagroups) or otherwise look for a different one more suited\nAn example working with a megagroup and AddChatUserRequest, it will fail because megagroups are channels. Use InviteToChannelRequest instead"
);
createBadRequestError!(
    PyChatInvalidError,
    "ChatInvalidError",
    "The chat is invalid for this request"
);
createBadRequestError!(
    PyChatInvitePermanentError,
    "ChatInvitePermanentError",
    "You can't set an expiration date on permanent invite links"
);
createBadRequestError!(
    PyChatLinkExistsError,
    "ChatLinkExistsError",
    "The chat is linked to a channel and cannot be used in that request"
);
createBadRequestError!(
    PyChatNotModifiedError,
    "ChatNotModifiedError",
    "The chat or channel wasn't modified (title, invites, username, admins, etc. are the same)"
);
createBadRequestError!(
    PyChatRestrictedError,
    "ChatRestrictedError",
    "The chat is restricted and cannot be used in that request"
);
createBadRequestError!(
    PyChatRevokeDateUnsupportedError,
    "ChatRevokeDateUnsupportedError",
    "`min_date` and `max_date` are not available for using with non-user peers"
);
createBadRequestError!(
    PyChatSendInlineForbiddenError,
    "ChatSendInlineForbiddenError",
    "You cannot send inline results in this chat"
);
createBadRequestError!(
    PyChatTitleEmptyError,
    "ChatTitleEmptyError",
    "No chat title provided"
);
createBadRequestError!(
    PyChatTooBigError,
    "ChatTooBigError",
    "This method is not available for groups with more than `chat_read_mark_size_threshold` members, [see client configuration](https://core.telegram.org/api/config#client-configuration)"
);
createBadRequestError!(
    PyCodeEmptyError,
    "CodeEmptyError",
    "The provided code is empty"
);
createBadRequestError!(
    PyCodeHashInvalidError,
    "CodeHashInvalidError",
    "Code hash invalid"
);
createBadRequestError!(
    PyCodeInvalidError,
    "CodeInvalidError",
    "Code invalid (i.e. from email)"
);
createBadRequestError!(
    PyConnectionApiIdInvalidError,
    "ConnectionApiIdInvalidError",
    "The provided API id is invalid"
);
createBadRequestError!(
    PyConnectionAppVersionEmptyError,
    "ConnectionAppVersionEmptyError",
    "App version is empty"
);
createBadRequestError!(
    PyConnectionDeviceModelEmptyError,
    "ConnectionDeviceModelEmptyError",
    "Device model empty"
);
createBadRequestError!(
    PyConnectionLangPackInvalidError,
    "ConnectionLangPackInvalidError",
    "The specified language pack is not valid. This is meant to be used by official applications only so far, leave it empty"
);
createBadRequestError!(
    PyConnectionLayerInvalidError,
    "ConnectionLayerInvalidError",
    "The very first request must always be InvokeWithLayerRequest"
);
createBadRequestError!(
    PyConnectionNotInitedError,
    "ConnectionNotInitedError",
    "Connection not initialized"
);
createBadRequestError!(
    PyConnectionSystemEmptyError,
    "ConnectionSystemEmptyError",
    "Connection system empty"
);
createBadRequestError!(
    PyConnectionSystemLangCodeEmptyError,
    "ConnectionSystemLangCodeEmptyError",
    "The system language string was empty during connection"
);
createBadRequestError!(
    PyContactAddMissingError,
    "ContactAddMissingError",
    "Contact to add is missing"
);
createBadRequestError!(
    PyContactIdInvalidError,
    "ContactIdInvalidError",
    "The provided contact ID is invalid"
);
createBadRequestError!(
    PyContactNameEmptyError,
    "ContactNameEmptyError",
    "The provided contact name cannot be empty"
);
createBadRequestError!(
    PyContactReqMissingError,
    "ContactReqMissingError",
    "Missing contact request"
);
createBadRequestError!(
    PyCreateCallFailedError,
    "CreateCallFailedError",
    "An error occurred while creating the call"
);
createBadRequestError!(
    PyCurrencyTotalAmountInvalidError,
    "CurrencyTotalAmountInvalidError",
    "The total amount of all prices is invalid"
);
createBadRequestError!(
    PyDataInvalidError,
    "DataInvalidError",
    "Encrypted data invalid"
);
createBadRequestError!(
    PyDataJsonInvalidError,
    "DataJsonInvalidError",
    "The provided JSON data is invalid"
);
createBadRequestError!(PyDataTooLongError, "DataTooLongError", "Data too long");
createBadRequestError!(PyDateEmptyError, "DateEmptyError", "Date empty");
createBadRequestError!(
    PyDcIdInvalidError,
    "DcIdInvalidError",
    "This occurs when an authorization is tried to be exported for the same data center one is currently connected to"
);
createBadRequestError!(PyDhGAInvalidError, "DhGAInvalidError", "g_a invalid");
createBadRequestError!(
    PyDocumentInvalidError,
    "DocumentInvalidError",
    "The document file was invalid and can't be used in inline mode"
);
createBadRequestError!(
    PyEmailHashExpiredError,
    "EmailHashExpiredError",
    "The email hash expired and cannot be used to verify it"
);
createBadRequestError!(
    PyEmailInvalidError,
    "EmailInvalidError",
    "The given email is invalid"
);
createBadRequestError!(
    PyEmailUnconfirmedError,
    "EmailUnconfirmedError",
    "Email unconfirmed, the length of the code must be {}"
);
createBadRequestError!(
    PyEmailVerifyExpiredError,
    "EmailVerifyExpiredError",
    "The verification email has expired"
);
createBadRequestError!(
    PyEmojiInvalidError,
    "EmojiInvalidError",
    "The specified theme emoji is valid"
);
createBadRequestError!(
    PyEmojiNotModifiedError,
    "EmojiNotModifiedError",
    "The theme wasn't changed"
);
createBadRequestError!(
    PyEmoticonEmptyError,
    "EmoticonEmptyError",
    "The emoticon field cannot be empty"
);
createBadRequestError!(
    PyEmoticonInvalidError,
    "EmoticonInvalidError",
    "The specified emoticon cannot be used or was not a emoticon"
);
createBadRequestError!(
    PyEmoticonStickerpackMissingError,
    "EmoticonStickerpackMissingError",
    "The emoticon sticker pack you are trying to get is missing"
);
createBadRequestError!(
    PyEncryptedMessageInvalidError,
    "EncryptedMessageInvalidError",
    "Encrypted message invalid"
);
createBadRequestError!(
    PyEncryptionAlreadyAcceptedError,
    "EncryptionAlreadyAcceptedError",
    "Secret chat already accepted"
);
createBadRequestError!(
    PyEncryptionAlreadyDeclinedError,
    "EncryptionAlreadyDeclinedError",
    "The secret chat was already declined"
);
createBadRequestError!(
    PyEncryptionDeclinedError,
    "EncryptionDeclinedError",
    "The secret chat was declined"
);
createBadRequestError!(
    PyEncryptionIdInvalidError,
    "EncryptionIdInvalidError",
    "The provided secret chat ID is invalid"
);
createBadRequestError!(
    PyEntitiesTooLongError,
    "EntitiesTooLongError",
    "It is no longer possible to send such long data inside entity tags (for example inline text URLs)"
);
createBadRequestError!(
    PyEntityBoundsInvalidError,
    "EntityBoundsInvalidError",
    "Some of provided entities have invalid bounds (length is zero or out of the boundaries of the string)"
);
createBadRequestError!(
    PyEntityMentionUserInvalidError,
    "EntityMentionUserInvalidError",
    "You can't use this entity"
);
createBadRequestError!(
    PyErrorTextEmptyError,
    "ErrorTextEmptyError",
    "The provided error message is empty"
);
createBadRequestError!(
    PyExpireDateInvalidError,
    "ExpireDateInvalidError",
    "The specified expiration date is invalid"
);
createBadRequestError!(PyExpireForbiddenError, "ExpireForbiddenError", "");
createBadRequestError!(
    PyExportCardInvalidError,
    "ExportCardInvalidError",
    "Provided card is invalid"
);
createBadRequestError!(
    PyExternalUrlInvalidError,
    "ExternalUrlInvalidError",
    "External URL invalid"
);
createBadRequestError!(
    PyFieldNameEmptyError,
    "FieldNameEmptyError",
    "The field with the name FIELD_NAME is missing"
);
createBadRequestError!(
    PyFieldNameInvalidError,
    "FieldNameInvalidError",
    "The field with the name FIELD_NAME is invalid"
);
createBadRequestError!(
    PyFileContentTypeInvalidError,
    "FileContentTypeInvalidError",
    "File content-type is invalid"
);
createBadRequestError!(
    PyFileEmtpyError,
    "FileEmtpyError",
    "An empty file was provided"
);
createBadRequestError!(
    PyFileIdInvalidError,
    "FileIdInvalidError",
    "The provided file id is invalid. Make sure all parameters are present, have the correct type and are not empty (ID, access hash, file reference, thumb size ...)"
);
createBadRequestError!(
    PyFilePartsInvalidError,
    "FilePartsInvalidError",
    "The number of file parts is invalid"
);
createBadRequestError!(
    PyFilePart0MissingError,
    "FilePart0MissingError",
    "File part 0 missing"
);
createBadRequestError!(
    PyFilePartEmptyError,
    "FilePartEmptyError",
    "The provided file part is empty"
);
createBadRequestError!(
    PyFilePartInvalidError,
    "FilePartInvalidError",
    "The file part number is invalid"
);
createBadRequestError!(
    PyFilePartLengthInvalidError,
    "FilePartLengthInvalidError",
    "The length of a file part is invalid"
);
createBadRequestError!(
    PyFilePartSizeChangedError,
    "FilePartSizeChangedError",
    "The file part size (chunk size) cannot change during upload"
);
createBadRequestError!(
    PyFilePartSizeInvalidError,
    "FilePartSizeInvalidError",
    "The provided file part size is invalid"
);
createBadRequestError!(
    PyFilePartTooBigError,
    "FilePartTooBigError",
    "The uploaded file part is too big"
);
createBadRequestError!(
    PyFilePartMissingError,
    "FilePartMissingError",
    "Part {} of the file is missing from storage"
);
createBadRequestError!(
    PyFileReferenceEmptyError,
    "FileReferenceEmptyError",
    "The file reference must exist to access the media and it cannot be empty"
);
createBadRequestError!(
    PyFileReferenceExpiredError,
    "FileReferenceExpiredError",
    "The file reference has expired and is no longer valid or it belongs to self-destructing media and cannot be resent"
);
createBadRequestError!(
    PyFileReferenceInvalidError,
    "FileReferenceInvalidError",
    "The file reference is invalid or you can't do that operation on such message"
);
createBadRequestError!(
    PyFileTitleEmptyError,
    "FileTitleEmptyError",
    "An empty file title was specified"
);
createBadRequestError!(
    PyFilterIdInvalidError,
    "FilterIdInvalidError",
    "The specified filter ID is invalid"
);
createBadRequestError!(
    PyFilterIncludeEmptyError,
    "FilterIncludeEmptyError",
    "The include_peers vector of the filter is empty"
);
createBadRequestError!(
    PyFilterNotSupportedError,
    "FilterNotSupportedError",
    "The specified filter cannot be used in this context"
);
createBadRequestError!(
    PyFilterTitleEmptyError,
    "FilterTitleEmptyError",
    "The title field of the filter is empty"
);
createBadRequestError!(
    PyFirstNameInvalidError,
    "FirstNameInvalidError",
    "The first name is invalid"
);
createBadRequestError!(
    PyFolderIdEmptyError,
    "FolderIdEmptyError",
    "The folder you tried to delete was already empty"
);
createBadRequestError!(
    PyFolderIdInvalidError,
    "FolderIdInvalidError",
    "The folder you tried to use was not valid"
);
createBadRequestError!(
    PyFreshChangeAdminsForbiddenError,
    "FreshChangeAdminsForbiddenError",
    "Recently logged-in users cannot add or change admins"
);
createBadRequestError!(
    PyFromMessageBotDisabledError,
    "FromMessageBotDisabledError",
    "Bots can't use fromMessage min constructors"
);
createBadRequestError!(
    PyFromPeerInvalidError,
    "FromPeerInvalidError",
    "The given from_user peer cannot be used for the parameter"
);
createBadRequestError!(
    PyGameBotInvalidError,
    "GameBotInvalidError",
    "You cannot send that game with the current bot"
);
createBadRequestError!(
    PyGeoPointInvalidError,
    "GeoPointInvalidError",
    "Invalid geoposition provided"
);
createBadRequestError!(
    PyGifContentTypeInvalidError,
    "GifContentTypeInvalidError",
    "GIF content-type invalid"
);
createBadRequestError!(
    PyGifIdInvalidError,
    "GifIdInvalidError",
    "The provided GIF ID is invalid"
);
createBadRequestError!(
    PyGraphExpiredReloadError,
    "GraphExpiredReloadError",
    "This graph has expired, please obtain a new graph token"
);
createBadRequestError!(
    PyGraphInvalidReloadError,
    "GraphInvalidReloadError",
    "Invalid graph token provided, please reload the stats and provide the updated token"
);
createBadRequestError!(
    PyGraphOutdatedReloadError,
    "GraphOutdatedReloadError",
    "Data can't be used for the channel statistics, graphs outdated"
);
createBadRequestError!(
    PyGroupcallAlreadyDiscardedError,
    "GroupcallAlreadyDiscardedError",
    "The group call was already discarded"
);
createBadRequestError!(
    PyGroupcallInvalidError,
    "GroupcallInvalidError",
    "The specified group call is invalid"
);
createBadRequestError!(
    PyGroupcallJoinMissingError,
    "GroupcallJoinMissingError",
    "You haven't joined this group call"
);
createBadRequestError!(
    PyGroupcallNotModifiedError,
    "GroupcallNotModifiedError",
    "Group call settings weren't modified"
);
createBadRequestError!(
    PyGroupcallSsrcDuplicateMuchError,
    "GroupcallSsrcDuplicateMuchError",
    "The app needs to retry joining the group call with a new SSRC value"
);
createBadRequestError!(
    PyGroupedMediaInvalidError,
    "GroupedMediaInvalidError",
    "Invalid grouped media"
);
createBadRequestError!(
    PyGroupCallInvalidError,
    "GroupCallInvalidError",
    "Group call invalid"
);
createBadRequestError!(
    PyHashInvalidError,
    "HashInvalidError",
    "The provided hash is invalid"
);
createBadRequestError!(
    PyHideRequesterMissingError,
    "HideRequesterMissingError",
    "The join request was missing or was already handled"
);
createBadRequestError!(
    PyImageProcessFailedError,
    "ImageProcessFailedError",
    "Failure while processing image"
);
createBadRequestError!(
    PyImportFileInvalidError,
    "ImportFileInvalidError",
    "The file is too large to be imported"
);
createBadRequestError!(
    PyImportFormatUnrecognizedError,
    "ImportFormatUnrecognizedError",
    "Unknown import format"
);
createBadRequestError!(
    PyImportIdInvalidError,
    "ImportIdInvalidError",
    "The specified import ID is invalid"
);
createBadRequestError!(
    PyInlineResultExpiredError,
    "InlineResultExpiredError",
    "The inline query expired"
);
createBadRequestError!(
    PyInputConstructorInvalidError,
    "InputConstructorInvalidError",
    "The provided constructor is invalid"
);
createBadRequestError!(
    PyInputFetchErrorError,
    "InputFetchErrorError",
    "An error occurred while deserializing TL parameters"
);
createBadRequestError!(
    PyInputFetchFailError,
    "InputFetchFailError",
    "Failed deserializing TL payload"
);
createBadRequestError!(
    PyInputFilterInvalidError,
    "InputFilterInvalidError",
    "The search query filter is invalid"
);
createBadRequestError!(
    PyInputLayerInvalidError,
    "InputLayerInvalidError",
    "The provided layer is invalid"
);
createBadRequestError!(
    PyInputMethodInvalidError,
    "InputMethodInvalidError",
    "The invoked method does not exist anymore or has never existed"
);
createBadRequestError!(
    PyInputRequestTooLongError,
    "InputRequestTooLongError",
    "The input request was too long. This may be a bug in the library as it can occur when serializing more bytes than it should (like appending the vector constructor code at the end of a message)"
);
createBadRequestError!(
    PyInputTextEmptyError,
    "InputTextEmptyError",
    "The specified text is empty"
);
createBadRequestError!(
    PyInputUserDeactivatedError,
    "InputUserDeactivatedError",
    "The specified user was deleted"
);
createBadRequestError!(
    PyInviteForbiddenWithJoinasError,
    "InviteForbiddenWithJoinasError",
    "If the user has anonymously joined a group call as a channel, they can't invite other users to the group call because that would cause deanonymization, because the invite would be sent using the original user ID, not the anonymized channel ID"
);
createBadRequestError!(
    PyInviteHashEmptyError,
    "InviteHashEmptyError",
    "The invite hash is empty"
);
createBadRequestError!(
    PyInviteHashExpiredError,
    "InviteHashExpiredError",
    "The chat the user tried to join has expired and is not valid anymore"
);
createBadRequestError!(
    PyInviteHashInvalidError,
    "InviteHashInvalidError",
    "The invite hash is invalid"
);
createBadRequestError!(
    PyInviteRequestSentError,
    "InviteRequestSentError",
    "You have successfully requested to join this chat or channel"
);
createBadRequestError!(
    PyInviteRevokedMissingError,
    "InviteRevokedMissingError",
    "The specified invite link was already revoked or is invalid"
);
createBadRequestError!(
    PyInvoicePayloadInvalidError,
    "InvoicePayloadInvalidError",
    "The specified invoice payload is invalid"
);
createBadRequestError!(
    PyJoinAsPeerInvalidError,
    "JoinAsPeerInvalidError",
    "The specified peer cannot be used to join a group call"
);
createBadRequestError!(
    PyLangCodeInvalidError,
    "LangCodeInvalidError",
    "The specified language code is invalid"
);
createBadRequestError!(
    PyLangCodeNotSupportedError,
    "LangCodeNotSupportedError",
    "The specified language code is not supported"
);
createBadRequestError!(
    PyLangPackInvalidError,
    "LangPackInvalidError",
    "The provided language pack is invalid"
);
createBadRequestError!(
    PyLastnameInvalidError,
    "LastnameInvalidError",
    "The last name is invalid"
);
createBadRequestError!(
    PyLimitInvalidError,
    "LimitInvalidError",
    "An invalid limit was provided. See https://core.telegram.org/api/files#downloading-files"
);
createBadRequestError!(
    PyLinkNotModifiedError,
    "LinkNotModifiedError",
    "The channel is already linked to this group"
);
createBadRequestError!(
    PyLocationInvalidError,
    "LocationInvalidError",
    "The location given for a file was invalid. See https://core.telegram.org/api/files#downloading-files"
);
createBadRequestError!(
    PyMaxDateInvalidError,
    "MaxDateInvalidError",
    "The specified maximum date is invalid"
);
createBadRequestError!(
    PyMaxIdInvalidError,
    "MaxIdInvalidError",
    "The provided max ID is invalid"
);
createBadRequestError!(
    PyMaxQtsInvalidError,
    "MaxQtsInvalidError",
    "The provided QTS were invalid"
);
createBadRequestError!(
    PyMd5ChecksumInvalidError,
    "Md5ChecksumInvalidError",
    "The MD5 check-sums do not match"
);
createBadRequestError!(
    PyMediaCaptionTooLongError,
    "MediaCaptionTooLongError",
    "The caption is too long"
);
createBadRequestError!(
    PyMediaEmptyError,
    "MediaEmptyError",
    "The provided media object is invalid or the current account may not be able to send it (such as games as users)"
);
createBadRequestError!(
    PyMediaGroupedInvalidError,
    "MediaGroupedInvalidError",
    "You tried to send media of different types in an album"
);
createBadRequestError!(PyMediaInvalidError, "MediaInvalidError", "Media invalid");
createBadRequestError!(
    PyMediaNewInvalidError,
    "MediaNewInvalidError",
    "The new media to edit the message with is invalid (such as stickers or voice notes)"
);
createBadRequestError!(
    PyMediaPrevInvalidError,
    "MediaPrevInvalidError",
    "The old media cannot be edited with anything else (such as stickers or voice notes)"
);
createBadRequestError!(PyMediaTtlInvalidError, "MediaTtlInvalidError", "");
createBadRequestError!(
    PyMegagroupIdInvalidError,
    "MegagroupIdInvalidError",
    "The group is invalid"
);
createBadRequestError!(
    PyMegagroupPrehistoryHiddenError,
    "MegagroupPrehistoryHiddenError",
    "You can't set this discussion group because it's history is hidden"
);
createBadRequestError!(
    PyMegagroupRequiredError,
    "MegagroupRequiredError",
    "The request can only be used with a megagroup channel"
);
createBadRequestError!(
    PyMessageEditTimeExpiredError,
    "MessageEditTimeExpiredError",
    "You can't edit this message anymore, too much time has passed since its creation."
);
createBadRequestError!(
    PyMessageEmptyError,
    "MessageEmptyError",
    "Empty or invalid UTF-8 message was sent"
);
createBadRequestError!(
    PyMessageIdsEmptyError,
    "MessageIdsEmptyError",
    "No message ids were provided"
);
createBadRequestError!(
    PyMessageIdInvalidError,
    "MessageIdInvalidError",
    "The specified message ID is invalid or you can't do that operation on such message"
);
createBadRequestError!(
    PyMessageNotModifiedError,
    "MessageNotModifiedError",
    "Content of the message was not modified"
);
createBadRequestError!(
    PyMessagePollClosedError,
    "MessagePollClosedError",
    "The poll was closed and can no longer be voted on"
);
createBadRequestError!(
    PyMessageTooLongError,
    "MessageTooLongError",
    "Message was too long"
);
createBadRequestError!(
    PyMethodInvalidError,
    "MethodInvalidError",
    "The API method is invalid and cannot be used"
);
createBadRequestError!(
    PyMinDateInvalidError,
    "MinDateInvalidError",
    "The specified minimum date is invalid"
);
createBadRequestError!(
    PyMsgIdInvalidError,
    "MsgIdInvalidError",
    "The message ID used in the peer was invalid"
);
createBadRequestError!(
    PyMsgTooOldError,
    "MsgTooOldError",
    "[`chat_read_mark_expire_period` seconds](https://core.telegram.org/api/config#chat-read-mark-expire-period) have passed since the message was sent, read receipts were deleted"
);
createBadRequestError!(
    PyMsgWaitFailedError,
    "MsgWaitFailedError",
    "A waiting call returned an error"
);
createBadRequestError!(
    PyMultiMediaTooLongError,
    "MultiMediaTooLongError",
    "Too many media files were included in the same album"
);
createBadRequestError!(
    PyNewSaltInvalidError,
    "NewSaltInvalidError",
    "The new salt is invalid"
);
createBadRequestError!(
    PyNewSettingsEmptyError,
    "NewSettingsEmptyError",
    "No password is set on the current account, and no new password was specified in `new_settings`"
);
createBadRequestError!(
    PyNewSettingsInvalidError,
    "NewSettingsInvalidError",
    "The new settings are invalid"
);
createBadRequestError!(
    PyNextOffsetInvalidError,
    "NextOffsetInvalidError",
    "The value for next_offset is invalid. Check that it has normal characters and is not too long"
);
createBadRequestError!(
    PyOffsetInvalidError,
    "OffsetInvalidError",
    "The given offset was invalid, it must be divisible by 1KB. See https://core.telegram.org/api/files#downloading-files"
);
createBadRequestError!(
    PyOffsetPeerIdInvalidError,
    "OffsetPeerIdInvalidError",
    "The provided offset peer is invalid"
);
createBadRequestError!(
    PyOptionsTooMuchError,
    "OptionsTooMuchError",
    "You defined too many options for the poll"
);
createBadRequestError!(
    PyOptionInvalidError,
    "OptionInvalidError",
    "The option specified is invalid and does not exist in the target poll"
);
createBadRequestError!(
    PyPackShortNameInvalidError,
    "PackShortNameInvalidError",
    "Invalid sticker pack name. It must begin with a letter, can't contain consecutive underscores and must end in \"_by_<bot username>"
);
createBadRequestError!(
    PyPackShortNameOccupiedError,
    "PackShortNameOccupiedError",
    "A stickerpack with this name already exists"
);
createBadRequestError!(
    PyPackTitleInvalidError,
    "PackTitleInvalidError",
    "The stickerpack title is invalid"
);
createBadRequestError!(
    PyParticipantsTooFewError,
    "ParticipantsTooFewError",
    "Not enough participants"
);
createBadRequestError!(
    PyParticipantIdInvalidError,
    "ParticipantIdInvalidError",
    "The specified participant ID is invalid"
);
createBadRequestError!(
    PyParticipantJoinMissingError,
    "ParticipantJoinMissingError",
    "Trying to enable a presentation, when the user hasn't joined the Video Chat with [phone.joinGroupCall](https://core.telegram.org/method/phone.joinGroupCall)"
);
createBadRequestError!(
    PyParticipantVersionOutdatedError,
    "ParticipantVersionOutdatedError",
    "The other participant does not use an up to date telegram client with support for calls"
);
createBadRequestError!(
    PyPasswordEmptyError,
    "PasswordEmptyError",
    "The provided password is empty"
);
createBadRequestError!(
    PyPasswordHashInvalidError,
    "PasswordHashInvalidError",
    "The password (and thus its hash value) you entered is invalid"
);
createBadRequestError!(
    PyPasswordMissingError,
    "PasswordMissingError",
    "The account must have 2-factor authentication enabled (a password) before this method can be used"
);
createBadRequestError!(
    PyPasswordRecoveryExpiredError,
    "PasswordRecoveryExpiredError",
    "The recovery code has expired"
);
createBadRequestError!(
    PyPasswordRecoveryNaError,
    "PasswordRecoveryNaError",
    "No email was set, can't recover password via email"
);
createBadRequestError!(
    PyPasswordRequiredError,
    "PasswordRequiredError",
    "The account must have 2-factor authentication enabled (a password) before this method can be used"
);
createBadRequestError!(
    PyPasswordTooFreshError,
    "PasswordTooFreshError",
    "The password was added too recently and {} seconds must pass before using the method"
);
createBadRequestError!(
    PyPaymentProviderInvalidError,
    "PaymentProviderInvalidError",
    "The payment provider was not recognised or its token was invalid"
);
createBadRequestError!(PyPeerFloodError, "PeerFloodError", "Too many requests");
createBadRequestError!(PyPeerHistoryEmptyError, "PeerHistoryEmptyError", "");
createBadRequestError!(
    PyPeerIdInvalidError,
    "PeerIdInvalidError",
    "An invalid Peer was used. Make sure to pass the right peer type and that the value is valid (for instance, bots cannot start conversations)"
);
createBadRequestError!(
    PyPeerIdNotSupportedError,
    "PeerIdNotSupportedError",
    "The provided peer ID is not supported"
);
createBadRequestError!(
    PyPersistentTimestampEmptyError,
    "PersistentTimestampEmptyError",
    "Persistent timestamp empty"
);
createBadRequestError!(
    PyPersistentTimestampInvalidError,
    "PersistentTimestampInvalidError",
    "Persistent timestamp invalid"
);
createBadRequestError!(
    PyPhoneCodeEmptyError,
    "PhoneCodeEmptyError",
    "The phone code is missing"
);
createBadRequestError!(
    PyPhoneCodeExpiredError,
    "PhoneCodeExpiredError",
    "The confirmation code has expired"
);
createBadRequestError!(
    PyPhoneCodeHashEmptyError,
    "PhoneCodeHashEmptyError",
    "The phone code hash is missing"
);
createBadRequestError!(
    PyPhoneCodeInvalidError,
    "PhoneCodeInvalidError",
    "The phone code entered was invalid"
);
createBadRequestError!(
    PyPhoneHashExpiredError,
    "PhoneHashExpiredError",
    "An invalid or expired `phone_code_hash` was provided"
);
createBadRequestError!(
    PyPhoneNotOccupiedError,
    "PhoneNotOccupiedError",
    "No user is associated to the specified phone number"
);
createBadRequestError!(
    PyPhoneNumberAppSignupForbiddenError,
    "PhoneNumberAppSignupForbiddenError",
    "You can't sign up using this app"
);
createBadRequestError!(
    PyPhoneNumberBannedError,
    "PhoneNumberBannedError",
    "The used phone number has been banned from Telegram and cannot be used anymore. Maybe check https://www.telegram.org/faq_spam"
);
createBadRequestError!(
    PyPhoneNumberFloodError,
    "PhoneNumberFloodError",
    "You asked for the code too many times."
);
createBadRequestError!(
    PyPhoneNumberInvalidError,
    "PhoneNumberInvalidError",
    "The phone number is invalid"
);
createBadRequestError!(
    PyPhoneNumberOccupiedError,
    "PhoneNumberOccupiedError",
    "The phone number is already in use"
);
createBadRequestError!(
    PyPhoneNumberUnoccupiedError,
    "PhoneNumberUnoccupiedError",
    "The phone number is not yet being used"
);
createBadRequestError!(
    PyPhonePasswordProtectedError,
    "PhonePasswordProtectedError",
    "This phone is password protected"
);
createBadRequestError!(
    PyPhotoContentTypeInvalidError,
    "PhotoContentTypeInvalidError",
    "Photo mime-type invalid"
);
createBadRequestError!(
    PyPhotoContentUrlEmptyError,
    "PhotoContentUrlEmptyError",
    "The content from the URL used as a photo appears to be empty or has caused another HTTP error"
);
createBadRequestError!(
    PyPhotoCropFileMissingError,
    "PhotoCropFileMissingError",
    "Photo crop file missing"
);
createBadRequestError!(
    PyPhotoCropSizeSmallError,
    "PhotoCropSizeSmallError",
    "Photo is too small"
);
createBadRequestError!(
    PyPhotoExtInvalidError,
    "PhotoExtInvalidError",
    "The extension of the photo is invalid"
);
createBadRequestError!(
    PyPhotoFileMissingError,
    "PhotoFileMissingError",
    "Profile photo file missing"
);
createBadRequestError!(
    PyPhotoIdInvalidError,
    "PhotoIdInvalidError",
    "Photo id is invalid"
);
createBadRequestError!(PyPhotoInvalidError, "PhotoInvalidError", "Photo invalid");
createBadRequestError!(
    PyPhotoInvalidDimensionsError,
    "PhotoInvalidDimensionsError",
    "The photo dimensions are invalid (hint: `pip install pillow` for `send_file` to resize images)"
);
createBadRequestError!(
    PyPhotoSaveFileInvalidError,
    "PhotoSaveFileInvalidError",
    "The photo you tried to send cannot be saved by Telegram. A reason may be that it exceeds 10MB. Try resizing it locally"
);
createBadRequestError!(
    PyPhotoThumbUrlEmptyError,
    "PhotoThumbUrlEmptyError",
    "The URL used as a thumbnail appears to be empty or has caused another HTTP error"
);
createBadRequestError!(
    PyPinnedDialogsTooMuchError,
    "PinnedDialogsTooMuchError",
    "Too many pinned dialogs"
);
createBadRequestError!(
    PyPinRestrictedError,
    "PinRestrictedError",
    "You can't pin messages in private chats with other people"
);
createBadRequestError!(
    PyPollAnswersInvalidError,
    "PollAnswersInvalidError",
    "The poll did not have enough answers or had too many"
);
createBadRequestError!(
    PyPollAnswerInvalidError,
    "PollAnswerInvalidError",
    "One of the poll answers is not acceptable"
);
createBadRequestError!(
    PyPollOptionDuplicateError,
    "PollOptionDuplicateError",
    "A duplicate option was sent in the same poll"
);
createBadRequestError!(
    PyPollOptionInvalidError,
    "PollOptionInvalidError",
    "A poll option used invalid data (the data may be too long)"
);
createBadRequestError!(
    PyPollQuestionInvalidError,
    "PollQuestionInvalidError",
    "The poll question was either empty or too long"
);
createBadRequestError!(
    PyPollUnsupportedError,
    "PollUnsupportedError",
    "This layer does not support polls in the issued method"
);
createBadRequestError!(
    PyPrivacyKeyInvalidError,
    "PrivacyKeyInvalidError",
    "The privacy key is invalid"
);
createBadRequestError!(
    PyPrivacyTooLongError,
    "PrivacyTooLongError",
    "Cannot add that many entities in a single request"
);
createBadRequestError!(
    PyPrivacyValueInvalidError,
    "PrivacyValueInvalidError",
    "The privacy value is invalid"
);
createBadRequestError!(
    PyPublicKeyRequiredError,
    "PublicKeyRequiredError",
    "A public key is required"
);
createBadRequestError!(
    PyQueryIdEmptyError,
    "QueryIdEmptyError",
    "The query ID is empty"
);
createBadRequestError!(
    PyQueryIdInvalidError,
    "QueryIdInvalidError",
    "The query ID is invalid"
);
createBadRequestError!(
    PyQueryTooShortError,
    "QueryTooShortError",
    "The query string is too short"
);
createBadRequestError!(
    PyQuizAnswerMissingError,
    "QuizAnswerMissingError",
    "You can forward a quiz while hiding the original author only after choosing an option in the quiz"
);
createBadRequestError!(
    PyQuizCorrectAnswersEmptyError,
    "QuizCorrectAnswersEmptyError",
    "A quiz must specify one correct answer"
);
createBadRequestError!(
    PyQuizCorrectAnswersTooMuchError,
    "QuizCorrectAnswersTooMuchError",
    "There can only be one correct answer"
);
createBadRequestError!(
    PyQuizCorrectAnswerInvalidError,
    "QuizCorrectAnswerInvalidError",
    "The correct answer is not an existing answer"
);
createBadRequestError!(
    PyQuizMultipleInvalidError,
    "QuizMultipleInvalidError",
    "A poll cannot be both multiple choice and quiz"
);
createBadRequestError!(
    PyRandomIdEmptyError,
    "RandomIdEmptyError",
    "Random ID empty"
);
createBadRequestError!(
    PyRandomIdInvalidError,
    "RandomIdInvalidError",
    "A provided random ID is invalid"
);
createBadRequestError!(
    PyRandomLengthInvalidError,
    "RandomLengthInvalidError",
    "Random length invalid"
);
createBadRequestError!(
    PyRangesInvalidError,
    "RangesInvalidError",
    "Invalid range provided"
);
createBadRequestError!(
    PyReactionsTooManyError,
    "ReactionsTooManyError",
    "The message already has exactly `reactions_uniq_max` reaction emojis, you can't react with a new emoji, see [the docs for more info](/api/config#client-configuration)"
);
createBadRequestError!(
    PyReactionEmptyError,
    "ReactionEmptyError",
    "No reaction provided"
);
createBadRequestError!(
    PyReactionInvalidError,
    "ReactionInvalidError",
    "Invalid reaction provided (only emoji are allowed)"
);
createBadRequestError!(
    PyReflectorNotAvailableError,
    "ReflectorNotAvailableError",
    "Invalid call reflector server"
);
createBadRequestError!(
    PyReplyMarkupBuyEmptyError,
    "ReplyMarkupBuyEmptyError",
    "Reply markup for buy button empty"
);
createBadRequestError!(
    PyReplyMarkupGameEmptyError,
    "ReplyMarkupGameEmptyError",
    "The provided reply markup for the game is empty"
);
createBadRequestError!(
    PyReplyMarkupInvalidError,
    "ReplyMarkupInvalidError",
    "The provided reply markup is invalid"
);
createBadRequestError!(
    PyReplyMarkupTooLongError,
    "ReplyMarkupTooLongError",
    "The data embedded in the reply markup buttons was too much"
);
createBadRequestError!(
    PyResetRequestMissingError,
    "ResetRequestMissingError",
    "No password reset is in progress"
);
createBadRequestError!(
    PyResultsTooMuchError,
    "ResultsTooMuchError",
    "You sent too many results, see https://core.telegram.org/bots/api#answerinlinequery for the current limit"
);
createBadRequestError!(
    PyResultIdDuplicateError,
    "ResultIdDuplicateError",
    "Duplicated IDs on the sent results. Make sure to use unique IDs"
);
createBadRequestError!(
    PyResultIdEmptyError,
    "ResultIdEmptyError",
    "Result ID empty"
);
createBadRequestError!(
    PyResultIdInvalidError,
    "ResultIdInvalidError",
    "The given result cannot be used to send the selection to the bot"
);
createBadRequestError!(
    PyResultTypeInvalidError,
    "ResultTypeInvalidError",
    "Result type invalid"
);
createBadRequestError!(
    PyRevoteNotAllowedError,
    "RevoteNotAllowedError",
    "You cannot change your vote"
);
createBadRequestError!(
    PyRightsNotModifiedError,
    "RightsNotModifiedError",
    "The new admin rights are equal to the old rights, no change was made"
);
createBadRequestError!(
    PyRsaDecryptFailedError,
    "RsaDecryptFailedError",
    "Internal RSA decryption failed"
);
createBadRequestError!(
    PyScheduleBotNotAllowedError,
    "ScheduleBotNotAllowedError",
    "Bots are not allowed to schedule messages"
);
createBadRequestError!(
    PyScheduleDateInvalidError,
    "ScheduleDateInvalidError",
    "Invalid schedule date provided"
);
createBadRequestError!(
    PyScheduleDateTooLateError,
    "ScheduleDateTooLateError",
    "The date you tried to schedule is too far in the future (last known limit of 1 year and a few hours)"
);
createBadRequestError!(
    PyScheduleStatusPrivateError,
    "ScheduleStatusPrivateError",
    "You cannot schedule a message until the person comes online if their privacy does not show this information"
);
createBadRequestError!(
    PyScheduleTooMuchError,
    "ScheduleTooMuchError",
    "You cannot schedule more messages in this chat (last known limit of 100 per chat)"
);
createBadRequestError!(
    PyScoreInvalidError,
    "ScoreInvalidError",
    "The specified game score is invalid"
);
createBadRequestError!(
    PySearchQueryEmptyError,
    "SearchQueryEmptyError",
    "The search query is empty"
);
createBadRequestError!(
    PySearchWithLinkNotSupportedError,
    "SearchWithLinkNotSupportedError",
    "You cannot provide a search query and an invite link at the same time"
);
createBadRequestError!(
    PySecondsInvalidError,
    "SecondsInvalidError",
    "Slow mode only supports certain values (e.g. 0, 10s, 30s, 1m, 5m, 15m and 1h)"
);
createBadRequestError!(
    PySendAsPeerInvalidError,
    "SendAsPeerInvalidError",
    "You can't send messages as the specified peer"
);
createBadRequestError!(
    PySendMessageMediaInvalidError,
    "SendMessageMediaInvalidError",
    "The message media was invalid or not specified"
);
createBadRequestError!(
    PySendMessageTypeInvalidError,
    "SendMessageTypeInvalidError",
    "The message type is invalid"
);
createBadRequestError!(
    PySessionTooFreshError,
    "SessionTooFreshError",
    "The session logged in too recently and {} seconds must pass before calling the method"
);
createBadRequestError!(
    PySettingsInvalidError,
    "SettingsInvalidError",
    "Invalid settings were provided"
);
createBadRequestError!(
    PySha256HashInvalidError,
    "Sha256HashInvalidError",
    "The provided SHA256 hash is invalid"
);
createBadRequestError!(
    PyShortnameOccupyFailedError,
    "ShortnameOccupyFailedError",
    "An error occurred when trying to register the short-name used for the sticker pack. Try a different name"
);
createBadRequestError!(
    PyShortNameInvalidError,
    "ShortNameInvalidError",
    "The specified short name is invalid"
);
createBadRequestError!(
    PyShortNameOccupiedError,
    "ShortNameOccupiedError",
    "The specified short name is already in use"
);
createBadRequestError!(
    PySlowModeMultiMsgsDisabledError,
    "SlowModeMultiMsgsDisabledError",
    "Slowmode is enabled, you cannot forward multiple messages to this group"
);
createBadRequestError!(
    PySmsCodeCreateFailedError,
    "SmsCodeCreateFailedError",
    "An error occurred while creating the SMS code"
);
createBadRequestError!(
    PySrpIdInvalidError,
    "SrpIdInvalidError",
    "Invalid SRP ID provided"
);
createBadRequestError!(
    PySrpPasswordChangedError,
    "SrpPasswordChangedError",
    "Password has changed"
);
createBadRequestError!(
    PyStartParamEmptyError,
    "StartParamEmptyError",
    "The start parameter is empty"
);
createBadRequestError!(
    PyStartParamInvalidError,
    "StartParamInvalidError",
    "Start parameter invalid"
);
createBadRequestError!(
    PyStartParamTooLongError,
    "StartParamTooLongError",
    "Start parameter is too long"
);
createBadRequestError!(
    PyStickerpackStickersTooMuchError,
    "StickerpackStickersTooMuchError",
    "There are too many stickers in this stickerpack, you can't add any more"
);
createBadRequestError!(
    PyStickersetInvalidError,
    "StickersetInvalidError",
    "The provided sticker set is invalid"
);
createBadRequestError!(
    PyStickersEmptyError,
    "StickersEmptyError",
    "No sticker provided"
);
createBadRequestError!(
    PyStickersTooMuchError,
    "StickersTooMuchError",
    "There are too many stickers in this stickerpack, you can't add any more"
);
createBadRequestError!(
    PyStickerDocumentInvalidError,
    "StickerDocumentInvalidError",
    "The sticker file was invalid (this file has failed Telegram internal checks, make sure to use the correct format and comply with https://core.telegram.org/animated_stickers)"
);
createBadRequestError!(
    PyStickerEmojiInvalidError,
    "StickerEmojiInvalidError",
    "Sticker emoji invalid"
);
createBadRequestError!(
    PyStickerFileInvalidError,
    "StickerFileInvalidError",
    "Sticker file invalid"
);
createBadRequestError!(
    PyStickerGifDimensionsError,
    "StickerGifDimensionsError",
    "The specified video sticker has invalid dimensions"
);
createBadRequestError!(
    PyStickerIdInvalidError,
    "StickerIdInvalidError",
    "The provided sticker ID is invalid"
);
createBadRequestError!(
    PyStickerInvalidError,
    "StickerInvalidError",
    "The provided sticker is invalid"
);
createBadRequestError!(
    PyStickerMimeInvalidError,
    "StickerMimeInvalidError",
    "Make sure to pass a valid image file for the right InputFile parameter"
);
createBadRequestError!(
    PyStickerPngDimensionsError,
    "StickerPngDimensionsError",
    "Sticker png dimensions invalid"
);
createBadRequestError!(
    PyStickerPngNopngError,
    "StickerPngNopngError",
    "Stickers must be a png file but the used image was not a png"
);
createBadRequestError!(
    PyStickerTgsNodocError,
    "StickerTgsNodocError",
    "You must send the animated sticker as a document"
);
createBadRequestError!(
    PyStickerTgsNotgsError,
    "StickerTgsNotgsError",
    "Stickers must be a tgs file but the used file was not a tgs"
);
createBadRequestError!(
    PyStickerThumbPngNopngError,
    "StickerThumbPngNopngError",
    "Stickerset thumb must be a png file but the used file was not png"
);
createBadRequestError!(
    PyStickerThumbTgsNotgsError,
    "StickerThumbTgsNotgsError",
    "Stickerset thumb must be a tgs file but the used file was not tgs"
);
createBadRequestError!(
    PyStickerVideoBigError,
    "StickerVideoBigError",
    "The specified video sticker is too big"
);
createBadRequestError!(
    PyStickerVideoNodocError,
    "StickerVideoNodocError",
    "You must send the video sticker as a document"
);
createBadRequestError!(
    PyStickerVideoNowebmError,
    "StickerVideoNowebmError",
    "The specified video sticker is not in webm format"
);
createBadRequestError!(
    PySwitchPmTextEmptyError,
    "SwitchPmTextEmptyError",
    "The switch_pm.text field was empty"
);
createBadRequestError!(
    PyTakeoutInvalidError,
    "TakeoutInvalidError",
    "The takeout session has been invalidated by another data export session"
);
createBadRequestError!(
    PyTakeoutRequiredError,
    "TakeoutRequiredError",
    "You must initialize a takeout request first"
);
createBadRequestError!(
    PyTempAuthKeyAlreadyBoundError,
    "TempAuthKeyAlreadyBoundError",
    "The passed temporary key is already bound to another **perm_auth_key_id**"
);
createBadRequestError!(
    PyTempAuthKeyEmptyError,
    "TempAuthKeyEmptyError",
    "No temporary auth key provided"
);
createBadRequestError!(
    PyThemeFileInvalidError,
    "ThemeFileInvalidError",
    "Invalid theme file provided"
);
createBadRequestError!(
    PyThemeFormatInvalidError,
    "ThemeFormatInvalidError",
    "Invalid theme format provided"
);
createBadRequestError!(PyThemeInvalidError, "ThemeInvalidError", "Theme invalid");
createBadRequestError!(
    PyThemeMimeInvalidError,
    "ThemeMimeInvalidError",
    "You cannot create this theme, the mime-type is invalid"
);
createBadRequestError!(
    PyThemeTitleInvalidError,
    "ThemeTitleInvalidError",
    "The specified theme title is invalid"
);
createBadRequestError!(
    PyTitleInvalidError,
    "TitleInvalidError",
    "The specified stickerpack title is invalid"
);
createBadRequestError!(
    PyTmpPasswordDisabledError,
    "TmpPasswordDisabledError",
    "The temporary password is disabled"
);
createBadRequestError!(
    PyTmpPasswordInvalidError,
    "TmpPasswordInvalidError",
    "Password auth needs to be regenerated"
);
createBadRequestError!(
    PyTokenInvalidError,
    "TokenInvalidError",
    "The provided token is invalid"
);
createBadRequestError!(
    PyTopicDeletedError,
    "TopicDeletedError",
    "The topic was deleted"
);
createBadRequestError!(
    PyToLangInvalidError,
    "ToLangInvalidError",
    "The specified destination language is invalid"
);
createBadRequestError!(
    PyTtlDaysInvalidError,
    "TtlDaysInvalidError",
    "The provided TTL is invalid"
);
createBadRequestError!(
    PyTtlMediaInvalidError,
    "TtlMediaInvalidError",
    "The provided media cannot be used with a TTL"
);
createBadRequestError!(
    PyTtlPeriodInvalidError,
    "TtlPeriodInvalidError",
    "The provided TTL Period is invalid"
);
createBadRequestError!(
    PyTypesEmptyError,
    "TypesEmptyError",
    "The types field is empty"
);
createBadRequestError!(
    PyTypeConstructorInvalidError,
    "TypeConstructorInvalidError",
    "The type constructor is invalid"
);
createBadRequestError!(PyUnknownErrorError, "UnknownErrorError", "");
createBadRequestError!(
    PyUntilDateInvalidError,
    "UntilDateInvalidError",
    "That date cannot be specified in this request (try using None)"
);
createBadRequestError!(
    PyUrlInvalidError,
    "UrlInvalidError",
    "The URL used was invalid (e.g. when answering a callback with a URL that's not t.me/yourbot or your game's URL)"
);
createBadRequestError!(
    PyUsageLimitInvalidError,
    "UsageLimitInvalidError",
    "The specified usage limit is invalid"
);
createBadRequestError!(
    PyUsernameInvalidError,
    "UsernameInvalidError",
    "Nobody is using this username, or the username is unacceptable. If the latter, it must match r\"[a-zA-Z][\\w\\d]{3,30}[a-zA-Z\\d]\""
);
createBadRequestError!(
    PyUsernameNotModifiedError,
    "UsernameNotModifiedError",
    "The username is not different from the current username"
);
createBadRequestError!(
    PyUsernameNotOccupiedError,
    "UsernameNotOccupiedError",
    "The username is not in use by anyone else yet"
);
createBadRequestError!(
    PyUsernameOccupiedError,
    "UsernameOccupiedError",
    "The username is already taken"
);
createBadRequestError!(
    PyUsernamePurchaseAvailableError,
    "UsernamePurchaseAvailableError",
    ""
);
createBadRequestError!(
    PyUserpicUploadRequiredError,
    "UserpicUploadRequiredError",
    "You must have a profile picture before using this method"
);
createBadRequestError!(
    PyUsersTooFewError,
    "UsersTooFewError",
    "Not enough users (to create a chat, for example)"
);
createBadRequestError!(
    PyUsersTooMuchError,
    "UsersTooMuchError",
    "The maximum number of users has been exceeded (to create a chat, for example)"
);
createBadRequestError!(
    PyUserAdminInvalidError,
    "UserAdminInvalidError",
    "Either you're not an admin or you tried to ban an admin that you didn't promote"
);
createBadRequestError!(
    PyUserAlreadyInvitedError,
    "UserAlreadyInvitedError",
    "You have already invited this user"
);
createBadRequestError!(
    PyUserAlreadyParticipantError,
    "UserAlreadyParticipantError",
    "The authenticated user is already a participant of the chat"
);
createBadRequestError!(
    PyUserBannedInChannelError,
    "UserBannedInChannelError",
    "You're banned from sending messages in supergroups/channels"
);
createBadRequestError!(PyUserBlockedError, "UserBlockedError", "User blocked");
createBadRequestError!(
    PyUserBotError,
    "UserBotError",
    "Bots can only be admins in channels."
);
createBadRequestError!(
    PyUserBotInvalidError,
    "UserBotInvalidError",
    "This method can only be called by a bot"
);
createBadRequestError!(
    PyUserBotRequiredError,
    "UserBotRequiredError",
    "This method can only be called by a bot"
);
createBadRequestError!(
    PyUserChannelsTooMuchError,
    "UserChannelsTooMuchError",
    "One of the users you tried to add is already in too many channels/supergroups"
);
createBadRequestError!(
    PyUserCreatorError,
    "UserCreatorError",
    "You can't leave this channel, because you're its creator"
);
createBadRequestError!(
    PyUserIdInvalidError,
    "UserIdInvalidError",
    "Invalid object ID for a user. Make sure to pass the right types, for instance making sure that the request is designed for users or otherwise look for a different one more suited"
);
createBadRequestError!(
    PyUserInvalidError,
    "UserInvalidError",
    "The given user was invalid"
);
createBadRequestError!(
    PyUserIsBlockedError,
    "UserIsBlockedError",
    "User is blocked"
);
createBadRequestError!(
    PyUserIsBotError,
    "UserIsBotError",
    "Bots can't send messages to other bots"
);
createBadRequestError!(
    PyUserKickedError,
    "UserKickedError",
    "This user was kicked from this supergroup/channel"
);
createBadRequestError!(
    PyUserNotMutualContactError,
    "UserNotMutualContactError",
    "The provided user is not a mutual contact"
);
createBadRequestError!(
    PyUserNotParticipantError,
    "UserNotParticipantError",
    "The target user is not a member of the specified megagroup or channel"
);
createBadRequestError!(
    PyUserVolumeInvalidError,
    "UserVolumeInvalidError",
    "The specified user volume is invalid"
);
createBadRequestError!(
    PyVideoContentTypeInvalidError,
    "VideoContentTypeInvalidError",
    "The video content type is not supported with the given parameters (i.e. supports_streaming)"
);
createBadRequestError!(
    PyVideoFileInvalidError,
    "VideoFileInvalidError",
    "The given video cannot be used"
);
createBadRequestError!(
    PyVideoTitleEmptyError,
    "VideoTitleEmptyError",
    "The specified video title is empty"
);
createBadRequestError!(
    PyVoiceMessagesForbiddenError,
    "VoiceMessagesForbiddenError",
    "This user's privacy settings forbid you from sending voice messages"
);
createBadRequestError!(
    PyWallpaperFileInvalidError,
    "WallpaperFileInvalidError",
    "The given file cannot be used as a wallpaper"
);
createBadRequestError!(
    PyWallpaperInvalidError,
    "WallpaperInvalidError",
    "The input wallpaper was not valid"
);
createBadRequestError!(
    PyWallpaperMimeInvalidError,
    "WallpaperMimeInvalidError",
    "The specified wallpaper MIME type is invalid"
);
createBadRequestError!(
    PyWcConvertUrlInvalidError,
    "WcConvertUrlInvalidError",
    "WC convert URL invalid"
);
createBadRequestError!(
    PyWebdocumentInvalidError,
    "WebdocumentInvalidError",
    "Invalid webdocument URL provided"
);
createBadRequestError!(
    PyWebdocumentMimeInvalidError,
    "WebdocumentMimeInvalidError",
    "Invalid webdocument mime type provided"
);
createBadRequestError!(
    PyWebdocumentSizeTooBigError,
    "WebdocumentSizeTooBigError",
    "Webdocument is too big!"
);
createBadRequestError!(
    PyWebdocumentUrlInvalidError,
    "WebdocumentUrlInvalidError",
    "The given URL cannot be used"
);
createBadRequestError!(
    PyWebpageCurlFailedError,
    "WebpageCurlFailedError",
    "Failure while fetching the webpage with cURL"
);
createBadRequestError!(
    PyWebpageMediaEmptyError,
    "WebpageMediaEmptyError",
    "Webpage media empty"
);
createBadRequestError!(
    PyWebpushAuthInvalidError,
    "WebpushAuthInvalidError",
    "The specified web push authentication secret is invalid"
);
createBadRequestError!(
    PyWebpushKeyInvalidError,
    "WebpushKeyInvalidError",
    "The specified web push elliptic curve Diffie-Hellman public key is invalid"
);
createBadRequestError!(
    PyWebpushTokenInvalidError,
    "WebpushTokenInvalidError",
    "The specified web push token is invalid"
);
createBadRequestError!(
    PyYouBlockedUserError,
    "YouBlockedUserError",
    "You blocked this user"
);
createBadRequestError!(
    PyFrozenParticipantMissingError,
    "FrozenParticipantMissingError",
    "Your account is frozen and can't access the chat"
);

// ========== UnauthorizedError ==========

createUnauthorizedError!(
    PyActiveUserRequiredError,
    "ActiveUserRequiredError",
    "The method is only available to already activated users"
);
createUnauthorizedError!(
    PyAuthKeyInvalidError,
    "AuthKeyInvalidError",
    "The key is invalid"
);
createUnauthorizedError!(
    PyAuthKeyPermEmptyError,
    "AuthKeyPermEmptyError",
    "The method is unavailable for temporary authorization key, not bound to permanent"
);
createUnauthorizedError!(
    PyAuthKeyUnregisteredError,
    "AuthKeyUnregisteredError",
    "The key is not registered in the system"
);
createUnauthorizedError!(
    PySessionExpiredError,
    "SessionExpiredError",
    "The authorization has expired"
);
createUnauthorizedError!(
    PySessionPasswordNeededError,
    "SessionPasswordNeededError",
    "Two-steps verification is enabled and a password is required"
);
createUnauthorizedError!(
    PySessionRevokedError,
    "SessionRevokedError",
    "The authorization has been invalidated, because of the user terminating all sessions"
);
createUnauthorizedError!(
    PyUserDeactivatedError,
    "UserDeactivatedError",
    "The user has been deleted/deactivated"
);
createUnauthorizedError!(
    PyUserDeactivatedBanError,
    "UserDeactivatedBanError",
    "The user has been deleted/deactivated"
);

// ========== ForbiddenError ==========

createForbiddenError!(
    PyBroadcastForbiddenError,
    "BroadcastForbiddenError",
    "The request cannot be used in broadcast channels"
);
createForbiddenError!(
    PyChannelPublicGroupNaError,
    "ChannelPublicGroupNaError",
    "channel/supergroup not available"
);
createForbiddenError!(
    PyChatAdminInviteRequiredError,
    "ChatAdminInviteRequiredError",
    "You do not have the rights to do this"
);
createForbiddenError!(
    PyChatForbiddenError,
    "ChatForbiddenError",
    "You cannot write in this chat"
);
createForbiddenError!(
    PyChatGuestSendForbiddenError,
    "ChatGuestSendForbiddenError",
    "You join the discussion group before commenting, see [here](/api/discussion#requiring-users-to-join-the-group) for more info"
);
createForbiddenError!(
    PyChatSendGameForbiddenError,
    "ChatSendGameForbiddenError",
    "You can't send a game to this chat"
);
createForbiddenError!(
    PyChatSendGifsForbiddenError,
    "ChatSendGifsForbiddenError",
    "You can't send gifs in this chat"
);
createForbiddenError!(
    PyChatSendMediaForbiddenError,
    "ChatSendMediaForbiddenError",
    "You can't send media in this chat"
);
createForbiddenError!(
    PyChatSendPollForbiddenError,
    "ChatSendPollForbiddenError",
    "You can't send polls in this chat"
);
createForbiddenError!(
    PyChatSendStickersForbiddenError,
    "ChatSendStickersForbiddenError",
    "You can't send stickers in this chat"
);
createForbiddenError!(
    PyChatWriteForbiddenError,
    "ChatWriteForbiddenError",
    "You can't write in this chat"
);
createForbiddenError!(
    PyEditBotInviteForbiddenError,
    "EditBotInviteForbiddenError",
    "Normal users can't edit invites that were created by bots"
);
createForbiddenError!(
    PyGroupcallAlreadyStartedError,
    "GroupcallAlreadyStartedError",
    "The groupcall has already started, you can join directly using [phone.joinGroupCall](https://core.telegram.org/method/phone.joinGroupCall)"
);
createForbiddenError!(
    PyGroupcallForbiddenError,
    "GroupcallForbiddenError",
    "The group call has already ended"
);
createForbiddenError!(
    PyInlineBotRequiredError,
    "InlineBotRequiredError",
    "The action must be performed through an inline bot callback"
);
createForbiddenError!(
    PyMessageAuthorRequiredError,
    "MessageAuthorRequiredError",
    "Message author required"
);
createForbiddenError!(
    PyMessageDeleteForbiddenError,
    "MessageDeleteForbiddenError",
    "You can't delete one of the messages you tried to delete, most likely because it is a service message."
);
createForbiddenError!(PyNotAllowedError, "NotAllowedError", "");
createForbiddenError!(
    PyPollVoteRequiredError,
    "PollVoteRequiredError",
    "Cast a vote in the poll before calling this method"
);
createForbiddenError!(
    PyPremiumAccountRequiredError,
    "PremiumAccountRequiredError",
    "A premium account is required to execute this action"
);
createForbiddenError!(
    PyPublicChannelMissingError,
    "PublicChannelMissingError",
    "You can only export group call invite links for public chats or channels"
);
createForbiddenError!(
    PyRightForbiddenError,
    "RightForbiddenError",
    "Either your admin rights do not allow you to do this or you passed the wrong rights combination (some rights only apply to channels and vice versa)"
);
createForbiddenError!(
    PySensitiveChangeForbiddenError,
    "SensitiveChangeForbiddenError",
    "Your sensitive content settings cannot be changed at this time"
);
createForbiddenError!(
    PyUserDeletedError,
    "UserDeletedError",
    "You can't send this secret message because the other participant deleted their account"
);
createForbiddenError!(
    PyUserPrivacyRestrictedError,
    "UserPrivacyRestrictedError",
    "The user's privacy settings do not allow you to do this"
);
createForbiddenError!(
    PyUserRestrictedError,
    "UserRestrictedError",
    "You're spamreported, you can't create channels or chats."
);

// ========== AuthKeyError ==========

createAuthKeyError!(
    PyAuthKeyDuplicatedError,
    "AuthKeyDuplicatedError",
    "The authorization key (session file) was used under two different IP addresses simultaneously, and can no longer be used. Use the same session exclusively, or use different sessions"
);
createAuthKeyError!(
    PyFilerefUpgradeNeededError,
    "FilerefUpgradeNeededError",
    "The file reference needs to be refreshed before being used again"
);
createAuthKeyError!(
    PyFreshChangePhoneForbiddenError,
    "FreshChangePhoneForbiddenError",
    "Recently logged-in users cannot use this request"
);
createAuthKeyError!(
    PyFreshResetAuthorisationForbiddenError,
    "FreshResetAuthorisationForbiddenError",
    "The current session is too new and cannot be used to reset other authorisations yet"
);
createAuthKeyError!(
    PyPhonePasswordFloodError,
    "PhonePasswordFloodError",
    "You have tried logging in too many times"
);
createAuthKeyError!(
    PyPremiumCurrentlyUnavailableError,
    "PremiumCurrentlyUnavailableError",
    ""
);
createAuthKeyError!(
    PyPreviousChatImportActiveWaitMinError,
    "PreviousChatImportActiveWaitMinError",
    "Similar to a flood wait, must wait {} minutes"
);
createAuthKeyError!(
    PySendCodeUnavailableError,
    "SendCodeUnavailableError",
    "Returned when all available options for this type of number were already used (e.g. flash-call, then SMS, then this error might be returned to trigger a second resend)"
);
createAuthKeyError!(
    PyStickersetOwnerAnonymousError,
    "StickersetOwnerAnonymousError",
    "This sticker set can't be used as the group's official stickers because it was created by one of its anonymous admins"
);
createAuthKeyError!(PyUpdateAppToLoginError, "UpdateAppToLoginError", "");
createAuthKeyError!(
    PyUserpicPrivacyRequiredError,
    "UserpicPrivacyRequiredError",
    "You need to disable privacy settings for your profile picture in order to make your geolocation public"
);

// ========== FloodError ==========

createFloodError!(
    PyTwoFaConfirmWaitError,
    "TwoFaConfirmWaitError",
    "The account is 2FA protected so it will be deleted in a week. Otherwise it can be reset in {}"
);
createFloodError!(
    PyFloodTestPhoneWaitError,
    "FloodTestPhoneWaitError",
    "A wait of {} seconds is required in the test servers"
);
createFloodError!(
    PyFloodWaitError,
    "FloodWaitError",
    "A wait of {} seconds is required"
);
createFloodError!(
    PyFloodPremiumWaitError,
    "FloodPremiumWaitError",
    "A wait of {} seconds is required in non-premium accounts"
);
createFloodError!(
    PySlowModeWaitError,
    "SlowModeWaitError",
    "A wait of {} seconds is required before sending another message in this chat"
);
createFloodError!(
    PyTakeoutInitDelayError,
    "TakeoutInitDelayError",
    "A wait of {} seconds is required before being able to initiate the takeout"
);
createFloodError!(
    PyFrozenMethodInvalidError,
    "FrozenMethodInvalidError",
    "You tried to use a method that is not available for frozen accounts"
);

// ========== ServerError ==========

createServerError!(
    PyAuthRestartError,
    "AuthRestartError",
    "Restart the authorization process"
);
createServerError!(
    PyCallOccupyFailedError,
    "CallOccupyFailedError",
    "The call failed because the user is already making another call"
);
createServerError!(
    PyCdnUploadTimeoutError,
    "CdnUploadTimeoutError",
    "A server-side timeout occurred while reuploading the file to the CDN DC"
);
createServerError!(PyChatGetFailedError, "ChatGetFailedError", "");
createServerError!(
    PyChatIdGenerateFailedError,
    "ChatIdGenerateFailedError",
    "Failure while generating the chat ID"
);
createServerError!(
    PyChpCallFailError,
    "ChpCallFailError",
    "The statistics cannot be retrieved at this time"
);
createServerError!(
    PyEncryptionOccupyFailedError,
    "EncryptionOccupyFailedError",
    "TDLib developer claimed it is not an error while accepting secret chats and 500 is used instead of 420"
);
createServerError!(
    PyGroupcallAddParticipantsFailedError,
    "GroupcallAddParticipantsFailedError",
    ""
);
createServerError!(
    PyHistoryGetFailedError,
    "HistoryGetFailedError",
    "Fetching of history failed"
);
createServerError!(
    PyInterdcCallErrorError,
    "InterdcCallErrorError",
    "An error occurred while communicating with DC {}"
);
createServerError!(
    PyInterdcCallRichErrorError,
    "InterdcCallRichErrorError",
    "A rich error occurred while communicating with DC {}"
);
createServerError!(
    PyMemberNoLocationError,
    "MemberNoLocationError",
    "An internal failure occurred while fetching user info (couldn't find location)"
);
createServerError!(
    PyMemberOccupyPrimaryLocFailedError,
    "MemberOccupyPrimaryLocFailedError",
    "Occupation of primary member location failed"
);
createServerError!(
    PyMsgidDecreaseRetryError,
    "MsgidDecreaseRetryError",
    "The request should be retried with a lower message ID"
);
createServerError!(PyMtSendQueueTooLongError, "MtSendQueueTooLongError", "");
createServerError!(
    PyNeedChatInvalidError,
    "NeedChatInvalidError",
    "The provided chat is invalid"
);
createServerError!(
    PyNeedMemberInvalidError,
    "NeedMemberInvalidError",
    "The provided member is invalid or does not exist (for example a thumb size)"
);
createServerError!(
    PyParticipantCallFailedError,
    "ParticipantCallFailedError",
    "Failure while making call"
);
createServerError!(
    PyPersistentTimestampOutdatedError,
    "PersistentTimestampOutdatedError",
    "Persistent timestamp outdated"
);
createServerError!(
    PyPostponedTimeoutError,
    "PostponedTimeoutError",
    "The postponed call has timed out"
);
createServerError!(
    PyPtsChangeEmptyError,
    "PtsChangeEmptyError",
    "No PTS change"
);
createServerError!(
    PyRandomIdDuplicateError,
    "RandomIdDuplicateError",
    "You provided a random ID that was already used"
);
createServerError!(
    PyRegIdGenerateFailedError,
    "RegIdGenerateFailedError",
    "Failure while generating registration ID"
);
createServerError!(
    PyRpcCallFailError,
    "RpcCallFailError",
    "Telegram is having internal issues, please try again later."
);
createServerError!(
    PyRpcMcgetFailError,
    "RpcMcgetFailError",
    "Telegram is having internal issues, please try again later."
);
createServerError!(
    PySignInFailedError,
    "SignInFailedError",
    "Failure while signing in"
);
createServerError!(
    PyStorageCheckFailedError,
    "StorageCheckFailedError",
    "Server storage check failed"
);
createServerError!(
    PyStoreInvalidScalarTypeError,
    "StoreInvalidScalarTypeError",
    ""
);
createServerError!(
    PyUnknownMethodError,
    "UnknownMethodError",
    "The method you tried to call cannot be called on non-CDN DCs"
);
createServerError!(
    PyWorkerBusyTooLongRetryError,
    "WorkerBusyTooLongRetryError",
    "Telegram workers are too busy to respond immediately"
);
