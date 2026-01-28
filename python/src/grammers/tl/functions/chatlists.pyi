from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class ExportChatlistInvite(TLRequest):
    """
    [Read `chatlists.exportChatlistInvite` docs](https://core.telegram.org/method/chatlists.exportChatlistInvite).

    Generated from the following TL definition:
    ```tl
    chatlists.exportChatlistInvite#8472478e chatlist:InputChatlist title:string peers:Vector<InputPeer> = chatlists.ExportedChatlistInvite
    ```
    """
    def __new__(
        cls,
        chatlist: types.InputChatlistDialogFilter,
        title: str,
        peers: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteExportedInvite(TLRequest):
    """
    [Read `chatlists.deleteExportedInvite` docs](https://core.telegram.org/method/chatlists.deleteExportedInvite).

    Generated from the following TL definition:
    ```tl
    chatlists.deleteExportedInvite#719c5c5e chatlist:InputChatlist slug:string = Bool
    ```
    """
    def __new__(
        cls,
        chatlist: types.InputChatlistDialogFilter,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditExportedInvite(TLRequest):
    """
    [Read `chatlists.editExportedInvite` docs](https://core.telegram.org/method/chatlists.editExportedInvite).

    Generated from the following TL definition:
    ```tl
    chatlists.editExportedInvite#653db63d flags:# chatlist:InputChatlist slug:string title:flags.1?string peers:flags.2?Vector<InputPeer> = ExportedChatlistInvite
    ```
    """
    def __new__(
        cls,
        chatlist: types.InputChatlistDialogFilter,
        slug: str,
        title: Optional[str],
        peers: Optional[Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetExportedInvites(TLRequest):
    """
    [Read `chatlists.getExportedInvites` docs](https://core.telegram.org/method/chatlists.getExportedInvites).

    Generated from the following TL definition:
    ```tl
    chatlists.getExportedInvites#ce03da83 chatlist:InputChatlist = chatlists.ExportedInvites
    ```
    """
    def __new__(
        cls,
        chatlist: types.InputChatlistDialogFilter,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckChatlistInvite(TLRequest):
    """
    [Read `chatlists.checkChatlistInvite` docs](https://core.telegram.org/method/chatlists.checkChatlistInvite).

    Generated from the following TL definition:
    ```tl
    chatlists.checkChatlistInvite#41c10fff slug:string = chatlists.ChatlistInvite
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JoinChatlistInvite(TLRequest):
    """
    [Read `chatlists.joinChatlistInvite` docs](https://core.telegram.org/method/chatlists.joinChatlistInvite).

    Generated from the following TL definition:
    ```tl
    chatlists.joinChatlistInvite#a6b1e39a slug:string peers:Vector<InputPeer> = Updates
    ```
    """
    def __new__(
        cls,
        slug: str,
        peers: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetChatlistUpdates(TLRequest):
    """
    [Read `chatlists.getChatlistUpdates` docs](https://core.telegram.org/method/chatlists.getChatlistUpdates).

    Generated from the following TL definition:
    ```tl
    chatlists.getChatlistUpdates#89419521 chatlist:InputChatlist = chatlists.ChatlistUpdates
    ```
    """
    def __new__(
        cls,
        chatlist: types.InputChatlistDialogFilter,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JoinChatlistUpdates(TLRequest):
    """
    [Read `chatlists.joinChatlistUpdates` docs](https://core.telegram.org/method/chatlists.joinChatlistUpdates).

    Generated from the following TL definition:
    ```tl
    chatlists.joinChatlistUpdates#e089f8f5 chatlist:InputChatlist peers:Vector<InputPeer> = Updates
    ```
    """
    def __new__(
        cls,
        chatlist: types.InputChatlistDialogFilter,
        peers: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class HideChatlistUpdates(TLRequest):
    """
    [Read `chatlists.hideChatlistUpdates` docs](https://core.telegram.org/method/chatlists.hideChatlistUpdates).

    Generated from the following TL definition:
    ```tl
    chatlists.hideChatlistUpdates#66e486fb chatlist:InputChatlist = Bool
    ```
    """
    def __new__(
        cls,
        chatlist: types.InputChatlistDialogFilter,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetLeaveChatlistSuggestions(TLRequest):
    """
    [Read `chatlists.getLeaveChatlistSuggestions` docs](https://core.telegram.org/method/chatlists.getLeaveChatlistSuggestions).

    Generated from the following TL definition:
    ```tl
    chatlists.getLeaveChatlistSuggestions#fdbcd714 chatlist:InputChatlist = Vector<Peer>
    ```
    """
    def __new__(
        cls,
        chatlist: types.InputChatlistDialogFilter,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LeaveChatlist(TLRequest):
    """
    [Read `chatlists.leaveChatlist` docs](https://core.telegram.org/method/chatlists.leaveChatlist).

    Generated from the following TL definition:
    ```tl
    chatlists.leaveChatlist#74fae13a chatlist:InputChatlist peers:Vector<InputPeer> = Updates
    ```
    """
    def __new__(
        cls,
        chatlist: types.InputChatlistDialogFilter,
        peers: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

