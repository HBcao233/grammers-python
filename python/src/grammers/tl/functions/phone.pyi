from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class GetCallConfig(TLRequest):
    """
    [Read `phone.getCallConfig` docs](https://core.telegram.org/method/phone.getCallConfig).

    Generated from the following TL definition:
    ```tl
    phone.getCallConfig#55451fa9 = DataJSON
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestCall(TLRequest):
    """
    [Read `phone.requestCall` docs](https://core.telegram.org/method/phone.requestCall).

    Generated from the following TL definition:
    ```tl
    phone.requestCall#42ff96ed flags:# video:flags.0?true user_id:InputUser random_id:int g_a_hash:bytes protocol:PhoneCallProtocol = phone.PhoneCall
    ```
    """
    def __new__(
        cls,
        video: bool,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        random_id: int,
        g_a_hash: bytes,
        protocol: types.PhoneCallProtocol,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AcceptCall(TLRequest):
    """
    [Read `phone.acceptCall` docs](https://core.telegram.org/method/phone.acceptCall).

    Generated from the following TL definition:
    ```tl
    phone.acceptCall#3bd2b4a0 peer:InputPhoneCall g_b:bytes protocol:PhoneCallProtocol = phone.PhoneCall
    ```
    """
    def __new__(
        cls,
        peer: types.InputPhoneCall,
        g_b: bytes,
        protocol: types.PhoneCallProtocol,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ConfirmCall(TLRequest):
    """
    [Read `phone.confirmCall` docs](https://core.telegram.org/method/phone.confirmCall).

    Generated from the following TL definition:
    ```tl
    phone.confirmCall#2efe1722 peer:InputPhoneCall g_a:bytes key_fingerprint:long protocol:PhoneCallProtocol = phone.PhoneCall
    ```
    """
    def __new__(
        cls,
        peer: types.InputPhoneCall,
        g_a: bytes,
        key_fingerprint: int,
        protocol: types.PhoneCallProtocol,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReceivedCall(TLRequest):
    """
    [Read `phone.receivedCall` docs](https://core.telegram.org/method/phone.receivedCall).

    Generated from the following TL definition:
    ```tl
    phone.receivedCall#17d54f61 peer:InputPhoneCall = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPhoneCall,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DiscardCall(TLRequest):
    """
    [Read `phone.discardCall` docs](https://core.telegram.org/method/phone.discardCall).

    Generated from the following TL definition:
    ```tl
    phone.discardCall#b2cbc1c0 flags:# video:flags.0?true peer:InputPhoneCall duration:int reason:PhoneCallDiscardReason connection_id:long = Updates
    ```
    """
    def __new__(
        cls,
        video: bool,
        peer: types.InputPhoneCall,
        duration: int,
        reason: types.PhoneCallDiscardReasonMissed | types.PhoneCallDiscardReasonDisconnect | types.PhoneCallDiscardReasonHangup | types.PhoneCallDiscardReasonBusy | types.PhoneCallDiscardReasonMigrateConferenceCall,
        connection_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetCallRating(TLRequest):
    """
    [Read `phone.setCallRating` docs](https://core.telegram.org/method/phone.setCallRating).

    Generated from the following TL definition:
    ```tl
    phone.setCallRating#59ead627 flags:# user_initiative:flags.0?true peer:InputPhoneCall rating:int comment:string = Updates
    ```
    """
    def __new__(
        cls,
        user_initiative: bool,
        peer: types.InputPhoneCall,
        rating: int,
        comment: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveCallDebug(TLRequest):
    """
    [Read `phone.saveCallDebug` docs](https://core.telegram.org/method/phone.saveCallDebug).

    Generated from the following TL definition:
    ```tl
    phone.saveCallDebug#277add7e peer:InputPhoneCall debug:DataJSON = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPhoneCall,
        debug: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendSignalingData(TLRequest):
    """
    [Read `phone.sendSignalingData` docs](https://core.telegram.org/method/phone.sendSignalingData).

    Generated from the following TL definition:
    ```tl
    phone.sendSignalingData#ff7a9383 peer:InputPhoneCall data:bytes = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPhoneCall,
        data: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CreateGroupCall(TLRequest):
    """
    [Read `phone.createGroupCall` docs](https://core.telegram.org/method/phone.createGroupCall).

    Generated from the following TL definition:
    ```tl
    phone.createGroupCall#48cdc6d8 flags:# rtmp_stream:flags.2?true peer:InputPeer random_id:int title:flags.0?string schedule_date:flags.1?int = Updates
    ```
    """
    def __new__(
        cls,
        rtmp_stream: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        random_id: int,
        title: Optional[str],
        schedule_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JoinGroupCall(TLRequest):
    """
    [Read `phone.joinGroupCall` docs](https://core.telegram.org/method/phone.joinGroupCall).

    Generated from the following TL definition:
    ```tl
    phone.joinGroupCall#8fb53057 flags:# muted:flags.0?true video_stopped:flags.2?true call:InputGroupCall join_as:InputPeer invite_hash:flags.1?string public_key:flags.3?int256 block:flags.3?bytes params:DataJSON = Updates
    ```
    """
    def __new__(
        cls,
        muted: bool,
        video_stopped: bool,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        join_as: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        invite_hash: Optional[str],
        public_key: Optional[int],
        block: Optional[bytes],
        params: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LeaveGroupCall(TLRequest):
    """
    [Read `phone.leaveGroupCall` docs](https://core.telegram.org/method/phone.leaveGroupCall).

    Generated from the following TL definition:
    ```tl
    phone.leaveGroupCall#500377f9 call:InputGroupCall source:int = Updates
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        source: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InviteToGroupCall(TLRequest):
    """
    [Read `phone.inviteToGroupCall` docs](https://core.telegram.org/method/phone.inviteToGroupCall).

    Generated from the following TL definition:
    ```tl
    phone.inviteToGroupCall#7b393160 call:InputGroupCall users:Vector<InputUser> = Updates
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        users: Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DiscardGroupCall(TLRequest):
    """
    [Read `phone.discardGroupCall` docs](https://core.telegram.org/method/phone.discardGroupCall).

    Generated from the following TL definition:
    ```tl
    phone.discardGroupCall#7a777135 call:InputGroupCall = Updates
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleGroupCallSettings(TLRequest):
    """
    [Read `phone.toggleGroupCallSettings` docs](https://core.telegram.org/method/phone.toggleGroupCallSettings).

    Generated from the following TL definition:
    ```tl
    phone.toggleGroupCallSettings#974392f2 flags:# reset_invite_hash:flags.1?true call:InputGroupCall join_muted:flags.0?Bool messages_enabled:flags.2?Bool send_paid_messages_stars:flags.3?long = Updates
    ```
    """
    def __new__(
        cls,
        reset_invite_hash: bool,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        join_muted: Optional[bool],
        messages_enabled: Optional[bool],
        send_paid_messages_stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetGroupCall(TLRequest):
    """
    [Read `phone.getGroupCall` docs](https://core.telegram.org/method/phone.getGroupCall).

    Generated from the following TL definition:
    ```tl
    phone.getGroupCall#41845db call:InputGroupCall limit:int = phone.GroupCall
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetGroupParticipants(TLRequest):
    """
    [Read `phone.getGroupParticipants` docs](https://core.telegram.org/method/phone.getGroupParticipants).

    Generated from the following TL definition:
    ```tl
    phone.getGroupParticipants#c558d8ab call:InputGroupCall ids:Vector<InputPeer> sources:Vector<int> offset:string limit:int = phone.GroupParticipants
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        ids: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        sources: Sequence[int],
        offset: str,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckGroupCall(TLRequest):
    """
    [Read `phone.checkGroupCall` docs](https://core.telegram.org/method/phone.checkGroupCall).

    Generated from the following TL definition:
    ```tl
    phone.checkGroupCall#b59cf977 call:InputGroupCall sources:Vector<int> = Vector<int>
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        sources: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleGroupCallRecord(TLRequest):
    """
    [Read `phone.toggleGroupCallRecord` docs](https://core.telegram.org/method/phone.toggleGroupCallRecord).

    Generated from the following TL definition:
    ```tl
    phone.toggleGroupCallRecord#f128c708 flags:# start:flags.0?true video:flags.2?true call:InputGroupCall title:flags.1?string video_portrait:flags.2?Bool = Updates
    ```
    """
    def __new__(
        cls,
        start: bool,
        video: bool,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        title: Optional[str],
        video_portrait: Optional[bool],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditGroupCallParticipant(TLRequest):
    """
    [Read `phone.editGroupCallParticipant` docs](https://core.telegram.org/method/phone.editGroupCallParticipant).

    Generated from the following TL definition:
    ```tl
    phone.editGroupCallParticipant#a5273abf flags:# call:InputGroupCall participant:InputPeer muted:flags.0?Bool volume:flags.1?int raise_hand:flags.2?Bool video_stopped:flags.3?Bool video_paused:flags.4?Bool presentation_paused:flags.5?Bool = Updates
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        participant: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        muted: Optional[bool],
        volume: Optional[int],
        raise_hand: Optional[bool],
        video_stopped: Optional[bool],
        video_paused: Optional[bool],
        presentation_paused: Optional[bool],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditGroupCallTitle(TLRequest):
    """
    [Read `phone.editGroupCallTitle` docs](https://core.telegram.org/method/phone.editGroupCallTitle).

    Generated from the following TL definition:
    ```tl
    phone.editGroupCallTitle#1ca6ac0a call:InputGroupCall title:string = Updates
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        title: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetGroupCallJoinAs(TLRequest):
    """
    [Read `phone.getGroupCallJoinAs` docs](https://core.telegram.org/method/phone.getGroupCallJoinAs).

    Generated from the following TL definition:
    ```tl
    phone.getGroupCallJoinAs#ef7c213a peer:InputPeer = phone.JoinAsPeers
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportGroupCallInvite(TLRequest):
    """
    [Read `phone.exportGroupCallInvite` docs](https://core.telegram.org/method/phone.exportGroupCallInvite).

    Generated from the following TL definition:
    ```tl
    phone.exportGroupCallInvite#e6aa647f flags:# can_self_unmute:flags.0?true call:InputGroupCall = phone.ExportedGroupCallInvite
    ```
    """
    def __new__(
        cls,
        can_self_unmute: bool,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleGroupCallStartSubscription(TLRequest):
    """
    [Read `phone.toggleGroupCallStartSubscription` docs](https://core.telegram.org/method/phone.toggleGroupCallStartSubscription).

    Generated from the following TL definition:
    ```tl
    phone.toggleGroupCallStartSubscription#219c34e6 call:InputGroupCall subscribed:Bool = Updates
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        subscribed: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StartScheduledGroupCall(TLRequest):
    """
    [Read `phone.startScheduledGroupCall` docs](https://core.telegram.org/method/phone.startScheduledGroupCall).

    Generated from the following TL definition:
    ```tl
    phone.startScheduledGroupCall#5680e342 call:InputGroupCall = Updates
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveDefaultGroupCallJoinAs(TLRequest):
    """
    [Read `phone.saveDefaultGroupCallJoinAs` docs](https://core.telegram.org/method/phone.saveDefaultGroupCallJoinAs).

    Generated from the following TL definition:
    ```tl
    phone.saveDefaultGroupCallJoinAs#575e1f8c peer:InputPeer join_as:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        join_as: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JoinGroupCallPresentation(TLRequest):
    """
    [Read `phone.joinGroupCallPresentation` docs](https://core.telegram.org/method/phone.joinGroupCallPresentation).

    Generated from the following TL definition:
    ```tl
    phone.joinGroupCallPresentation#cbea6bc4 call:InputGroupCall params:DataJSON = Updates
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        params: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LeaveGroupCallPresentation(TLRequest):
    """
    [Read `phone.leaveGroupCallPresentation` docs](https://core.telegram.org/method/phone.leaveGroupCallPresentation).

    Generated from the following TL definition:
    ```tl
    phone.leaveGroupCallPresentation#1c50d144 call:InputGroupCall = Updates
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetGroupCallStreamChannels(TLRequest):
    """
    [Read `phone.getGroupCallStreamChannels` docs](https://core.telegram.org/method/phone.getGroupCallStreamChannels).

    Generated from the following TL definition:
    ```tl
    phone.getGroupCallStreamChannels#1ab21940 call:InputGroupCall = phone.GroupCallStreamChannels
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetGroupCallStreamRtmpUrl(TLRequest):
    """
    [Read `phone.getGroupCallStreamRtmpUrl` docs](https://core.telegram.org/method/phone.getGroupCallStreamRtmpUrl).

    Generated from the following TL definition:
    ```tl
    phone.getGroupCallStreamRtmpUrl#5af4c73a flags:# live_story:flags.0?true peer:InputPeer revoke:Bool = phone.GroupCallStreamRtmpUrl
    ```
    """
    def __new__(
        cls,
        live_story: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        revoke: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveCallLog(TLRequest):
    """
    [Read `phone.saveCallLog` docs](https://core.telegram.org/method/phone.saveCallLog).

    Generated from the following TL definition:
    ```tl
    phone.saveCallLog#41248786 peer:InputPhoneCall file:InputFile = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPhoneCall,
        file: types.InputFile | types.InputFileBig | types.InputFileStoryDocument,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CreateConferenceCall(TLRequest):
    """
    [Read `phone.createConferenceCall` docs](https://core.telegram.org/method/phone.createConferenceCall).

    Generated from the following TL definition:
    ```tl
    phone.createConferenceCall#7d0444bb flags:# muted:flags.0?true video_stopped:flags.2?true join:flags.3?true random_id:int public_key:flags.3?int256 block:flags.3?bytes params:flags.3?DataJSON = Updates
    ```
    """
    def __new__(
        cls,
        muted: bool,
        video_stopped: bool,
        join: bool,
        random_id: int,
        public_key: Optional[int],
        block: Optional[bytes],
        params: Optional[types.DataJson],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteConferenceCallParticipants(TLRequest):
    """
    [Read `phone.deleteConferenceCallParticipants` docs](https://core.telegram.org/method/phone.deleteConferenceCallParticipants).

    Generated from the following TL definition:
    ```tl
    phone.deleteConferenceCallParticipants#8ca60525 flags:# only_left:flags.0?true kick:flags.1?true call:InputGroupCall ids:Vector<long> block:bytes = Updates
    ```
    """
    def __new__(
        cls,
        only_left: bool,
        kick: bool,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        ids: Sequence[int],
        block: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendConferenceCallBroadcast(TLRequest):
    """
    [Read `phone.sendConferenceCallBroadcast` docs](https://core.telegram.org/method/phone.sendConferenceCallBroadcast).

    Generated from the following TL definition:
    ```tl
    phone.sendConferenceCallBroadcast#c6701900 call:InputGroupCall block:bytes = Updates
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        block: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InviteConferenceCallParticipant(TLRequest):
    """
    [Read `phone.inviteConferenceCallParticipant` docs](https://core.telegram.org/method/phone.inviteConferenceCallParticipant).

    Generated from the following TL definition:
    ```tl
    phone.inviteConferenceCallParticipant#bcf22685 flags:# video:flags.0?true call:InputGroupCall user_id:InputUser = Updates
    ```
    """
    def __new__(
        cls,
        video: bool,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeclineConferenceCallInvite(TLRequest):
    """
    [Read `phone.declineConferenceCallInvite` docs](https://core.telegram.org/method/phone.declineConferenceCallInvite).

    Generated from the following TL definition:
    ```tl
    phone.declineConferenceCallInvite#3c479971 msg_id:int = Updates
    ```
    """
    def __new__(
        cls,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetGroupCallChainBlocks(TLRequest):
    """
    [Read `phone.getGroupCallChainBlocks` docs](https://core.telegram.org/method/phone.getGroupCallChainBlocks).

    Generated from the following TL definition:
    ```tl
    phone.getGroupCallChainBlocks#ee9f88a6 call:InputGroupCall sub_chain_id:int offset:int limit:int = Updates
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        sub_chain_id: int,
        offset: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendGroupCallMessage(TLRequest):
    """
    [Read `phone.sendGroupCallMessage` docs](https://core.telegram.org/method/phone.sendGroupCallMessage).

    Generated from the following TL definition:
    ```tl
    phone.sendGroupCallMessage#b1d11410 flags:# call:InputGroupCall random_id:long message:TextWithEntities allow_paid_stars:flags.0?long send_as:flags.1?InputPeer = Updates
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        random_id: int,
        message: types.TextWithEntities,
        allow_paid_stars: Optional[int],
        send_as: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendGroupCallEncryptedMessage(TLRequest):
    """
    [Read `phone.sendGroupCallEncryptedMessage` docs](https://core.telegram.org/method/phone.sendGroupCallEncryptedMessage).

    Generated from the following TL definition:
    ```tl
    phone.sendGroupCallEncryptedMessage#e5afa56d call:InputGroupCall encrypted_message:bytes = Bool
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        encrypted_message: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteGroupCallMessages(TLRequest):
    """
    [Read `phone.deleteGroupCallMessages` docs](https://core.telegram.org/method/phone.deleteGroupCallMessages).

    Generated from the following TL definition:
    ```tl
    phone.deleteGroupCallMessages#f64f54f7 flags:# report_spam:flags.0?true call:InputGroupCall messages:Vector<int> = Updates
    ```
    """
    def __new__(
        cls,
        report_spam: bool,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        messages: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteGroupCallParticipantMessages(TLRequest):
    """
    [Read `phone.deleteGroupCallParticipantMessages` docs](https://core.telegram.org/method/phone.deleteGroupCallParticipantMessages).

    Generated from the following TL definition:
    ```tl
    phone.deleteGroupCallParticipantMessages#1dbfeca0 flags:# report_spam:flags.0?true call:InputGroupCall participant:InputPeer = Updates
    ```
    """
    def __new__(
        cls,
        report_spam: bool,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        participant: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetGroupCallStars(TLRequest):
    """
    [Read `phone.getGroupCallStars` docs](https://core.telegram.org/method/phone.getGroupCallStars).

    Generated from the following TL definition:
    ```tl
    phone.getGroupCallStars#6f636302 call:InputGroupCall = phone.GroupCallStars
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveDefaultSendAs(TLRequest):
    """
    [Read `phone.saveDefaultSendAs` docs](https://core.telegram.org/method/phone.saveDefaultSendAs).

    Generated from the following TL definition:
    ```tl
    phone.saveDefaultSendAs#4167add1 call:InputGroupCall send_as:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        send_as: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

