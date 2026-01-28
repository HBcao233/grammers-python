from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class Dialogs(TLObject):
    """
    [Read `messages.dialogs` docs](https://core.telegram.org/constructor/messages.dialogs).

    Generated from the following TL definition:
    ```tl
    messages.dialogs#15ba6c40 dialogs:Vector<Dialog> messages:Vector<Message> chats:Vector<Chat> users:Vector<User> = messages.Dialogs
    ```
    """
    def __new__(
        cls,
        dialogs: Sequence[types.Dialog | types.DialogFolder],
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DialogsSlice(TLObject):
    """
    [Read `messages.dialogsSlice` docs](https://core.telegram.org/constructor/messages.dialogsSlice).

    Generated from the following TL definition:
    ```tl
    messages.dialogsSlice#71e094f3 count:int dialogs:Vector<Dialog> messages:Vector<Message> chats:Vector<Chat> users:Vector<User> = messages.Dialogs
    ```
    """
    def __new__(
        cls,
        count: int,
        dialogs: Sequence[types.Dialog | types.DialogFolder],
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DialogsNotModified(TLObject):
    """
    [Read `messages.dialogsNotModified` docs](https://core.telegram.org/constructor/messages.dialogsNotModified).

    Generated from the following TL definition:
    ```tl
    messages.dialogsNotModified#f0e3e596 count:int = messages.Dialogs
    ```
    """
    def __new__(
        cls,
        count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Messages(TLObject):
    """
    [Read `messages.messages` docs](https://core.telegram.org/constructor/messages.messages).

    Generated from the following TL definition:
    ```tl
    messages.messages#1d73e7ea messages:Vector<Message> topics:Vector<ForumTopic> chats:Vector<Chat> users:Vector<User> = messages.Messages
    ```
    """
    def __new__(
        cls,
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        topics: Sequence[types.ForumTopicDeleted | types.ForumTopic],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessagesSlice(TLObject):
    """
    [Read `messages.messagesSlice` docs](https://core.telegram.org/constructor/messages.messagesSlice).

    Generated from the following TL definition:
    ```tl
    messages.messagesSlice#5f206716 flags:# inexact:flags.1?true count:int next_rate:flags.0?int offset_id_offset:flags.2?int search_flood:flags.3?SearchPostsFlood messages:Vector<Message> topics:Vector<ForumTopic> chats:Vector<Chat> users:Vector<User> = messages.Messages
    ```
    """
    def __new__(
        cls,
        inexact: bool,
        count: int,
        next_rate: Optional[int],
        offset_id_offset: Optional[int],
        search_flood: Optional[types.SearchPostsFlood],
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        topics: Sequence[types.ForumTopicDeleted | types.ForumTopic],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelMessages(TLObject):
    """
    [Read `messages.channelMessages` docs](https://core.telegram.org/constructor/messages.channelMessages).

    Generated from the following TL definition:
    ```tl
    messages.channelMessages#c776ba4e flags:# inexact:flags.1?true pts:int count:int offset_id_offset:flags.2?int messages:Vector<Message> topics:Vector<ForumTopic> chats:Vector<Chat> users:Vector<User> = messages.Messages
    ```
    """
    def __new__(
        cls,
        inexact: bool,
        pts: int,
        count: int,
        offset_id_offset: Optional[int],
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        topics: Sequence[types.ForumTopicDeleted | types.ForumTopic],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessagesNotModified(TLObject):
    """
    [Read `messages.messagesNotModified` docs](https://core.telegram.org/constructor/messages.messagesNotModified).

    Generated from the following TL definition:
    ```tl
    messages.messagesNotModified#74535f21 count:int = messages.Messages
    ```
    """
    def __new__(
        cls,
        count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Chats(TLObject):
    """
    [Read `messages.chats` docs](https://core.telegram.org/constructor/messages.chats).

    Generated from the following TL definition:
    ```tl
    messages.chats#64ff9fd5 chats:Vector<Chat> = messages.Chats
    ```
    """
    def __new__(
        cls,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatsSlice(TLObject):
    """
    [Read `messages.chatsSlice` docs](https://core.telegram.org/constructor/messages.chatsSlice).

    Generated from the following TL definition:
    ```tl
    messages.chatsSlice#9cd81144 count:int chats:Vector<Chat> = messages.Chats
    ```
    """
    def __new__(
        cls,
        count: int,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatFull(TLObject):
    """
    [Read `messages.chatFull` docs](https://core.telegram.org/constructor/messages.chatFull).

    Generated from the following TL definition:
    ```tl
    messages.chatFull#e5d7d19c full_chat:ChatFull chats:Vector<Chat> users:Vector<User> = messages.ChatFull
    ```
    """
    def __new__(
        cls,
        full_chat: types.ChatFull | types.ChannelFull,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AffectedHistory(TLObject):
    """
    [Read `messages.affectedHistory` docs](https://core.telegram.org/constructor/messages.affectedHistory).

    Generated from the following TL definition:
    ```tl
    messages.affectedHistory#b45c69d1 pts:int pts_count:int offset:int = messages.AffectedHistory
    ```
    """
    def __new__(
        cls,
        pts: int,
        pts_count: int,
        offset: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DhConfigNotModified(TLObject):
    """
    [Read `messages.dhConfigNotModified` docs](https://core.telegram.org/constructor/messages.dhConfigNotModified).

    Generated from the following TL definition:
    ```tl
    messages.dhConfigNotModified#c0e24635 random:bytes = messages.DhConfig
    ```
    """
    def __new__(
        cls,
        random: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DhConfig(TLObject):
    """
    [Read `messages.dhConfig` docs](https://core.telegram.org/constructor/messages.dhConfig).

    Generated from the following TL definition:
    ```tl
    messages.dhConfig#2c221edd g:int p:bytes version:int random:bytes = messages.DhConfig
    ```
    """
    def __new__(
        cls,
        g: int,
        p: bytes,
        version: int,
        random: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentEncryptedMessage(TLObject):
    """
    [Read `messages.sentEncryptedMessage` docs](https://core.telegram.org/constructor/messages.sentEncryptedMessage).

    Generated from the following TL definition:
    ```tl
    messages.sentEncryptedMessage#560f8935 date:int = messages.SentEncryptedMessage
    ```
    """
    def __new__(
        cls,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SentEncryptedFile(TLObject):
    """
    [Read `messages.sentEncryptedFile` docs](https://core.telegram.org/constructor/messages.sentEncryptedFile).

    Generated from the following TL definition:
    ```tl
    messages.sentEncryptedFile#9493ff32 date:int file:EncryptedFile = messages.SentEncryptedMessage
    ```
    """
    def __new__(
        cls,
        date: int,
        file: types.EncryptedFileEmpty | types.EncryptedFile,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StickersNotModified(TLObject):
    """
    [Read `messages.stickersNotModified` docs](https://core.telegram.org/constructor/messages.stickersNotModified).

    Generated from the following TL definition:
    ```tl
    messages.stickersNotModified#f1749a22 = messages.Stickers
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Stickers(TLObject):
    """
    [Read `messages.stickers` docs](https://core.telegram.org/constructor/messages.stickers).

    Generated from the following TL definition:
    ```tl
    messages.stickers#30a6ec7e hash:long stickers:Vector<Document> = messages.Stickers
    ```
    """
    def __new__(
        cls,
        hash: int,
        stickers: Sequence[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AllStickersNotModified(TLObject):
    """
    [Read `messages.allStickersNotModified` docs](https://core.telegram.org/constructor/messages.allStickersNotModified).

    Generated from the following TL definition:
    ```tl
    messages.allStickersNotModified#e86602c3 = messages.AllStickers
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AllStickers(TLObject):
    """
    [Read `messages.allStickers` docs](https://core.telegram.org/constructor/messages.allStickers).

    Generated from the following TL definition:
    ```tl
    messages.allStickers#cdbbcebb hash:long sets:Vector<StickerSet> = messages.AllStickers
    ```
    """
    def __new__(
        cls,
        hash: int,
        sets: Sequence[types.StickerSet],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AffectedMessages(TLObject):
    """
    [Read `messages.affectedMessages` docs](https://core.telegram.org/constructor/messages.affectedMessages).

    Generated from the following TL definition:
    ```tl
    messages.affectedMessages#84d19185 pts:int pts_count:int = messages.AffectedMessages
    ```
    """
    def __new__(
        cls,
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StickerSet(TLObject):
    """
    [Read `messages.stickerSet` docs](https://core.telegram.org/constructor/messages.stickerSet).

    Generated from the following TL definition:
    ```tl
    messages.stickerSet#6e153f16 set:StickerSet packs:Vector<StickerPack> keywords:Vector<StickerKeyword> documents:Vector<Document> = messages.StickerSet
    ```
    """
    def __new__(
        cls,
        set: types.StickerSet,
        packs: Sequence[types.StickerPack],
        keywords: Sequence[types.StickerKeyword],
        documents: Sequence[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StickerSetNotModified(TLObject):
    """
    [Read `messages.stickerSetNotModified` docs](https://core.telegram.org/constructor/messages.stickerSetNotModified).

    Generated from the following TL definition:
    ```tl
    messages.stickerSetNotModified#d3f924eb = messages.StickerSet
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedGifsNotModified(TLObject):
    """
    [Read `messages.savedGifsNotModified` docs](https://core.telegram.org/constructor/messages.savedGifsNotModified).

    Generated from the following TL definition:
    ```tl
    messages.savedGifsNotModified#e8025ca2 = messages.SavedGifs
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedGifs(TLObject):
    """
    [Read `messages.savedGifs` docs](https://core.telegram.org/constructor/messages.savedGifs).

    Generated from the following TL definition:
    ```tl
    messages.savedGifs#84a02a0d hash:long gifs:Vector<Document> = messages.SavedGifs
    ```
    """
    def __new__(
        cls,
        hash: int,
        gifs: Sequence[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotResults(TLObject):
    """
    [Read `messages.botResults` docs](https://core.telegram.org/constructor/messages.botResults).

    Generated from the following TL definition:
    ```tl
    messages.botResults#e021f2f6 flags:# gallery:flags.0?true query_id:long next_offset:flags.1?string switch_pm:flags.2?InlineBotSwitchPM switch_webview:flags.3?InlineBotWebView results:Vector<BotInlineResult> cache_time:int users:Vector<User> = messages.BotResults
    ```
    """
    def __new__(
        cls,
        gallery: bool,
        query_id: int,
        next_offset: Optional[str],
        switch_pm: Optional[types.InlineBotSwitchPm],
        switch_webview: Optional[types.InlineBotWebView],
        results: Sequence[types.BotInlineResult | types.BotInlineMediaResult],
        cache_time: int,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotCallbackAnswer(TLObject):
    """
    [Read `messages.botCallbackAnswer` docs](https://core.telegram.org/constructor/messages.botCallbackAnswer).

    Generated from the following TL definition:
    ```tl
    messages.botCallbackAnswer#36585ea4 flags:# alert:flags.1?true has_url:flags.3?true native_ui:flags.4?true message:flags.0?string url:flags.2?string cache_time:int = messages.BotCallbackAnswer
    ```
    """
    def __new__(
        cls,
        alert: bool,
        has_url: bool,
        native_ui: bool,
        message: Optional[str],
        url: Optional[str],
        cache_time: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEditData(TLObject):
    """
    [Read `messages.messageEditData` docs](https://core.telegram.org/constructor/messages.messageEditData).

    Generated from the following TL definition:
    ```tl
    messages.messageEditData#26b5dde6 flags:# caption:flags.0?true = messages.MessageEditData
    ```
    """
    def __new__(
        cls,
        caption: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerDialogs(TLObject):
    """
    [Read `messages.peerDialogs` docs](https://core.telegram.org/constructor/messages.peerDialogs).

    Generated from the following TL definition:
    ```tl
    messages.peerDialogs#3371c354 dialogs:Vector<Dialog> messages:Vector<Message> chats:Vector<Chat> users:Vector<User> state:updates.State = messages.PeerDialogs
    ```
    """
    def __new__(
        cls,
        dialogs: Sequence[types.Dialog | types.DialogFolder],
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
        state: types.updates.State,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FeaturedStickersNotModified(TLObject):
    """
    [Read `messages.featuredStickersNotModified` docs](https://core.telegram.org/constructor/messages.featuredStickersNotModified).

    Generated from the following TL definition:
    ```tl
    messages.featuredStickersNotModified#c6dc0c66 count:int = messages.FeaturedStickers
    ```
    """
    def __new__(
        cls,
        count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FeaturedStickers(TLObject):
    """
    [Read `messages.featuredStickers` docs](https://core.telegram.org/constructor/messages.featuredStickers).

    Generated from the following TL definition:
    ```tl
    messages.featuredStickers#be382906 flags:# premium:flags.0?true hash:long count:int sets:Vector<StickerSetCovered> unread:Vector<long> = messages.FeaturedStickers
    ```
    """
    def __new__(
        cls,
        premium: bool,
        hash: int,
        count: int,
        sets: Sequence[types.StickerSetCovered | types.StickerSetMultiCovered | types.StickerSetFullCovered | types.StickerSetNoCovered],
        unread: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RecentStickersNotModified(TLObject):
    """
    [Read `messages.recentStickersNotModified` docs](https://core.telegram.org/constructor/messages.recentStickersNotModified).

    Generated from the following TL definition:
    ```tl
    messages.recentStickersNotModified#b17f890 = messages.RecentStickers
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RecentStickers(TLObject):
    """
    [Read `messages.recentStickers` docs](https://core.telegram.org/constructor/messages.recentStickers).

    Generated from the following TL definition:
    ```tl
    messages.recentStickers#88d37c56 hash:long packs:Vector<StickerPack> stickers:Vector<Document> dates:Vector<int> = messages.RecentStickers
    ```
    """
    def __new__(
        cls,
        hash: int,
        packs: Sequence[types.StickerPack],
        stickers: Sequence[types.DocumentEmpty | types.Document],
        dates: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ArchivedStickers(TLObject):
    """
    [Read `messages.archivedStickers` docs](https://core.telegram.org/constructor/messages.archivedStickers).

    Generated from the following TL definition:
    ```tl
    messages.archivedStickers#4fcba9c8 count:int sets:Vector<StickerSetCovered> = messages.ArchivedStickers
    ```
    """
    def __new__(
        cls,
        count: int,
        sets: Sequence[types.StickerSetCovered | types.StickerSetMultiCovered | types.StickerSetFullCovered | types.StickerSetNoCovered],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StickerSetInstallResultSuccess(TLObject):
    """
    [Read `messages.stickerSetInstallResultSuccess` docs](https://core.telegram.org/constructor/messages.stickerSetInstallResultSuccess).

    Generated from the following TL definition:
    ```tl
    messages.stickerSetInstallResultSuccess#38641628 = messages.StickerSetInstallResult
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StickerSetInstallResultArchive(TLObject):
    """
    [Read `messages.stickerSetInstallResultArchive` docs](https://core.telegram.org/constructor/messages.stickerSetInstallResultArchive).

    Generated from the following TL definition:
    ```tl
    messages.stickerSetInstallResultArchive#35e410a8 sets:Vector<StickerSetCovered> = messages.StickerSetInstallResult
    ```
    """
    def __new__(
        cls,
        sets: Sequence[types.StickerSetCovered | types.StickerSetMultiCovered | types.StickerSetFullCovered | types.StickerSetNoCovered],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class HighScores(TLObject):
    """
    [Read `messages.highScores` docs](https://core.telegram.org/constructor/messages.highScores).

    Generated from the following TL definition:
    ```tl
    messages.highScores#9a3bfd99 scores:Vector<HighScore> users:Vector<User> = messages.HighScores
    ```
    """
    def __new__(
        cls,
        scores: Sequence[types.HighScore],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FavedStickersNotModified(TLObject):
    """
    [Read `messages.favedStickersNotModified` docs](https://core.telegram.org/constructor/messages.favedStickersNotModified).

    Generated from the following TL definition:
    ```tl
    messages.favedStickersNotModified#9e8fa6d3 = messages.FavedStickers
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FavedStickers(TLObject):
    """
    [Read `messages.favedStickers` docs](https://core.telegram.org/constructor/messages.favedStickers).

    Generated from the following TL definition:
    ```tl
    messages.favedStickers#2cb51097 hash:long packs:Vector<StickerPack> stickers:Vector<Document> = messages.FavedStickers
    ```
    """
    def __new__(
        cls,
        hash: int,
        packs: Sequence[types.StickerPack],
        stickers: Sequence[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FoundStickerSetsNotModified(TLObject):
    """
    [Read `messages.foundStickerSetsNotModified` docs](https://core.telegram.org/constructor/messages.foundStickerSetsNotModified).

    Generated from the following TL definition:
    ```tl
    messages.foundStickerSetsNotModified#d54b65d = messages.FoundStickerSets
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FoundStickerSets(TLObject):
    """
    [Read `messages.foundStickerSets` docs](https://core.telegram.org/constructor/messages.foundStickerSets).

    Generated from the following TL definition:
    ```tl
    messages.foundStickerSets#8af09dd2 hash:long sets:Vector<StickerSetCovered> = messages.FoundStickerSets
    ```
    """
    def __new__(
        cls,
        hash: int,
        sets: Sequence[types.StickerSetCovered | types.StickerSetMultiCovered | types.StickerSetFullCovered | types.StickerSetNoCovered],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchCounter(TLObject):
    """
    [Read `messages.searchCounter` docs](https://core.telegram.org/constructor/messages.searchCounter).

    Generated from the following TL definition:
    ```tl
    messages.searchCounter#e844ebff flags:# inexact:flags.1?true filter:MessagesFilter count:int = messages.SearchCounter
    ```
    """
    def __new__(
        cls,
        inexact: bool,
        filter: types.InputMessagesFilterEmpty | types.InputMessagesFilterPhotos | types.InputMessagesFilterVideo | types.InputMessagesFilterPhotoVideo | types.InputMessagesFilterDocument | types.InputMessagesFilterUrl | types.InputMessagesFilterGif | types.InputMessagesFilterVoice | types.InputMessagesFilterMusic | types.InputMessagesFilterChatPhotos | types.InputMessagesFilterPhoneCalls | types.InputMessagesFilterRoundVoice | types.InputMessagesFilterRoundVideo | types.InputMessagesFilterMyMentions | types.InputMessagesFilterGeo | types.InputMessagesFilterContacts | types.InputMessagesFilterPinned,
        count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InactiveChats(TLObject):
    """
    [Read `messages.inactiveChats` docs](https://core.telegram.org/constructor/messages.inactiveChats).

    Generated from the following TL definition:
    ```tl
    messages.inactiveChats#a927fec5 dates:Vector<int> chats:Vector<Chat> users:Vector<User> = messages.InactiveChats
    ```
    """
    def __new__(
        cls,
        dates: Sequence[int],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class VotesList(TLObject):
    """
    [Read `messages.votesList` docs](https://core.telegram.org/constructor/messages.votesList).

    Generated from the following TL definition:
    ```tl
    messages.votesList#4899484e flags:# count:int votes:Vector<MessagePeerVote> chats:Vector<Chat> users:Vector<User> next_offset:flags.0?string = messages.VotesList
    ```
    """
    def __new__(
        cls,
        count: int,
        votes: Sequence[types.MessagePeerVote | types.MessagePeerVoteInputOption | types.MessagePeerVoteMultiple],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
        next_offset: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageViews(TLObject):
    """
    [Read `messages.messageViews` docs](https://core.telegram.org/constructor/messages.messageViews).

    Generated from the following TL definition:
    ```tl
    messages.messageViews#b6c4f543 views:Vector<MessageViews> chats:Vector<Chat> users:Vector<User> = messages.MessageViews
    ```
    """
    def __new__(
        cls,
        views: Sequence[types.MessageViews],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DiscussionMessage(TLObject):
    """
    [Read `messages.discussionMessage` docs](https://core.telegram.org/constructor/messages.discussionMessage).

    Generated from the following TL definition:
    ```tl
    messages.discussionMessage#a6341782 flags:# messages:Vector<Message> max_id:flags.0?int read_inbox_max_id:flags.1?int read_outbox_max_id:flags.2?int unread_count:int chats:Vector<Chat> users:Vector<User> = messages.DiscussionMessage
    ```
    """
    def __new__(
        cls,
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        max_id: Optional[int],
        read_inbox_max_id: Optional[int],
        read_outbox_max_id: Optional[int],
        unread_count: int,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class HistoryImport(TLObject):
    """
    [Read `messages.historyImport` docs](https://core.telegram.org/constructor/messages.historyImport).

    Generated from the following TL definition:
    ```tl
    messages.historyImport#1662af0b id:long = messages.HistoryImport
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class HistoryImportParsed(TLObject):
    """
    [Read `messages.historyImportParsed` docs](https://core.telegram.org/constructor/messages.historyImportParsed).

    Generated from the following TL definition:
    ```tl
    messages.historyImportParsed#5e0fb7b9 flags:# pm:flags.0?true group:flags.1?true title:flags.2?string = messages.HistoryImportParsed
    ```
    """
    def __new__(
        cls,
        pm: bool,
        group: bool,
        title: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AffectedFoundMessages(TLObject):
    """
    [Read `messages.affectedFoundMessages` docs](https://core.telegram.org/constructor/messages.affectedFoundMessages).

    Generated from the following TL definition:
    ```tl
    messages.affectedFoundMessages#ef8d3e6c pts:int pts_count:int offset:int messages:Vector<int> = messages.AffectedFoundMessages
    ```
    """
    def __new__(
        cls,
        pts: int,
        pts_count: int,
        offset: int,
        messages: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportedChatInvites(TLObject):
    """
    [Read `messages.exportedChatInvites` docs](https://core.telegram.org/constructor/messages.exportedChatInvites).

    Generated from the following TL definition:
    ```tl
    messages.exportedChatInvites#bdc62dcc count:int invites:Vector<ExportedChatInvite> users:Vector<User> = messages.ExportedChatInvites
    ```
    """
    def __new__(
        cls,
        count: int,
        invites: Sequence[types.ChatInviteExported | types.ChatInvitePublicJoinRequests],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportedChatInvite(TLObject):
    """
    [Read `messages.exportedChatInvite` docs](https://core.telegram.org/constructor/messages.exportedChatInvite).

    Generated from the following TL definition:
    ```tl
    messages.exportedChatInvite#1871be50 invite:ExportedChatInvite users:Vector<User> = messages.ExportedChatInvite
    ```
    """
    def __new__(
        cls,
        invite: types.ChatInviteExported | types.ChatInvitePublicJoinRequests,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportedChatInviteReplaced(TLObject):
    """
    [Read `messages.exportedChatInviteReplaced` docs](https://core.telegram.org/constructor/messages.exportedChatInviteReplaced).

    Generated from the following TL definition:
    ```tl
    messages.exportedChatInviteReplaced#222600ef invite:ExportedChatInvite new_invite:ExportedChatInvite users:Vector<User> = messages.ExportedChatInvite
    ```
    """
    def __new__(
        cls,
        invite: types.ChatInviteExported | types.ChatInvitePublicJoinRequests,
        new_invite: types.ChatInviteExported | types.ChatInvitePublicJoinRequests,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatInviteImporters(TLObject):
    """
    [Read `messages.chatInviteImporters` docs](https://core.telegram.org/constructor/messages.chatInviteImporters).

    Generated from the following TL definition:
    ```tl
    messages.chatInviteImporters#81b6b00a count:int importers:Vector<ChatInviteImporter> users:Vector<User> = messages.ChatInviteImporters
    ```
    """
    def __new__(
        cls,
        count: int,
        importers: Sequence[types.ChatInviteImporter],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatAdminsWithInvites(TLObject):
    """
    [Read `messages.chatAdminsWithInvites` docs](https://core.telegram.org/constructor/messages.chatAdminsWithInvites).

    Generated from the following TL definition:
    ```tl
    messages.chatAdminsWithInvites#b69b72d7 admins:Vector<ChatAdminWithInvites> users:Vector<User> = messages.ChatAdminsWithInvites
    ```
    """
    def __new__(
        cls,
        admins: Sequence[types.ChatAdminWithInvites],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckedHistoryImportPeer(TLObject):
    """
    [Read `messages.checkedHistoryImportPeer` docs](https://core.telegram.org/constructor/messages.checkedHistoryImportPeer).

    Generated from the following TL definition:
    ```tl
    messages.checkedHistoryImportPeer#a24de717 confirm_text:string = messages.CheckedHistoryImportPeer
    ```
    """
    def __new__(
        cls,
        confirm_text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SponsoredMessages(TLObject):
    """
    [Read `messages.sponsoredMessages` docs](https://core.telegram.org/constructor/messages.sponsoredMessages).

    Generated from the following TL definition:
    ```tl
    messages.sponsoredMessages#ffda656d flags:# posts_between:flags.0?int start_delay:flags.1?int between_delay:flags.2?int messages:Vector<SponsoredMessage> chats:Vector<Chat> users:Vector<User> = messages.SponsoredMessages
    ```
    """
    def __new__(
        cls,
        posts_between: Optional[int],
        start_delay: Optional[int],
        between_delay: Optional[int],
        messages: Sequence[types.SponsoredMessage],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SponsoredMessagesEmpty(TLObject):
    """
    [Read `messages.sponsoredMessagesEmpty` docs](https://core.telegram.org/constructor/messages.sponsoredMessagesEmpty).

    Generated from the following TL definition:
    ```tl
    messages.sponsoredMessagesEmpty#1839490f = messages.SponsoredMessages
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchResultsCalendar(TLObject):
    """
    [Read `messages.searchResultsCalendar` docs](https://core.telegram.org/constructor/messages.searchResultsCalendar).

    Generated from the following TL definition:
    ```tl
    messages.searchResultsCalendar#147ee23c flags:# inexact:flags.0?true count:int min_date:int min_msg_id:int offset_id_offset:flags.1?int periods:Vector<SearchResultsCalendarPeriod> messages:Vector<Message> chats:Vector<Chat> users:Vector<User> = messages.SearchResultsCalendar
    ```
    """
    def __new__(
        cls,
        inexact: bool,
        count: int,
        min_date: int,
        min_msg_id: int,
        offset_id_offset: Optional[int],
        periods: Sequence[types.SearchResultsCalendarPeriod],
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchResultsPositions(TLObject):
    """
    [Read `messages.searchResultsPositions` docs](https://core.telegram.org/constructor/messages.searchResultsPositions).

    Generated from the following TL definition:
    ```tl
    messages.searchResultsPositions#53b22baf count:int positions:Vector<SearchResultsPosition> = messages.SearchResultsPositions
    ```
    """
    def __new__(
        cls,
        count: int,
        positions: Sequence[types.SearchResultPosition],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerSettings(TLObject):
    """
    [Read `messages.peerSettings` docs](https://core.telegram.org/constructor/messages.peerSettings).

    Generated from the following TL definition:
    ```tl
    messages.peerSettings#6880b94d settings:PeerSettings chats:Vector<Chat> users:Vector<User> = messages.PeerSettings
    ```
    """
    def __new__(
        cls,
        settings: types.PeerSettings,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageReactionsList(TLObject):
    """
    [Read `messages.messageReactionsList` docs](https://core.telegram.org/constructor/messages.messageReactionsList).

    Generated from the following TL definition:
    ```tl
    messages.messageReactionsList#31bd492d flags:# count:int reactions:Vector<MessagePeerReaction> chats:Vector<Chat> users:Vector<User> next_offset:flags.0?string = messages.MessageReactionsList
    ```
    """
    def __new__(
        cls,
        count: int,
        reactions: Sequence[types.MessagePeerReaction],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
        next_offset: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AvailableReactionsNotModified(TLObject):
    """
    [Read `messages.availableReactionsNotModified` docs](https://core.telegram.org/constructor/messages.availableReactionsNotModified).

    Generated from the following TL definition:
    ```tl
    messages.availableReactionsNotModified#9f071957 = messages.AvailableReactions
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AvailableReactions(TLObject):
    """
    [Read `messages.availableReactions` docs](https://core.telegram.org/constructor/messages.availableReactions).

    Generated from the following TL definition:
    ```tl
    messages.availableReactions#768e3aad hash:int reactions:Vector<AvailableReaction> = messages.AvailableReactions
    ```
    """
    def __new__(
        cls,
        hash: int,
        reactions: Sequence[types.AvailableReaction],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TranscribedAudio(TLObject):
    """
    [Read `messages.transcribedAudio` docs](https://core.telegram.org/constructor/messages.transcribedAudio).

    Generated from the following TL definition:
    ```tl
    messages.transcribedAudio#cfb9d957 flags:# pending:flags.0?true transcription_id:long text:string trial_remains_num:flags.1?int trial_remains_until_date:flags.1?int = messages.TranscribedAudio
    ```
    """
    def __new__(
        cls,
        pending: bool,
        transcription_id: int,
        text: str,
        trial_remains_num: Optional[int],
        trial_remains_until_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReactionsNotModified(TLObject):
    """
    [Read `messages.reactionsNotModified` docs](https://core.telegram.org/constructor/messages.reactionsNotModified).

    Generated from the following TL definition:
    ```tl
    messages.reactionsNotModified#b06fdbdf = messages.Reactions
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Reactions(TLObject):
    """
    [Read `messages.reactions` docs](https://core.telegram.org/constructor/messages.reactions).

    Generated from the following TL definition:
    ```tl
    messages.reactions#eafdf716 hash:long reactions:Vector<Reaction> = messages.Reactions
    ```
    """
    def __new__(
        cls,
        hash: int,
        reactions: Sequence[types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ForumTopics(TLObject):
    """
    [Read `messages.forumTopics` docs](https://core.telegram.org/constructor/messages.forumTopics).

    Generated from the following TL definition:
    ```tl
    messages.forumTopics#367617d3 flags:# order_by_create_date:flags.0?true count:int topics:Vector<ForumTopic> messages:Vector<Message> chats:Vector<Chat> users:Vector<User> pts:int = messages.ForumTopics
    ```
    """
    def __new__(
        cls,
        order_by_create_date: bool,
        count: int,
        topics: Sequence[types.ForumTopicDeleted | types.ForumTopic],
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
        pts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiGroupsNotModified(TLObject):
    """
    [Read `messages.emojiGroupsNotModified` docs](https://core.telegram.org/constructor/messages.emojiGroupsNotModified).

    Generated from the following TL definition:
    ```tl
    messages.emojiGroupsNotModified#6fb4ad87 = messages.EmojiGroups
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiGroups(TLObject):
    """
    [Read `messages.emojiGroups` docs](https://core.telegram.org/constructor/messages.emojiGroups).

    Generated from the following TL definition:
    ```tl
    messages.emojiGroups#881fb94b hash:int groups:Vector<EmojiGroup> = messages.EmojiGroups
    ```
    """
    def __new__(
        cls,
        hash: int,
        groups: Sequence[types.EmojiGroup | types.EmojiGroupGreeting | types.EmojiGroupPremium],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TranslateResult(TLObject):
    """
    [Read `messages.translateResult` docs](https://core.telegram.org/constructor/messages.translateResult).

    Generated from the following TL definition:
    ```tl
    messages.translateResult#33db32f8 result:Vector<TextWithEntities> = messages.TranslatedText
    ```
    """
    def __new__(
        cls,
        result: Sequence[types.TextWithEntities],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotApp(TLObject):
    """
    [Read `messages.botApp` docs](https://core.telegram.org/constructor/messages.botApp).

    Generated from the following TL definition:
    ```tl
    messages.botApp#eb50adf5 flags:# inactive:flags.0?true request_write_access:flags.1?true has_settings:flags.2?true app:BotApp = messages.BotApp
    ```
    """
    def __new__(
        cls,
        inactive: bool,
        request_write_access: bool,
        has_settings: bool,
        app: types.BotAppNotModified | types.BotApp,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebPage(TLObject):
    """
    [Read `messages.webPage` docs](https://core.telegram.org/constructor/messages.webPage).

    Generated from the following TL definition:
    ```tl
    messages.webPage#fd5e12bd webpage:WebPage chats:Vector<Chat> users:Vector<User> = messages.WebPage
    ```
    """
    def __new__(
        cls,
        webpage: types.WebPageEmpty | types.WebPagePending | types.WebPage | types.WebPageNotModified,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedDialogs(TLObject):
    """
    [Read `messages.savedDialogs` docs](https://core.telegram.org/constructor/messages.savedDialogs).

    Generated from the following TL definition:
    ```tl
    messages.savedDialogs#f83ae221 dialogs:Vector<SavedDialog> messages:Vector<Message> chats:Vector<Chat> users:Vector<User> = messages.SavedDialogs
    ```
    """
    def __new__(
        cls,
        dialogs: Sequence[types.SavedDialog | types.MonoForumDialog],
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedDialogsSlice(TLObject):
    """
    [Read `messages.savedDialogsSlice` docs](https://core.telegram.org/constructor/messages.savedDialogsSlice).

    Generated from the following TL definition:
    ```tl
    messages.savedDialogsSlice#44ba9dd9 count:int dialogs:Vector<SavedDialog> messages:Vector<Message> chats:Vector<Chat> users:Vector<User> = messages.SavedDialogs
    ```
    """
    def __new__(
        cls,
        count: int,
        dialogs: Sequence[types.SavedDialog | types.MonoForumDialog],
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedDialogsNotModified(TLObject):
    """
    [Read `messages.savedDialogsNotModified` docs](https://core.telegram.org/constructor/messages.savedDialogsNotModified).

    Generated from the following TL definition:
    ```tl
    messages.savedDialogsNotModified#c01f6fe8 count:int = messages.SavedDialogs
    ```
    """
    def __new__(
        cls,
        count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedReactionTagsNotModified(TLObject):
    """
    [Read `messages.savedReactionTagsNotModified` docs](https://core.telegram.org/constructor/messages.savedReactionTagsNotModified).

    Generated from the following TL definition:
    ```tl
    messages.savedReactionTagsNotModified#889b59ef = messages.SavedReactionTags
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedReactionTags(TLObject):
    """
    [Read `messages.savedReactionTags` docs](https://core.telegram.org/constructor/messages.savedReactionTags).

    Generated from the following TL definition:
    ```tl
    messages.savedReactionTags#3259950a tags:Vector<SavedReactionTag> hash:long = messages.SavedReactionTags
    ```
    """
    def __new__(
        cls,
        tags: Sequence[types.SavedReactionTag],
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class QuickReplies(TLObject):
    """
    [Read `messages.quickReplies` docs](https://core.telegram.org/constructor/messages.quickReplies).

    Generated from the following TL definition:
    ```tl
    messages.quickReplies#c68d6695 quick_replies:Vector<QuickReply> messages:Vector<Message> chats:Vector<Chat> users:Vector<User> = messages.QuickReplies
    ```
    """
    def __new__(
        cls,
        quick_replies: Sequence[types.QuickReply],
        messages: Sequence[types.MessageEmpty | types.Message | types.MessageService],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class QuickRepliesNotModified(TLObject):
    """
    [Read `messages.quickRepliesNotModified` docs](https://core.telegram.org/constructor/messages.quickRepliesNotModified).

    Generated from the following TL definition:
    ```tl
    messages.quickRepliesNotModified#5f91eb5b = messages.QuickReplies
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DialogFilters(TLObject):
    """
    [Read `messages.dialogFilters` docs](https://core.telegram.org/constructor/messages.dialogFilters).

    Generated from the following TL definition:
    ```tl
    messages.dialogFilters#2ad93719 flags:# tags_enabled:flags.0?true filters:Vector<DialogFilter> = messages.DialogFilters
    ```
    """
    def __new__(
        cls,
        tags_enabled: bool,
        filters: Sequence[types.DialogFilter | types.DialogFilterDefault | types.DialogFilterChatlist],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MyStickers(TLObject):
    """
    [Read `messages.myStickers` docs](https://core.telegram.org/constructor/messages.myStickers).

    Generated from the following TL definition:
    ```tl
    messages.myStickers#faff629d count:int sets:Vector<StickerSetCovered> = messages.MyStickers
    ```
    """
    def __new__(
        cls,
        count: int,
        sets: Sequence[types.StickerSetCovered | types.StickerSetMultiCovered | types.StickerSetFullCovered | types.StickerSetNoCovered],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InvitedUsers(TLObject):
    """
    [Read `messages.invitedUsers` docs](https://core.telegram.org/constructor/messages.invitedUsers).

    Generated from the following TL definition:
    ```tl
    messages.invitedUsers#7f5defa6 updates:Updates missing_invitees:Vector<MissingInvitee> = messages.InvitedUsers
    ```
    """
    def __new__(
        cls,
        updates: types.UpdatesTooLong | types.UpdateShortMessage | types.UpdateShortChatMessage | types.UpdateShort | types.UpdatesCombined | types.Updates | types.UpdateShortSentMessage,
        missing_invitees: Sequence[types.MissingInvitee],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AvailableEffectsNotModified(TLObject):
    """
    [Read `messages.availableEffectsNotModified` docs](https://core.telegram.org/constructor/messages.availableEffectsNotModified).

    Generated from the following TL definition:
    ```tl
    messages.availableEffectsNotModified#d1ed9a5b = messages.AvailableEffects
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AvailableEffects(TLObject):
    """
    [Read `messages.availableEffects` docs](https://core.telegram.org/constructor/messages.availableEffects).

    Generated from the following TL definition:
    ```tl
    messages.availableEffects#bddb616e hash:int effects:Vector<AvailableEffect> documents:Vector<Document> = messages.AvailableEffects
    ```
    """
    def __new__(
        cls,
        hash: int,
        effects: Sequence[types.AvailableEffect],
        documents: Sequence[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotPreparedInlineMessage(TLObject):
    """
    [Read `messages.botPreparedInlineMessage` docs](https://core.telegram.org/constructor/messages.botPreparedInlineMessage).

    Generated from the following TL definition:
    ```tl
    messages.botPreparedInlineMessage#8ecf0511 id:string expire_date:int = messages.BotPreparedInlineMessage
    ```
    """
    def __new__(
        cls,
        id: str,
        expire_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PreparedInlineMessage(TLObject):
    """
    [Read `messages.preparedInlineMessage` docs](https://core.telegram.org/constructor/messages.preparedInlineMessage).

    Generated from the following TL definition:
    ```tl
    messages.preparedInlineMessage#ff57708d query_id:long result:BotInlineResult peer_types:Vector<InlineQueryPeerType> cache_time:int users:Vector<User> = messages.PreparedInlineMessage
    ```
    """
    def __new__(
        cls,
        query_id: int,
        result: types.BotInlineResult | types.BotInlineMediaResult,
        peer_types: Sequence[types.InlineQueryPeerTypeSameBotPm | types.InlineQueryPeerTypePm | types.InlineQueryPeerTypeChat | types.InlineQueryPeerTypeMegagroup | types.InlineQueryPeerTypeBroadcast | types.InlineQueryPeerTypeBotPm],
        cache_time: int,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FoundStickersNotModified(TLObject):
    """
    [Read `messages.foundStickersNotModified` docs](https://core.telegram.org/constructor/messages.foundStickersNotModified).

    Generated from the following TL definition:
    ```tl
    messages.foundStickersNotModified#6010c534 flags:# next_offset:flags.0?int = messages.FoundStickers
    ```
    """
    def __new__(
        cls,
        next_offset: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FoundStickers(TLObject):
    """
    [Read `messages.foundStickers` docs](https://core.telegram.org/constructor/messages.foundStickers).

    Generated from the following TL definition:
    ```tl
    messages.foundStickers#82c9e290 flags:# next_offset:flags.0?int hash:long stickers:Vector<Document> = messages.FoundStickers
    ```
    """
    def __new__(
        cls,
        next_offset: Optional[int],
        hash: int,
        stickers: Sequence[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebPagePreview(TLObject):
    """
    [Read `messages.webPagePreview` docs](https://core.telegram.org/constructor/messages.webPagePreview).

    Generated from the following TL definition:
    ```tl
    messages.webPagePreview#8c9a88ac media:MessageMedia chats:Vector<Chat> users:Vector<User> = messages.WebPagePreview
    ```
    """
    def __new__(
        cls,
        media: types.MessageMediaEmpty | types.MessageMediaPhoto | types.MessageMediaGeo | types.MessageMediaContact | types.MessageMediaUnsupported | types.MessageMediaDocument | types.MessageMediaWebPage | types.MessageMediaVenue | types.MessageMediaGame | types.MessageMediaInvoice | types.MessageMediaGeoLive | types.MessageMediaPoll | types.MessageMediaDice | types.MessageMediaStory | types.MessageMediaGiveaway | types.MessageMediaGiveawayResults | types.MessageMediaPaidMedia | types.MessageMediaToDo | types.MessageMediaVideoStream,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiGameOutcome(TLObject):
    """
    [Read `messages.emojiGameOutcome` docs](https://core.telegram.org/constructor/messages.emojiGameOutcome).

    Generated from the following TL definition:
    ```tl
    messages.emojiGameOutcome#da2ad647 seed:bytes stake_ton_amount:long ton_amount:long = messages.EmojiGameOutcome
    ```
    """
    def __new__(
        cls,
        seed: bytes,
        stake_ton_amount: int,
        ton_amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiGameUnavailable(TLObject):
    """
    [Read `messages.emojiGameUnavailable` docs](https://core.telegram.org/constructor/messages.emojiGameUnavailable).

    Generated from the following TL definition:
    ```tl
    messages.emojiGameUnavailable#59e65335 = messages.EmojiGameInfo
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiGameDiceInfo(TLObject):
    """
    [Read `messages.emojiGameDiceInfo` docs](https://core.telegram.org/constructor/messages.emojiGameDiceInfo).

    Generated from the following TL definition:
    ```tl
    messages.emojiGameDiceInfo#44e56023 flags:# game_hash:string prev_stake:long current_streak:int params:Vector<int> plays_left:flags.0?int = messages.EmojiGameInfo
    ```
    """
    def __new__(
        cls,
        game_hash: str,
        prev_stake: int,
        current_streak: int,
        params: Sequence[int],
        plays_left: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

