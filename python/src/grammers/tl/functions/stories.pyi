from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class CanSendStory(TLRequest):
    """
    [Read `stories.canSendStory` docs](https://core.telegram.org/method/stories.canSendStory).

    Generated from the following TL definition:
    ```tl
    stories.canSendStory#30eb63f0 peer:InputPeer = stories.CanSendStoryCount
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendStory(TLRequest):
    """
    [Read `stories.sendStory` docs](https://core.telegram.org/method/stories.sendStory).

    Generated from the following TL definition:
    ```tl
    stories.sendStory#737fc2ec flags:# pinned:flags.2?true noforwards:flags.4?true fwd_modified:flags.7?true peer:InputPeer media:InputMedia media_areas:flags.5?Vector<MediaArea> caption:flags.0?string entities:flags.1?Vector<MessageEntity> privacy_rules:Vector<InputPrivacyRule> random_id:long period:flags.3?int fwd_from_id:flags.6?InputPeer fwd_from_story:flags.6?int albums:flags.8?Vector<int> = Updates
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        noforwards: bool,
        fwd_modified: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        media: types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice,
        media_areas: Optional[Sequence[types.MediaAreaVenue | types.InputMediaAreaVenue | types.MediaAreaGeoPoint | types.MediaAreaSuggestedReaction | types.MediaAreaChannelPost | types.InputMediaAreaChannelPost | types.MediaAreaUrl | types.MediaAreaWeather | types.MediaAreaStarGift]],
        caption: Optional[str],
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        privacy_rules: Sequence[types.InputPrivacyValueAllowContacts | types.InputPrivacyValueAllowAll | types.InputPrivacyValueAllowUsers | types.InputPrivacyValueDisallowContacts | types.InputPrivacyValueDisallowAll | types.InputPrivacyValueDisallowUsers | types.InputPrivacyValueAllowChatParticipants | types.InputPrivacyValueDisallowChatParticipants | types.InputPrivacyValueAllowCloseFriends | types.InputPrivacyValueAllowPremium | types.InputPrivacyValueAllowBots | types.InputPrivacyValueDisallowBots],
        random_id: int,
        period: Optional[int],
        fwd_from_id: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        fwd_from_story: Optional[int],
        albums: Optional[Sequence[int]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditStory(TLRequest):
    """
    [Read `stories.editStory` docs](https://core.telegram.org/method/stories.editStory).

    Generated from the following TL definition:
    ```tl
    stories.editStory#b583ba46 flags:# peer:InputPeer id:int media:flags.0?InputMedia media_areas:flags.3?Vector<MediaArea> caption:flags.1?string entities:flags.1?Vector<MessageEntity> privacy_rules:flags.2?Vector<InputPrivacyRule> = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
        media: Optional[types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice],
        media_areas: Optional[Sequence[types.MediaAreaVenue | types.InputMediaAreaVenue | types.MediaAreaGeoPoint | types.MediaAreaSuggestedReaction | types.MediaAreaChannelPost | types.InputMediaAreaChannelPost | types.MediaAreaUrl | types.MediaAreaWeather | types.MediaAreaStarGift]],
        caption: Optional[str],
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        privacy_rules: Optional[Sequence[types.InputPrivacyValueAllowContacts | types.InputPrivacyValueAllowAll | types.InputPrivacyValueAllowUsers | types.InputPrivacyValueDisallowContacts | types.InputPrivacyValueDisallowAll | types.InputPrivacyValueDisallowUsers | types.InputPrivacyValueAllowChatParticipants | types.InputPrivacyValueDisallowChatParticipants | types.InputPrivacyValueAllowCloseFriends | types.InputPrivacyValueAllowPremium | types.InputPrivacyValueAllowBots | types.InputPrivacyValueDisallowBots]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteStories(TLRequest):
    """
    [Read `stories.deleteStories` docs](https://core.telegram.org/method/stories.deleteStories).

    Generated from the following TL definition:
    ```tl
    stories.deleteStories#ae59db5f peer:InputPeer id:Vector<int> = Vector<int>
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TogglePinned(TLRequest):
    """
    [Read `stories.togglePinned` docs](https://core.telegram.org/method/stories.togglePinned).

    Generated from the following TL definition:
    ```tl
    stories.togglePinned#9a75a1ef peer:InputPeer id:Vector<int> pinned:Bool = Vector<int>
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
        pinned: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAllStories(TLRequest):
    """
    [Read `stories.getAllStories` docs](https://core.telegram.org/method/stories.getAllStories).

    Generated from the following TL definition:
    ```tl
    stories.getAllStories#eeb0d625 flags:# next:flags.1?true hidden:flags.2?true state:flags.0?string = stories.AllStories
    ```
    """
    def __new__(
        cls,
        next: bool,
        hidden: bool,
        state: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPinnedStories(TLRequest):
    """
    [Read `stories.getPinnedStories` docs](https://core.telegram.org/method/stories.getPinnedStories).

    Generated from the following TL definition:
    ```tl
    stories.getPinnedStories#5821a5dc peer:InputPeer offset_id:int limit:int = stories.Stories
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        offset_id: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStoriesArchive(TLRequest):
    """
    [Read `stories.getStoriesArchive` docs](https://core.telegram.org/method/stories.getStoriesArchive).

    Generated from the following TL definition:
    ```tl
    stories.getStoriesArchive#b4352016 peer:InputPeer offset_id:int limit:int = stories.Stories
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        offset_id: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStoriesById(TLRequest):
    """
    [Read `stories.getStoriesByID` docs](https://core.telegram.org/method/stories.getStoriesByID).

    Generated from the following TL definition:
    ```tl
    stories.getStoriesByID#5774ca74 peer:InputPeer id:Vector<int> = stories.Stories
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleAllStoriesHidden(TLRequest):
    """
    [Read `stories.toggleAllStoriesHidden` docs](https://core.telegram.org/method/stories.toggleAllStoriesHidden).

    Generated from the following TL definition:
    ```tl
    stories.toggleAllStoriesHidden#7c2557c4 hidden:Bool = Bool
    ```
    """
    def __new__(
        cls,
        hidden: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReadStories(TLRequest):
    """
    [Read `stories.readStories` docs](https://core.telegram.org/method/stories.readStories).

    Generated from the following TL definition:
    ```tl
    stories.readStories#a556dac8 peer:InputPeer max_id:int = Vector<int>
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class IncrementStoryViews(TLRequest):
    """
    [Read `stories.incrementStoryViews` docs](https://core.telegram.org/method/stories.incrementStoryViews).

    Generated from the following TL definition:
    ```tl
    stories.incrementStoryViews#b2028afb peer:InputPeer id:Vector<int> = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStoryViewsList(TLRequest):
    """
    [Read `stories.getStoryViewsList` docs](https://core.telegram.org/method/stories.getStoryViewsList).

    Generated from the following TL definition:
    ```tl
    stories.getStoryViewsList#7ed23c57 flags:# just_contacts:flags.0?true reactions_first:flags.2?true forwards_first:flags.3?true peer:InputPeer q:flags.1?string id:int offset:string limit:int = stories.StoryViewsList
    ```
    """
    def __new__(
        cls,
        just_contacts: bool,
        reactions_first: bool,
        forwards_first: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        q: Optional[str],
        id: int,
        offset: str,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStoriesViews(TLRequest):
    """
    [Read `stories.getStoriesViews` docs](https://core.telegram.org/method/stories.getStoriesViews).

    Generated from the following TL definition:
    ```tl
    stories.getStoriesViews#28e16cc8 peer:InputPeer id:Vector<int> = stories.StoryViews
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportStoryLink(TLRequest):
    """
    [Read `stories.exportStoryLink` docs](https://core.telegram.org/method/stories.exportStoryLink).

    Generated from the following TL definition:
    ```tl
    stories.exportStoryLink#7b8def20 peer:InputPeer id:int = ExportedStoryLink
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Report(TLRequest):
    """
    [Read `stories.report` docs](https://core.telegram.org/method/stories.report).

    Generated from the following TL definition:
    ```tl
    stories.report#19d8eb45 peer:InputPeer id:Vector<int> option:bytes message:string = ReportResult
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
class ActivateStealthMode(TLRequest):
    """
    [Read `stories.activateStealthMode` docs](https://core.telegram.org/method/stories.activateStealthMode).

    Generated from the following TL definition:
    ```tl
    stories.activateStealthMode#57bbd166 flags:# past:flags.0?true future:flags.1?true = Updates
    ```
    """
    def __new__(
        cls,
        past: bool,
        future: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendReaction(TLRequest):
    """
    [Read `stories.sendReaction` docs](https://core.telegram.org/method/stories.sendReaction).

    Generated from the following TL definition:
    ```tl
    stories.sendReaction#7fd736b2 flags:# add_to_recent:flags.0?true peer:InputPeer story_id:int reaction:Reaction = Updates
    ```
    """
    def __new__(
        cls,
        add_to_recent: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        story_id: int,
        reaction: types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPeerStories(TLRequest):
    """
    [Read `stories.getPeerStories` docs](https://core.telegram.org/method/stories.getPeerStories).

    Generated from the following TL definition:
    ```tl
    stories.getPeerStories#2c4ada50 peer:InputPeer = stories.PeerStories
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAllReadPeerStories(TLRequest):
    """
    [Read `stories.getAllReadPeerStories` docs](https://core.telegram.org/method/stories.getAllReadPeerStories).

    Generated from the following TL definition:
    ```tl
    stories.getAllReadPeerStories#9b5ae7f9 = Updates
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPeerMaxIds(TLRequest):
    """
    [Read `stories.getPeerMaxIDs` docs](https://core.telegram.org/method/stories.getPeerMaxIDs).

    Generated from the following TL definition:
    ```tl
    stories.getPeerMaxIDs#78499170 id:Vector<InputPeer> = Vector<RecentStory>
    ```
    """
    def __new__(
        cls,
        id: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetChatsToSend(TLRequest):
    """
    [Read `stories.getChatsToSend` docs](https://core.telegram.org/method/stories.getChatsToSend).

    Generated from the following TL definition:
    ```tl
    stories.getChatsToSend#a56a8b60 = messages.Chats
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TogglePeerStoriesHidden(TLRequest):
    """
    [Read `stories.togglePeerStoriesHidden` docs](https://core.telegram.org/method/stories.togglePeerStoriesHidden).

    Generated from the following TL definition:
    ```tl
    stories.togglePeerStoriesHidden#bd0415c4 peer:InputPeer hidden:Bool = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        hidden: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStoryReactionsList(TLRequest):
    """
    [Read `stories.getStoryReactionsList` docs](https://core.telegram.org/method/stories.getStoryReactionsList).

    Generated from the following TL definition:
    ```tl
    stories.getStoryReactionsList#b9b2881f flags:# forwards_first:flags.2?true peer:InputPeer id:int reaction:flags.0?Reaction offset:flags.1?string limit:int = stories.StoryReactionsList
    ```
    """
    def __new__(
        cls,
        forwards_first: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
        reaction: Optional[types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid],
        offset: Optional[str],
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TogglePinnedToTop(TLRequest):
    """
    [Read `stories.togglePinnedToTop` docs](https://core.telegram.org/method/stories.togglePinnedToTop).

    Generated from the following TL definition:
    ```tl
    stories.togglePinnedToTop#b297e9b peer:InputPeer id:Vector<int> = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchPosts(TLRequest):
    """
    [Read `stories.searchPosts` docs](https://core.telegram.org/method/stories.searchPosts).

    Generated from the following TL definition:
    ```tl
    stories.searchPosts#d1810907 flags:# hashtag:flags.0?string area:flags.1?MediaArea peer:flags.2?InputPeer offset:string limit:int = stories.FoundStories
    ```
    """
    def __new__(
        cls,
        hashtag: Optional[str],
        area: Optional[types.MediaAreaVenue | types.InputMediaAreaVenue | types.MediaAreaGeoPoint | types.MediaAreaSuggestedReaction | types.MediaAreaChannelPost | types.InputMediaAreaChannelPost | types.MediaAreaUrl | types.MediaAreaWeather | types.MediaAreaStarGift],
        peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        offset: str,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CreateAlbum(TLRequest):
    """
    [Read `stories.createAlbum` docs](https://core.telegram.org/method/stories.createAlbum).

    Generated from the following TL definition:
    ```tl
    stories.createAlbum#a36396e5 peer:InputPeer title:string stories:Vector<int> = StoryAlbum
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        title: str,
        stories: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateAlbum(TLRequest):
    """
    [Read `stories.updateAlbum` docs](https://core.telegram.org/method/stories.updateAlbum).

    Generated from the following TL definition:
    ```tl
    stories.updateAlbum#5e5259b6 flags:# peer:InputPeer album_id:int title:flags.0?string delete_stories:flags.1?Vector<int> add_stories:flags.2?Vector<int> order:flags.3?Vector<int> = StoryAlbum
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        album_id: int,
        title: Optional[str],
        delete_stories: Optional[Sequence[int]],
        add_stories: Optional[Sequence[int]],
        order: Optional[Sequence[int]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReorderAlbums(TLRequest):
    """
    [Read `stories.reorderAlbums` docs](https://core.telegram.org/method/stories.reorderAlbums).

    Generated from the following TL definition:
    ```tl
    stories.reorderAlbums#8535fbd9 peer:InputPeer order:Vector<int> = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        order: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteAlbum(TLRequest):
    """
    [Read `stories.deleteAlbum` docs](https://core.telegram.org/method/stories.deleteAlbum).

    Generated from the following TL definition:
    ```tl
    stories.deleteAlbum#8d3456d0 peer:InputPeer album_id:int = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        album_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAlbums(TLRequest):
    """
    [Read `stories.getAlbums` docs](https://core.telegram.org/method/stories.getAlbums).

    Generated from the following TL definition:
    ```tl
    stories.getAlbums#25b3eac7 peer:InputPeer hash:long = stories.Albums
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAlbumStories(TLRequest):
    """
    [Read `stories.getAlbumStories` docs](https://core.telegram.org/method/stories.getAlbumStories).

    Generated from the following TL definition:
    ```tl
    stories.getAlbumStories#ac806d61 peer:InputPeer album_id:int offset:int limit:int = stories.Stories
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        album_id: int,
        offset: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StartLive(TLRequest):
    """
    [Read `stories.startLive` docs](https://core.telegram.org/method/stories.startLive).

    Generated from the following TL definition:
    ```tl
    stories.startLive#d069ccde flags:# pinned:flags.2?true noforwards:flags.4?true rtmp_stream:flags.5?true peer:InputPeer caption:flags.0?string entities:flags.1?Vector<MessageEntity> privacy_rules:Vector<InputPrivacyRule> random_id:long messages_enabled:flags.6?Bool send_paid_messages_stars:flags.7?long = Updates
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        noforwards: bool,
        rtmp_stream: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        caption: Optional[str],
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        privacy_rules: Sequence[types.InputPrivacyValueAllowContacts | types.InputPrivacyValueAllowAll | types.InputPrivacyValueAllowUsers | types.InputPrivacyValueDisallowContacts | types.InputPrivacyValueDisallowAll | types.InputPrivacyValueDisallowUsers | types.InputPrivacyValueAllowChatParticipants | types.InputPrivacyValueDisallowChatParticipants | types.InputPrivacyValueAllowCloseFriends | types.InputPrivacyValueAllowPremium | types.InputPrivacyValueAllowBots | types.InputPrivacyValueDisallowBots],
        random_id: int,
        messages_enabled: Optional[bool],
        send_paid_messages_stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

