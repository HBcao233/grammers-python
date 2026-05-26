from grammers import custom, types
from grammers.sessions import PeerIdLike

Phone = str
Username = str
InviteLink = str
InputPeerLike = Phone | Username | types.InputPeer | PeerIdLike
Peer = custom.User | custom.Group | custom.Channel

Message = types.MessageEmpty | types.Message | types.MessageService
MessageReplyHeader = types.MessageReplyHeader | types.MessageReplyStoryHeader
MessageMedia = (
    types.MessageMediaEmpty
    | types.MessageMediaPhoto
    | types.MessageMediaGeo
    | types.MessageMediaContact
    | types.MessageMediaUnsupported
    | types.MessageMediaDocument
    | types.MessageMediaWebPage
    | types.MessageMediaVenue
    | types.MessageMediaGame
    | types.MessageMediaInvoice
    | types.MessageMediaGeoLive
    | types.MessageMediaPoll
    | types.MessageMediaDice
    | types.MessageMediaStory
    | types.MessageMediaGiveaway
    | types.MessageMediaGiveawayResults
    | types.MessageMediaPaidMedia
    | types.MessageMediaToDo
)
ReplyMarkup = (
    types.ReplyKeyboardHide
    | types.ReplyKeyboardForceReply
    | types.ReplyKeyboardMarkup
    | types.ReplyInlineMarkup
)
MessageEntity = (
    types.MessageEntityUnknown
    | types.MessageEntityMention
    | types.MessageEntityHashtag
    | types.MessageEntityBotCommand
    | types.MessageEntityUrl
    | types.MessageEntityEmail
    | types.MessageEntityBold
    | types.MessageEntityItalic
    | types.MessageEntityCode
    | types.MessageEntityPre
    | types.MessageEntityTextUrl
    | types.MessageEntityMentionName
    | types.InputMessageEntityMentionName
    | types.MessageEntityPhone
    | types.MessageEntityCashtag
    | types.MessageEntityUnderline
    | types.MessageEntityStrike
    | types.MessageEntityBankCard
    | types.MessageEntitySpoiler
    | types.MessageEntityCustomEmoji
    | types.MessageEntityBlockquote
)

Update = (
    types.UpdateNewMessage
    | types.UpdateMessageId
    | types.UpdateDeleteMessages
    | types.UpdateUserTyping
    | types.UpdateChatUserTyping
    | types.UpdateChatParticipants
    | types.UpdateUserStatus
    | types.UpdateUserName
    | types.UpdateNewAuthorization
    | types.UpdateNewEncryptedMessage
    | types.UpdateEncryptedChatTyping
    | types.UpdateEncryption
    | types.UpdateEncryptedMessagesRead
    | types.UpdateChatParticipantAdd
    | types.UpdateChatParticipantDelete
    | types.UpdateDcOptions
    | types.UpdateNotifySettings
    | types.UpdateServiceNotification
    | types.UpdatePrivacy
    | types.UpdateUserPhone
    | types.UpdateReadHistoryInbox
    | types.UpdateReadHistoryOutbox
    | types.UpdateWebPage
    | types.UpdateReadMessagesContents
    | types.UpdateChannelTooLong
    | types.UpdateChannel
    | types.UpdateNewChannelMessage
    | types.UpdateReadChannelInbox
    | types.UpdateDeleteChannelMessages
    | types.UpdateChannelMessageViews
    | types.UpdateChatParticipantAdmin
    | types.UpdateNewStickerSet
    | types.UpdateStickerSetsOrder
    | types.UpdateStickerSets
    | types.UpdateSavedGifs
    | types.UpdateBotInlineQuery
    | types.UpdateBotInlineSend
    | types.UpdateEditChannelMessage
    | types.UpdateBotCallbackQuery
    | types.UpdateEditMessage
    | types.UpdateInlineBotCallbackQuery
    | types.UpdateReadChannelOutbox
    | types.UpdateDraftMessage
    | types.UpdateReadFeaturedStickers
    | types.UpdateRecentStickers
    | types.UpdateConfig
    | types.UpdatePtsChanged
    | types.UpdateChannelWebPage
    | types.UpdateDialogPinned
    | types.UpdatePinnedDialogs
    | types.UpdateBotWebhookJson
    | types.UpdateBotWebhookJsonquery
    | types.UpdateBotShippingQuery
    | types.UpdateBotPrecheckoutQuery
    | types.UpdatePhoneCall
    | types.UpdateLangPackTooLong
    | types.UpdateLangPack
    | types.UpdateFavedStickers
    | types.UpdateChannelReadMessagesContents
    | types.UpdateContactsReset
    | types.UpdateChannelAvailableMessages
    | types.UpdateDialogUnreadMark
    | types.UpdateMessagePoll
    | types.UpdateChatDefaultBannedRights
    | types.UpdateFolderPeers
    | types.UpdatePeerSettings
    | types.UpdatePeerLocated
    | types.UpdateNewScheduledMessage
    | types.UpdateDeleteScheduledMessages
    | types.UpdateTheme
    | types.UpdateGeoLiveViewed
    | types.UpdateLoginToken
    | types.UpdateMessagePollVote
    | types.UpdateDialogFilter
    | types.UpdateDialogFilterOrder
    | types.UpdateDialogFilters
    | types.UpdatePhoneCallSignalingData
    | types.UpdateChannelMessageForwards
    | types.UpdateReadChannelDiscussionInbox
    | types.UpdateReadChannelDiscussionOutbox
    | types.UpdatePeerBlocked
    | types.UpdateChannelUserTyping
    | types.UpdatePinnedMessages
    | types.UpdatePinnedChannelMessages
    | types.UpdateChat
    | types.UpdateGroupCallParticipants
    | types.UpdateGroupCall
    | types.UpdatePeerHistoryTtl
    | types.UpdateChatParticipant
    | types.UpdateChannelParticipant
    | types.UpdateBotStopped
    | types.UpdateGroupCallConnection
    | types.UpdateBotCommands
    | types.UpdatePendingJoinRequests
    | types.UpdateBotChatInviteRequester
    | types.UpdateMessageReactions
    | types.UpdateAttachMenuBots
    | types.UpdateWebViewResultSent
    | types.UpdateBotMenuButton
    | types.UpdateSavedRingtones
    | types.UpdateTranscribedAudio
    | types.UpdateReadFeaturedEmojiStickers
    | types.UpdateUserEmojiStatus
    | types.UpdateRecentEmojiStatuses
    | types.UpdateRecentReactions
    | types.UpdateMoveStickerSetToTop
    | types.UpdateMessageExtendedMedia
    | types.UpdateUser
    | types.UpdateAutoSaveSettings
    | types.UpdateStory
    | types.UpdateReadStories
    | types.UpdateStoryId
    | types.UpdateStoriesStealthMode
    | types.UpdateSentStoryReaction
    | types.UpdateBotChatBoost
    | types.UpdateChannelViewForumAsMessages
    | types.UpdatePeerWallpaper
    | types.UpdateBotMessageReaction
    | types.UpdateBotMessageReactions
    | types.UpdateSavedDialogPinned
    | types.UpdatePinnedSavedDialogs
    | types.UpdateSavedReactionTags
    | types.UpdateSmsJob
    | types.UpdateQuickReplies
    | types.UpdateNewQuickReply
    | types.UpdateDeleteQuickReply
    | types.UpdateQuickReplyMessage
    | types.UpdateDeleteQuickReplyMessages
    | types.UpdateBotBusinessConnect
    | types.UpdateBotNewBusinessMessage
    | types.UpdateBotEditBusinessMessage
    | types.UpdateBotDeleteBusinessMessage
    | types.UpdateNewStoryReaction
    | types.UpdateStarsBalance
    | types.UpdateBusinessBotCallbackQuery
    | types.UpdateStarsRevenueStatus
    | types.UpdateBotPurchasedPaidMedia
    | types.UpdatePaidReactionPrivacy
    | types.UpdateSentPhoneCode
    | types.UpdateGroupCallChainBlocks
    | types.UpdateReadMonoForumInbox
    | types.UpdateReadMonoForumOutbox
    | types.UpdateMonoForumNoPaidException
    | types.UpdateGroupCallMessage
    | types.UpdateGroupCallEncryptedMessage
    | types.UpdatePinnedForumTopic
    | types.UpdatePinnedForumTopics
    | types.UpdateDeleteGroupCallMessages
    | types.UpdateStarGiftAuctionState
    | types.UpdateStarGiftAuctionUserState
    | types.UpdateEmojiGameInfo
    | types.UpdateStarGiftCraftFail
    | types.UpdateChatParticipantRank
    | types.UpdateManagedBot
    | types.UpdateBotGuestChatQuery
    | types.UpdateAiComposeTones
)
