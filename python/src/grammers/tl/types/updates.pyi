from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class State(TLObject):
    """
    [Read `updates.state` docs](https://core.telegram.org/constructor/updates.state).

    Generated from the following TL definition:
    ```tl
    updates.state#a56c2a3e pts:int qts:int date:int seq:int unread_count:int = updates.State
    ```
    """
    def __new__(
        cls,
        pts: int,
        qts: int,
        date: int,
        seq: int,
        unread_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DifferenceEmpty(TLObject):
    """
    [Read `updates.differenceEmpty` docs](https://core.telegram.org/constructor/updates.differenceEmpty).

    Generated from the following TL definition:
    ```tl
    updates.differenceEmpty#5d75a138 date:int seq:int = updates.Difference
    ```
    """
    def __new__(
        cls,
        date: int,
        seq: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Difference(TLObject):
    """
    [Read `updates.difference` docs](https://core.telegram.org/constructor/updates.difference).

    Generated from the following TL definition:
    ```tl
    updates.difference#f49ca0 new_messages:Vector<Message> new_encrypted_messages:Vector<EncryptedMessage> other_updates:Vector<Update> chats:Vector<Chat> users:Vector<User> state:updates.State = updates.Difference
    ```
    """
    def __new__(
        cls,
        new_messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        new_encrypted_messages: Sequence[types.EncryptedMessage | types.EncryptedMessageService],
        other_updates: Sequence[types.UpdateNewMessage | types.UpdateMessageId | types.UpdateDeleteMessages | types.UpdateUserTyping | types.UpdateChatUserTyping | types.UpdateChatParticipants | types.UpdateUserStatus | types.UpdateUserName | types.UpdateNewAuthorization | types.UpdateNewEncryptedMessage | types.UpdateEncryptedChatTyping | types.UpdateEncryption | types.UpdateEncryptedMessagesRead | types.UpdateChatParticipantAdd | types.UpdateChatParticipantDelete | types.UpdateDcOptions | types.UpdateNotifySettings | types.UpdateServiceNotification | types.UpdatePrivacy | types.UpdateUserPhone | types.UpdateReadHistoryInbox | types.UpdateReadHistoryOutbox | types.UpdateWebPage | types.UpdateReadMessagesContents | types.UpdateChannelTooLong | types.UpdateChannel | types.UpdateNewChannelMessage | types.UpdateReadChannelInbox | types.UpdateDeleteChannelMessages | types.UpdateChannelMessageViews | types.UpdateChatParticipantAdmin | types.UpdateNewStickerSet | types.UpdateStickerSetsOrder | types.UpdateStickerSets | types.UpdateSavedGifs | types.UpdateBotInlineQuery | types.UpdateBotInlineSend | types.UpdateEditChannelMessage | types.UpdateBotCallbackQuery | types.UpdateEditMessage | types.UpdateInlineBotCallbackQuery | types.UpdateReadChannelOutbox | types.UpdateDraftMessage | types.UpdateReadFeaturedStickers | types.UpdateRecentStickers | types.UpdateConfig | types.UpdatePtsChanged | types.UpdateChannelWebPage | types.UpdateDialogPinned | types.UpdatePinnedDialogs | types.UpdateBotWebhookJson | types.UpdateBotWebhookJsonquery | types.UpdateBotShippingQuery | types.UpdateBotPrecheckoutQuery | types.UpdatePhoneCall | types.UpdateLangPackTooLong | types.UpdateLangPack | types.UpdateFavedStickers | types.UpdateChannelReadMessagesContents | types.UpdateContactsReset | types.UpdateChannelAvailableMessages | types.UpdateDialogUnreadMark | types.UpdateMessagePoll | types.UpdateChatDefaultBannedRights | types.UpdateFolderPeers | types.UpdatePeerSettings | types.UpdatePeerLocated | types.UpdateNewScheduledMessage | types.UpdateDeleteScheduledMessages | types.UpdateTheme | types.UpdateGeoLiveViewed | types.UpdateLoginToken | types.UpdateMessagePollVote | types.UpdateDialogFilter | types.UpdateDialogFilterOrder | types.UpdateDialogFilters | types.UpdatePhoneCallSignalingData | types.UpdateChannelMessageForwards | types.UpdateReadChannelDiscussionInbox | types.UpdateReadChannelDiscussionOutbox | types.UpdatePeerBlocked | types.UpdateChannelUserTyping | types.UpdatePinnedMessages | types.UpdatePinnedChannelMessages | types.UpdateChat | types.UpdateGroupCallParticipants | types.UpdateGroupCall | types.UpdatePeerHistoryTtl | types.UpdateChatParticipant | types.UpdateChannelParticipant | types.UpdateBotStopped | types.UpdateGroupCallConnection | types.UpdateBotCommands | types.UpdatePendingJoinRequests | types.UpdateBotChatInviteRequester | types.UpdateMessageReactions | types.UpdateAttachMenuBots | types.UpdateWebViewResultSent | types.UpdateBotMenuButton | types.UpdateSavedRingtones | types.UpdateTranscribedAudio | types.UpdateReadFeaturedEmojiStickers | types.UpdateUserEmojiStatus | types.UpdateRecentEmojiStatuses | types.UpdateRecentReactions | types.UpdateMoveStickerSetToTop | types.UpdateMessageExtendedMedia | types.UpdateUser | types.UpdateAutoSaveSettings | types.UpdateStory | types.UpdateReadStories | types.UpdateStoryId | types.UpdateStoriesStealthMode | types.UpdateSentStoryReaction | types.UpdateBotChatBoost | types.UpdateChannelViewForumAsMessages | types.UpdatePeerWallpaper | types.UpdateBotMessageReaction | types.UpdateBotMessageReactions | types.UpdateSavedDialogPinned | types.UpdatePinnedSavedDialogs | types.UpdateSavedReactionTags | types.UpdateSmsJob | types.UpdateQuickReplies | types.UpdateNewQuickReply | types.UpdateDeleteQuickReply | types.UpdateQuickReplyMessage | types.UpdateDeleteQuickReplyMessages | types.UpdateBotBusinessConnect | types.UpdateBotNewBusinessMessage | types.UpdateBotEditBusinessMessage | types.UpdateBotDeleteBusinessMessage | types.UpdateNewStoryReaction | types.UpdateStarsBalance | types.UpdateBusinessBotCallbackQuery | types.UpdateStarsRevenueStatus | types.UpdateBotPurchasedPaidMedia | types.UpdatePaidReactionPrivacy | types.UpdateSentPhoneCode | types.UpdateGroupCallChainBlocks | types.UpdateReadMonoForumInbox | types.UpdateReadMonoForumOutbox | types.UpdateMonoForumNoPaidException | types.UpdateGroupCallMessage | types.UpdateGroupCallEncryptedMessage | types.UpdatePinnedForumTopic | types.UpdatePinnedForumTopics | types.UpdateDeleteGroupCallMessages | types.UpdateStarGiftAuctionState | types.UpdateStarGiftAuctionUserState | types.UpdateEmojiGameInfo],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
        state: types.updates.State,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DifferenceSlice(TLObject):
    """
    [Read `updates.differenceSlice` docs](https://core.telegram.org/constructor/updates.differenceSlice).

    Generated from the following TL definition:
    ```tl
    updates.differenceSlice#a8fb1981 new_messages:Vector<Message> new_encrypted_messages:Vector<EncryptedMessage> other_updates:Vector<Update> chats:Vector<Chat> users:Vector<User> intermediate_state:updates.State = updates.Difference
    ```
    """
    def __new__(
        cls,
        new_messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        new_encrypted_messages: Sequence[types.EncryptedMessage | types.EncryptedMessageService],
        other_updates: Sequence[types.UpdateNewMessage | types.UpdateMessageId | types.UpdateDeleteMessages | types.UpdateUserTyping | types.UpdateChatUserTyping | types.UpdateChatParticipants | types.UpdateUserStatus | types.UpdateUserName | types.UpdateNewAuthorization | types.UpdateNewEncryptedMessage | types.UpdateEncryptedChatTyping | types.UpdateEncryption | types.UpdateEncryptedMessagesRead | types.UpdateChatParticipantAdd | types.UpdateChatParticipantDelete | types.UpdateDcOptions | types.UpdateNotifySettings | types.UpdateServiceNotification | types.UpdatePrivacy | types.UpdateUserPhone | types.UpdateReadHistoryInbox | types.UpdateReadHistoryOutbox | types.UpdateWebPage | types.UpdateReadMessagesContents | types.UpdateChannelTooLong | types.UpdateChannel | types.UpdateNewChannelMessage | types.UpdateReadChannelInbox | types.UpdateDeleteChannelMessages | types.UpdateChannelMessageViews | types.UpdateChatParticipantAdmin | types.UpdateNewStickerSet | types.UpdateStickerSetsOrder | types.UpdateStickerSets | types.UpdateSavedGifs | types.UpdateBotInlineQuery | types.UpdateBotInlineSend | types.UpdateEditChannelMessage | types.UpdateBotCallbackQuery | types.UpdateEditMessage | types.UpdateInlineBotCallbackQuery | types.UpdateReadChannelOutbox | types.UpdateDraftMessage | types.UpdateReadFeaturedStickers | types.UpdateRecentStickers | types.UpdateConfig | types.UpdatePtsChanged | types.UpdateChannelWebPage | types.UpdateDialogPinned | types.UpdatePinnedDialogs | types.UpdateBotWebhookJson | types.UpdateBotWebhookJsonquery | types.UpdateBotShippingQuery | types.UpdateBotPrecheckoutQuery | types.UpdatePhoneCall | types.UpdateLangPackTooLong | types.UpdateLangPack | types.UpdateFavedStickers | types.UpdateChannelReadMessagesContents | types.UpdateContactsReset | types.UpdateChannelAvailableMessages | types.UpdateDialogUnreadMark | types.UpdateMessagePoll | types.UpdateChatDefaultBannedRights | types.UpdateFolderPeers | types.UpdatePeerSettings | types.UpdatePeerLocated | types.UpdateNewScheduledMessage | types.UpdateDeleteScheduledMessages | types.UpdateTheme | types.UpdateGeoLiveViewed | types.UpdateLoginToken | types.UpdateMessagePollVote | types.UpdateDialogFilter | types.UpdateDialogFilterOrder | types.UpdateDialogFilters | types.UpdatePhoneCallSignalingData | types.UpdateChannelMessageForwards | types.UpdateReadChannelDiscussionInbox | types.UpdateReadChannelDiscussionOutbox | types.UpdatePeerBlocked | types.UpdateChannelUserTyping | types.UpdatePinnedMessages | types.UpdatePinnedChannelMessages | types.UpdateChat | types.UpdateGroupCallParticipants | types.UpdateGroupCall | types.UpdatePeerHistoryTtl | types.UpdateChatParticipant | types.UpdateChannelParticipant | types.UpdateBotStopped | types.UpdateGroupCallConnection | types.UpdateBotCommands | types.UpdatePendingJoinRequests | types.UpdateBotChatInviteRequester | types.UpdateMessageReactions | types.UpdateAttachMenuBots | types.UpdateWebViewResultSent | types.UpdateBotMenuButton | types.UpdateSavedRingtones | types.UpdateTranscribedAudio | types.UpdateReadFeaturedEmojiStickers | types.UpdateUserEmojiStatus | types.UpdateRecentEmojiStatuses | types.UpdateRecentReactions | types.UpdateMoveStickerSetToTop | types.UpdateMessageExtendedMedia | types.UpdateUser | types.UpdateAutoSaveSettings | types.UpdateStory | types.UpdateReadStories | types.UpdateStoryId | types.UpdateStoriesStealthMode | types.UpdateSentStoryReaction | types.UpdateBotChatBoost | types.UpdateChannelViewForumAsMessages | types.UpdatePeerWallpaper | types.UpdateBotMessageReaction | types.UpdateBotMessageReactions | types.UpdateSavedDialogPinned | types.UpdatePinnedSavedDialogs | types.UpdateSavedReactionTags | types.UpdateSmsJob | types.UpdateQuickReplies | types.UpdateNewQuickReply | types.UpdateDeleteQuickReply | types.UpdateQuickReplyMessage | types.UpdateDeleteQuickReplyMessages | types.UpdateBotBusinessConnect | types.UpdateBotNewBusinessMessage | types.UpdateBotEditBusinessMessage | types.UpdateBotDeleteBusinessMessage | types.UpdateNewStoryReaction | types.UpdateStarsBalance | types.UpdateBusinessBotCallbackQuery | types.UpdateStarsRevenueStatus | types.UpdateBotPurchasedPaidMedia | types.UpdatePaidReactionPrivacy | types.UpdateSentPhoneCode | types.UpdateGroupCallChainBlocks | types.UpdateReadMonoForumInbox | types.UpdateReadMonoForumOutbox | types.UpdateMonoForumNoPaidException | types.UpdateGroupCallMessage | types.UpdateGroupCallEncryptedMessage | types.UpdatePinnedForumTopic | types.UpdatePinnedForumTopics | types.UpdateDeleteGroupCallMessages | types.UpdateStarGiftAuctionState | types.UpdateStarGiftAuctionUserState | types.UpdateEmojiGameInfo],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
        intermediate_state: types.updates.State,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DifferenceTooLong(TLObject):
    """
    [Read `updates.differenceTooLong` docs](https://core.telegram.org/constructor/updates.differenceTooLong).

    Generated from the following TL definition:
    ```tl
    updates.differenceTooLong#4afe8f6d pts:int = updates.Difference
    ```
    """
    def __new__(
        cls,
        pts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelDifferenceEmpty(TLObject):
    """
    [Read `updates.channelDifferenceEmpty` docs](https://core.telegram.org/constructor/updates.channelDifferenceEmpty).

    Generated from the following TL definition:
    ```tl
    updates.channelDifferenceEmpty#3e11affb flags:# final:flags.0?true pts:int timeout:flags.1?int = updates.ChannelDifference
    ```
    """
    def __new__(
        cls,
        final: bool,
        pts: int,
        timeout: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelDifferenceTooLong(TLObject):
    """
    [Read `updates.channelDifferenceTooLong` docs](https://core.telegram.org/constructor/updates.channelDifferenceTooLong).

    Generated from the following TL definition:
    ```tl
    updates.channelDifferenceTooLong#a4bcc6fe flags:# final:flags.0?true timeout:flags.1?int dialog:Dialog messages:Vector<Message> chats:Vector<Chat> users:Vector<User> = updates.ChannelDifference
    ```
    """
    def __new__(
        cls,
        final: bool,
        timeout: Optional[int],
        dialog: types.Dialog | types.DialogFolder,
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelDifference(TLObject):
    """
    [Read `updates.channelDifference` docs](https://core.telegram.org/constructor/updates.channelDifference).

    Generated from the following TL definition:
    ```tl
    updates.channelDifference#2064674e flags:# final:flags.0?true pts:int timeout:flags.1?int new_messages:Vector<Message> other_updates:Vector<Update> chats:Vector<Chat> users:Vector<User> = updates.ChannelDifference
    ```
    """
    def __new__(
        cls,
        final: bool,
        pts: int,
        timeout: Optional[int],
        new_messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        other_updates: Sequence[types.UpdateNewMessage | types.UpdateMessageId | types.UpdateDeleteMessages | types.UpdateUserTyping | types.UpdateChatUserTyping | types.UpdateChatParticipants | types.UpdateUserStatus | types.UpdateUserName | types.UpdateNewAuthorization | types.UpdateNewEncryptedMessage | types.UpdateEncryptedChatTyping | types.UpdateEncryption | types.UpdateEncryptedMessagesRead | types.UpdateChatParticipantAdd | types.UpdateChatParticipantDelete | types.UpdateDcOptions | types.UpdateNotifySettings | types.UpdateServiceNotification | types.UpdatePrivacy | types.UpdateUserPhone | types.UpdateReadHistoryInbox | types.UpdateReadHistoryOutbox | types.UpdateWebPage | types.UpdateReadMessagesContents | types.UpdateChannelTooLong | types.UpdateChannel | types.UpdateNewChannelMessage | types.UpdateReadChannelInbox | types.UpdateDeleteChannelMessages | types.UpdateChannelMessageViews | types.UpdateChatParticipantAdmin | types.UpdateNewStickerSet | types.UpdateStickerSetsOrder | types.UpdateStickerSets | types.UpdateSavedGifs | types.UpdateBotInlineQuery | types.UpdateBotInlineSend | types.UpdateEditChannelMessage | types.UpdateBotCallbackQuery | types.UpdateEditMessage | types.UpdateInlineBotCallbackQuery | types.UpdateReadChannelOutbox | types.UpdateDraftMessage | types.UpdateReadFeaturedStickers | types.UpdateRecentStickers | types.UpdateConfig | types.UpdatePtsChanged | types.UpdateChannelWebPage | types.UpdateDialogPinned | types.UpdatePinnedDialogs | types.UpdateBotWebhookJson | types.UpdateBotWebhookJsonquery | types.UpdateBotShippingQuery | types.UpdateBotPrecheckoutQuery | types.UpdatePhoneCall | types.UpdateLangPackTooLong | types.UpdateLangPack | types.UpdateFavedStickers | types.UpdateChannelReadMessagesContents | types.UpdateContactsReset | types.UpdateChannelAvailableMessages | types.UpdateDialogUnreadMark | types.UpdateMessagePoll | types.UpdateChatDefaultBannedRights | types.UpdateFolderPeers | types.UpdatePeerSettings | types.UpdatePeerLocated | types.UpdateNewScheduledMessage | types.UpdateDeleteScheduledMessages | types.UpdateTheme | types.UpdateGeoLiveViewed | types.UpdateLoginToken | types.UpdateMessagePollVote | types.UpdateDialogFilter | types.UpdateDialogFilterOrder | types.UpdateDialogFilters | types.UpdatePhoneCallSignalingData | types.UpdateChannelMessageForwards | types.UpdateReadChannelDiscussionInbox | types.UpdateReadChannelDiscussionOutbox | types.UpdatePeerBlocked | types.UpdateChannelUserTyping | types.UpdatePinnedMessages | types.UpdatePinnedChannelMessages | types.UpdateChat | types.UpdateGroupCallParticipants | types.UpdateGroupCall | types.UpdatePeerHistoryTtl | types.UpdateChatParticipant | types.UpdateChannelParticipant | types.UpdateBotStopped | types.UpdateGroupCallConnection | types.UpdateBotCommands | types.UpdatePendingJoinRequests | types.UpdateBotChatInviteRequester | types.UpdateMessageReactions | types.UpdateAttachMenuBots | types.UpdateWebViewResultSent | types.UpdateBotMenuButton | types.UpdateSavedRingtones | types.UpdateTranscribedAudio | types.UpdateReadFeaturedEmojiStickers | types.UpdateUserEmojiStatus | types.UpdateRecentEmojiStatuses | types.UpdateRecentReactions | types.UpdateMoveStickerSetToTop | types.UpdateMessageExtendedMedia | types.UpdateUser | types.UpdateAutoSaveSettings | types.UpdateStory | types.UpdateReadStories | types.UpdateStoryId | types.UpdateStoriesStealthMode | types.UpdateSentStoryReaction | types.UpdateBotChatBoost | types.UpdateChannelViewForumAsMessages | types.UpdatePeerWallpaper | types.UpdateBotMessageReaction | types.UpdateBotMessageReactions | types.UpdateSavedDialogPinned | types.UpdatePinnedSavedDialogs | types.UpdateSavedReactionTags | types.UpdateSmsJob | types.UpdateQuickReplies | types.UpdateNewQuickReply | types.UpdateDeleteQuickReply | types.UpdateQuickReplyMessage | types.UpdateDeleteQuickReplyMessages | types.UpdateBotBusinessConnect | types.UpdateBotNewBusinessMessage | types.UpdateBotEditBusinessMessage | types.UpdateBotDeleteBusinessMessage | types.UpdateNewStoryReaction | types.UpdateStarsBalance | types.UpdateBusinessBotCallbackQuery | types.UpdateStarsRevenueStatus | types.UpdateBotPurchasedPaidMedia | types.UpdatePaidReactionPrivacy | types.UpdateSentPhoneCode | types.UpdateGroupCallChainBlocks | types.UpdateReadMonoForumInbox | types.UpdateReadMonoForumOutbox | types.UpdateMonoForumNoPaidException | types.UpdateGroupCallMessage | types.UpdateGroupCallEncryptedMessage | types.UpdatePinnedForumTopic | types.UpdatePinnedForumTopics | types.UpdateDeleteGroupCallMessages | types.UpdateStarGiftAuctionState | types.UpdateStarGiftAuctionUserState | types.UpdateEmojiGameInfo],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

