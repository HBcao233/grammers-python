mod common;
mod macros;
mod rpcbaseerrors;
mod rpcerrorlist;

pub use common::PyInvocationError;
use common::{DeserializeError, DroppedError, TransportError};

pub use rpcbaseerrors::{
    PyAuthKeyError, PyBadRequestError, PyFloodError, PyForbiddenError, PyInvalidDCError,
    PyNotFoundError, PyRpcError, PyServerError, PyTimedOutError, PyUnauthorizedError,
};
pub use rpcerrorlist::*;

#[pyo3::pymodule(name = "errors")]
pub mod errors_ {
    #[pymodule_export]
    use super::DroppedError;

    #[pymodule_export]
    use super::DeserializeError;

    #[pymodule_export]
    use super::TransportError;

    // ===== rpcbaseerrors =====
    #[pymodule_export]
    use super::PyRpcError;

    #[pymodule_export]
    use super::PyInvalidDCError;

    #[pymodule_export]
    use super::PyBadRequestError;

    #[pymodule_export]
    use super::PyUnauthorizedError;

    #[pymodule_export]
    use super::PyForbiddenError;

    #[pymodule_export]
    use super::PyNotFoundError;

    #[pymodule_export]
    use super::PyAuthKeyError;

    #[pymodule_export]
    use super::PyFloodError;

    #[pymodule_export]
    use super::PyServerError;

    #[pymodule_export]
    use super::PyTimedOutError;

    // ===== rpcerrorlist =====

    #[pymodule_export]
    use super::PyTwoFaConfirmWaitError;

    #[pymodule_export]
    use super::PyAboutTooLongError;

    #[pymodule_export]
    use super::PyAccessTokenExpiredError;

    #[pymodule_export]
    use super::PyAccessTokenInvalidError;

    #[pymodule_export]
    use super::PyActiveUserRequiredError;

    #[pymodule_export]
    use super::PyAdminsTooMuchError;

    #[pymodule_export]
    use super::PyAdminIdInvalidError;

    #[pymodule_export]
    use super::PyAdminRankEmojiNotAllowedError;

    #[pymodule_export]
    use super::PyAdminRankInvalidError;

    #[pymodule_export]
    use super::PyAlbumPhotosTooManyError;

    #[pymodule_export]
    use super::PyApiIdInvalidError;

    #[pymodule_export]
    use super::PyApiIdPublishedFloodError;

    #[pymodule_export]
    use super::PyArticleTitleEmptyError;

    #[pymodule_export]
    use super::PyAudioContentUrlEmptyError;

    #[pymodule_export]
    use super::PyAudioTitleEmptyError;

    #[pymodule_export]
    use super::PyAuthBytesInvalidError;

    #[pymodule_export]
    use super::PyAuthKeyDuplicatedError;

    #[pymodule_export]
    use super::PyAuthKeyInvalidError;

    #[pymodule_export]
    use super::PyAuthKeyPermEmptyError;

    #[pymodule_export]
    use super::PyAuthKeyUnregisteredError;

    #[pymodule_export]
    use super::PyAuthRestartError;

    #[pymodule_export]
    use super::PyAuthTokenAlreadyAcceptedError;

    #[pymodule_export]
    use super::PyAuthTokenExceptionError;

    #[pymodule_export]
    use super::PyAuthTokenExpiredError;

    #[pymodule_export]
    use super::PyAuthTokenInvalidError;

    #[pymodule_export]
    use super::PyAuthTokenInvalid2Error;

    #[pymodule_export]
    use super::PyAuthTokenInvalidxError;

    #[pymodule_export]
    use super::PyAutoarchiveNotAvailableError;

    #[pymodule_export]
    use super::PyBankCardNumberInvalidError;

    #[pymodule_export]
    use super::PyBannedRightsInvalidError;

    #[pymodule_export]
    use super::PyBasePortLocInvalidError;

    #[pymodule_export]
    use super::PyBotsTooMuchError;

    #[pymodule_export]
    use super::PyBotChannelsNaError;

    #[pymodule_export]
    use super::PyBotCommandDescriptionInvalidError;

    #[pymodule_export]
    use super::PyBotCommandInvalidError;

    #[pymodule_export]
    use super::PyBotDomainInvalidError;

    #[pymodule_export]
    use super::PyBotGamesDisabledError;

    #[pymodule_export]
    use super::PyBotGroupsBlockedError;

    #[pymodule_export]
    use super::PyBotInlineDisabledError;

    #[pymodule_export]
    use super::PyBotInvalidError;

    #[pymodule_export]
    use super::PyBotMethodInvalidError;

    #[pymodule_export]
    use super::PyBotMissingError;

    #[pymodule_export]
    use super::PyBotOnesideNotAvailError;

    #[pymodule_export]
    use super::PyBotPaymentsDisabledError;

    #[pymodule_export]
    use super::PyBotPollsDisabledError;

    #[pymodule_export]
    use super::PyBotResponseTimeoutError;

    #[pymodule_export]
    use super::PyBotScoreNotModifiedError;

    #[pymodule_export]
    use super::PyBroadcastCallsDisabledError;

    #[pymodule_export]
    use super::PyBroadcastForbiddenError;

    #[pymodule_export]
    use super::PyBroadcastIdInvalidError;

    #[pymodule_export]
    use super::PyBroadcastPublicVotersForbiddenError;

    #[pymodule_export]
    use super::PyBroadcastRequiredError;

    #[pymodule_export]
    use super::PyButtonDataInvalidError;

    #[pymodule_export]
    use super::PyButtonTextInvalidError;

    #[pymodule_export]
    use super::PyButtonTypeInvalidError;

    #[pymodule_export]
    use super::PyButtonUrlInvalidError;

    #[pymodule_export]
    use super::PyButtonUserPrivacyRestrictedError;

    #[pymodule_export]
    use super::PyCallAlreadyAcceptedError;

    #[pymodule_export]
    use super::PyCallAlreadyDeclinedError;

    #[pymodule_export]
    use super::PyCallOccupyFailedError;

    #[pymodule_export]
    use super::PyCallPeerInvalidError;

    #[pymodule_export]
    use super::PyCallProtocolFlagsInvalidError;

    #[pymodule_export]
    use super::PyCdnMethodInvalidError;

    #[pymodule_export]
    use super::PyCdnUploadTimeoutError;

    #[pymodule_export]
    use super::PyChannelsAdminLocatedTooMuchError;

    #[pymodule_export]
    use super::PyChannelsAdminPublicTooMuchError;

    #[pymodule_export]
    use super::PyChannelsTooMuchError;

    #[pymodule_export]
    use super::PyChannelBannedError;

    #[pymodule_export]
    use super::PyChannelForumMissingError;

    #[pymodule_export]
    use super::PyChannelIdInvalidError;

    #[pymodule_export]
    use super::PyChannelInvalidError;

    #[pymodule_export]
    use super::PyChannelParicipantMissingError;

    #[pymodule_export]
    use super::PyChannelPrivateError;

    #[pymodule_export]
    use super::PyChannelPublicGroupNaError;

    #[pymodule_export]
    use super::PyChannelTooBigError;

    #[pymodule_export]
    use super::PyChannelTooLargeError;

    #[pymodule_export]
    use super::PyChatAboutNotModifiedError;

    #[pymodule_export]
    use super::PyChatAboutTooLongError;

    #[pymodule_export]
    use super::PyChatAdminInviteRequiredError;

    #[pymodule_export]
    use super::PyChatAdminRequiredError;

    #[pymodule_export]
    use super::PyChatDiscussionUnallowedError;

    #[pymodule_export]
    use super::PyChatForbiddenError;

    #[pymodule_export]
    use super::PyChatForwardsRestrictedError;

    #[pymodule_export]
    use super::PyChatGetFailedError;

    #[pymodule_export]
    use super::PyChatGuestSendForbiddenError;

    #[pymodule_export]
    use super::PyChatIdEmptyError;

    #[pymodule_export]
    use super::PyChatIdGenerateFailedError;

    #[pymodule_export]
    use super::PyChatIdInvalidError;

    #[pymodule_export]
    use super::PyChatInvalidError;

    #[pymodule_export]
    use super::PyChatInvitePermanentError;

    #[pymodule_export]
    use super::PyChatLinkExistsError;

    #[pymodule_export]
    use super::PyChatNotModifiedError;

    #[pymodule_export]
    use super::PyChatRestrictedError;

    #[pymodule_export]
    use super::PyChatRevokeDateUnsupportedError;

    #[pymodule_export]
    use super::PyChatSendGameForbiddenError;

    #[pymodule_export]
    use super::PyChatSendGifsForbiddenError;

    #[pymodule_export]
    use super::PyChatSendInlineForbiddenError;

    #[pymodule_export]
    use super::PyChatSendMediaForbiddenError;

    #[pymodule_export]
    use super::PyChatSendPollForbiddenError;

    #[pymodule_export]
    use super::PyChatSendStickersForbiddenError;

    #[pymodule_export]
    use super::PyChatTitleEmptyError;

    #[pymodule_export]
    use super::PyChatTooBigError;

    #[pymodule_export]
    use super::PyChatWriteForbiddenError;

    #[pymodule_export]
    use super::PyChpCallFailError;

    #[pymodule_export]
    use super::PyCodeEmptyError;

    #[pymodule_export]
    use super::PyCodeHashInvalidError;

    #[pymodule_export]
    use super::PyCodeInvalidError;

    #[pymodule_export]
    use super::PyConnectionApiIdInvalidError;

    #[pymodule_export]
    use super::PyConnectionAppVersionEmptyError;

    #[pymodule_export]
    use super::PyConnectionDeviceModelEmptyError;

    #[pymodule_export]
    use super::PyConnectionLangPackInvalidError;

    #[pymodule_export]
    use super::PyConnectionLayerInvalidError;

    #[pymodule_export]
    use super::PyConnectionNotInitedError;

    #[pymodule_export]
    use super::PyConnectionSystemEmptyError;

    #[pymodule_export]
    use super::PyConnectionSystemLangCodeEmptyError;

    #[pymodule_export]
    use super::PyContactAddMissingError;

    #[pymodule_export]
    use super::PyContactIdInvalidError;

    #[pymodule_export]
    use super::PyContactNameEmptyError;

    #[pymodule_export]
    use super::PyContactReqMissingError;

    #[pymodule_export]
    use super::PyCreateCallFailedError;

    #[pymodule_export]
    use super::PyCurrencyTotalAmountInvalidError;

    #[pymodule_export]
    use super::PyDataInvalidError;

    #[pymodule_export]
    use super::PyDataJsonInvalidError;

    #[pymodule_export]
    use super::PyDataTooLongError;

    #[pymodule_export]
    use super::PyDateEmptyError;

    #[pymodule_export]
    use super::PyDcIdInvalidError;

    #[pymodule_export]
    use super::PyDhGAInvalidError;

    #[pymodule_export]
    use super::PyDocumentInvalidError;

    #[pymodule_export]
    use super::PyEditBotInviteForbiddenError;

    #[pymodule_export]
    use super::PyEmailHashExpiredError;

    #[pymodule_export]
    use super::PyEmailInvalidError;

    #[pymodule_export]
    use super::PyEmailUnconfirmedError;

    #[pymodule_export]
    use super::PyEmailVerifyExpiredError;

    #[pymodule_export]
    use super::PyEmojiInvalidError;

    #[pymodule_export]
    use super::PyEmojiNotModifiedError;

    #[pymodule_export]
    use super::PyEmoticonEmptyError;

    #[pymodule_export]
    use super::PyEmoticonInvalidError;

    #[pymodule_export]
    use super::PyEmoticonStickerpackMissingError;

    #[pymodule_export]
    use super::PyEncryptedMessageInvalidError;

    #[pymodule_export]
    use super::PyEncryptionAlreadyAcceptedError;

    #[pymodule_export]
    use super::PyEncryptionAlreadyDeclinedError;

    #[pymodule_export]
    use super::PyEncryptionDeclinedError;

    #[pymodule_export]
    use super::PyEncryptionIdInvalidError;

    #[pymodule_export]
    use super::PyEncryptionOccupyFailedError;

    #[pymodule_export]
    use super::PyEntitiesTooLongError;

    #[pymodule_export]
    use super::PyEntityBoundsInvalidError;

    #[pymodule_export]
    use super::PyEntityMentionUserInvalidError;

    #[pymodule_export]
    use super::PyErrorTextEmptyError;

    #[pymodule_export]
    use super::PyExpireDateInvalidError;

    #[pymodule_export]
    use super::PyExpireForbiddenError;

    #[pymodule_export]
    use super::PyExportCardInvalidError;

    #[pymodule_export]
    use super::PyExternalUrlInvalidError;

    #[pymodule_export]
    use super::PyFieldNameEmptyError;

    #[pymodule_export]
    use super::PyFieldNameInvalidError;

    #[pymodule_export]
    use super::PyFilerefUpgradeNeededError;

    #[pymodule_export]
    use super::PyFileContentTypeInvalidError;

    #[pymodule_export]
    use super::PyFileEmtpyError;

    #[pymodule_export]
    use super::PyFileIdInvalidError;

    #[pymodule_export]
    use super::PyFileMigrateError;

    #[pymodule_export]
    use super::PyFilePartsInvalidError;

    #[pymodule_export]
    use super::PyFilePart0MissingError;

    #[pymodule_export]
    use super::PyFilePartEmptyError;

    #[pymodule_export]
    use super::PyFilePartInvalidError;

    #[pymodule_export]
    use super::PyFilePartLengthInvalidError;

    #[pymodule_export]
    use super::PyFilePartSizeChangedError;

    #[pymodule_export]
    use super::PyFilePartSizeInvalidError;

    #[pymodule_export]
    use super::PyFilePartTooBigError;

    #[pymodule_export]
    use super::PyFilePartMissingError;

    #[pymodule_export]
    use super::PyFileReferenceEmptyError;

    #[pymodule_export]
    use super::PyFileReferenceExpiredError;

    #[pymodule_export]
    use super::PyFileReferenceInvalidError;

    #[pymodule_export]
    use super::PyFileTitleEmptyError;

    #[pymodule_export]
    use super::PyFilterIdInvalidError;

    #[pymodule_export]
    use super::PyFilterIncludeEmptyError;

    #[pymodule_export]
    use super::PyFilterNotSupportedError;

    #[pymodule_export]
    use super::PyFilterTitleEmptyError;

    #[pymodule_export]
    use super::PyFirstNameInvalidError;

    #[pymodule_export]
    use super::PyFloodTestPhoneWaitError;

    #[pymodule_export]
    use super::PyFloodWaitError;

    #[pymodule_export]
    use super::PyFloodPremiumWaitError;

    #[pymodule_export]
    use super::PyFolderIdEmptyError;

    #[pymodule_export]
    use super::PyFolderIdInvalidError;

    #[pymodule_export]
    use super::PyFreshChangeAdminsForbiddenError;

    #[pymodule_export]
    use super::PyFreshChangePhoneForbiddenError;

    #[pymodule_export]
    use super::PyFreshResetAuthorisationForbiddenError;

    #[pymodule_export]
    use super::PyFromMessageBotDisabledError;

    #[pymodule_export]
    use super::PyFromPeerInvalidError;

    #[pymodule_export]
    use super::PyGameBotInvalidError;

    #[pymodule_export]
    use super::PyGeoPointInvalidError;

    #[pymodule_export]
    use super::PyGifContentTypeInvalidError;

    #[pymodule_export]
    use super::PyGifIdInvalidError;

    #[pymodule_export]
    use super::PyGraphExpiredReloadError;

    #[pymodule_export]
    use super::PyGraphInvalidReloadError;

    #[pymodule_export]
    use super::PyGraphOutdatedReloadError;

    #[pymodule_export]
    use super::PyGroupcallAddParticipantsFailedError;

    #[pymodule_export]
    use super::PyGroupcallAlreadyDiscardedError;

    #[pymodule_export]
    use super::PyGroupcallAlreadyStartedError;

    #[pymodule_export]
    use super::PyGroupcallForbiddenError;

    #[pymodule_export]
    use super::PyGroupcallInvalidError;

    #[pymodule_export]
    use super::PyGroupcallJoinMissingError;

    #[pymodule_export]
    use super::PyGroupcallNotModifiedError;

    #[pymodule_export]
    use super::PyGroupcallSsrcDuplicateMuchError;

    #[pymodule_export]
    use super::PyGroupedMediaInvalidError;

    #[pymodule_export]
    use super::PyGroupCallInvalidError;

    #[pymodule_export]
    use super::PyHashInvalidError;

    #[pymodule_export]
    use super::PyHideRequesterMissingError;

    #[pymodule_export]
    use super::PyHistoryGetFailedError;

    #[pymodule_export]
    use super::PyImageProcessFailedError;

    #[pymodule_export]
    use super::PyImportFileInvalidError;

    #[pymodule_export]
    use super::PyImportFormatUnrecognizedError;

    #[pymodule_export]
    use super::PyImportIdInvalidError;

    #[pymodule_export]
    use super::PyInlineBotRequiredError;

    #[pymodule_export]
    use super::PyInlineResultExpiredError;

    #[pymodule_export]
    use super::PyInputConstructorInvalidError;

    #[pymodule_export]
    use super::PyInputFetchErrorError;

    #[pymodule_export]
    use super::PyInputFetchFailError;

    #[pymodule_export]
    use super::PyInputFilterInvalidError;

    #[pymodule_export]
    use super::PyInputLayerInvalidError;

    #[pymodule_export]
    use super::PyInputMethodInvalidError;

    #[pymodule_export]
    use super::PyInputRequestTooLongError;

    #[pymodule_export]
    use super::PyInputTextEmptyError;

    #[pymodule_export]
    use super::PyInputUserDeactivatedError;

    #[pymodule_export]
    use super::PyInterdcCallErrorError;

    #[pymodule_export]
    use super::PyInterdcCallRichErrorError;

    #[pymodule_export]
    use super::PyInviteForbiddenWithJoinasError;

    #[pymodule_export]
    use super::PyInviteHashEmptyError;

    #[pymodule_export]
    use super::PyInviteHashExpiredError;

    #[pymodule_export]
    use super::PyInviteHashInvalidError;

    #[pymodule_export]
    use super::PyInviteRequestSentError;

    #[pymodule_export]
    use super::PyInviteRevokedMissingError;

    #[pymodule_export]
    use super::PyInvoicePayloadInvalidError;

    #[pymodule_export]
    use super::PyJoinAsPeerInvalidError;

    #[pymodule_export]
    use super::PyLangCodeInvalidError;

    #[pymodule_export]
    use super::PyLangCodeNotSupportedError;

    #[pymodule_export]
    use super::PyLangPackInvalidError;

    #[pymodule_export]
    use super::PyLastnameInvalidError;

    #[pymodule_export]
    use super::PyLimitInvalidError;

    #[pymodule_export]
    use super::PyLinkNotModifiedError;

    #[pymodule_export]
    use super::PyLocationInvalidError;

    #[pymodule_export]
    use super::PyMaxDateInvalidError;

    #[pymodule_export]
    use super::PyMaxIdInvalidError;

    #[pymodule_export]
    use super::PyMaxQtsInvalidError;

    #[pymodule_export]
    use super::PyMd5ChecksumInvalidError;

    #[pymodule_export]
    use super::PyMediaCaptionTooLongError;

    #[pymodule_export]
    use super::PyMediaEmptyError;

    #[pymodule_export]
    use super::PyMediaGroupedInvalidError;

    #[pymodule_export]
    use super::PyMediaInvalidError;

    #[pymodule_export]
    use super::PyMediaNewInvalidError;

    #[pymodule_export]
    use super::PyMediaPrevInvalidError;

    #[pymodule_export]
    use super::PyMediaTtlInvalidError;

    #[pymodule_export]
    use super::PyMegagroupIdInvalidError;

    #[pymodule_export]
    use super::PyMegagroupPrehistoryHiddenError;

    #[pymodule_export]
    use super::PyMegagroupRequiredError;

    #[pymodule_export]
    use super::PyMemberNoLocationError;

    #[pymodule_export]
    use super::PyMemberOccupyPrimaryLocFailedError;

    #[pymodule_export]
    use super::PyMessageAuthorRequiredError;

    #[pymodule_export]
    use super::PyMessageDeleteForbiddenError;

    #[pymodule_export]
    use super::PyMessageEditTimeExpiredError;

    #[pymodule_export]
    use super::PyMessageEmptyError;

    #[pymodule_export]
    use super::PyMessageIdsEmptyError;

    #[pymodule_export]
    use super::PyMessageIdInvalidError;

    #[pymodule_export]
    use super::PyMessageNotModifiedError;

    #[pymodule_export]
    use super::PyMessagePollClosedError;

    #[pymodule_export]
    use super::PyMessageTooLongError;

    #[pymodule_export]
    use super::PyMethodInvalidError;

    #[pymodule_export]
    use super::PyMinDateInvalidError;

    #[pymodule_export]
    use super::PyMsgidDecreaseRetryError;

    #[pymodule_export]
    use super::PyMsgIdInvalidError;

    #[pymodule_export]
    use super::PyMsgTooOldError;

    #[pymodule_export]
    use super::PyMsgWaitFailedError;

    #[pymodule_export]
    use super::PyMtSendQueueTooLongError;

    #[pymodule_export]
    use super::PyMultiMediaTooLongError;

    #[pymodule_export]
    use super::PyNeedChatInvalidError;

    #[pymodule_export]
    use super::PyNeedMemberInvalidError;

    #[pymodule_export]
    use super::PyNetworkMigrateError;

    #[pymodule_export]
    use super::PyNewSaltInvalidError;

    #[pymodule_export]
    use super::PyNewSettingsEmptyError;

    #[pymodule_export]
    use super::PyNewSettingsInvalidError;

    #[pymodule_export]
    use super::PyNextOffsetInvalidError;

    #[pymodule_export]
    use super::PyNotAllowedError;

    #[pymodule_export]
    use super::PyOffsetInvalidError;

    #[pymodule_export]
    use super::PyOffsetPeerIdInvalidError;

    #[pymodule_export]
    use super::PyOptionsTooMuchError;

    #[pymodule_export]
    use super::PyOptionInvalidError;

    #[pymodule_export]
    use super::PyPackShortNameInvalidError;

    #[pymodule_export]
    use super::PyPackShortNameOccupiedError;

    #[pymodule_export]
    use super::PyPackTitleInvalidError;

    #[pymodule_export]
    use super::PyParticipantsTooFewError;

    #[pymodule_export]
    use super::PyParticipantCallFailedError;

    #[pymodule_export]
    use super::PyParticipantIdInvalidError;

    #[pymodule_export]
    use super::PyParticipantJoinMissingError;

    #[pymodule_export]
    use super::PyParticipantVersionOutdatedError;

    #[pymodule_export]
    use super::PyPasswordEmptyError;

    #[pymodule_export]
    use super::PyPasswordHashInvalidError;

    #[pymodule_export]
    use super::PyPasswordMissingError;

    #[pymodule_export]
    use super::PyPasswordRecoveryExpiredError;

    #[pymodule_export]
    use super::PyPasswordRecoveryNaError;

    #[pymodule_export]
    use super::PyPasswordRequiredError;

    #[pymodule_export]
    use super::PyPasswordTooFreshError;

    #[pymodule_export]
    use super::PyPaymentProviderInvalidError;

    #[pymodule_export]
    use super::PyPeerFloodError;

    #[pymodule_export]
    use super::PyPeerHistoryEmptyError;

    #[pymodule_export]
    use super::PyPeerIdInvalidError;

    #[pymodule_export]
    use super::PyPeerIdNotSupportedError;

    #[pymodule_export]
    use super::PyPersistentTimestampEmptyError;

    #[pymodule_export]
    use super::PyPersistentTimestampInvalidError;

    #[pymodule_export]
    use super::PyPersistentTimestampOutdatedError;

    #[pymodule_export]
    use super::PyPhoneCodeEmptyError;

    #[pymodule_export]
    use super::PyPhoneCodeExpiredError;

    #[pymodule_export]
    use super::PyPhoneCodeHashEmptyError;

    #[pymodule_export]
    use super::PyPhoneCodeInvalidError;

    #[pymodule_export]
    use super::PyPhoneHashExpiredError;

    #[pymodule_export]
    use super::PyPhoneMigrateError;

    #[pymodule_export]
    use super::PyPhoneNotOccupiedError;

    #[pymodule_export]
    use super::PyPhoneNumberAppSignupForbiddenError;

    #[pymodule_export]
    use super::PyPhoneNumberBannedError;

    #[pymodule_export]
    use super::PyPhoneNumberFloodError;

    #[pymodule_export]
    use super::PyPhoneNumberInvalidError;

    #[pymodule_export]
    use super::PyPhoneNumberOccupiedError;

    #[pymodule_export]
    use super::PyPhoneNumberUnoccupiedError;

    #[pymodule_export]
    use super::PyPhonePasswordFloodError;

    #[pymodule_export]
    use super::PyPhonePasswordProtectedError;

    #[pymodule_export]
    use super::PyPhotoContentTypeInvalidError;

    #[pymodule_export]
    use super::PyPhotoContentUrlEmptyError;

    #[pymodule_export]
    use super::PyPhotoCropFileMissingError;

    #[pymodule_export]
    use super::PyPhotoCropSizeSmallError;

    #[pymodule_export]
    use super::PyPhotoExtInvalidError;

    #[pymodule_export]
    use super::PyPhotoFileMissingError;

    #[pymodule_export]
    use super::PyPhotoIdInvalidError;

    #[pymodule_export]
    use super::PyPhotoInvalidError;

    #[pymodule_export]
    use super::PyPhotoInvalidDimensionsError;

    #[pymodule_export]
    use super::PyPhotoSaveFileInvalidError;

    #[pymodule_export]
    use super::PyPhotoThumbUrlEmptyError;

    #[pymodule_export]
    use super::PyPinnedDialogsTooMuchError;

    #[pymodule_export]
    use super::PyPinRestrictedError;

    #[pymodule_export]
    use super::PyPollAnswersInvalidError;

    #[pymodule_export]
    use super::PyPollAnswerInvalidError;

    #[pymodule_export]
    use super::PyPollOptionDuplicateError;

    #[pymodule_export]
    use super::PyPollOptionInvalidError;

    #[pymodule_export]
    use super::PyPollQuestionInvalidError;

    #[pymodule_export]
    use super::PyPollUnsupportedError;

    #[pymodule_export]
    use super::PyPollVoteRequiredError;

    #[pymodule_export]
    use super::PyPostponedTimeoutError;

    #[pymodule_export]
    use super::PyPremiumAccountRequiredError;

    #[pymodule_export]
    use super::PyPremiumCurrentlyUnavailableError;

    #[pymodule_export]
    use super::PyPreviousChatImportActiveWaitMinError;

    #[pymodule_export]
    use super::PyPrivacyKeyInvalidError;

    #[pymodule_export]
    use super::PyPrivacyTooLongError;

    #[pymodule_export]
    use super::PyPrivacyValueInvalidError;

    #[pymodule_export]
    use super::PyPtsChangeEmptyError;

    #[pymodule_export]
    use super::PyPublicChannelMissingError;

    #[pymodule_export]
    use super::PyPublicKeyRequiredError;

    #[pymodule_export]
    use super::PyQueryIdEmptyError;

    #[pymodule_export]
    use super::PyQueryIdInvalidError;

    #[pymodule_export]
    use super::PyQueryTooShortError;

    #[pymodule_export]
    use super::PyQuizAnswerMissingError;

    #[pymodule_export]
    use super::PyQuizCorrectAnswersEmptyError;

    #[pymodule_export]
    use super::PyQuizCorrectAnswersTooMuchError;

    #[pymodule_export]
    use super::PyQuizCorrectAnswerInvalidError;

    #[pymodule_export]
    use super::PyQuizMultipleInvalidError;

    #[pymodule_export]
    use super::PyRandomIdDuplicateError;

    #[pymodule_export]
    use super::PyRandomIdEmptyError;

    #[pymodule_export]
    use super::PyRandomIdInvalidError;

    #[pymodule_export]
    use super::PyRandomLengthInvalidError;

    #[pymodule_export]
    use super::PyRangesInvalidError;

    #[pymodule_export]
    use super::PyReactionsTooManyError;

    #[pymodule_export]
    use super::PyReactionEmptyError;

    #[pymodule_export]
    use super::PyReactionInvalidError;

    #[pymodule_export]
    use super::PyReflectorNotAvailableError;

    #[pymodule_export]
    use super::PyRegIdGenerateFailedError;

    #[pymodule_export]
    use super::PyReplyMarkupBuyEmptyError;

    #[pymodule_export]
    use super::PyReplyMarkupGameEmptyError;

    #[pymodule_export]
    use super::PyReplyMarkupInvalidError;

    #[pymodule_export]
    use super::PyReplyMarkupTooLongError;

    #[pymodule_export]
    use super::PyResetRequestMissingError;

    #[pymodule_export]
    use super::PyResultsTooMuchError;

    #[pymodule_export]
    use super::PyResultIdDuplicateError;

    #[pymodule_export]
    use super::PyResultIdEmptyError;

    #[pymodule_export]
    use super::PyResultIdInvalidError;

    #[pymodule_export]
    use super::PyResultTypeInvalidError;

    #[pymodule_export]
    use super::PyRevoteNotAllowedError;

    #[pymodule_export]
    use super::PyRightsNotModifiedError;

    #[pymodule_export]
    use super::PyRightForbiddenError;

    #[pymodule_export]
    use super::PyRpcCallFailError;

    #[pymodule_export]
    use super::PyRpcMcgetFailError;

    #[pymodule_export]
    use super::PyRsaDecryptFailedError;

    #[pymodule_export]
    use super::PyScheduleBotNotAllowedError;

    #[pymodule_export]
    use super::PyScheduleDateInvalidError;

    #[pymodule_export]
    use super::PyScheduleDateTooLateError;

    #[pymodule_export]
    use super::PyScheduleStatusPrivateError;

    #[pymodule_export]
    use super::PyScheduleTooMuchError;

    #[pymodule_export]
    use super::PyScoreInvalidError;

    #[pymodule_export]
    use super::PySearchQueryEmptyError;

    #[pymodule_export]
    use super::PySearchWithLinkNotSupportedError;

    #[pymodule_export]
    use super::PySecondsInvalidError;

    #[pymodule_export]
    use super::PySendAsPeerInvalidError;

    #[pymodule_export]
    use super::PySendCodeUnavailableError;

    #[pymodule_export]
    use super::PySendMessageMediaInvalidError;

    #[pymodule_export]
    use super::PySendMessageTypeInvalidError;

    #[pymodule_export]
    use super::PySensitiveChangeForbiddenError;

    #[pymodule_export]
    use super::PySessionExpiredError;

    #[pymodule_export]
    use super::PySessionPasswordNeededError;

    #[pymodule_export]
    use super::PySessionRevokedError;

    #[pymodule_export]
    use super::PySessionTooFreshError;

    #[pymodule_export]
    use super::PySettingsInvalidError;

    #[pymodule_export]
    use super::PySha256HashInvalidError;

    #[pymodule_export]
    use super::PyShortnameOccupyFailedError;

    #[pymodule_export]
    use super::PyShortNameInvalidError;

    #[pymodule_export]
    use super::PyShortNameOccupiedError;

    #[pymodule_export]
    use super::PySignInFailedError;

    #[pymodule_export]
    use super::PySlowModeMultiMsgsDisabledError;

    #[pymodule_export]
    use super::PySlowModeWaitError;

    #[pymodule_export]
    use super::PySmsCodeCreateFailedError;

    #[pymodule_export]
    use super::PySrpIdInvalidError;

    #[pymodule_export]
    use super::PySrpPasswordChangedError;

    #[pymodule_export]
    use super::PyStartParamEmptyError;

    #[pymodule_export]
    use super::PyStartParamInvalidError;

    #[pymodule_export]
    use super::PyStartParamTooLongError;

    #[pymodule_export]
    use super::PyStatsMigrateError;

    #[pymodule_export]
    use super::PyStickerpackStickersTooMuchError;

    #[pymodule_export]
    use super::PyStickersetInvalidError;

    #[pymodule_export]
    use super::PyStickersetOwnerAnonymousError;

    #[pymodule_export]
    use super::PyStickersEmptyError;

    #[pymodule_export]
    use super::PyStickersTooMuchError;

    #[pymodule_export]
    use super::PyStickerDocumentInvalidError;

    #[pymodule_export]
    use super::PyStickerEmojiInvalidError;

    #[pymodule_export]
    use super::PyStickerFileInvalidError;

    #[pymodule_export]
    use super::PyStickerGifDimensionsError;

    #[pymodule_export]
    use super::PyStickerIdInvalidError;

    #[pymodule_export]
    use super::PyStickerInvalidError;

    #[pymodule_export]
    use super::PyStickerMimeInvalidError;

    #[pymodule_export]
    use super::PyStickerPngDimensionsError;

    #[pymodule_export]
    use super::PyStickerPngNopngError;

    #[pymodule_export]
    use super::PyStickerTgsNodocError;

    #[pymodule_export]
    use super::PyStickerTgsNotgsError;

    #[pymodule_export]
    use super::PyStickerThumbPngNopngError;

    #[pymodule_export]
    use super::PyStickerThumbTgsNotgsError;

    #[pymodule_export]
    use super::PyStickerVideoBigError;

    #[pymodule_export]
    use super::PyStickerVideoNodocError;

    #[pymodule_export]
    use super::PyStickerVideoNowebmError;

    #[pymodule_export]
    use super::PyStorageCheckFailedError;

    #[pymodule_export]
    use super::PyStoreInvalidScalarTypeError;

    #[pymodule_export]
    use super::PySwitchPmTextEmptyError;

    #[pymodule_export]
    use super::PyTakeoutInitDelayError;

    #[pymodule_export]
    use super::PyTakeoutInvalidError;

    #[pymodule_export]
    use super::PyTakeoutRequiredError;

    #[pymodule_export]
    use super::PyTempAuthKeyAlreadyBoundError;

    #[pymodule_export]
    use super::PyTempAuthKeyEmptyError;

    #[pymodule_export]
    use super::PyThemeFileInvalidError;

    #[pymodule_export]
    use super::PyThemeFormatInvalidError;

    #[pymodule_export]
    use super::PyThemeInvalidError;

    #[pymodule_export]
    use super::PyThemeMimeInvalidError;

    #[pymodule_export]
    use super::PyThemeTitleInvalidError;

    #[pymodule_export]
    use super::PyTitleInvalidError;

    #[pymodule_export]
    use super::PyTmpPasswordDisabledError;

    #[pymodule_export]
    use super::PyTmpPasswordInvalidError;

    #[pymodule_export]
    use super::PyTokenInvalidError;

    #[pymodule_export]
    use super::PyTopicDeletedError;

    #[pymodule_export]
    use super::PyToLangInvalidError;

    #[pymodule_export]
    use super::PyTtlDaysInvalidError;

    #[pymodule_export]
    use super::PyTtlMediaInvalidError;

    #[pymodule_export]
    use super::PyTtlPeriodInvalidError;

    #[pymodule_export]
    use super::PyTypesEmptyError;

    #[pymodule_export]
    use super::PyTypeConstructorInvalidError;

    #[pymodule_export]
    use super::PyUnknownErrorError;

    #[pymodule_export]
    use super::PyUnknownMethodError;

    #[pymodule_export]
    use super::PyUntilDateInvalidError;

    #[pymodule_export]
    use super::PyUpdateAppToLoginError;

    #[pymodule_export]
    use super::PyUrlInvalidError;

    #[pymodule_export]
    use super::PyUsageLimitInvalidError;

    #[pymodule_export]
    use super::PyUsernameInvalidError;

    #[pymodule_export]
    use super::PyUsernameNotModifiedError;

    #[pymodule_export]
    use super::PyUsernameNotOccupiedError;

    #[pymodule_export]
    use super::PyUsernameOccupiedError;

    #[pymodule_export]
    use super::PyUsernamePurchaseAvailableError;

    #[pymodule_export]
    use super::PyUserpicPrivacyRequiredError;

    #[pymodule_export]
    use super::PyUserpicUploadRequiredError;

    #[pymodule_export]
    use super::PyUsersTooFewError;

    #[pymodule_export]
    use super::PyUsersTooMuchError;

    #[pymodule_export]
    use super::PyUserAdminInvalidError;

    #[pymodule_export]
    use super::PyUserAlreadyInvitedError;

    #[pymodule_export]
    use super::PyUserAlreadyParticipantError;

    #[pymodule_export]
    use super::PyUserBannedInChannelError;

    #[pymodule_export]
    use super::PyUserBlockedError;

    #[pymodule_export]
    use super::PyUserBotError;

    #[pymodule_export]
    use super::PyUserBotInvalidError;

    #[pymodule_export]
    use super::PyUserBotRequiredError;

    #[pymodule_export]
    use super::PyUserChannelsTooMuchError;

    #[pymodule_export]
    use super::PyUserCreatorError;

    #[pymodule_export]
    use super::PyUserDeactivatedError;

    #[pymodule_export]
    use super::PyUserDeactivatedBanError;

    #[pymodule_export]
    use super::PyUserDeletedError;

    #[pymodule_export]
    use super::PyUserIdInvalidError;

    #[pymodule_export]
    use super::PyUserInvalidError;

    #[pymodule_export]
    use super::PyUserIsBlockedError;

    #[pymodule_export]
    use super::PyUserIsBotError;

    #[pymodule_export]
    use super::PyUserKickedError;

    #[pymodule_export]
    use super::PyUserMigrateError;

    #[pymodule_export]
    use super::PyUserNotMutualContactError;

    #[pymodule_export]
    use super::PyUserNotParticipantError;

    #[pymodule_export]
    use super::PyUserPrivacyRestrictedError;

    #[pymodule_export]
    use super::PyUserRestrictedError;

    #[pymodule_export]
    use super::PyUserVolumeInvalidError;

    #[pymodule_export]
    use super::PyVideoContentTypeInvalidError;

    #[pymodule_export]
    use super::PyVideoFileInvalidError;

    #[pymodule_export]
    use super::PyVideoTitleEmptyError;

    #[pymodule_export]
    use super::PyVoiceMessagesForbiddenError;

    #[pymodule_export]
    use super::PyWallpaperFileInvalidError;

    #[pymodule_export]
    use super::PyWallpaperInvalidError;

    #[pymodule_export]
    use super::PyWallpaperMimeInvalidError;

    #[pymodule_export]
    use super::PyWcConvertUrlInvalidError;

    #[pymodule_export]
    use super::PyWebdocumentInvalidError;

    #[pymodule_export]
    use super::PyWebdocumentMimeInvalidError;

    #[pymodule_export]
    use super::PyWebdocumentSizeTooBigError;

    #[pymodule_export]
    use super::PyWebdocumentUrlInvalidError;

    #[pymodule_export]
    use super::PyWebpageCurlFailedError;

    #[pymodule_export]
    use super::PyWebpageMediaEmptyError;

    #[pymodule_export]
    use super::PyWebpushAuthInvalidError;

    #[pymodule_export]
    use super::PyWebpushKeyInvalidError;

    #[pymodule_export]
    use super::PyWebpushTokenInvalidError;

    #[pymodule_export]
    use super::PyWorkerBusyTooLongRetryError;

    #[pymodule_export]
    use super::PyYouBlockedUserError;

    #[pymodule_export]
    use super::PyFrozenMethodInvalidError;

    #[pymodule_export]
    use super::PyFrozenParticipantMissingError;
}
