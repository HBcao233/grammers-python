from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class GetMessages(TLRequest):
    """
    [Read `messages.getMessages` docs](https://core.telegram.org/method/messages.getMessages).

    Generated from the following TL definition:
    ```tl
    messages.getMessages#63c66506 id:Vector<InputMessage> = messages.Messages
    ```
    """
    def __new__(
        cls,
        id: Sequence[types.InputMessageId | types.InputMessageReplyTo | types.InputMessagePinned | types.InputMessageCallbackQuery],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDialogs(TLRequest):
    """
    [Read `messages.getDialogs` docs](https://core.telegram.org/method/messages.getDialogs).

    Generated from the following TL definition:
    ```tl
    messages.getDialogs#a0f4cb4f flags:# exclude_pinned:flags.0?true folder_id:flags.1?int offset_date:int offset_id:int offset_peer:InputPeer limit:int hash:long = messages.Dialogs
    ```
    """
    def __new__(
        cls,
        exclude_pinned: bool,
        folder_id: Optional[int],
        offset_date: int,
        offset_id: int,
        offset_peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        limit: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetHistory(TLRequest):
    """
    [Read `messages.getHistory` docs](https://core.telegram.org/method/messages.getHistory).

    Generated from the following TL definition:
    ```tl
    messages.getHistory#4423e6c5 peer:InputPeer offset_id:int offset_date:int add_offset:int limit:int max_id:int min_id:int hash:long = messages.Messages
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        offset_id: int,
        offset_date: int,
        add_offset: int,
        limit: int,
        max_id: int,
        min_id: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Search(TLRequest):
    """
    [Read `messages.search` docs](https://core.telegram.org/method/messages.search).

    Generated from the following TL definition:
    ```tl
    messages.search#29ee847a flags:# peer:InputPeer q:string from_id:flags.0?InputPeer saved_peer_id:flags.2?InputPeer saved_reaction:flags.3?Vector<Reaction> top_msg_id:flags.1?int filter:MessagesFilter min_date:int max_date:int offset_id:int add_offset:int limit:int max_id:int min_id:int hash:long = messages.Messages
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        q: str,
        from_id: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        saved_peer_id: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        saved_reaction: Optional[Sequence[types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid]],
        top_msg_id: Optional[int],
        filter: types.InputMessagesFilterEmpty | types.InputMessagesFilterPhotos | types.InputMessagesFilterVideo | types.InputMessagesFilterPhotoVideo | types.InputMessagesFilterDocument | types.InputMessagesFilterUrl | types.InputMessagesFilterGif | types.InputMessagesFilterVoice | types.InputMessagesFilterMusic | types.InputMessagesFilterChatPhotos | types.InputMessagesFilterPhoneCalls | types.InputMessagesFilterRoundVoice | types.InputMessagesFilterRoundVideo | types.InputMessagesFilterMyMentions | types.InputMessagesFilterGeo | types.InputMessagesFilterContacts | types.InputMessagesFilterPinned,
        min_date: int,
        max_date: int,
        offset_id: int,
        add_offset: int,
        limit: int,
        max_id: int,
        min_id: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReadHistory(TLRequest):
    """
    [Read `messages.readHistory` docs](https://core.telegram.org/method/messages.readHistory).

    Generated from the following TL definition:
    ```tl
    messages.readHistory#e306d3a peer:InputPeer max_id:int = messages.AffectedMessages
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteHistory(TLRequest):
    """
    [Read `messages.deleteHistory` docs](https://core.telegram.org/method/messages.deleteHistory).

    Generated from the following TL definition:
    ```tl
    messages.deleteHistory#b08f922a flags:# just_clear:flags.0?true revoke:flags.1?true peer:InputPeer max_id:int min_date:flags.2?int max_date:flags.3?int = messages.AffectedHistory
    ```
    """
    def __new__(
        cls,
        just_clear: bool,
        revoke: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        max_id: int,
        min_date: Optional[int],
        max_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteMessages(TLRequest):
    """
    [Read `messages.deleteMessages` docs](https://core.telegram.org/method/messages.deleteMessages).

    Generated from the following TL definition:
    ```tl
    messages.deleteMessages#e58e95d2 flags:# revoke:flags.0?true id:Vector<int> = messages.AffectedMessages
    ```
    """
    def __new__(
        cls,
        revoke: bool,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReceivedMessages(TLRequest):
    """
    [Read `messages.receivedMessages` docs](https://core.telegram.org/method/messages.receivedMessages).

    Generated from the following TL definition:
    ```tl
    messages.receivedMessages#5a954c0 max_id:int = Vector<ReceivedNotifyMessage>
    ```
    """
    def __new__(
        cls,
        max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetTyping(TLRequest):
    """
    [Read `messages.setTyping` docs](https://core.telegram.org/method/messages.setTyping).

    Generated from the following TL definition:
    ```tl
    messages.setTyping#58943ee2 flags:# peer:InputPeer top_msg_id:flags.0?int action:SendMessageAction = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        top_msg_id: Optional[int],
        action: types.SendMessageTypingAction | types.SendMessageCancelAction | types.SendMessageRecordVideoAction | types.SendMessageUploadVideoAction | types.SendMessageRecordAudioAction | types.SendMessageUploadAudioAction | types.SendMessageUploadPhotoAction | types.SendMessageUploadDocumentAction | types.SendMessageGeoLocationAction | types.SendMessageChooseContactAction | types.SendMessageGamePlayAction | types.SendMessageRecordRoundAction | types.SendMessageUploadRoundAction | types.SpeakingInGroupCallAction | types.SendMessageHistoryImportAction | types.SendMessageChooseStickerAction | types.SendMessageEmojiInteraction | types.SendMessageEmojiInteractionSeen | types.SendMessageTextDraftAction,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessage(TLRequest):
    """
    [Read `messages.sendMessage` docs](https://core.telegram.org/method/messages.sendMessage).

    Generated from the following TL definition:
    ```tl
    messages.sendMessage#545cd15a flags:# no_webpage:flags.1?true silent:flags.5?true background:flags.6?true clear_draft:flags.7?true noforwards:flags.14?true update_stickersets_order:flags.15?true invert_media:flags.16?true allow_paid_floodskip:flags.19?true peer:InputPeer reply_to:flags.0?InputReplyTo message:string random_id:long reply_markup:flags.2?ReplyMarkup entities:flags.3?Vector<MessageEntity> schedule_date:flags.10?int schedule_repeat_period:flags.24?int send_as:flags.13?InputPeer quick_reply_shortcut:flags.17?InputQuickReplyShortcut effect:flags.18?long allow_paid_stars:flags.21?long suggested_post:flags.22?SuggestedPost = Updates
    ```
    """
    def __new__(
        cls,
        no_webpage: bool,
        silent: bool,
        background: bool,
        clear_draft: bool,
        noforwards: bool,
        update_stickersets_order: bool,
        invert_media: bool,
        allow_paid_floodskip: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        reply_to: Optional[types.InputReplyToMessage | types.InputReplyToStory | types.InputReplyToMonoForum],
        message: str,
        random_id: int,
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        schedule_date: Optional[int],
        schedule_repeat_period: Optional[int],
        send_as: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        quick_reply_shortcut: Optional[types.InputQuickReplyShortcut | types.InputQuickReplyShortcutId],
        effect: Optional[int],
        allow_paid_stars: Optional[int],
        suggested_post: Optional[types.SuggestedPost],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMedia(TLRequest):
    """
    [Read `messages.sendMedia` docs](https://core.telegram.org/method/messages.sendMedia).

    Generated from the following TL definition:
    ```tl
    messages.sendMedia#330e77f flags:# silent:flags.5?true background:flags.6?true clear_draft:flags.7?true noforwards:flags.14?true update_stickersets_order:flags.15?true invert_media:flags.16?true allow_paid_floodskip:flags.19?true peer:InputPeer reply_to:flags.0?InputReplyTo media:InputMedia message:string random_id:long reply_markup:flags.2?ReplyMarkup entities:flags.3?Vector<MessageEntity> schedule_date:flags.10?int schedule_repeat_period:flags.24?int send_as:flags.13?InputPeer quick_reply_shortcut:flags.17?InputQuickReplyShortcut effect:flags.18?long allow_paid_stars:flags.21?long suggested_post:flags.22?SuggestedPost = Updates
    ```
    """
    def __new__(
        cls,
        silent: bool,
        background: bool,
        clear_draft: bool,
        noforwards: bool,
        update_stickersets_order: bool,
        invert_media: bool,
        allow_paid_floodskip: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        reply_to: Optional[types.InputReplyToMessage | types.InputReplyToStory | types.InputReplyToMonoForum],
        media: types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice,
        message: str,
        random_id: int,
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        schedule_date: Optional[int],
        schedule_repeat_period: Optional[int],
        send_as: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        quick_reply_shortcut: Optional[types.InputQuickReplyShortcut | types.InputQuickReplyShortcutId],
        effect: Optional[int],
        allow_paid_stars: Optional[int],
        suggested_post: Optional[types.SuggestedPost],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ForwardMessages(TLRequest):
    """
    [Read `messages.forwardMessages` docs](https://core.telegram.org/method/messages.forwardMessages).

    Generated from the following TL definition:
    ```tl
    messages.forwardMessages#13704a7c flags:# silent:flags.5?true background:flags.6?true with_my_score:flags.8?true drop_author:flags.11?true drop_media_captions:flags.12?true noforwards:flags.14?true allow_paid_floodskip:flags.19?true from_peer:InputPeer id:Vector<int> random_id:Vector<long> to_peer:InputPeer top_msg_id:flags.9?int reply_to:flags.22?InputReplyTo schedule_date:flags.10?int schedule_repeat_period:flags.24?int send_as:flags.13?InputPeer quick_reply_shortcut:flags.17?InputQuickReplyShortcut effect:flags.18?long video_timestamp:flags.20?int allow_paid_stars:flags.21?long suggested_post:flags.23?SuggestedPost = Updates
    ```
    """
    def __new__(
        cls,
        silent: bool,
        background: bool,
        with_my_score: bool,
        drop_author: bool,
        drop_media_captions: bool,
        noforwards: bool,
        allow_paid_floodskip: bool,
        from_peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
        random_id: Sequence[int],
        to_peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        top_msg_id: Optional[int],
        reply_to: Optional[types.InputReplyToMessage | types.InputReplyToStory | types.InputReplyToMonoForum],
        schedule_date: Optional[int],
        schedule_repeat_period: Optional[int],
        send_as: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        quick_reply_shortcut: Optional[types.InputQuickReplyShortcut | types.InputQuickReplyShortcutId],
        effect: Optional[int],
        video_timestamp: Optional[int],
        allow_paid_stars: Optional[int],
        suggested_post: Optional[types.SuggestedPost],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportSpam(TLRequest):
    """
    [Read `messages.reportSpam` docs](https://core.telegram.org/method/messages.reportSpam).

    Generated from the following TL definition:
    ```tl
    messages.reportSpam#cf1592db peer:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPeerSettings(TLRequest):
    """
    [Read `messages.getPeerSettings` docs](https://core.telegram.org/method/messages.getPeerSettings).

    Generated from the following TL definition:
    ```tl
    messages.getPeerSettings#efd9a6a2 peer:InputPeer = messages.PeerSettings
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Report(TLRequest):
    """
    [Read `messages.report` docs](https://core.telegram.org/method/messages.report).

    Generated from the following TL definition:
    ```tl
    messages.report#fc78af9b peer:InputPeer id:Vector<int> option:bytes message:string = ReportResult
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
        option: bytes,
        message: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetChats(TLRequest):
    """
    [Read `messages.getChats` docs](https://core.telegram.org/method/messages.getChats).

    Generated from the following TL definition:
    ```tl
    messages.getChats#49e9528f id:Vector<long> = messages.Chats
    ```
    """
    def __new__(
        cls,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetFullChat(TLRequest):
    """
    [Read `messages.getFullChat` docs](https://core.telegram.org/method/messages.getFullChat).

    Generated from the following TL definition:
    ```tl
    messages.getFullChat#aeb00b34 chat_id:long = messages.ChatFull
    ```
    """
    def __new__(
        cls,
        chat_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditChatTitle(TLRequest):
    """
    [Read `messages.editChatTitle` docs](https://core.telegram.org/method/messages.editChatTitle).

    Generated from the following TL definition:
    ```tl
    messages.editChatTitle#73783ffd chat_id:long title:string = Updates
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        title: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditChatPhoto(TLRequest):
    """
    [Read `messages.editChatPhoto` docs](https://core.telegram.org/method/messages.editChatPhoto).

    Generated from the following TL definition:
    ```tl
    messages.editChatPhoto#35ddd674 chat_id:long photo:InputChatPhoto = Updates
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        photo: types.InputChatPhotoEmpty | types.InputChatUploadedPhoto | types.InputChatPhoto,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AddChatUser(TLRequest):
    """
    [Read `messages.addChatUser` docs](https://core.telegram.org/method/messages.addChatUser).

    Generated from the following TL definition:
    ```tl
    messages.addChatUser#cbc6d107 chat_id:long user_id:InputUser fwd_limit:int = messages.InvitedUsers
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        fwd_limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteChatUser(TLRequest):
    """
    [Read `messages.deleteChatUser` docs](https://core.telegram.org/method/messages.deleteChatUser).

    Generated from the following TL definition:
    ```tl
    messages.deleteChatUser#a2185cab flags:# revoke_history:flags.0?true chat_id:long user_id:InputUser = Updates
    ```
    """
    def __new__(
        cls,
        revoke_history: bool,
        chat_id: int,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CreateChat(TLRequest):
    """
    [Read `messages.createChat` docs](https://core.telegram.org/method/messages.createChat).

    Generated from the following TL definition:
    ```tl
    messages.createChat#92ceddd4 flags:# users:Vector<InputUser> title:string ttl_period:flags.0?int = messages.InvitedUsers
    ```
    """
    def __new__(
        cls,
        users: Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
        title: str,
        ttl_period: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDhConfig(TLRequest):
    """
    [Read `messages.getDhConfig` docs](https://core.telegram.org/method/messages.getDhConfig).

    Generated from the following TL definition:
    ```tl
    messages.getDhConfig#26cf8950 version:int random_length:int = messages.DhConfig
    ```
    """
    def __new__(
        cls,
        version: int,
        random_length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestEncryption(TLRequest):
    """
    [Read `messages.requestEncryption` docs](https://core.telegram.org/method/messages.requestEncryption).

    Generated from the following TL definition:
    ```tl
    messages.requestEncryption#f64daf43 user_id:InputUser random_id:int g_a:bytes = EncryptedChat
    ```
    """
    def __new__(
        cls,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        random_id: int,
        g_a: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AcceptEncryption(TLRequest):
    """
    [Read `messages.acceptEncryption` docs](https://core.telegram.org/method/messages.acceptEncryption).

    Generated from the following TL definition:
    ```tl
    messages.acceptEncryption#3dbc0415 peer:InputEncryptedChat g_b:bytes key_fingerprint:long = EncryptedChat
    ```
    """
    def __new__(
        cls,
        peer: types.InputEncryptedChat,
        g_b: bytes,
        key_fingerprint: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DiscardEncryption(TLRequest):
    """
    [Read `messages.discardEncryption` docs](https://core.telegram.org/method/messages.discardEncryption).

    Generated from the following TL definition:
    ```tl
    messages.discardEncryption#f393aea0 flags:# delete_history:flags.0?true chat_id:int = Bool
    ```
    """
    def __new__(
        cls,
        delete_history: bool,
        chat_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetEncryptedTyping(TLRequest):
    """
    [Read `messages.setEncryptedTyping` docs](https://core.telegram.org/method/messages.setEncryptedTyping).

    Generated from the following TL definition:
    ```tl
    messages.setEncryptedTyping#791451ed peer:InputEncryptedChat typing:Bool = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputEncryptedChat,
        typing: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReadEncryptedHistory(TLRequest):
    """
    [Read `messages.readEncryptedHistory` docs](https://core.telegram.org/method/messages.readEncryptedHistory).

    Generated from the following TL definition:
    ```tl
    messages.readEncryptedHistory#7f4b690a peer:InputEncryptedChat max_date:int = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputEncryptedChat,
        max_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendEncrypted(TLRequest):
    """
    [Read `messages.sendEncrypted` docs](https://core.telegram.org/method/messages.sendEncrypted).

    Generated from the following TL definition:
    ```tl
    messages.sendEncrypted#44fa7a15 flags:# silent:flags.0?true peer:InputEncryptedChat random_id:long data:bytes = messages.SentEncryptedMessage
    ```
    """
    def __new__(
        cls,
        silent: bool,
        peer: types.InputEncryptedChat,
        random_id: int,
        data: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendEncryptedFile(TLRequest):
    """
    [Read `messages.sendEncryptedFile` docs](https://core.telegram.org/method/messages.sendEncryptedFile).

    Generated from the following TL definition:
    ```tl
    messages.sendEncryptedFile#5559481d flags:# silent:flags.0?true peer:InputEncryptedChat random_id:long data:bytes file:InputEncryptedFile = messages.SentEncryptedMessage
    ```
    """
    def __new__(
        cls,
        silent: bool,
        peer: types.InputEncryptedChat,
        random_id: int,
        data: bytes,
        file: types.InputEncryptedFileEmpty | types.InputEncryptedFileUploaded | types.InputEncryptedFile | types.InputEncryptedFileBigUploaded,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendEncryptedService(TLRequest):
    """
    [Read `messages.sendEncryptedService` docs](https://core.telegram.org/method/messages.sendEncryptedService).

    Generated from the following TL definition:
    ```tl
    messages.sendEncryptedService#32d439a4 peer:InputEncryptedChat random_id:long data:bytes = messages.SentEncryptedMessage
    ```
    """
    def __new__(
        cls,
        peer: types.InputEncryptedChat,
        random_id: int,
        data: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReceivedQueue(TLRequest):
    """
    [Read `messages.receivedQueue` docs](https://core.telegram.org/method/messages.receivedQueue).

    Generated from the following TL definition:
    ```tl
    messages.receivedQueue#55a5bb66 max_qts:int = Vector<long>
    ```
    """
    def __new__(
        cls,
        max_qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportEncryptedSpam(TLRequest):
    """
    [Read `messages.reportEncryptedSpam` docs](https://core.telegram.org/method/messages.reportEncryptedSpam).

    Generated from the following TL definition:
    ```tl
    messages.reportEncryptedSpam#4b0c8c0f peer:InputEncryptedChat = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputEncryptedChat,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReadMessageContents(TLRequest):
    """
    [Read `messages.readMessageContents` docs](https://core.telegram.org/method/messages.readMessageContents).

    Generated from the following TL definition:
    ```tl
    messages.readMessageContents#36a73f77 id:Vector<int> = messages.AffectedMessages
    ```
    """
    def __new__(
        cls,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStickers(TLRequest):
    """
    [Read `messages.getStickers` docs](https://core.telegram.org/method/messages.getStickers).

    Generated from the following TL definition:
    ```tl
    messages.getStickers#d5a5d3a1 emoticon:string hash:long = messages.Stickers
    ```
    """
    def __new__(
        cls,
        emoticon: str,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAllStickers(TLRequest):
    """
    [Read `messages.getAllStickers` docs](https://core.telegram.org/method/messages.getAllStickers).

    Generated from the following TL definition:
    ```tl
    messages.getAllStickers#b8a0a1a8 hash:long = messages.AllStickers
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetWebPagePreview(TLRequest):
    """
    [Read `messages.getWebPagePreview` docs](https://core.telegram.org/method/messages.getWebPagePreview).

    Generated from the following TL definition:
    ```tl
    messages.getWebPagePreview#570d6f6f flags:# message:string entities:flags.3?Vector<MessageEntity> = messages.WebPagePreview
    ```
    """
    def __new__(
        cls,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportChatInvite(TLRequest):
    """
    [Read `messages.exportChatInvite` docs](https://core.telegram.org/method/messages.exportChatInvite).

    Generated from the following TL definition:
    ```tl
    messages.exportChatInvite#a455de90 flags:# legacy_revoke_permanent:flags.2?true request_needed:flags.3?true peer:InputPeer expire_date:flags.0?int usage_limit:flags.1?int title:flags.4?string subscription_pricing:flags.5?StarsSubscriptionPricing = ExportedChatInvite
    ```
    """
    def __new__(
        cls,
        legacy_revoke_permanent: bool,
        request_needed: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        expire_date: Optional[int],
        usage_limit: Optional[int],
        title: Optional[str],
        subscription_pricing: Optional[types.StarsSubscriptionPricing],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckChatInvite(TLRequest):
    """
    [Read `messages.checkChatInvite` docs](https://core.telegram.org/method/messages.checkChatInvite).

    Generated from the following TL definition:
    ```tl
    messages.checkChatInvite#3eadb1bb hash:string = ChatInvite
    ```
    """
    def __new__(
        cls,
        hash: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ImportChatInvite(TLRequest):
    """
    [Read `messages.importChatInvite` docs](https://core.telegram.org/method/messages.importChatInvite).

    Generated from the following TL definition:
    ```tl
    messages.importChatInvite#6c50051c hash:string = Updates
    ```
    """
    def __new__(
        cls,
        hash: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStickerSet(TLRequest):
    """
    [Read `messages.getStickerSet` docs](https://core.telegram.org/method/messages.getStickerSet).

    Generated from the following TL definition:
    ```tl
    messages.getStickerSet#c8a0ec74 stickerset:InputStickerSet hash:int = messages.StickerSet
    ```
    """
    def __new__(
        cls,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InstallStickerSet(TLRequest):
    """
    [Read `messages.installStickerSet` docs](https://core.telegram.org/method/messages.installStickerSet).

    Generated from the following TL definition:
    ```tl
    messages.installStickerSet#c78fe460 stickerset:InputStickerSet archived:Bool = messages.StickerSetInstallResult
    ```
    """
    def __new__(
        cls,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
        archived: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UninstallStickerSet(TLRequest):
    """
    [Read `messages.uninstallStickerSet` docs](https://core.telegram.org/method/messages.uninstallStickerSet).

    Generated from the following TL definition:
    ```tl
    messages.uninstallStickerSet#f96e55de stickerset:InputStickerSet = Bool
    ```
    """
    def __new__(
        cls,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StartBot(TLRequest):
    """
    [Read `messages.startBot` docs](https://core.telegram.org/method/messages.startBot).

    Generated from the following TL definition:
    ```tl
    messages.startBot#e6df7378 bot:InputUser peer:InputPeer random_id:long start_param:string = Updates
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        random_id: int,
        start_param: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMessagesViews(TLRequest):
    """
    [Read `messages.getMessagesViews` docs](https://core.telegram.org/method/messages.getMessagesViews).

    Generated from the following TL definition:
    ```tl
    messages.getMessagesViews#5784d3e1 peer:InputPeer id:Vector<int> increment:Bool = messages.MessageViews
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
        increment: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditChatAdmin(TLRequest):
    """
    [Read `messages.editChatAdmin` docs](https://core.telegram.org/method/messages.editChatAdmin).

    Generated from the following TL definition:
    ```tl
    messages.editChatAdmin#a85bd1c2 chat_id:long user_id:InputUser is_admin:Bool = Bool
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        is_admin: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MigrateChat(TLRequest):
    """
    [Read `messages.migrateChat` docs](https://core.telegram.org/method/messages.migrateChat).

    Generated from the following TL definition:
    ```tl
    messages.migrateChat#a2875319 chat_id:long = Updates
    ```
    """
    def __new__(
        cls,
        chat_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchGlobal(TLRequest):
    """
    [Read `messages.searchGlobal` docs](https://core.telegram.org/method/messages.searchGlobal).

    Generated from the following TL definition:
    ```tl
    messages.searchGlobal#4bc6589a flags:# broadcasts_only:flags.1?true groups_only:flags.2?true users_only:flags.3?true folder_id:flags.0?int q:string filter:MessagesFilter min_date:int max_date:int offset_rate:int offset_peer:InputPeer offset_id:int limit:int = messages.Messages
    ```
    """
    def __new__(
        cls,
        broadcasts_only: bool,
        groups_only: bool,
        users_only: bool,
        folder_id: Optional[int],
        q: str,
        filter: types.InputMessagesFilterEmpty | types.InputMessagesFilterPhotos | types.InputMessagesFilterVideo | types.InputMessagesFilterPhotoVideo | types.InputMessagesFilterDocument | types.InputMessagesFilterUrl | types.InputMessagesFilterGif | types.InputMessagesFilterVoice | types.InputMessagesFilterMusic | types.InputMessagesFilterChatPhotos | types.InputMessagesFilterPhoneCalls | types.InputMessagesFilterRoundVoice | types.InputMessagesFilterRoundVideo | types.InputMessagesFilterMyMentions | types.InputMessagesFilterGeo | types.InputMessagesFilterContacts | types.InputMessagesFilterPinned,
        min_date: int,
        max_date: int,
        offset_rate: int,
        offset_peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        offset_id: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReorderStickerSets(TLRequest):
    """
    [Read `messages.reorderStickerSets` docs](https://core.telegram.org/method/messages.reorderStickerSets).

    Generated from the following TL definition:
    ```tl
    messages.reorderStickerSets#78337739 flags:# masks:flags.0?true emojis:flags.1?true order:Vector<long> = Bool
    ```
    """
    def __new__(
        cls,
        masks: bool,
        emojis: bool,
        order: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDocumentByHash(TLRequest):
    """
    [Read `messages.getDocumentByHash` docs](https://core.telegram.org/method/messages.getDocumentByHash).

    Generated from the following TL definition:
    ```tl
    messages.getDocumentByHash#b1f2061f sha256:bytes size:long mime_type:string = Document
    ```
    """
    def __new__(
        cls,
        sha256: bytes,
        size: int,
        mime_type: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSavedGifs(TLRequest):
    """
    [Read `messages.getSavedGifs` docs](https://core.telegram.org/method/messages.getSavedGifs).

    Generated from the following TL definition:
    ```tl
    messages.getSavedGifs#5cf09635 hash:long = messages.SavedGifs
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveGif(TLRequest):
    """
    [Read `messages.saveGif` docs](https://core.telegram.org/method/messages.saveGif).

    Generated from the following TL definition:
    ```tl
    messages.saveGif#327a30cb id:InputDocument unsave:Bool = Bool
    ```
    """
    def __new__(
        cls,
        id: types.InputDocumentEmpty | types.InputDocument,
        unsave: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetInlineBotResults(TLRequest):
    """
    [Read `messages.getInlineBotResults` docs](https://core.telegram.org/method/messages.getInlineBotResults).

    Generated from the following TL definition:
    ```tl
    messages.getInlineBotResults#514e999d flags:# bot:InputUser peer:InputPeer geo_point:flags.0?InputGeoPoint query:string offset:string = messages.BotResults
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        geo_point: Optional[types.InputGeoPointEmpty | types.InputGeoPoint],
        query: str,
        offset: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetInlineBotResults(TLRequest):
    """
    [Read `messages.setInlineBotResults` docs](https://core.telegram.org/method/messages.setInlineBotResults).

    Generated from the following TL definition:
    ```tl
    messages.setInlineBotResults#bb12a419 flags:# gallery:flags.0?true private:flags.1?true query_id:long results:Vector<InputBotInlineResult> cache_time:int next_offset:flags.2?string switch_pm:flags.3?InlineBotSwitchPM switch_webview:flags.4?InlineBotWebView = Bool
    ```
    """
    def __new__(
        cls,
        gallery: bool,
        private: bool,
        query_id: int,
        results: Sequence[types.InputBotInlineResult | types.InputBotInlineResultPhoto | types.InputBotInlineResultDocument | types.InputBotInlineResultGame],
        cache_time: int,
        next_offset: Optional[str],
        switch_pm: Optional[types.InlineBotSwitchPm],
        switch_webview: Optional[types.InlineBotWebView],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendInlineBotResult(TLRequest):
    """
    [Read `messages.sendInlineBotResult` docs](https://core.telegram.org/method/messages.sendInlineBotResult).

    Generated from the following TL definition:
    ```tl
    messages.sendInlineBotResult#c0cf7646 flags:# silent:flags.5?true background:flags.6?true clear_draft:flags.7?true hide_via:flags.11?true peer:InputPeer reply_to:flags.0?InputReplyTo random_id:long query_id:long id:string schedule_date:flags.10?int send_as:flags.13?InputPeer quick_reply_shortcut:flags.17?InputQuickReplyShortcut allow_paid_stars:flags.21?long = Updates
    ```
    """
    def __new__(
        cls,
        silent: bool,
        background: bool,
        clear_draft: bool,
        hide_via: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        reply_to: Optional[types.InputReplyToMessage | types.InputReplyToStory | types.InputReplyToMonoForum],
        random_id: int,
        query_id: int,
        id: str,
        schedule_date: Optional[int],
        send_as: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        quick_reply_shortcut: Optional[types.InputQuickReplyShortcut | types.InputQuickReplyShortcutId],
        allow_paid_stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMessageEditData(TLRequest):
    """
    [Read `messages.getMessageEditData` docs](https://core.telegram.org/method/messages.getMessageEditData).

    Generated from the following TL definition:
    ```tl
    messages.getMessageEditData#fda68d36 peer:InputPeer id:int = messages.MessageEditData
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditMessage(TLRequest):
    """
    [Read `messages.editMessage` docs](https://core.telegram.org/method/messages.editMessage).

    Generated from the following TL definition:
    ```tl
    messages.editMessage#51e842e1 flags:# no_webpage:flags.1?true invert_media:flags.16?true peer:InputPeer id:int message:flags.11?string media:flags.14?InputMedia reply_markup:flags.2?ReplyMarkup entities:flags.3?Vector<MessageEntity> schedule_date:flags.15?int schedule_repeat_period:flags.18?int quick_reply_shortcut_id:flags.17?int = Updates
    ```
    """
    def __new__(
        cls,
        no_webpage: bool,
        invert_media: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
        message: Optional[str],
        media: Optional[types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice],
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        schedule_date: Optional[int],
        schedule_repeat_period: Optional[int],
        quick_reply_shortcut_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditInlineBotMessage(TLRequest):
    """
    [Read `messages.editInlineBotMessage` docs](https://core.telegram.org/method/messages.editInlineBotMessage).

    Generated from the following TL definition:
    ```tl
    messages.editInlineBotMessage#83557dba flags:# no_webpage:flags.1?true invert_media:flags.16?true id:InputBotInlineMessageID message:flags.11?string media:flags.14?InputMedia reply_markup:flags.2?ReplyMarkup entities:flags.3?Vector<MessageEntity> = Bool
    ```
    """
    def __new__(
        cls,
        no_webpage: bool,
        invert_media: bool,
        id: types.InputBotInlineMessageId | types.InputBotInlineMessageId64,
        message: Optional[str],
        media: Optional[types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice],
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetBotCallbackAnswer(TLRequest):
    """
    [Read `messages.getBotCallbackAnswer` docs](https://core.telegram.org/method/messages.getBotCallbackAnswer).

    Generated from the following TL definition:
    ```tl
    messages.getBotCallbackAnswer#9342ca07 flags:# game:flags.1?true peer:InputPeer msg_id:int data:flags.0?bytes password:flags.2?InputCheckPasswordSRP = messages.BotCallbackAnswer
    ```
    """
    def __new__(
        cls,
        game: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        data: Optional[bytes],
        password: Optional[types.InputCheckPasswordEmpty | types.InputCheckPasswordSrp],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetBotCallbackAnswer(TLRequest):
    """
    [Read `messages.setBotCallbackAnswer` docs](https://core.telegram.org/method/messages.setBotCallbackAnswer).

    Generated from the following TL definition:
    ```tl
    messages.setBotCallbackAnswer#d58f130a flags:# alert:flags.1?true query_id:long message:flags.0?string url:flags.2?string cache_time:int = Bool
    ```
    """
    def __new__(
        cls,
        alert: bool,
        query_id: int,
        message: Optional[str],
        url: Optional[str],
        cache_time: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPeerDialogs(TLRequest):
    """
    [Read `messages.getPeerDialogs` docs](https://core.telegram.org/method/messages.getPeerDialogs).

    Generated from the following TL definition:
    ```tl
    messages.getPeerDialogs#e470bcfd peers:Vector<InputDialogPeer> = messages.PeerDialogs
    ```
    """
    def __new__(
        cls,
        peers: Sequence[types.InputDialogPeer | types.InputDialogPeerFolder],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveDraft(TLRequest):
    """
    [Read `messages.saveDraft` docs](https://core.telegram.org/method/messages.saveDraft).

    Generated from the following TL definition:
    ```tl
    messages.saveDraft#54ae308e flags:# no_webpage:flags.1?true invert_media:flags.6?true reply_to:flags.4?InputReplyTo peer:InputPeer message:string entities:flags.3?Vector<MessageEntity> media:flags.5?InputMedia effect:flags.7?long suggested_post:flags.8?SuggestedPost = Bool
    ```
    """
    def __new__(
        cls,
        no_webpage: bool,
        invert_media: bool,
        reply_to: Optional[types.InputReplyToMessage | types.InputReplyToStory | types.InputReplyToMonoForum],
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        media: Optional[types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice],
        effect: Optional[int],
        suggested_post: Optional[types.SuggestedPost],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAllDrafts(TLRequest):
    """
    [Read `messages.getAllDrafts` docs](https://core.telegram.org/method/messages.getAllDrafts).

    Generated from the following TL definition:
    ```tl
    messages.getAllDrafts#6a3f8d65 = Updates
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetFeaturedStickers(TLRequest):
    """
    [Read `messages.getFeaturedStickers` docs](https://core.telegram.org/method/messages.getFeaturedStickers).

    Generated from the following TL definition:
    ```tl
    messages.getFeaturedStickers#64780b14 hash:long = messages.FeaturedStickers
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReadFeaturedStickers(TLRequest):
    """
    [Read `messages.readFeaturedStickers` docs](https://core.telegram.org/method/messages.readFeaturedStickers).

    Generated from the following TL definition:
    ```tl
    messages.readFeaturedStickers#5b118126 id:Vector<long> = Bool
    ```
    """
    def __new__(
        cls,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetRecentStickers(TLRequest):
    """
    [Read `messages.getRecentStickers` docs](https://core.telegram.org/method/messages.getRecentStickers).

    Generated from the following TL definition:
    ```tl
    messages.getRecentStickers#9da9403b flags:# attached:flags.0?true hash:long = messages.RecentStickers
    ```
    """
    def __new__(
        cls,
        attached: bool,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveRecentSticker(TLRequest):
    """
    [Read `messages.saveRecentSticker` docs](https://core.telegram.org/method/messages.saveRecentSticker).

    Generated from the following TL definition:
    ```tl
    messages.saveRecentSticker#392718f8 flags:# attached:flags.0?true id:InputDocument unsave:Bool = Bool
    ```
    """
    def __new__(
        cls,
        attached: bool,
        id: types.InputDocumentEmpty | types.InputDocument,
        unsave: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ClearRecentStickers(TLRequest):
    """
    [Read `messages.clearRecentStickers` docs](https://core.telegram.org/method/messages.clearRecentStickers).

    Generated from the following TL definition:
    ```tl
    messages.clearRecentStickers#8999602d flags:# attached:flags.0?true = Bool
    ```
    """
    def __new__(
        cls,
        attached: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetArchivedStickers(TLRequest):
    """
    [Read `messages.getArchivedStickers` docs](https://core.telegram.org/method/messages.getArchivedStickers).

    Generated from the following TL definition:
    ```tl
    messages.getArchivedStickers#57f17692 flags:# masks:flags.0?true emojis:flags.1?true offset_id:long limit:int = messages.ArchivedStickers
    ```
    """
    def __new__(
        cls,
        masks: bool,
        emojis: bool,
        offset_id: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMaskStickers(TLRequest):
    """
    [Read `messages.getMaskStickers` docs](https://core.telegram.org/method/messages.getMaskStickers).

    Generated from the following TL definition:
    ```tl
    messages.getMaskStickers#640f82b8 hash:long = messages.AllStickers
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAttachedStickers(TLRequest):
    """
    [Read `messages.getAttachedStickers` docs](https://core.telegram.org/method/messages.getAttachedStickers).

    Generated from the following TL definition:
    ```tl
    messages.getAttachedStickers#cc5b67cc media:InputStickeredMedia = Vector<StickerSetCovered>
    ```
    """
    def __new__(
        cls,
        media: types.InputStickeredMediaPhoto | types.InputStickeredMediaDocument,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetGameScore(TLRequest):
    """
    [Read `messages.setGameScore` docs](https://core.telegram.org/method/messages.setGameScore).

    Generated from the following TL definition:
    ```tl
    messages.setGameScore#8ef8ecc0 flags:# edit_message:flags.0?true force:flags.1?true peer:InputPeer id:int user_id:InputUser score:int = Updates
    ```
    """
    def __new__(
        cls,
        edit_message: bool,
        force: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        score: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetInlineGameScore(TLRequest):
    """
    [Read `messages.setInlineGameScore` docs](https://core.telegram.org/method/messages.setInlineGameScore).

    Generated from the following TL definition:
    ```tl
    messages.setInlineGameScore#15ad9f64 flags:# edit_message:flags.0?true force:flags.1?true id:InputBotInlineMessageID user_id:InputUser score:int = Bool
    ```
    """
    def __new__(
        cls,
        edit_message: bool,
        force: bool,
        id: types.InputBotInlineMessageId | types.InputBotInlineMessageId64,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        score: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetGameHighScores(TLRequest):
    """
    [Read `messages.getGameHighScores` docs](https://core.telegram.org/method/messages.getGameHighScores).

    Generated from the following TL definition:
    ```tl
    messages.getGameHighScores#e822649d peer:InputPeer id:int user_id:InputUser = messages.HighScores
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetInlineGameHighScores(TLRequest):
    """
    [Read `messages.getInlineGameHighScores` docs](https://core.telegram.org/method/messages.getInlineGameHighScores).

    Generated from the following TL definition:
    ```tl
    messages.getInlineGameHighScores#f635e1b id:InputBotInlineMessageID user_id:InputUser = messages.HighScores
    ```
    """
    def __new__(
        cls,
        id: types.InputBotInlineMessageId | types.InputBotInlineMessageId64,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetCommonChats(TLRequest):
    """
    [Read `messages.getCommonChats` docs](https://core.telegram.org/method/messages.getCommonChats).

    Generated from the following TL definition:
    ```tl
    messages.getCommonChats#e40ca104 user_id:InputUser max_id:long limit:int = messages.Chats
    ```
    """
    def __new__(
        cls,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        max_id: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetWebPage(TLRequest):
    """
    [Read `messages.getWebPage` docs](https://core.telegram.org/method/messages.getWebPage).

    Generated from the following TL definition:
    ```tl
    messages.getWebPage#8d9692a3 url:string hash:int = messages.WebPage
    ```
    """
    def __new__(
        cls,
        url: str,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleDialogPin(TLRequest):
    """
    [Read `messages.toggleDialogPin` docs](https://core.telegram.org/method/messages.toggleDialogPin).

    Generated from the following TL definition:
    ```tl
    messages.toggleDialogPin#a731e257 flags:# pinned:flags.0?true peer:InputDialogPeer = Bool
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        peer: types.InputDialogPeer | types.InputDialogPeerFolder,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReorderPinnedDialogs(TLRequest):
    """
    [Read `messages.reorderPinnedDialogs` docs](https://core.telegram.org/method/messages.reorderPinnedDialogs).

    Generated from the following TL definition:
    ```tl
    messages.reorderPinnedDialogs#3b1adf37 flags:# force:flags.0?true folder_id:int order:Vector<InputDialogPeer> = Bool
    ```
    """
    def __new__(
        cls,
        force: bool,
        folder_id: int,
        order: Sequence[types.InputDialogPeer | types.InputDialogPeerFolder],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPinnedDialogs(TLRequest):
    """
    [Read `messages.getPinnedDialogs` docs](https://core.telegram.org/method/messages.getPinnedDialogs).

    Generated from the following TL definition:
    ```tl
    messages.getPinnedDialogs#d6b94df2 folder_id:int = messages.PeerDialogs
    ```
    """
    def __new__(
        cls,
        folder_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetBotShippingResults(TLRequest):
    """
    [Read `messages.setBotShippingResults` docs](https://core.telegram.org/method/messages.setBotShippingResults).

    Generated from the following TL definition:
    ```tl
    messages.setBotShippingResults#e5f672fa flags:# query_id:long error:flags.0?string shipping_options:flags.1?Vector<ShippingOption> = Bool
    ```
    """
    def __new__(
        cls,
        query_id: int,
        error: Optional[str],
        shipping_options: Optional[Sequence[types.ShippingOption]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetBotPrecheckoutResults(TLRequest):
    """
    [Read `messages.setBotPrecheckoutResults` docs](https://core.telegram.org/method/messages.setBotPrecheckoutResults).

    Generated from the following TL definition:
    ```tl
    messages.setBotPrecheckoutResults#9c2dd95 flags:# success:flags.1?true query_id:long error:flags.0?string = Bool
    ```
    """
    def __new__(
        cls,
        success: bool,
        query_id: int,
        error: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UploadMedia(TLRequest):
    """
    [Read `messages.uploadMedia` docs](https://core.telegram.org/method/messages.uploadMedia).

    Generated from the following TL definition:
    ```tl
    messages.uploadMedia#14967978 flags:# business_connection_id:flags.0?string peer:InputPeer media:InputMedia = MessageMedia
    ```
    """
    def __new__(
        cls,
        business_connection_id: Optional[str],
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        media: types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendScreenshotNotification(TLRequest):
    """
    [Read `messages.sendScreenshotNotification` docs](https://core.telegram.org/method/messages.sendScreenshotNotification).

    Generated from the following TL definition:
    ```tl
    messages.sendScreenshotNotification#a1405817 peer:InputPeer reply_to:InputReplyTo random_id:long = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        reply_to: types.InputReplyToMessage | types.InputReplyToStory | types.InputReplyToMonoForum,
        random_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetFavedStickers(TLRequest):
    """
    [Read `messages.getFavedStickers` docs](https://core.telegram.org/method/messages.getFavedStickers).

    Generated from the following TL definition:
    ```tl
    messages.getFavedStickers#4f1aaa9 hash:long = messages.FavedStickers
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FaveSticker(TLRequest):
    """
    [Read `messages.faveSticker` docs](https://core.telegram.org/method/messages.faveSticker).

    Generated from the following TL definition:
    ```tl
    messages.faveSticker#b9ffc55b id:InputDocument unfave:Bool = Bool
    ```
    """
    def __new__(
        cls,
        id: types.InputDocumentEmpty | types.InputDocument,
        unfave: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetUnreadMentions(TLRequest):
    """
    [Read `messages.getUnreadMentions` docs](https://core.telegram.org/method/messages.getUnreadMentions).

    Generated from the following TL definition:
    ```tl
    messages.getUnreadMentions#f107e790 flags:# peer:InputPeer top_msg_id:flags.0?int offset_id:int add_offset:int limit:int max_id:int min_id:int = messages.Messages
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        top_msg_id: Optional[int],
        offset_id: int,
        add_offset: int,
        limit: int,
        max_id: int,
        min_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReadMentions(TLRequest):
    """
    [Read `messages.readMentions` docs](https://core.telegram.org/method/messages.readMentions).

    Generated from the following TL definition:
    ```tl
    messages.readMentions#36e5bf4d flags:# peer:InputPeer top_msg_id:flags.0?int = messages.AffectedHistory
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        top_msg_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetRecentLocations(TLRequest):
    """
    [Read `messages.getRecentLocations` docs](https://core.telegram.org/method/messages.getRecentLocations).

    Generated from the following TL definition:
    ```tl
    messages.getRecentLocations#702a40e0 peer:InputPeer limit:int hash:long = messages.Messages
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        limit: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMultiMedia(TLRequest):
    """
    [Read `messages.sendMultiMedia` docs](https://core.telegram.org/method/messages.sendMultiMedia).

    Generated from the following TL definition:
    ```tl
    messages.sendMultiMedia#1bf89d74 flags:# silent:flags.5?true background:flags.6?true clear_draft:flags.7?true noforwards:flags.14?true update_stickersets_order:flags.15?true invert_media:flags.16?true allow_paid_floodskip:flags.19?true peer:InputPeer reply_to:flags.0?InputReplyTo multi_media:Vector<InputSingleMedia> schedule_date:flags.10?int send_as:flags.13?InputPeer quick_reply_shortcut:flags.17?InputQuickReplyShortcut effect:flags.18?long allow_paid_stars:flags.21?long = Updates
    ```
    """
    def __new__(
        cls,
        silent: bool,
        background: bool,
        clear_draft: bool,
        noforwards: bool,
        update_stickersets_order: bool,
        invert_media: bool,
        allow_paid_floodskip: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        reply_to: Optional[types.InputReplyToMessage | types.InputReplyToStory | types.InputReplyToMonoForum],
        multi_media: Sequence[types.InputSingleMedia],
        schedule_date: Optional[int],
        send_as: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        quick_reply_shortcut: Optional[types.InputQuickReplyShortcut | types.InputQuickReplyShortcutId],
        effect: Optional[int],
        allow_paid_stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UploadEncryptedFile(TLRequest):
    """
    [Read `messages.uploadEncryptedFile` docs](https://core.telegram.org/method/messages.uploadEncryptedFile).

    Generated from the following TL definition:
    ```tl
    messages.uploadEncryptedFile#5057c497 peer:InputEncryptedChat file:InputEncryptedFile = EncryptedFile
    ```
    """
    def __new__(
        cls,
        peer: types.InputEncryptedChat,
        file: types.InputEncryptedFileEmpty | types.InputEncryptedFileUploaded | types.InputEncryptedFile | types.InputEncryptedFileBigUploaded,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchStickerSets(TLRequest):
    """
    [Read `messages.searchStickerSets` docs](https://core.telegram.org/method/messages.searchStickerSets).

    Generated from the following TL definition:
    ```tl
    messages.searchStickerSets#35705b8a flags:# exclude_featured:flags.0?true q:string hash:long = messages.FoundStickerSets
    ```
    """
    def __new__(
        cls,
        exclude_featured: bool,
        q: str,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSplitRanges(TLRequest):
    """
    [Read `messages.getSplitRanges` docs](https://core.telegram.org/method/messages.getSplitRanges).

    Generated from the following TL definition:
    ```tl
    messages.getSplitRanges#1cff7e08 = Vector<MessageRange>
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MarkDialogUnread(TLRequest):
    """
    [Read `messages.markDialogUnread` docs](https://core.telegram.org/method/messages.markDialogUnread).

    Generated from the following TL definition:
    ```tl
    messages.markDialogUnread#8c5006f8 flags:# unread:flags.0?true parent_peer:flags.1?InputPeer peer:InputDialogPeer = Bool
    ```
    """
    def __new__(
        cls,
        unread: bool,
        parent_peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        peer: types.InputDialogPeer | types.InputDialogPeerFolder,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDialogUnreadMarks(TLRequest):
    """
    [Read `messages.getDialogUnreadMarks` docs](https://core.telegram.org/method/messages.getDialogUnreadMarks).

    Generated from the following TL definition:
    ```tl
    messages.getDialogUnreadMarks#21202222 flags:# parent_peer:flags.0?InputPeer = Vector<DialogPeer>
    ```
    """
    def __new__(
        cls,
        parent_peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ClearAllDrafts(TLRequest):
    """
    [Read `messages.clearAllDrafts` docs](https://core.telegram.org/method/messages.clearAllDrafts).

    Generated from the following TL definition:
    ```tl
    messages.clearAllDrafts#7e58ee9c = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePinnedMessage(TLRequest):
    """
    [Read `messages.updatePinnedMessage` docs](https://core.telegram.org/method/messages.updatePinnedMessage).

    Generated from the following TL definition:
    ```tl
    messages.updatePinnedMessage#d2aaf7ec flags:# silent:flags.0?true unpin:flags.1?true pm_oneside:flags.2?true peer:InputPeer id:int = Updates
    ```
    """
    def __new__(
        cls,
        silent: bool,
        unpin: bool,
        pm_oneside: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendVote(TLRequest):
    """
    [Read `messages.sendVote` docs](https://core.telegram.org/method/messages.sendVote).

    Generated from the following TL definition:
    ```tl
    messages.sendVote#10ea6184 peer:InputPeer msg_id:int options:Vector<bytes> = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        options: Sequence[bytes],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPollResults(TLRequest):
    """
    [Read `messages.getPollResults` docs](https://core.telegram.org/method/messages.getPollResults).

    Generated from the following TL definition:
    ```tl
    messages.getPollResults#73bb643b peer:InputPeer msg_id:int = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetOnlines(TLRequest):
    """
    [Read `messages.getOnlines` docs](https://core.telegram.org/method/messages.getOnlines).

    Generated from the following TL definition:
    ```tl
    messages.getOnlines#6e2be050 peer:InputPeer = ChatOnlines
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditChatAbout(TLRequest):
    """
    [Read `messages.editChatAbout` docs](https://core.telegram.org/method/messages.editChatAbout).

    Generated from the following TL definition:
    ```tl
    messages.editChatAbout#def60797 peer:InputPeer about:string = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        about: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditChatDefaultBannedRights(TLRequest):
    """
    [Read `messages.editChatDefaultBannedRights` docs](https://core.telegram.org/method/messages.editChatDefaultBannedRights).

    Generated from the following TL definition:
    ```tl
    messages.editChatDefaultBannedRights#a5866b41 peer:InputPeer banned_rights:ChatBannedRights = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        banned_rights: types.ChatBannedRights,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetEmojiKeywords(TLRequest):
    """
    [Read `messages.getEmojiKeywords` docs](https://core.telegram.org/method/messages.getEmojiKeywords).

    Generated from the following TL definition:
    ```tl
    messages.getEmojiKeywords#35a0e062 lang_code:string = EmojiKeywordsDifference
    ```
    """
    def __new__(
        cls,
        lang_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetEmojiKeywordsDifference(TLRequest):
    """
    [Read `messages.getEmojiKeywordsDifference` docs](https://core.telegram.org/method/messages.getEmojiKeywordsDifference).

    Generated from the following TL definition:
    ```tl
    messages.getEmojiKeywordsDifference#1508b6af lang_code:string from_version:int = EmojiKeywordsDifference
    ```
    """
    def __new__(
        cls,
        lang_code: str,
        from_version: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetEmojiKeywordsLanguages(TLRequest):
    """
    [Read `messages.getEmojiKeywordsLanguages` docs](https://core.telegram.org/method/messages.getEmojiKeywordsLanguages).

    Generated from the following TL definition:
    ```tl
    messages.getEmojiKeywordsLanguages#4e9963b2 lang_codes:Vector<string> = Vector<EmojiLanguage>
    ```
    """
    def __new__(
        cls,
        lang_codes: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetEmojiUrl(TLRequest):
    """
    [Read `messages.getEmojiURL` docs](https://core.telegram.org/method/messages.getEmojiURL).

    Generated from the following TL definition:
    ```tl
    messages.getEmojiURL#d5b10c26 lang_code:string = EmojiURL
    ```
    """
    def __new__(
        cls,
        lang_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSearchCounters(TLRequest):
    """
    [Read `messages.getSearchCounters` docs](https://core.telegram.org/method/messages.getSearchCounters).

    Generated from the following TL definition:
    ```tl
    messages.getSearchCounters#1bbcf300 flags:# peer:InputPeer saved_peer_id:flags.2?InputPeer top_msg_id:flags.0?int filters:Vector<MessagesFilter> = Vector<messages.SearchCounter>
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        saved_peer_id: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        top_msg_id: Optional[int],
        filters: Sequence[types.InputMessagesFilterEmpty | types.InputMessagesFilterPhotos | types.InputMessagesFilterVideo | types.InputMessagesFilterPhotoVideo | types.InputMessagesFilterDocument | types.InputMessagesFilterUrl | types.InputMessagesFilterGif | types.InputMessagesFilterVoice | types.InputMessagesFilterMusic | types.InputMessagesFilterChatPhotos | types.InputMessagesFilterPhoneCalls | types.InputMessagesFilterRoundVoice | types.InputMessagesFilterRoundVideo | types.InputMessagesFilterMyMentions | types.InputMessagesFilterGeo | types.InputMessagesFilterContacts | types.InputMessagesFilterPinned],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestUrlAuth(TLRequest):
    """
    [Read `messages.requestUrlAuth` docs](https://core.telegram.org/method/messages.requestUrlAuth).

    Generated from the following TL definition:
    ```tl
    messages.requestUrlAuth#198fb446 flags:# peer:flags.1?InputPeer msg_id:flags.1?int button_id:flags.1?int url:flags.2?string = UrlAuthResult
    ```
    """
    def __new__(
        cls,
        peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        msg_id: Optional[int],
        button_id: Optional[int],
        url: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AcceptUrlAuth(TLRequest):
    """
    [Read `messages.acceptUrlAuth` docs](https://core.telegram.org/method/messages.acceptUrlAuth).

    Generated from the following TL definition:
    ```tl
    messages.acceptUrlAuth#b12c7125 flags:# write_allowed:flags.0?true peer:flags.1?InputPeer msg_id:flags.1?int button_id:flags.1?int url:flags.2?string = UrlAuthResult
    ```
    """
    def __new__(
        cls,
        write_allowed: bool,
        peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        msg_id: Optional[int],
        button_id: Optional[int],
        url: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class HidePeerSettingsBar(TLRequest):
    """
    [Read `messages.hidePeerSettingsBar` docs](https://core.telegram.org/method/messages.hidePeerSettingsBar).

    Generated from the following TL definition:
    ```tl
    messages.hidePeerSettingsBar#4facb138 peer:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetScheduledHistory(TLRequest):
    """
    [Read `messages.getScheduledHistory` docs](https://core.telegram.org/method/messages.getScheduledHistory).

    Generated from the following TL definition:
    ```tl
    messages.getScheduledHistory#f516760b peer:InputPeer hash:long = messages.Messages
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetScheduledMessages(TLRequest):
    """
    [Read `messages.getScheduledMessages` docs](https://core.telegram.org/method/messages.getScheduledMessages).

    Generated from the following TL definition:
    ```tl
    messages.getScheduledMessages#bdbb0464 peer:InputPeer id:Vector<int> = messages.Messages
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendScheduledMessages(TLRequest):
    """
    [Read `messages.sendScheduledMessages` docs](https://core.telegram.org/method/messages.sendScheduledMessages).

    Generated from the following TL definition:
    ```tl
    messages.sendScheduledMessages#bd38850a peer:InputPeer id:Vector<int> = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteScheduledMessages(TLRequest):
    """
    [Read `messages.deleteScheduledMessages` docs](https://core.telegram.org/method/messages.deleteScheduledMessages).

    Generated from the following TL definition:
    ```tl
    messages.deleteScheduledMessages#59ae2b16 peer:InputPeer id:Vector<int> = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPollVotes(TLRequest):
    """
    [Read `messages.getPollVotes` docs](https://core.telegram.org/method/messages.getPollVotes).

    Generated from the following TL definition:
    ```tl
    messages.getPollVotes#b86e380e flags:# peer:InputPeer id:int option:flags.0?bytes offset:flags.1?string limit:int = messages.VotesList
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
        option: Optional[bytes],
        offset: Optional[str],
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleStickerSets(TLRequest):
    """
    [Read `messages.toggleStickerSets` docs](https://core.telegram.org/method/messages.toggleStickerSets).

    Generated from the following TL definition:
    ```tl
    messages.toggleStickerSets#b5052fea flags:# uninstall:flags.0?true archive:flags.1?true unarchive:flags.2?true stickersets:Vector<InputStickerSet> = Bool
    ```
    """
    def __new__(
        cls,
        uninstall: bool,
        archive: bool,
        unarchive: bool,
        stickersets: Sequence[types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDialogFilters(TLRequest):
    """
    [Read `messages.getDialogFilters` docs](https://core.telegram.org/method/messages.getDialogFilters).

    Generated from the following TL definition:
    ```tl
    messages.getDialogFilters#efd48c89 = messages.DialogFilters
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSuggestedDialogFilters(TLRequest):
    """
    [Read `messages.getSuggestedDialogFilters` docs](https://core.telegram.org/method/messages.getSuggestedDialogFilters).

    Generated from the following TL definition:
    ```tl
    messages.getSuggestedDialogFilters#a29cd42c = Vector<DialogFilterSuggested>
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDialogFilter(TLRequest):
    """
    [Read `messages.updateDialogFilter` docs](https://core.telegram.org/method/messages.updateDialogFilter).

    Generated from the following TL definition:
    ```tl
    messages.updateDialogFilter#1ad4a04a flags:# id:int filter:flags.0?DialogFilter = Bool
    ```
    """
    def __new__(
        cls,
        id: int,
        filter: Optional[types.DialogFilter | types.DialogFilterDefault | types.DialogFilterChatlist],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDialogFiltersOrder(TLRequest):
    """
    [Read `messages.updateDialogFiltersOrder` docs](https://core.telegram.org/method/messages.updateDialogFiltersOrder).

    Generated from the following TL definition:
    ```tl
    messages.updateDialogFiltersOrder#c563c1e4 order:Vector<int> = Bool
    ```
    """
    def __new__(
        cls,
        order: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetOldFeaturedStickers(TLRequest):
    """
    [Read `messages.getOldFeaturedStickers` docs](https://core.telegram.org/method/messages.getOldFeaturedStickers).

    Generated from the following TL definition:
    ```tl
    messages.getOldFeaturedStickers#7ed094a1 offset:int limit:int hash:long = messages.FeaturedStickers
    ```
    """
    def __new__(
        cls,
        offset: int,
        limit: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetReplies(TLRequest):
    """
    [Read `messages.getReplies` docs](https://core.telegram.org/method/messages.getReplies).

    Generated from the following TL definition:
    ```tl
    messages.getReplies#22ddd30c peer:InputPeer msg_id:int offset_id:int offset_date:int add_offset:int limit:int max_id:int min_id:int hash:long = messages.Messages
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        offset_id: int,
        offset_date: int,
        add_offset: int,
        limit: int,
        max_id: int,
        min_id: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDiscussionMessage(TLRequest):
    """
    [Read `messages.getDiscussionMessage` docs](https://core.telegram.org/method/messages.getDiscussionMessage).

    Generated from the following TL definition:
    ```tl
    messages.getDiscussionMessage#446972fd peer:InputPeer msg_id:int = messages.DiscussionMessage
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReadDiscussion(TLRequest):
    """
    [Read `messages.readDiscussion` docs](https://core.telegram.org/method/messages.readDiscussion).

    Generated from the following TL definition:
    ```tl
    messages.readDiscussion#f731a9f4 peer:InputPeer msg_id:int read_max_id:int = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        read_max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UnpinAllMessages(TLRequest):
    """
    [Read `messages.unpinAllMessages` docs](https://core.telegram.org/method/messages.unpinAllMessages).

    Generated from the following TL definition:
    ```tl
    messages.unpinAllMessages#62dd747 flags:# peer:InputPeer top_msg_id:flags.0?int saved_peer_id:flags.1?InputPeer = messages.AffectedHistory
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        top_msg_id: Optional[int],
        saved_peer_id: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteChat(TLRequest):
    """
    [Read `messages.deleteChat` docs](https://core.telegram.org/method/messages.deleteChat).

    Generated from the following TL definition:
    ```tl
    messages.deleteChat#5bd0ee50 chat_id:long = Bool
    ```
    """
    def __new__(
        cls,
        chat_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeletePhoneCallHistory(TLRequest):
    """
    [Read `messages.deletePhoneCallHistory` docs](https://core.telegram.org/method/messages.deletePhoneCallHistory).

    Generated from the following TL definition:
    ```tl
    messages.deletePhoneCallHistory#f9cbe409 flags:# revoke:flags.0?true = messages.AffectedFoundMessages
    ```
    """
    def __new__(
        cls,
        revoke: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckHistoryImport(TLRequest):
    """
    [Read `messages.checkHistoryImport` docs](https://core.telegram.org/method/messages.checkHistoryImport).

    Generated from the following TL definition:
    ```tl
    messages.checkHistoryImport#43fe19f3 import_head:string = messages.HistoryImportParsed
    ```
    """
    def __new__(
        cls,
        import_head: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InitHistoryImport(TLRequest):
    """
    [Read `messages.initHistoryImport` docs](https://core.telegram.org/method/messages.initHistoryImport).

    Generated from the following TL definition:
    ```tl
    messages.initHistoryImport#34090c3b peer:InputPeer file:InputFile media_count:int = messages.HistoryImport
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        file: types.InputFile | types.InputFileBig | types.InputFileStoryDocument,
        media_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UploadImportedMedia(TLRequest):
    """
    [Read `messages.uploadImportedMedia` docs](https://core.telegram.org/method/messages.uploadImportedMedia).

    Generated from the following TL definition:
    ```tl
    messages.uploadImportedMedia#2a862092 peer:InputPeer import_id:long file_name:string media:InputMedia = MessageMedia
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        import_id: int,
        file_name: str,
        media: types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StartHistoryImport(TLRequest):
    """
    [Read `messages.startHistoryImport` docs](https://core.telegram.org/method/messages.startHistoryImport).

    Generated from the following TL definition:
    ```tl
    messages.startHistoryImport#b43df344 peer:InputPeer import_id:long = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        import_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetExportedChatInvites(TLRequest):
    """
    [Read `messages.getExportedChatInvites` docs](https://core.telegram.org/method/messages.getExportedChatInvites).

    Generated from the following TL definition:
    ```tl
    messages.getExportedChatInvites#a2b5a3f6 flags:# revoked:flags.3?true peer:InputPeer admin_id:InputUser offset_date:flags.2?int offset_link:flags.2?string limit:int = messages.ExportedChatInvites
    ```
    """
    def __new__(
        cls,
        revoked: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        admin_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        offset_date: Optional[int],
        offset_link: Optional[str],
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetExportedChatInvite(TLRequest):
    """
    [Read `messages.getExportedChatInvite` docs](https://core.telegram.org/method/messages.getExportedChatInvite).

    Generated from the following TL definition:
    ```tl
    messages.getExportedChatInvite#73746f5c peer:InputPeer link:string = messages.ExportedChatInvite
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        link: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditExportedChatInvite(TLRequest):
    """
    [Read `messages.editExportedChatInvite` docs](https://core.telegram.org/method/messages.editExportedChatInvite).

    Generated from the following TL definition:
    ```tl
    messages.editExportedChatInvite#bdca2f75 flags:# revoked:flags.2?true peer:InputPeer link:string expire_date:flags.0?int usage_limit:flags.1?int request_needed:flags.3?Bool title:flags.4?string = messages.ExportedChatInvite
    ```
    """
    def __new__(
        cls,
        revoked: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        link: str,
        expire_date: Optional[int],
        usage_limit: Optional[int],
        request_needed: Optional[bool],
        title: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteRevokedExportedChatInvites(TLRequest):
    """
    [Read `messages.deleteRevokedExportedChatInvites` docs](https://core.telegram.org/method/messages.deleteRevokedExportedChatInvites).

    Generated from the following TL definition:
    ```tl
    messages.deleteRevokedExportedChatInvites#56987bd5 peer:InputPeer admin_id:InputUser = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        admin_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteExportedChatInvite(TLRequest):
    """
    [Read `messages.deleteExportedChatInvite` docs](https://core.telegram.org/method/messages.deleteExportedChatInvite).

    Generated from the following TL definition:
    ```tl
    messages.deleteExportedChatInvite#d464a42b peer:InputPeer link:string = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        link: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAdminsWithInvites(TLRequest):
    """
    [Read `messages.getAdminsWithInvites` docs](https://core.telegram.org/method/messages.getAdminsWithInvites).

    Generated from the following TL definition:
    ```tl
    messages.getAdminsWithInvites#3920e6ef peer:InputPeer = messages.ChatAdminsWithInvites
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetChatInviteImporters(TLRequest):
    """
    [Read `messages.getChatInviteImporters` docs](https://core.telegram.org/method/messages.getChatInviteImporters).

    Generated from the following TL definition:
    ```tl
    messages.getChatInviteImporters#df04dd4e flags:# requested:flags.0?true subscription_expired:flags.3?true peer:InputPeer link:flags.1?string q:flags.2?string offset_date:int offset_user:InputUser limit:int = messages.ChatInviteImporters
    ```
    """
    def __new__(
        cls,
        requested: bool,
        subscription_expired: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        link: Optional[str],
        q: Optional[str],
        offset_date: int,
        offset_user: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetHistoryTtl(TLRequest):
    """
    [Read `messages.setHistoryTTL` docs](https://core.telegram.org/method/messages.setHistoryTTL).

    Generated from the following TL definition:
    ```tl
    messages.setHistoryTTL#b80e5fe4 peer:InputPeer period:int = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        period: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckHistoryImportPeer(TLRequest):
    """
    [Read `messages.checkHistoryImportPeer` docs](https://core.telegram.org/method/messages.checkHistoryImportPeer).

    Generated from the following TL definition:
    ```tl
    messages.checkHistoryImportPeer#5dc60f03 peer:InputPeer = messages.CheckedHistoryImportPeer
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetChatTheme(TLRequest):
    """
    [Read `messages.setChatTheme` docs](https://core.telegram.org/method/messages.setChatTheme).

    Generated from the following TL definition:
    ```tl
    messages.setChatTheme#81202c9 peer:InputPeer theme:InputChatTheme = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        theme: types.InputChatThemeEmpty | types.InputChatTheme | types.InputChatThemeUniqueGift,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMessageReadParticipants(TLRequest):
    """
    [Read `messages.getMessageReadParticipants` docs](https://core.telegram.org/method/messages.getMessageReadParticipants).

    Generated from the following TL definition:
    ```tl
    messages.getMessageReadParticipants#31c1c44f peer:InputPeer msg_id:int = Vector<ReadParticipantDate>
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSearchResultsCalendar(TLRequest):
    """
    [Read `messages.getSearchResultsCalendar` docs](https://core.telegram.org/method/messages.getSearchResultsCalendar).

    Generated from the following TL definition:
    ```tl
    messages.getSearchResultsCalendar#6aa3f6bd flags:# peer:InputPeer saved_peer_id:flags.2?InputPeer filter:MessagesFilter offset_id:int offset_date:int = messages.SearchResultsCalendar
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        saved_peer_id: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        filter: types.InputMessagesFilterEmpty | types.InputMessagesFilterPhotos | types.InputMessagesFilterVideo | types.InputMessagesFilterPhotoVideo | types.InputMessagesFilterDocument | types.InputMessagesFilterUrl | types.InputMessagesFilterGif | types.InputMessagesFilterVoice | types.InputMessagesFilterMusic | types.InputMessagesFilterChatPhotos | types.InputMessagesFilterPhoneCalls | types.InputMessagesFilterRoundVoice | types.InputMessagesFilterRoundVideo | types.InputMessagesFilterMyMentions | types.InputMessagesFilterGeo | types.InputMessagesFilterContacts | types.InputMessagesFilterPinned,
        offset_id: int,
        offset_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSearchResultsPositions(TLRequest):
    """
    [Read `messages.getSearchResultsPositions` docs](https://core.telegram.org/method/messages.getSearchResultsPositions).

    Generated from the following TL definition:
    ```tl
    messages.getSearchResultsPositions#9c7f2f10 flags:# peer:InputPeer saved_peer_id:flags.2?InputPeer filter:MessagesFilter offset_id:int limit:int = messages.SearchResultsPositions
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        saved_peer_id: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        filter: types.InputMessagesFilterEmpty | types.InputMessagesFilterPhotos | types.InputMessagesFilterVideo | types.InputMessagesFilterPhotoVideo | types.InputMessagesFilterDocument | types.InputMessagesFilterUrl | types.InputMessagesFilterGif | types.InputMessagesFilterVoice | types.InputMessagesFilterMusic | types.InputMessagesFilterChatPhotos | types.InputMessagesFilterPhoneCalls | types.InputMessagesFilterRoundVoice | types.InputMessagesFilterRoundVideo | types.InputMessagesFilterMyMentions | types.InputMessagesFilterGeo | types.InputMessagesFilterContacts | types.InputMessagesFilterPinned,
        offset_id: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class HideChatJoinRequest(TLRequest):
    """
    [Read `messages.hideChatJoinRequest` docs](https://core.telegram.org/method/messages.hideChatJoinRequest).

    Generated from the following TL definition:
    ```tl
    messages.hideChatJoinRequest#7fe7e815 flags:# approved:flags.0?true peer:InputPeer user_id:InputUser = Updates
    ```
    """
    def __new__(
        cls,
        approved: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class HideAllChatJoinRequests(TLRequest):
    """
    [Read `messages.hideAllChatJoinRequests` docs](https://core.telegram.org/method/messages.hideAllChatJoinRequests).

    Generated from the following TL definition:
    ```tl
    messages.hideAllChatJoinRequests#e085f4ea flags:# approved:flags.0?true peer:InputPeer link:flags.1?string = Updates
    ```
    """
    def __new__(
        cls,
        approved: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        link: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleNoForwards(TLRequest):
    """
    [Read `messages.toggleNoForwards` docs](https://core.telegram.org/method/messages.toggleNoForwards).

    Generated from the following TL definition:
    ```tl
    messages.toggleNoForwards#b11eafa2 peer:InputPeer enabled:Bool = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveDefaultSendAs(TLRequest):
    """
    [Read `messages.saveDefaultSendAs` docs](https://core.telegram.org/method/messages.saveDefaultSendAs).

    Generated from the following TL definition:
    ```tl
    messages.saveDefaultSendAs#ccfddf96 peer:InputPeer send_as:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        send_as: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendReaction(TLRequest):
    """
    [Read `messages.sendReaction` docs](https://core.telegram.org/method/messages.sendReaction).

    Generated from the following TL definition:
    ```tl
    messages.sendReaction#d30d78d4 flags:# big:flags.1?true add_to_recent:flags.2?true peer:InputPeer msg_id:int reaction:flags.0?Vector<Reaction> = Updates
    ```
    """
    def __new__(
        cls,
        big: bool,
        add_to_recent: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        reaction: Optional[Sequence[types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMessagesReactions(TLRequest):
    """
    [Read `messages.getMessagesReactions` docs](https://core.telegram.org/method/messages.getMessagesReactions).

    Generated from the following TL definition:
    ```tl
    messages.getMessagesReactions#8bba90e6 peer:InputPeer id:Vector<int> = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMessageReactionsList(TLRequest):
    """
    [Read `messages.getMessageReactionsList` docs](https://core.telegram.org/method/messages.getMessageReactionsList).

    Generated from the following TL definition:
    ```tl
    messages.getMessageReactionsList#461b3f48 flags:# peer:InputPeer id:int reaction:flags.0?Reaction offset:flags.1?string limit:int = messages.MessageReactionsList
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
        reaction: Optional[types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid],
        offset: Optional[str],
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetChatAvailableReactions(TLRequest):
    """
    [Read `messages.setChatAvailableReactions` docs](https://core.telegram.org/method/messages.setChatAvailableReactions).

    Generated from the following TL definition:
    ```tl
    messages.setChatAvailableReactions#864b2581 flags:# peer:InputPeer available_reactions:ChatReactions reactions_limit:flags.0?int paid_enabled:flags.1?Bool = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        available_reactions: types.ChatReactionsNone | types.ChatReactionsAll | types.ChatReactionsSome,
        reactions_limit: Optional[int],
        paid_enabled: Optional[bool],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAvailableReactions(TLRequest):
    """
    [Read `messages.getAvailableReactions` docs](https://core.telegram.org/method/messages.getAvailableReactions).

    Generated from the following TL definition:
    ```tl
    messages.getAvailableReactions#18dea0ac hash:int = messages.AvailableReactions
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetDefaultReaction(TLRequest):
    """
    [Read `messages.setDefaultReaction` docs](https://core.telegram.org/method/messages.setDefaultReaction).

    Generated from the following TL definition:
    ```tl
    messages.setDefaultReaction#4f47a016 reaction:Reaction = Bool
    ```
    """
    def __new__(
        cls,
        reaction: types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TranslateText(TLRequest):
    """
    [Read `messages.translateText` docs](https://core.telegram.org/method/messages.translateText).

    Generated from the following TL definition:
    ```tl
    messages.translateText#63183030 flags:# peer:flags.0?InputPeer id:flags.0?Vector<int> text:flags.1?Vector<TextWithEntities> to_lang:string = messages.TranslatedText
    ```
    """
    def __new__(
        cls,
        peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        id: Optional[Sequence[int]],
        text: Optional[Sequence[types.TextWithEntities]],
        to_lang: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetUnreadReactions(TLRequest):
    """
    [Read `messages.getUnreadReactions` docs](https://core.telegram.org/method/messages.getUnreadReactions).

    Generated from the following TL definition:
    ```tl
    messages.getUnreadReactions#bd7f90ac flags:# peer:InputPeer top_msg_id:flags.0?int saved_peer_id:flags.1?InputPeer offset_id:int add_offset:int limit:int max_id:int min_id:int = messages.Messages
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        top_msg_id: Optional[int],
        saved_peer_id: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        offset_id: int,
        add_offset: int,
        limit: int,
        max_id: int,
        min_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReadReactions(TLRequest):
    """
    [Read `messages.readReactions` docs](https://core.telegram.org/method/messages.readReactions).

    Generated from the following TL definition:
    ```tl
    messages.readReactions#9ec44f93 flags:# peer:InputPeer top_msg_id:flags.0?int saved_peer_id:flags.1?InputPeer = messages.AffectedHistory
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        top_msg_id: Optional[int],
        saved_peer_id: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchSentMedia(TLRequest):
    """
    [Read `messages.searchSentMedia` docs](https://core.telegram.org/method/messages.searchSentMedia).

    Generated from the following TL definition:
    ```tl
    messages.searchSentMedia#107e31a0 q:string filter:MessagesFilter limit:int = messages.Messages
    ```
    """
    def __new__(
        cls,
        q: str,
        filter: types.InputMessagesFilterEmpty | types.InputMessagesFilterPhotos | types.InputMessagesFilterVideo | types.InputMessagesFilterPhotoVideo | types.InputMessagesFilterDocument | types.InputMessagesFilterUrl | types.InputMessagesFilterGif | types.InputMessagesFilterVoice | types.InputMessagesFilterMusic | types.InputMessagesFilterChatPhotos | types.InputMessagesFilterPhoneCalls | types.InputMessagesFilterRoundVoice | types.InputMessagesFilterRoundVideo | types.InputMessagesFilterMyMentions | types.InputMessagesFilterGeo | types.InputMessagesFilterContacts | types.InputMessagesFilterPinned,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAttachMenuBots(TLRequest):
    """
    [Read `messages.getAttachMenuBots` docs](https://core.telegram.org/method/messages.getAttachMenuBots).

    Generated from the following TL definition:
    ```tl
    messages.getAttachMenuBots#16fcc2cb hash:long = AttachMenuBots
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAttachMenuBot(TLRequest):
    """
    [Read `messages.getAttachMenuBot` docs](https://core.telegram.org/method/messages.getAttachMenuBot).

    Generated from the following TL definition:
    ```tl
    messages.getAttachMenuBot#77216192 bot:InputUser = AttachMenuBotsBot
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleBotInAttachMenu(TLRequest):
    """
    [Read `messages.toggleBotInAttachMenu` docs](https://core.telegram.org/method/messages.toggleBotInAttachMenu).

    Generated from the following TL definition:
    ```tl
    messages.toggleBotInAttachMenu#69f59d69 flags:# write_allowed:flags.0?true bot:InputUser enabled:Bool = Bool
    ```
    """
    def __new__(
        cls,
        write_allowed: bool,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestWebView(TLRequest):
    """
    [Read `messages.requestWebView` docs](https://core.telegram.org/method/messages.requestWebView).

    Generated from the following TL definition:
    ```tl
    messages.requestWebView#269dc2c1 flags:# from_bot_menu:flags.4?true silent:flags.5?true compact:flags.7?true fullscreen:flags.8?true peer:InputPeer bot:InputUser url:flags.1?string start_param:flags.3?string theme_params:flags.2?DataJSON platform:string reply_to:flags.0?InputReplyTo send_as:flags.13?InputPeer = WebViewResult
    ```
    """
    def __new__(
        cls,
        from_bot_menu: bool,
        silent: bool,
        compact: bool,
        fullscreen: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        url: Optional[str],
        start_param: Optional[str],
        theme_params: Optional[types.DataJson],
        platform: str,
        reply_to: Optional[types.InputReplyToMessage | types.InputReplyToStory | types.InputReplyToMonoForum],
        send_as: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ProlongWebView(TLRequest):
    """
    [Read `messages.prolongWebView` docs](https://core.telegram.org/method/messages.prolongWebView).

    Generated from the following TL definition:
    ```tl
    messages.prolongWebView#b0d81a83 flags:# silent:flags.5?true peer:InputPeer bot:InputUser query_id:long reply_to:flags.0?InputReplyTo send_as:flags.13?InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        silent: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        query_id: int,
        reply_to: Optional[types.InputReplyToMessage | types.InputReplyToStory | types.InputReplyToMonoForum],
        send_as: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestSimpleWebView(TLRequest):
    """
    [Read `messages.requestSimpleWebView` docs](https://core.telegram.org/method/messages.requestSimpleWebView).

    Generated from the following TL definition:
    ```tl
    messages.requestSimpleWebView#413a3e73 flags:# from_switch_webview:flags.1?true from_side_menu:flags.2?true compact:flags.7?true fullscreen:flags.8?true bot:InputUser url:flags.3?string start_param:flags.4?string theme_params:flags.0?DataJSON platform:string = WebViewResult
    ```
    """
    def __new__(
        cls,
        from_switch_webview: bool,
        from_side_menu: bool,
        compact: bool,
        fullscreen: bool,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        url: Optional[str],
        start_param: Optional[str],
        theme_params: Optional[types.DataJson],
        platform: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendWebViewResultMessage(TLRequest):
    """
    [Read `messages.sendWebViewResultMessage` docs](https://core.telegram.org/method/messages.sendWebViewResultMessage).

    Generated from the following TL definition:
    ```tl
    messages.sendWebViewResultMessage#a4314f5 bot_query_id:string result:InputBotInlineResult = WebViewMessageSent
    ```
    """
    def __new__(
        cls,
        bot_query_id: str,
        result: types.InputBotInlineResult | types.InputBotInlineResultPhoto | types.InputBotInlineResultDocument | types.InputBotInlineResultGame,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendWebViewData(TLRequest):
    """
    [Read `messages.sendWebViewData` docs](https://core.telegram.org/method/messages.sendWebViewData).

    Generated from the following TL definition:
    ```tl
    messages.sendWebViewData#dc0242c8 bot:InputUser random_id:long button_text:string data:string = Updates
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        random_id: int,
        button_text: str,
        data: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TranscribeAudio(TLRequest):
    """
    [Read `messages.transcribeAudio` docs](https://core.telegram.org/method/messages.transcribeAudio).

    Generated from the following TL definition:
    ```tl
    messages.transcribeAudio#269e9a49 peer:InputPeer msg_id:int = messages.TranscribedAudio
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RateTranscribedAudio(TLRequest):
    """
    [Read `messages.rateTranscribedAudio` docs](https://core.telegram.org/method/messages.rateTranscribedAudio).

    Generated from the following TL definition:
    ```tl
    messages.rateTranscribedAudio#7f1d072f peer:InputPeer msg_id:int transcription_id:long good:Bool = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        transcription_id: int,
        good: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetCustomEmojiDocuments(TLRequest):
    """
    [Read `messages.getCustomEmojiDocuments` docs](https://core.telegram.org/method/messages.getCustomEmojiDocuments).

    Generated from the following TL definition:
    ```tl
    messages.getCustomEmojiDocuments#d9ab0f54 document_id:Vector<long> = Vector<Document>
    ```
    """
    def __new__(
        cls,
        document_id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetEmojiStickers(TLRequest):
    """
    [Read `messages.getEmojiStickers` docs](https://core.telegram.org/method/messages.getEmojiStickers).

    Generated from the following TL definition:
    ```tl
    messages.getEmojiStickers#fbfca18f hash:long = messages.AllStickers
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetFeaturedEmojiStickers(TLRequest):
    """
    [Read `messages.getFeaturedEmojiStickers` docs](https://core.telegram.org/method/messages.getFeaturedEmojiStickers).

    Generated from the following TL definition:
    ```tl
    messages.getFeaturedEmojiStickers#ecf6736 hash:long = messages.FeaturedStickers
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportReaction(TLRequest):
    """
    [Read `messages.reportReaction` docs](https://core.telegram.org/method/messages.reportReaction).

    Generated from the following TL definition:
    ```tl
    messages.reportReaction#3f64c076 peer:InputPeer id:int reaction_peer:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
        reaction_peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetTopReactions(TLRequest):
    """
    [Read `messages.getTopReactions` docs](https://core.telegram.org/method/messages.getTopReactions).

    Generated from the following TL definition:
    ```tl
    messages.getTopReactions#bb8125ba limit:int hash:long = messages.Reactions
    ```
    """
    def __new__(
        cls,
        limit: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetRecentReactions(TLRequest):
    """
    [Read `messages.getRecentReactions` docs](https://core.telegram.org/method/messages.getRecentReactions).

    Generated from the following TL definition:
    ```tl
    messages.getRecentReactions#39461db2 limit:int hash:long = messages.Reactions
    ```
    """
    def __new__(
        cls,
        limit: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ClearRecentReactions(TLRequest):
    """
    [Read `messages.clearRecentReactions` docs](https://core.telegram.org/method/messages.clearRecentReactions).

    Generated from the following TL definition:
    ```tl
    messages.clearRecentReactions#9dfeefb4 = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetExtendedMedia(TLRequest):
    """
    [Read `messages.getExtendedMedia` docs](https://core.telegram.org/method/messages.getExtendedMedia).

    Generated from the following TL definition:
    ```tl
    messages.getExtendedMedia#84f80814 peer:InputPeer id:Vector<int> = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetDefaultHistoryTtl(TLRequest):
    """
    [Read `messages.setDefaultHistoryTTL` docs](https://core.telegram.org/method/messages.setDefaultHistoryTTL).

    Generated from the following TL definition:
    ```tl
    messages.setDefaultHistoryTTL#9eb51445 period:int = Bool
    ```
    """
    def __new__(
        cls,
        period: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDefaultHistoryTtl(TLRequest):
    """
    [Read `messages.getDefaultHistoryTTL` docs](https://core.telegram.org/method/messages.getDefaultHistoryTTL).

    Generated from the following TL definition:
    ```tl
    messages.getDefaultHistoryTTL#658b7188 = DefaultHistoryTTL
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendBotRequestedPeer(TLRequest):
    """
    [Read `messages.sendBotRequestedPeer` docs](https://core.telegram.org/method/messages.sendBotRequestedPeer).

    Generated from the following TL definition:
    ```tl
    messages.sendBotRequestedPeer#91b2d060 peer:InputPeer msg_id:int button_id:int requested_peers:Vector<InputPeer> = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        button_id: int,
        requested_peers: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetEmojiGroups(TLRequest):
    """
    [Read `messages.getEmojiGroups` docs](https://core.telegram.org/method/messages.getEmojiGroups).

    Generated from the following TL definition:
    ```tl
    messages.getEmojiGroups#7488ce5b hash:int = messages.EmojiGroups
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetEmojiStatusGroups(TLRequest):
    """
    [Read `messages.getEmojiStatusGroups` docs](https://core.telegram.org/method/messages.getEmojiStatusGroups).

    Generated from the following TL definition:
    ```tl
    messages.getEmojiStatusGroups#2ecd56cd hash:int = messages.EmojiGroups
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetEmojiProfilePhotoGroups(TLRequest):
    """
    [Read `messages.getEmojiProfilePhotoGroups` docs](https://core.telegram.org/method/messages.getEmojiProfilePhotoGroups).

    Generated from the following TL definition:
    ```tl
    messages.getEmojiProfilePhotoGroups#21a548f3 hash:int = messages.EmojiGroups
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchCustomEmoji(TLRequest):
    """
    [Read `messages.searchCustomEmoji` docs](https://core.telegram.org/method/messages.searchCustomEmoji).

    Generated from the following TL definition:
    ```tl
    messages.searchCustomEmoji#2c11c0d7 emoticon:string hash:long = EmojiList
    ```
    """
    def __new__(
        cls,
        emoticon: str,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TogglePeerTranslations(TLRequest):
    """
    [Read `messages.togglePeerTranslations` docs](https://core.telegram.org/method/messages.togglePeerTranslations).

    Generated from the following TL definition:
    ```tl
    messages.togglePeerTranslations#e47cb579 flags:# disabled:flags.0?true peer:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        disabled: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetBotApp(TLRequest):
    """
    [Read `messages.getBotApp` docs](https://core.telegram.org/method/messages.getBotApp).

    Generated from the following TL definition:
    ```tl
    messages.getBotApp#34fdc5c3 app:InputBotApp hash:long = messages.BotApp
    ```
    """
    def __new__(
        cls,
        app: types.InputBotAppId | types.InputBotAppShortName,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestAppWebView(TLRequest):
    """
    [Read `messages.requestAppWebView` docs](https://core.telegram.org/method/messages.requestAppWebView).

    Generated from the following TL definition:
    ```tl
    messages.requestAppWebView#53618bce flags:# write_allowed:flags.0?true compact:flags.7?true fullscreen:flags.8?true peer:InputPeer app:InputBotApp start_param:flags.1?string theme_params:flags.2?DataJSON platform:string = WebViewResult
    ```
    """
    def __new__(
        cls,
        write_allowed: bool,
        compact: bool,
        fullscreen: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        app: types.InputBotAppId | types.InputBotAppShortName,
        start_param: Optional[str],
        theme_params: Optional[types.DataJson],
        platform: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetChatWallPaper(TLRequest):
    """
    [Read `messages.setChatWallPaper` docs](https://core.telegram.org/method/messages.setChatWallPaper).

    Generated from the following TL definition:
    ```tl
    messages.setChatWallPaper#8ffacae1 flags:# for_both:flags.3?true revert:flags.4?true peer:InputPeer wallpaper:flags.0?InputWallPaper settings:flags.2?WallPaperSettings id:flags.1?int = Updates
    ```
    """
    def __new__(
        cls,
        for_both: bool,
        revert: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        wallpaper: Optional[types.InputWallPaper | types.InputWallPaperSlug | types.InputWallPaperNoFile],
        settings: Optional[types.WallPaperSettings],
        id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchEmojiStickerSets(TLRequest):
    """
    [Read `messages.searchEmojiStickerSets` docs](https://core.telegram.org/method/messages.searchEmojiStickerSets).

    Generated from the following TL definition:
    ```tl
    messages.searchEmojiStickerSets#92b4494c flags:# exclude_featured:flags.0?true q:string hash:long = messages.FoundStickerSets
    ```
    """
    def __new__(
        cls,
        exclude_featured: bool,
        q: str,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSavedDialogs(TLRequest):
    """
    [Read `messages.getSavedDialogs` docs](https://core.telegram.org/method/messages.getSavedDialogs).

    Generated from the following TL definition:
    ```tl
    messages.getSavedDialogs#1e91fc99 flags:# exclude_pinned:flags.0?true parent_peer:flags.1?InputPeer offset_date:int offset_id:int offset_peer:InputPeer limit:int hash:long = messages.SavedDialogs
    ```
    """
    def __new__(
        cls,
        exclude_pinned: bool,
        parent_peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        offset_date: int,
        offset_id: int,
        offset_peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        limit: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSavedHistory(TLRequest):
    """
    [Read `messages.getSavedHistory` docs](https://core.telegram.org/method/messages.getSavedHistory).

    Generated from the following TL definition:
    ```tl
    messages.getSavedHistory#998ab009 flags:# parent_peer:flags.0?InputPeer peer:InputPeer offset_id:int offset_date:int add_offset:int limit:int max_id:int min_id:int hash:long = messages.Messages
    ```
    """
    def __new__(
        cls,
        parent_peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        offset_id: int,
        offset_date: int,
        add_offset: int,
        limit: int,
        max_id: int,
        min_id: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteSavedHistory(TLRequest):
    """
    [Read `messages.deleteSavedHistory` docs](https://core.telegram.org/method/messages.deleteSavedHistory).

    Generated from the following TL definition:
    ```tl
    messages.deleteSavedHistory#4dc5085f flags:# parent_peer:flags.0?InputPeer peer:InputPeer max_id:int min_date:flags.2?int max_date:flags.3?int = messages.AffectedHistory
    ```
    """
    def __new__(
        cls,
        parent_peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        max_id: int,
        min_date: Optional[int],
        max_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPinnedSavedDialogs(TLRequest):
    """
    [Read `messages.getPinnedSavedDialogs` docs](https://core.telegram.org/method/messages.getPinnedSavedDialogs).

    Generated from the following TL definition:
    ```tl
    messages.getPinnedSavedDialogs#d63d94e0 = messages.SavedDialogs
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleSavedDialogPin(TLRequest):
    """
    [Read `messages.toggleSavedDialogPin` docs](https://core.telegram.org/method/messages.toggleSavedDialogPin).

    Generated from the following TL definition:
    ```tl
    messages.toggleSavedDialogPin#ac81bbde flags:# pinned:flags.0?true peer:InputDialogPeer = Bool
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        peer: types.InputDialogPeer | types.InputDialogPeerFolder,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReorderPinnedSavedDialogs(TLRequest):
    """
    [Read `messages.reorderPinnedSavedDialogs` docs](https://core.telegram.org/method/messages.reorderPinnedSavedDialogs).

    Generated from the following TL definition:
    ```tl
    messages.reorderPinnedSavedDialogs#8b716587 flags:# force:flags.0?true order:Vector<InputDialogPeer> = Bool
    ```
    """
    def __new__(
        cls,
        force: bool,
        order: Sequence[types.InputDialogPeer | types.InputDialogPeerFolder],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSavedReactionTags(TLRequest):
    """
    [Read `messages.getSavedReactionTags` docs](https://core.telegram.org/method/messages.getSavedReactionTags).

    Generated from the following TL definition:
    ```tl
    messages.getSavedReactionTags#3637e05b flags:# peer:flags.0?InputPeer hash:long = messages.SavedReactionTags
    ```
    """
    def __new__(
        cls,
        peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateSavedReactionTag(TLRequest):
    """
    [Read `messages.updateSavedReactionTag` docs](https://core.telegram.org/method/messages.updateSavedReactionTag).

    Generated from the following TL definition:
    ```tl
    messages.updateSavedReactionTag#60297dec flags:# reaction:Reaction title:flags.0?string = Bool
    ```
    """
    def __new__(
        cls,
        reaction: types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid,
        title: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDefaultTagReactions(TLRequest):
    """
    [Read `messages.getDefaultTagReactions` docs](https://core.telegram.org/method/messages.getDefaultTagReactions).

    Generated from the following TL definition:
    ```tl
    messages.getDefaultTagReactions#bdf93428 hash:long = messages.Reactions
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetOutboxReadDate(TLRequest):
    """
    [Read `messages.getOutboxReadDate` docs](https://core.telegram.org/method/messages.getOutboxReadDate).

    Generated from the following TL definition:
    ```tl
    messages.getOutboxReadDate#8c4bfe5d peer:InputPeer msg_id:int = OutboxReadDate
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetQuickReplies(TLRequest):
    """
    [Read `messages.getQuickReplies` docs](https://core.telegram.org/method/messages.getQuickReplies).

    Generated from the following TL definition:
    ```tl
    messages.getQuickReplies#d483f2a8 hash:long = messages.QuickReplies
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReorderQuickReplies(TLRequest):
    """
    [Read `messages.reorderQuickReplies` docs](https://core.telegram.org/method/messages.reorderQuickReplies).

    Generated from the following TL definition:
    ```tl
    messages.reorderQuickReplies#60331907 order:Vector<int> = Bool
    ```
    """
    def __new__(
        cls,
        order: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckQuickReplyShortcut(TLRequest):
    """
    [Read `messages.checkQuickReplyShortcut` docs](https://core.telegram.org/method/messages.checkQuickReplyShortcut).

    Generated from the following TL definition:
    ```tl
    messages.checkQuickReplyShortcut#f1d0fbd3 shortcut:string = Bool
    ```
    """
    def __new__(
        cls,
        shortcut: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditQuickReplyShortcut(TLRequest):
    """
    [Read `messages.editQuickReplyShortcut` docs](https://core.telegram.org/method/messages.editQuickReplyShortcut).

    Generated from the following TL definition:
    ```tl
    messages.editQuickReplyShortcut#5c003cef shortcut_id:int shortcut:string = Bool
    ```
    """
    def __new__(
        cls,
        shortcut_id: int,
        shortcut: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteQuickReplyShortcut(TLRequest):
    """
    [Read `messages.deleteQuickReplyShortcut` docs](https://core.telegram.org/method/messages.deleteQuickReplyShortcut).

    Generated from the following TL definition:
    ```tl
    messages.deleteQuickReplyShortcut#3cc04740 shortcut_id:int = Bool
    ```
    """
    def __new__(
        cls,
        shortcut_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetQuickReplyMessages(TLRequest):
    """
    [Read `messages.getQuickReplyMessages` docs](https://core.telegram.org/method/messages.getQuickReplyMessages).

    Generated from the following TL definition:
    ```tl
    messages.getQuickReplyMessages#94a495c3 flags:# shortcut_id:int id:flags.0?Vector<int> hash:long = messages.Messages
    ```
    """
    def __new__(
        cls,
        shortcut_id: int,
        id: Optional[Sequence[int]],
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendQuickReplyMessages(TLRequest):
    """
    [Read `messages.sendQuickReplyMessages` docs](https://core.telegram.org/method/messages.sendQuickReplyMessages).

    Generated from the following TL definition:
    ```tl
    messages.sendQuickReplyMessages#6c750de1 peer:InputPeer shortcut_id:int id:Vector<int> random_id:Vector<long> = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        shortcut_id: int,
        id: Sequence[int],
        random_id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteQuickReplyMessages(TLRequest):
    """
    [Read `messages.deleteQuickReplyMessages` docs](https://core.telegram.org/method/messages.deleteQuickReplyMessages).

    Generated from the following TL definition:
    ```tl
    messages.deleteQuickReplyMessages#e105e910 shortcut_id:int id:Vector<int> = Updates
    ```
    """
    def __new__(
        cls,
        shortcut_id: int,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleDialogFilterTags(TLRequest):
    """
    [Read `messages.toggleDialogFilterTags` docs](https://core.telegram.org/method/messages.toggleDialogFilterTags).

    Generated from the following TL definition:
    ```tl
    messages.toggleDialogFilterTags#fd2dda49 enabled:Bool = Bool
    ```
    """
    def __new__(
        cls,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMyStickers(TLRequest):
    """
    [Read `messages.getMyStickers` docs](https://core.telegram.org/method/messages.getMyStickers).

    Generated from the following TL definition:
    ```tl
    messages.getMyStickers#d0b5e1fc offset_id:long limit:int = messages.MyStickers
    ```
    """
    def __new__(
        cls,
        offset_id: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetEmojiStickerGroups(TLRequest):
    """
    [Read `messages.getEmojiStickerGroups` docs](https://core.telegram.org/method/messages.getEmojiStickerGroups).

    Generated from the following TL definition:
    ```tl
    messages.getEmojiStickerGroups#1dd840f5 hash:int = messages.EmojiGroups
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAvailableEffects(TLRequest):
    """
    [Read `messages.getAvailableEffects` docs](https://core.telegram.org/method/messages.getAvailableEffects).

    Generated from the following TL definition:
    ```tl
    messages.getAvailableEffects#dea20a39 hash:int = messages.AvailableEffects
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditFactCheck(TLRequest):
    """
    [Read `messages.editFactCheck` docs](https://core.telegram.org/method/messages.editFactCheck).

    Generated from the following TL definition:
    ```tl
    messages.editFactCheck#589ee75 peer:InputPeer msg_id:int text:TextWithEntities = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        text: types.TextWithEntities,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteFactCheck(TLRequest):
    """
    [Read `messages.deleteFactCheck` docs](https://core.telegram.org/method/messages.deleteFactCheck).

    Generated from the following TL definition:
    ```tl
    messages.deleteFactCheck#d1da940c peer:InputPeer msg_id:int = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetFactCheck(TLRequest):
    """
    [Read `messages.getFactCheck` docs](https://core.telegram.org/method/messages.getFactCheck).

    Generated from the following TL definition:
    ```tl
    messages.getFactCheck#b9cdc5ee peer:InputPeer msg_id:Vector<int> = Vector<FactCheck>
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestMainWebView(TLRequest):
    """
    [Read `messages.requestMainWebView` docs](https://core.telegram.org/method/messages.requestMainWebView).

    Generated from the following TL definition:
    ```tl
    messages.requestMainWebView#c9e01e7b flags:# compact:flags.7?true fullscreen:flags.8?true peer:InputPeer bot:InputUser start_param:flags.1?string theme_params:flags.0?DataJSON platform:string = WebViewResult
    ```
    """
    def __new__(
        cls,
        compact: bool,
        fullscreen: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        start_param: Optional[str],
        theme_params: Optional[types.DataJson],
        platform: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendPaidReaction(TLRequest):
    """
    [Read `messages.sendPaidReaction` docs](https://core.telegram.org/method/messages.sendPaidReaction).

    Generated from the following TL definition:
    ```tl
    messages.sendPaidReaction#58bbcb50 flags:# peer:InputPeer msg_id:int count:int random_id:long private:flags.0?PaidReactionPrivacy = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        count: int,
        random_id: int,
        private: Optional[types.PaidReactionPrivacyDefault | types.PaidReactionPrivacyAnonymous | types.PaidReactionPrivacyPeer],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TogglePaidReactionPrivacy(TLRequest):
    """
    [Read `messages.togglePaidReactionPrivacy` docs](https://core.telegram.org/method/messages.togglePaidReactionPrivacy).

    Generated from the following TL definition:
    ```tl
    messages.togglePaidReactionPrivacy#435885b5 peer:InputPeer msg_id:int private:PaidReactionPrivacy = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        private: types.PaidReactionPrivacyDefault | types.PaidReactionPrivacyAnonymous | types.PaidReactionPrivacyPeer,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPaidReactionPrivacy(TLRequest):
    """
    [Read `messages.getPaidReactionPrivacy` docs](https://core.telegram.org/method/messages.getPaidReactionPrivacy).

    Generated from the following TL definition:
    ```tl
    messages.getPaidReactionPrivacy#472455aa = Updates
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ViewSponsoredMessage(TLRequest):
    """
    [Read `messages.viewSponsoredMessage` docs](https://core.telegram.org/method/messages.viewSponsoredMessage).

    Generated from the following TL definition:
    ```tl
    messages.viewSponsoredMessage#269e3643 random_id:bytes = Bool
    ```
    """
    def __new__(
        cls,
        random_id: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ClickSponsoredMessage(TLRequest):
    """
    [Read `messages.clickSponsoredMessage` docs](https://core.telegram.org/method/messages.clickSponsoredMessage).

    Generated from the following TL definition:
    ```tl
    messages.clickSponsoredMessage#8235057e flags:# media:flags.0?true fullscreen:flags.1?true random_id:bytes = Bool
    ```
    """
    def __new__(
        cls,
        media: bool,
        fullscreen: bool,
        random_id: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportSponsoredMessage(TLRequest):
    """
    [Read `messages.reportSponsoredMessage` docs](https://core.telegram.org/method/messages.reportSponsoredMessage).

    Generated from the following TL definition:
    ```tl
    messages.reportSponsoredMessage#12cbf0c4 random_id:bytes option:bytes = channels.SponsoredMessageReportResult
    ```
    """
    def __new__(
        cls,
        random_id: bytes,
        option: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSponsoredMessages(TLRequest):
    """
    [Read `messages.getSponsoredMessages` docs](https://core.telegram.org/method/messages.getSponsoredMessages).

    Generated from the following TL definition:
    ```tl
    messages.getSponsoredMessages#3d6ce850 flags:# peer:InputPeer msg_id:flags.0?int = messages.SponsoredMessages
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavePreparedInlineMessage(TLRequest):
    """
    [Read `messages.savePreparedInlineMessage` docs](https://core.telegram.org/method/messages.savePreparedInlineMessage).

    Generated from the following TL definition:
    ```tl
    messages.savePreparedInlineMessage#f21f7f2f flags:# result:InputBotInlineResult user_id:InputUser peer_types:flags.0?Vector<InlineQueryPeerType> = messages.BotPreparedInlineMessage
    ```
    """
    def __new__(
        cls,
        result: types.InputBotInlineResult | types.InputBotInlineResultPhoto | types.InputBotInlineResultDocument | types.InputBotInlineResultGame,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        peer_types: Optional[Sequence[types.InlineQueryPeerTypeSameBotPm | types.InlineQueryPeerTypePm | types.InlineQueryPeerTypeChat | types.InlineQueryPeerTypeMegagroup | types.InlineQueryPeerTypeBroadcast | types.InlineQueryPeerTypeBotPm]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPreparedInlineMessage(TLRequest):
    """
    [Read `messages.getPreparedInlineMessage` docs](https://core.telegram.org/method/messages.getPreparedInlineMessage).

    Generated from the following TL definition:
    ```tl
    messages.getPreparedInlineMessage#857ebdb8 bot:InputUser id:string = messages.PreparedInlineMessage
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        id: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchStickers(TLRequest):
    """
    [Read `messages.searchStickers` docs](https://core.telegram.org/method/messages.searchStickers).

    Generated from the following TL definition:
    ```tl
    messages.searchStickers#29b1c66a flags:# emojis:flags.0?true q:string emoticon:string lang_code:Vector<string> offset:int limit:int hash:long = messages.FoundStickers
    ```
    """
    def __new__(
        cls,
        emojis: bool,
        q: str,
        emoticon: str,
        lang_code: Sequence[str],
        offset: int,
        limit: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportMessagesDelivery(TLRequest):
    """
    [Read `messages.reportMessagesDelivery` docs](https://core.telegram.org/method/messages.reportMessagesDelivery).

    Generated from the following TL definition:
    ```tl
    messages.reportMessagesDelivery#5a6d7395 flags:# push:flags.0?true peer:InputPeer id:Vector<int> = Bool
    ```
    """
    def __new__(
        cls,
        push: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSavedDialogsById(TLRequest):
    """
    [Read `messages.getSavedDialogsByID` docs](https://core.telegram.org/method/messages.getSavedDialogsByID).

    Generated from the following TL definition:
    ```tl
    messages.getSavedDialogsByID#6f6f9c96 flags:# parent_peer:flags.1?InputPeer ids:Vector<InputPeer> = messages.SavedDialogs
    ```
    """
    def __new__(
        cls,
        parent_peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        ids: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReadSavedHistory(TLRequest):
    """
    [Read `messages.readSavedHistory` docs](https://core.telegram.org/method/messages.readSavedHistory).

    Generated from the following TL definition:
    ```tl
    messages.readSavedHistory#ba4a3b5b parent_peer:InputPeer peer:InputPeer max_id:int = Bool
    ```
    """
    def __new__(
        cls,
        parent_peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleTodoCompleted(TLRequest):
    """
    [Read `messages.toggleTodoCompleted` docs](https://core.telegram.org/method/messages.toggleTodoCompleted).

    Generated from the following TL definition:
    ```tl
    messages.toggleTodoCompleted#d3e03124 peer:InputPeer msg_id:int completed:Vector<int> incompleted:Vector<int> = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        completed: Sequence[int],
        incompleted: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AppendTodoList(TLRequest):
    """
    [Read `messages.appendTodoList` docs](https://core.telegram.org/method/messages.appendTodoList).

    Generated from the following TL definition:
    ```tl
    messages.appendTodoList#21a61057 peer:InputPeer msg_id:int list:Vector<TodoItem> = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        list: Sequence[types.TodoItem],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleSuggestedPostApproval(TLRequest):
    """
    [Read `messages.toggleSuggestedPostApproval` docs](https://core.telegram.org/method/messages.toggleSuggestedPostApproval).

    Generated from the following TL definition:
    ```tl
    messages.toggleSuggestedPostApproval#8107455c flags:# reject:flags.1?true peer:InputPeer msg_id:int schedule_date:flags.0?int reject_comment:flags.2?string = Updates
    ```
    """
    def __new__(
        cls,
        reject: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        schedule_date: Optional[int],
        reject_comment: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetForumTopics(TLRequest):
    """
    [Read `messages.getForumTopics` docs](https://core.telegram.org/method/messages.getForumTopics).

    Generated from the following TL definition:
    ```tl
    messages.getForumTopics#3ba47bff flags:# peer:InputPeer q:flags.0?string offset_date:int offset_id:int offset_topic:int limit:int = messages.ForumTopics
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        q: Optional[str],
        offset_date: int,
        offset_id: int,
        offset_topic: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetForumTopicsById(TLRequest):
    """
    [Read `messages.getForumTopicsByID` docs](https://core.telegram.org/method/messages.getForumTopicsByID).

    Generated from the following TL definition:
    ```tl
    messages.getForumTopicsByID#af0a4a08 peer:InputPeer topics:Vector<int> = messages.ForumTopics
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        topics: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditForumTopic(TLRequest):
    """
    [Read `messages.editForumTopic` docs](https://core.telegram.org/method/messages.editForumTopic).

    Generated from the following TL definition:
    ```tl
    messages.editForumTopic#cecc1134 flags:# peer:InputPeer topic_id:int title:flags.0?string icon_emoji_id:flags.1?long closed:flags.2?Bool hidden:flags.3?Bool = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        topic_id: int,
        title: Optional[str],
        icon_emoji_id: Optional[int],
        closed: Optional[bool],
        hidden: Optional[bool],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePinnedForumTopic(TLRequest):
    """
    [Read `messages.updatePinnedForumTopic` docs](https://core.telegram.org/method/messages.updatePinnedForumTopic).

    Generated from the following TL definition:
    ```tl
    messages.updatePinnedForumTopic#175df251 peer:InputPeer topic_id:int pinned:Bool = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        topic_id: int,
        pinned: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReorderPinnedForumTopics(TLRequest):
    """
    [Read `messages.reorderPinnedForumTopics` docs](https://core.telegram.org/method/messages.reorderPinnedForumTopics).

    Generated from the following TL definition:
    ```tl
    messages.reorderPinnedForumTopics#e7841f0 flags:# force:flags.0?true peer:InputPeer order:Vector<int> = Updates
    ```
    """
    def __new__(
        cls,
        force: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        order: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CreateForumTopic(TLRequest):
    """
    [Read `messages.createForumTopic` docs](https://core.telegram.org/method/messages.createForumTopic).

    Generated from the following TL definition:
    ```tl
    messages.createForumTopic#2f98c3d5 flags:# title_missing:flags.4?true peer:InputPeer title:string icon_color:flags.0?int icon_emoji_id:flags.3?long random_id:long send_as:flags.2?InputPeer = Updates
    ```
    """
    def __new__(
        cls,
        title_missing: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        title: str,
        icon_color: Optional[int],
        icon_emoji_id: Optional[int],
        random_id: int,
        send_as: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteTopicHistory(TLRequest):
    """
    [Read `messages.deleteTopicHistory` docs](https://core.telegram.org/method/messages.deleteTopicHistory).

    Generated from the following TL definition:
    ```tl
    messages.deleteTopicHistory#d2816f10 peer:InputPeer top_msg_id:int = messages.AffectedHistory
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        top_msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetEmojiGameInfo(TLRequest):
    """
    [Read `messages.getEmojiGameInfo` docs](https://core.telegram.org/method/messages.getEmojiGameInfo).

    Generated from the following TL definition:
    ```tl
    messages.getEmojiGameInfo#fb7e8ca7 = messages.EmojiGameInfo
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SummarizeText(TLRequest):
    """
    [Read `messages.summarizeText` docs](https://core.telegram.org/method/messages.summarizeText).

    Generated from the following TL definition:
    ```tl
    messages.summarizeText#9d4104e2 flags:# peer:InputPeer id:int to_lang:flags.0?string = TextWithEntities
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
        to_lang: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

