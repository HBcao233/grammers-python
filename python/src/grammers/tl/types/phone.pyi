from typing import final, Self, Sequence
from grammers.tl import TLObject, types

@final
class PhoneCall(TLObject):
    """
    [Read `phone.phoneCall` docs](https://core.telegram.org/constructor/phone.phoneCall).

    Generated from the following TL definition:
    ```tl
    phone.phoneCall#ec82e140 phone_call:PhoneCall users:Vector<User> = phone.PhoneCall
    ```
    """
    def __new__(
        cls,
        phone_call: types.PhoneCallEmpty | types.PhoneCallWaiting | types.PhoneCallRequested | types.PhoneCallAccepted | types.PhoneCall | types.PhoneCallDiscarded,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupCall(TLObject):
    """
    [Read `phone.groupCall` docs](https://core.telegram.org/constructor/phone.groupCall).

    Generated from the following TL definition:
    ```tl
    phone.groupCall#9e727aad call:GroupCall participants:Vector<GroupCallParticipant> participants_next_offset:string chats:Vector<Chat> users:Vector<User> = phone.GroupCall
    ```
    """
    def __new__(
        cls,
        call: types.GroupCallDiscarded | types.GroupCall,
        participants: Sequence[types.GroupCallParticipant],
        participants_next_offset: str,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupParticipants(TLObject):
    """
    [Read `phone.groupParticipants` docs](https://core.telegram.org/constructor/phone.groupParticipants).

    Generated from the following TL definition:
    ```tl
    phone.groupParticipants#f47751b6 count:int participants:Vector<GroupCallParticipant> next_offset:string chats:Vector<Chat> users:Vector<User> version:int = phone.GroupParticipants
    ```
    """
    def __new__(
        cls,
        count: int,
        participants: Sequence[types.GroupCallParticipant],
        next_offset: str,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
        version: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JoinAsPeers(TLObject):
    """
    [Read `phone.joinAsPeers` docs](https://core.telegram.org/constructor/phone.joinAsPeers).

    Generated from the following TL definition:
    ```tl
    phone.joinAsPeers#afe5623f peers:Vector<Peer> chats:Vector<Chat> users:Vector<User> = phone.JoinAsPeers
    ```
    """
    def __new__(
        cls,
        peers: Sequence[types.PeerUser | types.PeerChat | types.PeerChannel],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportedGroupCallInvite(TLObject):
    """
    [Read `phone.exportedGroupCallInvite` docs](https://core.telegram.org/constructor/phone.exportedGroupCallInvite).

    Generated from the following TL definition:
    ```tl
    phone.exportedGroupCallInvite#204bd158 link:string = phone.ExportedGroupCallInvite
    ```
    """
    def __new__(
        cls,
        link: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupCallStreamChannels(TLObject):
    """
    [Read `phone.groupCallStreamChannels` docs](https://core.telegram.org/constructor/phone.groupCallStreamChannels).

    Generated from the following TL definition:
    ```tl
    phone.groupCallStreamChannels#d0e482b2 channels:Vector<GroupCallStreamChannel> = phone.GroupCallStreamChannels
    ```
    """
    def __new__(
        cls,
        channels: Sequence[types.GroupCallStreamChannel],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupCallStreamRtmpUrl(TLObject):
    """
    [Read `phone.groupCallStreamRtmpUrl` docs](https://core.telegram.org/constructor/phone.groupCallStreamRtmpUrl).

    Generated from the following TL definition:
    ```tl
    phone.groupCallStreamRtmpUrl#2dbf3432 url:string key:string = phone.GroupCallStreamRtmpUrl
    ```
    """
    def __new__(
        cls,
        url: str,
        key: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupCallStars(TLObject):
    """
    [Read `phone.groupCallStars` docs](https://core.telegram.org/constructor/phone.groupCallStars).

    Generated from the following TL definition:
    ```tl
    phone.groupCallStars#9d1dbd26 total_stars:long top_donors:Vector<GroupCallDonor> chats:Vector<Chat> users:Vector<User> = phone.GroupCallStars
    ```
    """
    def __new__(
        cls,
        total_stars: int,
        top_donors: Sequence[types.GroupCallDonor],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

