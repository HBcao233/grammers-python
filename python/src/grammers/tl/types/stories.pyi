from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class AllStoriesNotModified(TLObject):
    """
    [Read `stories.allStoriesNotModified` docs](https://core.telegram.org/constructor/stories.allStoriesNotModified).

    Generated from the following TL definition:
    ```tl
    stories.allStoriesNotModified#1158fe3e flags:# state:string stealth_mode:StoriesStealthMode = stories.AllStories
    ```
    """
    def __new__(
        cls,
        state: str,
        stealth_mode: types.StoriesStealthMode,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AllStories(TLObject):
    """
    [Read `stories.allStories` docs](https://core.telegram.org/constructor/stories.allStories).

    Generated from the following TL definition:
    ```tl
    stories.allStories#6efc5e81 flags:# has_more:flags.0?true count:int state:string peer_stories:Vector<PeerStories> chats:Vector<Chat> users:Vector<User> stealth_mode:StoriesStealthMode = stories.AllStories
    ```
    """
    def __new__(
        cls,
        has_more: bool,
        count: int,
        state: str,
        peer_stories: Sequence[types.PeerStories],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
        stealth_mode: types.StoriesStealthMode,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Stories(TLObject):
    """
    [Read `stories.stories` docs](https://core.telegram.org/constructor/stories.stories).

    Generated from the following TL definition:
    ```tl
    stories.stories#63c3dd0a flags:# count:int stories:Vector<StoryItem> pinned_to_top:flags.0?Vector<int> chats:Vector<Chat> users:Vector<User> = stories.Stories
    ```
    """
    def __new__(
        cls,
        count: int,
        stories: Sequence[types.StoryItemDeleted | types.StoryItemSkipped | types.StoryItem],
        pinned_to_top: Optional[Sequence[int]],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryViewsList(TLObject):
    """
    [Read `stories.storyViewsList` docs](https://core.telegram.org/constructor/stories.storyViewsList).

    Generated from the following TL definition:
    ```tl
    stories.storyViewsList#59d78fc5 flags:# count:int views_count:int forwards_count:int reactions_count:int views:Vector<StoryView> chats:Vector<Chat> users:Vector<User> next_offset:flags.0?string = stories.StoryViewsList
    ```
    """
    def __new__(
        cls,
        count: int,
        views_count: int,
        forwards_count: int,
        reactions_count: int,
        views: Sequence[types.StoryView | types.StoryViewPublicForward | types.StoryViewPublicRepost],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
        next_offset: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryViews(TLObject):
    """
    [Read `stories.storyViews` docs](https://core.telegram.org/constructor/stories.storyViews).

    Generated from the following TL definition:
    ```tl
    stories.storyViews#de9eed1d views:Vector<StoryViews> users:Vector<User> = stories.StoryViews
    ```
    """
    def __new__(
        cls,
        views: Sequence[types.StoryViews],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerStories(TLObject):
    """
    [Read `stories.peerStories` docs](https://core.telegram.org/constructor/stories.peerStories).

    Generated from the following TL definition:
    ```tl
    stories.peerStories#cae68768 stories:PeerStories chats:Vector<Chat> users:Vector<User> = stories.PeerStories
    ```
    """
    def __new__(
        cls,
        stories: types.PeerStories,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryReactionsList(TLObject):
    """
    [Read `stories.storyReactionsList` docs](https://core.telegram.org/constructor/stories.storyReactionsList).

    Generated from the following TL definition:
    ```tl
    stories.storyReactionsList#aa5f789c flags:# count:int reactions:Vector<StoryReaction> chats:Vector<Chat> users:Vector<User> next_offset:flags.0?string = stories.StoryReactionsList
    ```
    """
    def __new__(
        cls,
        count: int,
        reactions: Sequence[types.StoryReaction | types.StoryReactionPublicForward | types.StoryReactionPublicRepost],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
        next_offset: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FoundStories(TLObject):
    """
    [Read `stories.foundStories` docs](https://core.telegram.org/constructor/stories.foundStories).

    Generated from the following TL definition:
    ```tl
    stories.foundStories#e2de7737 flags:# count:int stories:Vector<FoundStory> next_offset:flags.0?string chats:Vector<Chat> users:Vector<User> = stories.FoundStories
    ```
    """
    def __new__(
        cls,
        count: int,
        stories: Sequence[types.FoundStory],
        next_offset: Optional[str],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CanSendStoryCount(TLObject):
    """
    [Read `stories.canSendStoryCount` docs](https://core.telegram.org/constructor/stories.canSendStoryCount).

    Generated from the following TL definition:
    ```tl
    stories.canSendStoryCount#c387c04e count_remains:int = stories.CanSendStoryCount
    ```
    """
    def __new__(
        cls,
        count_remains: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AlbumsNotModified(TLObject):
    """
    [Read `stories.albumsNotModified` docs](https://core.telegram.org/constructor/stories.albumsNotModified).

    Generated from the following TL definition:
    ```tl
    stories.albumsNotModified#564edaeb = stories.Albums
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Albums(TLObject):
    """
    [Read `stories.albums` docs](https://core.telegram.org/constructor/stories.albums).

    Generated from the following TL definition:
    ```tl
    stories.albums#c3987a3a hash:long albums:Vector<StoryAlbum> = stories.Albums
    ```
    """
    def __new__(
        cls,
        hash: int,
        albums: Sequence[types.StoryAlbum],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

