from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class ContactsNotModified(TLObject):
    """
    [Read `contacts.contactsNotModified` docs](https://core.telegram.org/constructor/contacts.contactsNotModified).

    Generated from the following TL definition:
    ```tl
    contacts.contactsNotModified#b74ba9d2 = contacts.Contacts
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Contacts(TLObject):
    """
    [Read `contacts.contacts` docs](https://core.telegram.org/constructor/contacts.contacts).

    Generated from the following TL definition:
    ```tl
    contacts.contacts#eae87e42 contacts:Vector<Contact> saved_count:int users:Vector<User> = contacts.Contacts
    ```
    """
    def __new__(
        cls,
        contacts: Sequence[types.Contact],
        saved_count: int,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ImportedContacts(TLObject):
    """
    [Read `contacts.importedContacts` docs](https://core.telegram.org/constructor/contacts.importedContacts).

    Generated from the following TL definition:
    ```tl
    contacts.importedContacts#77d01c3b imported:Vector<ImportedContact> popular_invites:Vector<PopularContact> retry_contacts:Vector<long> users:Vector<User> = contacts.ImportedContacts
    ```
    """
    def __new__(
        cls,
        imported: Sequence[types.ImportedContact],
        popular_invites: Sequence[types.PopularContact],
        retry_contacts: Sequence[int],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Blocked(TLObject):
    """
    [Read `contacts.blocked` docs](https://core.telegram.org/constructor/contacts.blocked).

    Generated from the following TL definition:
    ```tl
    contacts.blocked#ade1591 blocked:Vector<PeerBlocked> chats:Vector<Chat> users:Vector<User> = contacts.Blocked
    ```
    """
    def __new__(
        cls,
        blocked: Sequence[types.PeerBlocked],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BlockedSlice(TLObject):
    """
    [Read `contacts.blockedSlice` docs](https://core.telegram.org/constructor/contacts.blockedSlice).

    Generated from the following TL definition:
    ```tl
    contacts.blockedSlice#e1664194 count:int blocked:Vector<PeerBlocked> chats:Vector<Chat> users:Vector<User> = contacts.Blocked
    ```
    """
    def __new__(
        cls,
        count: int,
        blocked: Sequence[types.PeerBlocked],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Found(TLObject):
    """
    [Read `contacts.found` docs](https://core.telegram.org/constructor/contacts.found).

    Generated from the following TL definition:
    ```tl
    contacts.found#b3134d9d my_results:Vector<Peer> results:Vector<Peer> chats:Vector<Chat> users:Vector<User> = contacts.Found
    ```
    """
    def __new__(
        cls,
        my_results: Sequence[types.PeerUser | types.PeerChat | types.PeerChannel],
        results: Sequence[types.PeerUser | types.PeerChat | types.PeerChannel],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResolvedPeer(TLObject):
    """
    [Read `contacts.resolvedPeer` docs](https://core.telegram.org/constructor/contacts.resolvedPeer).

    Generated from the following TL definition:
    ```tl
    contacts.resolvedPeer#7f077ad9 peer:Peer chats:Vector<Chat> users:Vector<User> = contacts.ResolvedPeer
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeersNotModified(TLObject):
    """
    [Read `contacts.topPeersNotModified` docs](https://core.telegram.org/constructor/contacts.topPeersNotModified).

    Generated from the following TL definition:
    ```tl
    contacts.topPeersNotModified#de266ef5 = contacts.TopPeers
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeers(TLObject):
    """
    [Read `contacts.topPeers` docs](https://core.telegram.org/constructor/contacts.topPeers).

    Generated from the following TL definition:
    ```tl
    contacts.topPeers#70b772a8 categories:Vector<TopPeerCategoryPeers> chats:Vector<Chat> users:Vector<User> = contacts.TopPeers
    ```
    """
    def __new__(
        cls,
        categories: Sequence[types.TopPeerCategoryPeers],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeersDisabled(TLObject):
    """
    [Read `contacts.topPeersDisabled` docs](https://core.telegram.org/constructor/contacts.topPeersDisabled).

    Generated from the following TL definition:
    ```tl
    contacts.topPeersDisabled#b52c939d = contacts.TopPeers
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ContactBirthdays(TLObject):
    """
    [Read `contacts.contactBirthdays` docs](https://core.telegram.org/constructor/contacts.contactBirthdays).

    Generated from the following TL definition:
    ```tl
    contacts.contactBirthdays#114ff30d contacts:Vector<ContactBirthday> users:Vector<User> = contacts.ContactBirthdays
    ```
    """
    def __new__(
        cls,
        contacts: Sequence[types.ContactBirthday],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SponsoredPeersEmpty(TLObject):
    """
    [Read `contacts.sponsoredPeersEmpty` docs](https://core.telegram.org/constructor/contacts.sponsoredPeersEmpty).

    Generated from the following TL definition:
    ```tl
    contacts.sponsoredPeersEmpty#ea32b4b1 = contacts.SponsoredPeers
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SponsoredPeers(TLObject):
    """
    [Read `contacts.sponsoredPeers` docs](https://core.telegram.org/constructor/contacts.sponsoredPeers).

    Generated from the following TL definition:
    ```tl
    contacts.sponsoredPeers#eb032884 peers:Vector<SponsoredPeer> chats:Vector<Chat> users:Vector<User> = contacts.SponsoredPeers
    ```
    """
    def __new__(
        cls,
        peers: Sequence[types.SponsoredPeer],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

