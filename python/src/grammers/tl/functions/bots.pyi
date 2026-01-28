from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class SendCustomRequest(TLRequest):
    """
    [Read `bots.sendCustomRequest` docs](https://core.telegram.org/method/bots.sendCustomRequest).

    Generated from the following TL definition:
    ```tl
    bots.sendCustomRequest#aa2769ed custom_method:string params:DataJSON = DataJSON
    ```
    """
    def __new__(
        cls,
        custom_method: str,
        params: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AnswerWebhookJsonquery(TLRequest):
    """
    [Read `bots.answerWebhookJSONQuery` docs](https://core.telegram.org/method/bots.answerWebhookJSONQuery).

    Generated from the following TL definition:
    ```tl
    bots.answerWebhookJSONQuery#e6213f4d query_id:long data:DataJSON = Bool
    ```
    """
    def __new__(
        cls,
        query_id: int,
        data: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetBotCommands(TLRequest):
    """
    [Read `bots.setBotCommands` docs](https://core.telegram.org/method/bots.setBotCommands).

    Generated from the following TL definition:
    ```tl
    bots.setBotCommands#517165a scope:BotCommandScope lang_code:string commands:Vector<BotCommand> = Bool
    ```
    """
    def __new__(
        cls,
        scope: types.BotCommandScopeDefault | types.BotCommandScopeUsers | types.BotCommandScopeChats | types.BotCommandScopeChatAdmins | types.BotCommandScopePeer | types.BotCommandScopePeerAdmins | types.BotCommandScopePeerUser,
        lang_code: str,
        commands: Sequence[types.BotCommand],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResetBotCommands(TLRequest):
    """
    [Read `bots.resetBotCommands` docs](https://core.telegram.org/method/bots.resetBotCommands).

    Generated from the following TL definition:
    ```tl
    bots.resetBotCommands#3d8de0f9 scope:BotCommandScope lang_code:string = Bool
    ```
    """
    def __new__(
        cls,
        scope: types.BotCommandScopeDefault | types.BotCommandScopeUsers | types.BotCommandScopeChats | types.BotCommandScopeChatAdmins | types.BotCommandScopePeer | types.BotCommandScopePeerAdmins | types.BotCommandScopePeerUser,
        lang_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetBotCommands(TLRequest):
    """
    [Read `bots.getBotCommands` docs](https://core.telegram.org/method/bots.getBotCommands).

    Generated from the following TL definition:
    ```tl
    bots.getBotCommands#e34c0dd6 scope:BotCommandScope lang_code:string = Vector<BotCommand>
    ```
    """
    def __new__(
        cls,
        scope: types.BotCommandScopeDefault | types.BotCommandScopeUsers | types.BotCommandScopeChats | types.BotCommandScopeChatAdmins | types.BotCommandScopePeer | types.BotCommandScopePeerAdmins | types.BotCommandScopePeerUser,
        lang_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetBotMenuButton(TLRequest):
    """
    [Read `bots.setBotMenuButton` docs](https://core.telegram.org/method/bots.setBotMenuButton).

    Generated from the following TL definition:
    ```tl
    bots.setBotMenuButton#4504d54f user_id:InputUser button:BotMenuButton = Bool
    ```
    """
    def __new__(
        cls,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        button: types.BotMenuButtonDefault | types.BotMenuButtonCommands | types.BotMenuButton,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetBotMenuButton(TLRequest):
    """
    [Read `bots.getBotMenuButton` docs](https://core.telegram.org/method/bots.getBotMenuButton).

    Generated from the following TL definition:
    ```tl
    bots.getBotMenuButton#9c60eb28 user_id:InputUser = BotMenuButton
    ```
    """
    def __new__(
        cls,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetBotBroadcastDefaultAdminRights(TLRequest):
    """
    [Read `bots.setBotBroadcastDefaultAdminRights` docs](https://core.telegram.org/method/bots.setBotBroadcastDefaultAdminRights).

    Generated from the following TL definition:
    ```tl
    bots.setBotBroadcastDefaultAdminRights#788464e1 admin_rights:ChatAdminRights = Bool
    ```
    """
    def __new__(
        cls,
        admin_rights: types.ChatAdminRights,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetBotGroupDefaultAdminRights(TLRequest):
    """
    [Read `bots.setBotGroupDefaultAdminRights` docs](https://core.telegram.org/method/bots.setBotGroupDefaultAdminRights).

    Generated from the following TL definition:
    ```tl
    bots.setBotGroupDefaultAdminRights#925ec9ea admin_rights:ChatAdminRights = Bool
    ```
    """
    def __new__(
        cls,
        admin_rights: types.ChatAdminRights,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetBotInfo(TLRequest):
    """
    [Read `bots.setBotInfo` docs](https://core.telegram.org/method/bots.setBotInfo).

    Generated from the following TL definition:
    ```tl
    bots.setBotInfo#10cf3123 flags:# bot:flags.2?InputUser lang_code:string name:flags.3?string about:flags.0?string description:flags.1?string = Bool
    ```
    """
    def __new__(
        cls,
        bot: Optional[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
        lang_code: str,
        name: Optional[str],
        about: Optional[str],
        description: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetBotInfo(TLRequest):
    """
    [Read `bots.getBotInfo` docs](https://core.telegram.org/method/bots.getBotInfo).

    Generated from the following TL definition:
    ```tl
    bots.getBotInfo#dcd914fd flags:# bot:flags.0?InputUser lang_code:string = bots.BotInfo
    ```
    """
    def __new__(
        cls,
        bot: Optional[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
        lang_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReorderUsernames(TLRequest):
    """
    [Read `bots.reorderUsernames` docs](https://core.telegram.org/method/bots.reorderUsernames).

    Generated from the following TL definition:
    ```tl
    bots.reorderUsernames#9709b1c2 bot:InputUser order:Vector<string> = Bool
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        order: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleUsername(TLRequest):
    """
    [Read `bots.toggleUsername` docs](https://core.telegram.org/method/bots.toggleUsername).

    Generated from the following TL definition:
    ```tl
    bots.toggleUsername#53ca973 bot:InputUser username:string active:Bool = Bool
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        username: str,
        active: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CanSendMessage(TLRequest):
    """
    [Read `bots.canSendMessage` docs](https://core.telegram.org/method/bots.canSendMessage).

    Generated from the following TL definition:
    ```tl
    bots.canSendMessage#1359f4e6 bot:InputUser = Bool
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AllowSendMessage(TLRequest):
    """
    [Read `bots.allowSendMessage` docs](https://core.telegram.org/method/bots.allowSendMessage).

    Generated from the following TL definition:
    ```tl
    bots.allowSendMessage#f132e3ef bot:InputUser = Updates
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InvokeWebViewCustomMethod(TLRequest):
    """
    [Read `bots.invokeWebViewCustomMethod` docs](https://core.telegram.org/method/bots.invokeWebViewCustomMethod).

    Generated from the following TL definition:
    ```tl
    bots.invokeWebViewCustomMethod#87fc5e7 bot:InputUser custom_method:string params:DataJSON = DataJSON
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        custom_method: str,
        params: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPopularAppBots(TLRequest):
    """
    [Read `bots.getPopularAppBots` docs](https://core.telegram.org/method/bots.getPopularAppBots).

    Generated from the following TL definition:
    ```tl
    bots.getPopularAppBots#c2510192 offset:string limit:int = bots.PopularAppBots
    ```
    """
    def __new__(
        cls,
        offset: str,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AddPreviewMedia(TLRequest):
    """
    [Read `bots.addPreviewMedia` docs](https://core.telegram.org/method/bots.addPreviewMedia).

    Generated from the following TL definition:
    ```tl
    bots.addPreviewMedia#17aeb75a bot:InputUser lang_code:string media:InputMedia = BotPreviewMedia
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        lang_code: str,
        media: types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditPreviewMedia(TLRequest):
    """
    [Read `bots.editPreviewMedia` docs](https://core.telegram.org/method/bots.editPreviewMedia).

    Generated from the following TL definition:
    ```tl
    bots.editPreviewMedia#8525606f bot:InputUser lang_code:string media:InputMedia new_media:InputMedia = BotPreviewMedia
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        lang_code: str,
        media: types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice,
        new_media: types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeletePreviewMedia(TLRequest):
    """
    [Read `bots.deletePreviewMedia` docs](https://core.telegram.org/method/bots.deletePreviewMedia).

    Generated from the following TL definition:
    ```tl
    bots.deletePreviewMedia#2d0135b3 bot:InputUser lang_code:string media:Vector<InputMedia> = Bool
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        lang_code: str,
        media: Sequence[types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReorderPreviewMedias(TLRequest):
    """
    [Read `bots.reorderPreviewMedias` docs](https://core.telegram.org/method/bots.reorderPreviewMedias).

    Generated from the following TL definition:
    ```tl
    bots.reorderPreviewMedias#b627f3aa bot:InputUser lang_code:string order:Vector<InputMedia> = Bool
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        lang_code: str,
        order: Sequence[types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPreviewInfo(TLRequest):
    """
    [Read `bots.getPreviewInfo` docs](https://core.telegram.org/method/bots.getPreviewInfo).

    Generated from the following TL definition:
    ```tl
    bots.getPreviewInfo#423ab3ad bot:InputUser lang_code:string = bots.PreviewInfo
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        lang_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPreviewMedias(TLRequest):
    """
    [Read `bots.getPreviewMedias` docs](https://core.telegram.org/method/bots.getPreviewMedias).

    Generated from the following TL definition:
    ```tl
    bots.getPreviewMedias#a2a5594d bot:InputUser = Vector<BotPreviewMedia>
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateUserEmojiStatus(TLRequest):
    """
    [Read `bots.updateUserEmojiStatus` docs](https://core.telegram.org/method/bots.updateUserEmojiStatus).

    Generated from the following TL definition:
    ```tl
    bots.updateUserEmojiStatus#ed9f30c5 user_id:InputUser emoji_status:EmojiStatus = Bool
    ```
    """
    def __new__(
        cls,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        emoji_status: types.EmojiStatusEmpty | types.EmojiStatus | types.EmojiStatusCollectible | types.InputEmojiStatusCollectible,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleUserEmojiStatusPermission(TLRequest):
    """
    [Read `bots.toggleUserEmojiStatusPermission` docs](https://core.telegram.org/method/bots.toggleUserEmojiStatusPermission).

    Generated from the following TL definition:
    ```tl
    bots.toggleUserEmojiStatusPermission#6de6392 bot:InputUser enabled:Bool = Bool
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckDownloadFileParams(TLRequest):
    """
    [Read `bots.checkDownloadFileParams` docs](https://core.telegram.org/method/bots.checkDownloadFileParams).

    Generated from the following TL definition:
    ```tl
    bots.checkDownloadFileParams#50077589 bot:InputUser file_name:string url:string = Bool
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        file_name: str,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAdminedBots(TLRequest):
    """
    [Read `bots.getAdminedBots` docs](https://core.telegram.org/method/bots.getAdminedBots).

    Generated from the following TL definition:
    ```tl
    bots.getAdminedBots#b0711d83 = Vector<User>
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStarRefProgram(TLRequest):
    """
    [Read `bots.updateStarRefProgram` docs](https://core.telegram.org/method/bots.updateStarRefProgram).

    Generated from the following TL definition:
    ```tl
    bots.updateStarRefProgram#778b5ab3 flags:# bot:InputUser commission_permille:int duration_months:flags.0?int = StarRefProgram
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        commission_permille: int,
        duration_months: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetCustomVerification(TLRequest):
    """
    [Read `bots.setCustomVerification` docs](https://core.telegram.org/method/bots.setCustomVerification).

    Generated from the following TL definition:
    ```tl
    bots.setCustomVerification#8b89dfbd flags:# enabled:flags.1?true bot:flags.0?InputUser peer:InputPeer custom_description:flags.2?string = Bool
    ```
    """
    def __new__(
        cls,
        enabled: bool,
        bot: Optional[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        custom_description: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetBotRecommendations(TLRequest):
    """
    [Read `bots.getBotRecommendations` docs](https://core.telegram.org/method/bots.getBotRecommendations).

    Generated from the following TL definition:
    ```tl
    bots.getBotRecommendations#a1b70815 bot:InputUser = users.Users
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

