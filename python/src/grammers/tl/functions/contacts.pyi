from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class GetContactIds(TLRequest):
    """
    [Read `contacts.getContactIDs` docs](https://core.telegram.org/method/contacts.getContactIDs).

    Generated from the following TL definition:
    ```tl
    contacts.getContactIDs#7adc669d hash:long = Vector<int>
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStatuses(TLRequest):
    """
    [Read `contacts.getStatuses` docs](https://core.telegram.org/method/contacts.getStatuses).

    Generated from the following TL definition:
    ```tl
    contacts.getStatuses#c4a353ee = Vector<ContactStatus>
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetContacts(TLRequest):
    """
    [Read `contacts.getContacts` docs](https://core.telegram.org/method/contacts.getContacts).

    Generated from the following TL definition:
    ```tl
    contacts.getContacts#5dd69e12 hash:long = contacts.Contacts
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ImportContacts(TLRequest):
    """
    [Read `contacts.importContacts` docs](https://core.telegram.org/method/contacts.importContacts).

    Generated from the following TL definition:
    ```tl
    contacts.importContacts#2c800be5 contacts:Vector<InputContact> = contacts.ImportedContacts
    ```
    """
    def __new__(
        cls,
        contacts: Sequence[types.InputPhoneContact],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteContacts(TLRequest):
    """
    [Read `contacts.deleteContacts` docs](https://core.telegram.org/method/contacts.deleteContacts).

    Generated from the following TL definition:
    ```tl
    contacts.deleteContacts#96a0e00 id:Vector<InputUser> = Updates
    ```
    """
    def __new__(
        cls,
        id: Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteByPhones(TLRequest):
    """
    [Read `contacts.deleteByPhones` docs](https://core.telegram.org/method/contacts.deleteByPhones).

    Generated from the following TL definition:
    ```tl
    contacts.deleteByPhones#1013fd9e phones:Vector<string> = Bool
    ```
    """
    def __new__(
        cls,
        phones: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Block(TLRequest):
    """
    [Read `contacts.block` docs](https://core.telegram.org/method/contacts.block).

    Generated from the following TL definition:
    ```tl
    contacts.block#2e2e8734 flags:# my_stories_from:flags.0?true id:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        my_stories_from: bool,
        id: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Unblock(TLRequest):
    """
    [Read `contacts.unblock` docs](https://core.telegram.org/method/contacts.unblock).

    Generated from the following TL definition:
    ```tl
    contacts.unblock#b550d328 flags:# my_stories_from:flags.0?true id:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        my_stories_from: bool,
        id: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetBlocked(TLRequest):
    """
    [Read `contacts.getBlocked` docs](https://core.telegram.org/method/contacts.getBlocked).

    Generated from the following TL definition:
    ```tl
    contacts.getBlocked#9a868f80 flags:# my_stories_from:flags.0?true offset:int limit:int = contacts.Blocked
    ```
    """
    def __new__(
        cls,
        my_stories_from: bool,
        offset: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Search(TLRequest):
    """
    [Read `contacts.search` docs](https://core.telegram.org/method/contacts.search).

    Generated from the following TL definition:
    ```tl
    contacts.search#11f812d8 q:string limit:int = contacts.Found
    ```
    """
    def __new__(
        cls,
        q: str,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResolveUsername(TLRequest):
    """
    [Read `contacts.resolveUsername` docs](https://core.telegram.org/method/contacts.resolveUsername).

    Generated from the following TL definition:
    ```tl
    contacts.resolveUsername#725afbbc flags:# username:string referer:flags.0?string = contacts.ResolvedPeer
    ```
    """
    def __new__(
        cls,
        username: str,
        referer: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetTopPeers(TLRequest):
    """
    [Read `contacts.getTopPeers` docs](https://core.telegram.org/method/contacts.getTopPeers).

    Generated from the following TL definition:
    ```tl
    contacts.getTopPeers#973478b6 flags:# correspondents:flags.0?true bots_pm:flags.1?true bots_inline:flags.2?true phone_calls:flags.3?true forward_users:flags.4?true forward_chats:flags.5?true groups:flags.10?true channels:flags.15?true bots_app:flags.16?true offset:int limit:int hash:long = contacts.TopPeers
    ```
    """
    def __new__(
        cls,
        correspondents: bool,
        bots_pm: bool,
        bots_inline: bool,
        phone_calls: bool,
        forward_users: bool,
        forward_chats: bool,
        groups: bool,
        channels: bool,
        bots_app: bool,
        offset: int,
        limit: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetTopPeerRating(TLRequest):
    """
    [Read `contacts.resetTopPeerRating` docs](https://core.telegram.org/method/contacts.resetTopPeerRating).

    Generated from the following TL definition:
    ```tl
    contacts.resetTopPeerRating#1ae373ac category:TopPeerCategory peer:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        category: types.TopPeerCategoryBotsPm | types.TopPeerCategoryBotsInline | types.TopPeerCategoryCorrespondents | types.TopPeerCategoryGroups | types.TopPeerCategoryChannels | types.TopPeerCategoryPhoneCalls | types.TopPeerCategoryForwardUsers | types.TopPeerCategoryForwardChats | types.TopPeerCategoryBotsApp,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetSaved(TLRequest):
    """
    [Read `contacts.resetSaved` docs](https://core.telegram.org/method/contacts.resetSaved).

    Generated from the following TL definition:
    ```tl
    contacts.resetSaved#879537f1 = Bool
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSaved(TLRequest):
    """
    [Read `contacts.getSaved` docs](https://core.telegram.org/method/contacts.getSaved).

    Generated from the following TL definition:
    ```tl
    contacts.getSaved#82f1e39f = Vector<SavedContact>
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleTopPeers(TLRequest):
    """
    [Read `contacts.toggleTopPeers` docs](https://core.telegram.org/method/contacts.toggleTopPeers).

    Generated from the following TL definition:
    ```tl
    contacts.toggleTopPeers#8514bdda enabled:Bool = Bool
    ```
    """
    def __new__(
        cls,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AddContact(TLRequest):
    """
    [Read `contacts.addContact` docs](https://core.telegram.org/method/contacts.addContact).

    Generated from the following TL definition:
    ```tl
    contacts.addContact#d9ba2e54 flags:# add_phone_privacy_exception:flags.0?true id:InputUser first_name:string last_name:string phone:string note:flags.1?TextWithEntities = Updates
    ```
    """
    def __new__(
        cls,
        add_phone_privacy_exception: bool,
        id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        first_name: str,
        last_name: str,
        phone: str,
        note: Optional[types.TextWithEntities],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AcceptContact(TLRequest):
    """
    [Read `contacts.acceptContact` docs](https://core.telegram.org/method/contacts.acceptContact).

    Generated from the following TL definition:
    ```tl
    contacts.acceptContact#f831a20f id:InputUser = Updates
    ```
    """
    def __new__(
        cls,
        id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetLocated(TLRequest):
    """
    [Read `contacts.getLocated` docs](https://core.telegram.org/method/contacts.getLocated).

    Generated from the following TL definition:
    ```tl
    contacts.getLocated#d348bc44 flags:# background:flags.1?true geo_point:InputGeoPoint self_expires:flags.0?int = Updates
    ```
    """
    def __new__(
        cls,
        background: bool,
        geo_point: types.InputGeoPointEmpty | types.InputGeoPoint,
        self_expires: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BlockFromReplies(TLRequest):
    """
    [Read `contacts.blockFromReplies` docs](https://core.telegram.org/method/contacts.blockFromReplies).

    Generated from the following TL definition:
    ```tl
    contacts.blockFromReplies#29a8962c flags:# delete_message:flags.0?true delete_history:flags.1?true report_spam:flags.2?true msg_id:int = Updates
    ```
    """
    def __new__(
        cls,
        delete_message: bool,
        delete_history: bool,
        report_spam: bool,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResolvePhone(TLRequest):
    """
    [Read `contacts.resolvePhone` docs](https://core.telegram.org/method/contacts.resolvePhone).

    Generated from the following TL definition:
    ```tl
    contacts.resolvePhone#8af94344 phone:string = contacts.ResolvedPeer
    ```
    """
    def __new__(
        cls,
        phone: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportContactToken(TLRequest):
    """
    [Read `contacts.exportContactToken` docs](https://core.telegram.org/method/contacts.exportContactToken).

    Generated from the following TL definition:
    ```tl
    contacts.exportContactToken#f8654027 = ExportedContactToken
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ImportContactToken(TLRequest):
    """
    [Read `contacts.importContactToken` docs](https://core.telegram.org/method/contacts.importContactToken).

    Generated from the following TL definition:
    ```tl
    contacts.importContactToken#13005788 token:string = User
    ```
    """
    def __new__(
        cls,
        token: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditCloseFriends(TLRequest):
    """
    [Read `contacts.editCloseFriends` docs](https://core.telegram.org/method/contacts.editCloseFriends).

    Generated from the following TL definition:
    ```tl
    contacts.editCloseFriends#ba6705f0 id:Vector<long> = Bool
    ```
    """
    def __new__(
        cls,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetBlocked(TLRequest):
    """
    [Read `contacts.setBlocked` docs](https://core.telegram.org/method/contacts.setBlocked).

    Generated from the following TL definition:
    ```tl
    contacts.setBlocked#94c65c76 flags:# my_stories_from:flags.0?true id:Vector<InputPeer> limit:int = Bool
    ```
    """
    def __new__(
        cls,
        my_stories_from: bool,
        id: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetBirthdays(TLRequest):
    """
    [Read `contacts.getBirthdays` docs](https://core.telegram.org/method/contacts.getBirthdays).

    Generated from the following TL definition:
    ```tl
    contacts.getBirthdays#daeda864 = contacts.ContactBirthdays
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSponsoredPeers(TLRequest):
    """
    [Read `contacts.getSponsoredPeers` docs](https://core.telegram.org/method/contacts.getSponsoredPeers).

    Generated from the following TL definition:
    ```tl
    contacts.getSponsoredPeers#b6c8c393 q:string = contacts.SponsoredPeers
    ```
    """
    def __new__(
        cls,
        q: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateContactNote(TLRequest):
    """
    [Read `contacts.updateContactNote` docs](https://core.telegram.org/method/contacts.updateContactNote).

    Generated from the following TL definition:
    ```tl
    contacts.updateContactNote#139f63fb id:InputUser note:TextWithEntities = Bool
    ```
    """
    def __new__(
        cls,
        id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        note: types.TextWithEntities,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

