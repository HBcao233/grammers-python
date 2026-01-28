from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class ChannelParticipants(TLObject):
    """
    [Read `channels.channelParticipants` docs](https://core.telegram.org/constructor/channels.channelParticipants).

    Generated from the following TL definition:
    ```tl
    channels.channelParticipants#9ab0feaf count:int participants:Vector<ChannelParticipant> chats:Vector<Chat> users:Vector<User> = channels.ChannelParticipants
    ```
    """
    def __new__(
        cls,
        count: int,
        participants: Sequence[types.ChannelParticipant | types.ChannelParticipantSelf | types.ChannelParticipantCreator | types.ChannelParticipantAdmin | types.ChannelParticipantBanned | types.ChannelParticipantLeft],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantsNotModified(TLObject):
    """
    [Read `channels.channelParticipantsNotModified` docs](https://core.telegram.org/constructor/channels.channelParticipantsNotModified).

    Generated from the following TL definition:
    ```tl
    channels.channelParticipantsNotModified#f0173fe9 = channels.ChannelParticipants
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipant(TLObject):
    """
    [Read `channels.channelParticipant` docs](https://core.telegram.org/constructor/channels.channelParticipant).

    Generated from the following TL definition:
    ```tl
    channels.channelParticipant#dfb80317 participant:ChannelParticipant chats:Vector<Chat> users:Vector<User> = channels.ChannelParticipant
    ```
    """
    def __new__(
        cls,
        participant: types.ChannelParticipant | types.ChannelParticipantSelf | types.ChannelParticipantCreator | types.ChannelParticipantAdmin | types.ChannelParticipantBanned | types.ChannelParticipantLeft,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AdminLogResults(TLObject):
    """
    [Read `channels.adminLogResults` docs](https://core.telegram.org/constructor/channels.adminLogResults).

    Generated from the following TL definition:
    ```tl
    channels.adminLogResults#ed8af74d events:Vector<ChannelAdminLogEvent> chats:Vector<Chat> users:Vector<User> = channels.AdminLogResults
    ```
    """
    def __new__(
        cls,
        events: Sequence[types.ChannelAdminLogEvent],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendAsPeers(TLObject):
    """
    [Read `channels.sendAsPeers` docs](https://core.telegram.org/constructor/channels.sendAsPeers).

    Generated from the following TL definition:
    ```tl
    channels.sendAsPeers#f496b0c6 peers:Vector<SendAsPeer> chats:Vector<Chat> users:Vector<User> = channels.SendAsPeers
    ```
    """
    def __new__(
        cls,
        peers: Sequence[types.SendAsPeer],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SponsoredMessageReportResultChooseOption(TLObject):
    """
    [Read `channels.sponsoredMessageReportResultChooseOption` docs](https://core.telegram.org/constructor/channels.sponsoredMessageReportResultChooseOption).

    Generated from the following TL definition:
    ```tl
    channels.sponsoredMessageReportResultChooseOption#846f9e42 title:string options:Vector<SponsoredMessageReportOption> = channels.SponsoredMessageReportResult
    ```
    """
    def __new__(
        cls,
        title: str,
        options: Sequence[types.SponsoredMessageReportOption],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SponsoredMessageReportResultAdsHidden(TLObject):
    """
    [Read `channels.sponsoredMessageReportResultAdsHidden` docs](https://core.telegram.org/constructor/channels.sponsoredMessageReportResultAdsHidden).

    Generated from the following TL definition:
    ```tl
    channels.sponsoredMessageReportResultAdsHidden#3e3bcf2f = channels.SponsoredMessageReportResult
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SponsoredMessageReportResultReported(TLObject):
    """
    [Read `channels.sponsoredMessageReportResultReported` docs](https://core.telegram.org/constructor/channels.sponsoredMessageReportResultReported).

    Generated from the following TL definition:
    ```tl
    channels.sponsoredMessageReportResultReported#ad798849 = channels.SponsoredMessageReportResult
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

