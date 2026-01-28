from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class ReadHistory(TLRequest):
    """
    [Read `channels.readHistory` docs](https://core.telegram.org/method/channels.readHistory).

    Generated from the following TL definition:
    ```tl
    channels.readHistory#cc104937 channel:InputChannel max_id:int = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteMessages(TLRequest):
    """
    [Read `channels.deleteMessages` docs](https://core.telegram.org/method/channels.deleteMessages).

    Generated from the following TL definition:
    ```tl
    channels.deleteMessages#84c1fd4e channel:InputChannel id:Vector<int> = messages.AffectedMessages
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportSpam(TLRequest):
    """
    [Read `channels.reportSpam` docs](https://core.telegram.org/method/channels.reportSpam).

    Generated from the following TL definition:
    ```tl
    channels.reportSpam#f44a8315 channel:InputChannel participant:InputPeer id:Vector<int> = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        participant: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMessages(TLRequest):
    """
    [Read `channels.getMessages` docs](https://core.telegram.org/method/channels.getMessages).

    Generated from the following TL definition:
    ```tl
    channels.getMessages#ad8c9a23 channel:InputChannel id:Vector<InputMessage> = messages.Messages
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        id: Sequence[types.InputMessageId | types.InputMessageReplyTo | types.InputMessagePinned | types.InputMessageCallbackQuery],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetParticipants(TLRequest):
    """
    [Read `channels.getParticipants` docs](https://core.telegram.org/method/channels.getParticipants).

    Generated from the following TL definition:
    ```tl
    channels.getParticipants#77ced9d0 channel:InputChannel filter:ChannelParticipantsFilter offset:int limit:int hash:long = channels.ChannelParticipants
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        filter: types.ChannelParticipantsRecent | types.ChannelParticipantsAdmins | types.ChannelParticipantsKicked | types.ChannelParticipantsBots | types.ChannelParticipantsBanned | types.ChannelParticipantsSearch | types.ChannelParticipantsContacts | types.ChannelParticipantsMentions,
        offset: int,
        limit: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetParticipant(TLRequest):
    """
    [Read `channels.getParticipant` docs](https://core.telegram.org/method/channels.getParticipant).

    Generated from the following TL definition:
    ```tl
    channels.getParticipant#a0ab6cc6 channel:InputChannel participant:InputPeer = channels.ChannelParticipant
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        participant: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetChannels(TLRequest):
    """
    [Read `channels.getChannels` docs](https://core.telegram.org/method/channels.getChannels).

    Generated from the following TL definition:
    ```tl
    channels.getChannels#a7f6bbb id:Vector<InputChannel> = messages.Chats
    ```
    """
    def __new__(
        cls,
        id: Sequence[types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetFullChannel(TLRequest):
    """
    [Read `channels.getFullChannel` docs](https://core.telegram.org/method/channels.getFullChannel).

    Generated from the following TL definition:
    ```tl
    channels.getFullChannel#8736a09 channel:InputChannel = messages.ChatFull
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CreateChannel(TLRequest):
    """
    [Read `channels.createChannel` docs](https://core.telegram.org/method/channels.createChannel).

    Generated from the following TL definition:
    ```tl
    channels.createChannel#91006707 flags:# broadcast:flags.0?true megagroup:flags.1?true for_import:flags.3?true forum:flags.5?true title:string about:string geo_point:flags.2?InputGeoPoint address:flags.2?string ttl_period:flags.4?int = Updates
    ```
    """
    def __new__(
        cls,
        broadcast: bool,
        megagroup: bool,
        for_import: bool,
        forum: bool,
        title: str,
        about: str,
        geo_point: Optional[types.InputGeoPointEmpty | types.InputGeoPoint],
        address: Optional[str],
        ttl_period: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditAdmin(TLRequest):
    """
    [Read `channels.editAdmin` docs](https://core.telegram.org/method/channels.editAdmin).

    Generated from the following TL definition:
    ```tl
    channels.editAdmin#d33c8902 channel:InputChannel user_id:InputUser admin_rights:ChatAdminRights rank:string = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        admin_rights: types.ChatAdminRights,
        rank: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditTitle(TLRequest):
    """
    [Read `channels.editTitle` docs](https://core.telegram.org/method/channels.editTitle).

    Generated from the following TL definition:
    ```tl
    channels.editTitle#566decd0 channel:InputChannel title:string = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        title: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditPhoto(TLRequest):
    """
    [Read `channels.editPhoto` docs](https://core.telegram.org/method/channels.editPhoto).

    Generated from the following TL definition:
    ```tl
    channels.editPhoto#f12e57c9 channel:InputChannel photo:InputChatPhoto = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        photo: types.InputChatPhotoEmpty | types.InputChatUploadedPhoto | types.InputChatPhoto,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckUsername(TLRequest):
    """
    [Read `channels.checkUsername` docs](https://core.telegram.org/method/channels.checkUsername).

    Generated from the following TL definition:
    ```tl
    channels.checkUsername#10e6bd2c channel:InputChannel username:string = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        username: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateUsername(TLRequest):
    """
    [Read `channels.updateUsername` docs](https://core.telegram.org/method/channels.updateUsername).

    Generated from the following TL definition:
    ```tl
    channels.updateUsername#3514b3de channel:InputChannel username:string = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        username: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JoinChannel(TLRequest):
    """
    [Read `channels.joinChannel` docs](https://core.telegram.org/method/channels.joinChannel).

    Generated from the following TL definition:
    ```tl
    channels.joinChannel#24b524c5 channel:InputChannel = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LeaveChannel(TLRequest):
    """
    [Read `channels.leaveChannel` docs](https://core.telegram.org/method/channels.leaveChannel).

    Generated from the following TL definition:
    ```tl
    channels.leaveChannel#f836aa95 channel:InputChannel = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InviteToChannel(TLRequest):
    """
    [Read `channels.inviteToChannel` docs](https://core.telegram.org/method/channels.inviteToChannel).

    Generated from the following TL definition:
    ```tl
    channels.inviteToChannel#c9e33d54 channel:InputChannel users:Vector<InputUser> = messages.InvitedUsers
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        users: Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteChannel(TLRequest):
    """
    [Read `channels.deleteChannel` docs](https://core.telegram.org/method/channels.deleteChannel).

    Generated from the following TL definition:
    ```tl
    channels.deleteChannel#c0111fe3 channel:InputChannel = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportMessageLink(TLRequest):
    """
    [Read `channels.exportMessageLink` docs](https://core.telegram.org/method/channels.exportMessageLink).

    Generated from the following TL definition:
    ```tl
    channels.exportMessageLink#e63fadeb flags:# grouped:flags.0?true thread:flags.1?true channel:InputChannel id:int = ExportedMessageLink
    ```
    """
    def __new__(
        cls,
        grouped: bool,
        thread: bool,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleSignatures(TLRequest):
    """
    [Read `channels.toggleSignatures` docs](https://core.telegram.org/method/channels.toggleSignatures).

    Generated from the following TL definition:
    ```tl
    channels.toggleSignatures#418d549c flags:# signatures_enabled:flags.0?true profiles_enabled:flags.1?true channel:InputChannel = Updates
    ```
    """
    def __new__(
        cls,
        signatures_enabled: bool,
        profiles_enabled: bool,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAdminedPublicChannels(TLRequest):
    """
    [Read `channels.getAdminedPublicChannels` docs](https://core.telegram.org/method/channels.getAdminedPublicChannels).

    Generated from the following TL definition:
    ```tl
    channels.getAdminedPublicChannels#f8b036af flags:# by_location:flags.0?true check_limit:flags.1?true for_personal:flags.2?true = messages.Chats
    ```
    """
    def __new__(
        cls,
        by_location: bool,
        check_limit: bool,
        for_personal: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditBanned(TLRequest):
    """
    [Read `channels.editBanned` docs](https://core.telegram.org/method/channels.editBanned).

    Generated from the following TL definition:
    ```tl
    channels.editBanned#96e6cd81 channel:InputChannel participant:InputPeer banned_rights:ChatBannedRights = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        participant: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        banned_rights: types.ChatBannedRights,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAdminLog(TLRequest):
    """
    [Read `channels.getAdminLog` docs](https://core.telegram.org/method/channels.getAdminLog).

    Generated from the following TL definition:
    ```tl
    channels.getAdminLog#33ddf480 flags:# channel:InputChannel q:string events_filter:flags.0?ChannelAdminLogEventsFilter admins:flags.1?Vector<InputUser> max_id:long min_id:long limit:int = channels.AdminLogResults
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        q: str,
        events_filter: Optional[types.ChannelAdminLogEventsFilter],
        admins: Optional[Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage]],
        max_id: int,
        min_id: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetStickers(TLRequest):
    """
    [Read `channels.setStickers` docs](https://core.telegram.org/method/channels.setStickers).

    Generated from the following TL definition:
    ```tl
    channels.setStickers#ea8ca4f9 channel:InputChannel stickerset:InputStickerSet = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReadMessageContents(TLRequest):
    """
    [Read `channels.readMessageContents` docs](https://core.telegram.org/method/channels.readMessageContents).

    Generated from the following TL definition:
    ```tl
    channels.readMessageContents#eab5dc38 channel:InputChannel id:Vector<int> = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteHistory(TLRequest):
    """
    [Read `channels.deleteHistory` docs](https://core.telegram.org/method/channels.deleteHistory).

    Generated from the following TL definition:
    ```tl
    channels.deleteHistory#9baa9647 flags:# for_everyone:flags.0?true channel:InputChannel max_id:int = Updates
    ```
    """
    def __new__(
        cls,
        for_everyone: bool,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TogglePreHistoryHidden(TLRequest):
    """
    [Read `channels.togglePreHistoryHidden` docs](https://core.telegram.org/method/channels.togglePreHistoryHidden).

    Generated from the following TL definition:
    ```tl
    channels.togglePreHistoryHidden#eabbb94c channel:InputChannel enabled:Bool = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetLeftChannels(TLRequest):
    """
    [Read `channels.getLeftChannels` docs](https://core.telegram.org/method/channels.getLeftChannels).

    Generated from the following TL definition:
    ```tl
    channels.getLeftChannels#8341ecc0 offset:int = messages.Chats
    ```
    """
    def __new__(
        cls,
        offset: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetGroupsForDiscussion(TLRequest):
    """
    [Read `channels.getGroupsForDiscussion` docs](https://core.telegram.org/method/channels.getGroupsForDiscussion).

    Generated from the following TL definition:
    ```tl
    channels.getGroupsForDiscussion#f5dad378 = messages.Chats
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetDiscussionGroup(TLRequest):
    """
    [Read `channels.setDiscussionGroup` docs](https://core.telegram.org/method/channels.setDiscussionGroup).

    Generated from the following TL definition:
    ```tl
    channels.setDiscussionGroup#40582bb2 broadcast:InputChannel group:InputChannel = Bool
    ```
    """
    def __new__(
        cls,
        broadcast: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        group: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditCreator(TLRequest):
    """
    [Read `channels.editCreator` docs](https://core.telegram.org/method/channels.editCreator).

    Generated from the following TL definition:
    ```tl
    channels.editCreator#8f38cd1f channel:InputChannel user_id:InputUser password:InputCheckPasswordSRP = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        password: types.InputCheckPasswordEmpty | types.InputCheckPasswordSrp,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditLocation(TLRequest):
    """
    [Read `channels.editLocation` docs](https://core.telegram.org/method/channels.editLocation).

    Generated from the following TL definition:
    ```tl
    channels.editLocation#58e63f6d channel:InputChannel geo_point:InputGeoPoint address:string = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        geo_point: types.InputGeoPointEmpty | types.InputGeoPoint,
        address: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleSlowMode(TLRequest):
    """
    [Read `channels.toggleSlowMode` docs](https://core.telegram.org/method/channels.toggleSlowMode).

    Generated from the following TL definition:
    ```tl
    channels.toggleSlowMode#edd49ef0 channel:InputChannel seconds:int = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        seconds: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetInactiveChannels(TLRequest):
    """
    [Read `channels.getInactiveChannels` docs](https://core.telegram.org/method/channels.getInactiveChannels).

    Generated from the following TL definition:
    ```tl
    channels.getInactiveChannels#11e831ee = messages.InactiveChats
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ConvertToGigagroup(TLRequest):
    """
    [Read `channels.convertToGigagroup` docs](https://core.telegram.org/method/channels.convertToGigagroup).

    Generated from the following TL definition:
    ```tl
    channels.convertToGigagroup#b290c69 channel:InputChannel = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSendAs(TLRequest):
    """
    [Read `channels.getSendAs` docs](https://core.telegram.org/method/channels.getSendAs).

    Generated from the following TL definition:
    ```tl
    channels.getSendAs#e785a43f flags:# for_paid_reactions:flags.0?true for_live_stories:flags.1?true peer:InputPeer = channels.SendAsPeers
    ```
    """
    def __new__(
        cls,
        for_paid_reactions: bool,
        for_live_stories: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteParticipantHistory(TLRequest):
    """
    [Read `channels.deleteParticipantHistory` docs](https://core.telegram.org/method/channels.deleteParticipantHistory).

    Generated from the following TL definition:
    ```tl
    channels.deleteParticipantHistory#367544db channel:InputChannel participant:InputPeer = messages.AffectedHistory
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        participant: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleJoinToSend(TLRequest):
    """
    [Read `channels.toggleJoinToSend` docs](https://core.telegram.org/method/channels.toggleJoinToSend).

    Generated from the following TL definition:
    ```tl
    channels.toggleJoinToSend#e4cb9580 channel:InputChannel enabled:Bool = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleJoinRequest(TLRequest):
    """
    [Read `channels.toggleJoinRequest` docs](https://core.telegram.org/method/channels.toggleJoinRequest).

    Generated from the following TL definition:
    ```tl
    channels.toggleJoinRequest#4c2985b6 channel:InputChannel enabled:Bool = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReorderUsernames(TLRequest):
    """
    [Read `channels.reorderUsernames` docs](https://core.telegram.org/method/channels.reorderUsernames).

    Generated from the following TL definition:
    ```tl
    channels.reorderUsernames#b45ced1d channel:InputChannel order:Vector<string> = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        order: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleUsername(TLRequest):
    """
    [Read `channels.toggleUsername` docs](https://core.telegram.org/method/channels.toggleUsername).

    Generated from the following TL definition:
    ```tl
    channels.toggleUsername#50f24105 channel:InputChannel username:string active:Bool = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        username: str,
        active: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeactivateAllUsernames(TLRequest):
    """
    [Read `channels.deactivateAllUsernames` docs](https://core.telegram.org/method/channels.deactivateAllUsernames).

    Generated from the following TL definition:
    ```tl
    channels.deactivateAllUsernames#a245dd3 channel:InputChannel = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleForum(TLRequest):
    """
    [Read `channels.toggleForum` docs](https://core.telegram.org/method/channels.toggleForum).

    Generated from the following TL definition:
    ```tl
    channels.toggleForum#3ff75734 channel:InputChannel enabled:Bool tabs:Bool = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        enabled: bool,
        tabs: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleAntiSpam(TLRequest):
    """
    [Read `channels.toggleAntiSpam` docs](https://core.telegram.org/method/channels.toggleAntiSpam).

    Generated from the following TL definition:
    ```tl
    channels.toggleAntiSpam#68f3e4eb channel:InputChannel enabled:Bool = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportAntiSpamFalsePositive(TLRequest):
    """
    [Read `channels.reportAntiSpamFalsePositive` docs](https://core.telegram.org/method/channels.reportAntiSpamFalsePositive).

    Generated from the following TL definition:
    ```tl
    channels.reportAntiSpamFalsePositive#a850a693 channel:InputChannel msg_id:int = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleParticipantsHidden(TLRequest):
    """
    [Read `channels.toggleParticipantsHidden` docs](https://core.telegram.org/method/channels.toggleParticipantsHidden).

    Generated from the following TL definition:
    ```tl
    channels.toggleParticipantsHidden#6a6e7854 channel:InputChannel enabled:Bool = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateColor(TLRequest):
    """
    [Read `channels.updateColor` docs](https://core.telegram.org/method/channels.updateColor).

    Generated from the following TL definition:
    ```tl
    channels.updateColor#d8aa3671 flags:# for_profile:flags.1?true channel:InputChannel color:flags.2?int background_emoji_id:flags.0?long = Updates
    ```
    """
    def __new__(
        cls,
        for_profile: bool,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        color: Optional[int],
        background_emoji_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleViewForumAsMessages(TLRequest):
    """
    [Read `channels.toggleViewForumAsMessages` docs](https://core.telegram.org/method/channels.toggleViewForumAsMessages).

    Generated from the following TL definition:
    ```tl
    channels.toggleViewForumAsMessages#9738bb15 channel:InputChannel enabled:Bool = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetChannelRecommendations(TLRequest):
    """
    [Read `channels.getChannelRecommendations` docs](https://core.telegram.org/method/channels.getChannelRecommendations).

    Generated from the following TL definition:
    ```tl
    channels.getChannelRecommendations#25a71742 flags:# channel:flags.0?InputChannel = messages.Chats
    ```
    """
    def __new__(
        cls,
        channel: Optional[types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateEmojiStatus(TLRequest):
    """
    [Read `channels.updateEmojiStatus` docs](https://core.telegram.org/method/channels.updateEmojiStatus).

    Generated from the following TL definition:
    ```tl
    channels.updateEmojiStatus#f0d3e6a8 channel:InputChannel emoji_status:EmojiStatus = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        emoji_status: types.EmojiStatusEmpty | types.EmojiStatus | types.EmojiStatusCollectible | types.InputEmojiStatusCollectible,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetBoostsToUnblockRestrictions(TLRequest):
    """
    [Read `channels.setBoostsToUnblockRestrictions` docs](https://core.telegram.org/method/channels.setBoostsToUnblockRestrictions).

    Generated from the following TL definition:
    ```tl
    channels.setBoostsToUnblockRestrictions#ad399cee channel:InputChannel boosts:int = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        boosts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetEmojiStickers(TLRequest):
    """
    [Read `channels.setEmojiStickers` docs](https://core.telegram.org/method/channels.setEmojiStickers).

    Generated from the following TL definition:
    ```tl
    channels.setEmojiStickers#3cd930b7 channel:InputChannel stickerset:InputStickerSet = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RestrictSponsoredMessages(TLRequest):
    """
    [Read `channels.restrictSponsoredMessages` docs](https://core.telegram.org/method/channels.restrictSponsoredMessages).

    Generated from the following TL definition:
    ```tl
    channels.restrictSponsoredMessages#9ae91519 channel:InputChannel restricted:Bool = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        restricted: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchPosts(TLRequest):
    """
    [Read `channels.searchPosts` docs](https://core.telegram.org/method/channels.searchPosts).

    Generated from the following TL definition:
    ```tl
    channels.searchPosts#f2c4f24d flags:# hashtag:flags.0?string query:flags.1?string offset_rate:int offset_peer:InputPeer offset_id:int limit:int allow_paid_stars:flags.2?long = messages.Messages
    ```
    """
    def __new__(
        cls,
        hashtag: Optional[str],
        query: Optional[str],
        offset_rate: int,
        offset_peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        offset_id: int,
        limit: int,
        allow_paid_stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePaidMessagesPrice(TLRequest):
    """
    [Read `channels.updatePaidMessagesPrice` docs](https://core.telegram.org/method/channels.updatePaidMessagesPrice).

    Generated from the following TL definition:
    ```tl
    channels.updatePaidMessagesPrice#4b12327b flags:# broadcast_messages_allowed:flags.0?true channel:InputChannel send_paid_messages_stars:long = Updates
    ```
    """
    def __new__(
        cls,
        broadcast_messages_allowed: bool,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        send_paid_messages_stars: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleAutotranslation(TLRequest):
    """
    [Read `channels.toggleAutotranslation` docs](https://core.telegram.org/method/channels.toggleAutotranslation).

    Generated from the following TL definition:
    ```tl
    channels.toggleAutotranslation#167fc0a1 channel:InputChannel enabled:Bool = Updates
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetMessageAuthor(TLRequest):
    """
    [Read `channels.getMessageAuthor` docs](https://core.telegram.org/method/channels.getMessageAuthor).

    Generated from the following TL definition:
    ```tl
    channels.getMessageAuthor#ece2a0e6 channel:InputChannel id:int = User
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckSearchPostsFlood(TLRequest):
    """
    [Read `channels.checkSearchPostsFlood` docs](https://core.telegram.org/method/channels.checkSearchPostsFlood).

    Generated from the following TL definition:
    ```tl
    channels.checkSearchPostsFlood#22567115 flags:# query:flags.0?string = SearchPostsFlood
    ```
    """
    def __new__(
        cls,
        query: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetMainProfileTab(TLRequest):
    """
    [Read `channels.setMainProfileTab` docs](https://core.telegram.org/method/channels.setMainProfileTab).

    Generated from the following TL definition:
    ```tl
    channels.setMainProfileTab#3583fcb1 channel:InputChannel tab:ProfileTab = Bool
    ```
    """
    def __new__(
        cls,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        tab: types.ProfileTabPosts | types.ProfileTabGifts | types.ProfileTabMedia | types.ProfileTabFiles | types.ProfileTabMusic | types.ProfileTabVoice | types.ProfileTabLinks | types.ProfileTabGifs,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

