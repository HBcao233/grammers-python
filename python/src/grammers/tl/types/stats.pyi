from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class BroadcastStats(TLObject):
    """
    [Read `stats.broadcastStats` docs](https://core.telegram.org/constructor/stats.broadcastStats).

    Generated from the following TL definition:
    ```tl
    stats.broadcastStats#396ca5fc period:StatsDateRangeDays followers:StatsAbsValueAndPrev views_per_post:StatsAbsValueAndPrev shares_per_post:StatsAbsValueAndPrev reactions_per_post:StatsAbsValueAndPrev views_per_story:StatsAbsValueAndPrev shares_per_story:StatsAbsValueAndPrev reactions_per_story:StatsAbsValueAndPrev enabled_notifications:StatsPercentValue growth_graph:StatsGraph followers_graph:StatsGraph mute_graph:StatsGraph top_hours_graph:StatsGraph interactions_graph:StatsGraph iv_interactions_graph:StatsGraph views_by_source_graph:StatsGraph new_followers_by_source_graph:StatsGraph languages_graph:StatsGraph reactions_by_emotion_graph:StatsGraph story_interactions_graph:StatsGraph story_reactions_by_emotion_graph:StatsGraph recent_posts_interactions:Vector<PostInteractionCounters> = stats.BroadcastStats
    ```
    """
    def __new__(
        cls,
        period: types.StatsDateRangeDays,
        followers: types.StatsAbsValueAndPrev,
        views_per_post: types.StatsAbsValueAndPrev,
        shares_per_post: types.StatsAbsValueAndPrev,
        reactions_per_post: types.StatsAbsValueAndPrev,
        views_per_story: types.StatsAbsValueAndPrev,
        shares_per_story: types.StatsAbsValueAndPrev,
        reactions_per_story: types.StatsAbsValueAndPrev,
        enabled_notifications: types.StatsPercentValue,
        growth_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        followers_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        mute_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        top_hours_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        interactions_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        iv_interactions_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        views_by_source_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        new_followers_by_source_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        languages_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        reactions_by_emotion_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        story_interactions_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        story_reactions_by_emotion_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        recent_posts_interactions: Sequence[types.PostInteractionCountersMessage | types.PostInteractionCountersStory],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MegagroupStats(TLObject):
    """
    [Read `stats.megagroupStats` docs](https://core.telegram.org/constructor/stats.megagroupStats).

    Generated from the following TL definition:
    ```tl
    stats.megagroupStats#ef7ff916 period:StatsDateRangeDays members:StatsAbsValueAndPrev messages:StatsAbsValueAndPrev viewers:StatsAbsValueAndPrev posters:StatsAbsValueAndPrev growth_graph:StatsGraph members_graph:StatsGraph new_members_by_source_graph:StatsGraph languages_graph:StatsGraph messages_graph:StatsGraph actions_graph:StatsGraph top_hours_graph:StatsGraph weekdays_graph:StatsGraph top_posters:Vector<StatsGroupTopPoster> top_admins:Vector<StatsGroupTopAdmin> top_inviters:Vector<StatsGroupTopInviter> users:Vector<User> = stats.MegagroupStats
    ```
    """
    def __new__(
        cls,
        period: types.StatsDateRangeDays,
        members: types.StatsAbsValueAndPrev,
        messages: types.StatsAbsValueAndPrev,
        viewers: types.StatsAbsValueAndPrev,
        posters: types.StatsAbsValueAndPrev,
        growth_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        members_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        new_members_by_source_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        languages_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        messages_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        actions_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        top_hours_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        weekdays_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        top_posters: Sequence[types.StatsGroupTopPoster],
        top_admins: Sequence[types.StatsGroupTopAdmin],
        top_inviters: Sequence[types.StatsGroupTopInviter],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageStats(TLObject):
    """
    [Read `stats.messageStats` docs](https://core.telegram.org/constructor/stats.messageStats).

    Generated from the following TL definition:
    ```tl
    stats.messageStats#7fe91c14 views_graph:StatsGraph reactions_by_emotion_graph:StatsGraph = stats.MessageStats
    ```
    """
    def __new__(
        cls,
        views_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        reactions_by_emotion_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryStats(TLObject):
    """
    [Read `stats.storyStats` docs](https://core.telegram.org/constructor/stats.storyStats).

    Generated from the following TL definition:
    ```tl
    stats.storyStats#50cd067c views_graph:StatsGraph reactions_by_emotion_graph:StatsGraph = stats.StoryStats
    ```
    """
    def __new__(
        cls,
        views_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        reactions_by_emotion_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PublicForwards(TLObject):
    """
    [Read `stats.publicForwards` docs](https://core.telegram.org/constructor/stats.publicForwards).

    Generated from the following TL definition:
    ```tl
    stats.publicForwards#93037e20 flags:# count:int forwards:Vector<PublicForward> next_offset:flags.0?string chats:Vector<Chat> users:Vector<User> = stats.PublicForwards
    ```
    """
    def __new__(
        cls,
        count: int,
        forwards: Sequence[types.PublicForwardMessage | types.PublicForwardStory],
        next_offset: Optional[str],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

