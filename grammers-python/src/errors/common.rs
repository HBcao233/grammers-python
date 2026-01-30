use pyo3::create_exception;
use pyo3::exceptions::{PyException, PyIOError, PyRuntimeError};
use pyo3::prelude::*;

use grammers_mtsender_pyo3::InvocationError;

use super::rpcbaseerrors::{
    PyAuthKeyError, PyBadRequestError, PyFloodError, PyForbiddenError, PyInvalidDCError,
    PyNotFoundError, PyRpcError, PyServerError, PyTimedOutError, PyUnauthorizedError,
};
use super::rpcerrorlist::*;
use grammers_tl_types_pyo3 as pytl;

create_exception!("grammers.errors", DroppedError, PyException);
create_exception!("grammers.errors", DeserializeError, PyException);
create_exception!("grammers.errors", TransportError, PyException);

pub struct InvocationErrorConverter(pub InvocationError);

impl From<InvocationError> for InvocationErrorConverter {
    fn from(x: InvocationError) -> Self {
        InvocationErrorConverter(x)
    }
}
impl From<InvocationErrorConverter> for PyErr {
    fn from(err: InvocationErrorConverter) -> PyErr {
        match err.0 {
            InvocationError::Rpc(e) => match e.code {
                303 => if e.is("FILE_MIGRATE_*"){
                    PyFileMigrateError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("NETWORK_MIGRATE_*"){
                    PyNetworkMigrateError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_MIGRATE_*"){
                    PyPhoneMigrateError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STATS_MIGRATE_*"){
                    PyStatsMigrateError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_MIGRATE_*"){
                    PyUserMigrateError::new_err(e.name, e.value, e.caused_by)
                } else {
                    PyInvalidDCError::new_err(e.name, e.value, e.caused_by, None)
                },
                400 => if e.is("ABOUT_TOO_LONG"){
                    PyAboutTooLongError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ACCESS_TOKEN_EXPIRED"){
                    PyAccessTokenExpiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ACCESS_TOKEN_INVALID"){
                    PyAccessTokenInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ADMINS_TOO_MUCH"){
                    PyAdminsTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ADMIN_ID_INVALID"){
                    PyAdminIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ADMIN_RANK_EMOJI_NOT_ALLOWED"){
                    PyAdminRankEmojiNotAllowedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ADMIN_RANK_INVALID"){
                    PyAdminRankInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ALBUM_PHOTOS_TOO_MANY"){
                    PyAlbumPhotosTooManyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("API_ID_INVALID"){
                    PyApiIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("API_ID_PUBLISHED_FLOOD"){
                    PyApiIdPublishedFloodError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ARTICLE_TITLE_EMPTY"){
                    PyArticleTitleEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUDIO_CONTENT_URL_EMPTY"){
                    PyAudioContentUrlEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUDIO_TITLE_EMPTY"){
                    PyAudioTitleEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUTH_BYTES_INVALID"){
                    PyAuthBytesInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUTH_TOKEN_ALREADY_ACCEPTED"){
                    PyAuthTokenAlreadyAcceptedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUTH_TOKEN_EXCEPTION"){
                    PyAuthTokenExceptionError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUTH_TOKEN_EXPIRED"){
                    PyAuthTokenExpiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUTH_TOKEN_INVALID"){
                    PyAuthTokenInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUTH_TOKEN_INVALID2"){
                    PyAuthTokenInvalid2Error::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUTH_TOKEN_INVALIDX"){
                    PyAuthTokenInvalidxError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUTOARCHIVE_NOT_AVAILABLE"){
                    PyAutoarchiveNotAvailableError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BANK_CARD_NUMBER_INVALID"){
                    PyBankCardNumberInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BANNED_RIGHTS_INVALID"){
                    PyBannedRightsInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BASE_PORT_LOC_INVALID"){
                    PyBasePortLocInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOTS_TOO_MUCH"){
                    PyBotsTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_CHANNELS_NA"){
                    PyBotChannelsNaError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_COMMAND_DESCRIPTION_INVALID"){
                    PyBotCommandDescriptionInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_COMMAND_INVALID"){
                    PyBotCommandInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_DOMAIN_INVALID"){
                    PyBotDomainInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_GAMES_DISABLED"){
                    PyBotGamesDisabledError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_GROUPS_BLOCKED"){
                    PyBotGroupsBlockedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_INLINE_DISABLED"){
                    PyBotInlineDisabledError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_INVALID"){
                    PyBotInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_METHOD_INVALID"){
                    PyBotMethodInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_MISSING"){
                    PyBotMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_ONESIDE_NOT_AVAIL"){
                    PyBotOnesideNotAvailError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_PAYMENTS_DISABLED"){
                    PyBotPaymentsDisabledError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_POLLS_DISABLED"){
                    PyBotPollsDisabledError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_RESPONSE_TIMEOUT"){
                    PyBotResponseTimeoutError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BOT_SCORE_NOT_MODIFIED"){
                    PyBotScoreNotModifiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BROADCAST_CALLS_DISABLED"){
                    PyBroadcastCallsDisabledError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BROADCAST_ID_INVALID"){
                    PyBroadcastIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BROADCAST_PUBLIC_VOTERS_FORBIDDEN"){
                    PyBroadcastPublicVotersForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BROADCAST_REQUIRED"){
                    PyBroadcastRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BUTTON_DATA_INVALID"){
                    PyButtonDataInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BUTTON_TEXT_INVALID"){
                    PyButtonTextInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BUTTON_TYPE_INVALID"){
                    PyButtonTypeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BUTTON_URL_INVALID"){
                    PyButtonUrlInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("BUTTON_USER_PRIVACY_RESTRICTED"){
                    PyButtonUserPrivacyRestrictedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CALL_ALREADY_ACCEPTED"){
                    PyCallAlreadyAcceptedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CALL_ALREADY_DECLINED"){
                    PyCallAlreadyDeclinedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CALL_PEER_INVALID"){
                    PyCallPeerInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CALL_PROTOCOL_FLAGS_INVALID"){
                    PyCallProtocolFlagsInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CDN_METHOD_INVALID"){
                    PyCdnMethodInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHANNELS_ADMIN_LOCATED_TOO_MUCH"){
                    PyChannelsAdminLocatedTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHANNELS_ADMIN_PUBLIC_TOO_MUCH"){
                    PyChannelsAdminPublicTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHANNELS_TOO_MUCH"){
                    PyChannelsTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHANNEL_BANNED"){
                    PyChannelBannedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHANNEL_FORUM_MISSING"){
                    PyChannelForumMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHANNEL_ID_INVALID"){
                    PyChannelIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHANNEL_INVALID"){
                    PyChannelInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHANNEL_PARICIPANT_MISSING"){
                    PyChannelParicipantMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHANNEL_PRIVATE"){
                    PyChannelPrivateError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHANNEL_TOO_BIG"){
                    PyChannelTooBigError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHANNEL_TOO_LARGE"){
                    PyChannelTooLargeError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_ABOUT_NOT_MODIFIED"){
                    PyChatAboutNotModifiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_ABOUT_TOO_LONG"){
                    PyChatAboutTooLongError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_ADMIN_REQUIRED"){
                    PyChatAdminRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_DISCUSSION_UNALLOWED"){
                    PyChatDiscussionUnallowedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_FORWARDS_RESTRICTED"){
                    PyChatForwardsRestrictedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_ID_EMPTY"){
                    PyChatIdEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_ID_INVALID"){
                    PyChatIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_INVALID"){
                    PyChatInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_INVITE_PERMANENT"){
                    PyChatInvitePermanentError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_LINK_EXISTS"){
                    PyChatLinkExistsError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_NOT_MODIFIED"){
                    PyChatNotModifiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_RESTRICTED"){
                    PyChatRestrictedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_REVOKE_DATE_UNSUPPORTED"){
                    PyChatRevokeDateUnsupportedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_SEND_INLINE_FORBIDDEN"){
                    PyChatSendInlineForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_TITLE_EMPTY"){
                    PyChatTitleEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_TOO_BIG"){
                    PyChatTooBigError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CODE_EMPTY"){
                    PyCodeEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CODE_HASH_INVALID"){
                    PyCodeHashInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CODE_INVALID"){
                    PyCodeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CONNECTION_API_ID_INVALID"){
                    PyConnectionApiIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CONNECTION_APP_VERSION_EMPTY"){
                    PyConnectionAppVersionEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CONNECTION_DEVICE_MODEL_EMPTY"){
                    PyConnectionDeviceModelEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CONNECTION_LANG_PACK_INVALID"){
                    PyConnectionLangPackInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CONNECTION_LAYER_INVALID"){
                    PyConnectionLayerInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CONNECTION_NOT_INITED"){
                    PyConnectionNotInitedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CONNECTION_SYSTEM_EMPTY"){
                    PyConnectionSystemEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CONNECTION_SYSTEM_LANG_CODE_EMPTY"){
                    PyConnectionSystemLangCodeEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CONTACT_ADD_MISSING"){
                    PyContactAddMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CONTACT_ID_INVALID"){
                    PyContactIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CONTACT_NAME_EMPTY"){
                    PyContactNameEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CONTACT_REQ_MISSING"){
                    PyContactReqMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CREATE_CALL_FAILED"){
                    PyCreateCallFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CURRENCY_TOTAL_AMOUNT_INVALID"){
                    PyCurrencyTotalAmountInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("DATA_INVALID"){
                    PyDataInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("DATA_JSON_INVALID"){
                    PyDataJsonInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("DATA_TOO_LONG"){
                    PyDataTooLongError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("DATE_EMPTY"){
                    PyDateEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("DC_ID_INVALID"){
                    PyDcIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("DH_G_A_INVALID"){
                    PyDhGAInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("DOCUMENT_INVALID"){
                    PyDocumentInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EMAIL_HASH_EXPIRED"){
                    PyEmailHashExpiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EMAIL_INVALID"){
                    PyEmailInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EMAIL_UNCONFIRMED_*"){
                    PyEmailUnconfirmedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EMAIL_VERIFY_EXPIRED"){
                    PyEmailVerifyExpiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EMOJI_INVALID"){
                    PyEmojiInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EMOJI_NOT_MODIFIED"){
                    PyEmojiNotModifiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EMOTICON_EMPTY"){
                    PyEmoticonEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EMOTICON_INVALID"){
                    PyEmoticonInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EMOTICON_STICKERPACK_MISSING"){
                    PyEmoticonStickerpackMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ENCRYPTED_MESSAGE_INVALID"){
                    PyEncryptedMessageInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ENCRYPTION_ALREADY_ACCEPTED"){
                    PyEncryptionAlreadyAcceptedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ENCRYPTION_ALREADY_DECLINED"){
                    PyEncryptionAlreadyDeclinedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ENCRYPTION_DECLINED"){
                    PyEncryptionDeclinedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ENCRYPTION_ID_INVALID"){
                    PyEncryptionIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ENTITIES_TOO_LONG"){
                    PyEntitiesTooLongError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ENTITY_BOUNDS_INVALID"){
                    PyEntityBoundsInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ENTITY_MENTION_USER_INVALID"){
                    PyEntityMentionUserInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ERROR_TEXT_EMPTY"){
                    PyErrorTextEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EXPIRE_DATE_INVALID"){
                    PyExpireDateInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EXPIRE_FORBIDDEN"){
                    PyExpireForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EXPORT_CARD_INVALID"){
                    PyExportCardInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EXTERNAL_URL_INVALID"){
                    PyExternalUrlInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FIELD_NAME_EMPTY"){
                    PyFieldNameEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FIELD_NAME_INVALID"){
                    PyFieldNameInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_CONTENT_TYPE_INVALID"){
                    PyFileContentTypeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_EMTPY"){
                    PyFileEmtpyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_ID_INVALID"){
                    PyFileIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_PARTS_INVALID"){
                    PyFilePartsInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_PART_0_MISSING"){
                    PyFilePart0MissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_PART_EMPTY"){
                    PyFilePartEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_PART_INVALID"){
                    PyFilePartInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_PART_LENGTH_INVALID"){
                    PyFilePartLengthInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_PART_SIZE_CHANGED"){
                    PyFilePartSizeChangedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_PART_SIZE_INVALID"){
                    PyFilePartSizeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_PART_TOO_BIG"){
                    PyFilePartTooBigError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_PART_*_MISSING"){
                    PyFilePartMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_REFERENCE_EMPTY"){
                    PyFileReferenceEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_REFERENCE_EXPIRED"){
                    PyFileReferenceExpiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_REFERENCE_INVALID"){
                    PyFileReferenceInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILE_TITLE_EMPTY"){
                    PyFileTitleEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILTER_ID_INVALID"){
                    PyFilterIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILTER_INCLUDE_EMPTY"){
                    PyFilterIncludeEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILTER_NOT_SUPPORTED"){
                    PyFilterNotSupportedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILTER_TITLE_EMPTY"){
                    PyFilterTitleEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FIRSTNAME_INVALID"){
                    PyFirstNameInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FOLDER_ID_EMPTY"){
                    PyFolderIdEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FOLDER_ID_INVALID"){
                    PyFolderIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FRESH_CHANGE_ADMINS_FORBIDDEN"){
                    PyFreshChangeAdminsForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FROM_MESSAGE_BOT_DISABLED"){
                    PyFromMessageBotDisabledError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FROM_PEER_INVALID"){
                    PyFromPeerInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GAME_BOT_INVALID"){
                    PyGameBotInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GEO_POINT_INVALID"){
                    PyGeoPointInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GIF_CONTENT_TYPE_INVALID"){
                    PyGifContentTypeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GIF_ID_INVALID"){
                    PyGifIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GRAPH_EXPIRED_RELOAD"){
                    PyGraphExpiredReloadError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GRAPH_INVALID_RELOAD"){
                    PyGraphInvalidReloadError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GRAPH_OUTDATED_RELOAD"){
                    PyGraphOutdatedReloadError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GROUPCALL_ALREADY_DISCARDED"){
                    PyGroupcallAlreadyDiscardedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GROUPCALL_INVALID"){
                    PyGroupcallInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GROUPCALL_JOIN_MISSING"){
                    PyGroupcallJoinMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GROUPCALL_NOT_MODIFIED"){
                    PyGroupcallNotModifiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GROUPCALL_SSRC_DUPLICATE_MUCH"){
                    PyGroupcallSsrcDuplicateMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GROUPED_MEDIA_INVALID"){
                    PyGroupedMediaInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GROUP_CALL_INVALID"){
                    PyGroupCallInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("HASH_INVALID"){
                    PyHashInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("HIDE_REQUESTER_MISSING"){
                    PyHideRequesterMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("IMAGE_PROCESS_FAILED"){
                    PyImageProcessFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("IMPORT_FILE_INVALID"){
                    PyImportFileInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("IMPORT_FORMAT_UNRECOGNIZED"){
                    PyImportFormatUnrecognizedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("IMPORT_ID_INVALID"){
                    PyImportIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INLINE_RESULT_EXPIRED"){
                    PyInlineResultExpiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INPUT_CONSTRUCTOR_INVALID"){
                    PyInputConstructorInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INPUT_FETCH_ERROR"){
                    PyInputFetchErrorError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INPUT_FETCH_FAIL"){
                    PyInputFetchFailError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INPUT_FILTER_INVALID"){
                    PyInputFilterInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INPUT_LAYER_INVALID"){
                    PyInputLayerInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INPUT_METHOD_INVALID"){
                    PyInputMethodInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INPUT_REQUEST_TOO_LONG"){
                    PyInputRequestTooLongError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INPUT_TEXT_EMPTY"){
                    PyInputTextEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INPUT_USER_DEACTIVATED"){
                    PyInputUserDeactivatedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INVITE_FORBIDDEN_WITH_JOINAS"){
                    PyInviteForbiddenWithJoinasError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INVITE_HASH_EMPTY"){
                    PyInviteHashEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INVITE_HASH_EXPIRED"){
                    PyInviteHashExpiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INVITE_HASH_INVALID"){
                    PyInviteHashInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INVITE_REQUEST_SENT"){
                    PyInviteRequestSentError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INVITE_REVOKED_MISSING"){
                    PyInviteRevokedMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INVOICE_PAYLOAD_INVALID"){
                    PyInvoicePayloadInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("JOIN_AS_PEER_INVALID"){
                    PyJoinAsPeerInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("LANG_CODE_INVALID"){
                    PyLangCodeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("LANG_CODE_NOT_SUPPORTED"){
                    PyLangCodeNotSupportedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("LANG_PACK_INVALID"){
                    PyLangPackInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("LASTNAME_INVALID"){
                    PyLastnameInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("LIMIT_INVALID"){
                    PyLimitInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("LINK_NOT_MODIFIED"){
                    PyLinkNotModifiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("LOCATION_INVALID"){
                    PyLocationInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MAX_DATE_INVALID"){
                    PyMaxDateInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MAX_ID_INVALID"){
                    PyMaxIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MAX_QTS_INVALID"){
                    PyMaxQtsInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MD5_CHECKSUM_INVALID"){
                    PyMd5ChecksumInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MEDIA_CAPTION_TOO_LONG"){
                    PyMediaCaptionTooLongError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MEDIA_EMPTY"){
                    PyMediaEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MEDIA_GROUPED_INVALID"){
                    PyMediaGroupedInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MEDIA_INVALID"){
                    PyMediaInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MEDIA_NEW_INVALID"){
                    PyMediaNewInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MEDIA_PREV_INVALID"){
                    PyMediaPrevInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MEDIA_TTL_INVALID"){
                    PyMediaTtlInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MEGAGROUP_ID_INVALID"){
                    PyMegagroupIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MEGAGROUP_PREHISTORY_HIDDEN"){
                    PyMegagroupPrehistoryHiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MEGAGROUP_REQUIRED"){
                    PyMegagroupRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MESSAGE_EDIT_TIME_EXPIRED"){
                    PyMessageEditTimeExpiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MESSAGE_EMPTY"){
                    PyMessageEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MESSAGE_IDS_EMPTY"){
                    PyMessageIdsEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MESSAGE_ID_INVALID"){
                    PyMessageIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MESSAGE_NOT_MODIFIED"){
                    PyMessageNotModifiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MESSAGE_POLL_CLOSED"){
                    PyMessagePollClosedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MESSAGE_TOO_LONG"){
                    PyMessageTooLongError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("METHOD_INVALID"){
                    PyMethodInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MIN_DATE_INVALID"){
                    PyMinDateInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MSG_ID_INVALID"){
                    PyMsgIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MSG_TOO_OLD"){
                    PyMsgTooOldError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MSG_WAIT_FAILED"){
                    PyMsgWaitFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MULTI_MEDIA_TOO_LONG"){
                    PyMultiMediaTooLongError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("NEW_SALT_INVALID"){
                    PyNewSaltInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("NEW_SETTINGS_EMPTY"){
                    PyNewSettingsEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("NEW_SETTINGS_INVALID"){
                    PyNewSettingsInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("NEXT_OFFSET_INVALID"){
                    PyNextOffsetInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("OFFSET_INVALID"){
                    PyOffsetInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("OFFSET_PEER_ID_INVALID"){
                    PyOffsetPeerIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("OPTIONS_TOO_MUCH"){
                    PyOptionsTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("OPTION_INVALID"){
                    PyOptionInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PACK_SHORT_NAME_INVALID"){
                    PyPackShortNameInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PACK_SHORT_NAME_OCCUPIED"){
                    PyPackShortNameOccupiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PACK_TITLE_INVALID"){
                    PyPackTitleInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PARTICIPANTS_TOO_FEW"){
                    PyParticipantsTooFewError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PARTICIPANT_ID_INVALID"){
                    PyParticipantIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PARTICIPANT_JOIN_MISSING"){
                    PyParticipantJoinMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PARTICIPANT_VERSION_OUTDATED"){
                    PyParticipantVersionOutdatedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PASSWORD_EMPTY"){
                    PyPasswordEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PASSWORD_HASH_INVALID"){
                    PyPasswordHashInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PASSWORD_MISSING"){
                    PyPasswordMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PASSWORD_RECOVERY_EXPIRED"){
                    PyPasswordRecoveryExpiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PASSWORD_RECOVERY_NA"){
                    PyPasswordRecoveryNaError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PASSWORD_REQUIRED"){
                    PyPasswordRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PASSWORD_TOO_FRESH_*"){
                    PyPasswordTooFreshError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PAYMENT_PROVIDER_INVALID"){
                    PyPaymentProviderInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PEER_FLOOD"){
                    PyPeerFloodError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PEER_HISTORY_EMPTY"){
                    PyPeerHistoryEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PEER_ID_INVALID"){
                    PyPeerIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PEER_ID_NOT_SUPPORTED"){
                    PyPeerIdNotSupportedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PERSISTENT_TIMESTAMP_EMPTY"){
                    PyPersistentTimestampEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PERSISTENT_TIMESTAMP_INVALID"){
                    PyPersistentTimestampInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_CODE_EMPTY"){
                    PyPhoneCodeEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_CODE_EXPIRED"){
                    PyPhoneCodeExpiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_CODE_HASH_EMPTY"){
                    PyPhoneCodeHashEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_CODE_INVALID"){
                    PyPhoneCodeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_HASH_EXPIRED"){
                    PyPhoneHashExpiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_NOT_OCCUPIED"){
                    PyPhoneNotOccupiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_NUMBER_APP_SIGNUP_FORBIDDEN"){
                    PyPhoneNumberAppSignupForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_NUMBER_BANNED"){
                    PyPhoneNumberBannedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_NUMBER_FLOOD"){
                    PyPhoneNumberFloodError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_NUMBER_INVALID"){
                    PyPhoneNumberInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_NUMBER_OCCUPIED"){
                    PyPhoneNumberOccupiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_NUMBER_UNOCCUPIED"){
                    PyPhoneNumberUnoccupiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_PASSWORD_PROTECTED"){
                    PyPhonePasswordProtectedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHOTO_CONTENT_TYPE_INVALID"){
                    PyPhotoContentTypeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHOTO_CONTENT_URL_EMPTY"){
                    PyPhotoContentUrlEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHOTO_CROP_FILE_MISSING"){
                    PyPhotoCropFileMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHOTO_CROP_SIZE_SMALL"){
                    PyPhotoCropSizeSmallError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHOTO_EXT_INVALID"){
                    PyPhotoExtInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHOTO_FILE_MISSING"){
                    PyPhotoFileMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHOTO_ID_INVALID"){
                    PyPhotoIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHOTO_INVALID"){
                    PyPhotoInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHOTO_INVALID_DIMENSIONS"){
                    PyPhotoInvalidDimensionsError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHOTO_SAVE_FILE_INVALID"){
                    PyPhotoSaveFileInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHOTO_THUMB_URL_EMPTY"){
                    PyPhotoThumbUrlEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PINNED_DIALOGS_TOO_MUCH"){
                    PyPinnedDialogsTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PIN_RESTRICTED"){
                    PyPinRestrictedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("POLL_ANSWERS_INVALID"){
                    PyPollAnswersInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("POLL_ANSWER_INVALID"){
                    PyPollAnswerInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("POLL_OPTION_DUPLICATE"){
                    PyPollOptionDuplicateError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("POLL_OPTION_INVALID"){
                    PyPollOptionInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("POLL_QUESTION_INVALID"){
                    PyPollQuestionInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("POLL_UNSUPPORTED"){
                    PyPollUnsupportedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PRIVACY_KEY_INVALID"){
                    PyPrivacyKeyInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PRIVACY_TOO_LONG"){
                    PyPrivacyTooLongError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PRIVACY_VALUE_INVALID"){
                    PyPrivacyValueInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PUBLIC_KEY_REQUIRED"){
                    PyPublicKeyRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("QUERY_ID_EMPTY"){
                    PyQueryIdEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("QUERY_ID_INVALID"){
                    PyQueryIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("QUERY_TOO_SHORT"){
                    PyQueryTooShortError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("QUIZ_ANSWER_MISSING"){
                    PyQuizAnswerMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("QUIZ_CORRECT_ANSWERS_EMPTY"){
                    PyQuizCorrectAnswersEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("QUIZ_CORRECT_ANSWERS_TOO_MUCH"){
                    PyQuizCorrectAnswersTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("QUIZ_CORRECT_ANSWER_INVALID"){
                    PyQuizCorrectAnswerInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("QUIZ_MULTIPLE_INVALID"){
                    PyQuizMultipleInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RANDOM_ID_EMPTY"){
                    PyRandomIdEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RANDOM_ID_INVALID"){
                    PyRandomIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RANDOM_LENGTH_INVALID"){
                    PyRandomLengthInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RANGES_INVALID"){
                    PyRangesInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("REACTIONS_TOO_MANY"){
                    PyReactionsTooManyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("REACTION_EMPTY"){
                    PyReactionEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("REACTION_INVALID"){
                    PyReactionInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("REFLECTOR_NOT_AVAILABLE"){
                    PyReflectorNotAvailableError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("REPLY_MARKUP_BUY_EMPTY"){
                    PyReplyMarkupBuyEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("REPLY_MARKUP_GAME_EMPTY"){
                    PyReplyMarkupGameEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("REPLY_MARKUP_INVALID"){
                    PyReplyMarkupInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("REPLY_MARKUP_TOO_LONG"){
                    PyReplyMarkupTooLongError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RESET_REQUEST_MISSING"){
                    PyResetRequestMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RESULTS_TOO_MUCH"){
                    PyResultsTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RESULT_ID_DUPLICATE"){
                    PyResultIdDuplicateError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RESULT_ID_EMPTY"){
                    PyResultIdEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RESULT_ID_INVALID"){
                    PyResultIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RESULT_TYPE_INVALID"){
                    PyResultTypeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("REVOTE_NOT_ALLOWED"){
                    PyRevoteNotAllowedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RIGHTS_NOT_MODIFIED"){
                    PyRightsNotModifiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RSA_DECRYPT_FAILED"){
                    PyRsaDecryptFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SCHEDULE_BOT_NOT_ALLOWED"){
                    PyScheduleBotNotAllowedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SCHEDULE_DATE_INVALID"){
                    PyScheduleDateInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SCHEDULE_DATE_TOO_LATE"){
                    PyScheduleDateTooLateError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SCHEDULE_STATUS_PRIVATE"){
                    PyScheduleStatusPrivateError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SCHEDULE_TOO_MUCH"){
                    PyScheduleTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SCORE_INVALID"){
                    PyScoreInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SEARCH_QUERY_EMPTY"){
                    PySearchQueryEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SEARCH_WITH_LINK_NOT_SUPPORTED"){
                    PySearchWithLinkNotSupportedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SECONDS_INVALID"){
                    PySecondsInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SEND_AS_PEER_INVALID"){
                    PySendAsPeerInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SEND_MESSAGE_MEDIA_INVALID"){
                    PySendMessageMediaInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SEND_MESSAGE_TYPE_INVALID"){
                    PySendMessageTypeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SESSION_TOO_FRESH_*"){
                    PySessionTooFreshError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SETTINGS_INVALID"){
                    PySettingsInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SHA256_HASH_INVALID"){
                    PySha256HashInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SHORTNAME_OCCUPY_FAILED"){
                    PyShortnameOccupyFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SHORT_NAME_INVALID"){
                    PyShortNameInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SHORT_NAME_OCCUPIED"){
                    PyShortNameOccupiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SLOWMODE_MULTI_MSGS_DISABLED"){
                    PySlowModeMultiMsgsDisabledError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SMS_CODE_CREATE_FAILED"){
                    PySmsCodeCreateFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SRP_ID_INVALID"){
                    PySrpIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SRP_PASSWORD_CHANGED"){
                    PySrpPasswordChangedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("START_PARAM_EMPTY"){
                    PyStartParamEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("START_PARAM_INVALID"){
                    PyStartParamInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("START_PARAM_TOO_LONG"){
                    PyStartParamTooLongError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKERPACK_STICKERS_TOO_MUCH"){
                    PyStickerpackStickersTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKERSET_INVALID"){
                    PyStickersetInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKERS_EMPTY"){
                    PyStickersEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKERS_TOO_MUCH"){
                    PyStickersTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_DOCUMENT_INVALID"){
                    PyStickerDocumentInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_EMOJI_INVALID"){
                    PyStickerEmojiInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_FILE_INVALID"){
                    PyStickerFileInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_GIF_DIMENSIONS"){
                    PyStickerGifDimensionsError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_ID_INVALID"){
                    PyStickerIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_INVALID"){
                    PyStickerInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_MIME_INVALID"){
                    PyStickerMimeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_PNG_DIMENSIONS"){
                    PyStickerPngDimensionsError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_PNG_NOPNG"){
                    PyStickerPngNopngError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_TGS_NODOC"){
                    PyStickerTgsNodocError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_TGS_NOTGS"){
                    PyStickerTgsNotgsError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_THUMB_PNG_NOPNG"){
                    PyStickerThumbPngNopngError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_THUMB_TGS_NOTGS"){
                    PyStickerThumbTgsNotgsError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_VIDEO_BIG"){
                    PyStickerVideoBigError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_VIDEO_NODOC"){
                    PyStickerVideoNodocError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKER_VIDEO_NOWEBM"){
                    PyStickerVideoNowebmError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SWITCH_PM_TEXT_EMPTY"){
                    PySwitchPmTextEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TAKEOUT_INVALID"){
                    PyTakeoutInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TAKEOUT_REQUIRED"){
                    PyTakeoutRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TEMP_AUTH_KEY_ALREADY_BOUND"){
                    PyTempAuthKeyAlreadyBoundError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TEMP_AUTH_KEY_EMPTY"){
                    PyTempAuthKeyEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("THEME_FILE_INVALID"){
                    PyThemeFileInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("THEME_FORMAT_INVALID"){
                    PyThemeFormatInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("THEME_INVALID"){
                    PyThemeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("THEME_MIME_INVALID"){
                    PyThemeMimeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("THEME_TITLE_INVALID"){
                    PyThemeTitleInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TITLE_INVALID"){
                    PyTitleInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TMP_PASSWORD_DISABLED"){
                    PyTmpPasswordDisabledError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TMP_PASSWORD_INVALID"){
                    PyTmpPasswordInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TOKEN_INVALID"){
                    PyTokenInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TOPIC_DELETED"){
                    PyTopicDeletedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TO_LANG_INVALID"){
                    PyToLangInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TTL_DAYS_INVALID"){
                    PyTtlDaysInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TTL_MEDIA_INVALID"){
                    PyTtlMediaInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TTL_PERIOD_INVALID"){
                    PyTtlPeriodInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TYPES_EMPTY"){
                    PyTypesEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TYPE_CONSTRUCTOR_INVALID"){
                    PyTypeConstructorInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("UNKNOWN_ERROR"){
                    PyUnknownErrorError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("UNTIL_DATE_INVALID"){
                    PyUntilDateInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("URL_INVALID"){
                    PyUrlInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USAGE_LIMIT_INVALID"){
                    PyUsageLimitInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USERNAME_INVALID"){
                    PyUsernameInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USERNAME_NOT_MODIFIED"){
                    PyUsernameNotModifiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USERNAME_NOT_OCCUPIED"){
                    PyUsernameNotOccupiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USERNAME_OCCUPIED"){
                    PyUsernameOccupiedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USERNAME_PURCHASE_AVAILABLE"){
                    PyUsernamePurchaseAvailableError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USERPIC_UPLOAD_REQUIRED"){
                    PyUserpicUploadRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USERS_TOO_FEW"){
                    PyUsersTooFewError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USERS_TOO_MUCH"){
                    PyUsersTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_ADMIN_INVALID"){
                    PyUserAdminInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_ALREADY_INVITED"){
                    PyUserAlreadyInvitedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_ALREADY_PARTICIPANT"){
                    PyUserAlreadyParticipantError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_BANNED_IN_CHANNEL"){
                    PyUserBannedInChannelError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_BLOCKED"){
                    PyUserBlockedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_BOT"){
                    PyUserBotError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_BOT_INVALID"){
                    PyUserBotInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_BOT_REQUIRED"){
                    PyUserBotRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_CHANNELS_TOO_MUCH"){
                    PyUserChannelsTooMuchError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_CREATOR"){
                    PyUserCreatorError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_ID_INVALID"){
                    PyUserIdInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_INVALID"){
                    PyUserInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_IS_BLOCKED"){
                    PyUserIsBlockedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_IS_BOT"){
                    PyUserIsBotError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_KICKED"){
                    PyUserKickedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_NOT_MUTUAL_CONTACT"){
                    PyUserNotMutualContactError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_NOT_PARTICIPANT"){
                    PyUserNotParticipantError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_VOLUME_INVALID"){
                    PyUserVolumeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("VIDEO_CONTENT_TYPE_INVALID"){
                    PyVideoContentTypeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("VIDEO_FILE_INVALID"){
                    PyVideoFileInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("VIDEO_TITLE_EMPTY"){
                    PyVideoTitleEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("VOICE_MESSAGES_FORBIDDEN"){
                    PyVoiceMessagesForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WALLPAPER_FILE_INVALID"){
                    PyWallpaperFileInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WALLPAPER_INVALID"){
                    PyWallpaperInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WALLPAPER_MIME_INVALID"){
                    PyWallpaperMimeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WC_CONVERT_URL_INVALID"){
                    PyWcConvertUrlInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WEBDOCUMENT_INVALID"){
                    PyWebdocumentInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WEBDOCUMENT_MIME_INVALID"){
                    PyWebdocumentMimeInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WEBDOCUMENT_SIZE_TOO_BIG"){
                    PyWebdocumentSizeTooBigError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WEBDOCUMENT_URL_INVALID"){
                    PyWebdocumentUrlInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WEBPAGE_CURL_FAILED"){
                    PyWebpageCurlFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WEBPAGE_MEDIA_EMPTY"){
                    PyWebpageMediaEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WEBPUSH_AUTH_INVALID"){
                    PyWebpushAuthInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WEBPUSH_KEY_INVALID"){
                    PyWebpushKeyInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WEBPUSH_TOKEN_INVALID"){
                    PyWebpushTokenInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("YOU_BLOCKED_USER"){
                    PyYouBlockedUserError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FROZEN_PARTICIPANT_MISSING"){
                    PyFrozenParticipantMissingError::new_err(e.name, e.value, e.caused_by)
                } else {
                    PyBadRequestError::new_err(e.name, e.value, e.caused_by, None)
                },
                401 => if e.is("ACTIVE_USER_REQUIRED"){
                    PyActiveUserRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUTH_KEY_INVALID"){
                    PyAuthKeyInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUTH_KEY_PERM_EMPTY"){
                    PyAuthKeyPermEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("AUTH_KEY_UNREGISTERED"){
                    PyAuthKeyUnregisteredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SESSION_EXPIRED"){
                    PySessionExpiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SESSION_PASSWORD_NEEDED"){
                    PySessionPasswordNeededError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SESSION_REVOKED"){
                    PySessionRevokedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_DEACTIVATED"){
                    PyUserDeactivatedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_DEACTIVATED_BAN"){
                    PyUserDeactivatedBanError::new_err(e.name, e.value, e.caused_by)
                } else {
                    PyUnauthorizedError::new_err(e.name, e.value, e.caused_by, None)
                },
                403 => if e.is("BROADCAST_FORBIDDEN"){
                    PyBroadcastForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHANNEL_PUBLIC_GROUP_NA"){
                    PyChannelPublicGroupNaError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_ADMIN_INVITE_REQUIRED"){
                    PyChatAdminInviteRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_FORBIDDEN"){
                    PyChatForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_GUEST_SEND_FORBIDDEN"){
                    PyChatGuestSendForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_SEND_GAME_FORBIDDEN"){
                    PyChatSendGameForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_SEND_GIFS_FORBIDDEN"){
                    PyChatSendGifsForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_SEND_MEDIA_FORBIDDEN"){
                    PyChatSendMediaForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_SEND_POLL_FORBIDDEN"){
                    PyChatSendPollForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_SEND_STICKERS_FORBIDDEN"){
                    PyChatSendStickersForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_WRITE_FORBIDDEN"){
                    PyChatWriteForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("EDIT_BOT_INVITE_FORBIDDEN"){
                    PyEditBotInviteForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GROUPCALL_ALREADY_STARTED"){
                    PyGroupcallAlreadyStartedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GROUPCALL_FORBIDDEN"){
                    PyGroupcallForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INLINE_BOT_REQUIRED"){
                    PyInlineBotRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MESSAGE_AUTHOR_REQUIRED"){
                    PyMessageAuthorRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MESSAGE_DELETE_FORBIDDEN"){
                    PyMessageDeleteForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("NOT_ALLOWED"){
                    PyNotAllowedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("POLL_VOTE_REQUIRED"){
                    PyPollVoteRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PREMIUM_ACCOUNT_REQUIRED"){
                    PyPremiumAccountRequiredError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PUBLIC_CHANNEL_MISSING"){
                    PyPublicChannelMissingError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RIGHT_FORBIDDEN"){
                    PyRightForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SENSITIVE_CHANGE_FORBIDDEN"){
                    PySensitiveChangeForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_DELETED"){
                    PyUserDeletedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_PRIVACY_RESTRICTED"){
                    PyUserPrivacyRestrictedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USER_RESTRICTED"){
                    PyUserRestrictedError::new_err(e.name, e.value, e.caused_by)
                } else {
                    PyForbiddenError::new_err(e.name, e.value, e.caused_by, None)
                },
                404 => PyNotFoundError::new_err(e.name, e.value, e.caused_by, None),
                406 => if e.is("AUTH_KEY_DUPLICATED"){
                    PyAuthKeyDuplicatedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FILEREF_UPGRADE_NEEDED"){
                    PyFilerefUpgradeNeededError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FRESH_CHANGE_PHONE_FORBIDDEN"){
                    PyFreshChangePhoneForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FRESH_RESET_AUTHORISATION_FORBIDDEN"){
                    PyFreshResetAuthorisationForbiddenError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PHONE_PASSWORD_FLOOD"){
                    PyPhonePasswordFloodError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PREMIUM_CURRENTLY_UNAVAILABLE"){
                    PyPremiumCurrentlyUnavailableError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PREVIOUS_CHAT_IMPORT_ACTIVE_WAIT_*MIN"){
                    PyPreviousChatImportActiveWaitMinError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SEND_CODE_UNAVAILABLE"){
                    PySendCodeUnavailableError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STICKERSET_OWNER_ANONYMOUS"){
                    PyStickersetOwnerAnonymousError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("UPDATE_APP_TO_LOGIN"){
                    PyUpdateAppToLoginError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("USERPIC_PRIVACY_REQUIRED"){
                    PyUserpicPrivacyRequiredError::new_err(e.name, e.value, e.caused_by)
                } else {
                    PyAuthKeyError::new_err(e.name, e.value, e.caused_by, None)
                },
                420 => if e.is("2FA_CONFIRM_WAIT_*"){
                    PyTwoFaConfirmWaitError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FLOOD_TEST_PHONE_WAIT_*"){
                    PyFloodTestPhoneWaitError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FLOOD_WAIT_*"){
                    PyFloodWaitError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FLOOD_PREMIUM_WAIT_*"){
                    PyFloodPremiumWaitError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SLOWMODE_WAIT_*"){
                    PySlowModeWaitError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("TAKEOUT_INIT_DELAY_*"){
                    PyTakeoutInitDelayError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("FROZEN_METHOD_INVALID"){
                    PyFrozenMethodInvalidError::new_err(e.name, e.value, e.caused_by)
                } else {
                    PyFloodError::new_err(e.name, e.value, e.caused_by, None)
                },
                500 | -500 => if e.is("AUTH_RESTART"){
                    PyAuthRestartError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CALL_OCCUPY_FAILED"){
                    PyCallOccupyFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CDN_UPLOAD_TIMEOUT"){
                    PyCdnUploadTimeoutError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_GET_FAILED"){
                    PyChatGetFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHAT_ID_GENERATE_FAILED"){
                    PyChatIdGenerateFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("CHP_CALL_FAIL"){
                    PyChpCallFailError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("ENCRYPTION_OCCUPY_FAILED"){
                    PyEncryptionOccupyFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("GROUPCALL_ADD_PARTICIPANTS_FAILED"){
                    PyGroupcallAddParticipantsFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("HISTORY_GET_FAILED"){
                    PyHistoryGetFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INTERDC_*_CALL_ERROR"){
                    PyInterdcCallErrorError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("INTERDC_*_CALL_RICH_ERROR"){
                    PyInterdcCallRichErrorError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MEMBER_NO_LOCATION"){
                    PyMemberNoLocationError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MEMBER_OCCUPY_PRIMARY_LOC_FAILED"){
                    PyMemberOccupyPrimaryLocFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MSGID_DECREASE_RETRY"){
                    PyMsgidDecreaseRetryError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("MT_SEND_QUEUE_TOO_LONG"){
                    PyMtSendQueueTooLongError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("NEED_CHAT_INVALID"){
                    PyNeedChatInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("NEED_MEMBER_INVALID"){
                    PyNeedMemberInvalidError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PARTICIPANT_CALL_FAILED"){
                    PyParticipantCallFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PERSISTENT_TIMESTAMP_OUTDATED"){
                    PyPersistentTimestampOutdatedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("POSTPONED_TIMEOUT"){
                    PyPostponedTimeoutError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("PTS_CHANGE_EMPTY"){
                    PyPtsChangeEmptyError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RANDOM_ID_DUPLICATE"){
                    PyRandomIdDuplicateError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("REG_ID_GENERATE_FAILED"){
                    PyRegIdGenerateFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RPC_CALL_FAIL"){
                    PyRpcCallFailError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("RPC_MCGET_FAIL"){
                    PyRpcMcgetFailError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("SIGN_IN_FAILED"){
                    PySignInFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STORAGE_CHECK_FAILED"){
                    PyStorageCheckFailedError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("STORE_INVALID_SCALAR_TYPE"){
                    PyStoreInvalidScalarTypeError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("UNKNOWN_METHOD"){
                    PyUnknownMethodError::new_err(e.name, e.value, e.caused_by)
                } else if e.is("WORKER_BUSY_TOO_LONG_RETRY"){
                    PyWorkerBusyTooLongRetryError::new_err(e.name, e.value, e.caused_by)
                } else {
                    PyServerError::new_err(e.name, e.value, e.caused_by, None)
                },
                503 | -503 => PyTimedOutError::new_err(e.name, e.value, e.caused_by, None),
                _ => PyRpcError::new_err(e.code, e.name, e.value, e.caused_by, None),
            },
            InvocationError::Io(e) => PyIOError::new_err(e.to_string()),
            InvocationError::Deserialize(e) => DeserializeError::new_err(e.to_string()),
            InvocationError::Transport(e) => TransportError::new_err(e.to_string()),
            InvocationError::Dropped => DroppedError::new_err(
                "Client runner not start, and the sent data packet dropped. Pleace re-create Client() to restart.".to_string(),
            ),
            InvocationError::InvalidDc(dc_id) => PyInvalidDCError::new_err(
                "INVALID_DC".to_string(), 
                None,
                None,
                Some(format!(
                    "Session returns no infomation of the provided dc_id '{}'",
                    dc_id,
                )),
            ),
            InvocationError::Authentication(e) => {
                PyRuntimeError::new_err(format!("Authentication: {}", e))
            }
            InvocationError::PyErr(e) => e,
        }
    }
}

#[pyclass(name = "SignInError", module = "grammers.errors", extends = PyException, subclass)]
pub struct SignInError {
    #[pyo3(get)]
    message: String,
}

#[pymethods]
impl SignInError {
    #[new]
    fn new(message: String) -> Self {
        SignInError { message }
    }

    fn __str__(&self) -> String {
        self.message.clone()
    }

    fn __repr__(slf: &Bound<'_, Self>) -> PyResult<String> {
        let cls_name = slf.get_type().qualname()?;
        let message = slf.getattr("message")?;
        Ok(format!("{}(message={})", cls_name, message))
    }
}
/*
impl SignInError {
    pub fn new_err(message: &str) -> PyErr {
        PyErr::new::<SignInError, _>((message.to_string(),))
    }
}*/

#[pyclass(name = "SignUpRequiredError", module = "grammers.errors", extends = SignInError)]
pub struct SignUpRequiredError {}

#[pymethods]
impl SignUpRequiredError {
    #[new]
    fn new() -> (Self, SignInError) {
        (
            SignUpRequiredError {},
            SignInError {
                message: "Sign-up with an official client is required. (Third-party applications cannot sign up for Telegram.)".into()
            }
        )
    }
}
impl SignUpRequiredError {
    pub fn new_err() -> PyErr {
        PyErr::new::<SignUpRequiredError, _>(())
    }
}

#[pyclass(name = "PasswordRequiredError", module = "grammers.errors", extends = SignInError)]
pub struct PasswordRequiredError {
    #[pyo3(get)]
    pub password_token: Py<pytl::types::account::PyPassword>,
}

#[pymethods]
impl PasswordRequiredError {
    #[new]
    fn new(password_token: Py<pytl::types::account::PyPassword>) -> (Self, SignInError) {
        (
            PasswordRequiredError { password_token },
            SignInError {
                message: "The account has 2FA enabled, and the password is required.".into(),
            },
        )
    }

    fn __repr__(&self) -> PyResult<String> {
        let password_token = Python::attach(|py| {
            let p = self.password_token.bind(py);
            pytl::TLObject::pretty_format(&p, Some(1))
        })?;
        Ok(format!(
            "PasswordRequiredError(\n  password_token={},\n  message={},\n)",
            password_token, "'The account has 2FA enabled, and the password is required.'",
        ))
    }
}
impl PasswordRequiredError {
    pub fn new_err(password_token: Py<pytl::types::account::PyPassword>) -> PyErr {
        PyErr::new::<PasswordRequiredError, _>((password_token,))
    }
}

#[pyclass(name = "InvalidCodeError", module = "grammers.errors", extends = SignInError)]
pub struct InvalidCodeError {}

#[pymethods]
impl InvalidCodeError {
    #[new]
    fn new() -> (Self, SignInError) {
        (
            Self {},
            SignInError {
                message: "The code used to complete login was not valid.".into(),
            },
        )
    }
}
impl InvalidCodeError {
    pub fn new_err() -> PyErr {
        PyErr::new::<InvalidCodeError, _>(())
    }
}

#[pyclass(name = "InvalidPasswordError", module = "grammers.errors", extends = SignInError)]
pub struct InvalidPasswordError {
    #[pyo3(get)]
    pub password_token: Py<pytl::types::account::PyPassword>,
}

#[pymethods]
impl InvalidPasswordError {
    #[new]
    fn new(password_token: Py<pytl::types::account::PyPassword>) -> (Self, SignInError) {
        (
            InvalidPasswordError { password_token },
            SignInError {
                message: "The code used to complete login was not valid.".into(),
            },
        )
    }

    fn __repr__(&self) -> PyResult<String> {
        let password_token = Python::attach(|py| {
            let p = self.password_token.bind(py);
            pytl::TLObject::pretty_format(&p, Some(1))
        })?;
        Ok(format!(
            "InvalidPasswordError(\n  password_token={},\n  message={},\n)",
            password_token, "'The code used to complete login was not valid.'",
        ))
    }
}
impl InvalidPasswordError {
    pub fn new_err(password_token: Py<pytl::types::account::PyPassword>) -> PyErr {
        PyErr::new::<InvalidPasswordError, _>((password_token,))
    }
}
