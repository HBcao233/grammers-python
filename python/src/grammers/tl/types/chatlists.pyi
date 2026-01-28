from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class ExportedChatlistInvite(TLObject):
    """
    [Read `chatlists.exportedChatlistInvite` docs](https://core.telegram.org/constructor/chatlists.exportedChatlistInvite).

    Generated from the following TL definition:
    ```tl
    chatlists.exportedChatlistInvite#10e6e3a6 filter:DialogFilter invite:ExportedChatlistInvite = chatlists.ExportedChatlistInvite
    ```
    """
    def __new__(
        cls,
        filter: types.DialogFilter | types.DialogFilterDefault | types.DialogFilterChatlist,
        invite: types.ExportedChatlistInvite,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportedInvites(TLObject):
    """
    [Read `chatlists.exportedInvites` docs](https://core.telegram.org/constructor/chatlists.exportedInvites).

    Generated from the following TL definition:
    ```tl
    chatlists.exportedInvites#10ab6dc7 invites:Vector<ExportedChatlistInvite> chats:Vector<Chat> users:Vector<User> = chatlists.ExportedInvites
    ```
    """
    def __new__(
        cls,
        invites: Sequence[types.ExportedChatlistInvite],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatlistInviteAlready(TLObject):
    """
    [Read `chatlists.chatlistInviteAlready` docs](https://core.telegram.org/constructor/chatlists.chatlistInviteAlready).

    Generated from the following TL definition:
    ```tl
    chatlists.chatlistInviteAlready#fa87f659 filter_id:int missing_peers:Vector<Peer> already_peers:Vector<Peer> chats:Vector<Chat> users:Vector<User> = chatlists.ChatlistInvite
    ```
    """
    def __new__(
        cls,
        filter_id: int,
        missing_peers: Sequence[types.PeerUser | types.PeerChat | types.PeerChannel],
        already_peers: Sequence[types.PeerUser | types.PeerChat | types.PeerChannel],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatlistInvite(TLObject):
    """
    [Read `chatlists.chatlistInvite` docs](https://core.telegram.org/constructor/chatlists.chatlistInvite).

    Generated from the following TL definition:
    ```tl
    chatlists.chatlistInvite#f10ece2f flags:# title_noanimate:flags.1?true title:TextWithEntities emoticon:flags.0?string peers:Vector<Peer> chats:Vector<Chat> users:Vector<User> = chatlists.ChatlistInvite
    ```
    """
    def __new__(
        cls,
        title_noanimate: bool,
        title: types.TextWithEntities,
        emoticon: Optional[str],
        peers: Sequence[types.PeerUser | types.PeerChat | types.PeerChannel],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatlistUpdates(TLObject):
    """
    [Read `chatlists.chatlistUpdates` docs](https://core.telegram.org/constructor/chatlists.chatlistUpdates).

    Generated from the following TL definition:
    ```tl
    chatlists.chatlistUpdates#93bd878d missing_peers:Vector<Peer> chats:Vector<Chat> users:Vector<User> = chatlists.ChatlistUpdates
    ```
    """
    def __new__(
        cls,
        missing_peers: Sequence[types.PeerUser | types.PeerChat | types.PeerChannel],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

