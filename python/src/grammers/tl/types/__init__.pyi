from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class Error(TLObject):
    """
    [Read `error` docs](https://core.telegram.org/constructor/error).

    Generated from the following TL definition:
    ```tl
    error#c4b9f9bb code:int text:string = Error
    ```
    """
    def __new__(
        cls,
        code: int,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Null(TLObject):
    """
    [Read `null` docs](https://core.telegram.org/constructor/null).

    Generated from the following TL definition:
    ```tl
    null#56730bcc = Null
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPeerEmpty(TLObject):
    """
    [Read `inputPeerEmpty` docs](https://core.telegram.org/constructor/inputPeerEmpty).

    Generated from the following TL definition:
    ```tl
    inputPeerEmpty#7f3b18ea = InputPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPeerSelf(TLObject):
    """
    [Read `inputPeerSelf` docs](https://core.telegram.org/constructor/inputPeerSelf).

    Generated from the following TL definition:
    ```tl
    inputPeerSelf#7da07ec9 = InputPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPeerChat(TLObject):
    """
    [Read `inputPeerChat` docs](https://core.telegram.org/constructor/inputPeerChat).

    Generated from the following TL definition:
    ```tl
    inputPeerChat#35a95cb9 chat_id:long = InputPeer
    ```
    """
    def __new__(
        cls,
        chat_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPeerUser(TLObject):
    """
    [Read `inputPeerUser` docs](https://core.telegram.org/constructor/inputPeerUser).

    Generated from the following TL definition:
    ```tl
    inputPeerUser#dde8a54c user_id:long access_hash:long = InputPeer
    ```
    """
    def __new__(
        cls,
        user_id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPeerChannel(TLObject):
    """
    [Read `inputPeerChannel` docs](https://core.telegram.org/constructor/inputPeerChannel).

    Generated from the following TL definition:
    ```tl
    inputPeerChannel#27bcbbfc channel_id:long access_hash:long = InputPeer
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPeerUserFromMessage(TLObject):
    """
    [Read `inputPeerUserFromMessage` docs](https://core.telegram.org/constructor/inputPeerUserFromMessage).

    Generated from the following TL definition:
    ```tl
    inputPeerUserFromMessage#a87b0a1c peer:InputPeer msg_id:int user_id:long = InputPeer
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        user_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPeerChannelFromMessage(TLObject):
    """
    [Read `inputPeerChannelFromMessage` docs](https://core.telegram.org/constructor/inputPeerChannelFromMessage).

    Generated from the following TL definition:
    ```tl
    inputPeerChannelFromMessage#bd2a0840 peer:InputPeer msg_id:int channel_id:long = InputPeer
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        channel_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputUserEmpty(TLObject):
    """
    [Read `inputUserEmpty` docs](https://core.telegram.org/constructor/inputUserEmpty).

    Generated from the following TL definition:
    ```tl
    inputUserEmpty#b98886cf = InputUser
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputUserSelf(TLObject):
    """
    [Read `inputUserSelf` docs](https://core.telegram.org/constructor/inputUserSelf).

    Generated from the following TL definition:
    ```tl
    inputUserSelf#f7c1b13f = InputUser
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputUser(TLObject):
    """
    [Read `inputUser` docs](https://core.telegram.org/constructor/inputUser).

    Generated from the following TL definition:
    ```tl
    inputUser#f21158c6 user_id:long access_hash:long = InputUser
    ```
    """
    def __new__(
        cls,
        user_id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputUserFromMessage(TLObject):
    """
    [Read `inputUserFromMessage` docs](https://core.telegram.org/constructor/inputUserFromMessage).

    Generated from the following TL definition:
    ```tl
    inputUserFromMessage#1da448e2 peer:InputPeer msg_id:int user_id:long = InputUser
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        user_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPhoneContact(TLObject):
    """
    [Read `inputPhoneContact` docs](https://core.telegram.org/constructor/inputPhoneContact).

    Generated from the following TL definition:
    ```tl
    inputPhoneContact#6a1dc4be flags:# client_id:long phone:string first_name:string last_name:string note:flags.0?TextWithEntities = InputContact
    ```
    """
    def __new__(
        cls,
        client_id: int,
        phone: str,
        first_name: str,
        last_name: str,
        note: Optional[types.TextWithEntities],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputFile(TLObject):
    """
    [Read `inputFile` docs](https://core.telegram.org/constructor/inputFile).

    Generated from the following TL definition:
    ```tl
    inputFile#f52ff27f id:long parts:int name:string md5_checksum:string = InputFile
    ```
    """
    def __new__(
        cls,
        id: int,
        parts: int,
        name: str,
        md5_checksum: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputFileBig(TLObject):
    """
    [Read `inputFileBig` docs](https://core.telegram.org/constructor/inputFileBig).

    Generated from the following TL definition:
    ```tl
    inputFileBig#fa4f0bb5 id:long parts:int name:string = InputFile
    ```
    """
    def __new__(
        cls,
        id: int,
        parts: int,
        name: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputFileStoryDocument(TLObject):
    """
    [Read `inputFileStoryDocument` docs](https://core.telegram.org/constructor/inputFileStoryDocument).

    Generated from the following TL definition:
    ```tl
    inputFileStoryDocument#62dc8b48 id:InputDocument = InputFile
    ```
    """
    def __new__(
        cls,
        id: types.InputDocumentEmpty | types.InputDocument,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaEmpty(TLObject):
    """
    [Read `inputMediaEmpty` docs](https://core.telegram.org/constructor/inputMediaEmpty).

    Generated from the following TL definition:
    ```tl
    inputMediaEmpty#9664f57f = InputMedia
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaUploadedPhoto(TLObject):
    """
    [Read `inputMediaUploadedPhoto` docs](https://core.telegram.org/constructor/inputMediaUploadedPhoto).

    Generated from the following TL definition:
    ```tl
    inputMediaUploadedPhoto#1e287d04 flags:# spoiler:flags.2?true file:InputFile stickers:flags.0?Vector<InputDocument> ttl_seconds:flags.1?int = InputMedia
    ```
    """
    def __new__(
        cls,
        spoiler: bool,
        file: types.InputFile | types.InputFileBig | types.InputFileStoryDocument,
        stickers: Optional[Sequence[types.InputDocumentEmpty | types.InputDocument]],
        ttl_seconds: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaPhoto(TLObject):
    """
    [Read `inputMediaPhoto` docs](https://core.telegram.org/constructor/inputMediaPhoto).

    Generated from the following TL definition:
    ```tl
    inputMediaPhoto#b3ba0635 flags:# spoiler:flags.1?true id:InputPhoto ttl_seconds:flags.0?int = InputMedia
    ```
    """
    def __new__(
        cls,
        spoiler: bool,
        id: types.InputPhotoEmpty | types.InputPhoto,
        ttl_seconds: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaGeoPoint(TLObject):
    """
    [Read `inputMediaGeoPoint` docs](https://core.telegram.org/constructor/inputMediaGeoPoint).

    Generated from the following TL definition:
    ```tl
    inputMediaGeoPoint#f9c44144 geo_point:InputGeoPoint = InputMedia
    ```
    """
    def __new__(
        cls,
        geo_point: types.InputGeoPointEmpty | types.InputGeoPoint,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaContact(TLObject):
    """
    [Read `inputMediaContact` docs](https://core.telegram.org/constructor/inputMediaContact).

    Generated from the following TL definition:
    ```tl
    inputMediaContact#f8ab7dfb phone_number:string first_name:string last_name:string vcard:string = InputMedia
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        first_name: str,
        last_name: str,
        vcard: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaUploadedDocument(TLObject):
    """
    [Read `inputMediaUploadedDocument` docs](https://core.telegram.org/constructor/inputMediaUploadedDocument).

    Generated from the following TL definition:
    ```tl
    inputMediaUploadedDocument#37c9330 flags:# nosound_video:flags.3?true force_file:flags.4?true spoiler:flags.5?true file:InputFile thumb:flags.2?InputFile mime_type:string attributes:Vector<DocumentAttribute> stickers:flags.0?Vector<InputDocument> video_cover:flags.6?InputPhoto video_timestamp:flags.7?int ttl_seconds:flags.1?int = InputMedia
    ```
    """
    def __new__(
        cls,
        nosound_video: bool,
        force_file: bool,
        spoiler: bool,
        file: types.InputFile | types.InputFileBig | types.InputFileStoryDocument,
        thumb: Optional[types.InputFile | types.InputFileBig | types.InputFileStoryDocument],
        mime_type: str,
        attributes: Sequence[types.DocumentAttributeImageSize | types.DocumentAttributeAnimated | types.DocumentAttributeSticker | types.DocumentAttributeVideo | types.DocumentAttributeAudio | types.DocumentAttributeFilename | types.DocumentAttributeHasStickers | types.DocumentAttributeCustomEmoji],
        stickers: Optional[Sequence[types.InputDocumentEmpty | types.InputDocument]],
        video_cover: Optional[types.InputPhotoEmpty | types.InputPhoto],
        video_timestamp: Optional[int],
        ttl_seconds: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaDocument(TLObject):
    """
    [Read `inputMediaDocument` docs](https://core.telegram.org/constructor/inputMediaDocument).

    Generated from the following TL definition:
    ```tl
    inputMediaDocument#a8763ab5 flags:# spoiler:flags.2?true id:InputDocument video_cover:flags.3?InputPhoto video_timestamp:flags.4?int ttl_seconds:flags.0?int query:flags.1?string = InputMedia
    ```
    """
    def __new__(
        cls,
        spoiler: bool,
        id: types.InputDocumentEmpty | types.InputDocument,
        video_cover: Optional[types.InputPhotoEmpty | types.InputPhoto],
        video_timestamp: Optional[int],
        ttl_seconds: Optional[int],
        query: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaVenue(TLObject):
    """
    [Read `inputMediaVenue` docs](https://core.telegram.org/constructor/inputMediaVenue).

    Generated from the following TL definition:
    ```tl
    inputMediaVenue#c13d1c11 geo_point:InputGeoPoint title:string address:string provider:string venue_id:string venue_type:string = InputMedia
    ```
    """
    def __new__(
        cls,
        geo_point: types.InputGeoPointEmpty | types.InputGeoPoint,
        title: str,
        address: str,
        provider: str,
        venue_id: str,
        venue_type: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaPhotoExternal(TLObject):
    """
    [Read `inputMediaPhotoExternal` docs](https://core.telegram.org/constructor/inputMediaPhotoExternal).

    Generated from the following TL definition:
    ```tl
    inputMediaPhotoExternal#e5bbfe1a flags:# spoiler:flags.1?true url:string ttl_seconds:flags.0?int = InputMedia
    ```
    """
    def __new__(
        cls,
        spoiler: bool,
        url: str,
        ttl_seconds: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaDocumentExternal(TLObject):
    """
    [Read `inputMediaDocumentExternal` docs](https://core.telegram.org/constructor/inputMediaDocumentExternal).

    Generated from the following TL definition:
    ```tl
    inputMediaDocumentExternal#779600f9 flags:# spoiler:flags.1?true url:string ttl_seconds:flags.0?int video_cover:flags.2?InputPhoto video_timestamp:flags.3?int = InputMedia
    ```
    """
    def __new__(
        cls,
        spoiler: bool,
        url: str,
        ttl_seconds: Optional[int],
        video_cover: Optional[types.InputPhotoEmpty | types.InputPhoto],
        video_timestamp: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaGame(TLObject):
    """
    [Read `inputMediaGame` docs](https://core.telegram.org/constructor/inputMediaGame).

    Generated from the following TL definition:
    ```tl
    inputMediaGame#d33f43f3 id:InputGame = InputMedia
    ```
    """
    def __new__(
        cls,
        id: types.InputGameId | types.InputGameShortName,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaInvoice(TLObject):
    """
    [Read `inputMediaInvoice` docs](https://core.telegram.org/constructor/inputMediaInvoice).

    Generated from the following TL definition:
    ```tl
    inputMediaInvoice#405fef0d flags:# title:string description:string photo:flags.0?InputWebDocument invoice:Invoice payload:bytes provider:flags.3?string provider_data:DataJSON start_param:flags.1?string extended_media:flags.2?InputMedia = InputMedia
    ```
    """
    def __new__(
        cls,
        title: str,
        description: str,
        photo: Optional[types.InputWebDocument],
        invoice: types.Invoice,
        payload: bytes,
        provider: Optional[str],
        provider_data: types.DataJson,
        start_param: Optional[str],
        extended_media: Optional[types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaGeoLive(TLObject):
    """
    [Read `inputMediaGeoLive` docs](https://core.telegram.org/constructor/inputMediaGeoLive).

    Generated from the following TL definition:
    ```tl
    inputMediaGeoLive#971fa843 flags:# stopped:flags.0?true geo_point:InputGeoPoint heading:flags.2?int period:flags.1?int proximity_notification_radius:flags.3?int = InputMedia
    ```
    """
    def __new__(
        cls,
        stopped: bool,
        geo_point: types.InputGeoPointEmpty | types.InputGeoPoint,
        heading: Optional[int],
        period: Optional[int],
        proximity_notification_radius: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaPoll(TLObject):
    """
    [Read `inputMediaPoll` docs](https://core.telegram.org/constructor/inputMediaPoll).

    Generated from the following TL definition:
    ```tl
    inputMediaPoll#f94e5f1 flags:# poll:Poll correct_answers:flags.0?Vector<bytes> solution:flags.1?string solution_entities:flags.1?Vector<MessageEntity> = InputMedia
    ```
    """
    def __new__(
        cls,
        poll: types.Poll,
        correct_answers: Optional[Sequence[bytes]],
        solution: Optional[str],
        solution_entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaDice(TLObject):
    """
    [Read `inputMediaDice` docs](https://core.telegram.org/constructor/inputMediaDice).

    Generated from the following TL definition:
    ```tl
    inputMediaDice#e66fbf7b emoticon:string = InputMedia
    ```
    """
    def __new__(
        cls,
        emoticon: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaStory(TLObject):
    """
    [Read `inputMediaStory` docs](https://core.telegram.org/constructor/inputMediaStory).

    Generated from the following TL definition:
    ```tl
    inputMediaStory#89fdd778 peer:InputPeer id:int = InputMedia
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaWebPage(TLObject):
    """
    [Read `inputMediaWebPage` docs](https://core.telegram.org/constructor/inputMediaWebPage).

    Generated from the following TL definition:
    ```tl
    inputMediaWebPage#c21b8849 flags:# force_large_media:flags.0?true force_small_media:flags.1?true optional:flags.2?true url:string = InputMedia
    ```
    """
    def __new__(
        cls,
        force_large_media: bool,
        force_small_media: bool,
        optional: bool,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaPaidMedia(TLObject):
    """
    [Read `inputMediaPaidMedia` docs](https://core.telegram.org/constructor/inputMediaPaidMedia).

    Generated from the following TL definition:
    ```tl
    inputMediaPaidMedia#c4103386 flags:# stars_amount:long extended_media:Vector<InputMedia> payload:flags.0?string = InputMedia
    ```
    """
    def __new__(
        cls,
        stars_amount: int,
        extended_media: Sequence[types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice],
        payload: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaTodo(TLObject):
    """
    [Read `inputMediaTodo` docs](https://core.telegram.org/constructor/inputMediaTodo).

    Generated from the following TL definition:
    ```tl
    inputMediaTodo#9fc55fde todo:TodoList = InputMedia
    ```
    """
    def __new__(
        cls,
        todo: types.TodoList,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaStakeDice(TLObject):
    """
    [Read `inputMediaStakeDice` docs](https://core.telegram.org/constructor/inputMediaStakeDice).

    Generated from the following TL definition:
    ```tl
    inputMediaStakeDice#f3a9244a game_hash:string ton_amount:long client_seed:bytes = InputMedia
    ```
    """
    def __new__(
        cls,
        game_hash: str,
        ton_amount: int,
        client_seed: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputChatPhotoEmpty(TLObject):
    """
    [Read `inputChatPhotoEmpty` docs](https://core.telegram.org/constructor/inputChatPhotoEmpty).

    Generated from the following TL definition:
    ```tl
    inputChatPhotoEmpty#1ca48f57 = InputChatPhoto
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputChatUploadedPhoto(TLObject):
    """
    [Read `inputChatUploadedPhoto` docs](https://core.telegram.org/constructor/inputChatUploadedPhoto).

    Generated from the following TL definition:
    ```tl
    inputChatUploadedPhoto#bdcdaec0 flags:# file:flags.0?InputFile video:flags.1?InputFile video_start_ts:flags.2?double video_emoji_markup:flags.3?VideoSize = InputChatPhoto
    ```
    """
    def __new__(
        cls,
        file: Optional[types.InputFile | types.InputFileBig | types.InputFileStoryDocument],
        video: Optional[types.InputFile | types.InputFileBig | types.InputFileStoryDocument],
        video_start_ts: Optional[float],
        video_emoji_markup: Optional[types.VideoSize | types.VideoSizeEmojiMarkup | types.VideoSizeStickerMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputChatPhoto(TLObject):
    """
    [Read `inputChatPhoto` docs](https://core.telegram.org/constructor/inputChatPhoto).

    Generated from the following TL definition:
    ```tl
    inputChatPhoto#8953ad37 id:InputPhoto = InputChatPhoto
    ```
    """
    def __new__(
        cls,
        id: types.InputPhotoEmpty | types.InputPhoto,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputGeoPointEmpty(TLObject):
    """
    [Read `inputGeoPointEmpty` docs](https://core.telegram.org/constructor/inputGeoPointEmpty).

    Generated from the following TL definition:
    ```tl
    inputGeoPointEmpty#e4c123d6 = InputGeoPoint
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputGeoPoint(TLObject):
    """
    [Read `inputGeoPoint` docs](https://core.telegram.org/constructor/inputGeoPoint).

    Generated from the following TL definition:
    ```tl
    inputGeoPoint#48222faf flags:# lat:double long:double accuracy_radius:flags.0?int = InputGeoPoint
    ```
    """
    def __new__(
        cls,
        lat: float,
        long: float,
        accuracy_radius: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPhotoEmpty(TLObject):
    """
    [Read `inputPhotoEmpty` docs](https://core.telegram.org/constructor/inputPhotoEmpty).

    Generated from the following TL definition:
    ```tl
    inputPhotoEmpty#1cd7bf0d = InputPhoto
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPhoto(TLObject):
    """
    [Read `inputPhoto` docs](https://core.telegram.org/constructor/inputPhoto).

    Generated from the following TL definition:
    ```tl
    inputPhoto#3bb3b94a id:long access_hash:long file_reference:bytes = InputPhoto
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        file_reference: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputFileLocation(TLObject):
    """
    [Read `inputFileLocation` docs](https://core.telegram.org/constructor/inputFileLocation).

    Generated from the following TL definition:
    ```tl
    inputFileLocation#dfdaabe1 volume_id:long local_id:int secret:long file_reference:bytes = InputFileLocation
    ```
    """
    def __new__(
        cls,
        volume_id: int,
        local_id: int,
        secret: int,
        file_reference: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputEncryptedFileLocation(TLObject):
    """
    [Read `inputEncryptedFileLocation` docs](https://core.telegram.org/constructor/inputEncryptedFileLocation).

    Generated from the following TL definition:
    ```tl
    inputEncryptedFileLocation#f5235d55 id:long access_hash:long = InputFileLocation
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputDocumentFileLocation(TLObject):
    """
    [Read `inputDocumentFileLocation` docs](https://core.telegram.org/constructor/inputDocumentFileLocation).

    Generated from the following TL definition:
    ```tl
    inputDocumentFileLocation#bad07584 id:long access_hash:long file_reference:bytes thumb_size:string = InputFileLocation
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        file_reference: bytes,
        thumb_size: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputSecureFileLocation(TLObject):
    """
    [Read `inputSecureFileLocation` docs](https://core.telegram.org/constructor/inputSecureFileLocation).

    Generated from the following TL definition:
    ```tl
    inputSecureFileLocation#cbc7ee28 id:long access_hash:long = InputFileLocation
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputTakeoutFileLocation(TLObject):
    """
    [Read `inputTakeoutFileLocation` docs](https://core.telegram.org/constructor/inputTakeoutFileLocation).

    Generated from the following TL definition:
    ```tl
    inputTakeoutFileLocation#29be5899 = InputFileLocation
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPhotoFileLocation(TLObject):
    """
    [Read `inputPhotoFileLocation` docs](https://core.telegram.org/constructor/inputPhotoFileLocation).

    Generated from the following TL definition:
    ```tl
    inputPhotoFileLocation#40181ffe id:long access_hash:long file_reference:bytes thumb_size:string = InputFileLocation
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        file_reference: bytes,
        thumb_size: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPhotoLegacyFileLocation(TLObject):
    """
    [Read `inputPhotoLegacyFileLocation` docs](https://core.telegram.org/constructor/inputPhotoLegacyFileLocation).

    Generated from the following TL definition:
    ```tl
    inputPhotoLegacyFileLocation#d83466f3 id:long access_hash:long file_reference:bytes volume_id:long local_id:int secret:long = InputFileLocation
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        file_reference: bytes,
        volume_id: int,
        local_id: int,
        secret: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPeerPhotoFileLocation(TLObject):
    """
    [Read `inputPeerPhotoFileLocation` docs](https://core.telegram.org/constructor/inputPeerPhotoFileLocation).

    Generated from the following TL definition:
    ```tl
    inputPeerPhotoFileLocation#37257e99 flags:# big:flags.0?true peer:InputPeer photo_id:long = InputFileLocation
    ```
    """
    def __new__(
        cls,
        big: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        photo_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetThumb(TLObject):
    """
    [Read `inputStickerSetThumb` docs](https://core.telegram.org/constructor/inputStickerSetThumb).

    Generated from the following TL definition:
    ```tl
    inputStickerSetThumb#9d84f3db stickerset:InputStickerSet thumb_version:int = InputFileLocation
    ```
    """
    def __new__(
        cls,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
        thumb_version: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputGroupCallStream(TLObject):
    """
    [Read `inputGroupCallStream` docs](https://core.telegram.org/constructor/inputGroupCallStream).

    Generated from the following TL definition:
    ```tl
    inputGroupCallStream#598a92a flags:# call:InputGroupCall time_ms:long scale:int video_channel:flags.0?int video_quality:flags.0?int = InputFileLocation
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        time_ms: int,
        scale: int,
        video_channel: Optional[int],
        video_quality: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerUser(TLObject):
    """
    [Read `peerUser` docs](https://core.telegram.org/constructor/peerUser).

    Generated from the following TL definition:
    ```tl
    peerUser#59511722 user_id:long = Peer
    ```
    """
    def __new__(
        cls,
        user_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerChat(TLObject):
    """
    [Read `peerChat` docs](https://core.telegram.org/constructor/peerChat).

    Generated from the following TL definition:
    ```tl
    peerChat#36c6019a chat_id:long = Peer
    ```
    """
    def __new__(
        cls,
        chat_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerChannel(TLObject):
    """
    [Read `peerChannel` docs](https://core.telegram.org/constructor/peerChannel).

    Generated from the following TL definition:
    ```tl
    peerChannel#a2a5371e channel_id:long = Peer
    ```
    """
    def __new__(
        cls,
        channel_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UserEmpty(TLObject):
    """
    [Read `userEmpty` docs](https://core.telegram.org/constructor/userEmpty).

    Generated from the following TL definition:
    ```tl
    userEmpty#d3bc4b7a id:long = User
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class User(TLObject):
    """
    [Read `user` docs](https://core.telegram.org/constructor/user).

    Generated from the following TL definition:
    ```tl
    user#31774388 flags:# self:flags.10?true contact:flags.11?true mutual_contact:flags.12?true deleted:flags.13?true bot:flags.14?true bot_chat_history:flags.15?true bot_nochats:flags.16?true verified:flags.17?true restricted:flags.18?true min:flags.20?true bot_inline_geo:flags.21?true support:flags.23?true scam:flags.24?true apply_min_photo:flags.25?true fake:flags.26?true bot_attach_menu:flags.27?true premium:flags.28?true attach_menu_enabled:flags.29?true flags2:# bot_can_edit:flags2.1?true close_friend:flags2.2?true stories_hidden:flags2.3?true stories_unavailable:flags2.4?true contact_require_premium:flags2.10?true bot_business:flags2.11?true bot_has_main_app:flags2.13?true bot_forum_view:flags2.16?true id:long access_hash:flags.0?long first_name:flags.1?string last_name:flags.2?string username:flags.3?string phone:flags.4?string photo:flags.5?UserProfilePhoto status:flags.6?UserStatus bot_info_version:flags.14?int restriction_reason:flags.18?Vector<RestrictionReason> bot_inline_placeholder:flags.19?string lang_code:flags.22?string emoji_status:flags.30?EmojiStatus usernames:flags2.0?Vector<Username> stories_max_id:flags2.5?RecentStory color:flags2.8?PeerColor profile_color:flags2.9?PeerColor bot_active_users:flags2.12?int bot_verification_icon:flags2.14?long send_paid_messages_stars:flags2.15?long = User
    ```
    """
    def __new__(
        cls,
        is_self: bool,
        contact: bool,
        mutual_contact: bool,
        deleted: bool,
        bot: bool,
        bot_chat_history: bool,
        bot_nochats: bool,
        verified: bool,
        restricted: bool,
        min: bool,
        bot_inline_geo: bool,
        support: bool,
        scam: bool,
        apply_min_photo: bool,
        fake: bool,
        bot_attach_menu: bool,
        premium: bool,
        attach_menu_enabled: bool,
        bot_can_edit: bool,
        close_friend: bool,
        stories_hidden: bool,
        stories_unavailable: bool,
        contact_require_premium: bool,
        bot_business: bool,
        bot_has_main_app: bool,
        bot_forum_view: bool,
        id: int,
        access_hash: Optional[int],
        first_name: Optional[str],
        last_name: Optional[str],
        username: Optional[str],
        phone: Optional[str],
        photo: Optional[types.UserProfilePhotoEmpty | types.UserProfilePhoto],
        status: Optional[types.UserStatusEmpty | types.UserStatusOnline | types.UserStatusOffline | types.UserStatusRecently | types.UserStatusLastWeek | types.UserStatusLastMonth],
        bot_info_version: Optional[int],
        restriction_reason: Optional[Sequence[types.RestrictionReason]],
        bot_inline_placeholder: Optional[str],
        lang_code: Optional[str],
        emoji_status: Optional[types.EmojiStatusEmpty | types.EmojiStatus | types.EmojiStatusCollectible | types.InputEmojiStatusCollectible],
        usernames: Optional[Sequence[types.Username]],
        stories_max_id: Optional[types.RecentStory],
        color: Optional[types.PeerColor | types.PeerColorCollectible | types.InputPeerColorCollectible],
        profile_color: Optional[types.PeerColor | types.PeerColorCollectible | types.InputPeerColorCollectible],
        bot_active_users: Optional[int],
        bot_verification_icon: Optional[int],
        send_paid_messages_stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UserProfilePhotoEmpty(TLObject):
    """
    [Read `userProfilePhotoEmpty` docs](https://core.telegram.org/constructor/userProfilePhotoEmpty).

    Generated from the following TL definition:
    ```tl
    userProfilePhotoEmpty#4f11bae1 = UserProfilePhoto
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UserProfilePhoto(TLObject):
    """
    [Read `userProfilePhoto` docs](https://core.telegram.org/constructor/userProfilePhoto).

    Generated from the following TL definition:
    ```tl
    userProfilePhoto#82d1f706 flags:# has_video:flags.0?true personal:flags.2?true photo_id:long stripped_thumb:flags.1?bytes dc_id:int = UserProfilePhoto
    ```
    """
    def __new__(
        cls,
        has_video: bool,
        personal: bool,
        photo_id: int,
        stripped_thumb: Optional[bytes],
        dc_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UserStatusEmpty(TLObject):
    """
    [Read `userStatusEmpty` docs](https://core.telegram.org/constructor/userStatusEmpty).

    Generated from the following TL definition:
    ```tl
    userStatusEmpty#9d05049 = UserStatus
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UserStatusOnline(TLObject):
    """
    [Read `userStatusOnline` docs](https://core.telegram.org/constructor/userStatusOnline).

    Generated from the following TL definition:
    ```tl
    userStatusOnline#edb93949 expires:int = UserStatus
    ```
    """
    def __new__(
        cls,
        expires: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UserStatusOffline(TLObject):
    """
    [Read `userStatusOffline` docs](https://core.telegram.org/constructor/userStatusOffline).

    Generated from the following TL definition:
    ```tl
    userStatusOffline#8c703f was_online:int = UserStatus
    ```
    """
    def __new__(
        cls,
        was_online: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UserStatusRecently(TLObject):
    """
    [Read `userStatusRecently` docs](https://core.telegram.org/constructor/userStatusRecently).

    Generated from the following TL definition:
    ```tl
    userStatusRecently#7b197dc8 flags:# by_me:flags.0?true = UserStatus
    ```
    """
    def __new__(
        cls,
        by_me: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UserStatusLastWeek(TLObject):
    """
    [Read `userStatusLastWeek` docs](https://core.telegram.org/constructor/userStatusLastWeek).

    Generated from the following TL definition:
    ```tl
    userStatusLastWeek#541a1d1a flags:# by_me:flags.0?true = UserStatus
    ```
    """
    def __new__(
        cls,
        by_me: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UserStatusLastMonth(TLObject):
    """
    [Read `userStatusLastMonth` docs](https://core.telegram.org/constructor/userStatusLastMonth).

    Generated from the following TL definition:
    ```tl
    userStatusLastMonth#65899777 flags:# by_me:flags.0?true = UserStatus
    ```
    """
    def __new__(
        cls,
        by_me: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatEmpty(TLObject):
    """
    [Read `chatEmpty` docs](https://core.telegram.org/constructor/chatEmpty).

    Generated from the following TL definition:
    ```tl
    chatEmpty#29562865 id:long = Chat
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Chat(TLObject):
    """
    [Read `chat` docs](https://core.telegram.org/constructor/chat).

    Generated from the following TL definition:
    ```tl
    chat#41cbf256 flags:# creator:flags.0?true left:flags.2?true deactivated:flags.5?true call_active:flags.23?true call_not_empty:flags.24?true noforwards:flags.25?true id:long title:string photo:ChatPhoto participants_count:int date:int version:int migrated_to:flags.6?InputChannel admin_rights:flags.14?ChatAdminRights default_banned_rights:flags.18?ChatBannedRights = Chat
    ```
    """
    def __new__(
        cls,
        creator: bool,
        left: bool,
        deactivated: bool,
        call_active: bool,
        call_not_empty: bool,
        noforwards: bool,
        id: int,
        title: str,
        photo: types.ChatPhotoEmpty | types.ChatPhoto,
        participants_count: int,
        date: int,
        version: int,
        migrated_to: Optional[types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage],
        admin_rights: Optional[types.ChatAdminRights],
        default_banned_rights: Optional[types.ChatBannedRights],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatForbidden(TLObject):
    """
    [Read `chatForbidden` docs](https://core.telegram.org/constructor/chatForbidden).

    Generated from the following TL definition:
    ```tl
    chatForbidden#6592a1a7 id:long title:string = Chat
    ```
    """
    def __new__(
        cls,
        id: int,
        title: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Channel(TLObject):
    """
    [Read `channel` docs](https://core.telegram.org/constructor/channel).

    Generated from the following TL definition:
    ```tl
    channel#1c32b11c flags:# creator:flags.0?true left:flags.2?true broadcast:flags.5?true verified:flags.7?true megagroup:flags.8?true restricted:flags.9?true signatures:flags.11?true min:flags.12?true scam:flags.19?true has_link:flags.20?true has_geo:flags.21?true slowmode_enabled:flags.22?true call_active:flags.23?true call_not_empty:flags.24?true fake:flags.25?true gigagroup:flags.26?true noforwards:flags.27?true join_to_send:flags.28?true join_request:flags.29?true forum:flags.30?true flags2:# stories_hidden:flags2.1?true stories_hidden_min:flags2.2?true stories_unavailable:flags2.3?true signature_profiles:flags2.12?true autotranslation:flags2.15?true broadcast_messages_allowed:flags2.16?true monoforum:flags2.17?true forum_tabs:flags2.19?true id:long access_hash:flags.13?long title:string username:flags.6?string photo:ChatPhoto date:int restriction_reason:flags.9?Vector<RestrictionReason> admin_rights:flags.14?ChatAdminRights banned_rights:flags.15?ChatBannedRights default_banned_rights:flags.18?ChatBannedRights participants_count:flags.17?int usernames:flags2.0?Vector<Username> stories_max_id:flags2.4?RecentStory color:flags2.7?PeerColor profile_color:flags2.8?PeerColor emoji_status:flags2.9?EmojiStatus level:flags2.10?int subscription_until_date:flags2.11?int bot_verification_icon:flags2.13?long send_paid_messages_stars:flags2.14?long linked_monoforum_id:flags2.18?long = Chat
    ```
    """
    def __new__(
        cls,
        creator: bool,
        left: bool,
        broadcast: bool,
        verified: bool,
        megagroup: bool,
        restricted: bool,
        signatures: bool,
        min: bool,
        scam: bool,
        has_link: bool,
        has_geo: bool,
        slowmode_enabled: bool,
        call_active: bool,
        call_not_empty: bool,
        fake: bool,
        gigagroup: bool,
        noforwards: bool,
        join_to_send: bool,
        join_request: bool,
        forum: bool,
        stories_hidden: bool,
        stories_hidden_min: bool,
        stories_unavailable: bool,
        signature_profiles: bool,
        autotranslation: bool,
        broadcast_messages_allowed: bool,
        monoforum: bool,
        forum_tabs: bool,
        id: int,
        access_hash: Optional[int],
        title: str,
        username: Optional[str],
        photo: types.ChatPhotoEmpty | types.ChatPhoto,
        date: int,
        restriction_reason: Optional[Sequence[types.RestrictionReason]],
        admin_rights: Optional[types.ChatAdminRights],
        banned_rights: Optional[types.ChatBannedRights],
        default_banned_rights: Optional[types.ChatBannedRights],
        participants_count: Optional[int],
        usernames: Optional[Sequence[types.Username]],
        stories_max_id: Optional[types.RecentStory],
        color: Optional[types.PeerColor | types.PeerColorCollectible | types.InputPeerColorCollectible],
        profile_color: Optional[types.PeerColor | types.PeerColorCollectible | types.InputPeerColorCollectible],
        emoji_status: Optional[types.EmojiStatusEmpty | types.EmojiStatus | types.EmojiStatusCollectible | types.InputEmojiStatusCollectible],
        level: Optional[int],
        subscription_until_date: Optional[int],
        bot_verification_icon: Optional[int],
        send_paid_messages_stars: Optional[int],
        linked_monoforum_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelForbidden(TLObject):
    """
    [Read `channelForbidden` docs](https://core.telegram.org/constructor/channelForbidden).

    Generated from the following TL definition:
    ```tl
    channelForbidden#17d493d5 flags:# broadcast:flags.5?true megagroup:flags.8?true id:long access_hash:long title:string until_date:flags.16?int = Chat
    ```
    """
    def __new__(
        cls,
        broadcast: bool,
        megagroup: bool,
        id: int,
        access_hash: int,
        title: str,
        until_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatFull(TLObject):
    """
    [Read `chatFull` docs](https://core.telegram.org/constructor/chatFull).

    Generated from the following TL definition:
    ```tl
    chatFull#2633421b flags:# can_set_username:flags.7?true has_scheduled:flags.8?true translations_disabled:flags.19?true id:long about:string participants:ChatParticipants chat_photo:flags.2?Photo notify_settings:PeerNotifySettings exported_invite:flags.13?ExportedChatInvite bot_info:flags.3?Vector<BotInfo> pinned_msg_id:flags.6?int folder_id:flags.11?int call:flags.12?InputGroupCall ttl_period:flags.14?int groupcall_default_join_as:flags.15?Peer theme_emoticon:flags.16?string requests_pending:flags.17?int recent_requesters:flags.17?Vector<long> available_reactions:flags.18?ChatReactions reactions_limit:flags.20?int = ChatFull
    ```
    """
    def __new__(
        cls,
        can_set_username: bool,
        has_scheduled: bool,
        translations_disabled: bool,
        id: int,
        about: str,
        participants: types.ChatParticipantsForbidden | types.ChatParticipants,
        chat_photo: Optional[types.PhotoEmpty | types.Photo],
        notify_settings: types.PeerNotifySettings,
        exported_invite: Optional[types.ChatInviteExported | types.ChatInvitePublicJoinRequests],
        bot_info: Optional[Sequence[types.BotInfo]],
        pinned_msg_id: Optional[int],
        folder_id: Optional[int],
        call: Optional[types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage],
        ttl_period: Optional[int],
        groupcall_default_join_as: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        theme_emoticon: Optional[str],
        requests_pending: Optional[int],
        recent_requesters: Optional[Sequence[int]],
        available_reactions: Optional[types.ChatReactionsNone | types.ChatReactionsAll | types.ChatReactionsSome],
        reactions_limit: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelFull(TLObject):
    """
    [Read `channelFull` docs](https://core.telegram.org/constructor/channelFull).

    Generated from the following TL definition:
    ```tl
    channelFull#e4e0b29d flags:# can_view_participants:flags.3?true can_set_username:flags.6?true can_set_stickers:flags.7?true hidden_prehistory:flags.10?true can_set_location:flags.16?true has_scheduled:flags.19?true can_view_stats:flags.20?true blocked:flags.22?true flags2:# can_delete_channel:flags2.0?true antispam:flags2.1?true participants_hidden:flags2.2?true translations_disabled:flags2.3?true stories_pinned_available:flags2.5?true view_forum_as_messages:flags2.6?true restricted_sponsored:flags2.11?true can_view_revenue:flags2.12?true paid_media_allowed:flags2.14?true can_view_stars_revenue:flags2.15?true paid_reactions_available:flags2.16?true stargifts_available:flags2.19?true paid_messages_available:flags2.20?true id:long about:string participants_count:flags.0?int admins_count:flags.1?int kicked_count:flags.2?int banned_count:flags.2?int online_count:flags.13?int read_inbox_max_id:int read_outbox_max_id:int unread_count:int chat_photo:Photo notify_settings:PeerNotifySettings exported_invite:flags.23?ExportedChatInvite bot_info:Vector<BotInfo> migrated_from_chat_id:flags.4?long migrated_from_max_id:flags.4?int pinned_msg_id:flags.5?int stickerset:flags.8?StickerSet available_min_id:flags.9?int folder_id:flags.11?int linked_chat_id:flags.14?long location:flags.15?ChannelLocation slowmode_seconds:flags.17?int slowmode_next_send_date:flags.18?int stats_dc:flags.12?int pts:int call:flags.21?InputGroupCall ttl_period:flags.24?int pending_suggestions:flags.25?Vector<string> groupcall_default_join_as:flags.26?Peer theme_emoticon:flags.27?string requests_pending:flags.28?int recent_requesters:flags.28?Vector<long> default_send_as:flags.29?Peer available_reactions:flags.30?ChatReactions reactions_limit:flags2.13?int stories:flags2.4?PeerStories wallpaper:flags2.7?WallPaper boosts_applied:flags2.8?int boosts_unrestrict:flags2.9?int emojiset:flags2.10?StickerSet bot_verification:flags2.17?BotVerification stargifts_count:flags2.18?int send_paid_messages_stars:flags2.21?long main_tab:flags2.22?ProfileTab = ChatFull
    ```
    """
    def __new__(
        cls,
        can_view_participants: bool,
        can_set_username: bool,
        can_set_stickers: bool,
        hidden_prehistory: bool,
        can_set_location: bool,
        has_scheduled: bool,
        can_view_stats: bool,
        blocked: bool,
        can_delete_channel: bool,
        antispam: bool,
        participants_hidden: bool,
        translations_disabled: bool,
        stories_pinned_available: bool,
        view_forum_as_messages: bool,
        restricted_sponsored: bool,
        can_view_revenue: bool,
        paid_media_allowed: bool,
        can_view_stars_revenue: bool,
        paid_reactions_available: bool,
        stargifts_available: bool,
        paid_messages_available: bool,
        id: int,
        about: str,
        participants_count: Optional[int],
        admins_count: Optional[int],
        kicked_count: Optional[int],
        banned_count: Optional[int],
        online_count: Optional[int],
        read_inbox_max_id: int,
        read_outbox_max_id: int,
        unread_count: int,
        chat_photo: types.PhotoEmpty | types.Photo,
        notify_settings: types.PeerNotifySettings,
        exported_invite: Optional[types.ChatInviteExported | types.ChatInvitePublicJoinRequests],
        bot_info: Sequence[types.BotInfo],
        migrated_from_chat_id: Optional[int],
        migrated_from_max_id: Optional[int],
        pinned_msg_id: Optional[int],
        stickerset: Optional[types.StickerSet],
        available_min_id: Optional[int],
        folder_id: Optional[int],
        linked_chat_id: Optional[int],
        location: Optional[types.ChannelLocationEmpty | types.ChannelLocation],
        slowmode_seconds: Optional[int],
        slowmode_next_send_date: Optional[int],
        stats_dc: Optional[int],
        pts: int,
        call: Optional[types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage],
        ttl_period: Optional[int],
        pending_suggestions: Optional[Sequence[str]],
        groupcall_default_join_as: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        theme_emoticon: Optional[str],
        requests_pending: Optional[int],
        recent_requesters: Optional[Sequence[int]],
        default_send_as: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        available_reactions: Optional[types.ChatReactionsNone | types.ChatReactionsAll | types.ChatReactionsSome],
        reactions_limit: Optional[int],
        stories: Optional[types.PeerStories],
        wallpaper: Optional[types.WallPaper | types.WallPaperNoFile],
        boosts_applied: Optional[int],
        boosts_unrestrict: Optional[int],
        emojiset: Optional[types.StickerSet],
        bot_verification: Optional[types.BotVerification],
        stargifts_count: Optional[int],
        send_paid_messages_stars: Optional[int],
        main_tab: Optional[types.ProfileTabPosts | types.ProfileTabGifts | types.ProfileTabMedia | types.ProfileTabFiles | types.ProfileTabMusic | types.ProfileTabVoice | types.ProfileTabLinks | types.ProfileTabGifs],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatParticipant(TLObject):
    """
    [Read `chatParticipant` docs](https://core.telegram.org/constructor/chatParticipant).

    Generated from the following TL definition:
    ```tl
    chatParticipant#c02d4007 user_id:long inviter_id:long date:int = ChatParticipant
    ```
    """
    def __new__(
        cls,
        user_id: int,
        inviter_id: int,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatParticipantCreator(TLObject):
    """
    [Read `chatParticipantCreator` docs](https://core.telegram.org/constructor/chatParticipantCreator).

    Generated from the following TL definition:
    ```tl
    chatParticipantCreator#e46bcee4 user_id:long = ChatParticipant
    ```
    """
    def __new__(
        cls,
        user_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatParticipantAdmin(TLObject):
    """
    [Read `chatParticipantAdmin` docs](https://core.telegram.org/constructor/chatParticipantAdmin).

    Generated from the following TL definition:
    ```tl
    chatParticipantAdmin#a0933f5b user_id:long inviter_id:long date:int = ChatParticipant
    ```
    """
    def __new__(
        cls,
        user_id: int,
        inviter_id: int,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatParticipantsForbidden(TLObject):
    """
    [Read `chatParticipantsForbidden` docs](https://core.telegram.org/constructor/chatParticipantsForbidden).

    Generated from the following TL definition:
    ```tl
    chatParticipantsForbidden#8763d3e1 flags:# chat_id:long self_participant:flags.0?ChatParticipant = ChatParticipants
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        self_participant: Optional[types.ChatParticipant | types.ChatParticipantCreator | types.ChatParticipantAdmin],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatParticipants(TLObject):
    """
    [Read `chatParticipants` docs](https://core.telegram.org/constructor/chatParticipants).

    Generated from the following TL definition:
    ```tl
    chatParticipants#3cbc93f8 chat_id:long participants:Vector<ChatParticipant> version:int = ChatParticipants
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        participants: Sequence[types.ChatParticipant | types.ChatParticipantCreator | types.ChatParticipantAdmin],
        version: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatPhotoEmpty(TLObject):
    """
    [Read `chatPhotoEmpty` docs](https://core.telegram.org/constructor/chatPhotoEmpty).

    Generated from the following TL definition:
    ```tl
    chatPhotoEmpty#37c1011c = ChatPhoto
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatPhoto(TLObject):
    """
    [Read `chatPhoto` docs](https://core.telegram.org/constructor/chatPhoto).

    Generated from the following TL definition:
    ```tl
    chatPhoto#1c6e1c11 flags:# has_video:flags.0?true photo_id:long stripped_thumb:flags.1?bytes dc_id:int = ChatPhoto
    ```
    """
    def __new__(
        cls,
        has_video: bool,
        photo_id: int,
        stripped_thumb: Optional[bytes],
        dc_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEmpty(TLObject):
    """
    [Read `messageEmpty` docs](https://core.telegram.org/constructor/messageEmpty).

    Generated from the following TL definition:
    ```tl
    messageEmpty#90a6ca84 flags:# id:int peer_id:flags.0?Peer = Message
    ```
    """
    def __new__(
        cls,
        id: int,
        peer_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Message(TLObject):
    """
    [Read `message` docs](https://core.telegram.org/constructor/message).

    Generated from the following TL definition:
    ```tl
    message#9cb490e9 flags:# out:flags.1?true mentioned:flags.4?true media_unread:flags.5?true silent:flags.13?true post:flags.14?true from_scheduled:flags.18?true legacy:flags.19?true edit_hide:flags.21?true pinned:flags.24?true noforwards:flags.26?true invert_media:flags.27?true flags2:# offline:flags2.1?true video_processing_pending:flags2.4?true paid_suggested_post_stars:flags2.8?true paid_suggested_post_ton:flags2.9?true id:int from_id:flags.8?Peer from_boosts_applied:flags.29?int peer_id:Peer saved_peer_id:flags.28?Peer fwd_from:flags.2?MessageFwdHeader via_bot_id:flags.11?long via_business_bot_id:flags2.0?long reply_to:flags.3?MessageReplyHeader date:int message:string media:flags.9?MessageMedia reply_markup:flags.6?ReplyMarkup entities:flags.7?Vector<MessageEntity> views:flags.10?int forwards:flags.10?int replies:flags.23?MessageReplies edit_date:flags.15?int post_author:flags.16?string grouped_id:flags.17?long reactions:flags.20?MessageReactions restriction_reason:flags.22?Vector<RestrictionReason> ttl_period:flags.25?int quick_reply_shortcut_id:flags.30?int effect:flags2.2?long factcheck:flags2.3?FactCheck report_delivery_until_date:flags2.5?int paid_message_stars:flags2.6?long suggested_post:flags2.7?SuggestedPost schedule_repeat_period:flags2.10?int summary_from_language:flags2.11?string = Message
    ```
    """
    def __new__(
        cls,
        out: bool,
        mentioned: bool,
        media_unread: bool,
        silent: bool,
        post: bool,
        from_scheduled: bool,
        legacy: bool,
        edit_hide: bool,
        pinned: bool,
        noforwards: bool,
        invert_media: bool,
        offline: bool,
        video_processing_pending: bool,
        paid_suggested_post_stars: bool,
        paid_suggested_post_ton: bool,
        id: int,
        from_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        from_boosts_applied: Optional[int],
        peer_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        saved_peer_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        fwd_from: Optional[types.MessageFwdHeader],
        via_bot_id: Optional[int],
        via_business_bot_id: Optional[int],
        reply_to: Optional[types.MessageReplyHeader | types.MessageReplyStoryHeader],
        date: int,
        message: str,
        media: Optional[types.MessageMediaEmpty | types.MessageMediaPhoto | types.MessageMediaGeo | types.MessageMediaContact | types.MessageMediaUnsupported | types.MessageMediaDocument | types.MessageMediaWebPage | types.MessageMediaVenue | types.MessageMediaGame | types.MessageMediaInvoice | types.MessageMediaGeoLive | types.MessageMediaPoll | types.MessageMediaDice | types.MessageMediaStory | types.MessageMediaGiveaway | types.MessageMediaGiveawayResults | types.MessageMediaPaidMedia | types.MessageMediaToDo | types.MessageMediaVideoStream],
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        views: Optional[int],
        forwards: Optional[int],
        replies: Optional[types.MessageReplies],
        edit_date: Optional[int],
        post_author: Optional[str],
        grouped_id: Optional[int],
        reactions: Optional[types.MessageReactions],
        restriction_reason: Optional[Sequence[types.RestrictionReason]],
        ttl_period: Optional[int],
        quick_reply_shortcut_id: Optional[int],
        effect: Optional[int],
        factcheck: Optional[types.FactCheck],
        report_delivery_until_date: Optional[int],
        paid_message_stars: Optional[int],
        suggested_post: Optional[types.SuggestedPost],
        schedule_repeat_period: Optional[int],
        summary_from_language: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageService(TLObject):
    """
    [Read `messageService` docs](https://core.telegram.org/constructor/messageService).

    Generated from the following TL definition:
    ```tl
    messageService#7a800e0a flags:# out:flags.1?true mentioned:flags.4?true media_unread:flags.5?true reactions_are_possible:flags.9?true silent:flags.13?true post:flags.14?true legacy:flags.19?true id:int from_id:flags.8?Peer peer_id:Peer saved_peer_id:flags.28?Peer reply_to:flags.3?MessageReplyHeader date:int action:MessageAction reactions:flags.20?MessageReactions ttl_period:flags.25?int = Message
    ```
    """
    def __new__(
        cls,
        out: bool,
        mentioned: bool,
        media_unread: bool,
        reactions_are_possible: bool,
        silent: bool,
        post: bool,
        legacy: bool,
        id: int,
        from_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        peer_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        saved_peer_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        reply_to: Optional[types.MessageReplyHeader | types.MessageReplyStoryHeader],
        date: int,
        action: types.MessageActionEmpty | types.MessageActionChatCreate | types.MessageActionChatEditTitle | types.MessageActionChatEditPhoto | types.MessageActionChatDeletePhoto | types.MessageActionChatAddUser | types.MessageActionChatDeleteUser | types.MessageActionChatJoinedByLink | types.MessageActionChannelCreate | types.MessageActionChatMigrateTo | types.MessageActionChannelMigrateFrom | types.MessageActionPinMessage | types.MessageActionHistoryClear | types.MessageActionGameScore | types.MessageActionPaymentSentMe | types.MessageActionPaymentSent | types.MessageActionPhoneCall | types.MessageActionScreenshotTaken | types.MessageActionCustomAction | types.MessageActionBotAllowed | types.MessageActionSecureValuesSentMe | types.MessageActionSecureValuesSent | types.MessageActionContactSignUp | types.MessageActionGeoProximityReached | types.MessageActionGroupCall | types.MessageActionInviteToGroupCall | types.MessageActionSetMessagesTtl | types.MessageActionGroupCallScheduled | types.MessageActionSetChatTheme | types.MessageActionChatJoinedByRequest | types.MessageActionWebViewDataSentMe | types.MessageActionWebViewDataSent | types.MessageActionGiftPremium | types.MessageActionTopicCreate | types.MessageActionTopicEdit | types.MessageActionSuggestProfilePhoto | types.MessageActionRequestedPeer | types.MessageActionSetChatWallPaper | types.MessageActionGiftCode | types.MessageActionGiveawayLaunch | types.MessageActionGiveawayResults | types.MessageActionBoostApply | types.MessageActionRequestedPeerSentMe | types.MessageActionPaymentRefunded | types.MessageActionGiftStars | types.MessageActionPrizeStars | types.MessageActionStarGift | types.MessageActionStarGiftUnique | types.MessageActionPaidMessagesRefunded | types.MessageActionPaidMessagesPrice | types.MessageActionConferenceCall | types.MessageActionTodoCompletions | types.MessageActionTodoAppendTasks | types.MessageActionSuggestedPostApproval | types.MessageActionSuggestedPostSuccess | types.MessageActionSuggestedPostRefund | types.MessageActionGiftTon | types.MessageActionSuggestBirthday | types.MessageActionStarGiftPurchaseOffer | types.MessageActionStarGiftPurchaseOfferDeclined,
        reactions: Optional[types.MessageReactions],
        ttl_period: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaEmpty(TLObject):
    """
    [Read `messageMediaEmpty` docs](https://core.telegram.org/constructor/messageMediaEmpty).

    Generated from the following TL definition:
    ```tl
    messageMediaEmpty#3ded6320 = MessageMedia
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaPhoto(TLObject):
    """
    [Read `messageMediaPhoto` docs](https://core.telegram.org/constructor/messageMediaPhoto).

    Generated from the following TL definition:
    ```tl
    messageMediaPhoto#695150d7 flags:# spoiler:flags.3?true photo:flags.0?Photo ttl_seconds:flags.2?int = MessageMedia
    ```
    """
    def __new__(
        cls,
        spoiler: bool,
        photo: Optional[types.PhotoEmpty | types.Photo],
        ttl_seconds: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaGeo(TLObject):
    """
    [Read `messageMediaGeo` docs](https://core.telegram.org/constructor/messageMediaGeo).

    Generated from the following TL definition:
    ```tl
    messageMediaGeo#56e0d474 geo:GeoPoint = MessageMedia
    ```
    """
    def __new__(
        cls,
        geo: types.GeoPointEmpty | types.GeoPoint,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaContact(TLObject):
    """
    [Read `messageMediaContact` docs](https://core.telegram.org/constructor/messageMediaContact).

    Generated from the following TL definition:
    ```tl
    messageMediaContact#70322949 phone_number:string first_name:string last_name:string vcard:string user_id:long = MessageMedia
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        first_name: str,
        last_name: str,
        vcard: str,
        user_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaUnsupported(TLObject):
    """
    [Read `messageMediaUnsupported` docs](https://core.telegram.org/constructor/messageMediaUnsupported).

    Generated from the following TL definition:
    ```tl
    messageMediaUnsupported#9f84f49e = MessageMedia
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaDocument(TLObject):
    """
    [Read `messageMediaDocument` docs](https://core.telegram.org/constructor/messageMediaDocument).

    Generated from the following TL definition:
    ```tl
    messageMediaDocument#52d8ccd9 flags:# nopremium:flags.3?true spoiler:flags.4?true video:flags.6?true round:flags.7?true voice:flags.8?true document:flags.0?Document alt_documents:flags.5?Vector<Document> video_cover:flags.9?Photo video_timestamp:flags.10?int ttl_seconds:flags.2?int = MessageMedia
    ```
    """
    def __new__(
        cls,
        nopremium: bool,
        spoiler: bool,
        video: bool,
        round: bool,
        voice: bool,
        document: Optional[types.DocumentEmpty | types.Document],
        alt_documents: Optional[Sequence[types.DocumentEmpty | types.Document]],
        video_cover: Optional[types.PhotoEmpty | types.Photo],
        video_timestamp: Optional[int],
        ttl_seconds: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaWebPage(TLObject):
    """
    [Read `messageMediaWebPage` docs](https://core.telegram.org/constructor/messageMediaWebPage).

    Generated from the following TL definition:
    ```tl
    messageMediaWebPage#ddf10c3b flags:# force_large_media:flags.0?true force_small_media:flags.1?true manual:flags.3?true safe:flags.4?true webpage:WebPage = MessageMedia
    ```
    """
    def __new__(
        cls,
        force_large_media: bool,
        force_small_media: bool,
        manual: bool,
        safe: bool,
        webpage: types.WebPageEmpty | types.WebPagePending | types.WebPage | types.WebPageNotModified,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaVenue(TLObject):
    """
    [Read `messageMediaVenue` docs](https://core.telegram.org/constructor/messageMediaVenue).

    Generated from the following TL definition:
    ```tl
    messageMediaVenue#2ec0533f geo:GeoPoint title:string address:string provider:string venue_id:string venue_type:string = MessageMedia
    ```
    """
    def __new__(
        cls,
        geo: types.GeoPointEmpty | types.GeoPoint,
        title: str,
        address: str,
        provider: str,
        venue_id: str,
        venue_type: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaGame(TLObject):
    """
    [Read `messageMediaGame` docs](https://core.telegram.org/constructor/messageMediaGame).

    Generated from the following TL definition:
    ```tl
    messageMediaGame#fdb19008 game:Game = MessageMedia
    ```
    """
    def __new__(
        cls,
        game: types.Game,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaInvoice(TLObject):
    """
    [Read `messageMediaInvoice` docs](https://core.telegram.org/constructor/messageMediaInvoice).

    Generated from the following TL definition:
    ```tl
    messageMediaInvoice#f6a548d3 flags:# shipping_address_requested:flags.1?true test:flags.3?true title:string description:string photo:flags.0?WebDocument receipt_msg_id:flags.2?int currency:string total_amount:long start_param:string extended_media:flags.4?MessageExtendedMedia = MessageMedia
    ```
    """
    def __new__(
        cls,
        shipping_address_requested: bool,
        test: bool,
        title: str,
        description: str,
        photo: Optional[types.WebDocument | types.WebDocumentNoProxy],
        receipt_msg_id: Optional[int],
        currency: str,
        total_amount: int,
        start_param: str,
        extended_media: Optional[types.MessageExtendedMediaPreview | types.MessageExtendedMedia],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaGeoLive(TLObject):
    """
    [Read `messageMediaGeoLive` docs](https://core.telegram.org/constructor/messageMediaGeoLive).

    Generated from the following TL definition:
    ```tl
    messageMediaGeoLive#b940c666 flags:# geo:GeoPoint heading:flags.0?int period:int proximity_notification_radius:flags.1?int = MessageMedia
    ```
    """
    def __new__(
        cls,
        geo: types.GeoPointEmpty | types.GeoPoint,
        heading: Optional[int],
        period: int,
        proximity_notification_radius: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaPoll(TLObject):
    """
    [Read `messageMediaPoll` docs](https://core.telegram.org/constructor/messageMediaPoll).

    Generated from the following TL definition:
    ```tl
    messageMediaPoll#4bd6e798 poll:Poll results:PollResults = MessageMedia
    ```
    """
    def __new__(
        cls,
        poll: types.Poll,
        results: types.PollResults,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaDice(TLObject):
    """
    [Read `messageMediaDice` docs](https://core.telegram.org/constructor/messageMediaDice).

    Generated from the following TL definition:
    ```tl
    messageMediaDice#8cbec07 flags:# value:int emoticon:string game_outcome:flags.0?messages.EmojiGameOutcome = MessageMedia
    ```
    """
    def __new__(
        cls,
        value: int,
        emoticon: str,
        game_outcome: Optional[types.messages.EmojiGameOutcome],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaStory(TLObject):
    """
    [Read `messageMediaStory` docs](https://core.telegram.org/constructor/messageMediaStory).

    Generated from the following TL definition:
    ```tl
    messageMediaStory#68cb6283 flags:# via_mention:flags.1?true peer:Peer id:int story:flags.0?StoryItem = MessageMedia
    ```
    """
    def __new__(
        cls,
        via_mention: bool,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        id: int,
        story: Optional[types.StoryItemDeleted | types.StoryItemSkipped | types.StoryItem],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaGiveaway(TLObject):
    """
    [Read `messageMediaGiveaway` docs](https://core.telegram.org/constructor/messageMediaGiveaway).

    Generated from the following TL definition:
    ```tl
    messageMediaGiveaway#aa073beb flags:# only_new_subscribers:flags.0?true winners_are_visible:flags.2?true channels:Vector<long> countries_iso2:flags.1?Vector<string> prize_description:flags.3?string quantity:int months:flags.4?int stars:flags.5?long until_date:int = MessageMedia
    ```
    """
    def __new__(
        cls,
        only_new_subscribers: bool,
        winners_are_visible: bool,
        channels: Sequence[int],
        countries_iso2: Optional[Sequence[str]],
        prize_description: Optional[str],
        quantity: int,
        months: Optional[int],
        stars: Optional[int],
        until_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaGiveawayResults(TLObject):
    """
    [Read `messageMediaGiveawayResults` docs](https://core.telegram.org/constructor/messageMediaGiveawayResults).

    Generated from the following TL definition:
    ```tl
    messageMediaGiveawayResults#ceaa3ea1 flags:# only_new_subscribers:flags.0?true refunded:flags.2?true channel_id:long additional_peers_count:flags.3?int launch_msg_id:int winners_count:int unclaimed_count:int winners:Vector<long> months:flags.4?int stars:flags.5?long prize_description:flags.1?string until_date:int = MessageMedia
    ```
    """
    def __new__(
        cls,
        only_new_subscribers: bool,
        refunded: bool,
        channel_id: int,
        additional_peers_count: Optional[int],
        launch_msg_id: int,
        winners_count: int,
        unclaimed_count: int,
        winners: Sequence[int],
        months: Optional[int],
        stars: Optional[int],
        prize_description: Optional[str],
        until_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaPaidMedia(TLObject):
    """
    [Read `messageMediaPaidMedia` docs](https://core.telegram.org/constructor/messageMediaPaidMedia).

    Generated from the following TL definition:
    ```tl
    messageMediaPaidMedia#a8852491 stars_amount:long extended_media:Vector<MessageExtendedMedia> = MessageMedia
    ```
    """
    def __new__(
        cls,
        stars_amount: int,
        extended_media: Sequence[types.MessageExtendedMediaPreview | types.MessageExtendedMedia],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaToDo(TLObject):
    """
    [Read `messageMediaToDo` docs](https://core.telegram.org/constructor/messageMediaToDo).

    Generated from the following TL definition:
    ```tl
    messageMediaToDo#8a53b014 flags:# todo:TodoList completions:flags.0?Vector<TodoCompletion> = MessageMedia
    ```
    """
    def __new__(
        cls,
        todo: types.TodoList,
        completions: Optional[Sequence[types.TodoCompletion]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageMediaVideoStream(TLObject):
    """
    [Read `messageMediaVideoStream` docs](https://core.telegram.org/constructor/messageMediaVideoStream).

    Generated from the following TL definition:
    ```tl
    messageMediaVideoStream#ca5cab89 flags:# rtmp_stream:flags.0?true call:InputGroupCall = MessageMedia
    ```
    """
    def __new__(
        cls,
        rtmp_stream: bool,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionEmpty(TLObject):
    """
    [Read `messageActionEmpty` docs](https://core.telegram.org/constructor/messageActionEmpty).

    Generated from the following TL definition:
    ```tl
    messageActionEmpty#b6aef7b0 = MessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionChatCreate(TLObject):
    """
    [Read `messageActionChatCreate` docs](https://core.telegram.org/constructor/messageActionChatCreate).

    Generated from the following TL definition:
    ```tl
    messageActionChatCreate#bd47cbad title:string users:Vector<long> = MessageAction
    ```
    """
    def __new__(
        cls,
        title: str,
        users: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionChatEditTitle(TLObject):
    """
    [Read `messageActionChatEditTitle` docs](https://core.telegram.org/constructor/messageActionChatEditTitle).

    Generated from the following TL definition:
    ```tl
    messageActionChatEditTitle#b5a1ce5a title:string = MessageAction
    ```
    """
    def __new__(
        cls,
        title: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionChatEditPhoto(TLObject):
    """
    [Read `messageActionChatEditPhoto` docs](https://core.telegram.org/constructor/messageActionChatEditPhoto).

    Generated from the following TL definition:
    ```tl
    messageActionChatEditPhoto#7fcb13a8 photo:Photo = MessageAction
    ```
    """
    def __new__(
        cls,
        photo: types.PhotoEmpty | types.Photo,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionChatDeletePhoto(TLObject):
    """
    [Read `messageActionChatDeletePhoto` docs](https://core.telegram.org/constructor/messageActionChatDeletePhoto).

    Generated from the following TL definition:
    ```tl
    messageActionChatDeletePhoto#95e3fbef = MessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionChatAddUser(TLObject):
    """
    [Read `messageActionChatAddUser` docs](https://core.telegram.org/constructor/messageActionChatAddUser).

    Generated from the following TL definition:
    ```tl
    messageActionChatAddUser#15cefd00 users:Vector<long> = MessageAction
    ```
    """
    def __new__(
        cls,
        users: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionChatDeleteUser(TLObject):
    """
    [Read `messageActionChatDeleteUser` docs](https://core.telegram.org/constructor/messageActionChatDeleteUser).

    Generated from the following TL definition:
    ```tl
    messageActionChatDeleteUser#a43f30cc user_id:long = MessageAction
    ```
    """
    def __new__(
        cls,
        user_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionChatJoinedByLink(TLObject):
    """
    [Read `messageActionChatJoinedByLink` docs](https://core.telegram.org/constructor/messageActionChatJoinedByLink).

    Generated from the following TL definition:
    ```tl
    messageActionChatJoinedByLink#31224c3 inviter_id:long = MessageAction
    ```
    """
    def __new__(
        cls,
        inviter_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionChannelCreate(TLObject):
    """
    [Read `messageActionChannelCreate` docs](https://core.telegram.org/constructor/messageActionChannelCreate).

    Generated from the following TL definition:
    ```tl
    messageActionChannelCreate#95d2ac92 title:string = MessageAction
    ```
    """
    def __new__(
        cls,
        title: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionChatMigrateTo(TLObject):
    """
    [Read `messageActionChatMigrateTo` docs](https://core.telegram.org/constructor/messageActionChatMigrateTo).

    Generated from the following TL definition:
    ```tl
    messageActionChatMigrateTo#e1037f92 channel_id:long = MessageAction
    ```
    """
    def __new__(
        cls,
        channel_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionChannelMigrateFrom(TLObject):
    """
    [Read `messageActionChannelMigrateFrom` docs](https://core.telegram.org/constructor/messageActionChannelMigrateFrom).

    Generated from the following TL definition:
    ```tl
    messageActionChannelMigrateFrom#ea3948e9 title:string chat_id:long = MessageAction
    ```
    """
    def __new__(
        cls,
        title: str,
        chat_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionPinMessage(TLObject):
    """
    [Read `messageActionPinMessage` docs](https://core.telegram.org/constructor/messageActionPinMessage).

    Generated from the following TL definition:
    ```tl
    messageActionPinMessage#94bd38ed = MessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionHistoryClear(TLObject):
    """
    [Read `messageActionHistoryClear` docs](https://core.telegram.org/constructor/messageActionHistoryClear).

    Generated from the following TL definition:
    ```tl
    messageActionHistoryClear#9fbab604 = MessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionGameScore(TLObject):
    """
    [Read `messageActionGameScore` docs](https://core.telegram.org/constructor/messageActionGameScore).

    Generated from the following TL definition:
    ```tl
    messageActionGameScore#92a72876 game_id:long score:int = MessageAction
    ```
    """
    def __new__(
        cls,
        game_id: int,
        score: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionPaymentSentMe(TLObject):
    """
    [Read `messageActionPaymentSentMe` docs](https://core.telegram.org/constructor/messageActionPaymentSentMe).

    Generated from the following TL definition:
    ```tl
    messageActionPaymentSentMe#ffa00ccc flags:# recurring_init:flags.2?true recurring_used:flags.3?true currency:string total_amount:long payload:bytes info:flags.0?PaymentRequestedInfo shipping_option_id:flags.1?string charge:PaymentCharge subscription_until_date:flags.4?int = MessageAction
    ```
    """
    def __new__(
        cls,
        recurring_init: bool,
        recurring_used: bool,
        currency: str,
        total_amount: int,
        payload: bytes,
        info: Optional[types.PaymentRequestedInfo],
        shipping_option_id: Optional[str],
        charge: types.PaymentCharge,
        subscription_until_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionPaymentSent(TLObject):
    """
    [Read `messageActionPaymentSent` docs](https://core.telegram.org/constructor/messageActionPaymentSent).

    Generated from the following TL definition:
    ```tl
    messageActionPaymentSent#c624b16e flags:# recurring_init:flags.2?true recurring_used:flags.3?true currency:string total_amount:long invoice_slug:flags.0?string subscription_until_date:flags.4?int = MessageAction
    ```
    """
    def __new__(
        cls,
        recurring_init: bool,
        recurring_used: bool,
        currency: str,
        total_amount: int,
        invoice_slug: Optional[str],
        subscription_until_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionPhoneCall(TLObject):
    """
    [Read `messageActionPhoneCall` docs](https://core.telegram.org/constructor/messageActionPhoneCall).

    Generated from the following TL definition:
    ```tl
    messageActionPhoneCall#80e11a7f flags:# video:flags.2?true call_id:long reason:flags.0?PhoneCallDiscardReason duration:flags.1?int = MessageAction
    ```
    """
    def __new__(
        cls,
        video: bool,
        call_id: int,
        reason: Optional[types.PhoneCallDiscardReasonMissed | types.PhoneCallDiscardReasonDisconnect | types.PhoneCallDiscardReasonHangup | types.PhoneCallDiscardReasonBusy | types.PhoneCallDiscardReasonMigrateConferenceCall],
        duration: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionScreenshotTaken(TLObject):
    """
    [Read `messageActionScreenshotTaken` docs](https://core.telegram.org/constructor/messageActionScreenshotTaken).

    Generated from the following TL definition:
    ```tl
    messageActionScreenshotTaken#4792929b = MessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionCustomAction(TLObject):
    """
    [Read `messageActionCustomAction` docs](https://core.telegram.org/constructor/messageActionCustomAction).

    Generated from the following TL definition:
    ```tl
    messageActionCustomAction#fae69f56 message:string = MessageAction
    ```
    """
    def __new__(
        cls,
        message: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionBotAllowed(TLObject):
    """
    [Read `messageActionBotAllowed` docs](https://core.telegram.org/constructor/messageActionBotAllowed).

    Generated from the following TL definition:
    ```tl
    messageActionBotAllowed#c516d679 flags:# attach_menu:flags.1?true from_request:flags.3?true domain:flags.0?string app:flags.2?BotApp = MessageAction
    ```
    """
    def __new__(
        cls,
        attach_menu: bool,
        from_request: bool,
        domain: Optional[str],
        app: Optional[types.BotAppNotModified | types.BotApp],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionSecureValuesSentMe(TLObject):
    """
    [Read `messageActionSecureValuesSentMe` docs](https://core.telegram.org/constructor/messageActionSecureValuesSentMe).

    Generated from the following TL definition:
    ```tl
    messageActionSecureValuesSentMe#1b287353 values:Vector<SecureValue> credentials:SecureCredentialsEncrypted = MessageAction
    ```
    """
    def __new__(
        cls,
        values: Sequence[types.SecureValue],
        credentials: types.SecureCredentialsEncrypted,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionSecureValuesSent(TLObject):
    """
    [Read `messageActionSecureValuesSent` docs](https://core.telegram.org/constructor/messageActionSecureValuesSent).

    Generated from the following TL definition:
    ```tl
    messageActionSecureValuesSent#d95c6154 types:Vector<SecureValueType> = MessageAction
    ```
    """
    def __new__(
        cls,
        types: Sequence[types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionContactSignUp(TLObject):
    """
    [Read `messageActionContactSignUp` docs](https://core.telegram.org/constructor/messageActionContactSignUp).

    Generated from the following TL definition:
    ```tl
    messageActionContactSignUp#f3f25f76 = MessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionGeoProximityReached(TLObject):
    """
    [Read `messageActionGeoProximityReached` docs](https://core.telegram.org/constructor/messageActionGeoProximityReached).

    Generated from the following TL definition:
    ```tl
    messageActionGeoProximityReached#98e0d697 from_id:Peer to_id:Peer distance:int = MessageAction
    ```
    """
    def __new__(
        cls,
        from_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        to_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        distance: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionGroupCall(TLObject):
    """
    [Read `messageActionGroupCall` docs](https://core.telegram.org/constructor/messageActionGroupCall).

    Generated from the following TL definition:
    ```tl
    messageActionGroupCall#7a0d7f42 flags:# call:InputGroupCall duration:flags.0?int = MessageAction
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        duration: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionInviteToGroupCall(TLObject):
    """
    [Read `messageActionInviteToGroupCall` docs](https://core.telegram.org/constructor/messageActionInviteToGroupCall).

    Generated from the following TL definition:
    ```tl
    messageActionInviteToGroupCall#502f92f7 call:InputGroupCall users:Vector<long> = MessageAction
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        users: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionSetMessagesTtl(TLObject):
    """
    [Read `messageActionSetMessagesTTL` docs](https://core.telegram.org/constructor/messageActionSetMessagesTTL).

    Generated from the following TL definition:
    ```tl
    messageActionSetMessagesTTL#3c134d7b flags:# period:int auto_setting_from:flags.0?long = MessageAction
    ```
    """
    def __new__(
        cls,
        period: int,
        auto_setting_from: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionGroupCallScheduled(TLObject):
    """
    [Read `messageActionGroupCallScheduled` docs](https://core.telegram.org/constructor/messageActionGroupCallScheduled).

    Generated from the following TL definition:
    ```tl
    messageActionGroupCallScheduled#b3a07661 call:InputGroupCall schedule_date:int = MessageAction
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        schedule_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionSetChatTheme(TLObject):
    """
    [Read `messageActionSetChatTheme` docs](https://core.telegram.org/constructor/messageActionSetChatTheme).

    Generated from the following TL definition:
    ```tl
    messageActionSetChatTheme#b91bbd3a theme:ChatTheme = MessageAction
    ```
    """
    def __new__(
        cls,
        theme: types.ChatTheme | types.ChatThemeUniqueGift,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionChatJoinedByRequest(TLObject):
    """
    [Read `messageActionChatJoinedByRequest` docs](https://core.telegram.org/constructor/messageActionChatJoinedByRequest).

    Generated from the following TL definition:
    ```tl
    messageActionChatJoinedByRequest#ebbca3cb = MessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionWebViewDataSentMe(TLObject):
    """
    [Read `messageActionWebViewDataSentMe` docs](https://core.telegram.org/constructor/messageActionWebViewDataSentMe).

    Generated from the following TL definition:
    ```tl
    messageActionWebViewDataSentMe#47dd8079 text:string data:string = MessageAction
    ```
    """
    def __new__(
        cls,
        text: str,
        data: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionWebViewDataSent(TLObject):
    """
    [Read `messageActionWebViewDataSent` docs](https://core.telegram.org/constructor/messageActionWebViewDataSent).

    Generated from the following TL definition:
    ```tl
    messageActionWebViewDataSent#b4c38cb5 text:string = MessageAction
    ```
    """
    def __new__(
        cls,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionGiftPremium(TLObject):
    """
    [Read `messageActionGiftPremium` docs](https://core.telegram.org/constructor/messageActionGiftPremium).

    Generated from the following TL definition:
    ```tl
    messageActionGiftPremium#48e91302 flags:# currency:string amount:long days:int crypto_currency:flags.0?string crypto_amount:flags.0?long message:flags.1?TextWithEntities = MessageAction
    ```
    """
    def __new__(
        cls,
        currency: str,
        amount: int,
        days: int,
        crypto_currency: Optional[str],
        crypto_amount: Optional[int],
        message: Optional[types.TextWithEntities],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionTopicCreate(TLObject):
    """
    [Read `messageActionTopicCreate` docs](https://core.telegram.org/constructor/messageActionTopicCreate).

    Generated from the following TL definition:
    ```tl
    messageActionTopicCreate#d999256 flags:# title_missing:flags.1?true title:string icon_color:int icon_emoji_id:flags.0?long = MessageAction
    ```
    """
    def __new__(
        cls,
        title_missing: bool,
        title: str,
        icon_color: int,
        icon_emoji_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionTopicEdit(TLObject):
    """
    [Read `messageActionTopicEdit` docs](https://core.telegram.org/constructor/messageActionTopicEdit).

    Generated from the following TL definition:
    ```tl
    messageActionTopicEdit#c0944820 flags:# title:flags.0?string icon_emoji_id:flags.1?long closed:flags.2?Bool hidden:flags.3?Bool = MessageAction
    ```
    """
    def __new__(
        cls,
        title: Optional[str],
        icon_emoji_id: Optional[int],
        closed: Optional[bool],
        hidden: Optional[bool],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionSuggestProfilePhoto(TLObject):
    """
    [Read `messageActionSuggestProfilePhoto` docs](https://core.telegram.org/constructor/messageActionSuggestProfilePhoto).

    Generated from the following TL definition:
    ```tl
    messageActionSuggestProfilePhoto#57de635e photo:Photo = MessageAction
    ```
    """
    def __new__(
        cls,
        photo: types.PhotoEmpty | types.Photo,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionRequestedPeer(TLObject):
    """
    [Read `messageActionRequestedPeer` docs](https://core.telegram.org/constructor/messageActionRequestedPeer).

    Generated from the following TL definition:
    ```tl
    messageActionRequestedPeer#31518e9b button_id:int peers:Vector<Peer> = MessageAction
    ```
    """
    def __new__(
        cls,
        button_id: int,
        peers: Sequence[types.PeerUser | types.PeerChat | types.PeerChannel],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionSetChatWallPaper(TLObject):
    """
    [Read `messageActionSetChatWallPaper` docs](https://core.telegram.org/constructor/messageActionSetChatWallPaper).

    Generated from the following TL definition:
    ```tl
    messageActionSetChatWallPaper#5060a3f4 flags:# same:flags.0?true for_both:flags.1?true wallpaper:WallPaper = MessageAction
    ```
    """
    def __new__(
        cls,
        same: bool,
        for_both: bool,
        wallpaper: types.WallPaper | types.WallPaperNoFile,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionGiftCode(TLObject):
    """
    [Read `messageActionGiftCode` docs](https://core.telegram.org/constructor/messageActionGiftCode).

    Generated from the following TL definition:
    ```tl
    messageActionGiftCode#31c48347 flags:# via_giveaway:flags.0?true unclaimed:flags.5?true boost_peer:flags.1?Peer days:int slug:string currency:flags.2?string amount:flags.2?long crypto_currency:flags.3?string crypto_amount:flags.3?long message:flags.4?TextWithEntities = MessageAction
    ```
    """
    def __new__(
        cls,
        via_giveaway: bool,
        unclaimed: bool,
        boost_peer: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        days: int,
        slug: str,
        currency: Optional[str],
        amount: Optional[int],
        crypto_currency: Optional[str],
        crypto_amount: Optional[int],
        message: Optional[types.TextWithEntities],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionGiveawayLaunch(TLObject):
    """
    [Read `messageActionGiveawayLaunch` docs](https://core.telegram.org/constructor/messageActionGiveawayLaunch).

    Generated from the following TL definition:
    ```tl
    messageActionGiveawayLaunch#a80f51e4 flags:# stars:flags.0?long = MessageAction
    ```
    """
    def __new__(
        cls,
        stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionGiveawayResults(TLObject):
    """
    [Read `messageActionGiveawayResults` docs](https://core.telegram.org/constructor/messageActionGiveawayResults).

    Generated from the following TL definition:
    ```tl
    messageActionGiveawayResults#87e2f155 flags:# stars:flags.0?true winners_count:int unclaimed_count:int = MessageAction
    ```
    """
    def __new__(
        cls,
        stars: bool,
        winners_count: int,
        unclaimed_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionBoostApply(TLObject):
    """
    [Read `messageActionBoostApply` docs](https://core.telegram.org/constructor/messageActionBoostApply).

    Generated from the following TL definition:
    ```tl
    messageActionBoostApply#cc02aa6d boosts:int = MessageAction
    ```
    """
    def __new__(
        cls,
        boosts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionRequestedPeerSentMe(TLObject):
    """
    [Read `messageActionRequestedPeerSentMe` docs](https://core.telegram.org/constructor/messageActionRequestedPeerSentMe).

    Generated from the following TL definition:
    ```tl
    messageActionRequestedPeerSentMe#93b31848 button_id:int peers:Vector<RequestedPeer> = MessageAction
    ```
    """
    def __new__(
        cls,
        button_id: int,
        peers: Sequence[types.RequestedPeerUser | types.RequestedPeerChat | types.RequestedPeerChannel],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionPaymentRefunded(TLObject):
    """
    [Read `messageActionPaymentRefunded` docs](https://core.telegram.org/constructor/messageActionPaymentRefunded).

    Generated from the following TL definition:
    ```tl
    messageActionPaymentRefunded#41b3e202 flags:# peer:Peer currency:string total_amount:long payload:flags.0?bytes charge:PaymentCharge = MessageAction
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        currency: str,
        total_amount: int,
        payload: Optional[bytes],
        charge: types.PaymentCharge,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionGiftStars(TLObject):
    """
    [Read `messageActionGiftStars` docs](https://core.telegram.org/constructor/messageActionGiftStars).

    Generated from the following TL definition:
    ```tl
    messageActionGiftStars#45d5b021 flags:# currency:string amount:long stars:long crypto_currency:flags.0?string crypto_amount:flags.0?long transaction_id:flags.1?string = MessageAction
    ```
    """
    def __new__(
        cls,
        currency: str,
        amount: int,
        stars: int,
        crypto_currency: Optional[str],
        crypto_amount: Optional[int],
        transaction_id: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionPrizeStars(TLObject):
    """
    [Read `messageActionPrizeStars` docs](https://core.telegram.org/constructor/messageActionPrizeStars).

    Generated from the following TL definition:
    ```tl
    messageActionPrizeStars#b00c47a2 flags:# unclaimed:flags.0?true stars:long transaction_id:string boost_peer:Peer giveaway_msg_id:int = MessageAction
    ```
    """
    def __new__(
        cls,
        unclaimed: bool,
        stars: int,
        transaction_id: str,
        boost_peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        giveaway_msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionStarGift(TLObject):
    """
    [Read `messageActionStarGift` docs](https://core.telegram.org/constructor/messageActionStarGift).

    Generated from the following TL definition:
    ```tl
    messageActionStarGift#ea2c31d3 flags:# name_hidden:flags.0?true saved:flags.2?true converted:flags.3?true upgraded:flags.5?true refunded:flags.9?true can_upgrade:flags.10?true prepaid_upgrade:flags.13?true upgrade_separate:flags.16?true auction_acquired:flags.17?true gift:StarGift message:flags.1?TextWithEntities convert_stars:flags.4?long upgrade_msg_id:flags.5?int upgrade_stars:flags.8?long from_id:flags.11?Peer peer:flags.12?Peer saved_id:flags.12?long prepaid_upgrade_hash:flags.14?string gift_msg_id:flags.15?int to_id:flags.18?Peer gift_num:flags.19?int = MessageAction
    ```
    """
    def __new__(
        cls,
        name_hidden: bool,
        saved: bool,
        converted: bool,
        upgraded: bool,
        refunded: bool,
        can_upgrade: bool,
        prepaid_upgrade: bool,
        upgrade_separate: bool,
        auction_acquired: bool,
        gift: types.StarGift | types.StarGiftUnique,
        message: Optional[types.TextWithEntities],
        convert_stars: Optional[int],
        upgrade_msg_id: Optional[int],
        upgrade_stars: Optional[int],
        from_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        peer: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        saved_id: Optional[int],
        prepaid_upgrade_hash: Optional[str],
        gift_msg_id: Optional[int],
        to_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        gift_num: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionStarGiftUnique(TLObject):
    """
    [Read `messageActionStarGiftUnique` docs](https://core.telegram.org/constructor/messageActionStarGiftUnique).

    Generated from the following TL definition:
    ```tl
    messageActionStarGiftUnique#95728543 flags:# upgrade:flags.0?true transferred:flags.1?true saved:flags.2?true refunded:flags.5?true prepaid_upgrade:flags.11?true assigned:flags.13?true from_offer:flags.14?true gift:StarGift can_export_at:flags.3?int transfer_stars:flags.4?long from_id:flags.6?Peer peer:flags.7?Peer saved_id:flags.7?long resale_amount:flags.8?StarsAmount can_transfer_at:flags.9?int can_resell_at:flags.10?int drop_original_details_stars:flags.12?long = MessageAction
    ```
    """
    def __new__(
        cls,
        upgrade: bool,
        transferred: bool,
        saved: bool,
        refunded: bool,
        prepaid_upgrade: bool,
        assigned: bool,
        from_offer: bool,
        gift: types.StarGift | types.StarGiftUnique,
        can_export_at: Optional[int],
        transfer_stars: Optional[int],
        from_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        peer: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        saved_id: Optional[int],
        resale_amount: Optional[types.StarsAmount | types.StarsTonAmount],
        can_transfer_at: Optional[int],
        can_resell_at: Optional[int],
        drop_original_details_stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionPaidMessagesRefunded(TLObject):
    """
    [Read `messageActionPaidMessagesRefunded` docs](https://core.telegram.org/constructor/messageActionPaidMessagesRefunded).

    Generated from the following TL definition:
    ```tl
    messageActionPaidMessagesRefunded#ac1f1fcd count:int stars:long = MessageAction
    ```
    """
    def __new__(
        cls,
        count: int,
        stars: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionPaidMessagesPrice(TLObject):
    """
    [Read `messageActionPaidMessagesPrice` docs](https://core.telegram.org/constructor/messageActionPaidMessagesPrice).

    Generated from the following TL definition:
    ```tl
    messageActionPaidMessagesPrice#84b88578 flags:# broadcast_messages_allowed:flags.0?true stars:long = MessageAction
    ```
    """
    def __new__(
        cls,
        broadcast_messages_allowed: bool,
        stars: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionConferenceCall(TLObject):
    """
    [Read `messageActionConferenceCall` docs](https://core.telegram.org/constructor/messageActionConferenceCall).

    Generated from the following TL definition:
    ```tl
    messageActionConferenceCall#2ffe2f7a flags:# missed:flags.0?true active:flags.1?true video:flags.4?true call_id:long duration:flags.2?int other_participants:flags.3?Vector<Peer> = MessageAction
    ```
    """
    def __new__(
        cls,
        missed: bool,
        active: bool,
        video: bool,
        call_id: int,
        duration: Optional[int],
        other_participants: Optional[Sequence[types.PeerUser | types.PeerChat | types.PeerChannel]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionTodoCompletions(TLObject):
    """
    [Read `messageActionTodoCompletions` docs](https://core.telegram.org/constructor/messageActionTodoCompletions).

    Generated from the following TL definition:
    ```tl
    messageActionTodoCompletions#cc7c5c89 completed:Vector<int> incompleted:Vector<int> = MessageAction
    ```
    """
    def __new__(
        cls,
        completed: Sequence[int],
        incompleted: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionTodoAppendTasks(TLObject):
    """
    [Read `messageActionTodoAppendTasks` docs](https://core.telegram.org/constructor/messageActionTodoAppendTasks).

    Generated from the following TL definition:
    ```tl
    messageActionTodoAppendTasks#c7edbc83 list:Vector<TodoItem> = MessageAction
    ```
    """
    def __new__(
        cls,
        list: Sequence[types.TodoItem],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionSuggestedPostApproval(TLObject):
    """
    [Read `messageActionSuggestedPostApproval` docs](https://core.telegram.org/constructor/messageActionSuggestedPostApproval).

    Generated from the following TL definition:
    ```tl
    messageActionSuggestedPostApproval#ee7a1596 flags:# rejected:flags.0?true balance_too_low:flags.1?true reject_comment:flags.2?string schedule_date:flags.3?int price:flags.4?StarsAmount = MessageAction
    ```
    """
    def __new__(
        cls,
        rejected: bool,
        balance_too_low: bool,
        reject_comment: Optional[str],
        schedule_date: Optional[int],
        price: Optional[types.StarsAmount | types.StarsTonAmount],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionSuggestedPostSuccess(TLObject):
    """
    [Read `messageActionSuggestedPostSuccess` docs](https://core.telegram.org/constructor/messageActionSuggestedPostSuccess).

    Generated from the following TL definition:
    ```tl
    messageActionSuggestedPostSuccess#95ddcf69 price:StarsAmount = MessageAction
    ```
    """
    def __new__(
        cls,
        price: types.StarsAmount | types.StarsTonAmount,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionSuggestedPostRefund(TLObject):
    """
    [Read `messageActionSuggestedPostRefund` docs](https://core.telegram.org/constructor/messageActionSuggestedPostRefund).

    Generated from the following TL definition:
    ```tl
    messageActionSuggestedPostRefund#69f916f8 flags:# payer_initiated:flags.0?true = MessageAction
    ```
    """
    def __new__(
        cls,
        payer_initiated: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionGiftTon(TLObject):
    """
    [Read `messageActionGiftTon` docs](https://core.telegram.org/constructor/messageActionGiftTon).

    Generated from the following TL definition:
    ```tl
    messageActionGiftTon#a8a3c699 flags:# currency:string amount:long crypto_currency:string crypto_amount:long transaction_id:flags.0?string = MessageAction
    ```
    """
    def __new__(
        cls,
        currency: str,
        amount: int,
        crypto_currency: str,
        crypto_amount: int,
        transaction_id: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionSuggestBirthday(TLObject):
    """
    [Read `messageActionSuggestBirthday` docs](https://core.telegram.org/constructor/messageActionSuggestBirthday).

    Generated from the following TL definition:
    ```tl
    messageActionSuggestBirthday#2c8f2a25 birthday:Birthday = MessageAction
    ```
    """
    def __new__(
        cls,
        birthday: types.Birthday,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionStarGiftPurchaseOffer(TLObject):
    """
    [Read `messageActionStarGiftPurchaseOffer` docs](https://core.telegram.org/constructor/messageActionStarGiftPurchaseOffer).

    Generated from the following TL definition:
    ```tl
    messageActionStarGiftPurchaseOffer#774278d4 flags:# accepted:flags.0?true declined:flags.1?true gift:StarGift price:StarsAmount expires_at:int = MessageAction
    ```
    """
    def __new__(
        cls,
        accepted: bool,
        declined: bool,
        gift: types.StarGift | types.StarGiftUnique,
        price: types.StarsAmount | types.StarsTonAmount,
        expires_at: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageActionStarGiftPurchaseOfferDeclined(TLObject):
    """
    [Read `messageActionStarGiftPurchaseOfferDeclined` docs](https://core.telegram.org/constructor/messageActionStarGiftPurchaseOfferDeclined).

    Generated from the following TL definition:
    ```tl
    messageActionStarGiftPurchaseOfferDeclined#73ada76b flags:# expired:flags.0?true gift:StarGift price:StarsAmount = MessageAction
    ```
    """
    def __new__(
        cls,
        expired: bool,
        gift: types.StarGift | types.StarGiftUnique,
        price: types.StarsAmount | types.StarsTonAmount,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Dialog(TLObject):
    """
    [Read `dialog` docs](https://core.telegram.org/constructor/dialog).

    Generated from the following TL definition:
    ```tl
    dialog#d58a08c6 flags:# pinned:flags.2?true unread_mark:flags.3?true view_forum_as_messages:flags.6?true peer:Peer top_message:int read_inbox_max_id:int read_outbox_max_id:int unread_count:int unread_mentions_count:int unread_reactions_count:int notify_settings:PeerNotifySettings pts:flags.0?int draft:flags.1?DraftMessage folder_id:flags.4?int ttl_period:flags.5?int = Dialog
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        unread_mark: bool,
        view_forum_as_messages: bool,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        top_message: int,
        read_inbox_max_id: int,
        read_outbox_max_id: int,
        unread_count: int,
        unread_mentions_count: int,
        unread_reactions_count: int,
        notify_settings: types.PeerNotifySettings,
        pts: Optional[int],
        draft: Optional[types.DraftMessageEmpty | types.DraftMessage],
        folder_id: Optional[int],
        ttl_period: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DialogFolder(TLObject):
    """
    [Read `dialogFolder` docs](https://core.telegram.org/constructor/dialogFolder).

    Generated from the following TL definition:
    ```tl
    dialogFolder#71bd134c flags:# pinned:flags.2?true folder:Folder peer:Peer top_message:int unread_muted_peers_count:int unread_unmuted_peers_count:int unread_muted_messages_count:int unread_unmuted_messages_count:int = Dialog
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        folder: types.Folder,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        top_message: int,
        unread_muted_peers_count: int,
        unread_unmuted_peers_count: int,
        unread_muted_messages_count: int,
        unread_unmuted_messages_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhotoEmpty(TLObject):
    """
    [Read `photoEmpty` docs](https://core.telegram.org/constructor/photoEmpty).

    Generated from the following TL definition:
    ```tl
    photoEmpty#2331b22d id:long = Photo
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Photo(TLObject):
    """
    [Read `photo` docs](https://core.telegram.org/constructor/photo).

    Generated from the following TL definition:
    ```tl
    photo#fb197a65 flags:# has_stickers:flags.0?true id:long access_hash:long file_reference:bytes date:int sizes:Vector<PhotoSize> video_sizes:flags.1?Vector<VideoSize> dc_id:int = Photo
    ```
    """
    def __new__(
        cls,
        has_stickers: bool,
        id: int,
        access_hash: int,
        file_reference: bytes,
        date: int,
        sizes: Sequence[types.PhotoSizeEmpty | types.PhotoSize | types.PhotoCachedSize | types.PhotoStrippedSize | types.PhotoSizeProgressive | types.PhotoPathSize],
        video_sizes: Optional[Sequence[types.VideoSize | types.VideoSizeEmojiMarkup | types.VideoSizeStickerMarkup]],
        dc_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhotoSizeEmpty(TLObject):
    """
    [Read `photoSizeEmpty` docs](https://core.telegram.org/constructor/photoSizeEmpty).

    Generated from the following TL definition:
    ```tl
    photoSizeEmpty#e17e23c type:string = PhotoSize
    ```
    """
    def __new__(
        cls,
        type: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhotoSize(TLObject):
    """
    [Read `photoSize` docs](https://core.telegram.org/constructor/photoSize).

    Generated from the following TL definition:
    ```tl
    photoSize#75c78e60 type:string w:int h:int size:int = PhotoSize
    ```
    """
    def __new__(
        cls,
        type: str,
        w: int,
        h: int,
        size: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhotoCachedSize(TLObject):
    """
    [Read `photoCachedSize` docs](https://core.telegram.org/constructor/photoCachedSize).

    Generated from the following TL definition:
    ```tl
    photoCachedSize#21e1ad6 type:string w:int h:int bytes:bytes = PhotoSize
    ```
    """
    def __new__(
        cls,
        type: str,
        w: int,
        h: int,
        bytes: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhotoStrippedSize(TLObject):
    """
    [Read `photoStrippedSize` docs](https://core.telegram.org/constructor/photoStrippedSize).

    Generated from the following TL definition:
    ```tl
    photoStrippedSize#e0b0bc2e type:string bytes:bytes = PhotoSize
    ```
    """
    def __new__(
        cls,
        type: str,
        bytes: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhotoSizeProgressive(TLObject):
    """
    [Read `photoSizeProgressive` docs](https://core.telegram.org/constructor/photoSizeProgressive).

    Generated from the following TL definition:
    ```tl
    photoSizeProgressive#fa3efb95 type:string w:int h:int sizes:Vector<int> = PhotoSize
    ```
    """
    def __new__(
        cls,
        type: str,
        w: int,
        h: int,
        sizes: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhotoPathSize(TLObject):
    """
    [Read `photoPathSize` docs](https://core.telegram.org/constructor/photoPathSize).

    Generated from the following TL definition:
    ```tl
    photoPathSize#d8214d41 type:string bytes:bytes = PhotoSize
    ```
    """
    def __new__(
        cls,
        type: str,
        bytes: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GeoPointEmpty(TLObject):
    """
    [Read `geoPointEmpty` docs](https://core.telegram.org/constructor/geoPointEmpty).

    Generated from the following TL definition:
    ```tl
    geoPointEmpty#1117dd5f = GeoPoint
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GeoPoint(TLObject):
    """
    [Read `geoPoint` docs](https://core.telegram.org/constructor/geoPoint).

    Generated from the following TL definition:
    ```tl
    geoPoint#b2a2f663 flags:# long:double lat:double access_hash:long accuracy_radius:flags.0?int = GeoPoint
    ```
    """
    def __new__(
        cls,
        long: float,
        lat: float,
        access_hash: int,
        accuracy_radius: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputNotifyPeer(TLObject):
    """
    [Read `inputNotifyPeer` docs](https://core.telegram.org/constructor/inputNotifyPeer).

    Generated from the following TL definition:
    ```tl
    inputNotifyPeer#b8bc5b0c peer:InputPeer = InputNotifyPeer
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputNotifyUsers(TLObject):
    """
    [Read `inputNotifyUsers` docs](https://core.telegram.org/constructor/inputNotifyUsers).

    Generated from the following TL definition:
    ```tl
    inputNotifyUsers#193b4417 = InputNotifyPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputNotifyChats(TLObject):
    """
    [Read `inputNotifyChats` docs](https://core.telegram.org/constructor/inputNotifyChats).

    Generated from the following TL definition:
    ```tl
    inputNotifyChats#4a95e84e = InputNotifyPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputNotifyBroadcasts(TLObject):
    """
    [Read `inputNotifyBroadcasts` docs](https://core.telegram.org/constructor/inputNotifyBroadcasts).

    Generated from the following TL definition:
    ```tl
    inputNotifyBroadcasts#b1db7c7e = InputNotifyPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputNotifyForumTopic(TLObject):
    """
    [Read `inputNotifyForumTopic` docs](https://core.telegram.org/constructor/inputNotifyForumTopic).

    Generated from the following TL definition:
    ```tl
    inputNotifyForumTopic#5c467992 peer:InputPeer top_msg_id:int = InputNotifyPeer
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        top_msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPeerNotifySettings(TLObject):
    """
    [Read `inputPeerNotifySettings` docs](https://core.telegram.org/constructor/inputPeerNotifySettings).

    Generated from the following TL definition:
    ```tl
    inputPeerNotifySettings#cacb6ae2 flags:# show_previews:flags.0?Bool silent:flags.1?Bool mute_until:flags.2?int sound:flags.3?NotificationSound stories_muted:flags.6?Bool stories_hide_sender:flags.7?Bool stories_sound:flags.8?NotificationSound = InputPeerNotifySettings
    ```
    """
    def __new__(
        cls,
        show_previews: Optional[bool],
        silent: Optional[bool],
        mute_until: Optional[int],
        sound: Optional[types.NotificationSoundDefault | types.NotificationSoundNone | types.NotificationSoundLocal | types.NotificationSoundRingtone],
        stories_muted: Optional[bool],
        stories_hide_sender: Optional[bool],
        stories_sound: Optional[types.NotificationSoundDefault | types.NotificationSoundNone | types.NotificationSoundLocal | types.NotificationSoundRingtone],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerNotifySettings(TLObject):
    """
    [Read `peerNotifySettings` docs](https://core.telegram.org/constructor/peerNotifySettings).

    Generated from the following TL definition:
    ```tl
    peerNotifySettings#99622c0c flags:# show_previews:flags.0?Bool silent:flags.1?Bool mute_until:flags.2?int ios_sound:flags.3?NotificationSound android_sound:flags.4?NotificationSound other_sound:flags.5?NotificationSound stories_muted:flags.6?Bool stories_hide_sender:flags.7?Bool stories_ios_sound:flags.8?NotificationSound stories_android_sound:flags.9?NotificationSound stories_other_sound:flags.10?NotificationSound = PeerNotifySettings
    ```
    """
    def __new__(
        cls,
        show_previews: Optional[bool],
        silent: Optional[bool],
        mute_until: Optional[int],
        ios_sound: Optional[types.NotificationSoundDefault | types.NotificationSoundNone | types.NotificationSoundLocal | types.NotificationSoundRingtone],
        android_sound: Optional[types.NotificationSoundDefault | types.NotificationSoundNone | types.NotificationSoundLocal | types.NotificationSoundRingtone],
        other_sound: Optional[types.NotificationSoundDefault | types.NotificationSoundNone | types.NotificationSoundLocal | types.NotificationSoundRingtone],
        stories_muted: Optional[bool],
        stories_hide_sender: Optional[bool],
        stories_ios_sound: Optional[types.NotificationSoundDefault | types.NotificationSoundNone | types.NotificationSoundLocal | types.NotificationSoundRingtone],
        stories_android_sound: Optional[types.NotificationSoundDefault | types.NotificationSoundNone | types.NotificationSoundLocal | types.NotificationSoundRingtone],
        stories_other_sound: Optional[types.NotificationSoundDefault | types.NotificationSoundNone | types.NotificationSoundLocal | types.NotificationSoundRingtone],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerSettings(TLObject):
    """
    [Read `peerSettings` docs](https://core.telegram.org/constructor/peerSettings).

    Generated from the following TL definition:
    ```tl
    peerSettings#f47741f7 flags:# report_spam:flags.0?true add_contact:flags.1?true block_contact:flags.2?true share_contact:flags.3?true need_contacts_exception:flags.4?true report_geo:flags.5?true autoarchived:flags.7?true invite_members:flags.8?true request_chat_broadcast:flags.10?true business_bot_paused:flags.11?true business_bot_can_reply:flags.12?true geo_distance:flags.6?int request_chat_title:flags.9?string request_chat_date:flags.9?int business_bot_id:flags.13?long business_bot_manage_url:flags.13?string charge_paid_message_stars:flags.14?long registration_month:flags.15?string phone_country:flags.16?string name_change_date:flags.17?int photo_change_date:flags.18?int = PeerSettings
    ```
    """
    def __new__(
        cls,
        report_spam: bool,
        add_contact: bool,
        block_contact: bool,
        share_contact: bool,
        need_contacts_exception: bool,
        report_geo: bool,
        autoarchived: bool,
        invite_members: bool,
        request_chat_broadcast: bool,
        business_bot_paused: bool,
        business_bot_can_reply: bool,
        geo_distance: Optional[int],
        request_chat_title: Optional[str],
        request_chat_date: Optional[int],
        business_bot_id: Optional[int],
        business_bot_manage_url: Optional[str],
        charge_paid_message_stars: Optional[int],
        registration_month: Optional[str],
        phone_country: Optional[str],
        name_change_date: Optional[int],
        photo_change_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WallPaper(TLObject):
    """
    [Read `wallPaper` docs](https://core.telegram.org/constructor/wallPaper).

    Generated from the following TL definition:
    ```tl
    wallPaper#a437c3ed id:long flags:# creator:flags.0?true default:flags.1?true pattern:flags.3?true dark:flags.4?true access_hash:long slug:string document:Document settings:flags.2?WallPaperSettings = WallPaper
    ```
    """
    def __new__(
        cls,
        id: int,
        creator: bool,
        default: bool,
        pattern: bool,
        dark: bool,
        access_hash: int,
        slug: str,
        document: types.DocumentEmpty | types.Document,
        settings: Optional[types.WallPaperSettings],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WallPaperNoFile(TLObject):
    """
    [Read `wallPaperNoFile` docs](https://core.telegram.org/constructor/wallPaperNoFile).

    Generated from the following TL definition:
    ```tl
    wallPaperNoFile#e0804116 id:long flags:# default:flags.1?true dark:flags.4?true settings:flags.2?WallPaperSettings = WallPaper
    ```
    """
    def __new__(
        cls,
        id: int,
        default: bool,
        dark: bool,
        settings: Optional[types.WallPaperSettings],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReportReasonSpam(TLObject):
    """
    [Read `inputReportReasonSpam` docs](https://core.telegram.org/constructor/inputReportReasonSpam).

    Generated from the following TL definition:
    ```tl
    inputReportReasonSpam#58dbcab8 = ReportReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReportReasonViolence(TLObject):
    """
    [Read `inputReportReasonViolence` docs](https://core.telegram.org/constructor/inputReportReasonViolence).

    Generated from the following TL definition:
    ```tl
    inputReportReasonViolence#1e22c78d = ReportReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReportReasonPornography(TLObject):
    """
    [Read `inputReportReasonPornography` docs](https://core.telegram.org/constructor/inputReportReasonPornography).

    Generated from the following TL definition:
    ```tl
    inputReportReasonPornography#2e59d922 = ReportReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReportReasonChildAbuse(TLObject):
    """
    [Read `inputReportReasonChildAbuse` docs](https://core.telegram.org/constructor/inputReportReasonChildAbuse).

    Generated from the following TL definition:
    ```tl
    inputReportReasonChildAbuse#adf44ee3 = ReportReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReportReasonOther(TLObject):
    """
    [Read `inputReportReasonOther` docs](https://core.telegram.org/constructor/inputReportReasonOther).

    Generated from the following TL definition:
    ```tl
    inputReportReasonOther#c1e4a2b1 = ReportReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReportReasonCopyright(TLObject):
    """
    [Read `inputReportReasonCopyright` docs](https://core.telegram.org/constructor/inputReportReasonCopyright).

    Generated from the following TL definition:
    ```tl
    inputReportReasonCopyright#9b89f93a = ReportReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReportReasonGeoIrrelevant(TLObject):
    """
    [Read `inputReportReasonGeoIrrelevant` docs](https://core.telegram.org/constructor/inputReportReasonGeoIrrelevant).

    Generated from the following TL definition:
    ```tl
    inputReportReasonGeoIrrelevant#dbd4feed = ReportReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReportReasonFake(TLObject):
    """
    [Read `inputReportReasonFake` docs](https://core.telegram.org/constructor/inputReportReasonFake).

    Generated from the following TL definition:
    ```tl
    inputReportReasonFake#f5ddd6e7 = ReportReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReportReasonIllegalDrugs(TLObject):
    """
    [Read `inputReportReasonIllegalDrugs` docs](https://core.telegram.org/constructor/inputReportReasonIllegalDrugs).

    Generated from the following TL definition:
    ```tl
    inputReportReasonIllegalDrugs#a8eb2be = ReportReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReportReasonPersonalDetails(TLObject):
    """
    [Read `inputReportReasonPersonalDetails` docs](https://core.telegram.org/constructor/inputReportReasonPersonalDetails).

    Generated from the following TL definition:
    ```tl
    inputReportReasonPersonalDetails#9ec7863d = ReportReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UserFull(TLObject):
    """
    [Read `userFull` docs](https://core.telegram.org/constructor/userFull).

    Generated from the following TL definition:
    ```tl
    userFull#a02bc13e flags:# blocked:flags.0?true phone_calls_available:flags.4?true phone_calls_private:flags.5?true can_pin_message:flags.7?true has_scheduled:flags.12?true video_calls_available:flags.13?true voice_messages_forbidden:flags.20?true translations_disabled:flags.23?true stories_pinned_available:flags.26?true blocked_my_stories_from:flags.27?true wallpaper_overridden:flags.28?true contact_require_premium:flags.29?true read_dates_private:flags.30?true flags2:# sponsored_enabled:flags2.7?true can_view_revenue:flags2.9?true bot_can_manage_emoji_status:flags2.10?true display_gifts_button:flags2.16?true id:long about:flags.1?string settings:PeerSettings personal_photo:flags.21?Photo profile_photo:flags.2?Photo fallback_photo:flags.22?Photo notify_settings:PeerNotifySettings bot_info:flags.3?BotInfo pinned_msg_id:flags.6?int common_chats_count:int folder_id:flags.11?int ttl_period:flags.14?int theme:flags.15?ChatTheme private_forward_name:flags.16?string bot_group_admin_rights:flags.17?ChatAdminRights bot_broadcast_admin_rights:flags.18?ChatAdminRights wallpaper:flags.24?WallPaper stories:flags.25?PeerStories business_work_hours:flags2.0?BusinessWorkHours business_location:flags2.1?BusinessLocation business_greeting_message:flags2.2?BusinessGreetingMessage business_away_message:flags2.3?BusinessAwayMessage business_intro:flags2.4?BusinessIntro birthday:flags2.5?Birthday personal_channel_id:flags2.6?long personal_channel_message:flags2.6?int stargifts_count:flags2.8?int starref_program:flags2.11?StarRefProgram bot_verification:flags2.12?BotVerification send_paid_messages_stars:flags2.14?long disallowed_gifts:flags2.15?DisallowedGiftsSettings stars_rating:flags2.17?StarsRating stars_my_pending_rating:flags2.18?StarsRating stars_my_pending_rating_date:flags2.18?int main_tab:flags2.20?ProfileTab saved_music:flags2.21?Document note:flags2.22?TextWithEntities = UserFull
    ```
    """
    def __new__(
        cls,
        blocked: bool,
        phone_calls_available: bool,
        phone_calls_private: bool,
        can_pin_message: bool,
        has_scheduled: bool,
        video_calls_available: bool,
        voice_messages_forbidden: bool,
        translations_disabled: bool,
        stories_pinned_available: bool,
        blocked_my_stories_from: bool,
        wallpaper_overridden: bool,
        contact_require_premium: bool,
        read_dates_private: bool,
        sponsored_enabled: bool,
        can_view_revenue: bool,
        bot_can_manage_emoji_status: bool,
        display_gifts_button: bool,
        id: int,
        about: Optional[str],
        settings: types.PeerSettings,
        personal_photo: Optional[types.PhotoEmpty | types.Photo],
        profile_photo: Optional[types.PhotoEmpty | types.Photo],
        fallback_photo: Optional[types.PhotoEmpty | types.Photo],
        notify_settings: types.PeerNotifySettings,
        bot_info: Optional[types.BotInfo],
        pinned_msg_id: Optional[int],
        common_chats_count: int,
        folder_id: Optional[int],
        ttl_period: Optional[int],
        theme: Optional[types.ChatTheme | types.ChatThemeUniqueGift],
        private_forward_name: Optional[str],
        bot_group_admin_rights: Optional[types.ChatAdminRights],
        bot_broadcast_admin_rights: Optional[types.ChatAdminRights],
        wallpaper: Optional[types.WallPaper | types.WallPaperNoFile],
        stories: Optional[types.PeerStories],
        business_work_hours: Optional[types.BusinessWorkHours],
        business_location: Optional[types.BusinessLocation],
        business_greeting_message: Optional[types.BusinessGreetingMessage],
        business_away_message: Optional[types.BusinessAwayMessage],
        business_intro: Optional[types.BusinessIntro],
        birthday: Optional[types.Birthday],
        personal_channel_id: Optional[int],
        personal_channel_message: Optional[int],
        stargifts_count: Optional[int],
        starref_program: Optional[types.StarRefProgram],
        bot_verification: Optional[types.BotVerification],
        send_paid_messages_stars: Optional[int],
        disallowed_gifts: Optional[types.DisallowedGiftsSettings],
        stars_rating: Optional[types.StarsRating],
        stars_my_pending_rating: Optional[types.StarsRating],
        stars_my_pending_rating_date: Optional[int],
        main_tab: Optional[types.ProfileTabPosts | types.ProfileTabGifts | types.ProfileTabMedia | types.ProfileTabFiles | types.ProfileTabMusic | types.ProfileTabVoice | types.ProfileTabLinks | types.ProfileTabGifs],
        saved_music: Optional[types.DocumentEmpty | types.Document],
        note: Optional[types.TextWithEntities],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Contact(TLObject):
    """
    [Read `contact` docs](https://core.telegram.org/constructor/contact).

    Generated from the following TL definition:
    ```tl
    contact#145ade0b user_id:long mutual:Bool = Contact
    ```
    """
    def __new__(
        cls,
        user_id: int,
        mutual: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ImportedContact(TLObject):
    """
    [Read `importedContact` docs](https://core.telegram.org/constructor/importedContact).

    Generated from the following TL definition:
    ```tl
    importedContact#c13e3c50 user_id:long client_id:long = ImportedContact
    ```
    """
    def __new__(
        cls,
        user_id: int,
        client_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ContactStatus(TLObject):
    """
    [Read `contactStatus` docs](https://core.telegram.org/constructor/contactStatus).

    Generated from the following TL definition:
    ```tl
    contactStatus#16d9703b user_id:long status:UserStatus = ContactStatus
    ```
    """
    def __new__(
        cls,
        user_id: int,
        status: types.UserStatusEmpty | types.UserStatusOnline | types.UserStatusOffline | types.UserStatusRecently | types.UserStatusLastWeek | types.UserStatusLastMonth,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterEmpty(TLObject):
    """
    [Read `inputMessagesFilterEmpty` docs](https://core.telegram.org/constructor/inputMessagesFilterEmpty).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterEmpty#57e2f66c = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterPhotos(TLObject):
    """
    [Read `inputMessagesFilterPhotos` docs](https://core.telegram.org/constructor/inputMessagesFilterPhotos).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterPhotos#9609a51c = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterVideo(TLObject):
    """
    [Read `inputMessagesFilterVideo` docs](https://core.telegram.org/constructor/inputMessagesFilterVideo).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterVideo#9fc00e65 = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterPhotoVideo(TLObject):
    """
    [Read `inputMessagesFilterPhotoVideo` docs](https://core.telegram.org/constructor/inputMessagesFilterPhotoVideo).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterPhotoVideo#56e9f0e4 = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterDocument(TLObject):
    """
    [Read `inputMessagesFilterDocument` docs](https://core.telegram.org/constructor/inputMessagesFilterDocument).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterDocument#9eddf188 = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterUrl(TLObject):
    """
    [Read `inputMessagesFilterUrl` docs](https://core.telegram.org/constructor/inputMessagesFilterUrl).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterUrl#7ef0dd87 = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterGif(TLObject):
    """
    [Read `inputMessagesFilterGif` docs](https://core.telegram.org/constructor/inputMessagesFilterGif).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterGif#ffc86587 = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterVoice(TLObject):
    """
    [Read `inputMessagesFilterVoice` docs](https://core.telegram.org/constructor/inputMessagesFilterVoice).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterVoice#50f5c392 = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterMusic(TLObject):
    """
    [Read `inputMessagesFilterMusic` docs](https://core.telegram.org/constructor/inputMessagesFilterMusic).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterMusic#3751b49e = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterChatPhotos(TLObject):
    """
    [Read `inputMessagesFilterChatPhotos` docs](https://core.telegram.org/constructor/inputMessagesFilterChatPhotos).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterChatPhotos#3a20ecb8 = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterPhoneCalls(TLObject):
    """
    [Read `inputMessagesFilterPhoneCalls` docs](https://core.telegram.org/constructor/inputMessagesFilterPhoneCalls).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterPhoneCalls#80c99768 flags:# missed:flags.0?true = MessagesFilter
    ```
    """
    def __new__(
        cls,
        missed: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterRoundVoice(TLObject):
    """
    [Read `inputMessagesFilterRoundVoice` docs](https://core.telegram.org/constructor/inputMessagesFilterRoundVoice).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterRoundVoice#7a7c17a4 = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterRoundVideo(TLObject):
    """
    [Read `inputMessagesFilterRoundVideo` docs](https://core.telegram.org/constructor/inputMessagesFilterRoundVideo).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterRoundVideo#b549da53 = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterMyMentions(TLObject):
    """
    [Read `inputMessagesFilterMyMentions` docs](https://core.telegram.org/constructor/inputMessagesFilterMyMentions).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterMyMentions#c1f8e69a = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterGeo(TLObject):
    """
    [Read `inputMessagesFilterGeo` docs](https://core.telegram.org/constructor/inputMessagesFilterGeo).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterGeo#e7026d0d = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterContacts(TLObject):
    """
    [Read `inputMessagesFilterContacts` docs](https://core.telegram.org/constructor/inputMessagesFilterContacts).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterContacts#e062db83 = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagesFilterPinned(TLObject):
    """
    [Read `inputMessagesFilterPinned` docs](https://core.telegram.org/constructor/inputMessagesFilterPinned).

    Generated from the following TL definition:
    ```tl
    inputMessagesFilterPinned#1bb00451 = MessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateNewMessage(TLObject):
    """
    [Read `updateNewMessage` docs](https://core.telegram.org/constructor/updateNewMessage).

    Generated from the following TL definition:
    ```tl
    updateNewMessage#1f2b0afd message:Message pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        message: types.MessageEmpty | types.Message | types.MessageService,
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateMessageId(TLObject):
    """
    [Read `updateMessageID` docs](https://core.telegram.org/constructor/updateMessageID).

    Generated from the following TL definition:
    ```tl
    updateMessageID#4e90bfd6 id:int random_id:long = Update
    ```
    """
    def __new__(
        cls,
        id: int,
        random_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDeleteMessages(TLObject):
    """
    [Read `updateDeleteMessages` docs](https://core.telegram.org/constructor/updateDeleteMessages).

    Generated from the following TL definition:
    ```tl
    updateDeleteMessages#a20db0e5 messages:Vector<int> pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        messages: Sequence[int],
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateUserTyping(TLObject):
    """
    [Read `updateUserTyping` docs](https://core.telegram.org/constructor/updateUserTyping).

    Generated from the following TL definition:
    ```tl
    updateUserTyping#2a17bf5c flags:# user_id:long top_msg_id:flags.0?int action:SendMessageAction = Update
    ```
    """
    def __new__(
        cls,
        user_id: int,
        top_msg_id: Optional[int],
        action: types.SendMessageTypingAction | types.SendMessageCancelAction | types.SendMessageRecordVideoAction | types.SendMessageUploadVideoAction | types.SendMessageRecordAudioAction | types.SendMessageUploadAudioAction | types.SendMessageUploadPhotoAction | types.SendMessageUploadDocumentAction | types.SendMessageGeoLocationAction | types.SendMessageChooseContactAction | types.SendMessageGamePlayAction | types.SendMessageRecordRoundAction | types.SendMessageUploadRoundAction | types.SpeakingInGroupCallAction | types.SendMessageHistoryImportAction | types.SendMessageChooseStickerAction | types.SendMessageEmojiInteraction | types.SendMessageEmojiInteractionSeen | types.SendMessageTextDraftAction,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChatUserTyping(TLObject):
    """
    [Read `updateChatUserTyping` docs](https://core.telegram.org/constructor/updateChatUserTyping).

    Generated from the following TL definition:
    ```tl
    updateChatUserTyping#83487af0 chat_id:long from_id:Peer action:SendMessageAction = Update
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        from_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        action: types.SendMessageTypingAction | types.SendMessageCancelAction | types.SendMessageRecordVideoAction | types.SendMessageUploadVideoAction | types.SendMessageRecordAudioAction | types.SendMessageUploadAudioAction | types.SendMessageUploadPhotoAction | types.SendMessageUploadDocumentAction | types.SendMessageGeoLocationAction | types.SendMessageChooseContactAction | types.SendMessageGamePlayAction | types.SendMessageRecordRoundAction | types.SendMessageUploadRoundAction | types.SpeakingInGroupCallAction | types.SendMessageHistoryImportAction | types.SendMessageChooseStickerAction | types.SendMessageEmojiInteraction | types.SendMessageEmojiInteractionSeen | types.SendMessageTextDraftAction,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChatParticipants(TLObject):
    """
    [Read `updateChatParticipants` docs](https://core.telegram.org/constructor/updateChatParticipants).

    Generated from the following TL definition:
    ```tl
    updateChatParticipants#7761198 participants:ChatParticipants = Update
    ```
    """
    def __new__(
        cls,
        participants: types.ChatParticipantsForbidden | types.ChatParticipants,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateUserStatus(TLObject):
    """
    [Read `updateUserStatus` docs](https://core.telegram.org/constructor/updateUserStatus).

    Generated from the following TL definition:
    ```tl
    updateUserStatus#e5bdf8de user_id:long status:UserStatus = Update
    ```
    """
    def __new__(
        cls,
        user_id: int,
        status: types.UserStatusEmpty | types.UserStatusOnline | types.UserStatusOffline | types.UserStatusRecently | types.UserStatusLastWeek | types.UserStatusLastMonth,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateUserName(TLObject):
    """
    [Read `updateUserName` docs](https://core.telegram.org/constructor/updateUserName).

    Generated from the following TL definition:
    ```tl
    updateUserName#a7848924 user_id:long first_name:string last_name:string usernames:Vector<Username> = Update
    ```
    """
    def __new__(
        cls,
        user_id: int,
        first_name: str,
        last_name: str,
        usernames: Sequence[types.Username],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateNewAuthorization(TLObject):
    """
    [Read `updateNewAuthorization` docs](https://core.telegram.org/constructor/updateNewAuthorization).

    Generated from the following TL definition:
    ```tl
    updateNewAuthorization#8951abef flags:# unconfirmed:flags.0?true hash:long date:flags.0?int device:flags.0?string location:flags.0?string = Update
    ```
    """
    def __new__(
        cls,
        unconfirmed: bool,
        hash: int,
        date: Optional[int],
        device: Optional[str],
        location: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateNewEncryptedMessage(TLObject):
    """
    [Read `updateNewEncryptedMessage` docs](https://core.telegram.org/constructor/updateNewEncryptedMessage).

    Generated from the following TL definition:
    ```tl
    updateNewEncryptedMessage#12bcbd9a message:EncryptedMessage qts:int = Update
    ```
    """
    def __new__(
        cls,
        message: types.EncryptedMessage | types.EncryptedMessageService,
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateEncryptedChatTyping(TLObject):
    """
    [Read `updateEncryptedChatTyping` docs](https://core.telegram.org/constructor/updateEncryptedChatTyping).

    Generated from the following TL definition:
    ```tl
    updateEncryptedChatTyping#1710f156 chat_id:int = Update
    ```
    """
    def __new__(
        cls,
        chat_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateEncryption(TLObject):
    """
    [Read `updateEncryption` docs](https://core.telegram.org/constructor/updateEncryption).

    Generated from the following TL definition:
    ```tl
    updateEncryption#b4a2e88d chat:EncryptedChat date:int = Update
    ```
    """
    def __new__(
        cls,
        chat: types.EncryptedChatEmpty | types.EncryptedChatWaiting | types.EncryptedChatRequested | types.EncryptedChat | types.EncryptedChatDiscarded,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateEncryptedMessagesRead(TLObject):
    """
    [Read `updateEncryptedMessagesRead` docs](https://core.telegram.org/constructor/updateEncryptedMessagesRead).

    Generated from the following TL definition:
    ```tl
    updateEncryptedMessagesRead#38fe25b7 chat_id:int max_date:int date:int = Update
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        max_date: int,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChatParticipantAdd(TLObject):
    """
    [Read `updateChatParticipantAdd` docs](https://core.telegram.org/constructor/updateChatParticipantAdd).

    Generated from the following TL definition:
    ```tl
    updateChatParticipantAdd#3dda5451 chat_id:long user_id:long inviter_id:long date:int version:int = Update
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        user_id: int,
        inviter_id: int,
        date: int,
        version: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChatParticipantDelete(TLObject):
    """
    [Read `updateChatParticipantDelete` docs](https://core.telegram.org/constructor/updateChatParticipantDelete).

    Generated from the following TL definition:
    ```tl
    updateChatParticipantDelete#e32f3d77 chat_id:long user_id:long version:int = Update
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        user_id: int,
        version: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDcOptions(TLObject):
    """
    [Read `updateDcOptions` docs](https://core.telegram.org/constructor/updateDcOptions).

    Generated from the following TL definition:
    ```tl
    updateDcOptions#8e5e9873 dc_options:Vector<DcOption> = Update
    ```
    """
    def __new__(
        cls,
        dc_options: Sequence[types.DcOption],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateNotifySettings(TLObject):
    """
    [Read `updateNotifySettings` docs](https://core.telegram.org/constructor/updateNotifySettings).

    Generated from the following TL definition:
    ```tl
    updateNotifySettings#bec268ef peer:NotifyPeer notify_settings:PeerNotifySettings = Update
    ```
    """
    def __new__(
        cls,
        peer: types.NotifyPeer | types.NotifyUsers | types.NotifyChats | types.NotifyBroadcasts | types.NotifyForumTopic,
        notify_settings: types.PeerNotifySettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateServiceNotification(TLObject):
    """
    [Read `updateServiceNotification` docs](https://core.telegram.org/constructor/updateServiceNotification).

    Generated from the following TL definition:
    ```tl
    updateServiceNotification#ebe46819 flags:# popup:flags.0?true invert_media:flags.2?true inbox_date:flags.1?int type:string message:string media:MessageMedia entities:Vector<MessageEntity> = Update
    ```
    """
    def __new__(
        cls,
        popup: bool,
        invert_media: bool,
        inbox_date: Optional[int],
        type: str,
        message: str,
        media: types.MessageMediaEmpty | types.MessageMediaPhoto | types.MessageMediaGeo | types.MessageMediaContact | types.MessageMediaUnsupported | types.MessageMediaDocument | types.MessageMediaWebPage | types.MessageMediaVenue | types.MessageMediaGame | types.MessageMediaInvoice | types.MessageMediaGeoLive | types.MessageMediaPoll | types.MessageMediaDice | types.MessageMediaStory | types.MessageMediaGiveaway | types.MessageMediaGiveawayResults | types.MessageMediaPaidMedia | types.MessageMediaToDo | types.MessageMediaVideoStream,
        entities: Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePrivacy(TLObject):
    """
    [Read `updatePrivacy` docs](https://core.telegram.org/constructor/updatePrivacy).

    Generated from the following TL definition:
    ```tl
    updatePrivacy#ee3b272a key:PrivacyKey rules:Vector<PrivacyRule> = Update
    ```
    """
    def __new__(
        cls,
        key: types.PrivacyKeyStatusTimestamp | types.PrivacyKeyChatInvite | types.PrivacyKeyPhoneCall | types.PrivacyKeyPhoneP2P | types.PrivacyKeyForwards | types.PrivacyKeyProfilePhoto | types.PrivacyKeyPhoneNumber | types.PrivacyKeyAddedByPhone | types.PrivacyKeyVoiceMessages | types.PrivacyKeyAbout | types.PrivacyKeyBirthday | types.PrivacyKeyStarGiftsAutoSave | types.PrivacyKeyNoPaidMessages | types.PrivacyKeySavedMusic,
        rules: Sequence[types.PrivacyValueAllowContacts | types.PrivacyValueAllowAll | types.PrivacyValueAllowUsers | types.PrivacyValueDisallowContacts | types.PrivacyValueDisallowAll | types.PrivacyValueDisallowUsers | types.PrivacyValueAllowChatParticipants | types.PrivacyValueDisallowChatParticipants | types.PrivacyValueAllowCloseFriends | types.PrivacyValueAllowPremium | types.PrivacyValueAllowBots | types.PrivacyValueDisallowBots],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateUserPhone(TLObject):
    """
    [Read `updateUserPhone` docs](https://core.telegram.org/constructor/updateUserPhone).

    Generated from the following TL definition:
    ```tl
    updateUserPhone#5492a13 user_id:long phone:string = Update
    ```
    """
    def __new__(
        cls,
        user_id: int,
        phone: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateReadHistoryInbox(TLObject):
    """
    [Read `updateReadHistoryInbox` docs](https://core.telegram.org/constructor/updateReadHistoryInbox).

    Generated from the following TL definition:
    ```tl
    updateReadHistoryInbox#9e84bc99 flags:# folder_id:flags.0?int peer:Peer top_msg_id:flags.1?int max_id:int still_unread_count:int pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        folder_id: Optional[int],
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        top_msg_id: Optional[int],
        max_id: int,
        still_unread_count: int,
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateReadHistoryOutbox(TLObject):
    """
    [Read `updateReadHistoryOutbox` docs](https://core.telegram.org/constructor/updateReadHistoryOutbox).

    Generated from the following TL definition:
    ```tl
    updateReadHistoryOutbox#2f2f21bf peer:Peer max_id:int pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        max_id: int,
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateWebPage(TLObject):
    """
    [Read `updateWebPage` docs](https://core.telegram.org/constructor/updateWebPage).

    Generated from the following TL definition:
    ```tl
    updateWebPage#7f891213 webpage:WebPage pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        webpage: types.WebPageEmpty | types.WebPagePending | types.WebPage | types.WebPageNotModified,
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateReadMessagesContents(TLObject):
    """
    [Read `updateReadMessagesContents` docs](https://core.telegram.org/constructor/updateReadMessagesContents).

    Generated from the following TL definition:
    ```tl
    updateReadMessagesContents#f8227181 flags:# messages:Vector<int> pts:int pts_count:int date:flags.0?int = Update
    ```
    """
    def __new__(
        cls,
        messages: Sequence[int],
        pts: int,
        pts_count: int,
        date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChannelTooLong(TLObject):
    """
    [Read `updateChannelTooLong` docs](https://core.telegram.org/constructor/updateChannelTooLong).

    Generated from the following TL definition:
    ```tl
    updateChannelTooLong#108d941f flags:# channel_id:long pts:flags.0?int = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        pts: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChannel(TLObject):
    """
    [Read `updateChannel` docs](https://core.telegram.org/constructor/updateChannel).

    Generated from the following TL definition:
    ```tl
    updateChannel#635b4c09 channel_id:long = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateNewChannelMessage(TLObject):
    """
    [Read `updateNewChannelMessage` docs](https://core.telegram.org/constructor/updateNewChannelMessage).

    Generated from the following TL definition:
    ```tl
    updateNewChannelMessage#62ba04d9 message:Message pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        message: types.MessageEmpty | types.Message | types.MessageService,
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateReadChannelInbox(TLObject):
    """
    [Read `updateReadChannelInbox` docs](https://core.telegram.org/constructor/updateReadChannelInbox).

    Generated from the following TL definition:
    ```tl
    updateReadChannelInbox#922e6e10 flags:# folder_id:flags.0?int channel_id:long max_id:int still_unread_count:int pts:int = Update
    ```
    """
    def __new__(
        cls,
        folder_id: Optional[int],
        channel_id: int,
        max_id: int,
        still_unread_count: int,
        pts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDeleteChannelMessages(TLObject):
    """
    [Read `updateDeleteChannelMessages` docs](https://core.telegram.org/constructor/updateDeleteChannelMessages).

    Generated from the following TL definition:
    ```tl
    updateDeleteChannelMessages#c32d5b12 channel_id:long messages:Vector<int> pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        messages: Sequence[int],
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChannelMessageViews(TLObject):
    """
    [Read `updateChannelMessageViews` docs](https://core.telegram.org/constructor/updateChannelMessageViews).

    Generated from the following TL definition:
    ```tl
    updateChannelMessageViews#f226ac08 channel_id:long id:int views:int = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        id: int,
        views: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChatParticipantAdmin(TLObject):
    """
    [Read `updateChatParticipantAdmin` docs](https://core.telegram.org/constructor/updateChatParticipantAdmin).

    Generated from the following TL definition:
    ```tl
    updateChatParticipantAdmin#d7ca61a2 chat_id:long user_id:long is_admin:Bool version:int = Update
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        user_id: int,
        is_admin: bool,
        version: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateNewStickerSet(TLObject):
    """
    [Read `updateNewStickerSet` docs](https://core.telegram.org/constructor/updateNewStickerSet).

    Generated from the following TL definition:
    ```tl
    updateNewStickerSet#688a30aa stickerset:messages.StickerSet = Update
    ```
    """
    def __new__(
        cls,
        stickerset: types.messages.StickerSet | types.messages.StickerSetNotModified,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStickerSetsOrder(TLObject):
    """
    [Read `updateStickerSetsOrder` docs](https://core.telegram.org/constructor/updateStickerSetsOrder).

    Generated from the following TL definition:
    ```tl
    updateStickerSetsOrder#bb2d201 flags:# masks:flags.0?true emojis:flags.1?true order:Vector<long> = Update
    ```
    """
    def __new__(
        cls,
        masks: bool,
        emojis: bool,
        order: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStickerSets(TLObject):
    """
    [Read `updateStickerSets` docs](https://core.telegram.org/constructor/updateStickerSets).

    Generated from the following TL definition:
    ```tl
    updateStickerSets#31c24808 flags:# masks:flags.0?true emojis:flags.1?true = Update
    ```
    """
    def __new__(
        cls,
        masks: bool,
        emojis: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateSavedGifs(TLObject):
    """
    [Read `updateSavedGifs` docs](https://core.telegram.org/constructor/updateSavedGifs).

    Generated from the following TL definition:
    ```tl
    updateSavedGifs#9375341e = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotInlineQuery(TLObject):
    """
    [Read `updateBotInlineQuery` docs](https://core.telegram.org/constructor/updateBotInlineQuery).

    Generated from the following TL definition:
    ```tl
    updateBotInlineQuery#496f379c flags:# query_id:long user_id:long query:string geo:flags.0?GeoPoint peer_type:flags.1?InlineQueryPeerType offset:string = Update
    ```
    """
    def __new__(
        cls,
        query_id: int,
        user_id: int,
        query: str,
        geo: Optional[types.GeoPointEmpty | types.GeoPoint],
        peer_type: Optional[types.InlineQueryPeerTypeSameBotPm | types.InlineQueryPeerTypePm | types.InlineQueryPeerTypeChat | types.InlineQueryPeerTypeMegagroup | types.InlineQueryPeerTypeBroadcast | types.InlineQueryPeerTypeBotPm],
        offset: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotInlineSend(TLObject):
    """
    [Read `updateBotInlineSend` docs](https://core.telegram.org/constructor/updateBotInlineSend).

    Generated from the following TL definition:
    ```tl
    updateBotInlineSend#12f12a07 flags:# user_id:long query:string geo:flags.0?GeoPoint id:string msg_id:flags.1?InputBotInlineMessageID = Update
    ```
    """
    def __new__(
        cls,
        user_id: int,
        query: str,
        geo: Optional[types.GeoPointEmpty | types.GeoPoint],
        id: str,
        msg_id: Optional[types.InputBotInlineMessageId | types.InputBotInlineMessageId64],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateEditChannelMessage(TLObject):
    """
    [Read `updateEditChannelMessage` docs](https://core.telegram.org/constructor/updateEditChannelMessage).

    Generated from the following TL definition:
    ```tl
    updateEditChannelMessage#1b3f4df7 message:Message pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        message: types.MessageEmpty | types.Message | types.MessageService,
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotCallbackQuery(TLObject):
    """
    [Read `updateBotCallbackQuery` docs](https://core.telegram.org/constructor/updateBotCallbackQuery).

    Generated from the following TL definition:
    ```tl
    updateBotCallbackQuery#b9cfc48d flags:# query_id:long user_id:long peer:Peer msg_id:int chat_instance:long data:flags.0?bytes game_short_name:flags.1?string = Update
    ```
    """
    def __new__(
        cls,
        query_id: int,
        user_id: int,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        msg_id: int,
        chat_instance: int,
        data: Optional[bytes],
        game_short_name: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateEditMessage(TLObject):
    """
    [Read `updateEditMessage` docs](https://core.telegram.org/constructor/updateEditMessage).

    Generated from the following TL definition:
    ```tl
    updateEditMessage#e40370a3 message:Message pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        message: types.MessageEmpty | types.Message | types.MessageService,
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateInlineBotCallbackQuery(TLObject):
    """
    [Read `updateInlineBotCallbackQuery` docs](https://core.telegram.org/constructor/updateInlineBotCallbackQuery).

    Generated from the following TL definition:
    ```tl
    updateInlineBotCallbackQuery#691e9052 flags:# query_id:long user_id:long msg_id:InputBotInlineMessageID chat_instance:long data:flags.0?bytes game_short_name:flags.1?string = Update
    ```
    """
    def __new__(
        cls,
        query_id: int,
        user_id: int,
        msg_id: types.InputBotInlineMessageId | types.InputBotInlineMessageId64,
        chat_instance: int,
        data: Optional[bytes],
        game_short_name: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateReadChannelOutbox(TLObject):
    """
    [Read `updateReadChannelOutbox` docs](https://core.telegram.org/constructor/updateReadChannelOutbox).

    Generated from the following TL definition:
    ```tl
    updateReadChannelOutbox#b75f99a9 channel_id:long max_id:int = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDraftMessage(TLObject):
    """
    [Read `updateDraftMessage` docs](https://core.telegram.org/constructor/updateDraftMessage).

    Generated from the following TL definition:
    ```tl
    updateDraftMessage#edfc111e flags:# peer:Peer top_msg_id:flags.0?int saved_peer_id:flags.1?Peer draft:DraftMessage = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        top_msg_id: Optional[int],
        saved_peer_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        draft: types.DraftMessageEmpty | types.DraftMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateReadFeaturedStickers(TLObject):
    """
    [Read `updateReadFeaturedStickers` docs](https://core.telegram.org/constructor/updateReadFeaturedStickers).

    Generated from the following TL definition:
    ```tl
    updateReadFeaturedStickers#571d2742 = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateRecentStickers(TLObject):
    """
    [Read `updateRecentStickers` docs](https://core.telegram.org/constructor/updateRecentStickers).

    Generated from the following TL definition:
    ```tl
    updateRecentStickers#9a422c20 = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateConfig(TLObject):
    """
    [Read `updateConfig` docs](https://core.telegram.org/constructor/updateConfig).

    Generated from the following TL definition:
    ```tl
    updateConfig#a229dd06 = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePtsChanged(TLObject):
    """
    [Read `updatePtsChanged` docs](https://core.telegram.org/constructor/updatePtsChanged).

    Generated from the following TL definition:
    ```tl
    updatePtsChanged#3354678f = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChannelWebPage(TLObject):
    """
    [Read `updateChannelWebPage` docs](https://core.telegram.org/constructor/updateChannelWebPage).

    Generated from the following TL definition:
    ```tl
    updateChannelWebPage#2f2ba99f channel_id:long webpage:WebPage pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        webpage: types.WebPageEmpty | types.WebPagePending | types.WebPage | types.WebPageNotModified,
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDialogPinned(TLObject):
    """
    [Read `updateDialogPinned` docs](https://core.telegram.org/constructor/updateDialogPinned).

    Generated from the following TL definition:
    ```tl
    updateDialogPinned#6e6fe51c flags:# pinned:flags.0?true folder_id:flags.1?int peer:DialogPeer = Update
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        folder_id: Optional[int],
        peer: types.DialogPeer | types.DialogPeerFolder,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePinnedDialogs(TLObject):
    """
    [Read `updatePinnedDialogs` docs](https://core.telegram.org/constructor/updatePinnedDialogs).

    Generated from the following TL definition:
    ```tl
    updatePinnedDialogs#fa0f3ca2 flags:# folder_id:flags.1?int order:flags.0?Vector<DialogPeer> = Update
    ```
    """
    def __new__(
        cls,
        folder_id: Optional[int],
        order: Optional[Sequence[types.DialogPeer | types.DialogPeerFolder]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotWebhookJson(TLObject):
    """
    [Read `updateBotWebhookJSON` docs](https://core.telegram.org/constructor/updateBotWebhookJSON).

    Generated from the following TL definition:
    ```tl
    updateBotWebhookJSON#8317c0c3 data:DataJSON = Update
    ```
    """
    def __new__(
        cls,
        data: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotWebhookJsonquery(TLObject):
    """
    [Read `updateBotWebhookJSONQuery` docs](https://core.telegram.org/constructor/updateBotWebhookJSONQuery).

    Generated from the following TL definition:
    ```tl
    updateBotWebhookJSONQuery#9b9240a6 query_id:long data:DataJSON timeout:int = Update
    ```
    """
    def __new__(
        cls,
        query_id: int,
        data: types.DataJson,
        timeout: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotShippingQuery(TLObject):
    """
    [Read `updateBotShippingQuery` docs](https://core.telegram.org/constructor/updateBotShippingQuery).

    Generated from the following TL definition:
    ```tl
    updateBotShippingQuery#b5aefd7d query_id:long user_id:long payload:bytes shipping_address:PostAddress = Update
    ```
    """
    def __new__(
        cls,
        query_id: int,
        user_id: int,
        payload: bytes,
        shipping_address: types.PostAddress,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotPrecheckoutQuery(TLObject):
    """
    [Read `updateBotPrecheckoutQuery` docs](https://core.telegram.org/constructor/updateBotPrecheckoutQuery).

    Generated from the following TL definition:
    ```tl
    updateBotPrecheckoutQuery#8caa9a96 flags:# query_id:long user_id:long payload:bytes info:flags.0?PaymentRequestedInfo shipping_option_id:flags.1?string currency:string total_amount:long = Update
    ```
    """
    def __new__(
        cls,
        query_id: int,
        user_id: int,
        payload: bytes,
        info: Optional[types.PaymentRequestedInfo],
        shipping_option_id: Optional[str],
        currency: str,
        total_amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePhoneCall(TLObject):
    """
    [Read `updatePhoneCall` docs](https://core.telegram.org/constructor/updatePhoneCall).

    Generated from the following TL definition:
    ```tl
    updatePhoneCall#ab0f6b1e phone_call:PhoneCall = Update
    ```
    """
    def __new__(
        cls,
        phone_call: types.PhoneCallEmpty | types.PhoneCallWaiting | types.PhoneCallRequested | types.PhoneCallAccepted | types.PhoneCall | types.PhoneCallDiscarded,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateLangPackTooLong(TLObject):
    """
    [Read `updateLangPackTooLong` docs](https://core.telegram.org/constructor/updateLangPackTooLong).

    Generated from the following TL definition:
    ```tl
    updateLangPackTooLong#46560264 lang_code:string = Update
    ```
    """
    def __new__(
        cls,
        lang_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateLangPack(TLObject):
    """
    [Read `updateLangPack` docs](https://core.telegram.org/constructor/updateLangPack).

    Generated from the following TL definition:
    ```tl
    updateLangPack#56022f4d difference:LangPackDifference = Update
    ```
    """
    def __new__(
        cls,
        difference: types.LangPackDifference,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateFavedStickers(TLObject):
    """
    [Read `updateFavedStickers` docs](https://core.telegram.org/constructor/updateFavedStickers).

    Generated from the following TL definition:
    ```tl
    updateFavedStickers#e511996d = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChannelReadMessagesContents(TLObject):
    """
    [Read `updateChannelReadMessagesContents` docs](https://core.telegram.org/constructor/updateChannelReadMessagesContents).

    Generated from the following TL definition:
    ```tl
    updateChannelReadMessagesContents#25f324f7 flags:# channel_id:long top_msg_id:flags.0?int saved_peer_id:flags.1?Peer messages:Vector<int> = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        top_msg_id: Optional[int],
        saved_peer_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        messages: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateContactsReset(TLObject):
    """
    [Read `updateContactsReset` docs](https://core.telegram.org/constructor/updateContactsReset).

    Generated from the following TL definition:
    ```tl
    updateContactsReset#7084a7be = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChannelAvailableMessages(TLObject):
    """
    [Read `updateChannelAvailableMessages` docs](https://core.telegram.org/constructor/updateChannelAvailableMessages).

    Generated from the following TL definition:
    ```tl
    updateChannelAvailableMessages#b23fc698 channel_id:long available_min_id:int = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        available_min_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDialogUnreadMark(TLObject):
    """
    [Read `updateDialogUnreadMark` docs](https://core.telegram.org/constructor/updateDialogUnreadMark).

    Generated from the following TL definition:
    ```tl
    updateDialogUnreadMark#b658f23e flags:# unread:flags.0?true peer:DialogPeer saved_peer_id:flags.1?Peer = Update
    ```
    """
    def __new__(
        cls,
        unread: bool,
        peer: types.DialogPeer | types.DialogPeerFolder,
        saved_peer_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateMessagePoll(TLObject):
    """
    [Read `updateMessagePoll` docs](https://core.telegram.org/constructor/updateMessagePoll).

    Generated from the following TL definition:
    ```tl
    updateMessagePoll#aca1657b flags:# poll_id:long poll:flags.0?Poll results:PollResults = Update
    ```
    """
    def __new__(
        cls,
        poll_id: int,
        poll: Optional[types.Poll],
        results: types.PollResults,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChatDefaultBannedRights(TLObject):
    """
    [Read `updateChatDefaultBannedRights` docs](https://core.telegram.org/constructor/updateChatDefaultBannedRights).

    Generated from the following TL definition:
    ```tl
    updateChatDefaultBannedRights#54c01850 peer:Peer default_banned_rights:ChatBannedRights version:int = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        default_banned_rights: types.ChatBannedRights,
        version: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateFolderPeers(TLObject):
    """
    [Read `updateFolderPeers` docs](https://core.telegram.org/constructor/updateFolderPeers).

    Generated from the following TL definition:
    ```tl
    updateFolderPeers#19360dc0 folder_peers:Vector<FolderPeer> pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        folder_peers: Sequence[types.FolderPeer],
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePeerSettings(TLObject):
    """
    [Read `updatePeerSettings` docs](https://core.telegram.org/constructor/updatePeerSettings).

    Generated from the following TL definition:
    ```tl
    updatePeerSettings#6a7e7366 peer:Peer settings:PeerSettings = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        settings: types.PeerSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePeerLocated(TLObject):
    """
    [Read `updatePeerLocated` docs](https://core.telegram.org/constructor/updatePeerLocated).

    Generated from the following TL definition:
    ```tl
    updatePeerLocated#b4afcfb0 peers:Vector<PeerLocated> = Update
    ```
    """
    def __new__(
        cls,
        peers: Sequence[types.PeerLocated | types.PeerSelfLocated],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateNewScheduledMessage(TLObject):
    """
    [Read `updateNewScheduledMessage` docs](https://core.telegram.org/constructor/updateNewScheduledMessage).

    Generated from the following TL definition:
    ```tl
    updateNewScheduledMessage#39a51dfb message:Message = Update
    ```
    """
    def __new__(
        cls,
        message: types.MessageEmpty | types.Message | types.MessageService,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDeleteScheduledMessages(TLObject):
    """
    [Read `updateDeleteScheduledMessages` docs](https://core.telegram.org/constructor/updateDeleteScheduledMessages).

    Generated from the following TL definition:
    ```tl
    updateDeleteScheduledMessages#f2a71983 flags:# peer:Peer messages:Vector<int> sent_messages:flags.0?Vector<int> = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        messages: Sequence[int],
        sent_messages: Optional[Sequence[int]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateTheme(TLObject):
    """
    [Read `updateTheme` docs](https://core.telegram.org/constructor/updateTheme).

    Generated from the following TL definition:
    ```tl
    updateTheme#8216fba3 theme:Theme = Update
    ```
    """
    def __new__(
        cls,
        theme: types.Theme,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateGeoLiveViewed(TLObject):
    """
    [Read `updateGeoLiveViewed` docs](https://core.telegram.org/constructor/updateGeoLiveViewed).

    Generated from the following TL definition:
    ```tl
    updateGeoLiveViewed#871fb939 peer:Peer msg_id:int = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateLoginToken(TLObject):
    """
    [Read `updateLoginToken` docs](https://core.telegram.org/constructor/updateLoginToken).

    Generated from the following TL definition:
    ```tl
    updateLoginToken#564fe691 = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateMessagePollVote(TLObject):
    """
    [Read `updateMessagePollVote` docs](https://core.telegram.org/constructor/updateMessagePollVote).

    Generated from the following TL definition:
    ```tl
    updateMessagePollVote#24f40e77 poll_id:long peer:Peer options:Vector<bytes> qts:int = Update
    ```
    """
    def __new__(
        cls,
        poll_id: int,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        options: Sequence[bytes],
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDialogFilter(TLObject):
    """
    [Read `updateDialogFilter` docs](https://core.telegram.org/constructor/updateDialogFilter).

    Generated from the following TL definition:
    ```tl
    updateDialogFilter#26ffde7d flags:# id:int filter:flags.0?DialogFilter = Update
    ```
    """
    def __new__(
        cls,
        id: int,
        filter: Optional[types.DialogFilter | types.DialogFilterDefault | types.DialogFilterChatlist],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDialogFilterOrder(TLObject):
    """
    [Read `updateDialogFilterOrder` docs](https://core.telegram.org/constructor/updateDialogFilterOrder).

    Generated from the following TL definition:
    ```tl
    updateDialogFilterOrder#a5d72105 order:Vector<int> = Update
    ```
    """
    def __new__(
        cls,
        order: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDialogFilters(TLObject):
    """
    [Read `updateDialogFilters` docs](https://core.telegram.org/constructor/updateDialogFilters).

    Generated from the following TL definition:
    ```tl
    updateDialogFilters#3504914f = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePhoneCallSignalingData(TLObject):
    """
    [Read `updatePhoneCallSignalingData` docs](https://core.telegram.org/constructor/updatePhoneCallSignalingData).

    Generated from the following TL definition:
    ```tl
    updatePhoneCallSignalingData#2661bf09 phone_call_id:long data:bytes = Update
    ```
    """
    def __new__(
        cls,
        phone_call_id: int,
        data: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChannelMessageForwards(TLObject):
    """
    [Read `updateChannelMessageForwards` docs](https://core.telegram.org/constructor/updateChannelMessageForwards).

    Generated from the following TL definition:
    ```tl
    updateChannelMessageForwards#d29a27f4 channel_id:long id:int forwards:int = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        id: int,
        forwards: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateReadChannelDiscussionInbox(TLObject):
    """
    [Read `updateReadChannelDiscussionInbox` docs](https://core.telegram.org/constructor/updateReadChannelDiscussionInbox).

    Generated from the following TL definition:
    ```tl
    updateReadChannelDiscussionInbox#d6b19546 flags:# channel_id:long top_msg_id:int read_max_id:int broadcast_id:flags.0?long broadcast_post:flags.0?int = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        top_msg_id: int,
        read_max_id: int,
        broadcast_id: Optional[int],
        broadcast_post: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateReadChannelDiscussionOutbox(TLObject):
    """
    [Read `updateReadChannelDiscussionOutbox` docs](https://core.telegram.org/constructor/updateReadChannelDiscussionOutbox).

    Generated from the following TL definition:
    ```tl
    updateReadChannelDiscussionOutbox#695c9e7c channel_id:long top_msg_id:int read_max_id:int = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        top_msg_id: int,
        read_max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePeerBlocked(TLObject):
    """
    [Read `updatePeerBlocked` docs](https://core.telegram.org/constructor/updatePeerBlocked).

    Generated from the following TL definition:
    ```tl
    updatePeerBlocked#ebe07752 flags:# blocked:flags.0?true blocked_my_stories_from:flags.1?true peer_id:Peer = Update
    ```
    """
    def __new__(
        cls,
        blocked: bool,
        blocked_my_stories_from: bool,
        peer_id: types.PeerUser | types.PeerChat | types.PeerChannel,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChannelUserTyping(TLObject):
    """
    [Read `updateChannelUserTyping` docs](https://core.telegram.org/constructor/updateChannelUserTyping).

    Generated from the following TL definition:
    ```tl
    updateChannelUserTyping#8c88c923 flags:# channel_id:long top_msg_id:flags.0?int from_id:Peer action:SendMessageAction = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        top_msg_id: Optional[int],
        from_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        action: types.SendMessageTypingAction | types.SendMessageCancelAction | types.SendMessageRecordVideoAction | types.SendMessageUploadVideoAction | types.SendMessageRecordAudioAction | types.SendMessageUploadAudioAction | types.SendMessageUploadPhotoAction | types.SendMessageUploadDocumentAction | types.SendMessageGeoLocationAction | types.SendMessageChooseContactAction | types.SendMessageGamePlayAction | types.SendMessageRecordRoundAction | types.SendMessageUploadRoundAction | types.SpeakingInGroupCallAction | types.SendMessageHistoryImportAction | types.SendMessageChooseStickerAction | types.SendMessageEmojiInteraction | types.SendMessageEmojiInteractionSeen | types.SendMessageTextDraftAction,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePinnedMessages(TLObject):
    """
    [Read `updatePinnedMessages` docs](https://core.telegram.org/constructor/updatePinnedMessages).

    Generated from the following TL definition:
    ```tl
    updatePinnedMessages#ed85eab5 flags:# pinned:flags.0?true peer:Peer messages:Vector<int> pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        messages: Sequence[int],
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePinnedChannelMessages(TLObject):
    """
    [Read `updatePinnedChannelMessages` docs](https://core.telegram.org/constructor/updatePinnedChannelMessages).

    Generated from the following TL definition:
    ```tl
    updatePinnedChannelMessages#5bb98608 flags:# pinned:flags.0?true channel_id:long messages:Vector<int> pts:int pts_count:int = Update
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        channel_id: int,
        messages: Sequence[int],
        pts: int,
        pts_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChat(TLObject):
    """
    [Read `updateChat` docs](https://core.telegram.org/constructor/updateChat).

    Generated from the following TL definition:
    ```tl
    updateChat#f89a6a4e chat_id:long = Update
    ```
    """
    def __new__(
        cls,
        chat_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateGroupCallParticipants(TLObject):
    """
    [Read `updateGroupCallParticipants` docs](https://core.telegram.org/constructor/updateGroupCallParticipants).

    Generated from the following TL definition:
    ```tl
    updateGroupCallParticipants#f2ebdb4e call:InputGroupCall participants:Vector<GroupCallParticipant> version:int = Update
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        participants: Sequence[types.GroupCallParticipant],
        version: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateGroupCall(TLObject):
    """
    [Read `updateGroupCall` docs](https://core.telegram.org/constructor/updateGroupCall).

    Generated from the following TL definition:
    ```tl
    updateGroupCall#9d2216e0 flags:# live_story:flags.2?true peer:flags.1?Peer call:GroupCall = Update
    ```
    """
    def __new__(
        cls,
        live_story: bool,
        peer: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        call: types.GroupCallDiscarded | types.GroupCall,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePeerHistoryTtl(TLObject):
    """
    [Read `updatePeerHistoryTTL` docs](https://core.telegram.org/constructor/updatePeerHistoryTTL).

    Generated from the following TL definition:
    ```tl
    updatePeerHistoryTTL#bb9bb9a5 flags:# peer:Peer ttl_period:flags.0?int = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        ttl_period: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChatParticipant(TLObject):
    """
    [Read `updateChatParticipant` docs](https://core.telegram.org/constructor/updateChatParticipant).

    Generated from the following TL definition:
    ```tl
    updateChatParticipant#d087663a flags:# chat_id:long date:int actor_id:long user_id:long prev_participant:flags.0?ChatParticipant new_participant:flags.1?ChatParticipant invite:flags.2?ExportedChatInvite qts:int = Update
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        date: int,
        actor_id: int,
        user_id: int,
        prev_participant: Optional[types.ChatParticipant | types.ChatParticipantCreator | types.ChatParticipantAdmin],
        new_participant: Optional[types.ChatParticipant | types.ChatParticipantCreator | types.ChatParticipantAdmin],
        invite: Optional[types.ChatInviteExported | types.ChatInvitePublicJoinRequests],
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChannelParticipant(TLObject):
    """
    [Read `updateChannelParticipant` docs](https://core.telegram.org/constructor/updateChannelParticipant).

    Generated from the following TL definition:
    ```tl
    updateChannelParticipant#985d3abb flags:# via_chatlist:flags.3?true channel_id:long date:int actor_id:long user_id:long prev_participant:flags.0?ChannelParticipant new_participant:flags.1?ChannelParticipant invite:flags.2?ExportedChatInvite qts:int = Update
    ```
    """
    def __new__(
        cls,
        via_chatlist: bool,
        channel_id: int,
        date: int,
        actor_id: int,
        user_id: int,
        prev_participant: Optional[types.ChannelParticipant | types.ChannelParticipantSelf | types.ChannelParticipantCreator | types.ChannelParticipantAdmin | types.ChannelParticipantBanned | types.ChannelParticipantLeft],
        new_participant: Optional[types.ChannelParticipant | types.ChannelParticipantSelf | types.ChannelParticipantCreator | types.ChannelParticipantAdmin | types.ChannelParticipantBanned | types.ChannelParticipantLeft],
        invite: Optional[types.ChatInviteExported | types.ChatInvitePublicJoinRequests],
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotStopped(TLObject):
    """
    [Read `updateBotStopped` docs](https://core.telegram.org/constructor/updateBotStopped).

    Generated from the following TL definition:
    ```tl
    updateBotStopped#c4870a49 user_id:long date:int stopped:Bool qts:int = Update
    ```
    """
    def __new__(
        cls,
        user_id: int,
        date: int,
        stopped: bool,
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateGroupCallConnection(TLObject):
    """
    [Read `updateGroupCallConnection` docs](https://core.telegram.org/constructor/updateGroupCallConnection).

    Generated from the following TL definition:
    ```tl
    updateGroupCallConnection#b783982 flags:# presentation:flags.0?true params:DataJSON = Update
    ```
    """
    def __new__(
        cls,
        presentation: bool,
        params: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotCommands(TLObject):
    """
    [Read `updateBotCommands` docs](https://core.telegram.org/constructor/updateBotCommands).

    Generated from the following TL definition:
    ```tl
    updateBotCommands#4d712f2e peer:Peer bot_id:long commands:Vector<BotCommand> = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        bot_id: int,
        commands: Sequence[types.BotCommand],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePendingJoinRequests(TLObject):
    """
    [Read `updatePendingJoinRequests` docs](https://core.telegram.org/constructor/updatePendingJoinRequests).

    Generated from the following TL definition:
    ```tl
    updatePendingJoinRequests#7063c3db peer:Peer requests_pending:int recent_requesters:Vector<long> = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        requests_pending: int,
        recent_requesters: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotChatInviteRequester(TLObject):
    """
    [Read `updateBotChatInviteRequester` docs](https://core.telegram.org/constructor/updateBotChatInviteRequester).

    Generated from the following TL definition:
    ```tl
    updateBotChatInviteRequester#11dfa986 peer:Peer date:int user_id:long about:string invite:ExportedChatInvite qts:int = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        date: int,
        user_id: int,
        about: str,
        invite: types.ChatInviteExported | types.ChatInvitePublicJoinRequests,
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateMessageReactions(TLObject):
    """
    [Read `updateMessageReactions` docs](https://core.telegram.org/constructor/updateMessageReactions).

    Generated from the following TL definition:
    ```tl
    updateMessageReactions#1e297bfa flags:# peer:Peer msg_id:int top_msg_id:flags.0?int saved_peer_id:flags.1?Peer reactions:MessageReactions = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        msg_id: int,
        top_msg_id: Optional[int],
        saved_peer_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        reactions: types.MessageReactions,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateAttachMenuBots(TLObject):
    """
    [Read `updateAttachMenuBots` docs](https://core.telegram.org/constructor/updateAttachMenuBots).

    Generated from the following TL definition:
    ```tl
    updateAttachMenuBots#17b7a20b = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateWebViewResultSent(TLObject):
    """
    [Read `updateWebViewResultSent` docs](https://core.telegram.org/constructor/updateWebViewResultSent).

    Generated from the following TL definition:
    ```tl
    updateWebViewResultSent#1592b79d query_id:long = Update
    ```
    """
    def __new__(
        cls,
        query_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotMenuButton(TLObject):
    """
    [Read `updateBotMenuButton` docs](https://core.telegram.org/constructor/updateBotMenuButton).

    Generated from the following TL definition:
    ```tl
    updateBotMenuButton#14b85813 bot_id:long button:BotMenuButton = Update
    ```
    """
    def __new__(
        cls,
        bot_id: int,
        button: types.BotMenuButtonDefault | types.BotMenuButtonCommands | types.BotMenuButton,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateSavedRingtones(TLObject):
    """
    [Read `updateSavedRingtones` docs](https://core.telegram.org/constructor/updateSavedRingtones).

    Generated from the following TL definition:
    ```tl
    updateSavedRingtones#74d8be99 = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateTranscribedAudio(TLObject):
    """
    [Read `updateTranscribedAudio` docs](https://core.telegram.org/constructor/updateTranscribedAudio).

    Generated from the following TL definition:
    ```tl
    updateTranscribedAudio#84cd5a flags:# pending:flags.0?true peer:Peer msg_id:int transcription_id:long text:string = Update
    ```
    """
    def __new__(
        cls,
        pending: bool,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        msg_id: int,
        transcription_id: int,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateReadFeaturedEmojiStickers(TLObject):
    """
    [Read `updateReadFeaturedEmojiStickers` docs](https://core.telegram.org/constructor/updateReadFeaturedEmojiStickers).

    Generated from the following TL definition:
    ```tl
    updateReadFeaturedEmojiStickers#fb4c496c = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateUserEmojiStatus(TLObject):
    """
    [Read `updateUserEmojiStatus` docs](https://core.telegram.org/constructor/updateUserEmojiStatus).

    Generated from the following TL definition:
    ```tl
    updateUserEmojiStatus#28373599 user_id:long emoji_status:EmojiStatus = Update
    ```
    """
    def __new__(
        cls,
        user_id: int,
        emoji_status: types.EmojiStatusEmpty | types.EmojiStatus | types.EmojiStatusCollectible | types.InputEmojiStatusCollectible,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateRecentEmojiStatuses(TLObject):
    """
    [Read `updateRecentEmojiStatuses` docs](https://core.telegram.org/constructor/updateRecentEmojiStatuses).

    Generated from the following TL definition:
    ```tl
    updateRecentEmojiStatuses#30f443db = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateRecentReactions(TLObject):
    """
    [Read `updateRecentReactions` docs](https://core.telegram.org/constructor/updateRecentReactions).

    Generated from the following TL definition:
    ```tl
    updateRecentReactions#6f7863f4 = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateMoveStickerSetToTop(TLObject):
    """
    [Read `updateMoveStickerSetToTop` docs](https://core.telegram.org/constructor/updateMoveStickerSetToTop).

    Generated from the following TL definition:
    ```tl
    updateMoveStickerSetToTop#86fccf85 flags:# masks:flags.0?true emojis:flags.1?true stickerset:long = Update
    ```
    """
    def __new__(
        cls,
        masks: bool,
        emojis: bool,
        stickerset: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateMessageExtendedMedia(TLObject):
    """
    [Read `updateMessageExtendedMedia` docs](https://core.telegram.org/constructor/updateMessageExtendedMedia).

    Generated from the following TL definition:
    ```tl
    updateMessageExtendedMedia#d5a41724 peer:Peer msg_id:int extended_media:Vector<MessageExtendedMedia> = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        msg_id: int,
        extended_media: Sequence[types.MessageExtendedMediaPreview | types.MessageExtendedMedia],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateUser(TLObject):
    """
    [Read `updateUser` docs](https://core.telegram.org/constructor/updateUser).

    Generated from the following TL definition:
    ```tl
    updateUser#20529438 user_id:long = Update
    ```
    """
    def __new__(
        cls,
        user_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateAutoSaveSettings(TLObject):
    """
    [Read `updateAutoSaveSettings` docs](https://core.telegram.org/constructor/updateAutoSaveSettings).

    Generated from the following TL definition:
    ```tl
    updateAutoSaveSettings#ec05b097 = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStory(TLObject):
    """
    [Read `updateStory` docs](https://core.telegram.org/constructor/updateStory).

    Generated from the following TL definition:
    ```tl
    updateStory#75b3b798 peer:Peer story:StoryItem = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        story: types.StoryItemDeleted | types.StoryItemSkipped | types.StoryItem,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateReadStories(TLObject):
    """
    [Read `updateReadStories` docs](https://core.telegram.org/constructor/updateReadStories).

    Generated from the following TL definition:
    ```tl
    updateReadStories#f74e932b peer:Peer max_id:int = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStoryId(TLObject):
    """
    [Read `updateStoryID` docs](https://core.telegram.org/constructor/updateStoryID).

    Generated from the following TL definition:
    ```tl
    updateStoryID#1bf335b9 id:int random_id:long = Update
    ```
    """
    def __new__(
        cls,
        id: int,
        random_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStoriesStealthMode(TLObject):
    """
    [Read `updateStoriesStealthMode` docs](https://core.telegram.org/constructor/updateStoriesStealthMode).

    Generated from the following TL definition:
    ```tl
    updateStoriesStealthMode#2c084dc1 stealth_mode:StoriesStealthMode = Update
    ```
    """
    def __new__(
        cls,
        stealth_mode: types.StoriesStealthMode,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateSentStoryReaction(TLObject):
    """
    [Read `updateSentStoryReaction` docs](https://core.telegram.org/constructor/updateSentStoryReaction).

    Generated from the following TL definition:
    ```tl
    updateSentStoryReaction#7d627683 peer:Peer story_id:int reaction:Reaction = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        story_id: int,
        reaction: types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotChatBoost(TLObject):
    """
    [Read `updateBotChatBoost` docs](https://core.telegram.org/constructor/updateBotChatBoost).

    Generated from the following TL definition:
    ```tl
    updateBotChatBoost#904dd49c peer:Peer boost:Boost qts:int = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        boost: types.Boost,
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateChannelViewForumAsMessages(TLObject):
    """
    [Read `updateChannelViewForumAsMessages` docs](https://core.telegram.org/constructor/updateChannelViewForumAsMessages).

    Generated from the following TL definition:
    ```tl
    updateChannelViewForumAsMessages#7b68920 channel_id:long enabled:Bool = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        enabled: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePeerWallpaper(TLObject):
    """
    [Read `updatePeerWallpaper` docs](https://core.telegram.org/constructor/updatePeerWallpaper).

    Generated from the following TL definition:
    ```tl
    updatePeerWallpaper#ae3f101d flags:# wallpaper_overridden:flags.1?true peer:Peer wallpaper:flags.0?WallPaper = Update
    ```
    """
    def __new__(
        cls,
        wallpaper_overridden: bool,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        wallpaper: Optional[types.WallPaper | types.WallPaperNoFile],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotMessageReaction(TLObject):
    """
    [Read `updateBotMessageReaction` docs](https://core.telegram.org/constructor/updateBotMessageReaction).

    Generated from the following TL definition:
    ```tl
    updateBotMessageReaction#ac21d3ce peer:Peer msg_id:int date:int actor:Peer old_reactions:Vector<Reaction> new_reactions:Vector<Reaction> qts:int = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        msg_id: int,
        date: int,
        actor: types.PeerUser | types.PeerChat | types.PeerChannel,
        old_reactions: Sequence[types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid],
        new_reactions: Sequence[types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid],
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotMessageReactions(TLObject):
    """
    [Read `updateBotMessageReactions` docs](https://core.telegram.org/constructor/updateBotMessageReactions).

    Generated from the following TL definition:
    ```tl
    updateBotMessageReactions#9cb7759 peer:Peer msg_id:int date:int reactions:Vector<ReactionCount> qts:int = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        msg_id: int,
        date: int,
        reactions: Sequence[types.ReactionCount],
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateSavedDialogPinned(TLObject):
    """
    [Read `updateSavedDialogPinned` docs](https://core.telegram.org/constructor/updateSavedDialogPinned).

    Generated from the following TL definition:
    ```tl
    updateSavedDialogPinned#aeaf9e74 flags:# pinned:flags.0?true peer:DialogPeer = Update
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        peer: types.DialogPeer | types.DialogPeerFolder,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePinnedSavedDialogs(TLObject):
    """
    [Read `updatePinnedSavedDialogs` docs](https://core.telegram.org/constructor/updatePinnedSavedDialogs).

    Generated from the following TL definition:
    ```tl
    updatePinnedSavedDialogs#686c85a6 flags:# order:flags.0?Vector<DialogPeer> = Update
    ```
    """
    def __new__(
        cls,
        order: Optional[Sequence[types.DialogPeer | types.DialogPeerFolder]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateSavedReactionTags(TLObject):
    """
    [Read `updateSavedReactionTags` docs](https://core.telegram.org/constructor/updateSavedReactionTags).

    Generated from the following TL definition:
    ```tl
    updateSavedReactionTags#39c67432 = Update
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateSmsJob(TLObject):
    """
    [Read `updateSmsJob` docs](https://core.telegram.org/constructor/updateSmsJob).

    Generated from the following TL definition:
    ```tl
    updateSmsJob#f16269d4 job_id:string = Update
    ```
    """
    def __new__(
        cls,
        job_id: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateQuickReplies(TLObject):
    """
    [Read `updateQuickReplies` docs](https://core.telegram.org/constructor/updateQuickReplies).

    Generated from the following TL definition:
    ```tl
    updateQuickReplies#f9470ab2 quick_replies:Vector<QuickReply> = Update
    ```
    """
    def __new__(
        cls,
        quick_replies: Sequence[types.QuickReply],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateNewQuickReply(TLObject):
    """
    [Read `updateNewQuickReply` docs](https://core.telegram.org/constructor/updateNewQuickReply).

    Generated from the following TL definition:
    ```tl
    updateNewQuickReply#f53da717 quick_reply:QuickReply = Update
    ```
    """
    def __new__(
        cls,
        quick_reply: types.QuickReply,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDeleteQuickReply(TLObject):
    """
    [Read `updateDeleteQuickReply` docs](https://core.telegram.org/constructor/updateDeleteQuickReply).

    Generated from the following TL definition:
    ```tl
    updateDeleteQuickReply#53e6f1ec shortcut_id:int = Update
    ```
    """
    def __new__(
        cls,
        shortcut_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateQuickReplyMessage(TLObject):
    """
    [Read `updateQuickReplyMessage` docs](https://core.telegram.org/constructor/updateQuickReplyMessage).

    Generated from the following TL definition:
    ```tl
    updateQuickReplyMessage#3e050d0f message:Message = Update
    ```
    """
    def __new__(
        cls,
        message: types.MessageEmpty | types.Message | types.MessageService,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDeleteQuickReplyMessages(TLObject):
    """
    [Read `updateDeleteQuickReplyMessages` docs](https://core.telegram.org/constructor/updateDeleteQuickReplyMessages).

    Generated from the following TL definition:
    ```tl
    updateDeleteQuickReplyMessages#566fe7cd shortcut_id:int messages:Vector<int> = Update
    ```
    """
    def __new__(
        cls,
        shortcut_id: int,
        messages: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotBusinessConnect(TLObject):
    """
    [Read `updateBotBusinessConnect` docs](https://core.telegram.org/constructor/updateBotBusinessConnect).

    Generated from the following TL definition:
    ```tl
    updateBotBusinessConnect#8ae5c97a connection:BotBusinessConnection qts:int = Update
    ```
    """
    def __new__(
        cls,
        connection: types.BotBusinessConnection,
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotNewBusinessMessage(TLObject):
    """
    [Read `updateBotNewBusinessMessage` docs](https://core.telegram.org/constructor/updateBotNewBusinessMessage).

    Generated from the following TL definition:
    ```tl
    updateBotNewBusinessMessage#9ddb347c flags:# connection_id:string message:Message reply_to_message:flags.0?Message qts:int = Update
    ```
    """
    def __new__(
        cls,
        connection_id: str,
        message: types.MessageEmpty | types.Message | types.MessageService,
        reply_to_message: Optional[types.MessageEmpty | types.Message | types.MessageService],
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotEditBusinessMessage(TLObject):
    """
    [Read `updateBotEditBusinessMessage` docs](https://core.telegram.org/constructor/updateBotEditBusinessMessage).

    Generated from the following TL definition:
    ```tl
    updateBotEditBusinessMessage#7df587c flags:# connection_id:string message:Message reply_to_message:flags.0?Message qts:int = Update
    ```
    """
    def __new__(
        cls,
        connection_id: str,
        message: types.MessageEmpty | types.Message | types.MessageService,
        reply_to_message: Optional[types.MessageEmpty | types.Message | types.MessageService],
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotDeleteBusinessMessage(TLObject):
    """
    [Read `updateBotDeleteBusinessMessage` docs](https://core.telegram.org/constructor/updateBotDeleteBusinessMessage).

    Generated from the following TL definition:
    ```tl
    updateBotDeleteBusinessMessage#a02a982e connection_id:string peer:Peer messages:Vector<int> qts:int = Update
    ```
    """
    def __new__(
        cls,
        connection_id: str,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        messages: Sequence[int],
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateNewStoryReaction(TLObject):
    """
    [Read `updateNewStoryReaction` docs](https://core.telegram.org/constructor/updateNewStoryReaction).

    Generated from the following TL definition:
    ```tl
    updateNewStoryReaction#1824e40b story_id:int peer:Peer reaction:Reaction = Update
    ```
    """
    def __new__(
        cls,
        story_id: int,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        reaction: types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStarsBalance(TLObject):
    """
    [Read `updateStarsBalance` docs](https://core.telegram.org/constructor/updateStarsBalance).

    Generated from the following TL definition:
    ```tl
    updateStarsBalance#4e80a379 balance:StarsAmount = Update
    ```
    """
    def __new__(
        cls,
        balance: types.StarsAmount | types.StarsTonAmount,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBusinessBotCallbackQuery(TLObject):
    """
    [Read `updateBusinessBotCallbackQuery` docs](https://core.telegram.org/constructor/updateBusinessBotCallbackQuery).

    Generated from the following TL definition:
    ```tl
    updateBusinessBotCallbackQuery#1ea2fda7 flags:# query_id:long user_id:long connection_id:string message:Message reply_to_message:flags.2?Message chat_instance:long data:flags.0?bytes = Update
    ```
    """
    def __new__(
        cls,
        query_id: int,
        user_id: int,
        connection_id: str,
        message: types.MessageEmpty | types.Message | types.MessageService,
        reply_to_message: Optional[types.MessageEmpty | types.Message | types.MessageService],
        chat_instance: int,
        data: Optional[bytes],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStarsRevenueStatus(TLObject):
    """
    [Read `updateStarsRevenueStatus` docs](https://core.telegram.org/constructor/updateStarsRevenueStatus).

    Generated from the following TL definition:
    ```tl
    updateStarsRevenueStatus#a584b019 peer:Peer status:StarsRevenueStatus = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        status: types.StarsRevenueStatus,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateBotPurchasedPaidMedia(TLObject):
    """
    [Read `updateBotPurchasedPaidMedia` docs](https://core.telegram.org/constructor/updateBotPurchasedPaidMedia).

    Generated from the following TL definition:
    ```tl
    updateBotPurchasedPaidMedia#283bd312 user_id:long payload:string qts:int = Update
    ```
    """
    def __new__(
        cls,
        user_id: int,
        payload: str,
        qts: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePaidReactionPrivacy(TLObject):
    """
    [Read `updatePaidReactionPrivacy` docs](https://core.telegram.org/constructor/updatePaidReactionPrivacy).

    Generated from the following TL definition:
    ```tl
    updatePaidReactionPrivacy#8b725fce private:PaidReactionPrivacy = Update
    ```
    """
    def __new__(
        cls,
        private: types.PaidReactionPrivacyDefault | types.PaidReactionPrivacyAnonymous | types.PaidReactionPrivacyPeer,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateSentPhoneCode(TLObject):
    """
    [Read `updateSentPhoneCode` docs](https://core.telegram.org/constructor/updateSentPhoneCode).

    Generated from the following TL definition:
    ```tl
    updateSentPhoneCode#504aa18f sent_code:auth.SentCode = Update
    ```
    """
    def __new__(
        cls,
        sent_code: types.auth.SentCode | types.auth.SentCodeSuccess | types.auth.SentCodePaymentRequired,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateGroupCallChainBlocks(TLObject):
    """
    [Read `updateGroupCallChainBlocks` docs](https://core.telegram.org/constructor/updateGroupCallChainBlocks).

    Generated from the following TL definition:
    ```tl
    updateGroupCallChainBlocks#a477288f call:InputGroupCall sub_chain_id:int blocks:Vector<bytes> next_offset:int = Update
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        sub_chain_id: int,
        blocks: Sequence[bytes],
        next_offset: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateReadMonoForumInbox(TLObject):
    """
    [Read `updateReadMonoForumInbox` docs](https://core.telegram.org/constructor/updateReadMonoForumInbox).

    Generated from the following TL definition:
    ```tl
    updateReadMonoForumInbox#77b0e372 channel_id:long saved_peer_id:Peer read_max_id:int = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        saved_peer_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        read_max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateReadMonoForumOutbox(TLObject):
    """
    [Read `updateReadMonoForumOutbox` docs](https://core.telegram.org/constructor/updateReadMonoForumOutbox).

    Generated from the following TL definition:
    ```tl
    updateReadMonoForumOutbox#a4a79376 channel_id:long saved_peer_id:Peer read_max_id:int = Update
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        saved_peer_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        read_max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateMonoForumNoPaidException(TLObject):
    """
    [Read `updateMonoForumNoPaidException` docs](https://core.telegram.org/constructor/updateMonoForumNoPaidException).

    Generated from the following TL definition:
    ```tl
    updateMonoForumNoPaidException#9f812b08 flags:# exception:flags.0?true channel_id:long saved_peer_id:Peer = Update
    ```
    """
    def __new__(
        cls,
        exception: bool,
        channel_id: int,
        saved_peer_id: types.PeerUser | types.PeerChat | types.PeerChannel,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateGroupCallMessage(TLObject):
    """
    [Read `updateGroupCallMessage` docs](https://core.telegram.org/constructor/updateGroupCallMessage).

    Generated from the following TL definition:
    ```tl
    updateGroupCallMessage#d8326f0d call:InputGroupCall message:GroupCallMessage = Update
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        message: types.GroupCallMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateGroupCallEncryptedMessage(TLObject):
    """
    [Read `updateGroupCallEncryptedMessage` docs](https://core.telegram.org/constructor/updateGroupCallEncryptedMessage).

    Generated from the following TL definition:
    ```tl
    updateGroupCallEncryptedMessage#c957a766 call:InputGroupCall from_id:Peer encrypted_message:bytes = Update
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        from_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        encrypted_message: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePinnedForumTopic(TLObject):
    """
    [Read `updatePinnedForumTopic` docs](https://core.telegram.org/constructor/updatePinnedForumTopic).

    Generated from the following TL definition:
    ```tl
    updatePinnedForumTopic#683b2c52 flags:# pinned:flags.0?true peer:Peer topic_id:int = Update
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        topic_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatePinnedForumTopics(TLObject):
    """
    [Read `updatePinnedForumTopics` docs](https://core.telegram.org/constructor/updatePinnedForumTopics).

    Generated from the following TL definition:
    ```tl
    updatePinnedForumTopics#def143d0 flags:# peer:Peer order:flags.0?Vector<int> = Update
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        order: Optional[Sequence[int]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateDeleteGroupCallMessages(TLObject):
    """
    [Read `updateDeleteGroupCallMessages` docs](https://core.telegram.org/constructor/updateDeleteGroupCallMessages).

    Generated from the following TL definition:
    ```tl
    updateDeleteGroupCallMessages#3e85e92c call:InputGroupCall messages:Vector<int> = Update
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
        messages: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStarGiftAuctionState(TLObject):
    """
    [Read `updateStarGiftAuctionState` docs](https://core.telegram.org/constructor/updateStarGiftAuctionState).

    Generated from the following TL definition:
    ```tl
    updateStarGiftAuctionState#48e246c2 gift_id:long state:StarGiftAuctionState = Update
    ```
    """
    def __new__(
        cls,
        gift_id: int,
        state: types.StarGiftAuctionStateNotModified | types.StarGiftAuctionState | types.StarGiftAuctionStateFinished,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStarGiftAuctionUserState(TLObject):
    """
    [Read `updateStarGiftAuctionUserState` docs](https://core.telegram.org/constructor/updateStarGiftAuctionUserState).

    Generated from the following TL definition:
    ```tl
    updateStarGiftAuctionUserState#dc58f31e gift_id:long user_state:StarGiftAuctionUserState = Update
    ```
    """
    def __new__(
        cls,
        gift_id: int,
        user_state: types.StarGiftAuctionUserState,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateEmojiGameInfo(TLObject):
    """
    [Read `updateEmojiGameInfo` docs](https://core.telegram.org/constructor/updateEmojiGameInfo).

    Generated from the following TL definition:
    ```tl
    updateEmojiGameInfo#fb9c547a info:messages.EmojiGameInfo = Update
    ```
    """
    def __new__(
        cls,
        info: types.messages.EmojiGameUnavailable | types.messages.EmojiGameDiceInfo,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatesTooLong(TLObject):
    """
    [Read `updatesTooLong` docs](https://core.telegram.org/constructor/updatesTooLong).

    Generated from the following TL definition:
    ```tl
    updatesTooLong#e317af7e = Updates
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateShortMessage(TLObject):
    """
    [Read `updateShortMessage` docs](https://core.telegram.org/constructor/updateShortMessage).

    Generated from the following TL definition:
    ```tl
    updateShortMessage#313bc7f8 flags:# out:flags.1?true mentioned:flags.4?true media_unread:flags.5?true silent:flags.13?true id:int user_id:long message:string pts:int pts_count:int date:int fwd_from:flags.2?MessageFwdHeader via_bot_id:flags.11?long reply_to:flags.3?MessageReplyHeader entities:flags.7?Vector<MessageEntity> ttl_period:flags.25?int = Updates
    ```
    """
    def __new__(
        cls,
        out: bool,
        mentioned: bool,
        media_unread: bool,
        silent: bool,
        id: int,
        user_id: int,
        message: str,
        pts: int,
        pts_count: int,
        date: int,
        fwd_from: Optional[types.MessageFwdHeader],
        via_bot_id: Optional[int],
        reply_to: Optional[types.MessageReplyHeader | types.MessageReplyStoryHeader],
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        ttl_period: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateShortChatMessage(TLObject):
    """
    [Read `updateShortChatMessage` docs](https://core.telegram.org/constructor/updateShortChatMessage).

    Generated from the following TL definition:
    ```tl
    updateShortChatMessage#4d6deea5 flags:# out:flags.1?true mentioned:flags.4?true media_unread:flags.5?true silent:flags.13?true id:int from_id:long chat_id:long message:string pts:int pts_count:int date:int fwd_from:flags.2?MessageFwdHeader via_bot_id:flags.11?long reply_to:flags.3?MessageReplyHeader entities:flags.7?Vector<MessageEntity> ttl_period:flags.25?int = Updates
    ```
    """
    def __new__(
        cls,
        out: bool,
        mentioned: bool,
        media_unread: bool,
        silent: bool,
        id: int,
        from_id: int,
        chat_id: int,
        message: str,
        pts: int,
        pts_count: int,
        date: int,
        fwd_from: Optional[types.MessageFwdHeader],
        via_bot_id: Optional[int],
        reply_to: Optional[types.MessageReplyHeader | types.MessageReplyStoryHeader],
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        ttl_period: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateShort(TLObject):
    """
    [Read `updateShort` docs](https://core.telegram.org/constructor/updateShort).

    Generated from the following TL definition:
    ```tl
    updateShort#78d4dec1 update:Update date:int = Updates
    ```
    """
    def __new__(
        cls,
        update: types.UpdateNewMessage | types.UpdateMessageId | types.UpdateDeleteMessages | types.UpdateUserTyping | types.UpdateChatUserTyping | types.UpdateChatParticipants | types.UpdateUserStatus | types.UpdateUserName | types.UpdateNewAuthorization | types.UpdateNewEncryptedMessage | types.UpdateEncryptedChatTyping | types.UpdateEncryption | types.UpdateEncryptedMessagesRead | types.UpdateChatParticipantAdd | types.UpdateChatParticipantDelete | types.UpdateDcOptions | types.UpdateNotifySettings | types.UpdateServiceNotification | types.UpdatePrivacy | types.UpdateUserPhone | types.UpdateReadHistoryInbox | types.UpdateReadHistoryOutbox | types.UpdateWebPage | types.UpdateReadMessagesContents | types.UpdateChannelTooLong | types.UpdateChannel | types.UpdateNewChannelMessage | types.UpdateReadChannelInbox | types.UpdateDeleteChannelMessages | types.UpdateChannelMessageViews | types.UpdateChatParticipantAdmin | types.UpdateNewStickerSet | types.UpdateStickerSetsOrder | types.UpdateStickerSets | types.UpdateSavedGifs | types.UpdateBotInlineQuery | types.UpdateBotInlineSend | types.UpdateEditChannelMessage | types.UpdateBotCallbackQuery | types.UpdateEditMessage | types.UpdateInlineBotCallbackQuery | types.UpdateReadChannelOutbox | types.UpdateDraftMessage | types.UpdateReadFeaturedStickers | types.UpdateRecentStickers | types.UpdateConfig | types.UpdatePtsChanged | types.UpdateChannelWebPage | types.UpdateDialogPinned | types.UpdatePinnedDialogs | types.UpdateBotWebhookJson | types.UpdateBotWebhookJsonquery | types.UpdateBotShippingQuery | types.UpdateBotPrecheckoutQuery | types.UpdatePhoneCall | types.UpdateLangPackTooLong | types.UpdateLangPack | types.UpdateFavedStickers | types.UpdateChannelReadMessagesContents | types.UpdateContactsReset | types.UpdateChannelAvailableMessages | types.UpdateDialogUnreadMark | types.UpdateMessagePoll | types.UpdateChatDefaultBannedRights | types.UpdateFolderPeers | types.UpdatePeerSettings | types.UpdatePeerLocated | types.UpdateNewScheduledMessage | types.UpdateDeleteScheduledMessages | types.UpdateTheme | types.UpdateGeoLiveViewed | types.UpdateLoginToken | types.UpdateMessagePollVote | types.UpdateDialogFilter | types.UpdateDialogFilterOrder | types.UpdateDialogFilters | types.UpdatePhoneCallSignalingData | types.UpdateChannelMessageForwards | types.UpdateReadChannelDiscussionInbox | types.UpdateReadChannelDiscussionOutbox | types.UpdatePeerBlocked | types.UpdateChannelUserTyping | types.UpdatePinnedMessages | types.UpdatePinnedChannelMessages | types.UpdateChat | types.UpdateGroupCallParticipants | types.UpdateGroupCall | types.UpdatePeerHistoryTtl | types.UpdateChatParticipant | types.UpdateChannelParticipant | types.UpdateBotStopped | types.UpdateGroupCallConnection | types.UpdateBotCommands | types.UpdatePendingJoinRequests | types.UpdateBotChatInviteRequester | types.UpdateMessageReactions | types.UpdateAttachMenuBots | types.UpdateWebViewResultSent | types.UpdateBotMenuButton | types.UpdateSavedRingtones | types.UpdateTranscribedAudio | types.UpdateReadFeaturedEmojiStickers | types.UpdateUserEmojiStatus | types.UpdateRecentEmojiStatuses | types.UpdateRecentReactions | types.UpdateMoveStickerSetToTop | types.UpdateMessageExtendedMedia | types.UpdateUser | types.UpdateAutoSaveSettings | types.UpdateStory | types.UpdateReadStories | types.UpdateStoryId | types.UpdateStoriesStealthMode | types.UpdateSentStoryReaction | types.UpdateBotChatBoost | types.UpdateChannelViewForumAsMessages | types.UpdatePeerWallpaper | types.UpdateBotMessageReaction | types.UpdateBotMessageReactions | types.UpdateSavedDialogPinned | types.UpdatePinnedSavedDialogs | types.UpdateSavedReactionTags | types.UpdateSmsJob | types.UpdateQuickReplies | types.UpdateNewQuickReply | types.UpdateDeleteQuickReply | types.UpdateQuickReplyMessage | types.UpdateDeleteQuickReplyMessages | types.UpdateBotBusinessConnect | types.UpdateBotNewBusinessMessage | types.UpdateBotEditBusinessMessage | types.UpdateBotDeleteBusinessMessage | types.UpdateNewStoryReaction | types.UpdateStarsBalance | types.UpdateBusinessBotCallbackQuery | types.UpdateStarsRevenueStatus | types.UpdateBotPurchasedPaidMedia | types.UpdatePaidReactionPrivacy | types.UpdateSentPhoneCode | types.UpdateGroupCallChainBlocks | types.UpdateReadMonoForumInbox | types.UpdateReadMonoForumOutbox | types.UpdateMonoForumNoPaidException | types.UpdateGroupCallMessage | types.UpdateGroupCallEncryptedMessage | types.UpdatePinnedForumTopic | types.UpdatePinnedForumTopics | types.UpdateDeleteGroupCallMessages | types.UpdateStarGiftAuctionState | types.UpdateStarGiftAuctionUserState | types.UpdateEmojiGameInfo,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdatesCombined(TLObject):
    """
    [Read `updatesCombined` docs](https://core.telegram.org/constructor/updatesCombined).

    Generated from the following TL definition:
    ```tl
    updatesCombined#725b04c3 updates:Vector<Update> users:Vector<User> chats:Vector<Chat> date:int seq_start:int seq:int = Updates
    ```
    """
    def __new__(
        cls,
        updates: Sequence[types.UpdateNewMessage | types.UpdateMessageId | types.UpdateDeleteMessages | types.UpdateUserTyping | types.UpdateChatUserTyping | types.UpdateChatParticipants | types.UpdateUserStatus | types.UpdateUserName | types.UpdateNewAuthorization | types.UpdateNewEncryptedMessage | types.UpdateEncryptedChatTyping | types.UpdateEncryption | types.UpdateEncryptedMessagesRead | types.UpdateChatParticipantAdd | types.UpdateChatParticipantDelete | types.UpdateDcOptions | types.UpdateNotifySettings | types.UpdateServiceNotification | types.UpdatePrivacy | types.UpdateUserPhone | types.UpdateReadHistoryInbox | types.UpdateReadHistoryOutbox | types.UpdateWebPage | types.UpdateReadMessagesContents | types.UpdateChannelTooLong | types.UpdateChannel | types.UpdateNewChannelMessage | types.UpdateReadChannelInbox | types.UpdateDeleteChannelMessages | types.UpdateChannelMessageViews | types.UpdateChatParticipantAdmin | types.UpdateNewStickerSet | types.UpdateStickerSetsOrder | types.UpdateStickerSets | types.UpdateSavedGifs | types.UpdateBotInlineQuery | types.UpdateBotInlineSend | types.UpdateEditChannelMessage | types.UpdateBotCallbackQuery | types.UpdateEditMessage | types.UpdateInlineBotCallbackQuery | types.UpdateReadChannelOutbox | types.UpdateDraftMessage | types.UpdateReadFeaturedStickers | types.UpdateRecentStickers | types.UpdateConfig | types.UpdatePtsChanged | types.UpdateChannelWebPage | types.UpdateDialogPinned | types.UpdatePinnedDialogs | types.UpdateBotWebhookJson | types.UpdateBotWebhookJsonquery | types.UpdateBotShippingQuery | types.UpdateBotPrecheckoutQuery | types.UpdatePhoneCall | types.UpdateLangPackTooLong | types.UpdateLangPack | types.UpdateFavedStickers | types.UpdateChannelReadMessagesContents | types.UpdateContactsReset | types.UpdateChannelAvailableMessages | types.UpdateDialogUnreadMark | types.UpdateMessagePoll | types.UpdateChatDefaultBannedRights | types.UpdateFolderPeers | types.UpdatePeerSettings | types.UpdatePeerLocated | types.UpdateNewScheduledMessage | types.UpdateDeleteScheduledMessages | types.UpdateTheme | types.UpdateGeoLiveViewed | types.UpdateLoginToken | types.UpdateMessagePollVote | types.UpdateDialogFilter | types.UpdateDialogFilterOrder | types.UpdateDialogFilters | types.UpdatePhoneCallSignalingData | types.UpdateChannelMessageForwards | types.UpdateReadChannelDiscussionInbox | types.UpdateReadChannelDiscussionOutbox | types.UpdatePeerBlocked | types.UpdateChannelUserTyping | types.UpdatePinnedMessages | types.UpdatePinnedChannelMessages | types.UpdateChat | types.UpdateGroupCallParticipants | types.UpdateGroupCall | types.UpdatePeerHistoryTtl | types.UpdateChatParticipant | types.UpdateChannelParticipant | types.UpdateBotStopped | types.UpdateGroupCallConnection | types.UpdateBotCommands | types.UpdatePendingJoinRequests | types.UpdateBotChatInviteRequester | types.UpdateMessageReactions | types.UpdateAttachMenuBots | types.UpdateWebViewResultSent | types.UpdateBotMenuButton | types.UpdateSavedRingtones | types.UpdateTranscribedAudio | types.UpdateReadFeaturedEmojiStickers | types.UpdateUserEmojiStatus | types.UpdateRecentEmojiStatuses | types.UpdateRecentReactions | types.UpdateMoveStickerSetToTop | types.UpdateMessageExtendedMedia | types.UpdateUser | types.UpdateAutoSaveSettings | types.UpdateStory | types.UpdateReadStories | types.UpdateStoryId | types.UpdateStoriesStealthMode | types.UpdateSentStoryReaction | types.UpdateBotChatBoost | types.UpdateChannelViewForumAsMessages | types.UpdatePeerWallpaper | types.UpdateBotMessageReaction | types.UpdateBotMessageReactions | types.UpdateSavedDialogPinned | types.UpdatePinnedSavedDialogs | types.UpdateSavedReactionTags | types.UpdateSmsJob | types.UpdateQuickReplies | types.UpdateNewQuickReply | types.UpdateDeleteQuickReply | types.UpdateQuickReplyMessage | types.UpdateDeleteQuickReplyMessages | types.UpdateBotBusinessConnect | types.UpdateBotNewBusinessMessage | types.UpdateBotEditBusinessMessage | types.UpdateBotDeleteBusinessMessage | types.UpdateNewStoryReaction | types.UpdateStarsBalance | types.UpdateBusinessBotCallbackQuery | types.UpdateStarsRevenueStatus | types.UpdateBotPurchasedPaidMedia | types.UpdatePaidReactionPrivacy | types.UpdateSentPhoneCode | types.UpdateGroupCallChainBlocks | types.UpdateReadMonoForumInbox | types.UpdateReadMonoForumOutbox | types.UpdateMonoForumNoPaidException | types.UpdateGroupCallMessage | types.UpdateGroupCallEncryptedMessage | types.UpdatePinnedForumTopic | types.UpdatePinnedForumTopics | types.UpdateDeleteGroupCallMessages | types.UpdateStarGiftAuctionState | types.UpdateStarGiftAuctionUserState | types.UpdateEmojiGameInfo],
        users: Sequence[types.UserEmpty | types.User],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        date: int,
        seq_start: int,
        seq: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Updates(TLObject):
    """
    [Read `updates` docs](https://core.telegram.org/constructor/updates).

    Generated from the following TL definition:
    ```tl
    updates#74ae4240 updates:Vector<Update> users:Vector<User> chats:Vector<Chat> date:int seq:int = Updates
    ```
    """
    def __new__(
        cls,
        updates: Sequence[types.UpdateNewMessage | types.UpdateMessageId | types.UpdateDeleteMessages | types.UpdateUserTyping | types.UpdateChatUserTyping | types.UpdateChatParticipants | types.UpdateUserStatus | types.UpdateUserName | types.UpdateNewAuthorization | types.UpdateNewEncryptedMessage | types.UpdateEncryptedChatTyping | types.UpdateEncryption | types.UpdateEncryptedMessagesRead | types.UpdateChatParticipantAdd | types.UpdateChatParticipantDelete | types.UpdateDcOptions | types.UpdateNotifySettings | types.UpdateServiceNotification | types.UpdatePrivacy | types.UpdateUserPhone | types.UpdateReadHistoryInbox | types.UpdateReadHistoryOutbox | types.UpdateWebPage | types.UpdateReadMessagesContents | types.UpdateChannelTooLong | types.UpdateChannel | types.UpdateNewChannelMessage | types.UpdateReadChannelInbox | types.UpdateDeleteChannelMessages | types.UpdateChannelMessageViews | types.UpdateChatParticipantAdmin | types.UpdateNewStickerSet | types.UpdateStickerSetsOrder | types.UpdateStickerSets | types.UpdateSavedGifs | types.UpdateBotInlineQuery | types.UpdateBotInlineSend | types.UpdateEditChannelMessage | types.UpdateBotCallbackQuery | types.UpdateEditMessage | types.UpdateInlineBotCallbackQuery | types.UpdateReadChannelOutbox | types.UpdateDraftMessage | types.UpdateReadFeaturedStickers | types.UpdateRecentStickers | types.UpdateConfig | types.UpdatePtsChanged | types.UpdateChannelWebPage | types.UpdateDialogPinned | types.UpdatePinnedDialogs | types.UpdateBotWebhookJson | types.UpdateBotWebhookJsonquery | types.UpdateBotShippingQuery | types.UpdateBotPrecheckoutQuery | types.UpdatePhoneCall | types.UpdateLangPackTooLong | types.UpdateLangPack | types.UpdateFavedStickers | types.UpdateChannelReadMessagesContents | types.UpdateContactsReset | types.UpdateChannelAvailableMessages | types.UpdateDialogUnreadMark | types.UpdateMessagePoll | types.UpdateChatDefaultBannedRights | types.UpdateFolderPeers | types.UpdatePeerSettings | types.UpdatePeerLocated | types.UpdateNewScheduledMessage | types.UpdateDeleteScheduledMessages | types.UpdateTheme | types.UpdateGeoLiveViewed | types.UpdateLoginToken | types.UpdateMessagePollVote | types.UpdateDialogFilter | types.UpdateDialogFilterOrder | types.UpdateDialogFilters | types.UpdatePhoneCallSignalingData | types.UpdateChannelMessageForwards | types.UpdateReadChannelDiscussionInbox | types.UpdateReadChannelDiscussionOutbox | types.UpdatePeerBlocked | types.UpdateChannelUserTyping | types.UpdatePinnedMessages | types.UpdatePinnedChannelMessages | types.UpdateChat | types.UpdateGroupCallParticipants | types.UpdateGroupCall | types.UpdatePeerHistoryTtl | types.UpdateChatParticipant | types.UpdateChannelParticipant | types.UpdateBotStopped | types.UpdateGroupCallConnection | types.UpdateBotCommands | types.UpdatePendingJoinRequests | types.UpdateBotChatInviteRequester | types.UpdateMessageReactions | types.UpdateAttachMenuBots | types.UpdateWebViewResultSent | types.UpdateBotMenuButton | types.UpdateSavedRingtones | types.UpdateTranscribedAudio | types.UpdateReadFeaturedEmojiStickers | types.UpdateUserEmojiStatus | types.UpdateRecentEmojiStatuses | types.UpdateRecentReactions | types.UpdateMoveStickerSetToTop | types.UpdateMessageExtendedMedia | types.UpdateUser | types.UpdateAutoSaveSettings | types.UpdateStory | types.UpdateReadStories | types.UpdateStoryId | types.UpdateStoriesStealthMode | types.UpdateSentStoryReaction | types.UpdateBotChatBoost | types.UpdateChannelViewForumAsMessages | types.UpdatePeerWallpaper | types.UpdateBotMessageReaction | types.UpdateBotMessageReactions | types.UpdateSavedDialogPinned | types.UpdatePinnedSavedDialogs | types.UpdateSavedReactionTags | types.UpdateSmsJob | types.UpdateQuickReplies | types.UpdateNewQuickReply | types.UpdateDeleteQuickReply | types.UpdateQuickReplyMessage | types.UpdateDeleteQuickReplyMessages | types.UpdateBotBusinessConnect | types.UpdateBotNewBusinessMessage | types.UpdateBotEditBusinessMessage | types.UpdateBotDeleteBusinessMessage | types.UpdateNewStoryReaction | types.UpdateStarsBalance | types.UpdateBusinessBotCallbackQuery | types.UpdateStarsRevenueStatus | types.UpdateBotPurchasedPaidMedia | types.UpdatePaidReactionPrivacy | types.UpdateSentPhoneCode | types.UpdateGroupCallChainBlocks | types.UpdateReadMonoForumInbox | types.UpdateReadMonoForumOutbox | types.UpdateMonoForumNoPaidException | types.UpdateGroupCallMessage | types.UpdateGroupCallEncryptedMessage | types.UpdatePinnedForumTopic | types.UpdatePinnedForumTopics | types.UpdateDeleteGroupCallMessages | types.UpdateStarGiftAuctionState | types.UpdateStarGiftAuctionUserState | types.UpdateEmojiGameInfo],
        users: Sequence[types.UserEmpty | types.User],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        date: int,
        seq: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateShortSentMessage(TLObject):
    """
    [Read `updateShortSentMessage` docs](https://core.telegram.org/constructor/updateShortSentMessage).

    Generated from the following TL definition:
    ```tl
    updateShortSentMessage#9015e101 flags:# out:flags.1?true id:int pts:int pts_count:int date:int media:flags.9?MessageMedia entities:flags.7?Vector<MessageEntity> ttl_period:flags.25?int = Updates
    ```
    """
    def __new__(
        cls,
        out: bool,
        id: int,
        pts: int,
        pts_count: int,
        date: int,
        media: Optional[types.MessageMediaEmpty | types.MessageMediaPhoto | types.MessageMediaGeo | types.MessageMediaContact | types.MessageMediaUnsupported | types.MessageMediaDocument | types.MessageMediaWebPage | types.MessageMediaVenue | types.MessageMediaGame | types.MessageMediaInvoice | types.MessageMediaGeoLive | types.MessageMediaPoll | types.MessageMediaDice | types.MessageMediaStory | types.MessageMediaGiveaway | types.MessageMediaGiveawayResults | types.MessageMediaPaidMedia | types.MessageMediaToDo | types.MessageMediaVideoStream],
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        ttl_period: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DcOption(TLObject):
    """
    [Read `dcOption` docs](https://core.telegram.org/constructor/dcOption).

    Generated from the following TL definition:
    ```tl
    dcOption#18b7a10d flags:# ipv6:flags.0?true media_only:flags.1?true tcpo_only:flags.2?true cdn:flags.3?true static:flags.4?true this_port_only:flags.5?true id:int ip_address:string port:int secret:flags.10?bytes = DcOption
    ```
    """
    def __new__(
        cls,
        ipv6: bool,
        media_only: bool,
        tcpo_only: bool,
        cdn: bool,
        static: bool,
        this_port_only: bool,
        id: int,
        ip_address: str,
        port: int,
        secret: Optional[bytes],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Config(TLObject):
    """
    [Read `config` docs](https://core.telegram.org/constructor/config).

    Generated from the following TL definition:
    ```tl
    config#cc1a241e flags:# default_p2p_contacts:flags.3?true preload_featured_stickers:flags.4?true revoke_pm_inbox:flags.6?true blocked_mode:flags.8?true force_try_ipv6:flags.14?true date:int expires:int test_mode:Bool this_dc:int dc_options:Vector<DcOption> dc_txt_domain_name:string chat_size_max:int megagroup_size_max:int forwarded_count_max:int online_update_period_ms:int offline_blur_timeout_ms:int offline_idle_timeout_ms:int online_cloud_timeout_ms:int notify_cloud_delay_ms:int notify_default_delay_ms:int push_chat_period_ms:int push_chat_limit:int edit_time_limit:int revoke_time_limit:int revoke_pm_time_limit:int rating_e_decay:int stickers_recent_limit:int channels_read_media_period:int tmp_sessions:flags.0?int call_receive_timeout_ms:int call_ring_timeout_ms:int call_connect_timeout_ms:int call_packet_timeout_ms:int me_url_prefix:string autoupdate_url_prefix:flags.7?string gif_search_username:flags.9?string venue_search_username:flags.10?string img_search_username:flags.11?string static_maps_provider:flags.12?string caption_length_max:int message_length_max:int webfile_dc_id:int suggested_lang_code:flags.2?string lang_pack_version:flags.2?int base_lang_pack_version:flags.2?int reactions_default:flags.15?Reaction autologin_token:flags.16?string = Config
    ```
    """
    def __new__(
        cls,
        default_p2p_contacts: bool,
        preload_featured_stickers: bool,
        revoke_pm_inbox: bool,
        blocked_mode: bool,
        force_try_ipv6: bool,
        date: int,
        expires: int,
        test_mode: bool,
        this_dc: int,
        dc_options: Sequence[types.DcOption],
        dc_txt_domain_name: str,
        chat_size_max: int,
        megagroup_size_max: int,
        forwarded_count_max: int,
        online_update_period_ms: int,
        offline_blur_timeout_ms: int,
        offline_idle_timeout_ms: int,
        online_cloud_timeout_ms: int,
        notify_cloud_delay_ms: int,
        notify_default_delay_ms: int,
        push_chat_period_ms: int,
        push_chat_limit: int,
        edit_time_limit: int,
        revoke_time_limit: int,
        revoke_pm_time_limit: int,
        rating_e_decay: int,
        stickers_recent_limit: int,
        channels_read_media_period: int,
        tmp_sessions: Optional[int],
        call_receive_timeout_ms: int,
        call_ring_timeout_ms: int,
        call_connect_timeout_ms: int,
        call_packet_timeout_ms: int,
        me_url_prefix: str,
        autoupdate_url_prefix: Optional[str],
        gif_search_username: Optional[str],
        venue_search_username: Optional[str],
        img_search_username: Optional[str],
        static_maps_provider: Optional[str],
        caption_length_max: int,
        message_length_max: int,
        webfile_dc_id: int,
        suggested_lang_code: Optional[str],
        lang_pack_version: Optional[int],
        base_lang_pack_version: Optional[int],
        reactions_default: Optional[types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid],
        autologin_token: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class NearestDc(TLObject):
    """
    [Read `nearestDc` docs](https://core.telegram.org/constructor/nearestDc).

    Generated from the following TL definition:
    ```tl
    nearestDc#8e1a1775 country:string this_dc:int nearest_dc:int = NearestDc
    ```
    """
    def __new__(
        cls,
        country: str,
        this_dc: int,
        nearest_dc: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EncryptedChatEmpty(TLObject):
    """
    [Read `encryptedChatEmpty` docs](https://core.telegram.org/constructor/encryptedChatEmpty).

    Generated from the following TL definition:
    ```tl
    encryptedChatEmpty#ab7ec0a0 id:int = EncryptedChat
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EncryptedChatWaiting(TLObject):
    """
    [Read `encryptedChatWaiting` docs](https://core.telegram.org/constructor/encryptedChatWaiting).

    Generated from the following TL definition:
    ```tl
    encryptedChatWaiting#66b25953 id:int access_hash:long date:int admin_id:long participant_id:long = EncryptedChat
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        date: int,
        admin_id: int,
        participant_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EncryptedChatRequested(TLObject):
    """
    [Read `encryptedChatRequested` docs](https://core.telegram.org/constructor/encryptedChatRequested).

    Generated from the following TL definition:
    ```tl
    encryptedChatRequested#48f1d94c flags:# folder_id:flags.0?int id:int access_hash:long date:int admin_id:long participant_id:long g_a:bytes = EncryptedChat
    ```
    """
    def __new__(
        cls,
        folder_id: Optional[int],
        id: int,
        access_hash: int,
        date: int,
        admin_id: int,
        participant_id: int,
        g_a: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EncryptedChat(TLObject):
    """
    [Read `encryptedChat` docs](https://core.telegram.org/constructor/encryptedChat).

    Generated from the following TL definition:
    ```tl
    encryptedChat#61f0d4c7 id:int access_hash:long date:int admin_id:long participant_id:long g_a_or_b:bytes key_fingerprint:long = EncryptedChat
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        date: int,
        admin_id: int,
        participant_id: int,
        g_a_or_b: bytes,
        key_fingerprint: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EncryptedChatDiscarded(TLObject):
    """
    [Read `encryptedChatDiscarded` docs](https://core.telegram.org/constructor/encryptedChatDiscarded).

    Generated from the following TL definition:
    ```tl
    encryptedChatDiscarded#1e1c7c45 flags:# history_deleted:flags.0?true id:int = EncryptedChat
    ```
    """
    def __new__(
        cls,
        history_deleted: bool,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputEncryptedChat(TLObject):
    """
    [Read `inputEncryptedChat` docs](https://core.telegram.org/constructor/inputEncryptedChat).

    Generated from the following TL definition:
    ```tl
    inputEncryptedChat#f141b5e1 chat_id:int access_hash:long = InputEncryptedChat
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EncryptedFileEmpty(TLObject):
    """
    [Read `encryptedFileEmpty` docs](https://core.telegram.org/constructor/encryptedFileEmpty).

    Generated from the following TL definition:
    ```tl
    encryptedFileEmpty#c21f497e = EncryptedFile
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EncryptedFile(TLObject):
    """
    [Read `encryptedFile` docs](https://core.telegram.org/constructor/encryptedFile).

    Generated from the following TL definition:
    ```tl
    encryptedFile#a8008cd8 id:long access_hash:long size:long dc_id:int key_fingerprint:int = EncryptedFile
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        size: int,
        dc_id: int,
        key_fingerprint: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputEncryptedFileEmpty(TLObject):
    """
    [Read `inputEncryptedFileEmpty` docs](https://core.telegram.org/constructor/inputEncryptedFileEmpty).

    Generated from the following TL definition:
    ```tl
    inputEncryptedFileEmpty#1837c364 = InputEncryptedFile
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputEncryptedFileUploaded(TLObject):
    """
    [Read `inputEncryptedFileUploaded` docs](https://core.telegram.org/constructor/inputEncryptedFileUploaded).

    Generated from the following TL definition:
    ```tl
    inputEncryptedFileUploaded#64bd0306 id:long parts:int md5_checksum:string key_fingerprint:int = InputEncryptedFile
    ```
    """
    def __new__(
        cls,
        id: int,
        parts: int,
        md5_checksum: str,
        key_fingerprint: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputEncryptedFile(TLObject):
    """
    [Read `inputEncryptedFile` docs](https://core.telegram.org/constructor/inputEncryptedFile).

    Generated from the following TL definition:
    ```tl
    inputEncryptedFile#5a17b5e5 id:long access_hash:long = InputEncryptedFile
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputEncryptedFileBigUploaded(TLObject):
    """
    [Read `inputEncryptedFileBigUploaded` docs](https://core.telegram.org/constructor/inputEncryptedFileBigUploaded).

    Generated from the following TL definition:
    ```tl
    inputEncryptedFileBigUploaded#2dc173c8 id:long parts:int key_fingerprint:int = InputEncryptedFile
    ```
    """
    def __new__(
        cls,
        id: int,
        parts: int,
        key_fingerprint: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EncryptedMessage(TLObject):
    """
    [Read `encryptedMessage` docs](https://core.telegram.org/constructor/encryptedMessage).

    Generated from the following TL definition:
    ```tl
    encryptedMessage#ed18c118 random_id:long chat_id:int date:int bytes:bytes file:EncryptedFile = EncryptedMessage
    ```
    """
    def __new__(
        cls,
        random_id: int,
        chat_id: int,
        date: int,
        bytes: bytes,
        file: types.EncryptedFileEmpty | types.EncryptedFile,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EncryptedMessageService(TLObject):
    """
    [Read `encryptedMessageService` docs](https://core.telegram.org/constructor/encryptedMessageService).

    Generated from the following TL definition:
    ```tl
    encryptedMessageService#23734b06 random_id:long chat_id:int date:int bytes:bytes = EncryptedMessage
    ```
    """
    def __new__(
        cls,
        random_id: int,
        chat_id: int,
        date: int,
        bytes: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputDocumentEmpty(TLObject):
    """
    [Read `inputDocumentEmpty` docs](https://core.telegram.org/constructor/inputDocumentEmpty).

    Generated from the following TL definition:
    ```tl
    inputDocumentEmpty#72f0eaae = InputDocument
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputDocument(TLObject):
    """
    [Read `inputDocument` docs](https://core.telegram.org/constructor/inputDocument).

    Generated from the following TL definition:
    ```tl
    inputDocument#1abfb575 id:long access_hash:long file_reference:bytes = InputDocument
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        file_reference: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DocumentEmpty(TLObject):
    """
    [Read `documentEmpty` docs](https://core.telegram.org/constructor/documentEmpty).

    Generated from the following TL definition:
    ```tl
    documentEmpty#36f8c871 id:long = Document
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Document(TLObject):
    """
    [Read `document` docs](https://core.telegram.org/constructor/document).

    Generated from the following TL definition:
    ```tl
    document#8fd4c4d8 flags:# id:long access_hash:long file_reference:bytes date:int mime_type:string size:long thumbs:flags.0?Vector<PhotoSize> video_thumbs:flags.1?Vector<VideoSize> dc_id:int attributes:Vector<DocumentAttribute> = Document
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        file_reference: bytes,
        date: int,
        mime_type: str,
        size: int,
        thumbs: Optional[Sequence[types.PhotoSizeEmpty | types.PhotoSize | types.PhotoCachedSize | types.PhotoStrippedSize | types.PhotoSizeProgressive | types.PhotoPathSize]],
        video_thumbs: Optional[Sequence[types.VideoSize | types.VideoSizeEmojiMarkup | types.VideoSizeStickerMarkup]],
        dc_id: int,
        attributes: Sequence[types.DocumentAttributeImageSize | types.DocumentAttributeAnimated | types.DocumentAttributeSticker | types.DocumentAttributeVideo | types.DocumentAttributeAudio | types.DocumentAttributeFilename | types.DocumentAttributeHasStickers | types.DocumentAttributeCustomEmoji],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class NotifyPeer(TLObject):
    """
    [Read `notifyPeer` docs](https://core.telegram.org/constructor/notifyPeer).

    Generated from the following TL definition:
    ```tl
    notifyPeer#9fd40bd8 peer:Peer = NotifyPeer
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class NotifyUsers(TLObject):
    """
    [Read `notifyUsers` docs](https://core.telegram.org/constructor/notifyUsers).

    Generated from the following TL definition:
    ```tl
    notifyUsers#b4c83b4c = NotifyPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class NotifyChats(TLObject):
    """
    [Read `notifyChats` docs](https://core.telegram.org/constructor/notifyChats).

    Generated from the following TL definition:
    ```tl
    notifyChats#c007cec3 = NotifyPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class NotifyBroadcasts(TLObject):
    """
    [Read `notifyBroadcasts` docs](https://core.telegram.org/constructor/notifyBroadcasts).

    Generated from the following TL definition:
    ```tl
    notifyBroadcasts#d612e8ef = NotifyPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class NotifyForumTopic(TLObject):
    """
    [Read `notifyForumTopic` docs](https://core.telegram.org/constructor/notifyForumTopic).

    Generated from the following TL definition:
    ```tl
    notifyForumTopic#226e6308 peer:Peer top_msg_id:int = NotifyPeer
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        top_msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageTypingAction(TLObject):
    """
    [Read `sendMessageTypingAction` docs](https://core.telegram.org/constructor/sendMessageTypingAction).

    Generated from the following TL definition:
    ```tl
    sendMessageTypingAction#16bf744e = SendMessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageCancelAction(TLObject):
    """
    [Read `sendMessageCancelAction` docs](https://core.telegram.org/constructor/sendMessageCancelAction).

    Generated from the following TL definition:
    ```tl
    sendMessageCancelAction#fd5ec8f5 = SendMessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageRecordVideoAction(TLObject):
    """
    [Read `sendMessageRecordVideoAction` docs](https://core.telegram.org/constructor/sendMessageRecordVideoAction).

    Generated from the following TL definition:
    ```tl
    sendMessageRecordVideoAction#a187d66f = SendMessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageUploadVideoAction(TLObject):
    """
    [Read `sendMessageUploadVideoAction` docs](https://core.telegram.org/constructor/sendMessageUploadVideoAction).

    Generated from the following TL definition:
    ```tl
    sendMessageUploadVideoAction#e9763aec progress:int = SendMessageAction
    ```
    """
    def __new__(
        cls,
        progress: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageRecordAudioAction(TLObject):
    """
    [Read `sendMessageRecordAudioAction` docs](https://core.telegram.org/constructor/sendMessageRecordAudioAction).

    Generated from the following TL definition:
    ```tl
    sendMessageRecordAudioAction#d52f73f7 = SendMessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageUploadAudioAction(TLObject):
    """
    [Read `sendMessageUploadAudioAction` docs](https://core.telegram.org/constructor/sendMessageUploadAudioAction).

    Generated from the following TL definition:
    ```tl
    sendMessageUploadAudioAction#f351d7ab progress:int = SendMessageAction
    ```
    """
    def __new__(
        cls,
        progress: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageUploadPhotoAction(TLObject):
    """
    [Read `sendMessageUploadPhotoAction` docs](https://core.telegram.org/constructor/sendMessageUploadPhotoAction).

    Generated from the following TL definition:
    ```tl
    sendMessageUploadPhotoAction#d1d34a26 progress:int = SendMessageAction
    ```
    """
    def __new__(
        cls,
        progress: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageUploadDocumentAction(TLObject):
    """
    [Read `sendMessageUploadDocumentAction` docs](https://core.telegram.org/constructor/sendMessageUploadDocumentAction).

    Generated from the following TL definition:
    ```tl
    sendMessageUploadDocumentAction#aa0cd9e4 progress:int = SendMessageAction
    ```
    """
    def __new__(
        cls,
        progress: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageGeoLocationAction(TLObject):
    """
    [Read `sendMessageGeoLocationAction` docs](https://core.telegram.org/constructor/sendMessageGeoLocationAction).

    Generated from the following TL definition:
    ```tl
    sendMessageGeoLocationAction#176f8ba1 = SendMessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageChooseContactAction(TLObject):
    """
    [Read `sendMessageChooseContactAction` docs](https://core.telegram.org/constructor/sendMessageChooseContactAction).

    Generated from the following TL definition:
    ```tl
    sendMessageChooseContactAction#628cbc6f = SendMessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageGamePlayAction(TLObject):
    """
    [Read `sendMessageGamePlayAction` docs](https://core.telegram.org/constructor/sendMessageGamePlayAction).

    Generated from the following TL definition:
    ```tl
    sendMessageGamePlayAction#dd6a8f48 = SendMessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageRecordRoundAction(TLObject):
    """
    [Read `sendMessageRecordRoundAction` docs](https://core.telegram.org/constructor/sendMessageRecordRoundAction).

    Generated from the following TL definition:
    ```tl
    sendMessageRecordRoundAction#88f27fbc = SendMessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageUploadRoundAction(TLObject):
    """
    [Read `sendMessageUploadRoundAction` docs](https://core.telegram.org/constructor/sendMessageUploadRoundAction).

    Generated from the following TL definition:
    ```tl
    sendMessageUploadRoundAction#243e1c66 progress:int = SendMessageAction
    ```
    """
    def __new__(
        cls,
        progress: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SpeakingInGroupCallAction(TLObject):
    """
    [Read `speakingInGroupCallAction` docs](https://core.telegram.org/constructor/speakingInGroupCallAction).

    Generated from the following TL definition:
    ```tl
    speakingInGroupCallAction#d92c2285 = SendMessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageHistoryImportAction(TLObject):
    """
    [Read `sendMessageHistoryImportAction` docs](https://core.telegram.org/constructor/sendMessageHistoryImportAction).

    Generated from the following TL definition:
    ```tl
    sendMessageHistoryImportAction#dbda9246 progress:int = SendMessageAction
    ```
    """
    def __new__(
        cls,
        progress: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageChooseStickerAction(TLObject):
    """
    [Read `sendMessageChooseStickerAction` docs](https://core.telegram.org/constructor/sendMessageChooseStickerAction).

    Generated from the following TL definition:
    ```tl
    sendMessageChooseStickerAction#b05ac6b1 = SendMessageAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageEmojiInteraction(TLObject):
    """
    [Read `sendMessageEmojiInteraction` docs](https://core.telegram.org/constructor/sendMessageEmojiInteraction).

    Generated from the following TL definition:
    ```tl
    sendMessageEmojiInteraction#25972bcb emoticon:string msg_id:int interaction:DataJSON = SendMessageAction
    ```
    """
    def __new__(
        cls,
        emoticon: str,
        msg_id: int,
        interaction: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageEmojiInteractionSeen(TLObject):
    """
    [Read `sendMessageEmojiInteractionSeen` docs](https://core.telegram.org/constructor/sendMessageEmojiInteractionSeen).

    Generated from the following TL definition:
    ```tl
    sendMessageEmojiInteractionSeen#b665902e emoticon:string = SendMessageAction
    ```
    """
    def __new__(
        cls,
        emoticon: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendMessageTextDraftAction(TLObject):
    """
    [Read `sendMessageTextDraftAction` docs](https://core.telegram.org/constructor/sendMessageTextDraftAction).

    Generated from the following TL definition:
    ```tl
    sendMessageTextDraftAction#376d975c random_id:long text:TextWithEntities = SendMessageAction
    ```
    """
    def __new__(
        cls,
        random_id: int,
        text: types.TextWithEntities,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyStatusTimestamp(TLObject):
    """
    [Read `inputPrivacyKeyStatusTimestamp` docs](https://core.telegram.org/constructor/inputPrivacyKeyStatusTimestamp).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyStatusTimestamp#4f96cb18 = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyChatInvite(TLObject):
    """
    [Read `inputPrivacyKeyChatInvite` docs](https://core.telegram.org/constructor/inputPrivacyKeyChatInvite).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyChatInvite#bdfb0426 = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyPhoneCall(TLObject):
    """
    [Read `inputPrivacyKeyPhoneCall` docs](https://core.telegram.org/constructor/inputPrivacyKeyPhoneCall).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyPhoneCall#fabadc5f = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyPhoneP2P(TLObject):
    """
    [Read `inputPrivacyKeyPhoneP2P` docs](https://core.telegram.org/constructor/inputPrivacyKeyPhoneP2P).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyPhoneP2P#db9e70d2 = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyForwards(TLObject):
    """
    [Read `inputPrivacyKeyForwards` docs](https://core.telegram.org/constructor/inputPrivacyKeyForwards).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyForwards#a4dd4c08 = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyProfilePhoto(TLObject):
    """
    [Read `inputPrivacyKeyProfilePhoto` docs](https://core.telegram.org/constructor/inputPrivacyKeyProfilePhoto).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyProfilePhoto#5719bacc = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyPhoneNumber(TLObject):
    """
    [Read `inputPrivacyKeyPhoneNumber` docs](https://core.telegram.org/constructor/inputPrivacyKeyPhoneNumber).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyPhoneNumber#352dafa = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyAddedByPhone(TLObject):
    """
    [Read `inputPrivacyKeyAddedByPhone` docs](https://core.telegram.org/constructor/inputPrivacyKeyAddedByPhone).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyAddedByPhone#d1219bdd = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyVoiceMessages(TLObject):
    """
    [Read `inputPrivacyKeyVoiceMessages` docs](https://core.telegram.org/constructor/inputPrivacyKeyVoiceMessages).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyVoiceMessages#aee69d68 = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyAbout(TLObject):
    """
    [Read `inputPrivacyKeyAbout` docs](https://core.telegram.org/constructor/inputPrivacyKeyAbout).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyAbout#3823cc40 = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyBirthday(TLObject):
    """
    [Read `inputPrivacyKeyBirthday` docs](https://core.telegram.org/constructor/inputPrivacyKeyBirthday).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyBirthday#d65a11cc = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyStarGiftsAutoSave(TLObject):
    """
    [Read `inputPrivacyKeyStarGiftsAutoSave` docs](https://core.telegram.org/constructor/inputPrivacyKeyStarGiftsAutoSave).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyStarGiftsAutoSave#e1732341 = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeyNoPaidMessages(TLObject):
    """
    [Read `inputPrivacyKeyNoPaidMessages` docs](https://core.telegram.org/constructor/inputPrivacyKeyNoPaidMessages).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeyNoPaidMessages#bdc597b4 = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyKeySavedMusic(TLObject):
    """
    [Read `inputPrivacyKeySavedMusic` docs](https://core.telegram.org/constructor/inputPrivacyKeySavedMusic).

    Generated from the following TL definition:
    ```tl
    inputPrivacyKeySavedMusic#4dbe9226 = InputPrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyStatusTimestamp(TLObject):
    """
    [Read `privacyKeyStatusTimestamp` docs](https://core.telegram.org/constructor/privacyKeyStatusTimestamp).

    Generated from the following TL definition:
    ```tl
    privacyKeyStatusTimestamp#bc2eab30 = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyChatInvite(TLObject):
    """
    [Read `privacyKeyChatInvite` docs](https://core.telegram.org/constructor/privacyKeyChatInvite).

    Generated from the following TL definition:
    ```tl
    privacyKeyChatInvite#500e6dfa = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyPhoneCall(TLObject):
    """
    [Read `privacyKeyPhoneCall` docs](https://core.telegram.org/constructor/privacyKeyPhoneCall).

    Generated from the following TL definition:
    ```tl
    privacyKeyPhoneCall#3d662b7b = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyPhoneP2P(TLObject):
    """
    [Read `privacyKeyPhoneP2P` docs](https://core.telegram.org/constructor/privacyKeyPhoneP2P).

    Generated from the following TL definition:
    ```tl
    privacyKeyPhoneP2P#39491cc8 = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyForwards(TLObject):
    """
    [Read `privacyKeyForwards` docs](https://core.telegram.org/constructor/privacyKeyForwards).

    Generated from the following TL definition:
    ```tl
    privacyKeyForwards#69ec56a3 = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyProfilePhoto(TLObject):
    """
    [Read `privacyKeyProfilePhoto` docs](https://core.telegram.org/constructor/privacyKeyProfilePhoto).

    Generated from the following TL definition:
    ```tl
    privacyKeyProfilePhoto#96151fed = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyPhoneNumber(TLObject):
    """
    [Read `privacyKeyPhoneNumber` docs](https://core.telegram.org/constructor/privacyKeyPhoneNumber).

    Generated from the following TL definition:
    ```tl
    privacyKeyPhoneNumber#d19ae46d = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyAddedByPhone(TLObject):
    """
    [Read `privacyKeyAddedByPhone` docs](https://core.telegram.org/constructor/privacyKeyAddedByPhone).

    Generated from the following TL definition:
    ```tl
    privacyKeyAddedByPhone#42ffd42b = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyVoiceMessages(TLObject):
    """
    [Read `privacyKeyVoiceMessages` docs](https://core.telegram.org/constructor/privacyKeyVoiceMessages).

    Generated from the following TL definition:
    ```tl
    privacyKeyVoiceMessages#697f414 = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyAbout(TLObject):
    """
    [Read `privacyKeyAbout` docs](https://core.telegram.org/constructor/privacyKeyAbout).

    Generated from the following TL definition:
    ```tl
    privacyKeyAbout#a486b761 = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyBirthday(TLObject):
    """
    [Read `privacyKeyBirthday` docs](https://core.telegram.org/constructor/privacyKeyBirthday).

    Generated from the following TL definition:
    ```tl
    privacyKeyBirthday#2000a518 = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyStarGiftsAutoSave(TLObject):
    """
    [Read `privacyKeyStarGiftsAutoSave` docs](https://core.telegram.org/constructor/privacyKeyStarGiftsAutoSave).

    Generated from the following TL definition:
    ```tl
    privacyKeyStarGiftsAutoSave#2ca4fdf8 = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeyNoPaidMessages(TLObject):
    """
    [Read `privacyKeyNoPaidMessages` docs](https://core.telegram.org/constructor/privacyKeyNoPaidMessages).

    Generated from the following TL definition:
    ```tl
    privacyKeyNoPaidMessages#17d348d2 = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyKeySavedMusic(TLObject):
    """
    [Read `privacyKeySavedMusic` docs](https://core.telegram.org/constructor/privacyKeySavedMusic).

    Generated from the following TL definition:
    ```tl
    privacyKeySavedMusic#ff7a571b = PrivacyKey
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyValueAllowContacts(TLObject):
    """
    [Read `inputPrivacyValueAllowContacts` docs](https://core.telegram.org/constructor/inputPrivacyValueAllowContacts).

    Generated from the following TL definition:
    ```tl
    inputPrivacyValueAllowContacts#d09e07b = InputPrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyValueAllowAll(TLObject):
    """
    [Read `inputPrivacyValueAllowAll` docs](https://core.telegram.org/constructor/inputPrivacyValueAllowAll).

    Generated from the following TL definition:
    ```tl
    inputPrivacyValueAllowAll#184b35ce = InputPrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyValueAllowUsers(TLObject):
    """
    [Read `inputPrivacyValueAllowUsers` docs](https://core.telegram.org/constructor/inputPrivacyValueAllowUsers).

    Generated from the following TL definition:
    ```tl
    inputPrivacyValueAllowUsers#131cc67f users:Vector<InputUser> = InputPrivacyRule
    ```
    """
    def __new__(
        cls,
        users: Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyValueDisallowContacts(TLObject):
    """
    [Read `inputPrivacyValueDisallowContacts` docs](https://core.telegram.org/constructor/inputPrivacyValueDisallowContacts).

    Generated from the following TL definition:
    ```tl
    inputPrivacyValueDisallowContacts#ba52007 = InputPrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyValueDisallowAll(TLObject):
    """
    [Read `inputPrivacyValueDisallowAll` docs](https://core.telegram.org/constructor/inputPrivacyValueDisallowAll).

    Generated from the following TL definition:
    ```tl
    inputPrivacyValueDisallowAll#d66b66c9 = InputPrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyValueDisallowUsers(TLObject):
    """
    [Read `inputPrivacyValueDisallowUsers` docs](https://core.telegram.org/constructor/inputPrivacyValueDisallowUsers).

    Generated from the following TL definition:
    ```tl
    inputPrivacyValueDisallowUsers#90110467 users:Vector<InputUser> = InputPrivacyRule
    ```
    """
    def __new__(
        cls,
        users: Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyValueAllowChatParticipants(TLObject):
    """
    [Read `inputPrivacyValueAllowChatParticipants` docs](https://core.telegram.org/constructor/inputPrivacyValueAllowChatParticipants).

    Generated from the following TL definition:
    ```tl
    inputPrivacyValueAllowChatParticipants#840649cf chats:Vector<long> = InputPrivacyRule
    ```
    """
    def __new__(
        cls,
        chats: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyValueDisallowChatParticipants(TLObject):
    """
    [Read `inputPrivacyValueDisallowChatParticipants` docs](https://core.telegram.org/constructor/inputPrivacyValueDisallowChatParticipants).

    Generated from the following TL definition:
    ```tl
    inputPrivacyValueDisallowChatParticipants#e94f0f86 chats:Vector<long> = InputPrivacyRule
    ```
    """
    def __new__(
        cls,
        chats: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyValueAllowCloseFriends(TLObject):
    """
    [Read `inputPrivacyValueAllowCloseFriends` docs](https://core.telegram.org/constructor/inputPrivacyValueAllowCloseFriends).

    Generated from the following TL definition:
    ```tl
    inputPrivacyValueAllowCloseFriends#2f453e49 = InputPrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyValueAllowPremium(TLObject):
    """
    [Read `inputPrivacyValueAllowPremium` docs](https://core.telegram.org/constructor/inputPrivacyValueAllowPremium).

    Generated from the following TL definition:
    ```tl
    inputPrivacyValueAllowPremium#77cdc9f1 = InputPrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyValueAllowBots(TLObject):
    """
    [Read `inputPrivacyValueAllowBots` docs](https://core.telegram.org/constructor/inputPrivacyValueAllowBots).

    Generated from the following TL definition:
    ```tl
    inputPrivacyValueAllowBots#5a4fcce5 = InputPrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPrivacyValueDisallowBots(TLObject):
    """
    [Read `inputPrivacyValueDisallowBots` docs](https://core.telegram.org/constructor/inputPrivacyValueDisallowBots).

    Generated from the following TL definition:
    ```tl
    inputPrivacyValueDisallowBots#c4e57915 = InputPrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyValueAllowContacts(TLObject):
    """
    [Read `privacyValueAllowContacts` docs](https://core.telegram.org/constructor/privacyValueAllowContacts).

    Generated from the following TL definition:
    ```tl
    privacyValueAllowContacts#fffe1bac = PrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyValueAllowAll(TLObject):
    """
    [Read `privacyValueAllowAll` docs](https://core.telegram.org/constructor/privacyValueAllowAll).

    Generated from the following TL definition:
    ```tl
    privacyValueAllowAll#65427b82 = PrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyValueAllowUsers(TLObject):
    """
    [Read `privacyValueAllowUsers` docs](https://core.telegram.org/constructor/privacyValueAllowUsers).

    Generated from the following TL definition:
    ```tl
    privacyValueAllowUsers#b8905fb2 users:Vector<long> = PrivacyRule
    ```
    """
    def __new__(
        cls,
        users: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyValueDisallowContacts(TLObject):
    """
    [Read `privacyValueDisallowContacts` docs](https://core.telegram.org/constructor/privacyValueDisallowContacts).

    Generated from the following TL definition:
    ```tl
    privacyValueDisallowContacts#f888fa1a = PrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyValueDisallowAll(TLObject):
    """
    [Read `privacyValueDisallowAll` docs](https://core.telegram.org/constructor/privacyValueDisallowAll).

    Generated from the following TL definition:
    ```tl
    privacyValueDisallowAll#8b73e763 = PrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyValueDisallowUsers(TLObject):
    """
    [Read `privacyValueDisallowUsers` docs](https://core.telegram.org/constructor/privacyValueDisallowUsers).

    Generated from the following TL definition:
    ```tl
    privacyValueDisallowUsers#e4621141 users:Vector<long> = PrivacyRule
    ```
    """
    def __new__(
        cls,
        users: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyValueAllowChatParticipants(TLObject):
    """
    [Read `privacyValueAllowChatParticipants` docs](https://core.telegram.org/constructor/privacyValueAllowChatParticipants).

    Generated from the following TL definition:
    ```tl
    privacyValueAllowChatParticipants#6b134e8e chats:Vector<long> = PrivacyRule
    ```
    """
    def __new__(
        cls,
        chats: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyValueDisallowChatParticipants(TLObject):
    """
    [Read `privacyValueDisallowChatParticipants` docs](https://core.telegram.org/constructor/privacyValueDisallowChatParticipants).

    Generated from the following TL definition:
    ```tl
    privacyValueDisallowChatParticipants#41c87565 chats:Vector<long> = PrivacyRule
    ```
    """
    def __new__(
        cls,
        chats: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyValueAllowCloseFriends(TLObject):
    """
    [Read `privacyValueAllowCloseFriends` docs](https://core.telegram.org/constructor/privacyValueAllowCloseFriends).

    Generated from the following TL definition:
    ```tl
    privacyValueAllowCloseFriends#f7e8d89b = PrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyValueAllowPremium(TLObject):
    """
    [Read `privacyValueAllowPremium` docs](https://core.telegram.org/constructor/privacyValueAllowPremium).

    Generated from the following TL definition:
    ```tl
    privacyValueAllowPremium#ece9814b = PrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyValueAllowBots(TLObject):
    """
    [Read `privacyValueAllowBots` docs](https://core.telegram.org/constructor/privacyValueAllowBots).

    Generated from the following TL definition:
    ```tl
    privacyValueAllowBots#21461b5d = PrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrivacyValueDisallowBots(TLObject):
    """
    [Read `privacyValueDisallowBots` docs](https://core.telegram.org/constructor/privacyValueDisallowBots).

    Generated from the following TL definition:
    ```tl
    privacyValueDisallowBots#f6a5f82f = PrivacyRule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AccountDaysTtl(TLObject):
    """
    [Read `accountDaysTTL` docs](https://core.telegram.org/constructor/accountDaysTTL).

    Generated from the following TL definition:
    ```tl
    accountDaysTTL#b8d0afdf days:int = AccountDaysTTL
    ```
    """
    def __new__(
        cls,
        days: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DocumentAttributeImageSize(TLObject):
    """
    [Read `documentAttributeImageSize` docs](https://core.telegram.org/constructor/documentAttributeImageSize).

    Generated from the following TL definition:
    ```tl
    documentAttributeImageSize#6c37c15c w:int h:int = DocumentAttribute
    ```
    """
    def __new__(
        cls,
        w: int,
        h: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DocumentAttributeAnimated(TLObject):
    """
    [Read `documentAttributeAnimated` docs](https://core.telegram.org/constructor/documentAttributeAnimated).

    Generated from the following TL definition:
    ```tl
    documentAttributeAnimated#11b58939 = DocumentAttribute
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DocumentAttributeSticker(TLObject):
    """
    [Read `documentAttributeSticker` docs](https://core.telegram.org/constructor/documentAttributeSticker).

    Generated from the following TL definition:
    ```tl
    documentAttributeSticker#6319d612 flags:# mask:flags.1?true alt:string stickerset:InputStickerSet mask_coords:flags.0?MaskCoords = DocumentAttribute
    ```
    """
    def __new__(
        cls,
        mask: bool,
        alt: str,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
        mask_coords: Optional[types.MaskCoords],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DocumentAttributeVideo(TLObject):
    """
    [Read `documentAttributeVideo` docs](https://core.telegram.org/constructor/documentAttributeVideo).

    Generated from the following TL definition:
    ```tl
    documentAttributeVideo#43c57c48 flags:# round_message:flags.0?true supports_streaming:flags.1?true nosound:flags.3?true duration:double w:int h:int preload_prefix_size:flags.2?int video_start_ts:flags.4?double video_codec:flags.5?string = DocumentAttribute
    ```
    """
    def __new__(
        cls,
        round_message: bool,
        supports_streaming: bool,
        nosound: bool,
        duration: float,
        w: int,
        h: int,
        preload_prefix_size: Optional[int],
        video_start_ts: Optional[float],
        video_codec: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DocumentAttributeAudio(TLObject):
    """
    [Read `documentAttributeAudio` docs](https://core.telegram.org/constructor/documentAttributeAudio).

    Generated from the following TL definition:
    ```tl
    documentAttributeAudio#9852f9c6 flags:# voice:flags.10?true duration:int title:flags.0?string performer:flags.1?string waveform:flags.2?bytes = DocumentAttribute
    ```
    """
    def __new__(
        cls,
        voice: bool,
        duration: int,
        title: Optional[str],
        performer: Optional[str],
        waveform: Optional[bytes],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DocumentAttributeFilename(TLObject):
    """
    [Read `documentAttributeFilename` docs](https://core.telegram.org/constructor/documentAttributeFilename).

    Generated from the following TL definition:
    ```tl
    documentAttributeFilename#15590068 file_name:string = DocumentAttribute
    ```
    """
    def __new__(
        cls,
        file_name: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DocumentAttributeHasStickers(TLObject):
    """
    [Read `documentAttributeHasStickers` docs](https://core.telegram.org/constructor/documentAttributeHasStickers).

    Generated from the following TL definition:
    ```tl
    documentAttributeHasStickers#9801d2f7 = DocumentAttribute
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DocumentAttributeCustomEmoji(TLObject):
    """
    [Read `documentAttributeCustomEmoji` docs](https://core.telegram.org/constructor/documentAttributeCustomEmoji).

    Generated from the following TL definition:
    ```tl
    documentAttributeCustomEmoji#fd149899 flags:# free:flags.0?true text_color:flags.1?true alt:string stickerset:InputStickerSet = DocumentAttribute
    ```
    """
    def __new__(
        cls,
        free: bool,
        text_color: bool,
        alt: str,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StickerPack(TLObject):
    """
    [Read `stickerPack` docs](https://core.telegram.org/constructor/stickerPack).

    Generated from the following TL definition:
    ```tl
    stickerPack#12b299d4 emoticon:string documents:Vector<long> = StickerPack
    ```
    """
    def __new__(
        cls,
        emoticon: str,
        documents: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebPageEmpty(TLObject):
    """
    [Read `webPageEmpty` docs](https://core.telegram.org/constructor/webPageEmpty).

    Generated from the following TL definition:
    ```tl
    webPageEmpty#211a1788 flags:# id:long url:flags.0?string = WebPage
    ```
    """
    def __new__(
        cls,
        id: int,
        url: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebPagePending(TLObject):
    """
    [Read `webPagePending` docs](https://core.telegram.org/constructor/webPagePending).

    Generated from the following TL definition:
    ```tl
    webPagePending#b0d13e47 flags:# id:long url:flags.0?string date:int = WebPage
    ```
    """
    def __new__(
        cls,
        id: int,
        url: Optional[str],
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebPage(TLObject):
    """
    [Read `webPage` docs](https://core.telegram.org/constructor/webPage).

    Generated from the following TL definition:
    ```tl
    webPage#e89c45b2 flags:# has_large_media:flags.13?true video_cover_photo:flags.14?true id:long url:string display_url:string hash:int type:flags.0?string site_name:flags.1?string title:flags.2?string description:flags.3?string photo:flags.4?Photo embed_url:flags.5?string embed_type:flags.5?string embed_width:flags.6?int embed_height:flags.6?int duration:flags.7?int author:flags.8?string document:flags.9?Document cached_page:flags.10?Page attributes:flags.12?Vector<WebPageAttribute> = WebPage
    ```
    """
    def __new__(
        cls,
        has_large_media: bool,
        video_cover_photo: bool,
        id: int,
        url: str,
        display_url: str,
        hash: int,
        type: Optional[str],
        site_name: Optional[str],
        title: Optional[str],
        description: Optional[str],
        photo: Optional[types.PhotoEmpty | types.Photo],
        embed_url: Optional[str],
        embed_type: Optional[str],
        embed_width: Optional[int],
        embed_height: Optional[int],
        duration: Optional[int],
        author: Optional[str],
        document: Optional[types.DocumentEmpty | types.Document],
        cached_page: Optional[types.Page],
        attributes: Optional[Sequence[types.WebPageAttributeTheme | types.WebPageAttributeStory | types.WebPageAttributeStickerSet | types.WebPageAttributeUniqueStarGift | types.WebPageAttributeStarGiftCollection | types.WebPageAttributeStarGiftAuction]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebPageNotModified(TLObject):
    """
    [Read `webPageNotModified` docs](https://core.telegram.org/constructor/webPageNotModified).

    Generated from the following TL definition:
    ```tl
    webPageNotModified#7311ca11 flags:# cached_page_views:flags.0?int = WebPage
    ```
    """
    def __new__(
        cls,
        cached_page_views: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Authorization(TLObject):
    """
    [Read `authorization` docs](https://core.telegram.org/constructor/authorization).

    Generated from the following TL definition:
    ```tl
    authorization#ad01d61d flags:# current:flags.0?true official_app:flags.1?true password_pending:flags.2?true encrypted_requests_disabled:flags.3?true call_requests_disabled:flags.4?true unconfirmed:flags.5?true hash:long device_model:string platform:string system_version:string api_id:int app_name:string app_version:string date_created:int date_active:int ip:string country:string region:string = Authorization
    ```
    """
    def __new__(
        cls,
        current: bool,
        official_app: bool,
        password_pending: bool,
        encrypted_requests_disabled: bool,
        call_requests_disabled: bool,
        unconfirmed: bool,
        hash: int,
        device_model: str,
        platform: str,
        system_version: str,
        api_id: int,
        app_name: str,
        app_version: str,
        date_created: int,
        date_active: int,
        ip: str,
        country: str,
        region: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReceivedNotifyMessage(TLObject):
    """
    [Read `receivedNotifyMessage` docs](https://core.telegram.org/constructor/receivedNotifyMessage).

    Generated from the following TL definition:
    ```tl
    receivedNotifyMessage#a384b779 id:int flags:int = ReceivedNotifyMessage
    ```
    """
    def __new__(
        cls,
        id: int,
        flags: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatInviteExported(TLObject):
    """
    [Read `chatInviteExported` docs](https://core.telegram.org/constructor/chatInviteExported).

    Generated from the following TL definition:
    ```tl
    chatInviteExported#a22cbd96 flags:# revoked:flags.0?true permanent:flags.5?true request_needed:flags.6?true link:string admin_id:long date:int start_date:flags.4?int expire_date:flags.1?int usage_limit:flags.2?int usage:flags.3?int requested:flags.7?int subscription_expired:flags.10?int title:flags.8?string subscription_pricing:flags.9?StarsSubscriptionPricing = ExportedChatInvite
    ```
    """
    def __new__(
        cls,
        revoked: bool,
        permanent: bool,
        request_needed: bool,
        link: str,
        admin_id: int,
        date: int,
        start_date: Optional[int],
        expire_date: Optional[int],
        usage_limit: Optional[int],
        usage: Optional[int],
        requested: Optional[int],
        subscription_expired: Optional[int],
        title: Optional[str],
        subscription_pricing: Optional[types.StarsSubscriptionPricing],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatInvitePublicJoinRequests(TLObject):
    """
    [Read `chatInvitePublicJoinRequests` docs](https://core.telegram.org/constructor/chatInvitePublicJoinRequests).

    Generated from the following TL definition:
    ```tl
    chatInvitePublicJoinRequests#ed107ab7 = ExportedChatInvite
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatInviteAlready(TLObject):
    """
    [Read `chatInviteAlready` docs](https://core.telegram.org/constructor/chatInviteAlready).

    Generated from the following TL definition:
    ```tl
    chatInviteAlready#5a686d7c chat:Chat = ChatInvite
    ```
    """
    def __new__(
        cls,
        chat: types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatInvite(TLObject):
    """
    [Read `chatInvite` docs](https://core.telegram.org/constructor/chatInvite).

    Generated from the following TL definition:
    ```tl
    chatInvite#5c9d3702 flags:# channel:flags.0?true broadcast:flags.1?true public:flags.2?true megagroup:flags.3?true request_needed:flags.6?true verified:flags.7?true scam:flags.8?true fake:flags.9?true can_refulfill_subscription:flags.11?true title:string about:flags.5?string photo:Photo participants_count:int participants:flags.4?Vector<User> color:int subscription_pricing:flags.10?StarsSubscriptionPricing subscription_form_id:flags.12?long bot_verification:flags.13?BotVerification = ChatInvite
    ```
    """
    def __new__(
        cls,
        channel: bool,
        broadcast: bool,
        public: bool,
        megagroup: bool,
        request_needed: bool,
        verified: bool,
        scam: bool,
        fake: bool,
        can_refulfill_subscription: bool,
        title: str,
        about: Optional[str],
        photo: types.PhotoEmpty | types.Photo,
        participants_count: int,
        participants: Optional[Sequence[types.UserEmpty | types.User]],
        color: int,
        subscription_pricing: Optional[types.StarsSubscriptionPricing],
        subscription_form_id: Optional[int],
        bot_verification: Optional[types.BotVerification],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatInvitePeek(TLObject):
    """
    [Read `chatInvitePeek` docs](https://core.telegram.org/constructor/chatInvitePeek).

    Generated from the following TL definition:
    ```tl
    chatInvitePeek#61695cb0 chat:Chat expires:int = ChatInvite
    ```
    """
    def __new__(
        cls,
        chat: types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden,
        expires: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetEmpty(TLObject):
    """
    [Read `inputStickerSetEmpty` docs](https://core.telegram.org/constructor/inputStickerSetEmpty).

    Generated from the following TL definition:
    ```tl
    inputStickerSetEmpty#ffb62b95 = InputStickerSet
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetId(TLObject):
    """
    [Read `inputStickerSetID` docs](https://core.telegram.org/constructor/inputStickerSetID).

    Generated from the following TL definition:
    ```tl
    inputStickerSetID#9de7a269 id:long access_hash:long = InputStickerSet
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetShortName(TLObject):
    """
    [Read `inputStickerSetShortName` docs](https://core.telegram.org/constructor/inputStickerSetShortName).

    Generated from the following TL definition:
    ```tl
    inputStickerSetShortName#861cc8a0 short_name:string = InputStickerSet
    ```
    """
    def __new__(
        cls,
        short_name: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetAnimatedEmoji(TLObject):
    """
    [Read `inputStickerSetAnimatedEmoji` docs](https://core.telegram.org/constructor/inputStickerSetAnimatedEmoji).

    Generated from the following TL definition:
    ```tl
    inputStickerSetAnimatedEmoji#28703c8 = InputStickerSet
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetDice(TLObject):
    """
    [Read `inputStickerSetDice` docs](https://core.telegram.org/constructor/inputStickerSetDice).

    Generated from the following TL definition:
    ```tl
    inputStickerSetDice#e67f520e emoticon:string = InputStickerSet
    ```
    """
    def __new__(
        cls,
        emoticon: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetAnimatedEmojiAnimations(TLObject):
    """
    [Read `inputStickerSetAnimatedEmojiAnimations` docs](https://core.telegram.org/constructor/inputStickerSetAnimatedEmojiAnimations).

    Generated from the following TL definition:
    ```tl
    inputStickerSetAnimatedEmojiAnimations#cde3739 = InputStickerSet
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetPremiumGifts(TLObject):
    """
    [Read `inputStickerSetPremiumGifts` docs](https://core.telegram.org/constructor/inputStickerSetPremiumGifts).

    Generated from the following TL definition:
    ```tl
    inputStickerSetPremiumGifts#c88b3b02 = InputStickerSet
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetEmojiGenericAnimations(TLObject):
    """
    [Read `inputStickerSetEmojiGenericAnimations` docs](https://core.telegram.org/constructor/inputStickerSetEmojiGenericAnimations).

    Generated from the following TL definition:
    ```tl
    inputStickerSetEmojiGenericAnimations#4c4d4ce = InputStickerSet
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetEmojiDefaultStatuses(TLObject):
    """
    [Read `inputStickerSetEmojiDefaultStatuses` docs](https://core.telegram.org/constructor/inputStickerSetEmojiDefaultStatuses).

    Generated from the following TL definition:
    ```tl
    inputStickerSetEmojiDefaultStatuses#29d0f5ee = InputStickerSet
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetEmojiDefaultTopicIcons(TLObject):
    """
    [Read `inputStickerSetEmojiDefaultTopicIcons` docs](https://core.telegram.org/constructor/inputStickerSetEmojiDefaultTopicIcons).

    Generated from the following TL definition:
    ```tl
    inputStickerSetEmojiDefaultTopicIcons#44c1f8e9 = InputStickerSet
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetEmojiChannelDefaultStatuses(TLObject):
    """
    [Read `inputStickerSetEmojiChannelDefaultStatuses` docs](https://core.telegram.org/constructor/inputStickerSetEmojiChannelDefaultStatuses).

    Generated from the following TL definition:
    ```tl
    inputStickerSetEmojiChannelDefaultStatuses#49748553 = InputStickerSet
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetTonGifts(TLObject):
    """
    [Read `inputStickerSetTonGifts` docs](https://core.telegram.org/constructor/inputStickerSetTonGifts).

    Generated from the following TL definition:
    ```tl
    inputStickerSetTonGifts#1cf671a0 = InputStickerSet
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StickerSet(TLObject):
    """
    [Read `stickerSet` docs](https://core.telegram.org/constructor/stickerSet).

    Generated from the following TL definition:
    ```tl
    stickerSet#2dd14edc flags:# archived:flags.1?true official:flags.2?true masks:flags.3?true emojis:flags.7?true text_color:flags.9?true channel_emoji_status:flags.10?true creator:flags.11?true installed_date:flags.0?int id:long access_hash:long title:string short_name:string thumbs:flags.4?Vector<PhotoSize> thumb_dc_id:flags.4?int thumb_version:flags.4?int thumb_document_id:flags.8?long count:int hash:int = StickerSet
    ```
    """
    def __new__(
        cls,
        archived: bool,
        official: bool,
        masks: bool,
        emojis: bool,
        text_color: bool,
        channel_emoji_status: bool,
        creator: bool,
        installed_date: Optional[int],
        id: int,
        access_hash: int,
        title: str,
        short_name: str,
        thumbs: Optional[Sequence[types.PhotoSizeEmpty | types.PhotoSize | types.PhotoCachedSize | types.PhotoStrippedSize | types.PhotoSizeProgressive | types.PhotoPathSize]],
        thumb_dc_id: Optional[int],
        thumb_version: Optional[int],
        thumb_document_id: Optional[int],
        count: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotCommand(TLObject):
    """
    [Read `botCommand` docs](https://core.telegram.org/constructor/botCommand).

    Generated from the following TL definition:
    ```tl
    botCommand#c27ac8c7 command:string description:string = BotCommand
    ```
    """
    def __new__(
        cls,
        command: str,
        description: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotInfo(TLObject):
    """
    [Read `botInfo` docs](https://core.telegram.org/constructor/botInfo).

    Generated from the following TL definition:
    ```tl
    botInfo#4d8a0299 flags:# has_preview_medias:flags.6?true user_id:flags.0?long description:flags.1?string description_photo:flags.4?Photo description_document:flags.5?Document commands:flags.2?Vector<BotCommand> menu_button:flags.3?BotMenuButton privacy_policy_url:flags.7?string app_settings:flags.8?BotAppSettings verifier_settings:flags.9?BotVerifierSettings = BotInfo
    ```
    """
    def __new__(
        cls,
        has_preview_medias: bool,
        user_id: Optional[int],
        description: Optional[str],
        description_photo: Optional[types.PhotoEmpty | types.Photo],
        description_document: Optional[types.DocumentEmpty | types.Document],
        commands: Optional[Sequence[types.BotCommand]],
        menu_button: Optional[types.BotMenuButtonDefault | types.BotMenuButtonCommands | types.BotMenuButton],
        privacy_policy_url: Optional[str],
        app_settings: Optional[types.BotAppSettings],
        verifier_settings: Optional[types.BotVerifierSettings],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButton(TLObject):
    """
    [Read `keyboardButton` docs](https://core.telegram.org/constructor/keyboardButton).

    Generated from the following TL definition:
    ```tl
    keyboardButton#a2fa4880 text:string = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonUrl(TLObject):
    """
    [Read `keyboardButtonUrl` docs](https://core.telegram.org/constructor/keyboardButtonUrl).

    Generated from the following TL definition:
    ```tl
    keyboardButtonUrl#258aff05 text:string url:string = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonCallback(TLObject):
    """
    [Read `keyboardButtonCallback` docs](https://core.telegram.org/constructor/keyboardButtonCallback).

    Generated from the following TL definition:
    ```tl
    keyboardButtonCallback#35bbdb6b flags:# requires_password:flags.0?true text:string data:bytes = KeyboardButton
    ```
    """
    def __new__(
        cls,
        requires_password: bool,
        text: str,
        data: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonRequestPhone(TLObject):
    """
    [Read `keyboardButtonRequestPhone` docs](https://core.telegram.org/constructor/keyboardButtonRequestPhone).

    Generated from the following TL definition:
    ```tl
    keyboardButtonRequestPhone#b16a6c29 text:string = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonRequestGeoLocation(TLObject):
    """
    [Read `keyboardButtonRequestGeoLocation` docs](https://core.telegram.org/constructor/keyboardButtonRequestGeoLocation).

    Generated from the following TL definition:
    ```tl
    keyboardButtonRequestGeoLocation#fc796b3f text:string = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonSwitchInline(TLObject):
    """
    [Read `keyboardButtonSwitchInline` docs](https://core.telegram.org/constructor/keyboardButtonSwitchInline).

    Generated from the following TL definition:
    ```tl
    keyboardButtonSwitchInline#93b9fbb5 flags:# same_peer:flags.0?true text:string query:string peer_types:flags.1?Vector<InlineQueryPeerType> = KeyboardButton
    ```
    """
    def __new__(
        cls,
        same_peer: bool,
        text: str,
        query: str,
        peer_types: Optional[Sequence[types.InlineQueryPeerTypeSameBotPm | types.InlineQueryPeerTypePm | types.InlineQueryPeerTypeChat | types.InlineQueryPeerTypeMegagroup | types.InlineQueryPeerTypeBroadcast | types.InlineQueryPeerTypeBotPm]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonGame(TLObject):
    """
    [Read `keyboardButtonGame` docs](https://core.telegram.org/constructor/keyboardButtonGame).

    Generated from the following TL definition:
    ```tl
    keyboardButtonGame#50f41ccf text:string = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonBuy(TLObject):
    """
    [Read `keyboardButtonBuy` docs](https://core.telegram.org/constructor/keyboardButtonBuy).

    Generated from the following TL definition:
    ```tl
    keyboardButtonBuy#afd93fbb text:string = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonUrlAuth(TLObject):
    """
    [Read `keyboardButtonUrlAuth` docs](https://core.telegram.org/constructor/keyboardButtonUrlAuth).

    Generated from the following TL definition:
    ```tl
    keyboardButtonUrlAuth#10b78d29 flags:# text:string fwd_text:flags.0?string url:string button_id:int = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
        fwd_text: Optional[str],
        url: str,
        button_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputKeyboardButtonUrlAuth(TLObject):
    """
    [Read `inputKeyboardButtonUrlAuth` docs](https://core.telegram.org/constructor/inputKeyboardButtonUrlAuth).

    Generated from the following TL definition:
    ```tl
    inputKeyboardButtonUrlAuth#d02e7fd4 flags:# request_write_access:flags.0?true text:string fwd_text:flags.1?string url:string bot:InputUser = KeyboardButton
    ```
    """
    def __new__(
        cls,
        request_write_access: bool,
        text: str,
        fwd_text: Optional[str],
        url: str,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonRequestPoll(TLObject):
    """
    [Read `keyboardButtonRequestPoll` docs](https://core.telegram.org/constructor/keyboardButtonRequestPoll).

    Generated from the following TL definition:
    ```tl
    keyboardButtonRequestPoll#bbc7515d flags:# quiz:flags.0?Bool text:string = KeyboardButton
    ```
    """
    def __new__(
        cls,
        quiz: Optional[bool],
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputKeyboardButtonUserProfile(TLObject):
    """
    [Read `inputKeyboardButtonUserProfile` docs](https://core.telegram.org/constructor/inputKeyboardButtonUserProfile).

    Generated from the following TL definition:
    ```tl
    inputKeyboardButtonUserProfile#e988037b text:string user_id:InputUser = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonUserProfile(TLObject):
    """
    [Read `keyboardButtonUserProfile` docs](https://core.telegram.org/constructor/keyboardButtonUserProfile).

    Generated from the following TL definition:
    ```tl
    keyboardButtonUserProfile#308660c1 text:string user_id:long = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
        user_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonWebView(TLObject):
    """
    [Read `keyboardButtonWebView` docs](https://core.telegram.org/constructor/keyboardButtonWebView).

    Generated from the following TL definition:
    ```tl
    keyboardButtonWebView#13767230 text:string url:string = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonSimpleWebView(TLObject):
    """
    [Read `keyboardButtonSimpleWebView` docs](https://core.telegram.org/constructor/keyboardButtonSimpleWebView).

    Generated from the following TL definition:
    ```tl
    keyboardButtonSimpleWebView#a0c0505c text:string url:string = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonRequestPeer(TLObject):
    """
    [Read `keyboardButtonRequestPeer` docs](https://core.telegram.org/constructor/keyboardButtonRequestPeer).

    Generated from the following TL definition:
    ```tl
    keyboardButtonRequestPeer#53d7bfd8 text:string button_id:int peer_type:RequestPeerType max_quantity:int = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
        button_id: int,
        peer_type: types.RequestPeerTypeUser | types.RequestPeerTypeChat | types.RequestPeerTypeBroadcast,
        max_quantity: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputKeyboardButtonRequestPeer(TLObject):
    """
    [Read `inputKeyboardButtonRequestPeer` docs](https://core.telegram.org/constructor/inputKeyboardButtonRequestPeer).

    Generated from the following TL definition:
    ```tl
    inputKeyboardButtonRequestPeer#c9662d05 flags:# name_requested:flags.0?true username_requested:flags.1?true photo_requested:flags.2?true text:string button_id:int peer_type:RequestPeerType max_quantity:int = KeyboardButton
    ```
    """
    def __new__(
        cls,
        name_requested: bool,
        username_requested: bool,
        photo_requested: bool,
        text: str,
        button_id: int,
        peer_type: types.RequestPeerTypeUser | types.RequestPeerTypeChat | types.RequestPeerTypeBroadcast,
        max_quantity: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonCopy(TLObject):
    """
    [Read `keyboardButtonCopy` docs](https://core.telegram.org/constructor/keyboardButtonCopy).

    Generated from the following TL definition:
    ```tl
    keyboardButtonCopy#75d2698e text:string copy_text:string = KeyboardButton
    ```
    """
    def __new__(
        cls,
        text: str,
        copy_text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class KeyboardButtonRow(TLObject):
    """
    [Read `keyboardButtonRow` docs](https://core.telegram.org/constructor/keyboardButtonRow).

    Generated from the following TL definition:
    ```tl
    keyboardButtonRow#77608b83 buttons:Vector<KeyboardButton> = KeyboardButtonRow
    ```
    """
    def __new__(
        cls,
        buttons: Sequence[types.KeyboardButton | types.KeyboardButtonUrl | types.KeyboardButtonCallback | types.KeyboardButtonRequestPhone | types.KeyboardButtonRequestGeoLocation | types.KeyboardButtonSwitchInline | types.KeyboardButtonGame | types.KeyboardButtonBuy | types.KeyboardButtonUrlAuth | types.InputKeyboardButtonUrlAuth | types.KeyboardButtonRequestPoll | types.InputKeyboardButtonUserProfile | types.KeyboardButtonUserProfile | types.KeyboardButtonWebView | types.KeyboardButtonSimpleWebView | types.KeyboardButtonRequestPeer | types.InputKeyboardButtonRequestPeer | types.KeyboardButtonCopy],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReplyKeyboardHide(TLObject):
    """
    [Read `replyKeyboardHide` docs](https://core.telegram.org/constructor/replyKeyboardHide).

    Generated from the following TL definition:
    ```tl
    replyKeyboardHide#a03e5b85 flags:# selective:flags.2?true = ReplyMarkup
    ```
    """
    def __new__(
        cls,
        selective: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReplyKeyboardForceReply(TLObject):
    """
    [Read `replyKeyboardForceReply` docs](https://core.telegram.org/constructor/replyKeyboardForceReply).

    Generated from the following TL definition:
    ```tl
    replyKeyboardForceReply#86b40b08 flags:# single_use:flags.1?true selective:flags.2?true placeholder:flags.3?string = ReplyMarkup
    ```
    """
    def __new__(
        cls,
        single_use: bool,
        selective: bool,
        placeholder: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReplyKeyboardMarkup(TLObject):
    """
    [Read `replyKeyboardMarkup` docs](https://core.telegram.org/constructor/replyKeyboardMarkup).

    Generated from the following TL definition:
    ```tl
    replyKeyboardMarkup#85dd99d1 flags:# resize:flags.0?true single_use:flags.1?true selective:flags.2?true persistent:flags.4?true rows:Vector<KeyboardButtonRow> placeholder:flags.3?string = ReplyMarkup
    ```
    """
    def __new__(
        cls,
        resize: bool,
        single_use: bool,
        selective: bool,
        persistent: bool,
        rows: Sequence[types.KeyboardButtonRow],
        placeholder: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReplyInlineMarkup(TLObject):
    """
    [Read `replyInlineMarkup` docs](https://core.telegram.org/constructor/replyInlineMarkup).

    Generated from the following TL definition:
    ```tl
    replyInlineMarkup#48a30254 rows:Vector<KeyboardButtonRow> = ReplyMarkup
    ```
    """
    def __new__(
        cls,
        rows: Sequence[types.KeyboardButtonRow],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityUnknown(TLObject):
    """
    [Read `messageEntityUnknown` docs](https://core.telegram.org/constructor/messageEntityUnknown).

    Generated from the following TL definition:
    ```tl
    messageEntityUnknown#bb92ba95 offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityMention(TLObject):
    """
    [Read `messageEntityMention` docs](https://core.telegram.org/constructor/messageEntityMention).

    Generated from the following TL definition:
    ```tl
    messageEntityMention#fa04579d offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityHashtag(TLObject):
    """
    [Read `messageEntityHashtag` docs](https://core.telegram.org/constructor/messageEntityHashtag).

    Generated from the following TL definition:
    ```tl
    messageEntityHashtag#6f635b0d offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityBotCommand(TLObject):
    """
    [Read `messageEntityBotCommand` docs](https://core.telegram.org/constructor/messageEntityBotCommand).

    Generated from the following TL definition:
    ```tl
    messageEntityBotCommand#6cef8ac7 offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityUrl(TLObject):
    """
    [Read `messageEntityUrl` docs](https://core.telegram.org/constructor/messageEntityUrl).

    Generated from the following TL definition:
    ```tl
    messageEntityUrl#6ed02538 offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityEmail(TLObject):
    """
    [Read `messageEntityEmail` docs](https://core.telegram.org/constructor/messageEntityEmail).

    Generated from the following TL definition:
    ```tl
    messageEntityEmail#64e475c2 offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityBold(TLObject):
    """
    [Read `messageEntityBold` docs](https://core.telegram.org/constructor/messageEntityBold).

    Generated from the following TL definition:
    ```tl
    messageEntityBold#bd610bc9 offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityItalic(TLObject):
    """
    [Read `messageEntityItalic` docs](https://core.telegram.org/constructor/messageEntityItalic).

    Generated from the following TL definition:
    ```tl
    messageEntityItalic#826f8b60 offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityCode(TLObject):
    """
    [Read `messageEntityCode` docs](https://core.telegram.org/constructor/messageEntityCode).

    Generated from the following TL definition:
    ```tl
    messageEntityCode#28a20571 offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityPre(TLObject):
    """
    [Read `messageEntityPre` docs](https://core.telegram.org/constructor/messageEntityPre).

    Generated from the following TL definition:
    ```tl
    messageEntityPre#73924be0 offset:int length:int language:string = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
        language: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityTextUrl(TLObject):
    """
    [Read `messageEntityTextUrl` docs](https://core.telegram.org/constructor/messageEntityTextUrl).

    Generated from the following TL definition:
    ```tl
    messageEntityTextUrl#76a6d327 offset:int length:int url:string = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityMentionName(TLObject):
    """
    [Read `messageEntityMentionName` docs](https://core.telegram.org/constructor/messageEntityMentionName).

    Generated from the following TL definition:
    ```tl
    messageEntityMentionName#dc7b1140 offset:int length:int user_id:long = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
        user_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessageEntityMentionName(TLObject):
    """
    [Read `inputMessageEntityMentionName` docs](https://core.telegram.org/constructor/inputMessageEntityMentionName).

    Generated from the following TL definition:
    ```tl
    inputMessageEntityMentionName#208e68c9 offset:int length:int user_id:InputUser = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityPhone(TLObject):
    """
    [Read `messageEntityPhone` docs](https://core.telegram.org/constructor/messageEntityPhone).

    Generated from the following TL definition:
    ```tl
    messageEntityPhone#9b69e34b offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityCashtag(TLObject):
    """
    [Read `messageEntityCashtag` docs](https://core.telegram.org/constructor/messageEntityCashtag).

    Generated from the following TL definition:
    ```tl
    messageEntityCashtag#4c4e743f offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityUnderline(TLObject):
    """
    [Read `messageEntityUnderline` docs](https://core.telegram.org/constructor/messageEntityUnderline).

    Generated from the following TL definition:
    ```tl
    messageEntityUnderline#9c4e7e8b offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityStrike(TLObject):
    """
    [Read `messageEntityStrike` docs](https://core.telegram.org/constructor/messageEntityStrike).

    Generated from the following TL definition:
    ```tl
    messageEntityStrike#bf0693d4 offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityBankCard(TLObject):
    """
    [Read `messageEntityBankCard` docs](https://core.telegram.org/constructor/messageEntityBankCard).

    Generated from the following TL definition:
    ```tl
    messageEntityBankCard#761e6af4 offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntitySpoiler(TLObject):
    """
    [Read `messageEntitySpoiler` docs](https://core.telegram.org/constructor/messageEntitySpoiler).

    Generated from the following TL definition:
    ```tl
    messageEntitySpoiler#32ca960f offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityCustomEmoji(TLObject):
    """
    [Read `messageEntityCustomEmoji` docs](https://core.telegram.org/constructor/messageEntityCustomEmoji).

    Generated from the following TL definition:
    ```tl
    messageEntityCustomEmoji#c8cf05f8 offset:int length:int document_id:long = MessageEntity
    ```
    """
    def __new__(
        cls,
        offset: int,
        length: int,
        document_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageEntityBlockquote(TLObject):
    """
    [Read `messageEntityBlockquote` docs](https://core.telegram.org/constructor/messageEntityBlockquote).

    Generated from the following TL definition:
    ```tl
    messageEntityBlockquote#f1ccaaac flags:# collapsed:flags.0?true offset:int length:int = MessageEntity
    ```
    """
    def __new__(
        cls,
        collapsed: bool,
        offset: int,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputChannelEmpty(TLObject):
    """
    [Read `inputChannelEmpty` docs](https://core.telegram.org/constructor/inputChannelEmpty).

    Generated from the following TL definition:
    ```tl
    inputChannelEmpty#ee8c1e86 = InputChannel
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputChannel(TLObject):
    """
    [Read `inputChannel` docs](https://core.telegram.org/constructor/inputChannel).

    Generated from the following TL definition:
    ```tl
    inputChannel#f35aec28 channel_id:long access_hash:long = InputChannel
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputChannelFromMessage(TLObject):
    """
    [Read `inputChannelFromMessage` docs](https://core.telegram.org/constructor/inputChannelFromMessage).

    Generated from the following TL definition:
    ```tl
    inputChannelFromMessage#5b934f9d peer:InputPeer msg_id:int channel_id:long = InputChannel
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
        channel_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageRange(TLObject):
    """
    [Read `messageRange` docs](https://core.telegram.org/constructor/messageRange).

    Generated from the following TL definition:
    ```tl
    messageRange#ae30253 min_id:int max_id:int = MessageRange
    ```
    """
    def __new__(
        cls,
        min_id: int,
        max_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelMessagesFilterEmpty(TLObject):
    """
    [Read `channelMessagesFilterEmpty` docs](https://core.telegram.org/constructor/channelMessagesFilterEmpty).

    Generated from the following TL definition:
    ```tl
    channelMessagesFilterEmpty#94d42ee7 = ChannelMessagesFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelMessagesFilter(TLObject):
    """
    [Read `channelMessagesFilter` docs](https://core.telegram.org/constructor/channelMessagesFilter).

    Generated from the following TL definition:
    ```tl
    channelMessagesFilter#cd77d957 flags:# exclude_new_messages:flags.1?true ranges:Vector<MessageRange> = ChannelMessagesFilter
    ```
    """
    def __new__(
        cls,
        exclude_new_messages: bool,
        ranges: Sequence[types.MessageRange],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipant(TLObject):
    """
    [Read `channelParticipant` docs](https://core.telegram.org/constructor/channelParticipant).

    Generated from the following TL definition:
    ```tl
    channelParticipant#cb397619 flags:# user_id:long date:int subscription_until_date:flags.0?int = ChannelParticipant
    ```
    """
    def __new__(
        cls,
        user_id: int,
        date: int,
        subscription_until_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantSelf(TLObject):
    """
    [Read `channelParticipantSelf` docs](https://core.telegram.org/constructor/channelParticipantSelf).

    Generated from the following TL definition:
    ```tl
    channelParticipantSelf#4f607bef flags:# via_request:flags.0?true user_id:long inviter_id:long date:int subscription_until_date:flags.1?int = ChannelParticipant
    ```
    """
    def __new__(
        cls,
        via_request: bool,
        user_id: int,
        inviter_id: int,
        date: int,
        subscription_until_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantCreator(TLObject):
    """
    [Read `channelParticipantCreator` docs](https://core.telegram.org/constructor/channelParticipantCreator).

    Generated from the following TL definition:
    ```tl
    channelParticipantCreator#2fe601d3 flags:# user_id:long admin_rights:ChatAdminRights rank:flags.0?string = ChannelParticipant
    ```
    """
    def __new__(
        cls,
        user_id: int,
        admin_rights: types.ChatAdminRights,
        rank: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantAdmin(TLObject):
    """
    [Read `channelParticipantAdmin` docs](https://core.telegram.org/constructor/channelParticipantAdmin).

    Generated from the following TL definition:
    ```tl
    channelParticipantAdmin#34c3bb53 flags:# can_edit:flags.0?true self:flags.1?true user_id:long inviter_id:flags.1?long promoted_by:long date:int admin_rights:ChatAdminRights rank:flags.2?string = ChannelParticipant
    ```
    """
    def __new__(
        cls,
        can_edit: bool,
        is_self: bool,
        user_id: int,
        inviter_id: Optional[int],
        promoted_by: int,
        date: int,
        admin_rights: types.ChatAdminRights,
        rank: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantBanned(TLObject):
    """
    [Read `channelParticipantBanned` docs](https://core.telegram.org/constructor/channelParticipantBanned).

    Generated from the following TL definition:
    ```tl
    channelParticipantBanned#6df8014e flags:# left:flags.0?true peer:Peer kicked_by:long date:int banned_rights:ChatBannedRights = ChannelParticipant
    ```
    """
    def __new__(
        cls,
        left: bool,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        kicked_by: int,
        date: int,
        banned_rights: types.ChatBannedRights,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantLeft(TLObject):
    """
    [Read `channelParticipantLeft` docs](https://core.telegram.org/constructor/channelParticipantLeft).

    Generated from the following TL definition:
    ```tl
    channelParticipantLeft#1b03f006 peer:Peer = ChannelParticipant
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantsRecent(TLObject):
    """
    [Read `channelParticipantsRecent` docs](https://core.telegram.org/constructor/channelParticipantsRecent).

    Generated from the following TL definition:
    ```tl
    channelParticipantsRecent#de3f3c79 = ChannelParticipantsFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantsAdmins(TLObject):
    """
    [Read `channelParticipantsAdmins` docs](https://core.telegram.org/constructor/channelParticipantsAdmins).

    Generated from the following TL definition:
    ```tl
    channelParticipantsAdmins#b4608969 = ChannelParticipantsFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantsKicked(TLObject):
    """
    [Read `channelParticipantsKicked` docs](https://core.telegram.org/constructor/channelParticipantsKicked).

    Generated from the following TL definition:
    ```tl
    channelParticipantsKicked#a3b54985 q:string = ChannelParticipantsFilter
    ```
    """
    def __new__(
        cls,
        q: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantsBots(TLObject):
    """
    [Read `channelParticipantsBots` docs](https://core.telegram.org/constructor/channelParticipantsBots).

    Generated from the following TL definition:
    ```tl
    channelParticipantsBots#b0d1865b = ChannelParticipantsFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantsBanned(TLObject):
    """
    [Read `channelParticipantsBanned` docs](https://core.telegram.org/constructor/channelParticipantsBanned).

    Generated from the following TL definition:
    ```tl
    channelParticipantsBanned#1427a5e1 q:string = ChannelParticipantsFilter
    ```
    """
    def __new__(
        cls,
        q: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantsSearch(TLObject):
    """
    [Read `channelParticipantsSearch` docs](https://core.telegram.org/constructor/channelParticipantsSearch).

    Generated from the following TL definition:
    ```tl
    channelParticipantsSearch#656ac4b q:string = ChannelParticipantsFilter
    ```
    """
    def __new__(
        cls,
        q: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantsContacts(TLObject):
    """
    [Read `channelParticipantsContacts` docs](https://core.telegram.org/constructor/channelParticipantsContacts).

    Generated from the following TL definition:
    ```tl
    channelParticipantsContacts#bb6ae88d q:string = ChannelParticipantsFilter
    ```
    """
    def __new__(
        cls,
        q: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelParticipantsMentions(TLObject):
    """
    [Read `channelParticipantsMentions` docs](https://core.telegram.org/constructor/channelParticipantsMentions).

    Generated from the following TL definition:
    ```tl
    channelParticipantsMentions#e04b5ceb flags:# q:flags.0?string top_msg_id:flags.1?int = ChannelParticipantsFilter
    ```
    """
    def __new__(
        cls,
        q: Optional[str],
        top_msg_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineMessageMediaAuto(TLObject):
    """
    [Read `inputBotInlineMessageMediaAuto` docs](https://core.telegram.org/constructor/inputBotInlineMessageMediaAuto).

    Generated from the following TL definition:
    ```tl
    inputBotInlineMessageMediaAuto#3380c786 flags:# invert_media:flags.3?true message:string entities:flags.1?Vector<MessageEntity> reply_markup:flags.2?ReplyMarkup = InputBotInlineMessage
    ```
    """
    def __new__(
        cls,
        invert_media: bool,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineMessageText(TLObject):
    """
    [Read `inputBotInlineMessageText` docs](https://core.telegram.org/constructor/inputBotInlineMessageText).

    Generated from the following TL definition:
    ```tl
    inputBotInlineMessageText#3dcd7a87 flags:# no_webpage:flags.0?true invert_media:flags.3?true message:string entities:flags.1?Vector<MessageEntity> reply_markup:flags.2?ReplyMarkup = InputBotInlineMessage
    ```
    """
    def __new__(
        cls,
        no_webpage: bool,
        invert_media: bool,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineMessageMediaGeo(TLObject):
    """
    [Read `inputBotInlineMessageMediaGeo` docs](https://core.telegram.org/constructor/inputBotInlineMessageMediaGeo).

    Generated from the following TL definition:
    ```tl
    inputBotInlineMessageMediaGeo#96929a85 flags:# geo_point:InputGeoPoint heading:flags.0?int period:flags.1?int proximity_notification_radius:flags.3?int reply_markup:flags.2?ReplyMarkup = InputBotInlineMessage
    ```
    """
    def __new__(
        cls,
        geo_point: types.InputGeoPointEmpty | types.InputGeoPoint,
        heading: Optional[int],
        period: Optional[int],
        proximity_notification_radius: Optional[int],
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineMessageMediaVenue(TLObject):
    """
    [Read `inputBotInlineMessageMediaVenue` docs](https://core.telegram.org/constructor/inputBotInlineMessageMediaVenue).

    Generated from the following TL definition:
    ```tl
    inputBotInlineMessageMediaVenue#417bbf11 flags:# geo_point:InputGeoPoint title:string address:string provider:string venue_id:string venue_type:string reply_markup:flags.2?ReplyMarkup = InputBotInlineMessage
    ```
    """
    def __new__(
        cls,
        geo_point: types.InputGeoPointEmpty | types.InputGeoPoint,
        title: str,
        address: str,
        provider: str,
        venue_id: str,
        venue_type: str,
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineMessageMediaContact(TLObject):
    """
    [Read `inputBotInlineMessageMediaContact` docs](https://core.telegram.org/constructor/inputBotInlineMessageMediaContact).

    Generated from the following TL definition:
    ```tl
    inputBotInlineMessageMediaContact#a6edbffd flags:# phone_number:string first_name:string last_name:string vcard:string reply_markup:flags.2?ReplyMarkup = InputBotInlineMessage
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        first_name: str,
        last_name: str,
        vcard: str,
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineMessageGame(TLObject):
    """
    [Read `inputBotInlineMessageGame` docs](https://core.telegram.org/constructor/inputBotInlineMessageGame).

    Generated from the following TL definition:
    ```tl
    inputBotInlineMessageGame#4b425864 flags:# reply_markup:flags.2?ReplyMarkup = InputBotInlineMessage
    ```
    """
    def __new__(
        cls,
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineMessageMediaInvoice(TLObject):
    """
    [Read `inputBotInlineMessageMediaInvoice` docs](https://core.telegram.org/constructor/inputBotInlineMessageMediaInvoice).

    Generated from the following TL definition:
    ```tl
    inputBotInlineMessageMediaInvoice#d7e78225 flags:# title:string description:string photo:flags.0?InputWebDocument invoice:Invoice payload:bytes provider:string provider_data:DataJSON reply_markup:flags.2?ReplyMarkup = InputBotInlineMessage
    ```
    """
    def __new__(
        cls,
        title: str,
        description: str,
        photo: Optional[types.InputWebDocument],
        invoice: types.Invoice,
        payload: bytes,
        provider: str,
        provider_data: types.DataJson,
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineMessageMediaWebPage(TLObject):
    """
    [Read `inputBotInlineMessageMediaWebPage` docs](https://core.telegram.org/constructor/inputBotInlineMessageMediaWebPage).

    Generated from the following TL definition:
    ```tl
    inputBotInlineMessageMediaWebPage#bddcc510 flags:# invert_media:flags.3?true force_large_media:flags.4?true force_small_media:flags.5?true optional:flags.6?true message:string entities:flags.1?Vector<MessageEntity> url:string reply_markup:flags.2?ReplyMarkup = InputBotInlineMessage
    ```
    """
    def __new__(
        cls,
        invert_media: bool,
        force_large_media: bool,
        force_small_media: bool,
        optional: bool,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        url: str,
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineResult(TLObject):
    """
    [Read `inputBotInlineResult` docs](https://core.telegram.org/constructor/inputBotInlineResult).

    Generated from the following TL definition:
    ```tl
    inputBotInlineResult#88bf9319 flags:# id:string type:string title:flags.1?string description:flags.2?string url:flags.3?string thumb:flags.4?InputWebDocument content:flags.5?InputWebDocument send_message:InputBotInlineMessage = InputBotInlineResult
    ```
    """
    def __new__(
        cls,
        id: str,
        type: str,
        title: Optional[str],
        description: Optional[str],
        url: Optional[str],
        thumb: Optional[types.InputWebDocument],
        content: Optional[types.InputWebDocument],
        send_message: types.InputBotInlineMessageMediaAuto | types.InputBotInlineMessageText | types.InputBotInlineMessageMediaGeo | types.InputBotInlineMessageMediaVenue | types.InputBotInlineMessageMediaContact | types.InputBotInlineMessageGame | types.InputBotInlineMessageMediaInvoice | types.InputBotInlineMessageMediaWebPage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineResultPhoto(TLObject):
    """
    [Read `inputBotInlineResultPhoto` docs](https://core.telegram.org/constructor/inputBotInlineResultPhoto).

    Generated from the following TL definition:
    ```tl
    inputBotInlineResultPhoto#a8d864a7 id:string type:string photo:InputPhoto send_message:InputBotInlineMessage = InputBotInlineResult
    ```
    """
    def __new__(
        cls,
        id: str,
        type: str,
        photo: types.InputPhotoEmpty | types.InputPhoto,
        send_message: types.InputBotInlineMessageMediaAuto | types.InputBotInlineMessageText | types.InputBotInlineMessageMediaGeo | types.InputBotInlineMessageMediaVenue | types.InputBotInlineMessageMediaContact | types.InputBotInlineMessageGame | types.InputBotInlineMessageMediaInvoice | types.InputBotInlineMessageMediaWebPage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineResultDocument(TLObject):
    """
    [Read `inputBotInlineResultDocument` docs](https://core.telegram.org/constructor/inputBotInlineResultDocument).

    Generated from the following TL definition:
    ```tl
    inputBotInlineResultDocument#fff8fdc4 flags:# id:string type:string title:flags.1?string description:flags.2?string document:InputDocument send_message:InputBotInlineMessage = InputBotInlineResult
    ```
    """
    def __new__(
        cls,
        id: str,
        type: str,
        title: Optional[str],
        description: Optional[str],
        document: types.InputDocumentEmpty | types.InputDocument,
        send_message: types.InputBotInlineMessageMediaAuto | types.InputBotInlineMessageText | types.InputBotInlineMessageMediaGeo | types.InputBotInlineMessageMediaVenue | types.InputBotInlineMessageMediaContact | types.InputBotInlineMessageGame | types.InputBotInlineMessageMediaInvoice | types.InputBotInlineMessageMediaWebPage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineResultGame(TLObject):
    """
    [Read `inputBotInlineResultGame` docs](https://core.telegram.org/constructor/inputBotInlineResultGame).

    Generated from the following TL definition:
    ```tl
    inputBotInlineResultGame#4fa417f2 id:string short_name:string send_message:InputBotInlineMessage = InputBotInlineResult
    ```
    """
    def __new__(
        cls,
        id: str,
        short_name: str,
        send_message: types.InputBotInlineMessageMediaAuto | types.InputBotInlineMessageText | types.InputBotInlineMessageMediaGeo | types.InputBotInlineMessageMediaVenue | types.InputBotInlineMessageMediaContact | types.InputBotInlineMessageGame | types.InputBotInlineMessageMediaInvoice | types.InputBotInlineMessageMediaWebPage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotInlineMessageMediaAuto(TLObject):
    """
    [Read `botInlineMessageMediaAuto` docs](https://core.telegram.org/constructor/botInlineMessageMediaAuto).

    Generated from the following TL definition:
    ```tl
    botInlineMessageMediaAuto#764cf810 flags:# invert_media:flags.3?true message:string entities:flags.1?Vector<MessageEntity> reply_markup:flags.2?ReplyMarkup = BotInlineMessage
    ```
    """
    def __new__(
        cls,
        invert_media: bool,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotInlineMessageText(TLObject):
    """
    [Read `botInlineMessageText` docs](https://core.telegram.org/constructor/botInlineMessageText).

    Generated from the following TL definition:
    ```tl
    botInlineMessageText#8c7f65e2 flags:# no_webpage:flags.0?true invert_media:flags.3?true message:string entities:flags.1?Vector<MessageEntity> reply_markup:flags.2?ReplyMarkup = BotInlineMessage
    ```
    """
    def __new__(
        cls,
        no_webpage: bool,
        invert_media: bool,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotInlineMessageMediaGeo(TLObject):
    """
    [Read `botInlineMessageMediaGeo` docs](https://core.telegram.org/constructor/botInlineMessageMediaGeo).

    Generated from the following TL definition:
    ```tl
    botInlineMessageMediaGeo#51846fd flags:# geo:GeoPoint heading:flags.0?int period:flags.1?int proximity_notification_radius:flags.3?int reply_markup:flags.2?ReplyMarkup = BotInlineMessage
    ```
    """
    def __new__(
        cls,
        geo: types.GeoPointEmpty | types.GeoPoint,
        heading: Optional[int],
        period: Optional[int],
        proximity_notification_radius: Optional[int],
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotInlineMessageMediaVenue(TLObject):
    """
    [Read `botInlineMessageMediaVenue` docs](https://core.telegram.org/constructor/botInlineMessageMediaVenue).

    Generated from the following TL definition:
    ```tl
    botInlineMessageMediaVenue#8a86659c flags:# geo:GeoPoint title:string address:string provider:string venue_id:string venue_type:string reply_markup:flags.2?ReplyMarkup = BotInlineMessage
    ```
    """
    def __new__(
        cls,
        geo: types.GeoPointEmpty | types.GeoPoint,
        title: str,
        address: str,
        provider: str,
        venue_id: str,
        venue_type: str,
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotInlineMessageMediaContact(TLObject):
    """
    [Read `botInlineMessageMediaContact` docs](https://core.telegram.org/constructor/botInlineMessageMediaContact).

    Generated from the following TL definition:
    ```tl
    botInlineMessageMediaContact#18d1cdc2 flags:# phone_number:string first_name:string last_name:string vcard:string reply_markup:flags.2?ReplyMarkup = BotInlineMessage
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        first_name: str,
        last_name: str,
        vcard: str,
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotInlineMessageMediaInvoice(TLObject):
    """
    [Read `botInlineMessageMediaInvoice` docs](https://core.telegram.org/constructor/botInlineMessageMediaInvoice).

    Generated from the following TL definition:
    ```tl
    botInlineMessageMediaInvoice#354a9b09 flags:# shipping_address_requested:flags.1?true test:flags.3?true title:string description:string photo:flags.0?WebDocument currency:string total_amount:long reply_markup:flags.2?ReplyMarkup = BotInlineMessage
    ```
    """
    def __new__(
        cls,
        shipping_address_requested: bool,
        test: bool,
        title: str,
        description: str,
        photo: Optional[types.WebDocument | types.WebDocumentNoProxy],
        currency: str,
        total_amount: int,
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotInlineMessageMediaWebPage(TLObject):
    """
    [Read `botInlineMessageMediaWebPage` docs](https://core.telegram.org/constructor/botInlineMessageMediaWebPage).

    Generated from the following TL definition:
    ```tl
    botInlineMessageMediaWebPage#809ad9a6 flags:# invert_media:flags.3?true force_large_media:flags.4?true force_small_media:flags.5?true manual:flags.7?true safe:flags.8?true message:string entities:flags.1?Vector<MessageEntity> url:string reply_markup:flags.2?ReplyMarkup = BotInlineMessage
    ```
    """
    def __new__(
        cls,
        invert_media: bool,
        force_large_media: bool,
        force_small_media: bool,
        manual: bool,
        safe: bool,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        url: str,
        reply_markup: Optional[types.ReplyKeyboardHide | types.ReplyKeyboardForceReply | types.ReplyKeyboardMarkup | types.ReplyInlineMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotInlineResult(TLObject):
    """
    [Read `botInlineResult` docs](https://core.telegram.org/constructor/botInlineResult).

    Generated from the following TL definition:
    ```tl
    botInlineResult#11965f3a flags:# id:string type:string title:flags.1?string description:flags.2?string url:flags.3?string thumb:flags.4?WebDocument content:flags.5?WebDocument send_message:BotInlineMessage = BotInlineResult
    ```
    """
    def __new__(
        cls,
        id: str,
        type: str,
        title: Optional[str],
        description: Optional[str],
        url: Optional[str],
        thumb: Optional[types.WebDocument | types.WebDocumentNoProxy],
        content: Optional[types.WebDocument | types.WebDocumentNoProxy],
        send_message: types.BotInlineMessageMediaAuto | types.BotInlineMessageText | types.BotInlineMessageMediaGeo | types.BotInlineMessageMediaVenue | types.BotInlineMessageMediaContact | types.BotInlineMessageMediaInvoice | types.BotInlineMessageMediaWebPage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotInlineMediaResult(TLObject):
    """
    [Read `botInlineMediaResult` docs](https://core.telegram.org/constructor/botInlineMediaResult).

    Generated from the following TL definition:
    ```tl
    botInlineMediaResult#17db940b flags:# id:string type:string photo:flags.0?Photo document:flags.1?Document title:flags.2?string description:flags.3?string send_message:BotInlineMessage = BotInlineResult
    ```
    """
    def __new__(
        cls,
        id: str,
        type: str,
        photo: Optional[types.PhotoEmpty | types.Photo],
        document: Optional[types.DocumentEmpty | types.Document],
        title: Optional[str],
        description: Optional[str],
        send_message: types.BotInlineMessageMediaAuto | types.BotInlineMessageText | types.BotInlineMessageMediaGeo | types.BotInlineMessageMediaVenue | types.BotInlineMessageMediaContact | types.BotInlineMessageMediaInvoice | types.BotInlineMessageMediaWebPage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportedMessageLink(TLObject):
    """
    [Read `exportedMessageLink` docs](https://core.telegram.org/constructor/exportedMessageLink).

    Generated from the following TL definition:
    ```tl
    exportedMessageLink#5dab1af4 link:string html:string = ExportedMessageLink
    ```
    """
    def __new__(
        cls,
        link: str,
        html: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageFwdHeader(TLObject):
    """
    [Read `messageFwdHeader` docs](https://core.telegram.org/constructor/messageFwdHeader).

    Generated from the following TL definition:
    ```tl
    messageFwdHeader#4e4df4bb flags:# imported:flags.7?true saved_out:flags.11?true from_id:flags.0?Peer from_name:flags.5?string date:int channel_post:flags.2?int post_author:flags.3?string saved_from_peer:flags.4?Peer saved_from_msg_id:flags.4?int saved_from_id:flags.8?Peer saved_from_name:flags.9?string saved_date:flags.10?int psa_type:flags.6?string = MessageFwdHeader
    ```
    """
    def __new__(
        cls,
        imported: bool,
        saved_out: bool,
        from_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        from_name: Optional[str],
        date: int,
        channel_post: Optional[int],
        post_author: Optional[str],
        saved_from_peer: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        saved_from_msg_id: Optional[int],
        saved_from_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        saved_from_name: Optional[str],
        saved_date: Optional[int],
        psa_type: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineMessageId(TLObject):
    """
    [Read `inputBotInlineMessageID` docs](https://core.telegram.org/constructor/inputBotInlineMessageID).

    Generated from the following TL definition:
    ```tl
    inputBotInlineMessageID#890c3d89 dc_id:int id:long access_hash:long = InputBotInlineMessageID
    ```
    """
    def __new__(
        cls,
        dc_id: int,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotInlineMessageId64(TLObject):
    """
    [Read `inputBotInlineMessageID64` docs](https://core.telegram.org/constructor/inputBotInlineMessageID64).

    Generated from the following TL definition:
    ```tl
    inputBotInlineMessageID64#b6d915d7 dc_id:int owner_id:long id:int access_hash:long = InputBotInlineMessageID
    ```
    """
    def __new__(
        cls,
        dc_id: int,
        owner_id: int,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InlineBotSwitchPm(TLObject):
    """
    [Read `inlineBotSwitchPM` docs](https://core.telegram.org/constructor/inlineBotSwitchPM).

    Generated from the following TL definition:
    ```tl
    inlineBotSwitchPM#3c20629f text:string start_param:string = InlineBotSwitchPM
    ```
    """
    def __new__(
        cls,
        text: str,
        start_param: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeer(TLObject):
    """
    [Read `topPeer` docs](https://core.telegram.org/constructor/topPeer).

    Generated from the following TL definition:
    ```tl
    topPeer#edcdc05b peer:Peer rating:double = TopPeer
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        rating: float,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeerCategoryBotsPm(TLObject):
    """
    [Read `topPeerCategoryBotsPM` docs](https://core.telegram.org/constructor/topPeerCategoryBotsPM).

    Generated from the following TL definition:
    ```tl
    topPeerCategoryBotsPM#ab661b5b = TopPeerCategory
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeerCategoryBotsInline(TLObject):
    """
    [Read `topPeerCategoryBotsInline` docs](https://core.telegram.org/constructor/topPeerCategoryBotsInline).

    Generated from the following TL definition:
    ```tl
    topPeerCategoryBotsInline#148677e2 = TopPeerCategory
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeerCategoryCorrespondents(TLObject):
    """
    [Read `topPeerCategoryCorrespondents` docs](https://core.telegram.org/constructor/topPeerCategoryCorrespondents).

    Generated from the following TL definition:
    ```tl
    topPeerCategoryCorrespondents#637b7ed = TopPeerCategory
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeerCategoryGroups(TLObject):
    """
    [Read `topPeerCategoryGroups` docs](https://core.telegram.org/constructor/topPeerCategoryGroups).

    Generated from the following TL definition:
    ```tl
    topPeerCategoryGroups#bd17a14a = TopPeerCategory
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeerCategoryChannels(TLObject):
    """
    [Read `topPeerCategoryChannels` docs](https://core.telegram.org/constructor/topPeerCategoryChannels).

    Generated from the following TL definition:
    ```tl
    topPeerCategoryChannels#161d9628 = TopPeerCategory
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeerCategoryPhoneCalls(TLObject):
    """
    [Read `topPeerCategoryPhoneCalls` docs](https://core.telegram.org/constructor/topPeerCategoryPhoneCalls).

    Generated from the following TL definition:
    ```tl
    topPeerCategoryPhoneCalls#1e76a78c = TopPeerCategory
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeerCategoryForwardUsers(TLObject):
    """
    [Read `topPeerCategoryForwardUsers` docs](https://core.telegram.org/constructor/topPeerCategoryForwardUsers).

    Generated from the following TL definition:
    ```tl
    topPeerCategoryForwardUsers#a8406ca9 = TopPeerCategory
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeerCategoryForwardChats(TLObject):
    """
    [Read `topPeerCategoryForwardChats` docs](https://core.telegram.org/constructor/topPeerCategoryForwardChats).

    Generated from the following TL definition:
    ```tl
    topPeerCategoryForwardChats#fbeec0f0 = TopPeerCategory
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeerCategoryBotsApp(TLObject):
    """
    [Read `topPeerCategoryBotsApp` docs](https://core.telegram.org/constructor/topPeerCategoryBotsApp).

    Generated from the following TL definition:
    ```tl
    topPeerCategoryBotsApp#fd9e7bec = TopPeerCategory
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TopPeerCategoryPeers(TLObject):
    """
    [Read `topPeerCategoryPeers` docs](https://core.telegram.org/constructor/topPeerCategoryPeers).

    Generated from the following TL definition:
    ```tl
    topPeerCategoryPeers#fb834291 category:TopPeerCategory count:int peers:Vector<TopPeer> = TopPeerCategoryPeers
    ```
    """
    def __new__(
        cls,
        category: types.TopPeerCategoryBotsPm | types.TopPeerCategoryBotsInline | types.TopPeerCategoryCorrespondents | types.TopPeerCategoryGroups | types.TopPeerCategoryChannels | types.TopPeerCategoryPhoneCalls | types.TopPeerCategoryForwardUsers | types.TopPeerCategoryForwardChats | types.TopPeerCategoryBotsApp,
        count: int,
        peers: Sequence[types.TopPeer],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DraftMessageEmpty(TLObject):
    """
    [Read `draftMessageEmpty` docs](https://core.telegram.org/constructor/draftMessageEmpty).

    Generated from the following TL definition:
    ```tl
    draftMessageEmpty#1b0c841a flags:# date:flags.0?int = DraftMessage
    ```
    """
    def __new__(
        cls,
        date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DraftMessage(TLObject):
    """
    [Read `draftMessage` docs](https://core.telegram.org/constructor/draftMessage).

    Generated from the following TL definition:
    ```tl
    draftMessage#96eaa5eb flags:# no_webpage:flags.1?true invert_media:flags.6?true reply_to:flags.4?InputReplyTo message:string entities:flags.3?Vector<MessageEntity> media:flags.5?InputMedia date:int effect:flags.7?long suggested_post:flags.8?SuggestedPost = DraftMessage
    ```
    """
    def __new__(
        cls,
        no_webpage: bool,
        invert_media: bool,
        reply_to: Optional[types.InputReplyToMessage | types.InputReplyToStory | types.InputReplyToMonoForum],
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        media: Optional[types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice],
        date: int,
        effect: Optional[int],
        suggested_post: Optional[types.SuggestedPost],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StickerSetCovered(TLObject):
    """
    [Read `stickerSetCovered` docs](https://core.telegram.org/constructor/stickerSetCovered).

    Generated from the following TL definition:
    ```tl
    stickerSetCovered#6410a5d2 set:StickerSet cover:Document = StickerSetCovered
    ```
    """
    def __new__(
        cls,
        set: types.StickerSet,
        cover: types.DocumentEmpty | types.Document,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StickerSetMultiCovered(TLObject):
    """
    [Read `stickerSetMultiCovered` docs](https://core.telegram.org/constructor/stickerSetMultiCovered).

    Generated from the following TL definition:
    ```tl
    stickerSetMultiCovered#3407e51b set:StickerSet covers:Vector<Document> = StickerSetCovered
    ```
    """
    def __new__(
        cls,
        set: types.StickerSet,
        covers: Sequence[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StickerSetFullCovered(TLObject):
    """
    [Read `stickerSetFullCovered` docs](https://core.telegram.org/constructor/stickerSetFullCovered).

    Generated from the following TL definition:
    ```tl
    stickerSetFullCovered#40d13c0e set:StickerSet packs:Vector<StickerPack> keywords:Vector<StickerKeyword> documents:Vector<Document> = StickerSetCovered
    ```
    """
    def __new__(
        cls,
        set: types.StickerSet,
        packs: Sequence[types.StickerPack],
        keywords: Sequence[types.StickerKeyword],
        documents: Sequence[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StickerSetNoCovered(TLObject):
    """
    [Read `stickerSetNoCovered` docs](https://core.telegram.org/constructor/stickerSetNoCovered).

    Generated from the following TL definition:
    ```tl
    stickerSetNoCovered#77b15d1c set:StickerSet = StickerSetCovered
    ```
    """
    def __new__(
        cls,
        set: types.StickerSet,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MaskCoords(TLObject):
    """
    [Read `maskCoords` docs](https://core.telegram.org/constructor/maskCoords).

    Generated from the following TL definition:
    ```tl
    maskCoords#aed6dbb2 n:int x:double y:double zoom:double = MaskCoords
    ```
    """
    def __new__(
        cls,
        n: int,
        x: float,
        y: float,
        zoom: float,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickeredMediaPhoto(TLObject):
    """
    [Read `inputStickeredMediaPhoto` docs](https://core.telegram.org/constructor/inputStickeredMediaPhoto).

    Generated from the following TL definition:
    ```tl
    inputStickeredMediaPhoto#4a992157 id:InputPhoto = InputStickeredMedia
    ```
    """
    def __new__(
        cls,
        id: types.InputPhotoEmpty | types.InputPhoto,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickeredMediaDocument(TLObject):
    """
    [Read `inputStickeredMediaDocument` docs](https://core.telegram.org/constructor/inputStickeredMediaDocument).

    Generated from the following TL definition:
    ```tl
    inputStickeredMediaDocument#438865b id:InputDocument = InputStickeredMedia
    ```
    """
    def __new__(
        cls,
        id: types.InputDocumentEmpty | types.InputDocument,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Game(TLObject):
    """
    [Read `game` docs](https://core.telegram.org/constructor/game).

    Generated from the following TL definition:
    ```tl
    game#bdf9653b flags:# id:long access_hash:long short_name:string title:string description:string photo:Photo document:flags.0?Document = Game
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        short_name: str,
        title: str,
        description: str,
        photo: types.PhotoEmpty | types.Photo,
        document: Optional[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputGameId(TLObject):
    """
    [Read `inputGameID` docs](https://core.telegram.org/constructor/inputGameID).

    Generated from the following TL definition:
    ```tl
    inputGameID#32c3e77 id:long access_hash:long = InputGame
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputGameShortName(TLObject):
    """
    [Read `inputGameShortName` docs](https://core.telegram.org/constructor/inputGameShortName).

    Generated from the following TL definition:
    ```tl
    inputGameShortName#c331e80a bot_id:InputUser short_name:string = InputGame
    ```
    """
    def __new__(
        cls,
        bot_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        short_name: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class HighScore(TLObject):
    """
    [Read `highScore` docs](https://core.telegram.org/constructor/highScore).

    Generated from the following TL definition:
    ```tl
    highScore#73a379eb pos:int user_id:long score:int = HighScore
    ```
    """
    def __new__(
        cls,
        pos: int,
        user_id: int,
        score: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextEmpty(TLObject):
    """
    [Read `textEmpty` docs](https://core.telegram.org/constructor/textEmpty).

    Generated from the following TL definition:
    ```tl
    textEmpty#dc3d824f = RichText
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextPlain(TLObject):
    """
    [Read `textPlain` docs](https://core.telegram.org/constructor/textPlain).

    Generated from the following TL definition:
    ```tl
    textPlain#744694e0 text:string = RichText
    ```
    """
    def __new__(
        cls,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextBold(TLObject):
    """
    [Read `textBold` docs](https://core.telegram.org/constructor/textBold).

    Generated from the following TL definition:
    ```tl
    textBold#6724abc4 text:RichText = RichText
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextItalic(TLObject):
    """
    [Read `textItalic` docs](https://core.telegram.org/constructor/textItalic).

    Generated from the following TL definition:
    ```tl
    textItalic#d912a59c text:RichText = RichText
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextUnderline(TLObject):
    """
    [Read `textUnderline` docs](https://core.telegram.org/constructor/textUnderline).

    Generated from the following TL definition:
    ```tl
    textUnderline#c12622c4 text:RichText = RichText
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextStrike(TLObject):
    """
    [Read `textStrike` docs](https://core.telegram.org/constructor/textStrike).

    Generated from the following TL definition:
    ```tl
    textStrike#9bf8bb95 text:RichText = RichText
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextFixed(TLObject):
    """
    [Read `textFixed` docs](https://core.telegram.org/constructor/textFixed).

    Generated from the following TL definition:
    ```tl
    textFixed#6c3f19b9 text:RichText = RichText
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextUrl(TLObject):
    """
    [Read `textUrl` docs](https://core.telegram.org/constructor/textUrl).

    Generated from the following TL definition:
    ```tl
    textUrl#3c2884c1 text:RichText url:string webpage_id:long = RichText
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
        url: str,
        webpage_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextEmail(TLObject):
    """
    [Read `textEmail` docs](https://core.telegram.org/constructor/textEmail).

    Generated from the following TL definition:
    ```tl
    textEmail#de5a0dd6 text:RichText email:string = RichText
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
        email: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextConcat(TLObject):
    """
    [Read `textConcat` docs](https://core.telegram.org/constructor/textConcat).

    Generated from the following TL definition:
    ```tl
    textConcat#7e6260d7 texts:Vector<RichText> = RichText
    ```
    """
    def __new__(
        cls,
        texts: Sequence[types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextSubscript(TLObject):
    """
    [Read `textSubscript` docs](https://core.telegram.org/constructor/textSubscript).

    Generated from the following TL definition:
    ```tl
    textSubscript#ed6a8504 text:RichText = RichText
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextSuperscript(TLObject):
    """
    [Read `textSuperscript` docs](https://core.telegram.org/constructor/textSuperscript).

    Generated from the following TL definition:
    ```tl
    textSuperscript#c7fb5e01 text:RichText = RichText
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextMarked(TLObject):
    """
    [Read `textMarked` docs](https://core.telegram.org/constructor/textMarked).

    Generated from the following TL definition:
    ```tl
    textMarked#34b8621 text:RichText = RichText
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextPhone(TLObject):
    """
    [Read `textPhone` docs](https://core.telegram.org/constructor/textPhone).

    Generated from the following TL definition:
    ```tl
    textPhone#1ccb966a text:RichText phone:string = RichText
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
        phone: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextImage(TLObject):
    """
    [Read `textImage` docs](https://core.telegram.org/constructor/textImage).

    Generated from the following TL definition:
    ```tl
    textImage#81ccf4f document_id:long w:int h:int = RichText
    ```
    """
    def __new__(
        cls,
        document_id: int,
        w: int,
        h: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextAnchor(TLObject):
    """
    [Read `textAnchor` docs](https://core.telegram.org/constructor/textAnchor).

    Generated from the following TL definition:
    ```tl
    textAnchor#35553762 text:RichText name:string = RichText
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
        name: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockUnsupported(TLObject):
    """
    [Read `pageBlockUnsupported` docs](https://core.telegram.org/constructor/pageBlockUnsupported).

    Generated from the following TL definition:
    ```tl
    pageBlockUnsupported#13567e8a = PageBlock
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockTitle(TLObject):
    """
    [Read `pageBlockTitle` docs](https://core.telegram.org/constructor/pageBlockTitle).

    Generated from the following TL definition:
    ```tl
    pageBlockTitle#70abc3fd text:RichText = PageBlock
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockSubtitle(TLObject):
    """
    [Read `pageBlockSubtitle` docs](https://core.telegram.org/constructor/pageBlockSubtitle).

    Generated from the following TL definition:
    ```tl
    pageBlockSubtitle#8ffa9a1f text:RichText = PageBlock
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockAuthorDate(TLObject):
    """
    [Read `pageBlockAuthorDate` docs](https://core.telegram.org/constructor/pageBlockAuthorDate).

    Generated from the following TL definition:
    ```tl
    pageBlockAuthorDate#baafe5e0 author:RichText published_date:int = PageBlock
    ```
    """
    def __new__(
        cls,
        author: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
        published_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockHeader(TLObject):
    """
    [Read `pageBlockHeader` docs](https://core.telegram.org/constructor/pageBlockHeader).

    Generated from the following TL definition:
    ```tl
    pageBlockHeader#bfd064ec text:RichText = PageBlock
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockSubheader(TLObject):
    """
    [Read `pageBlockSubheader` docs](https://core.telegram.org/constructor/pageBlockSubheader).

    Generated from the following TL definition:
    ```tl
    pageBlockSubheader#f12bb6e1 text:RichText = PageBlock
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockParagraph(TLObject):
    """
    [Read `pageBlockParagraph` docs](https://core.telegram.org/constructor/pageBlockParagraph).

    Generated from the following TL definition:
    ```tl
    pageBlockParagraph#467a0766 text:RichText = PageBlock
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockPreformatted(TLObject):
    """
    [Read `pageBlockPreformatted` docs](https://core.telegram.org/constructor/pageBlockPreformatted).

    Generated from the following TL definition:
    ```tl
    pageBlockPreformatted#c070d93e text:RichText language:string = PageBlock
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
        language: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockFooter(TLObject):
    """
    [Read `pageBlockFooter` docs](https://core.telegram.org/constructor/pageBlockFooter).

    Generated from the following TL definition:
    ```tl
    pageBlockFooter#48870999 text:RichText = PageBlock
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockDivider(TLObject):
    """
    [Read `pageBlockDivider` docs](https://core.telegram.org/constructor/pageBlockDivider).

    Generated from the following TL definition:
    ```tl
    pageBlockDivider#db20b188 = PageBlock
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockAnchor(TLObject):
    """
    [Read `pageBlockAnchor` docs](https://core.telegram.org/constructor/pageBlockAnchor).

    Generated from the following TL definition:
    ```tl
    pageBlockAnchor#ce0d37b0 name:string = PageBlock
    ```
    """
    def __new__(
        cls,
        name: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockList(TLObject):
    """
    [Read `pageBlockList` docs](https://core.telegram.org/constructor/pageBlockList).

    Generated from the following TL definition:
    ```tl
    pageBlockList#e4e88011 items:Vector<PageListItem> = PageBlock
    ```
    """
    def __new__(
        cls,
        items: Sequence[types.PageListItemText | types.PageListItemBlocks],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockBlockquote(TLObject):
    """
    [Read `pageBlockBlockquote` docs](https://core.telegram.org/constructor/pageBlockBlockquote).

    Generated from the following TL definition:
    ```tl
    pageBlockBlockquote#263d7c26 text:RichText caption:RichText = PageBlock
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
        caption: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockPullquote(TLObject):
    """
    [Read `pageBlockPullquote` docs](https://core.telegram.org/constructor/pageBlockPullquote).

    Generated from the following TL definition:
    ```tl
    pageBlockPullquote#4f4456d3 text:RichText caption:RichText = PageBlock
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
        caption: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockPhoto(TLObject):
    """
    [Read `pageBlockPhoto` docs](https://core.telegram.org/constructor/pageBlockPhoto).

    Generated from the following TL definition:
    ```tl
    pageBlockPhoto#1759c560 flags:# photo_id:long caption:PageCaption url:flags.0?string webpage_id:flags.0?long = PageBlock
    ```
    """
    def __new__(
        cls,
        photo_id: int,
        caption: types.PageCaption,
        url: Optional[str],
        webpage_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockVideo(TLObject):
    """
    [Read `pageBlockVideo` docs](https://core.telegram.org/constructor/pageBlockVideo).

    Generated from the following TL definition:
    ```tl
    pageBlockVideo#7c8fe7b6 flags:# autoplay:flags.0?true loop:flags.1?true video_id:long caption:PageCaption = PageBlock
    ```
    """
    def __new__(
        cls,
        autoplay: bool,
        loop: bool,
        video_id: int,
        caption: types.PageCaption,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockCover(TLObject):
    """
    [Read `pageBlockCover` docs](https://core.telegram.org/constructor/pageBlockCover).

    Generated from the following TL definition:
    ```tl
    pageBlockCover#39f23300 cover:PageBlock = PageBlock
    ```
    """
    def __new__(
        cls,
        cover: types.PageBlockUnsupported | types.PageBlockTitle | types.PageBlockSubtitle | types.PageBlockAuthorDate | types.PageBlockHeader | types.PageBlockSubheader | types.PageBlockParagraph | types.PageBlockPreformatted | types.PageBlockFooter | types.PageBlockDivider | types.PageBlockAnchor | types.PageBlockList | types.PageBlockBlockquote | types.PageBlockPullquote | types.PageBlockPhoto | types.PageBlockVideo | types.PageBlockCover | types.PageBlockEmbed | types.PageBlockEmbedPost | types.PageBlockCollage | types.PageBlockSlideshow | types.PageBlockChannel | types.PageBlockAudio | types.PageBlockKicker | types.PageBlockTable | types.PageBlockOrderedList | types.PageBlockDetails | types.PageBlockRelatedArticles | types.PageBlockMap,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockEmbed(TLObject):
    """
    [Read `pageBlockEmbed` docs](https://core.telegram.org/constructor/pageBlockEmbed).

    Generated from the following TL definition:
    ```tl
    pageBlockEmbed#a8718dc5 flags:# full_width:flags.0?true allow_scrolling:flags.3?true url:flags.1?string html:flags.2?string poster_photo_id:flags.4?long w:flags.5?int h:flags.5?int caption:PageCaption = PageBlock
    ```
    """
    def __new__(
        cls,
        full_width: bool,
        allow_scrolling: bool,
        url: Optional[str],
        html: Optional[str],
        poster_photo_id: Optional[int],
        w: Optional[int],
        h: Optional[int],
        caption: types.PageCaption,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockEmbedPost(TLObject):
    """
    [Read `pageBlockEmbedPost` docs](https://core.telegram.org/constructor/pageBlockEmbedPost).

    Generated from the following TL definition:
    ```tl
    pageBlockEmbedPost#f259a80b url:string webpage_id:long author_photo_id:long author:string date:int blocks:Vector<PageBlock> caption:PageCaption = PageBlock
    ```
    """
    def __new__(
        cls,
        url: str,
        webpage_id: int,
        author_photo_id: int,
        author: str,
        date: int,
        blocks: Sequence[types.PageBlockUnsupported | types.PageBlockTitle | types.PageBlockSubtitle | types.PageBlockAuthorDate | types.PageBlockHeader | types.PageBlockSubheader | types.PageBlockParagraph | types.PageBlockPreformatted | types.PageBlockFooter | types.PageBlockDivider | types.PageBlockAnchor | types.PageBlockList | types.PageBlockBlockquote | types.PageBlockPullquote | types.PageBlockPhoto | types.PageBlockVideo | types.PageBlockCover | types.PageBlockEmbed | types.PageBlockEmbedPost | types.PageBlockCollage | types.PageBlockSlideshow | types.PageBlockChannel | types.PageBlockAudio | types.PageBlockKicker | types.PageBlockTable | types.PageBlockOrderedList | types.PageBlockDetails | types.PageBlockRelatedArticles | types.PageBlockMap],
        caption: types.PageCaption,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockCollage(TLObject):
    """
    [Read `pageBlockCollage` docs](https://core.telegram.org/constructor/pageBlockCollage).

    Generated from the following TL definition:
    ```tl
    pageBlockCollage#65a0fa4d items:Vector<PageBlock> caption:PageCaption = PageBlock
    ```
    """
    def __new__(
        cls,
        items: Sequence[types.PageBlockUnsupported | types.PageBlockTitle | types.PageBlockSubtitle | types.PageBlockAuthorDate | types.PageBlockHeader | types.PageBlockSubheader | types.PageBlockParagraph | types.PageBlockPreformatted | types.PageBlockFooter | types.PageBlockDivider | types.PageBlockAnchor | types.PageBlockList | types.PageBlockBlockquote | types.PageBlockPullquote | types.PageBlockPhoto | types.PageBlockVideo | types.PageBlockCover | types.PageBlockEmbed | types.PageBlockEmbedPost | types.PageBlockCollage | types.PageBlockSlideshow | types.PageBlockChannel | types.PageBlockAudio | types.PageBlockKicker | types.PageBlockTable | types.PageBlockOrderedList | types.PageBlockDetails | types.PageBlockRelatedArticles | types.PageBlockMap],
        caption: types.PageCaption,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockSlideshow(TLObject):
    """
    [Read `pageBlockSlideshow` docs](https://core.telegram.org/constructor/pageBlockSlideshow).

    Generated from the following TL definition:
    ```tl
    pageBlockSlideshow#31f9590 items:Vector<PageBlock> caption:PageCaption = PageBlock
    ```
    """
    def __new__(
        cls,
        items: Sequence[types.PageBlockUnsupported | types.PageBlockTitle | types.PageBlockSubtitle | types.PageBlockAuthorDate | types.PageBlockHeader | types.PageBlockSubheader | types.PageBlockParagraph | types.PageBlockPreformatted | types.PageBlockFooter | types.PageBlockDivider | types.PageBlockAnchor | types.PageBlockList | types.PageBlockBlockquote | types.PageBlockPullquote | types.PageBlockPhoto | types.PageBlockVideo | types.PageBlockCover | types.PageBlockEmbed | types.PageBlockEmbedPost | types.PageBlockCollage | types.PageBlockSlideshow | types.PageBlockChannel | types.PageBlockAudio | types.PageBlockKicker | types.PageBlockTable | types.PageBlockOrderedList | types.PageBlockDetails | types.PageBlockRelatedArticles | types.PageBlockMap],
        caption: types.PageCaption,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockChannel(TLObject):
    """
    [Read `pageBlockChannel` docs](https://core.telegram.org/constructor/pageBlockChannel).

    Generated from the following TL definition:
    ```tl
    pageBlockChannel#ef1751b5 channel:Chat = PageBlock
    ```
    """
    def __new__(
        cls,
        channel: types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockAudio(TLObject):
    """
    [Read `pageBlockAudio` docs](https://core.telegram.org/constructor/pageBlockAudio).

    Generated from the following TL definition:
    ```tl
    pageBlockAudio#804361ea audio_id:long caption:PageCaption = PageBlock
    ```
    """
    def __new__(
        cls,
        audio_id: int,
        caption: types.PageCaption,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockKicker(TLObject):
    """
    [Read `pageBlockKicker` docs](https://core.telegram.org/constructor/pageBlockKicker).

    Generated from the following TL definition:
    ```tl
    pageBlockKicker#1e148390 text:RichText = PageBlock
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockTable(TLObject):
    """
    [Read `pageBlockTable` docs](https://core.telegram.org/constructor/pageBlockTable).

    Generated from the following TL definition:
    ```tl
    pageBlockTable#bf4dea82 flags:# bordered:flags.0?true striped:flags.1?true title:RichText rows:Vector<PageTableRow> = PageBlock
    ```
    """
    def __new__(
        cls,
        bordered: bool,
        striped: bool,
        title: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
        rows: Sequence[types.PageTableRow],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockOrderedList(TLObject):
    """
    [Read `pageBlockOrderedList` docs](https://core.telegram.org/constructor/pageBlockOrderedList).

    Generated from the following TL definition:
    ```tl
    pageBlockOrderedList#9a8ae1e1 items:Vector<PageListOrderedItem> = PageBlock
    ```
    """
    def __new__(
        cls,
        items: Sequence[types.PageListOrderedItemText | types.PageListOrderedItemBlocks],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockDetails(TLObject):
    """
    [Read `pageBlockDetails` docs](https://core.telegram.org/constructor/pageBlockDetails).

    Generated from the following TL definition:
    ```tl
    pageBlockDetails#76768bed flags:# open:flags.0?true blocks:Vector<PageBlock> title:RichText = PageBlock
    ```
    """
    def __new__(
        cls,
        open: bool,
        blocks: Sequence[types.PageBlockUnsupported | types.PageBlockTitle | types.PageBlockSubtitle | types.PageBlockAuthorDate | types.PageBlockHeader | types.PageBlockSubheader | types.PageBlockParagraph | types.PageBlockPreformatted | types.PageBlockFooter | types.PageBlockDivider | types.PageBlockAnchor | types.PageBlockList | types.PageBlockBlockquote | types.PageBlockPullquote | types.PageBlockPhoto | types.PageBlockVideo | types.PageBlockCover | types.PageBlockEmbed | types.PageBlockEmbedPost | types.PageBlockCollage | types.PageBlockSlideshow | types.PageBlockChannel | types.PageBlockAudio | types.PageBlockKicker | types.PageBlockTable | types.PageBlockOrderedList | types.PageBlockDetails | types.PageBlockRelatedArticles | types.PageBlockMap],
        title: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockRelatedArticles(TLObject):
    """
    [Read `pageBlockRelatedArticles` docs](https://core.telegram.org/constructor/pageBlockRelatedArticles).

    Generated from the following TL definition:
    ```tl
    pageBlockRelatedArticles#16115a96 title:RichText articles:Vector<PageRelatedArticle> = PageBlock
    ```
    """
    def __new__(
        cls,
        title: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
        articles: Sequence[types.PageRelatedArticle],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageBlockMap(TLObject):
    """
    [Read `pageBlockMap` docs](https://core.telegram.org/constructor/pageBlockMap).

    Generated from the following TL definition:
    ```tl
    pageBlockMap#a44f3ef6 geo:GeoPoint zoom:int w:int h:int caption:PageCaption = PageBlock
    ```
    """
    def __new__(
        cls,
        geo: types.GeoPointEmpty | types.GeoPoint,
        zoom: int,
        w: int,
        h: int,
        caption: types.PageCaption,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneCallDiscardReasonMissed(TLObject):
    """
    [Read `phoneCallDiscardReasonMissed` docs](https://core.telegram.org/constructor/phoneCallDiscardReasonMissed).

    Generated from the following TL definition:
    ```tl
    phoneCallDiscardReasonMissed#85e42301 = PhoneCallDiscardReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneCallDiscardReasonDisconnect(TLObject):
    """
    [Read `phoneCallDiscardReasonDisconnect` docs](https://core.telegram.org/constructor/phoneCallDiscardReasonDisconnect).

    Generated from the following TL definition:
    ```tl
    phoneCallDiscardReasonDisconnect#e095c1a0 = PhoneCallDiscardReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneCallDiscardReasonHangup(TLObject):
    """
    [Read `phoneCallDiscardReasonHangup` docs](https://core.telegram.org/constructor/phoneCallDiscardReasonHangup).

    Generated from the following TL definition:
    ```tl
    phoneCallDiscardReasonHangup#57adc690 = PhoneCallDiscardReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneCallDiscardReasonBusy(TLObject):
    """
    [Read `phoneCallDiscardReasonBusy` docs](https://core.telegram.org/constructor/phoneCallDiscardReasonBusy).

    Generated from the following TL definition:
    ```tl
    phoneCallDiscardReasonBusy#faf7e8c9 = PhoneCallDiscardReason
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneCallDiscardReasonMigrateConferenceCall(TLObject):
    """
    [Read `phoneCallDiscardReasonMigrateConferenceCall` docs](https://core.telegram.org/constructor/phoneCallDiscardReasonMigrateConferenceCall).

    Generated from the following TL definition:
    ```tl
    phoneCallDiscardReasonMigrateConferenceCall#9fbbf1f7 slug:string = PhoneCallDiscardReason
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DataJson(TLObject):
    """
    [Read `dataJSON` docs](https://core.telegram.org/constructor/dataJSON).

    Generated from the following TL definition:
    ```tl
    dataJSON#7d748d04 data:string = DataJSON
    ```
    """
    def __new__(
        cls,
        data: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LabeledPrice(TLObject):
    """
    [Read `labeledPrice` docs](https://core.telegram.org/constructor/labeledPrice).

    Generated from the following TL definition:
    ```tl
    labeledPrice#cb296bf8 label:string amount:long = LabeledPrice
    ```
    """
    def __new__(
        cls,
        label: str,
        amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Invoice(TLObject):
    """
    [Read `invoice` docs](https://core.telegram.org/constructor/invoice).

    Generated from the following TL definition:
    ```tl
    invoice#49ee584 flags:# test:flags.0?true name_requested:flags.1?true phone_requested:flags.2?true email_requested:flags.3?true shipping_address_requested:flags.4?true flexible:flags.5?true phone_to_provider:flags.6?true email_to_provider:flags.7?true recurring:flags.9?true currency:string prices:Vector<LabeledPrice> max_tip_amount:flags.8?long suggested_tip_amounts:flags.8?Vector<long> terms_url:flags.10?string subscription_period:flags.11?int = Invoice
    ```
    """
    def __new__(
        cls,
        test: bool,
        name_requested: bool,
        phone_requested: bool,
        email_requested: bool,
        shipping_address_requested: bool,
        flexible: bool,
        phone_to_provider: bool,
        email_to_provider: bool,
        recurring: bool,
        currency: str,
        prices: Sequence[types.LabeledPrice],
        max_tip_amount: Optional[int],
        suggested_tip_amounts: Optional[Sequence[int]],
        terms_url: Optional[str],
        subscription_period: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaymentCharge(TLObject):
    """
    [Read `paymentCharge` docs](https://core.telegram.org/constructor/paymentCharge).

    Generated from the following TL definition:
    ```tl
    paymentCharge#ea02c27e id:string provider_charge_id:string = PaymentCharge
    ```
    """
    def __new__(
        cls,
        id: str,
        provider_charge_id: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PostAddress(TLObject):
    """
    [Read `postAddress` docs](https://core.telegram.org/constructor/postAddress).

    Generated from the following TL definition:
    ```tl
    postAddress#1e8caaeb street_line1:string street_line2:string city:string state:string country_iso2:string post_code:string = PostAddress
    ```
    """
    def __new__(
        cls,
        street_line1: str,
        street_line2: str,
        city: str,
        state: str,
        country_iso2: str,
        post_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaymentRequestedInfo(TLObject):
    """
    [Read `paymentRequestedInfo` docs](https://core.telegram.org/constructor/paymentRequestedInfo).

    Generated from the following TL definition:
    ```tl
    paymentRequestedInfo#909c3f94 flags:# name:flags.0?string phone:flags.1?string email:flags.2?string shipping_address:flags.3?PostAddress = PaymentRequestedInfo
    ```
    """
    def __new__(
        cls,
        name: Optional[str],
        phone: Optional[str],
        email: Optional[str],
        shipping_address: Optional[types.PostAddress],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaymentSavedCredentialsCard(TLObject):
    """
    [Read `paymentSavedCredentialsCard` docs](https://core.telegram.org/constructor/paymentSavedCredentialsCard).

    Generated from the following TL definition:
    ```tl
    paymentSavedCredentialsCard#cdc27a1f id:string title:string = PaymentSavedCredentials
    ```
    """
    def __new__(
        cls,
        id: str,
        title: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebDocument(TLObject):
    """
    [Read `webDocument` docs](https://core.telegram.org/constructor/webDocument).

    Generated from the following TL definition:
    ```tl
    webDocument#1c570ed1 url:string access_hash:long size:int mime_type:string attributes:Vector<DocumentAttribute> = WebDocument
    ```
    """
    def __new__(
        cls,
        url: str,
        access_hash: int,
        size: int,
        mime_type: str,
        attributes: Sequence[types.DocumentAttributeImageSize | types.DocumentAttributeAnimated | types.DocumentAttributeSticker | types.DocumentAttributeVideo | types.DocumentAttributeAudio | types.DocumentAttributeFilename | types.DocumentAttributeHasStickers | types.DocumentAttributeCustomEmoji],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebDocumentNoProxy(TLObject):
    """
    [Read `webDocumentNoProxy` docs](https://core.telegram.org/constructor/webDocumentNoProxy).

    Generated from the following TL definition:
    ```tl
    webDocumentNoProxy#f9c8bcc6 url:string size:int mime_type:string attributes:Vector<DocumentAttribute> = WebDocument
    ```
    """
    def __new__(
        cls,
        url: str,
        size: int,
        mime_type: str,
        attributes: Sequence[types.DocumentAttributeImageSize | types.DocumentAttributeAnimated | types.DocumentAttributeSticker | types.DocumentAttributeVideo | types.DocumentAttributeAudio | types.DocumentAttributeFilename | types.DocumentAttributeHasStickers | types.DocumentAttributeCustomEmoji],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputWebDocument(TLObject):
    """
    [Read `inputWebDocument` docs](https://core.telegram.org/constructor/inputWebDocument).

    Generated from the following TL definition:
    ```tl
    inputWebDocument#9bed434d url:string size:int mime_type:string attributes:Vector<DocumentAttribute> = InputWebDocument
    ```
    """
    def __new__(
        cls,
        url: str,
        size: int,
        mime_type: str,
        attributes: Sequence[types.DocumentAttributeImageSize | types.DocumentAttributeAnimated | types.DocumentAttributeSticker | types.DocumentAttributeVideo | types.DocumentAttributeAudio | types.DocumentAttributeFilename | types.DocumentAttributeHasStickers | types.DocumentAttributeCustomEmoji],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputWebFileLocation(TLObject):
    """
    [Read `inputWebFileLocation` docs](https://core.telegram.org/constructor/inputWebFileLocation).

    Generated from the following TL definition:
    ```tl
    inputWebFileLocation#c239d686 url:string access_hash:long = InputWebFileLocation
    ```
    """
    def __new__(
        cls,
        url: str,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputWebFileGeoPointLocation(TLObject):
    """
    [Read `inputWebFileGeoPointLocation` docs](https://core.telegram.org/constructor/inputWebFileGeoPointLocation).

    Generated from the following TL definition:
    ```tl
    inputWebFileGeoPointLocation#9f2221c9 geo_point:InputGeoPoint access_hash:long w:int h:int zoom:int scale:int = InputWebFileLocation
    ```
    """
    def __new__(
        cls,
        geo_point: types.InputGeoPointEmpty | types.InputGeoPoint,
        access_hash: int,
        w: int,
        h: int,
        zoom: int,
        scale: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputWebFileAudioAlbumThumbLocation(TLObject):
    """
    [Read `inputWebFileAudioAlbumThumbLocation` docs](https://core.telegram.org/constructor/inputWebFileAudioAlbumThumbLocation).

    Generated from the following TL definition:
    ```tl
    inputWebFileAudioAlbumThumbLocation#f46fe924 flags:# small:flags.2?true document:flags.0?InputDocument title:flags.1?string performer:flags.1?string = InputWebFileLocation
    ```
    """
    def __new__(
        cls,
        small: bool,
        document: Optional[types.InputDocumentEmpty | types.InputDocument],
        title: Optional[str],
        performer: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPaymentCredentialsSaved(TLObject):
    """
    [Read `inputPaymentCredentialsSaved` docs](https://core.telegram.org/constructor/inputPaymentCredentialsSaved).

    Generated from the following TL definition:
    ```tl
    inputPaymentCredentialsSaved#c10eb2cf id:string tmp_password:bytes = InputPaymentCredentials
    ```
    """
    def __new__(
        cls,
        id: str,
        tmp_password: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPaymentCredentials(TLObject):
    """
    [Read `inputPaymentCredentials` docs](https://core.telegram.org/constructor/inputPaymentCredentials).

    Generated from the following TL definition:
    ```tl
    inputPaymentCredentials#3417d728 flags:# save:flags.0?true data:DataJSON = InputPaymentCredentials
    ```
    """
    def __new__(
        cls,
        save: bool,
        data: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPaymentCredentialsApplePay(TLObject):
    """
    [Read `inputPaymentCredentialsApplePay` docs](https://core.telegram.org/constructor/inputPaymentCredentialsApplePay).

    Generated from the following TL definition:
    ```tl
    inputPaymentCredentialsApplePay#aa1c39f payment_data:DataJSON = InputPaymentCredentials
    ```
    """
    def __new__(
        cls,
        payment_data: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPaymentCredentialsGooglePay(TLObject):
    """
    [Read `inputPaymentCredentialsGooglePay` docs](https://core.telegram.org/constructor/inputPaymentCredentialsGooglePay).

    Generated from the following TL definition:
    ```tl
    inputPaymentCredentialsGooglePay#8ac32801 payment_token:DataJSON = InputPaymentCredentials
    ```
    """
    def __new__(
        cls,
        payment_token: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ShippingOption(TLObject):
    """
    [Read `shippingOption` docs](https://core.telegram.org/constructor/shippingOption).

    Generated from the following TL definition:
    ```tl
    shippingOption#b6213cdf id:string title:string prices:Vector<LabeledPrice> = ShippingOption
    ```
    """
    def __new__(
        cls,
        id: str,
        title: str,
        prices: Sequence[types.LabeledPrice],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStickerSetItem(TLObject):
    """
    [Read `inputStickerSetItem` docs](https://core.telegram.org/constructor/inputStickerSetItem).

    Generated from the following TL definition:
    ```tl
    inputStickerSetItem#32da9e9c flags:# document:InputDocument emoji:string mask_coords:flags.0?MaskCoords keywords:flags.1?string = InputStickerSetItem
    ```
    """
    def __new__(
        cls,
        document: types.InputDocumentEmpty | types.InputDocument,
        emoji: str,
        mask_coords: Optional[types.MaskCoords],
        keywords: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPhoneCall(TLObject):
    """
    [Read `inputPhoneCall` docs](https://core.telegram.org/constructor/inputPhoneCall).

    Generated from the following TL definition:
    ```tl
    inputPhoneCall#1e36fded id:long access_hash:long = InputPhoneCall
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneCallEmpty(TLObject):
    """
    [Read `phoneCallEmpty` docs](https://core.telegram.org/constructor/phoneCallEmpty).

    Generated from the following TL definition:
    ```tl
    phoneCallEmpty#5366c915 id:long = PhoneCall
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneCallWaiting(TLObject):
    """
    [Read `phoneCallWaiting` docs](https://core.telegram.org/constructor/phoneCallWaiting).

    Generated from the following TL definition:
    ```tl
    phoneCallWaiting#c5226f17 flags:# video:flags.6?true id:long access_hash:long date:int admin_id:long participant_id:long protocol:PhoneCallProtocol receive_date:flags.0?int = PhoneCall
    ```
    """
    def __new__(
        cls,
        video: bool,
        id: int,
        access_hash: int,
        date: int,
        admin_id: int,
        participant_id: int,
        protocol: types.PhoneCallProtocol,
        receive_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneCallRequested(TLObject):
    """
    [Read `phoneCallRequested` docs](https://core.telegram.org/constructor/phoneCallRequested).

    Generated from the following TL definition:
    ```tl
    phoneCallRequested#14b0ed0c flags:# video:flags.6?true id:long access_hash:long date:int admin_id:long participant_id:long g_a_hash:bytes protocol:PhoneCallProtocol = PhoneCall
    ```
    """
    def __new__(
        cls,
        video: bool,
        id: int,
        access_hash: int,
        date: int,
        admin_id: int,
        participant_id: int,
        g_a_hash: bytes,
        protocol: types.PhoneCallProtocol,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneCallAccepted(TLObject):
    """
    [Read `phoneCallAccepted` docs](https://core.telegram.org/constructor/phoneCallAccepted).

    Generated from the following TL definition:
    ```tl
    phoneCallAccepted#3660c311 flags:# video:flags.6?true id:long access_hash:long date:int admin_id:long participant_id:long g_b:bytes protocol:PhoneCallProtocol = PhoneCall
    ```
    """
    def __new__(
        cls,
        video: bool,
        id: int,
        access_hash: int,
        date: int,
        admin_id: int,
        participant_id: int,
        g_b: bytes,
        protocol: types.PhoneCallProtocol,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneCall(TLObject):
    """
    [Read `phoneCall` docs](https://core.telegram.org/constructor/phoneCall).

    Generated from the following TL definition:
    ```tl
    phoneCall#30535af5 flags:# p2p_allowed:flags.5?true video:flags.6?true conference_supported:flags.8?true id:long access_hash:long date:int admin_id:long participant_id:long g_a_or_b:bytes key_fingerprint:long protocol:PhoneCallProtocol connections:Vector<PhoneConnection> start_date:int custom_parameters:flags.7?DataJSON = PhoneCall
    ```
    """
    def __new__(
        cls,
        p2p_allowed: bool,
        video: bool,
        conference_supported: bool,
        id: int,
        access_hash: int,
        date: int,
        admin_id: int,
        participant_id: int,
        g_a_or_b: bytes,
        key_fingerprint: int,
        protocol: types.PhoneCallProtocol,
        connections: Sequence[types.PhoneConnection | types.PhoneConnectionWebrtc],
        start_date: int,
        custom_parameters: Optional[types.DataJson],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneCallDiscarded(TLObject):
    """
    [Read `phoneCallDiscarded` docs](https://core.telegram.org/constructor/phoneCallDiscarded).

    Generated from the following TL definition:
    ```tl
    phoneCallDiscarded#50ca4de1 flags:# need_rating:flags.2?true need_debug:flags.3?true video:flags.6?true id:long reason:flags.0?PhoneCallDiscardReason duration:flags.1?int = PhoneCall
    ```
    """
    def __new__(
        cls,
        need_rating: bool,
        need_debug: bool,
        video: bool,
        id: int,
        reason: Optional[types.PhoneCallDiscardReasonMissed | types.PhoneCallDiscardReasonDisconnect | types.PhoneCallDiscardReasonHangup | types.PhoneCallDiscardReasonBusy | types.PhoneCallDiscardReasonMigrateConferenceCall],
        duration: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneConnection(TLObject):
    """
    [Read `phoneConnection` docs](https://core.telegram.org/constructor/phoneConnection).

    Generated from the following TL definition:
    ```tl
    phoneConnection#9cc123c7 flags:# tcp:flags.0?true id:long ip:string ipv6:string port:int peer_tag:bytes = PhoneConnection
    ```
    """
    def __new__(
        cls,
        tcp: bool,
        id: int,
        ip: str,
        ipv6: str,
        port: int,
        peer_tag: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneConnectionWebrtc(TLObject):
    """
    [Read `phoneConnectionWebrtc` docs](https://core.telegram.org/constructor/phoneConnectionWebrtc).

    Generated from the following TL definition:
    ```tl
    phoneConnectionWebrtc#635fe375 flags:# turn:flags.0?true stun:flags.1?true id:long ip:string ipv6:string port:int username:string password:string = PhoneConnection
    ```
    """
    def __new__(
        cls,
        turn: bool,
        stun: bool,
        id: int,
        ip: str,
        ipv6: str,
        port: int,
        username: str,
        password: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhoneCallProtocol(TLObject):
    """
    [Read `phoneCallProtocol` docs](https://core.telegram.org/constructor/phoneCallProtocol).

    Generated from the following TL definition:
    ```tl
    phoneCallProtocol#fc878fc8 flags:# udp_p2p:flags.0?true udp_reflector:flags.1?true min_layer:int max_layer:int library_versions:Vector<string> = PhoneCallProtocol
    ```
    """
    def __new__(
        cls,
        udp_p2p: bool,
        udp_reflector: bool,
        min_layer: int,
        max_layer: int,
        library_versions: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CdnPublicKey(TLObject):
    """
    [Read `cdnPublicKey` docs](https://core.telegram.org/constructor/cdnPublicKey).

    Generated from the following TL definition:
    ```tl
    cdnPublicKey#c982eaba dc_id:int public_key:string = CdnPublicKey
    ```
    """
    def __new__(
        cls,
        dc_id: int,
        public_key: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CdnConfig(TLObject):
    """
    [Read `cdnConfig` docs](https://core.telegram.org/constructor/cdnConfig).

    Generated from the following TL definition:
    ```tl
    cdnConfig#5725e40a public_keys:Vector<CdnPublicKey> = CdnConfig
    ```
    """
    def __new__(
        cls,
        public_keys: Sequence[types.CdnPublicKey],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LangPackString(TLObject):
    """
    [Read `langPackString` docs](https://core.telegram.org/constructor/langPackString).

    Generated from the following TL definition:
    ```tl
    langPackString#cad181f6 key:string value:string = LangPackString
    ```
    """
    def __new__(
        cls,
        key: str,
        value: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LangPackStringPluralized(TLObject):
    """
    [Read `langPackStringPluralized` docs](https://core.telegram.org/constructor/langPackStringPluralized).

    Generated from the following TL definition:
    ```tl
    langPackStringPluralized#6c47ac9f flags:# key:string zero_value:flags.0?string one_value:flags.1?string two_value:flags.2?string few_value:flags.3?string many_value:flags.4?string other_value:string = LangPackString
    ```
    """
    def __new__(
        cls,
        key: str,
        zero_value: Optional[str],
        one_value: Optional[str],
        two_value: Optional[str],
        few_value: Optional[str],
        many_value: Optional[str],
        other_value: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LangPackStringDeleted(TLObject):
    """
    [Read `langPackStringDeleted` docs](https://core.telegram.org/constructor/langPackStringDeleted).

    Generated from the following TL definition:
    ```tl
    langPackStringDeleted#2979eeb2 key:string = LangPackString
    ```
    """
    def __new__(
        cls,
        key: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LangPackDifference(TLObject):
    """
    [Read `langPackDifference` docs](https://core.telegram.org/constructor/langPackDifference).

    Generated from the following TL definition:
    ```tl
    langPackDifference#f385c1f6 lang_code:string from_version:int version:int strings:Vector<LangPackString> = LangPackDifference
    ```
    """
    def __new__(
        cls,
        lang_code: str,
        from_version: int,
        version: int,
        strings: Sequence[types.LangPackString | types.LangPackStringPluralized | types.LangPackStringDeleted],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LangPackLanguage(TLObject):
    """
    [Read `langPackLanguage` docs](https://core.telegram.org/constructor/langPackLanguage).

    Generated from the following TL definition:
    ```tl
    langPackLanguage#eeca5ce3 flags:# official:flags.0?true rtl:flags.2?true beta:flags.3?true name:string native_name:string lang_code:string base_lang_code:flags.1?string plural_code:string strings_count:int translated_count:int translations_url:string = LangPackLanguage
    ```
    """
    def __new__(
        cls,
        official: bool,
        rtl: bool,
        beta: bool,
        name: str,
        native_name: str,
        lang_code: str,
        base_lang_code: Optional[str],
        plural_code: str,
        strings_count: int,
        translated_count: int,
        translations_url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeTitle(TLObject):
    """
    [Read `channelAdminLogEventActionChangeTitle` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeTitle).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeTitle#e6dfb825 prev_value:string new_value:string = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: str,
        new_value: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeAbout(TLObject):
    """
    [Read `channelAdminLogEventActionChangeAbout` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeAbout).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeAbout#55188a2e prev_value:string new_value:string = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: str,
        new_value: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeUsername(TLObject):
    """
    [Read `channelAdminLogEventActionChangeUsername` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeUsername).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeUsername#6a4afc38 prev_value:string new_value:string = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: str,
        new_value: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangePhoto(TLObject):
    """
    [Read `channelAdminLogEventActionChangePhoto` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangePhoto).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangePhoto#434bd2af prev_photo:Photo new_photo:Photo = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_photo: types.PhotoEmpty | types.Photo,
        new_photo: types.PhotoEmpty | types.Photo,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionToggleInvites(TLObject):
    """
    [Read `channelAdminLogEventActionToggleInvites` docs](https://core.telegram.org/constructor/channelAdminLogEventActionToggleInvites).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionToggleInvites#1b7907ae new_value:Bool = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        new_value: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionToggleSignatures(TLObject):
    """
    [Read `channelAdminLogEventActionToggleSignatures` docs](https://core.telegram.org/constructor/channelAdminLogEventActionToggleSignatures).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionToggleSignatures#26ae0971 new_value:Bool = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        new_value: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionUpdatePinned(TLObject):
    """
    [Read `channelAdminLogEventActionUpdatePinned` docs](https://core.telegram.org/constructor/channelAdminLogEventActionUpdatePinned).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionUpdatePinned#e9e82c18 message:Message = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        message: types.MessageEmpty | types.Message | types.MessageService,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionEditMessage(TLObject):
    """
    [Read `channelAdminLogEventActionEditMessage` docs](https://core.telegram.org/constructor/channelAdminLogEventActionEditMessage).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionEditMessage#709b2405 prev_message:Message new_message:Message = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_message: types.MessageEmpty | types.Message | types.MessageService,
        new_message: types.MessageEmpty | types.Message | types.MessageService,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionDeleteMessage(TLObject):
    """
    [Read `channelAdminLogEventActionDeleteMessage` docs](https://core.telegram.org/constructor/channelAdminLogEventActionDeleteMessage).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionDeleteMessage#42e047bb message:Message = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        message: types.MessageEmpty | types.Message | types.MessageService,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionParticipantJoin(TLObject):
    """
    [Read `channelAdminLogEventActionParticipantJoin` docs](https://core.telegram.org/constructor/channelAdminLogEventActionParticipantJoin).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionParticipantJoin#183040d3 = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionParticipantLeave(TLObject):
    """
    [Read `channelAdminLogEventActionParticipantLeave` docs](https://core.telegram.org/constructor/channelAdminLogEventActionParticipantLeave).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionParticipantLeave#f89777f2 = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionParticipantInvite(TLObject):
    """
    [Read `channelAdminLogEventActionParticipantInvite` docs](https://core.telegram.org/constructor/channelAdminLogEventActionParticipantInvite).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionParticipantInvite#e31c34d8 participant:ChannelParticipant = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        participant: types.ChannelParticipant | types.ChannelParticipantSelf | types.ChannelParticipantCreator | types.ChannelParticipantAdmin | types.ChannelParticipantBanned | types.ChannelParticipantLeft,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionParticipantToggleBan(TLObject):
    """
    [Read `channelAdminLogEventActionParticipantToggleBan` docs](https://core.telegram.org/constructor/channelAdminLogEventActionParticipantToggleBan).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionParticipantToggleBan#e6d83d7e prev_participant:ChannelParticipant new_participant:ChannelParticipant = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_participant: types.ChannelParticipant | types.ChannelParticipantSelf | types.ChannelParticipantCreator | types.ChannelParticipantAdmin | types.ChannelParticipantBanned | types.ChannelParticipantLeft,
        new_participant: types.ChannelParticipant | types.ChannelParticipantSelf | types.ChannelParticipantCreator | types.ChannelParticipantAdmin | types.ChannelParticipantBanned | types.ChannelParticipantLeft,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionParticipantToggleAdmin(TLObject):
    """
    [Read `channelAdminLogEventActionParticipantToggleAdmin` docs](https://core.telegram.org/constructor/channelAdminLogEventActionParticipantToggleAdmin).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionParticipantToggleAdmin#d5676710 prev_participant:ChannelParticipant new_participant:ChannelParticipant = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_participant: types.ChannelParticipant | types.ChannelParticipantSelf | types.ChannelParticipantCreator | types.ChannelParticipantAdmin | types.ChannelParticipantBanned | types.ChannelParticipantLeft,
        new_participant: types.ChannelParticipant | types.ChannelParticipantSelf | types.ChannelParticipantCreator | types.ChannelParticipantAdmin | types.ChannelParticipantBanned | types.ChannelParticipantLeft,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeStickerSet(TLObject):
    """
    [Read `channelAdminLogEventActionChangeStickerSet` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeStickerSet).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeStickerSet#b1c3caa7 prev_stickerset:InputStickerSet new_stickerset:InputStickerSet = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
        new_stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionTogglePreHistoryHidden(TLObject):
    """
    [Read `channelAdminLogEventActionTogglePreHistoryHidden` docs](https://core.telegram.org/constructor/channelAdminLogEventActionTogglePreHistoryHidden).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionTogglePreHistoryHidden#5f5c95f1 new_value:Bool = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        new_value: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionDefaultBannedRights(TLObject):
    """
    [Read `channelAdminLogEventActionDefaultBannedRights` docs](https://core.telegram.org/constructor/channelAdminLogEventActionDefaultBannedRights).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionDefaultBannedRights#2df5fc0a prev_banned_rights:ChatBannedRights new_banned_rights:ChatBannedRights = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_banned_rights: types.ChatBannedRights,
        new_banned_rights: types.ChatBannedRights,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionStopPoll(TLObject):
    """
    [Read `channelAdminLogEventActionStopPoll` docs](https://core.telegram.org/constructor/channelAdminLogEventActionStopPoll).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionStopPoll#8f079643 message:Message = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        message: types.MessageEmpty | types.Message | types.MessageService,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeLinkedChat(TLObject):
    """
    [Read `channelAdminLogEventActionChangeLinkedChat` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeLinkedChat).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeLinkedChat#50c7ac8 prev_value:long new_value:long = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: int,
        new_value: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeLocation(TLObject):
    """
    [Read `channelAdminLogEventActionChangeLocation` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeLocation).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeLocation#e6b76ae prev_value:ChannelLocation new_value:ChannelLocation = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: types.ChannelLocationEmpty | types.ChannelLocation,
        new_value: types.ChannelLocationEmpty | types.ChannelLocation,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionToggleSlowMode(TLObject):
    """
    [Read `channelAdminLogEventActionToggleSlowMode` docs](https://core.telegram.org/constructor/channelAdminLogEventActionToggleSlowMode).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionToggleSlowMode#53909779 prev_value:int new_value:int = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: int,
        new_value: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionStartGroupCall(TLObject):
    """
    [Read `channelAdminLogEventActionStartGroupCall` docs](https://core.telegram.org/constructor/channelAdminLogEventActionStartGroupCall).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionStartGroupCall#23209745 call:InputGroupCall = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionDiscardGroupCall(TLObject):
    """
    [Read `channelAdminLogEventActionDiscardGroupCall` docs](https://core.telegram.org/constructor/channelAdminLogEventActionDiscardGroupCall).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionDiscardGroupCall#db9f9140 call:InputGroupCall = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        call: types.InputGroupCall | types.InputGroupCallSlug | types.InputGroupCallInviteMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionParticipantMute(TLObject):
    """
    [Read `channelAdminLogEventActionParticipantMute` docs](https://core.telegram.org/constructor/channelAdminLogEventActionParticipantMute).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionParticipantMute#f92424d2 participant:GroupCallParticipant = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        participant: types.GroupCallParticipant,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionParticipantUnmute(TLObject):
    """
    [Read `channelAdminLogEventActionParticipantUnmute` docs](https://core.telegram.org/constructor/channelAdminLogEventActionParticipantUnmute).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionParticipantUnmute#e64429c0 participant:GroupCallParticipant = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        participant: types.GroupCallParticipant,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionToggleGroupCallSetting(TLObject):
    """
    [Read `channelAdminLogEventActionToggleGroupCallSetting` docs](https://core.telegram.org/constructor/channelAdminLogEventActionToggleGroupCallSetting).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionToggleGroupCallSetting#56d6a247 join_muted:Bool = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        join_muted: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionParticipantJoinByInvite(TLObject):
    """
    [Read `channelAdminLogEventActionParticipantJoinByInvite` docs](https://core.telegram.org/constructor/channelAdminLogEventActionParticipantJoinByInvite).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionParticipantJoinByInvite#fe9fc158 flags:# via_chatlist:flags.0?true invite:ExportedChatInvite = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        via_chatlist: bool,
        invite: types.ChatInviteExported | types.ChatInvitePublicJoinRequests,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionExportedInviteDelete(TLObject):
    """
    [Read `channelAdminLogEventActionExportedInviteDelete` docs](https://core.telegram.org/constructor/channelAdminLogEventActionExportedInviteDelete).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionExportedInviteDelete#5a50fca4 invite:ExportedChatInvite = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        invite: types.ChatInviteExported | types.ChatInvitePublicJoinRequests,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionExportedInviteRevoke(TLObject):
    """
    [Read `channelAdminLogEventActionExportedInviteRevoke` docs](https://core.telegram.org/constructor/channelAdminLogEventActionExportedInviteRevoke).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionExportedInviteRevoke#410a134e invite:ExportedChatInvite = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        invite: types.ChatInviteExported | types.ChatInvitePublicJoinRequests,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionExportedInviteEdit(TLObject):
    """
    [Read `channelAdminLogEventActionExportedInviteEdit` docs](https://core.telegram.org/constructor/channelAdminLogEventActionExportedInviteEdit).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionExportedInviteEdit#e90ebb59 prev_invite:ExportedChatInvite new_invite:ExportedChatInvite = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_invite: types.ChatInviteExported | types.ChatInvitePublicJoinRequests,
        new_invite: types.ChatInviteExported | types.ChatInvitePublicJoinRequests,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionParticipantVolume(TLObject):
    """
    [Read `channelAdminLogEventActionParticipantVolume` docs](https://core.telegram.org/constructor/channelAdminLogEventActionParticipantVolume).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionParticipantVolume#3e7f6847 participant:GroupCallParticipant = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        participant: types.GroupCallParticipant,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeHistoryTtl(TLObject):
    """
    [Read `channelAdminLogEventActionChangeHistoryTTL` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeHistoryTTL).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeHistoryTTL#6e941a38 prev_value:int new_value:int = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: int,
        new_value: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionParticipantJoinByRequest(TLObject):
    """
    [Read `channelAdminLogEventActionParticipantJoinByRequest` docs](https://core.telegram.org/constructor/channelAdminLogEventActionParticipantJoinByRequest).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionParticipantJoinByRequest#afb6144a invite:ExportedChatInvite approved_by:long = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        invite: types.ChatInviteExported | types.ChatInvitePublicJoinRequests,
        approved_by: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionToggleNoForwards(TLObject):
    """
    [Read `channelAdminLogEventActionToggleNoForwards` docs](https://core.telegram.org/constructor/channelAdminLogEventActionToggleNoForwards).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionToggleNoForwards#cb2ac766 new_value:Bool = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        new_value: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionSendMessage(TLObject):
    """
    [Read `channelAdminLogEventActionSendMessage` docs](https://core.telegram.org/constructor/channelAdminLogEventActionSendMessage).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionSendMessage#278f2868 message:Message = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        message: types.MessageEmpty | types.Message | types.MessageService,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeAvailableReactions(TLObject):
    """
    [Read `channelAdminLogEventActionChangeAvailableReactions` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeAvailableReactions).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeAvailableReactions#be4e0ef8 prev_value:ChatReactions new_value:ChatReactions = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: types.ChatReactionsNone | types.ChatReactionsAll | types.ChatReactionsSome,
        new_value: types.ChatReactionsNone | types.ChatReactionsAll | types.ChatReactionsSome,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeUsernames(TLObject):
    """
    [Read `channelAdminLogEventActionChangeUsernames` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeUsernames).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeUsernames#f04fb3a9 prev_value:Vector<string> new_value:Vector<string> = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: Sequence[str],
        new_value: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionToggleForum(TLObject):
    """
    [Read `channelAdminLogEventActionToggleForum` docs](https://core.telegram.org/constructor/channelAdminLogEventActionToggleForum).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionToggleForum#2cc6383 new_value:Bool = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        new_value: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionCreateTopic(TLObject):
    """
    [Read `channelAdminLogEventActionCreateTopic` docs](https://core.telegram.org/constructor/channelAdminLogEventActionCreateTopic).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionCreateTopic#58707d28 topic:ForumTopic = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        topic: types.ForumTopicDeleted | types.ForumTopic,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionEditTopic(TLObject):
    """
    [Read `channelAdminLogEventActionEditTopic` docs](https://core.telegram.org/constructor/channelAdminLogEventActionEditTopic).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionEditTopic#f06fe208 prev_topic:ForumTopic new_topic:ForumTopic = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_topic: types.ForumTopicDeleted | types.ForumTopic,
        new_topic: types.ForumTopicDeleted | types.ForumTopic,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionDeleteTopic(TLObject):
    """
    [Read `channelAdminLogEventActionDeleteTopic` docs](https://core.telegram.org/constructor/channelAdminLogEventActionDeleteTopic).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionDeleteTopic#ae168909 topic:ForumTopic = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        topic: types.ForumTopicDeleted | types.ForumTopic,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionPinTopic(TLObject):
    """
    [Read `channelAdminLogEventActionPinTopic` docs](https://core.telegram.org/constructor/channelAdminLogEventActionPinTopic).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionPinTopic#5d8d353b flags:# prev_topic:flags.0?ForumTopic new_topic:flags.1?ForumTopic = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_topic: Optional[types.ForumTopicDeleted | types.ForumTopic],
        new_topic: Optional[types.ForumTopicDeleted | types.ForumTopic],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionToggleAntiSpam(TLObject):
    """
    [Read `channelAdminLogEventActionToggleAntiSpam` docs](https://core.telegram.org/constructor/channelAdminLogEventActionToggleAntiSpam).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionToggleAntiSpam#64f36dfc new_value:Bool = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        new_value: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangePeerColor(TLObject):
    """
    [Read `channelAdminLogEventActionChangePeerColor` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangePeerColor).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangePeerColor#5796e780 prev_value:PeerColor new_value:PeerColor = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: types.PeerColor | types.PeerColorCollectible | types.InputPeerColorCollectible,
        new_value: types.PeerColor | types.PeerColorCollectible | types.InputPeerColorCollectible,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeProfilePeerColor(TLObject):
    """
    [Read `channelAdminLogEventActionChangeProfilePeerColor` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeProfilePeerColor).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeProfilePeerColor#5e477b25 prev_value:PeerColor new_value:PeerColor = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: types.PeerColor | types.PeerColorCollectible | types.InputPeerColorCollectible,
        new_value: types.PeerColor | types.PeerColorCollectible | types.InputPeerColorCollectible,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeWallpaper(TLObject):
    """
    [Read `channelAdminLogEventActionChangeWallpaper` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeWallpaper).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeWallpaper#31bb5d52 prev_value:WallPaper new_value:WallPaper = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: types.WallPaper | types.WallPaperNoFile,
        new_value: types.WallPaper | types.WallPaperNoFile,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeEmojiStatus(TLObject):
    """
    [Read `channelAdminLogEventActionChangeEmojiStatus` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeEmojiStatus).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeEmojiStatus#3ea9feb1 prev_value:EmojiStatus new_value:EmojiStatus = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_value: types.EmojiStatusEmpty | types.EmojiStatus | types.EmojiStatusCollectible | types.InputEmojiStatusCollectible,
        new_value: types.EmojiStatusEmpty | types.EmojiStatus | types.EmojiStatusCollectible | types.InputEmojiStatusCollectible,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionChangeEmojiStickerSet(TLObject):
    """
    [Read `channelAdminLogEventActionChangeEmojiStickerSet` docs](https://core.telegram.org/constructor/channelAdminLogEventActionChangeEmojiStickerSet).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionChangeEmojiStickerSet#46d840ab prev_stickerset:InputStickerSet new_stickerset:InputStickerSet = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
        new_stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionToggleSignatureProfiles(TLObject):
    """
    [Read `channelAdminLogEventActionToggleSignatureProfiles` docs](https://core.telegram.org/constructor/channelAdminLogEventActionToggleSignatureProfiles).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionToggleSignatureProfiles#60a79c79 new_value:Bool = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        new_value: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionParticipantSubExtend(TLObject):
    """
    [Read `channelAdminLogEventActionParticipantSubExtend` docs](https://core.telegram.org/constructor/channelAdminLogEventActionParticipantSubExtend).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionParticipantSubExtend#64642db3 prev_participant:ChannelParticipant new_participant:ChannelParticipant = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        prev_participant: types.ChannelParticipant | types.ChannelParticipantSelf | types.ChannelParticipantCreator | types.ChannelParticipantAdmin | types.ChannelParticipantBanned | types.ChannelParticipantLeft,
        new_participant: types.ChannelParticipant | types.ChannelParticipantSelf | types.ChannelParticipantCreator | types.ChannelParticipantAdmin | types.ChannelParticipantBanned | types.ChannelParticipantLeft,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventActionToggleAutotranslation(TLObject):
    """
    [Read `channelAdminLogEventActionToggleAutotranslation` docs](https://core.telegram.org/constructor/channelAdminLogEventActionToggleAutotranslation).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventActionToggleAutotranslation#c517f77e new_value:Bool = ChannelAdminLogEventAction
    ```
    """
    def __new__(
        cls,
        new_value: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEvent(TLObject):
    """
    [Read `channelAdminLogEvent` docs](https://core.telegram.org/constructor/channelAdminLogEvent).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEvent#1fad68cd id:long date:int user_id:long action:ChannelAdminLogEventAction = ChannelAdminLogEvent
    ```
    """
    def __new__(
        cls,
        id: int,
        date: int,
        user_id: int,
        action: types.ChannelAdminLogEventActionChangeTitle | types.ChannelAdminLogEventActionChangeAbout | types.ChannelAdminLogEventActionChangeUsername | types.ChannelAdminLogEventActionChangePhoto | types.ChannelAdminLogEventActionToggleInvites | types.ChannelAdminLogEventActionToggleSignatures | types.ChannelAdminLogEventActionUpdatePinned | types.ChannelAdminLogEventActionEditMessage | types.ChannelAdminLogEventActionDeleteMessage | types.ChannelAdminLogEventActionParticipantJoin | types.ChannelAdminLogEventActionParticipantLeave | types.ChannelAdminLogEventActionParticipantInvite | types.ChannelAdminLogEventActionParticipantToggleBan | types.ChannelAdminLogEventActionParticipantToggleAdmin | types.ChannelAdminLogEventActionChangeStickerSet | types.ChannelAdminLogEventActionTogglePreHistoryHidden | types.ChannelAdminLogEventActionDefaultBannedRights | types.ChannelAdminLogEventActionStopPoll | types.ChannelAdminLogEventActionChangeLinkedChat | types.ChannelAdminLogEventActionChangeLocation | types.ChannelAdminLogEventActionToggleSlowMode | types.ChannelAdminLogEventActionStartGroupCall | types.ChannelAdminLogEventActionDiscardGroupCall | types.ChannelAdminLogEventActionParticipantMute | types.ChannelAdminLogEventActionParticipantUnmute | types.ChannelAdminLogEventActionToggleGroupCallSetting | types.ChannelAdminLogEventActionParticipantJoinByInvite | types.ChannelAdminLogEventActionExportedInviteDelete | types.ChannelAdminLogEventActionExportedInviteRevoke | types.ChannelAdminLogEventActionExportedInviteEdit | types.ChannelAdminLogEventActionParticipantVolume | types.ChannelAdminLogEventActionChangeHistoryTtl | types.ChannelAdminLogEventActionParticipantJoinByRequest | types.ChannelAdminLogEventActionToggleNoForwards | types.ChannelAdminLogEventActionSendMessage | types.ChannelAdminLogEventActionChangeAvailableReactions | types.ChannelAdminLogEventActionChangeUsernames | types.ChannelAdminLogEventActionToggleForum | types.ChannelAdminLogEventActionCreateTopic | types.ChannelAdminLogEventActionEditTopic | types.ChannelAdminLogEventActionDeleteTopic | types.ChannelAdminLogEventActionPinTopic | types.ChannelAdminLogEventActionToggleAntiSpam | types.ChannelAdminLogEventActionChangePeerColor | types.ChannelAdminLogEventActionChangeProfilePeerColor | types.ChannelAdminLogEventActionChangeWallpaper | types.ChannelAdminLogEventActionChangeEmojiStatus | types.ChannelAdminLogEventActionChangeEmojiStickerSet | types.ChannelAdminLogEventActionToggleSignatureProfiles | types.ChannelAdminLogEventActionParticipantSubExtend | types.ChannelAdminLogEventActionToggleAutotranslation,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelAdminLogEventsFilter(TLObject):
    """
    [Read `channelAdminLogEventsFilter` docs](https://core.telegram.org/constructor/channelAdminLogEventsFilter).

    Generated from the following TL definition:
    ```tl
    channelAdminLogEventsFilter#ea107ae4 flags:# join:flags.0?true leave:flags.1?true invite:flags.2?true ban:flags.3?true unban:flags.4?true kick:flags.5?true unkick:flags.6?true promote:flags.7?true demote:flags.8?true info:flags.9?true settings:flags.10?true pinned:flags.11?true edit:flags.12?true delete:flags.13?true group_call:flags.14?true invites:flags.15?true send:flags.16?true forums:flags.17?true sub_extend:flags.18?true = ChannelAdminLogEventsFilter
    ```
    """
    def __new__(
        cls,
        join: bool,
        leave: bool,
        invite: bool,
        ban: bool,
        unban: bool,
        kick: bool,
        unkick: bool,
        promote: bool,
        demote: bool,
        info: bool,
        settings: bool,
        pinned: bool,
        edit: bool,
        delete: bool,
        group_call: bool,
        invites: bool,
        send: bool,
        forums: bool,
        sub_extend: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PopularContact(TLObject):
    """
    [Read `popularContact` docs](https://core.telegram.org/constructor/popularContact).

    Generated from the following TL definition:
    ```tl
    popularContact#5ce14175 client_id:long importers:int = PopularContact
    ```
    """
    def __new__(
        cls,
        client_id: int,
        importers: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RecentMeUrlUnknown(TLObject):
    """
    [Read `recentMeUrlUnknown` docs](https://core.telegram.org/constructor/recentMeUrlUnknown).

    Generated from the following TL definition:
    ```tl
    recentMeUrlUnknown#46e1d13d url:string = RecentMeUrl
    ```
    """
    def __new__(
        cls,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RecentMeUrlUser(TLObject):
    """
    [Read `recentMeUrlUser` docs](https://core.telegram.org/constructor/recentMeUrlUser).

    Generated from the following TL definition:
    ```tl
    recentMeUrlUser#b92c09e2 url:string user_id:long = RecentMeUrl
    ```
    """
    def __new__(
        cls,
        url: str,
        user_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RecentMeUrlChat(TLObject):
    """
    [Read `recentMeUrlChat` docs](https://core.telegram.org/constructor/recentMeUrlChat).

    Generated from the following TL definition:
    ```tl
    recentMeUrlChat#b2da71d2 url:string chat_id:long = RecentMeUrl
    ```
    """
    def __new__(
        cls,
        url: str,
        chat_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RecentMeUrlChatInvite(TLObject):
    """
    [Read `recentMeUrlChatInvite` docs](https://core.telegram.org/constructor/recentMeUrlChatInvite).

    Generated from the following TL definition:
    ```tl
    recentMeUrlChatInvite#eb49081d url:string chat_invite:ChatInvite = RecentMeUrl
    ```
    """
    def __new__(
        cls,
        url: str,
        chat_invite: types.ChatInviteAlready | types.ChatInvite | types.ChatInvitePeek,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RecentMeUrlStickerSet(TLObject):
    """
    [Read `recentMeUrlStickerSet` docs](https://core.telegram.org/constructor/recentMeUrlStickerSet).

    Generated from the following TL definition:
    ```tl
    recentMeUrlStickerSet#bc0a57dc url:string set:StickerSetCovered = RecentMeUrl
    ```
    """
    def __new__(
        cls,
        url: str,
        set: types.StickerSetCovered | types.StickerSetMultiCovered | types.StickerSetFullCovered | types.StickerSetNoCovered,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputSingleMedia(TLObject):
    """
    [Read `inputSingleMedia` docs](https://core.telegram.org/constructor/inputSingleMedia).

    Generated from the following TL definition:
    ```tl
    inputSingleMedia#1cc6e91f flags:# media:InputMedia random_id:long message:string entities:flags.0?Vector<MessageEntity> = InputSingleMedia
    ```
    """
    def __new__(
        cls,
        media: types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice,
        random_id: int,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebAuthorization(TLObject):
    """
    [Read `webAuthorization` docs](https://core.telegram.org/constructor/webAuthorization).

    Generated from the following TL definition:
    ```tl
    webAuthorization#a6f8f452 hash:long bot_id:long domain:string browser:string platform:string date_created:int date_active:int ip:string region:string = WebAuthorization
    ```
    """
    def __new__(
        cls,
        hash: int,
        bot_id: int,
        domain: str,
        browser: str,
        platform: str,
        date_created: int,
        date_active: int,
        ip: str,
        region: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessageId(TLObject):
    """
    [Read `inputMessageID` docs](https://core.telegram.org/constructor/inputMessageID).

    Generated from the following TL definition:
    ```tl
    inputMessageID#a676a322 id:int = InputMessage
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessageReplyTo(TLObject):
    """
    [Read `inputMessageReplyTo` docs](https://core.telegram.org/constructor/inputMessageReplyTo).

    Generated from the following TL definition:
    ```tl
    inputMessageReplyTo#bad88395 id:int = InputMessage
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessagePinned(TLObject):
    """
    [Read `inputMessagePinned` docs](https://core.telegram.org/constructor/inputMessagePinned).

    Generated from the following TL definition:
    ```tl
    inputMessagePinned#86872538 = InputMessage
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMessageCallbackQuery(TLObject):
    """
    [Read `inputMessageCallbackQuery` docs](https://core.telegram.org/constructor/inputMessageCallbackQuery).

    Generated from the following TL definition:
    ```tl
    inputMessageCallbackQuery#acfa1a7e id:int query_id:long = InputMessage
    ```
    """
    def __new__(
        cls,
        id: int,
        query_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputDialogPeer(TLObject):
    """
    [Read `inputDialogPeer` docs](https://core.telegram.org/constructor/inputDialogPeer).

    Generated from the following TL definition:
    ```tl
    inputDialogPeer#fcaafeb7 peer:InputPeer = InputDialogPeer
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputDialogPeerFolder(TLObject):
    """
    [Read `inputDialogPeerFolder` docs](https://core.telegram.org/constructor/inputDialogPeerFolder).

    Generated from the following TL definition:
    ```tl
    inputDialogPeerFolder#64600527 folder_id:int = InputDialogPeer
    ```
    """
    def __new__(
        cls,
        folder_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DialogPeer(TLObject):
    """
    [Read `dialogPeer` docs](https://core.telegram.org/constructor/dialogPeer).

    Generated from the following TL definition:
    ```tl
    dialogPeer#e56dbf05 peer:Peer = DialogPeer
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DialogPeerFolder(TLObject):
    """
    [Read `dialogPeerFolder` docs](https://core.telegram.org/constructor/dialogPeerFolder).

    Generated from the following TL definition:
    ```tl
    dialogPeerFolder#514519e2 folder_id:int = DialogPeer
    ```
    """
    def __new__(
        cls,
        folder_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FileHash(TLObject):
    """
    [Read `fileHash` docs](https://core.telegram.org/constructor/fileHash).

    Generated from the following TL definition:
    ```tl
    fileHash#f39b035c offset:long limit:int hash:bytes = FileHash
    ```
    """
    def __new__(
        cls,
        offset: int,
        limit: int,
        hash: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputClientProxy(TLObject):
    """
    [Read `inputClientProxy` docs](https://core.telegram.org/constructor/inputClientProxy).

    Generated from the following TL definition:
    ```tl
    inputClientProxy#75588b3f address:string port:int = InputClientProxy
    ```
    """
    def __new__(
        cls,
        address: str,
        port: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputSecureFileUploaded(TLObject):
    """
    [Read `inputSecureFileUploaded` docs](https://core.telegram.org/constructor/inputSecureFileUploaded).

    Generated from the following TL definition:
    ```tl
    inputSecureFileUploaded#3334b0f0 id:long parts:int md5_checksum:string file_hash:bytes secret:bytes = InputSecureFile
    ```
    """
    def __new__(
        cls,
        id: int,
        parts: int,
        md5_checksum: str,
        file_hash: bytes,
        secret: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputSecureFile(TLObject):
    """
    [Read `inputSecureFile` docs](https://core.telegram.org/constructor/inputSecureFile).

    Generated from the following TL definition:
    ```tl
    inputSecureFile#5367e5be id:long access_hash:long = InputSecureFile
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureFileEmpty(TLObject):
    """
    [Read `secureFileEmpty` docs](https://core.telegram.org/constructor/secureFileEmpty).

    Generated from the following TL definition:
    ```tl
    secureFileEmpty#64199744 = SecureFile
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureFile(TLObject):
    """
    [Read `secureFile` docs](https://core.telegram.org/constructor/secureFile).

    Generated from the following TL definition:
    ```tl
    secureFile#7d09c27e id:long access_hash:long size:long dc_id:int date:int file_hash:bytes secret:bytes = SecureFile
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        size: int,
        dc_id: int,
        date: int,
        file_hash: bytes,
        secret: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureData(TLObject):
    """
    [Read `secureData` docs](https://core.telegram.org/constructor/secureData).

    Generated from the following TL definition:
    ```tl
    secureData#8aeabec3 data:bytes data_hash:bytes secret:bytes = SecureData
    ```
    """
    def __new__(
        cls,
        data: bytes,
        data_hash: bytes,
        secret: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecurePlainPhone(TLObject):
    """
    [Read `securePlainPhone` docs](https://core.telegram.org/constructor/securePlainPhone).

    Generated from the following TL definition:
    ```tl
    securePlainPhone#7d6099dd phone:string = SecurePlainData
    ```
    """
    def __new__(
        cls,
        phone: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecurePlainEmail(TLObject):
    """
    [Read `securePlainEmail` docs](https://core.telegram.org/constructor/securePlainEmail).

    Generated from the following TL definition:
    ```tl
    securePlainEmail#21ec5a5f email:string = SecurePlainData
    ```
    """
    def __new__(
        cls,
        email: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypePersonalDetails(TLObject):
    """
    [Read `secureValueTypePersonalDetails` docs](https://core.telegram.org/constructor/secureValueTypePersonalDetails).

    Generated from the following TL definition:
    ```tl
    secureValueTypePersonalDetails#9d2a81e3 = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypePassport(TLObject):
    """
    [Read `secureValueTypePassport` docs](https://core.telegram.org/constructor/secureValueTypePassport).

    Generated from the following TL definition:
    ```tl
    secureValueTypePassport#3dac6a00 = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypeDriverLicense(TLObject):
    """
    [Read `secureValueTypeDriverLicense` docs](https://core.telegram.org/constructor/secureValueTypeDriverLicense).

    Generated from the following TL definition:
    ```tl
    secureValueTypeDriverLicense#6e425c4 = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypeIdentityCard(TLObject):
    """
    [Read `secureValueTypeIdentityCard` docs](https://core.telegram.org/constructor/secureValueTypeIdentityCard).

    Generated from the following TL definition:
    ```tl
    secureValueTypeIdentityCard#a0d0744b = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypeInternalPassport(TLObject):
    """
    [Read `secureValueTypeInternalPassport` docs](https://core.telegram.org/constructor/secureValueTypeInternalPassport).

    Generated from the following TL definition:
    ```tl
    secureValueTypeInternalPassport#99a48f23 = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypeAddress(TLObject):
    """
    [Read `secureValueTypeAddress` docs](https://core.telegram.org/constructor/secureValueTypeAddress).

    Generated from the following TL definition:
    ```tl
    secureValueTypeAddress#cbe31e26 = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypeUtilityBill(TLObject):
    """
    [Read `secureValueTypeUtilityBill` docs](https://core.telegram.org/constructor/secureValueTypeUtilityBill).

    Generated from the following TL definition:
    ```tl
    secureValueTypeUtilityBill#fc36954e = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypeBankStatement(TLObject):
    """
    [Read `secureValueTypeBankStatement` docs](https://core.telegram.org/constructor/secureValueTypeBankStatement).

    Generated from the following TL definition:
    ```tl
    secureValueTypeBankStatement#89137c0d = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypeRentalAgreement(TLObject):
    """
    [Read `secureValueTypeRentalAgreement` docs](https://core.telegram.org/constructor/secureValueTypeRentalAgreement).

    Generated from the following TL definition:
    ```tl
    secureValueTypeRentalAgreement#8b883488 = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypePassportRegistration(TLObject):
    """
    [Read `secureValueTypePassportRegistration` docs](https://core.telegram.org/constructor/secureValueTypePassportRegistration).

    Generated from the following TL definition:
    ```tl
    secureValueTypePassportRegistration#99e3806a = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypeTemporaryRegistration(TLObject):
    """
    [Read `secureValueTypeTemporaryRegistration` docs](https://core.telegram.org/constructor/secureValueTypeTemporaryRegistration).

    Generated from the following TL definition:
    ```tl
    secureValueTypeTemporaryRegistration#ea02ec33 = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypePhone(TLObject):
    """
    [Read `secureValueTypePhone` docs](https://core.telegram.org/constructor/secureValueTypePhone).

    Generated from the following TL definition:
    ```tl
    secureValueTypePhone#b320aadb = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueTypeEmail(TLObject):
    """
    [Read `secureValueTypeEmail` docs](https://core.telegram.org/constructor/secureValueTypeEmail).

    Generated from the following TL definition:
    ```tl
    secureValueTypeEmail#8e3ca7ee = SecureValueType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValue(TLObject):
    """
    [Read `secureValue` docs](https://core.telegram.org/constructor/secureValue).

    Generated from the following TL definition:
    ```tl
    secureValue#187fa0ca flags:# type:SecureValueType data:flags.0?SecureData front_side:flags.1?SecureFile reverse_side:flags.2?SecureFile selfie:flags.3?SecureFile translation:flags.6?Vector<SecureFile> files:flags.4?Vector<SecureFile> plain_data:flags.5?SecurePlainData hash:bytes = SecureValue
    ```
    """
    def __new__(
        cls,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
        data: Optional[types.SecureData],
        front_side: Optional[types.SecureFileEmpty | types.SecureFile],
        reverse_side: Optional[types.SecureFileEmpty | types.SecureFile],
        selfie: Optional[types.SecureFileEmpty | types.SecureFile],
        translation: Optional[Sequence[types.SecureFileEmpty | types.SecureFile]],
        files: Optional[Sequence[types.SecureFileEmpty | types.SecureFile]],
        plain_data: Optional[types.SecurePlainPhone | types.SecurePlainEmail],
        hash: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputSecureValue(TLObject):
    """
    [Read `inputSecureValue` docs](https://core.telegram.org/constructor/inputSecureValue).

    Generated from the following TL definition:
    ```tl
    inputSecureValue#db21d0a7 flags:# type:SecureValueType data:flags.0?SecureData front_side:flags.1?InputSecureFile reverse_side:flags.2?InputSecureFile selfie:flags.3?InputSecureFile translation:flags.6?Vector<InputSecureFile> files:flags.4?Vector<InputSecureFile> plain_data:flags.5?SecurePlainData = InputSecureValue
    ```
    """
    def __new__(
        cls,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
        data: Optional[types.SecureData],
        front_side: Optional[types.InputSecureFileUploaded | types.InputSecureFile],
        reverse_side: Optional[types.InputSecureFileUploaded | types.InputSecureFile],
        selfie: Optional[types.InputSecureFileUploaded | types.InputSecureFile],
        translation: Optional[Sequence[types.InputSecureFileUploaded | types.InputSecureFile]],
        files: Optional[Sequence[types.InputSecureFileUploaded | types.InputSecureFile]],
        plain_data: Optional[types.SecurePlainPhone | types.SecurePlainEmail],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueHash(TLObject):
    """
    [Read `secureValueHash` docs](https://core.telegram.org/constructor/secureValueHash).

    Generated from the following TL definition:
    ```tl
    secureValueHash#ed1ecdb0 type:SecureValueType hash:bytes = SecureValueHash
    ```
    """
    def __new__(
        cls,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
        hash: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueErrorData(TLObject):
    """
    [Read `secureValueErrorData` docs](https://core.telegram.org/constructor/secureValueErrorData).

    Generated from the following TL definition:
    ```tl
    secureValueErrorData#e8a40bd9 type:SecureValueType data_hash:bytes field:string text:string = SecureValueError
    ```
    """
    def __new__(
        cls,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
        data_hash: bytes,
        field: str,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueErrorFrontSide(TLObject):
    """
    [Read `secureValueErrorFrontSide` docs](https://core.telegram.org/constructor/secureValueErrorFrontSide).

    Generated from the following TL definition:
    ```tl
    secureValueErrorFrontSide#be3dfa type:SecureValueType file_hash:bytes text:string = SecureValueError
    ```
    """
    def __new__(
        cls,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
        file_hash: bytes,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueErrorReverseSide(TLObject):
    """
    [Read `secureValueErrorReverseSide` docs](https://core.telegram.org/constructor/secureValueErrorReverseSide).

    Generated from the following TL definition:
    ```tl
    secureValueErrorReverseSide#868a2aa5 type:SecureValueType file_hash:bytes text:string = SecureValueError
    ```
    """
    def __new__(
        cls,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
        file_hash: bytes,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueErrorSelfie(TLObject):
    """
    [Read `secureValueErrorSelfie` docs](https://core.telegram.org/constructor/secureValueErrorSelfie).

    Generated from the following TL definition:
    ```tl
    secureValueErrorSelfie#e537ced6 type:SecureValueType file_hash:bytes text:string = SecureValueError
    ```
    """
    def __new__(
        cls,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
        file_hash: bytes,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueErrorFile(TLObject):
    """
    [Read `secureValueErrorFile` docs](https://core.telegram.org/constructor/secureValueErrorFile).

    Generated from the following TL definition:
    ```tl
    secureValueErrorFile#7a700873 type:SecureValueType file_hash:bytes text:string = SecureValueError
    ```
    """
    def __new__(
        cls,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
        file_hash: bytes,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueErrorFiles(TLObject):
    """
    [Read `secureValueErrorFiles` docs](https://core.telegram.org/constructor/secureValueErrorFiles).

    Generated from the following TL definition:
    ```tl
    secureValueErrorFiles#666220e9 type:SecureValueType file_hash:Vector<bytes> text:string = SecureValueError
    ```
    """
    def __new__(
        cls,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
        file_hash: Sequence[bytes],
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueError(TLObject):
    """
    [Read `secureValueError` docs](https://core.telegram.org/constructor/secureValueError).

    Generated from the following TL definition:
    ```tl
    secureValueError#869d758f type:SecureValueType hash:bytes text:string = SecureValueError
    ```
    """
    def __new__(
        cls,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
        hash: bytes,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueErrorTranslationFile(TLObject):
    """
    [Read `secureValueErrorTranslationFile` docs](https://core.telegram.org/constructor/secureValueErrorTranslationFile).

    Generated from the following TL definition:
    ```tl
    secureValueErrorTranslationFile#a1144770 type:SecureValueType file_hash:bytes text:string = SecureValueError
    ```
    """
    def __new__(
        cls,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
        file_hash: bytes,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureValueErrorTranslationFiles(TLObject):
    """
    [Read `secureValueErrorTranslationFiles` docs](https://core.telegram.org/constructor/secureValueErrorTranslationFiles).

    Generated from the following TL definition:
    ```tl
    secureValueErrorTranslationFiles#34636dd8 type:SecureValueType file_hash:Vector<bytes> text:string = SecureValueError
    ```
    """
    def __new__(
        cls,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
        file_hash: Sequence[bytes],
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureCredentialsEncrypted(TLObject):
    """
    [Read `secureCredentialsEncrypted` docs](https://core.telegram.org/constructor/secureCredentialsEncrypted).

    Generated from the following TL definition:
    ```tl
    secureCredentialsEncrypted#33f0ea47 data:bytes hash:bytes secret:bytes = SecureCredentialsEncrypted
    ```
    """
    def __new__(
        cls,
        data: bytes,
        hash: bytes,
        secret: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedPhoneContact(TLObject):
    """
    [Read `savedPhoneContact` docs](https://core.telegram.org/constructor/savedPhoneContact).

    Generated from the following TL definition:
    ```tl
    savedPhoneContact#1142bd56 phone:string first_name:string last_name:string date:int = SavedContact
    ```
    """
    def __new__(
        cls,
        phone: str,
        first_name: str,
        last_name: str,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PasswordKdfAlgoUnknown(TLObject):
    """
    [Read `passwordKdfAlgoUnknown` docs](https://core.telegram.org/constructor/passwordKdfAlgoUnknown).

    Generated from the following TL definition:
    ```tl
    passwordKdfAlgoUnknown#d45ab096 = PasswordKdfAlgo
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PasswordKdfAlgoSha256Sha256Pbkdf2Hmacsha512iter100000Sha256ModPow(TLObject):
    """
    [Read `passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow` docs](https://core.telegram.org/constructor/passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow).

    Generated from the following TL definition:
    ```tl
    passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow#3a912d4a salt1:bytes salt2:bytes g:int p:bytes = PasswordKdfAlgo
    ```
    """
    def __new__(
        cls,
        salt1: bytes,
        salt2: bytes,
        g: int,
        p: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecurePasswordKdfAlgoUnknown(TLObject):
    """
    [Read `securePasswordKdfAlgoUnknown` docs](https://core.telegram.org/constructor/securePasswordKdfAlgoUnknown).

    Generated from the following TL definition:
    ```tl
    securePasswordKdfAlgoUnknown#4a8537 = SecurePasswordKdfAlgo
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecurePasswordKdfAlgoPbkdf2Hmacsha512iter100000(TLObject):
    """
    [Read `securePasswordKdfAlgoPBKDF2HMACSHA512iter100000` docs](https://core.telegram.org/constructor/securePasswordKdfAlgoPBKDF2HMACSHA512iter100000).

    Generated from the following TL definition:
    ```tl
    securePasswordKdfAlgoPBKDF2HMACSHA512iter100000#bbf2dda0 salt:bytes = SecurePasswordKdfAlgo
    ```
    """
    def __new__(
        cls,
        salt: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecurePasswordKdfAlgoSha512(TLObject):
    """
    [Read `securePasswordKdfAlgoSHA512` docs](https://core.telegram.org/constructor/securePasswordKdfAlgoSHA512).

    Generated from the following TL definition:
    ```tl
    securePasswordKdfAlgoSHA512#86471d92 salt:bytes = SecurePasswordKdfAlgo
    ```
    """
    def __new__(
        cls,
        salt: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureSecretSettings(TLObject):
    """
    [Read `secureSecretSettings` docs](https://core.telegram.org/constructor/secureSecretSettings).

    Generated from the following TL definition:
    ```tl
    secureSecretSettings#1527bcac secure_algo:SecurePasswordKdfAlgo secure_secret:bytes secure_secret_id:long = SecureSecretSettings
    ```
    """
    def __new__(
        cls,
        secure_algo: types.SecurePasswordKdfAlgoUnknown | types.SecurePasswordKdfAlgoPbkdf2Hmacsha512iter100000 | types.SecurePasswordKdfAlgoSha512,
        secure_secret: bytes,
        secure_secret_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputCheckPasswordEmpty(TLObject):
    """
    [Read `inputCheckPasswordEmpty` docs](https://core.telegram.org/constructor/inputCheckPasswordEmpty).

    Generated from the following TL definition:
    ```tl
    inputCheckPasswordEmpty#9880f658 = InputCheckPasswordSRP
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputCheckPasswordSrp(TLObject):
    """
    [Read `inputCheckPasswordSRP` docs](https://core.telegram.org/constructor/inputCheckPasswordSRP).

    Generated from the following TL definition:
    ```tl
    inputCheckPasswordSRP#d27ff082 srp_id:long A:bytes M1:bytes = InputCheckPasswordSRP
    ```
    """
    def __new__(
        cls,
        srp_id: int,
        a: bytes,
        m1: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureRequiredType(TLObject):
    """
    [Read `secureRequiredType` docs](https://core.telegram.org/constructor/secureRequiredType).

    Generated from the following TL definition:
    ```tl
    secureRequiredType#829d99da flags:# native_names:flags.0?true selfie_required:flags.1?true translation_required:flags.2?true type:SecureValueType = SecureRequiredType
    ```
    """
    def __new__(
        cls,
        native_names: bool,
        selfie_required: bool,
        translation_required: bool,
        type: types.SecureValueTypePersonalDetails | types.SecureValueTypePassport | types.SecureValueTypeDriverLicense | types.SecureValueTypeIdentityCard | types.SecureValueTypeInternalPassport | types.SecureValueTypeAddress | types.SecureValueTypeUtilityBill | types.SecureValueTypeBankStatement | types.SecureValueTypeRentalAgreement | types.SecureValueTypePassportRegistration | types.SecureValueTypeTemporaryRegistration | types.SecureValueTypePhone | types.SecureValueTypeEmail,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SecureRequiredTypeOneOf(TLObject):
    """
    [Read `secureRequiredTypeOneOf` docs](https://core.telegram.org/constructor/secureRequiredTypeOneOf).

    Generated from the following TL definition:
    ```tl
    secureRequiredTypeOneOf#27477b4 types:Vector<SecureRequiredType> = SecureRequiredType
    ```
    """
    def __new__(
        cls,
        types: Sequence[types.SecureRequiredType | types.SecureRequiredTypeOneOf],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputAppEvent(TLObject):
    """
    [Read `inputAppEvent` docs](https://core.telegram.org/constructor/inputAppEvent).

    Generated from the following TL definition:
    ```tl
    inputAppEvent#1d1b1245 time:double type:string peer:long data:JSONValue = InputAppEvent
    ```
    """
    def __new__(
        cls,
        time: float,
        type: str,
        peer: int,
        data: types.JsonNull | types.JsonBool | types.JsonNumber | types.JsonString | types.JsonArray | types.JsonObject,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JsonObjectValue(TLObject):
    """
    [Read `jsonObjectValue` docs](https://core.telegram.org/constructor/jsonObjectValue).

    Generated from the following TL definition:
    ```tl
    jsonObjectValue#c0de1bd9 key:string value:JSONValue = JSONObjectValue
    ```
    """
    def __new__(
        cls,
        key: str,
        value: types.JsonNull | types.JsonBool | types.JsonNumber | types.JsonString | types.JsonArray | types.JsonObject,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JsonNull(TLObject):
    """
    [Read `jsonNull` docs](https://core.telegram.org/constructor/jsonNull).

    Generated from the following TL definition:
    ```tl
    jsonNull#3f6d7b68 = JSONValue
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JsonBool(TLObject):
    """
    [Read `jsonBool` docs](https://core.telegram.org/constructor/jsonBool).

    Generated from the following TL definition:
    ```tl
    jsonBool#c7345e6a value:Bool = JSONValue
    ```
    """
    def __new__(
        cls,
        value: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JsonNumber(TLObject):
    """
    [Read `jsonNumber` docs](https://core.telegram.org/constructor/jsonNumber).

    Generated from the following TL definition:
    ```tl
    jsonNumber#2be0dfa4 value:double = JSONValue
    ```
    """
    def __new__(
        cls,
        value: float,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JsonString(TLObject):
    """
    [Read `jsonString` docs](https://core.telegram.org/constructor/jsonString).

    Generated from the following TL definition:
    ```tl
    jsonString#b71e767a value:string = JSONValue
    ```
    """
    def __new__(
        cls,
        value: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JsonArray(TLObject):
    """
    [Read `jsonArray` docs](https://core.telegram.org/constructor/jsonArray).

    Generated from the following TL definition:
    ```tl
    jsonArray#f7444763 value:Vector<JSONValue> = JSONValue
    ```
    """
    def __new__(
        cls,
        value: Sequence[types.JsonNull | types.JsonBool | types.JsonNumber | types.JsonString | types.JsonArray | types.JsonObject],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class JsonObject(TLObject):
    """
    [Read `jsonObject` docs](https://core.telegram.org/constructor/jsonObject).

    Generated from the following TL definition:
    ```tl
    jsonObject#99c1d49d value:Vector<JSONObjectValue> = JSONValue
    ```
    """
    def __new__(
        cls,
        value: Sequence[types.JsonObjectValue],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageTableCell(TLObject):
    """
    [Read `pageTableCell` docs](https://core.telegram.org/constructor/pageTableCell).

    Generated from the following TL definition:
    ```tl
    pageTableCell#34566b6a flags:# header:flags.0?true align_center:flags.3?true align_right:flags.4?true valign_middle:flags.5?true valign_bottom:flags.6?true text:flags.7?RichText colspan:flags.1?int rowspan:flags.2?int = PageTableCell
    ```
    """
    def __new__(
        cls,
        header: bool,
        align_center: bool,
        align_right: bool,
        valign_middle: bool,
        valign_bottom: bool,
        text: Optional[types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor],
        colspan: Optional[int],
        rowspan: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageTableRow(TLObject):
    """
    [Read `pageTableRow` docs](https://core.telegram.org/constructor/pageTableRow).

    Generated from the following TL definition:
    ```tl
    pageTableRow#e0c0c5e5 cells:Vector<PageTableCell> = PageTableRow
    ```
    """
    def __new__(
        cls,
        cells: Sequence[types.PageTableCell],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageCaption(TLObject):
    """
    [Read `pageCaption` docs](https://core.telegram.org/constructor/pageCaption).

    Generated from the following TL definition:
    ```tl
    pageCaption#6f747657 text:RichText credit:RichText = PageCaption
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
        credit: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageListItemText(TLObject):
    """
    [Read `pageListItemText` docs](https://core.telegram.org/constructor/pageListItemText).

    Generated from the following TL definition:
    ```tl
    pageListItemText#b92fb6cd text:RichText = PageListItem
    ```
    """
    def __new__(
        cls,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageListItemBlocks(TLObject):
    """
    [Read `pageListItemBlocks` docs](https://core.telegram.org/constructor/pageListItemBlocks).

    Generated from the following TL definition:
    ```tl
    pageListItemBlocks#25e073fc blocks:Vector<PageBlock> = PageListItem
    ```
    """
    def __new__(
        cls,
        blocks: Sequence[types.PageBlockUnsupported | types.PageBlockTitle | types.PageBlockSubtitle | types.PageBlockAuthorDate | types.PageBlockHeader | types.PageBlockSubheader | types.PageBlockParagraph | types.PageBlockPreformatted | types.PageBlockFooter | types.PageBlockDivider | types.PageBlockAnchor | types.PageBlockList | types.PageBlockBlockquote | types.PageBlockPullquote | types.PageBlockPhoto | types.PageBlockVideo | types.PageBlockCover | types.PageBlockEmbed | types.PageBlockEmbedPost | types.PageBlockCollage | types.PageBlockSlideshow | types.PageBlockChannel | types.PageBlockAudio | types.PageBlockKicker | types.PageBlockTable | types.PageBlockOrderedList | types.PageBlockDetails | types.PageBlockRelatedArticles | types.PageBlockMap],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageListOrderedItemText(TLObject):
    """
    [Read `pageListOrderedItemText` docs](https://core.telegram.org/constructor/pageListOrderedItemText).

    Generated from the following TL definition:
    ```tl
    pageListOrderedItemText#5e068047 num:string text:RichText = PageListOrderedItem
    ```
    """
    def __new__(
        cls,
        num: str,
        text: types.TextEmpty | types.TextPlain | types.TextBold | types.TextItalic | types.TextUnderline | types.TextStrike | types.TextFixed | types.TextUrl | types.TextEmail | types.TextConcat | types.TextSubscript | types.TextSuperscript | types.TextMarked | types.TextPhone | types.TextImage | types.TextAnchor,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageListOrderedItemBlocks(TLObject):
    """
    [Read `pageListOrderedItemBlocks` docs](https://core.telegram.org/constructor/pageListOrderedItemBlocks).

    Generated from the following TL definition:
    ```tl
    pageListOrderedItemBlocks#98dd8936 num:string blocks:Vector<PageBlock> = PageListOrderedItem
    ```
    """
    def __new__(
        cls,
        num: str,
        blocks: Sequence[types.PageBlockUnsupported | types.PageBlockTitle | types.PageBlockSubtitle | types.PageBlockAuthorDate | types.PageBlockHeader | types.PageBlockSubheader | types.PageBlockParagraph | types.PageBlockPreformatted | types.PageBlockFooter | types.PageBlockDivider | types.PageBlockAnchor | types.PageBlockList | types.PageBlockBlockquote | types.PageBlockPullquote | types.PageBlockPhoto | types.PageBlockVideo | types.PageBlockCover | types.PageBlockEmbed | types.PageBlockEmbedPost | types.PageBlockCollage | types.PageBlockSlideshow | types.PageBlockChannel | types.PageBlockAudio | types.PageBlockKicker | types.PageBlockTable | types.PageBlockOrderedList | types.PageBlockDetails | types.PageBlockRelatedArticles | types.PageBlockMap],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PageRelatedArticle(TLObject):
    """
    [Read `pageRelatedArticle` docs](https://core.telegram.org/constructor/pageRelatedArticle).

    Generated from the following TL definition:
    ```tl
    pageRelatedArticle#b390dc08 flags:# url:string webpage_id:long title:flags.0?string description:flags.1?string photo_id:flags.2?long author:flags.3?string published_date:flags.4?int = PageRelatedArticle
    ```
    """
    def __new__(
        cls,
        url: str,
        webpage_id: int,
        title: Optional[str],
        description: Optional[str],
        photo_id: Optional[int],
        author: Optional[str],
        published_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Page(TLObject):
    """
    [Read `page` docs](https://core.telegram.org/constructor/page).

    Generated from the following TL definition:
    ```tl
    page#98657f0d flags:# part:flags.0?true rtl:flags.1?true v2:flags.2?true url:string blocks:Vector<PageBlock> photos:Vector<Photo> documents:Vector<Document> views:flags.3?int = Page
    ```
    """
    def __new__(
        cls,
        part: bool,
        rtl: bool,
        v2: bool,
        url: str,
        blocks: Sequence[types.PageBlockUnsupported | types.PageBlockTitle | types.PageBlockSubtitle | types.PageBlockAuthorDate | types.PageBlockHeader | types.PageBlockSubheader | types.PageBlockParagraph | types.PageBlockPreformatted | types.PageBlockFooter | types.PageBlockDivider | types.PageBlockAnchor | types.PageBlockList | types.PageBlockBlockquote | types.PageBlockPullquote | types.PageBlockPhoto | types.PageBlockVideo | types.PageBlockCover | types.PageBlockEmbed | types.PageBlockEmbedPost | types.PageBlockCollage | types.PageBlockSlideshow | types.PageBlockChannel | types.PageBlockAudio | types.PageBlockKicker | types.PageBlockTable | types.PageBlockOrderedList | types.PageBlockDetails | types.PageBlockRelatedArticles | types.PageBlockMap],
        photos: Sequence[types.PhotoEmpty | types.Photo],
        documents: Sequence[types.DocumentEmpty | types.Document],
        views: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PollAnswer(TLObject):
    """
    [Read `pollAnswer` docs](https://core.telegram.org/constructor/pollAnswer).

    Generated from the following TL definition:
    ```tl
    pollAnswer#ff16e2ca text:TextWithEntities option:bytes = PollAnswer
    ```
    """
    def __new__(
        cls,
        text: types.TextWithEntities,
        option: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Poll(TLObject):
    """
    [Read `poll` docs](https://core.telegram.org/constructor/poll).

    Generated from the following TL definition:
    ```tl
    poll#58747131 id:long flags:# closed:flags.0?true public_voters:flags.1?true multiple_choice:flags.2?true quiz:flags.3?true question:TextWithEntities answers:Vector<PollAnswer> close_period:flags.4?int close_date:flags.5?int = Poll
    ```
    """
    def __new__(
        cls,
        id: int,
        closed: bool,
        public_voters: bool,
        multiple_choice: bool,
        quiz: bool,
        question: types.TextWithEntities,
        answers: Sequence[types.PollAnswer],
        close_period: Optional[int],
        close_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PollAnswerVoters(TLObject):
    """
    [Read `pollAnswerVoters` docs](https://core.telegram.org/constructor/pollAnswerVoters).

    Generated from the following TL definition:
    ```tl
    pollAnswerVoters#3b6ddad2 flags:# chosen:flags.0?true correct:flags.1?true option:bytes voters:int = PollAnswerVoters
    ```
    """
    def __new__(
        cls,
        chosen: bool,
        correct: bool,
        option: bytes,
        voters: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PollResults(TLObject):
    """
    [Read `pollResults` docs](https://core.telegram.org/constructor/pollResults).

    Generated from the following TL definition:
    ```tl
    pollResults#7adf2420 flags:# min:flags.0?true results:flags.1?Vector<PollAnswerVoters> total_voters:flags.2?int recent_voters:flags.3?Vector<Peer> solution:flags.4?string solution_entities:flags.4?Vector<MessageEntity> = PollResults
    ```
    """
    def __new__(
        cls,
        min: bool,
        results: Optional[Sequence[types.PollAnswerVoters]],
        total_voters: Optional[int],
        recent_voters: Optional[Sequence[types.PeerUser | types.PeerChat | types.PeerChannel]],
        solution: Optional[str],
        solution_entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatOnlines(TLObject):
    """
    [Read `chatOnlines` docs](https://core.telegram.org/constructor/chatOnlines).

    Generated from the following TL definition:
    ```tl
    chatOnlines#f041e250 onlines:int = ChatOnlines
    ```
    """
    def __new__(
        cls,
        onlines: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StatsUrl(TLObject):
    """
    [Read `statsURL` docs](https://core.telegram.org/constructor/statsURL).

    Generated from the following TL definition:
    ```tl
    statsURL#47a971e0 url:string = StatsURL
    ```
    """
    def __new__(
        cls,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatAdminRights(TLObject):
    """
    [Read `chatAdminRights` docs](https://core.telegram.org/constructor/chatAdminRights).

    Generated from the following TL definition:
    ```tl
    chatAdminRights#5fb224d5 flags:# change_info:flags.0?true post_messages:flags.1?true edit_messages:flags.2?true delete_messages:flags.3?true ban_users:flags.4?true invite_users:flags.5?true pin_messages:flags.7?true add_admins:flags.9?true anonymous:flags.10?true manage_call:flags.11?true other:flags.12?true manage_topics:flags.13?true post_stories:flags.14?true edit_stories:flags.15?true delete_stories:flags.16?true manage_direct_messages:flags.17?true = ChatAdminRights
    ```
    """
    def __new__(
        cls,
        change_info: bool,
        post_messages: bool,
        edit_messages: bool,
        delete_messages: bool,
        ban_users: bool,
        invite_users: bool,
        pin_messages: bool,
        add_admins: bool,
        anonymous: bool,
        manage_call: bool,
        other: bool,
        manage_topics: bool,
        post_stories: bool,
        edit_stories: bool,
        delete_stories: bool,
        manage_direct_messages: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatBannedRights(TLObject):
    """
    [Read `chatBannedRights` docs](https://core.telegram.org/constructor/chatBannedRights).

    Generated from the following TL definition:
    ```tl
    chatBannedRights#9f120418 flags:# view_messages:flags.0?true send_messages:flags.1?true send_media:flags.2?true send_stickers:flags.3?true send_gifs:flags.4?true send_games:flags.5?true send_inline:flags.6?true embed_links:flags.7?true send_polls:flags.8?true change_info:flags.10?true invite_users:flags.15?true pin_messages:flags.17?true manage_topics:flags.18?true send_photos:flags.19?true send_videos:flags.20?true send_roundvideos:flags.21?true send_audios:flags.22?true send_voices:flags.23?true send_docs:flags.24?true send_plain:flags.25?true until_date:int = ChatBannedRights
    ```
    """
    def __new__(
        cls,
        view_messages: bool,
        send_messages: bool,
        send_media: bool,
        send_stickers: bool,
        send_gifs: bool,
        send_games: bool,
        send_inline: bool,
        embed_links: bool,
        send_polls: bool,
        change_info: bool,
        invite_users: bool,
        pin_messages: bool,
        manage_topics: bool,
        send_photos: bool,
        send_videos: bool,
        send_roundvideos: bool,
        send_audios: bool,
        send_voices: bool,
        send_docs: bool,
        send_plain: bool,
        until_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputWallPaper(TLObject):
    """
    [Read `inputWallPaper` docs](https://core.telegram.org/constructor/inputWallPaper).

    Generated from the following TL definition:
    ```tl
    inputWallPaper#e630b979 id:long access_hash:long = InputWallPaper
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputWallPaperSlug(TLObject):
    """
    [Read `inputWallPaperSlug` docs](https://core.telegram.org/constructor/inputWallPaperSlug).

    Generated from the following TL definition:
    ```tl
    inputWallPaperSlug#72091c80 slug:string = InputWallPaper
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputWallPaperNoFile(TLObject):
    """
    [Read `inputWallPaperNoFile` docs](https://core.telegram.org/constructor/inputWallPaperNoFile).

    Generated from the following TL definition:
    ```tl
    inputWallPaperNoFile#967a462e id:long = InputWallPaper
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CodeSettings(TLObject):
    """
    [Read `codeSettings` docs](https://core.telegram.org/constructor/codeSettings).

    Generated from the following TL definition:
    ```tl
    codeSettings#ad253d78 flags:# allow_flashcall:flags.0?true current_number:flags.1?true allow_app_hash:flags.4?true allow_missed_call:flags.5?true allow_firebase:flags.7?true unknown_number:flags.9?true logout_tokens:flags.6?Vector<bytes> token:flags.8?string app_sandbox:flags.8?Bool = CodeSettings
    ```
    """
    def __new__(
        cls,
        allow_flashcall: bool,
        current_number: bool,
        allow_app_hash: bool,
        allow_missed_call: bool,
        allow_firebase: bool,
        unknown_number: bool,
        logout_tokens: Optional[Sequence[bytes]],
        token: Optional[str],
        app_sandbox: Optional[bool],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WallPaperSettings(TLObject):
    """
    [Read `wallPaperSettings` docs](https://core.telegram.org/constructor/wallPaperSettings).

    Generated from the following TL definition:
    ```tl
    wallPaperSettings#372efcd0 flags:# blur:flags.1?true motion:flags.2?true background_color:flags.0?int second_background_color:flags.4?int third_background_color:flags.5?int fourth_background_color:flags.6?int intensity:flags.3?int rotation:flags.4?int emoticon:flags.7?string = WallPaperSettings
    ```
    """
    def __new__(
        cls,
        blur: bool,
        motion: bool,
        background_color: Optional[int],
        second_background_color: Optional[int],
        third_background_color: Optional[int],
        fourth_background_color: Optional[int],
        intensity: Optional[int],
        rotation: Optional[int],
        emoticon: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AutoDownloadSettings(TLObject):
    """
    [Read `autoDownloadSettings` docs](https://core.telegram.org/constructor/autoDownloadSettings).

    Generated from the following TL definition:
    ```tl
    autoDownloadSettings#baa57628 flags:# disabled:flags.0?true video_preload_large:flags.1?true audio_preload_next:flags.2?true phonecalls_less_data:flags.3?true stories_preload:flags.4?true photo_size_max:int video_size_max:long file_size_max:long video_upload_maxbitrate:int small_queue_active_operations_max:int large_queue_active_operations_max:int = AutoDownloadSettings
    ```
    """
    def __new__(
        cls,
        disabled: bool,
        video_preload_large: bool,
        audio_preload_next: bool,
        phonecalls_less_data: bool,
        stories_preload: bool,
        photo_size_max: int,
        video_size_max: int,
        file_size_max: int,
        video_upload_maxbitrate: int,
        small_queue_active_operations_max: int,
        large_queue_active_operations_max: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiKeyword(TLObject):
    """
    [Read `emojiKeyword` docs](https://core.telegram.org/constructor/emojiKeyword).

    Generated from the following TL definition:
    ```tl
    emojiKeyword#d5b3b9f9 keyword:string emoticons:Vector<string> = EmojiKeyword
    ```
    """
    def __new__(
        cls,
        keyword: str,
        emoticons: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiKeywordDeleted(TLObject):
    """
    [Read `emojiKeywordDeleted` docs](https://core.telegram.org/constructor/emojiKeywordDeleted).

    Generated from the following TL definition:
    ```tl
    emojiKeywordDeleted#236df622 keyword:string emoticons:Vector<string> = EmojiKeyword
    ```
    """
    def __new__(
        cls,
        keyword: str,
        emoticons: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiKeywordsDifference(TLObject):
    """
    [Read `emojiKeywordsDifference` docs](https://core.telegram.org/constructor/emojiKeywordsDifference).

    Generated from the following TL definition:
    ```tl
    emojiKeywordsDifference#5cc761bd lang_code:string from_version:int version:int keywords:Vector<EmojiKeyword> = EmojiKeywordsDifference
    ```
    """
    def __new__(
        cls,
        lang_code: str,
        from_version: int,
        version: int,
        keywords: Sequence[types.EmojiKeyword | types.EmojiKeywordDeleted],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiUrl(TLObject):
    """
    [Read `emojiURL` docs](https://core.telegram.org/constructor/emojiURL).

    Generated from the following TL definition:
    ```tl
    emojiURL#a575739d url:string = EmojiURL
    ```
    """
    def __new__(
        cls,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiLanguage(TLObject):
    """
    [Read `emojiLanguage` docs](https://core.telegram.org/constructor/emojiLanguage).

    Generated from the following TL definition:
    ```tl
    emojiLanguage#b3fb5361 lang_code:string = EmojiLanguage
    ```
    """
    def __new__(
        cls,
        lang_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Folder(TLObject):
    """
    [Read `folder` docs](https://core.telegram.org/constructor/folder).

    Generated from the following TL definition:
    ```tl
    folder#ff544e65 flags:# autofill_new_broadcasts:flags.0?true autofill_public_groups:flags.1?true autofill_new_correspondents:flags.2?true id:int title:string photo:flags.3?ChatPhoto = Folder
    ```
    """
    def __new__(
        cls,
        autofill_new_broadcasts: bool,
        autofill_public_groups: bool,
        autofill_new_correspondents: bool,
        id: int,
        title: str,
        photo: Optional[types.ChatPhotoEmpty | types.ChatPhoto],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputFolderPeer(TLObject):
    """
    [Read `inputFolderPeer` docs](https://core.telegram.org/constructor/inputFolderPeer).

    Generated from the following TL definition:
    ```tl
    inputFolderPeer#fbd2c296 peer:InputPeer folder_id:int = InputFolderPeer
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        folder_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FolderPeer(TLObject):
    """
    [Read `folderPeer` docs](https://core.telegram.org/constructor/folderPeer).

    Generated from the following TL definition:
    ```tl
    folderPeer#e9baa668 peer:Peer folder_id:int = FolderPeer
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        folder_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UrlAuthResultRequest(TLObject):
    """
    [Read `urlAuthResultRequest` docs](https://core.telegram.org/constructor/urlAuthResultRequest).

    Generated from the following TL definition:
    ```tl
    urlAuthResultRequest#92d33a0e flags:# request_write_access:flags.0?true bot:User domain:string = UrlAuthResult
    ```
    """
    def __new__(
        cls,
        request_write_access: bool,
        bot: types.UserEmpty | types.User,
        domain: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UrlAuthResultAccepted(TLObject):
    """
    [Read `urlAuthResultAccepted` docs](https://core.telegram.org/constructor/urlAuthResultAccepted).

    Generated from the following TL definition:
    ```tl
    urlAuthResultAccepted#8f8c0e4e url:string = UrlAuthResult
    ```
    """
    def __new__(
        cls,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UrlAuthResultDefault(TLObject):
    """
    [Read `urlAuthResultDefault` docs](https://core.telegram.org/constructor/urlAuthResultDefault).

    Generated from the following TL definition:
    ```tl
    urlAuthResultDefault#a9d6db1f = UrlAuthResult
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelLocationEmpty(TLObject):
    """
    [Read `channelLocationEmpty` docs](https://core.telegram.org/constructor/channelLocationEmpty).

    Generated from the following TL definition:
    ```tl
    channelLocationEmpty#bfb5ad8b = ChannelLocation
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChannelLocation(TLObject):
    """
    [Read `channelLocation` docs](https://core.telegram.org/constructor/channelLocation).

    Generated from the following TL definition:
    ```tl
    channelLocation#209b82db geo_point:GeoPoint address:string = ChannelLocation
    ```
    """
    def __new__(
        cls,
        geo_point: types.GeoPointEmpty | types.GeoPoint,
        address: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerLocated(TLObject):
    """
    [Read `peerLocated` docs](https://core.telegram.org/constructor/peerLocated).

    Generated from the following TL definition:
    ```tl
    peerLocated#ca461b5d peer:Peer expires:int distance:int = PeerLocated
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        expires: int,
        distance: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerSelfLocated(TLObject):
    """
    [Read `peerSelfLocated` docs](https://core.telegram.org/constructor/peerSelfLocated).

    Generated from the following TL definition:
    ```tl
    peerSelfLocated#f8ec284b expires:int = PeerLocated
    ```
    """
    def __new__(
        cls,
        expires: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RestrictionReason(TLObject):
    """
    [Read `restrictionReason` docs](https://core.telegram.org/constructor/restrictionReason).

    Generated from the following TL definition:
    ```tl
    restrictionReason#d072acb4 platform:string reason:string text:string = RestrictionReason
    ```
    """
    def __new__(
        cls,
        platform: str,
        reason: str,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputTheme(TLObject):
    """
    [Read `inputTheme` docs](https://core.telegram.org/constructor/inputTheme).

    Generated from the following TL definition:
    ```tl
    inputTheme#3c5693e9 id:long access_hash:long = InputTheme
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputThemeSlug(TLObject):
    """
    [Read `inputThemeSlug` docs](https://core.telegram.org/constructor/inputThemeSlug).

    Generated from the following TL definition:
    ```tl
    inputThemeSlug#f5890df1 slug:string = InputTheme
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Theme(TLObject):
    """
    [Read `theme` docs](https://core.telegram.org/constructor/theme).

    Generated from the following TL definition:
    ```tl
    theme#a00e67d6 flags:# creator:flags.0?true default:flags.1?true for_chat:flags.5?true id:long access_hash:long slug:string title:string document:flags.2?Document settings:flags.3?Vector<ThemeSettings> emoticon:flags.6?string installs_count:flags.4?int = Theme
    ```
    """
    def __new__(
        cls,
        creator: bool,
        default: bool,
        for_chat: bool,
        id: int,
        access_hash: int,
        slug: str,
        title: str,
        document: Optional[types.DocumentEmpty | types.Document],
        settings: Optional[Sequence[types.ThemeSettings]],
        emoticon: Optional[str],
        installs_count: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BaseThemeClassic(TLObject):
    """
    [Read `baseThemeClassic` docs](https://core.telegram.org/constructor/baseThemeClassic).

    Generated from the following TL definition:
    ```tl
    baseThemeClassic#c3a12462 = BaseTheme
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BaseThemeDay(TLObject):
    """
    [Read `baseThemeDay` docs](https://core.telegram.org/constructor/baseThemeDay).

    Generated from the following TL definition:
    ```tl
    baseThemeDay#fbd81688 = BaseTheme
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BaseThemeNight(TLObject):
    """
    [Read `baseThemeNight` docs](https://core.telegram.org/constructor/baseThemeNight).

    Generated from the following TL definition:
    ```tl
    baseThemeNight#b7b31ea8 = BaseTheme
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BaseThemeTinted(TLObject):
    """
    [Read `baseThemeTinted` docs](https://core.telegram.org/constructor/baseThemeTinted).

    Generated from the following TL definition:
    ```tl
    baseThemeTinted#6d5f77ee = BaseTheme
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BaseThemeArctic(TLObject):
    """
    [Read `baseThemeArctic` docs](https://core.telegram.org/constructor/baseThemeArctic).

    Generated from the following TL definition:
    ```tl
    baseThemeArctic#5b11125a = BaseTheme
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputThemeSettings(TLObject):
    """
    [Read `inputThemeSettings` docs](https://core.telegram.org/constructor/inputThemeSettings).

    Generated from the following TL definition:
    ```tl
    inputThemeSettings#8fde504f flags:# message_colors_animated:flags.2?true base_theme:BaseTheme accent_color:int outbox_accent_color:flags.3?int message_colors:flags.0?Vector<int> wallpaper:flags.1?InputWallPaper wallpaper_settings:flags.1?WallPaperSettings = InputThemeSettings
    ```
    """
    def __new__(
        cls,
        message_colors_animated: bool,
        base_theme: types.BaseThemeClassic | types.BaseThemeDay | types.BaseThemeNight | types.BaseThemeTinted | types.BaseThemeArctic,
        accent_color: int,
        outbox_accent_color: Optional[int],
        message_colors: Optional[Sequence[int]],
        wallpaper: Optional[types.InputWallPaper | types.InputWallPaperSlug | types.InputWallPaperNoFile],
        wallpaper_settings: Optional[types.WallPaperSettings],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ThemeSettings(TLObject):
    """
    [Read `themeSettings` docs](https://core.telegram.org/constructor/themeSettings).

    Generated from the following TL definition:
    ```tl
    themeSettings#fa58b6d4 flags:# message_colors_animated:flags.2?true base_theme:BaseTheme accent_color:int outbox_accent_color:flags.3?int message_colors:flags.0?Vector<int> wallpaper:flags.1?WallPaper = ThemeSettings
    ```
    """
    def __new__(
        cls,
        message_colors_animated: bool,
        base_theme: types.BaseThemeClassic | types.BaseThemeDay | types.BaseThemeNight | types.BaseThemeTinted | types.BaseThemeArctic,
        accent_color: int,
        outbox_accent_color: Optional[int],
        message_colors: Optional[Sequence[int]],
        wallpaper: Optional[types.WallPaper | types.WallPaperNoFile],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebPageAttributeTheme(TLObject):
    """
    [Read `webPageAttributeTheme` docs](https://core.telegram.org/constructor/webPageAttributeTheme).

    Generated from the following TL definition:
    ```tl
    webPageAttributeTheme#54b56617 flags:# documents:flags.0?Vector<Document> settings:flags.1?ThemeSettings = WebPageAttribute
    ```
    """
    def __new__(
        cls,
        documents: Optional[Sequence[types.DocumentEmpty | types.Document]],
        settings: Optional[types.ThemeSettings],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebPageAttributeStory(TLObject):
    """
    [Read `webPageAttributeStory` docs](https://core.telegram.org/constructor/webPageAttributeStory).

    Generated from the following TL definition:
    ```tl
    webPageAttributeStory#2e94c3e7 flags:# peer:Peer id:int story:flags.0?StoryItem = WebPageAttribute
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        id: int,
        story: Optional[types.StoryItemDeleted | types.StoryItemSkipped | types.StoryItem],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebPageAttributeStickerSet(TLObject):
    """
    [Read `webPageAttributeStickerSet` docs](https://core.telegram.org/constructor/webPageAttributeStickerSet).

    Generated from the following TL definition:
    ```tl
    webPageAttributeStickerSet#50cc03d3 flags:# emojis:flags.0?true text_color:flags.1?true stickers:Vector<Document> = WebPageAttribute
    ```
    """
    def __new__(
        cls,
        emojis: bool,
        text_color: bool,
        stickers: Sequence[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebPageAttributeUniqueStarGift(TLObject):
    """
    [Read `webPageAttributeUniqueStarGift` docs](https://core.telegram.org/constructor/webPageAttributeUniqueStarGift).

    Generated from the following TL definition:
    ```tl
    webPageAttributeUniqueStarGift#cf6f6db8 gift:StarGift = WebPageAttribute
    ```
    """
    def __new__(
        cls,
        gift: types.StarGift | types.StarGiftUnique,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebPageAttributeStarGiftCollection(TLObject):
    """
    [Read `webPageAttributeStarGiftCollection` docs](https://core.telegram.org/constructor/webPageAttributeStarGiftCollection).

    Generated from the following TL definition:
    ```tl
    webPageAttributeStarGiftCollection#31cad303 icons:Vector<Document> = WebPageAttribute
    ```
    """
    def __new__(
        cls,
        icons: Sequence[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebPageAttributeStarGiftAuction(TLObject):
    """
    [Read `webPageAttributeStarGiftAuction` docs](https://core.telegram.org/constructor/webPageAttributeStarGiftAuction).

    Generated from the following TL definition:
    ```tl
    webPageAttributeStarGiftAuction#1c641c2 gift:StarGift end_date:int = WebPageAttribute
    ```
    """
    def __new__(
        cls,
        gift: types.StarGift | types.StarGiftUnique,
        end_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BankCardOpenUrl(TLObject):
    """
    [Read `bankCardOpenUrl` docs](https://core.telegram.org/constructor/bankCardOpenUrl).

    Generated from the following TL definition:
    ```tl
    bankCardOpenUrl#f568028a url:string name:string = BankCardOpenUrl
    ```
    """
    def __new__(
        cls,
        url: str,
        name: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DialogFilter(TLObject):
    """
    [Read `dialogFilter` docs](https://core.telegram.org/constructor/dialogFilter).

    Generated from the following TL definition:
    ```tl
    dialogFilter#aa472651 flags:# contacts:flags.0?true non_contacts:flags.1?true groups:flags.2?true broadcasts:flags.3?true bots:flags.4?true exclude_muted:flags.11?true exclude_read:flags.12?true exclude_archived:flags.13?true title_noanimate:flags.28?true id:int title:TextWithEntities emoticon:flags.25?string color:flags.27?int pinned_peers:Vector<InputPeer> include_peers:Vector<InputPeer> exclude_peers:Vector<InputPeer> = DialogFilter
    ```
    """
    def __new__(
        cls,
        contacts: bool,
        non_contacts: bool,
        groups: bool,
        broadcasts: bool,
        bots: bool,
        exclude_muted: bool,
        exclude_read: bool,
        exclude_archived: bool,
        title_noanimate: bool,
        id: int,
        title: types.TextWithEntities,
        emoticon: Optional[str],
        color: Optional[int],
        pinned_peers: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        include_peers: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        exclude_peers: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DialogFilterDefault(TLObject):
    """
    [Read `dialogFilterDefault` docs](https://core.telegram.org/constructor/dialogFilterDefault).

    Generated from the following TL definition:
    ```tl
    dialogFilterDefault#363293ae = DialogFilter
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DialogFilterChatlist(TLObject):
    """
    [Read `dialogFilterChatlist` docs](https://core.telegram.org/constructor/dialogFilterChatlist).

    Generated from the following TL definition:
    ```tl
    dialogFilterChatlist#96537bd7 flags:# has_my_invites:flags.26?true title_noanimate:flags.28?true id:int title:TextWithEntities emoticon:flags.25?string color:flags.27?int pinned_peers:Vector<InputPeer> include_peers:Vector<InputPeer> = DialogFilter
    ```
    """
    def __new__(
        cls,
        has_my_invites: bool,
        title_noanimate: bool,
        id: int,
        title: types.TextWithEntities,
        emoticon: Optional[str],
        color: Optional[int],
        pinned_peers: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        include_peers: Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DialogFilterSuggested(TLObject):
    """
    [Read `dialogFilterSuggested` docs](https://core.telegram.org/constructor/dialogFilterSuggested).

    Generated from the following TL definition:
    ```tl
    dialogFilterSuggested#77744d4a filter:DialogFilter description:string = DialogFilterSuggested
    ```
    """
    def __new__(
        cls,
        filter: types.DialogFilter | types.DialogFilterDefault | types.DialogFilterChatlist,
        description: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StatsDateRangeDays(TLObject):
    """
    [Read `statsDateRangeDays` docs](https://core.telegram.org/constructor/statsDateRangeDays).

    Generated from the following TL definition:
    ```tl
    statsDateRangeDays#b637edaf min_date:int max_date:int = StatsDateRangeDays
    ```
    """
    def __new__(
        cls,
        min_date: int,
        max_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StatsAbsValueAndPrev(TLObject):
    """
    [Read `statsAbsValueAndPrev` docs](https://core.telegram.org/constructor/statsAbsValueAndPrev).

    Generated from the following TL definition:
    ```tl
    statsAbsValueAndPrev#cb43acde current:double previous:double = StatsAbsValueAndPrev
    ```
    """
    def __new__(
        cls,
        current: float,
        previous: float,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StatsPercentValue(TLObject):
    """
    [Read `statsPercentValue` docs](https://core.telegram.org/constructor/statsPercentValue).

    Generated from the following TL definition:
    ```tl
    statsPercentValue#cbce2fe0 part:double total:double = StatsPercentValue
    ```
    """
    def __new__(
        cls,
        part: float,
        total: float,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StatsGraphAsync(TLObject):
    """
    [Read `statsGraphAsync` docs](https://core.telegram.org/constructor/statsGraphAsync).

    Generated from the following TL definition:
    ```tl
    statsGraphAsync#4a27eb2d token:string = StatsGraph
    ```
    """
    def __new__(
        cls,
        token: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StatsGraphError(TLObject):
    """
    [Read `statsGraphError` docs](https://core.telegram.org/constructor/statsGraphError).

    Generated from the following TL definition:
    ```tl
    statsGraphError#bedc9822 error:string = StatsGraph
    ```
    """
    def __new__(
        cls,
        error: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StatsGraph(TLObject):
    """
    [Read `statsGraph` docs](https://core.telegram.org/constructor/statsGraph).

    Generated from the following TL definition:
    ```tl
    statsGraph#8ea464b6 flags:# json:DataJSON zoom_token:flags.0?string = StatsGraph
    ```
    """
    def __new__(
        cls,
        json: types.DataJson,
        zoom_token: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class VideoSize(TLObject):
    """
    [Read `videoSize` docs](https://core.telegram.org/constructor/videoSize).

    Generated from the following TL definition:
    ```tl
    videoSize#de33b094 flags:# type:string w:int h:int size:int video_start_ts:flags.0?double = VideoSize
    ```
    """
    def __new__(
        cls,
        type: str,
        w: int,
        h: int,
        size: int,
        video_start_ts: Optional[float],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class VideoSizeEmojiMarkup(TLObject):
    """
    [Read `videoSizeEmojiMarkup` docs](https://core.telegram.org/constructor/videoSizeEmojiMarkup).

    Generated from the following TL definition:
    ```tl
    videoSizeEmojiMarkup#f85c413c emoji_id:long background_colors:Vector<int> = VideoSize
    ```
    """
    def __new__(
        cls,
        emoji_id: int,
        background_colors: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class VideoSizeStickerMarkup(TLObject):
    """
    [Read `videoSizeStickerMarkup` docs](https://core.telegram.org/constructor/videoSizeStickerMarkup).

    Generated from the following TL definition:
    ```tl
    videoSizeStickerMarkup#da082fe stickerset:InputStickerSet sticker_id:long background_colors:Vector<int> = VideoSize
    ```
    """
    def __new__(
        cls,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
        sticker_id: int,
        background_colors: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StatsGroupTopPoster(TLObject):
    """
    [Read `statsGroupTopPoster` docs](https://core.telegram.org/constructor/statsGroupTopPoster).

    Generated from the following TL definition:
    ```tl
    statsGroupTopPoster#9d04af9b user_id:long messages:int avg_chars:int = StatsGroupTopPoster
    ```
    """
    def __new__(
        cls,
        user_id: int,
        messages: int,
        avg_chars: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StatsGroupTopAdmin(TLObject):
    """
    [Read `statsGroupTopAdmin` docs](https://core.telegram.org/constructor/statsGroupTopAdmin).

    Generated from the following TL definition:
    ```tl
    statsGroupTopAdmin#d7584c87 user_id:long deleted:int kicked:int banned:int = StatsGroupTopAdmin
    ```
    """
    def __new__(
        cls,
        user_id: int,
        deleted: int,
        kicked: int,
        banned: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StatsGroupTopInviter(TLObject):
    """
    [Read `statsGroupTopInviter` docs](https://core.telegram.org/constructor/statsGroupTopInviter).

    Generated from the following TL definition:
    ```tl
    statsGroupTopInviter#535f779d user_id:long invitations:int = StatsGroupTopInviter
    ```
    """
    def __new__(
        cls,
        user_id: int,
        invitations: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GlobalPrivacySettings(TLObject):
    """
    [Read `globalPrivacySettings` docs](https://core.telegram.org/constructor/globalPrivacySettings).

    Generated from the following TL definition:
    ```tl
    globalPrivacySettings#fe41b34f flags:# archive_and_mute_new_noncontact_peers:flags.0?true keep_archived_unmuted:flags.1?true keep_archived_folders:flags.2?true hide_read_marks:flags.3?true new_noncontact_peers_require_premium:flags.4?true display_gifts_button:flags.7?true noncontact_peers_paid_stars:flags.5?long disallowed_gifts:flags.6?DisallowedGiftsSettings = GlobalPrivacySettings
    ```
    """
    def __new__(
        cls,
        archive_and_mute_new_noncontact_peers: bool,
        keep_archived_unmuted: bool,
        keep_archived_folders: bool,
        hide_read_marks: bool,
        new_noncontact_peers_require_premium: bool,
        display_gifts_button: bool,
        noncontact_peers_paid_stars: Optional[int],
        disallowed_gifts: Optional[types.DisallowedGiftsSettings],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageViews(TLObject):
    """
    [Read `messageViews` docs](https://core.telegram.org/constructor/messageViews).

    Generated from the following TL definition:
    ```tl
    messageViews#455b853d flags:# views:flags.0?int forwards:flags.1?int replies:flags.2?MessageReplies = MessageViews
    ```
    """
    def __new__(
        cls,
        views: Optional[int],
        forwards: Optional[int],
        replies: Optional[types.MessageReplies],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageReplyHeader(TLObject):
    """
    [Read `messageReplyHeader` docs](https://core.telegram.org/constructor/messageReplyHeader).

    Generated from the following TL definition:
    ```tl
    messageReplyHeader#6917560b flags:# reply_to_scheduled:flags.2?true forum_topic:flags.3?true quote:flags.9?true reply_to_msg_id:flags.4?int reply_to_peer_id:flags.0?Peer reply_from:flags.5?MessageFwdHeader reply_media:flags.8?MessageMedia reply_to_top_id:flags.1?int quote_text:flags.6?string quote_entities:flags.7?Vector<MessageEntity> quote_offset:flags.10?int todo_item_id:flags.11?int = MessageReplyHeader
    ```
    """
    def __new__(
        cls,
        reply_to_scheduled: bool,
        forum_topic: bool,
        quote: bool,
        reply_to_msg_id: Optional[int],
        reply_to_peer_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        reply_from: Optional[types.MessageFwdHeader],
        reply_media: Optional[types.MessageMediaEmpty | types.MessageMediaPhoto | types.MessageMediaGeo | types.MessageMediaContact | types.MessageMediaUnsupported | types.MessageMediaDocument | types.MessageMediaWebPage | types.MessageMediaVenue | types.MessageMediaGame | types.MessageMediaInvoice | types.MessageMediaGeoLive | types.MessageMediaPoll | types.MessageMediaDice | types.MessageMediaStory | types.MessageMediaGiveaway | types.MessageMediaGiveawayResults | types.MessageMediaPaidMedia | types.MessageMediaToDo | types.MessageMediaVideoStream],
        reply_to_top_id: Optional[int],
        quote_text: Optional[str],
        quote_entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        quote_offset: Optional[int],
        todo_item_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageReplyStoryHeader(TLObject):
    """
    [Read `messageReplyStoryHeader` docs](https://core.telegram.org/constructor/messageReplyStoryHeader).

    Generated from the following TL definition:
    ```tl
    messageReplyStoryHeader#e5af939 peer:Peer story_id:int = MessageReplyHeader
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        story_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageReplies(TLObject):
    """
    [Read `messageReplies` docs](https://core.telegram.org/constructor/messageReplies).

    Generated from the following TL definition:
    ```tl
    messageReplies#83d60fc2 flags:# comments:flags.0?true replies:int replies_pts:int recent_repliers:flags.1?Vector<Peer> channel_id:flags.0?long max_id:flags.2?int read_max_id:flags.3?int = MessageReplies
    ```
    """
    def __new__(
        cls,
        comments: bool,
        replies: int,
        replies_pts: int,
        recent_repliers: Optional[Sequence[types.PeerUser | types.PeerChat | types.PeerChannel]],
        channel_id: Optional[int],
        max_id: Optional[int],
        read_max_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerBlocked(TLObject):
    """
    [Read `peerBlocked` docs](https://core.telegram.org/constructor/peerBlocked).

    Generated from the following TL definition:
    ```tl
    peerBlocked#e8fd8014 peer_id:Peer date:int = PeerBlocked
    ```
    """
    def __new__(
        cls,
        peer_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupCallDiscarded(TLObject):
    """
    [Read `groupCallDiscarded` docs](https://core.telegram.org/constructor/groupCallDiscarded).

    Generated from the following TL definition:
    ```tl
    groupCallDiscarded#7780bcb4 id:long access_hash:long duration:int = GroupCall
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        duration: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupCall(TLObject):
    """
    [Read `groupCall` docs](https://core.telegram.org/constructor/groupCall).

    Generated from the following TL definition:
    ```tl
    groupCall#efb2b617 flags:# join_muted:flags.1?true can_change_join_muted:flags.2?true join_date_asc:flags.6?true schedule_start_subscribed:flags.8?true can_start_video:flags.9?true record_video_active:flags.11?true rtmp_stream:flags.12?true listeners_hidden:flags.13?true conference:flags.14?true creator:flags.15?true messages_enabled:flags.17?true can_change_messages_enabled:flags.18?true min:flags.19?true id:long access_hash:long participants_count:int title:flags.3?string stream_dc_id:flags.4?int record_start_date:flags.5?int schedule_date:flags.7?int unmuted_video_count:flags.10?int unmuted_video_limit:int version:int invite_link:flags.16?string send_paid_messages_stars:flags.20?long default_send_as:flags.21?Peer = GroupCall
    ```
    """
    def __new__(
        cls,
        join_muted: bool,
        can_change_join_muted: bool,
        join_date_asc: bool,
        schedule_start_subscribed: bool,
        can_start_video: bool,
        record_video_active: bool,
        rtmp_stream: bool,
        listeners_hidden: bool,
        conference: bool,
        creator: bool,
        messages_enabled: bool,
        can_change_messages_enabled: bool,
        min: bool,
        id: int,
        access_hash: int,
        participants_count: int,
        title: Optional[str],
        stream_dc_id: Optional[int],
        record_start_date: Optional[int],
        schedule_date: Optional[int],
        unmuted_video_count: Optional[int],
        unmuted_video_limit: int,
        version: int,
        invite_link: Optional[str],
        send_paid_messages_stars: Optional[int],
        default_send_as: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputGroupCall(TLObject):
    """
    [Read `inputGroupCall` docs](https://core.telegram.org/constructor/inputGroupCall).

    Generated from the following TL definition:
    ```tl
    inputGroupCall#d8aa840f id:long access_hash:long = InputGroupCall
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputGroupCallSlug(TLObject):
    """
    [Read `inputGroupCallSlug` docs](https://core.telegram.org/constructor/inputGroupCallSlug).

    Generated from the following TL definition:
    ```tl
    inputGroupCallSlug#fe06823f slug:string = InputGroupCall
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputGroupCallInviteMessage(TLObject):
    """
    [Read `inputGroupCallInviteMessage` docs](https://core.telegram.org/constructor/inputGroupCallInviteMessage).

    Generated from the following TL definition:
    ```tl
    inputGroupCallInviteMessage#8c10603f msg_id:int = InputGroupCall
    ```
    """
    def __new__(
        cls,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupCallParticipant(TLObject):
    """
    [Read `groupCallParticipant` docs](https://core.telegram.org/constructor/groupCallParticipant).

    Generated from the following TL definition:
    ```tl
    groupCallParticipant#2a3dc7ac flags:# muted:flags.0?true left:flags.1?true can_self_unmute:flags.2?true just_joined:flags.4?true versioned:flags.5?true min:flags.8?true muted_by_you:flags.9?true volume_by_admin:flags.10?true self:flags.12?true video_joined:flags.15?true peer:Peer date:int active_date:flags.3?int source:int volume:flags.7?int about:flags.11?string raise_hand_rating:flags.13?long video:flags.6?GroupCallParticipantVideo presentation:flags.14?GroupCallParticipantVideo paid_stars_total:flags.16?long = GroupCallParticipant
    ```
    """
    def __new__(
        cls,
        muted: bool,
        left: bool,
        can_self_unmute: bool,
        just_joined: bool,
        versioned: bool,
        min: bool,
        muted_by_you: bool,
        volume_by_admin: bool,
        is_self: bool,
        video_joined: bool,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        date: int,
        active_date: Optional[int],
        source: int,
        volume: Optional[int],
        about: Optional[str],
        raise_hand_rating: Optional[int],
        video: Optional[types.GroupCallParticipantVideo],
        presentation: Optional[types.GroupCallParticipantVideo],
        paid_stars_total: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InlineQueryPeerTypeSameBotPm(TLObject):
    """
    [Read `inlineQueryPeerTypeSameBotPM` docs](https://core.telegram.org/constructor/inlineQueryPeerTypeSameBotPM).

    Generated from the following TL definition:
    ```tl
    inlineQueryPeerTypeSameBotPM#3081ed9d = InlineQueryPeerType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InlineQueryPeerTypePm(TLObject):
    """
    [Read `inlineQueryPeerTypePM` docs](https://core.telegram.org/constructor/inlineQueryPeerTypePM).

    Generated from the following TL definition:
    ```tl
    inlineQueryPeerTypePM#833c0fac = InlineQueryPeerType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InlineQueryPeerTypeChat(TLObject):
    """
    [Read `inlineQueryPeerTypeChat` docs](https://core.telegram.org/constructor/inlineQueryPeerTypeChat).

    Generated from the following TL definition:
    ```tl
    inlineQueryPeerTypeChat#d766c50a = InlineQueryPeerType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InlineQueryPeerTypeMegagroup(TLObject):
    """
    [Read `inlineQueryPeerTypeMegagroup` docs](https://core.telegram.org/constructor/inlineQueryPeerTypeMegagroup).

    Generated from the following TL definition:
    ```tl
    inlineQueryPeerTypeMegagroup#5ec4be43 = InlineQueryPeerType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InlineQueryPeerTypeBroadcast(TLObject):
    """
    [Read `inlineQueryPeerTypeBroadcast` docs](https://core.telegram.org/constructor/inlineQueryPeerTypeBroadcast).

    Generated from the following TL definition:
    ```tl
    inlineQueryPeerTypeBroadcast#6334ee9a = InlineQueryPeerType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InlineQueryPeerTypeBotPm(TLObject):
    """
    [Read `inlineQueryPeerTypeBotPM` docs](https://core.telegram.org/constructor/inlineQueryPeerTypeBotPM).

    Generated from the following TL definition:
    ```tl
    inlineQueryPeerTypeBotPM#e3b2d0c = InlineQueryPeerType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatInviteImporter(TLObject):
    """
    [Read `chatInviteImporter` docs](https://core.telegram.org/constructor/chatInviteImporter).

    Generated from the following TL definition:
    ```tl
    chatInviteImporter#8c5adfd9 flags:# requested:flags.0?true via_chatlist:flags.3?true user_id:long date:int about:flags.2?string approved_by:flags.1?long = ChatInviteImporter
    ```
    """
    def __new__(
        cls,
        requested: bool,
        via_chatlist: bool,
        user_id: int,
        date: int,
        about: Optional[str],
        approved_by: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatAdminWithInvites(TLObject):
    """
    [Read `chatAdminWithInvites` docs](https://core.telegram.org/constructor/chatAdminWithInvites).

    Generated from the following TL definition:
    ```tl
    chatAdminWithInvites#f2ecef23 admin_id:long invites_count:int revoked_invites_count:int = ChatAdminWithInvites
    ```
    """
    def __new__(
        cls,
        admin_id: int,
        invites_count: int,
        revoked_invites_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupCallParticipantVideoSourceGroup(TLObject):
    """
    [Read `groupCallParticipantVideoSourceGroup` docs](https://core.telegram.org/constructor/groupCallParticipantVideoSourceGroup).

    Generated from the following TL definition:
    ```tl
    groupCallParticipantVideoSourceGroup#dcb118b7 semantics:string sources:Vector<int> = GroupCallParticipantVideoSourceGroup
    ```
    """
    def __new__(
        cls,
        semantics: str,
        sources: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupCallParticipantVideo(TLObject):
    """
    [Read `groupCallParticipantVideo` docs](https://core.telegram.org/constructor/groupCallParticipantVideo).

    Generated from the following TL definition:
    ```tl
    groupCallParticipantVideo#67753ac8 flags:# paused:flags.0?true endpoint:string source_groups:Vector<GroupCallParticipantVideoSourceGroup> audio_source:flags.1?int = GroupCallParticipantVideo
    ```
    """
    def __new__(
        cls,
        paused: bool,
        endpoint: str,
        source_groups: Sequence[types.GroupCallParticipantVideoSourceGroup],
        audio_source: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotCommandScopeDefault(TLObject):
    """
    [Read `botCommandScopeDefault` docs](https://core.telegram.org/constructor/botCommandScopeDefault).

    Generated from the following TL definition:
    ```tl
    botCommandScopeDefault#2f6cb2ab = BotCommandScope
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotCommandScopeUsers(TLObject):
    """
    [Read `botCommandScopeUsers` docs](https://core.telegram.org/constructor/botCommandScopeUsers).

    Generated from the following TL definition:
    ```tl
    botCommandScopeUsers#3c4f04d8 = BotCommandScope
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotCommandScopeChats(TLObject):
    """
    [Read `botCommandScopeChats` docs](https://core.telegram.org/constructor/botCommandScopeChats).

    Generated from the following TL definition:
    ```tl
    botCommandScopeChats#6fe1a881 = BotCommandScope
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotCommandScopeChatAdmins(TLObject):
    """
    [Read `botCommandScopeChatAdmins` docs](https://core.telegram.org/constructor/botCommandScopeChatAdmins).

    Generated from the following TL definition:
    ```tl
    botCommandScopeChatAdmins#b9aa606a = BotCommandScope
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotCommandScopePeer(TLObject):
    """
    [Read `botCommandScopePeer` docs](https://core.telegram.org/constructor/botCommandScopePeer).

    Generated from the following TL definition:
    ```tl
    botCommandScopePeer#db9d897d peer:InputPeer = BotCommandScope
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotCommandScopePeerAdmins(TLObject):
    """
    [Read `botCommandScopePeerAdmins` docs](https://core.telegram.org/constructor/botCommandScopePeerAdmins).

    Generated from the following TL definition:
    ```tl
    botCommandScopePeerAdmins#3fd863d1 peer:InputPeer = BotCommandScope
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotCommandScopePeerUser(TLObject):
    """
    [Read `botCommandScopePeerUser` docs](https://core.telegram.org/constructor/botCommandScopePeerUser).

    Generated from the following TL definition:
    ```tl
    botCommandScopePeerUser#a1321f3 peer:InputPeer user_id:InputUser = BotCommandScope
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatTheme(TLObject):
    """
    [Read `chatTheme` docs](https://core.telegram.org/constructor/chatTheme).

    Generated from the following TL definition:
    ```tl
    chatTheme#c3dffc04 emoticon:string = ChatTheme
    ```
    """
    def __new__(
        cls,
        emoticon: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatThemeUniqueGift(TLObject):
    """
    [Read `chatThemeUniqueGift` docs](https://core.telegram.org/constructor/chatThemeUniqueGift).

    Generated from the following TL definition:
    ```tl
    chatThemeUniqueGift#3458f9c8 gift:StarGift theme_settings:Vector<ThemeSettings> = ChatTheme
    ```
    """
    def __new__(
        cls,
        gift: types.StarGift | types.StarGiftUnique,
        theme_settings: Sequence[types.ThemeSettings],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SponsoredMessage(TLObject):
    """
    [Read `sponsoredMessage` docs](https://core.telegram.org/constructor/sponsoredMessage).

    Generated from the following TL definition:
    ```tl
    sponsoredMessage#7dbf8673 flags:# recommended:flags.5?true can_report:flags.12?true random_id:bytes url:string title:string message:string entities:flags.1?Vector<MessageEntity> photo:flags.6?Photo media:flags.14?MessageMedia color:flags.13?PeerColor button_text:string sponsor_info:flags.7?string additional_info:flags.8?string min_display_duration:flags.15?int max_display_duration:flags.15?int = SponsoredMessage
    ```
    """
    def __new__(
        cls,
        recommended: bool,
        can_report: bool,
        random_id: bytes,
        url: str,
        title: str,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        photo: Optional[types.PhotoEmpty | types.Photo],
        media: Optional[types.MessageMediaEmpty | types.MessageMediaPhoto | types.MessageMediaGeo | types.MessageMediaContact | types.MessageMediaUnsupported | types.MessageMediaDocument | types.MessageMediaWebPage | types.MessageMediaVenue | types.MessageMediaGame | types.MessageMediaInvoice | types.MessageMediaGeoLive | types.MessageMediaPoll | types.MessageMediaDice | types.MessageMediaStory | types.MessageMediaGiveaway | types.MessageMediaGiveawayResults | types.MessageMediaPaidMedia | types.MessageMediaToDo | types.MessageMediaVideoStream],
        color: Optional[types.PeerColor | types.PeerColorCollectible | types.InputPeerColorCollectible],
        button_text: str,
        sponsor_info: Optional[str],
        additional_info: Optional[str],
        min_display_duration: Optional[int],
        max_display_duration: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchResultsCalendarPeriod(TLObject):
    """
    [Read `searchResultsCalendarPeriod` docs](https://core.telegram.org/constructor/searchResultsCalendarPeriod).

    Generated from the following TL definition:
    ```tl
    searchResultsCalendarPeriod#c9b0539f date:int min_msg_id:int max_msg_id:int count:int = SearchResultsCalendarPeriod
    ```
    """
    def __new__(
        cls,
        date: int,
        min_msg_id: int,
        max_msg_id: int,
        count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchResultPosition(TLObject):
    """
    [Read `searchResultPosition` docs](https://core.telegram.org/constructor/searchResultPosition).

    Generated from the following TL definition:
    ```tl
    searchResultPosition#7f648b67 msg_id:int date:int offset:int = SearchResultsPosition
    ```
    """
    def __new__(
        cls,
        msg_id: int,
        date: int,
        offset: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReactionCount(TLObject):
    """
    [Read `reactionCount` docs](https://core.telegram.org/constructor/reactionCount).

    Generated from the following TL definition:
    ```tl
    reactionCount#a3d1cb80 flags:# chosen_order:flags.0?int reaction:Reaction count:int = ReactionCount
    ```
    """
    def __new__(
        cls,
        chosen_order: Optional[int],
        reaction: types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid,
        count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageReactions(TLObject):
    """
    [Read `messageReactions` docs](https://core.telegram.org/constructor/messageReactions).

    Generated from the following TL definition:
    ```tl
    messageReactions#a339f0b flags:# min:flags.0?true can_see_list:flags.2?true reactions_as_tags:flags.3?true results:Vector<ReactionCount> recent_reactions:flags.1?Vector<MessagePeerReaction> top_reactors:flags.4?Vector<MessageReactor> = MessageReactions
    ```
    """
    def __new__(
        cls,
        min: bool,
        can_see_list: bool,
        reactions_as_tags: bool,
        results: Sequence[types.ReactionCount],
        recent_reactions: Optional[Sequence[types.MessagePeerReaction]],
        top_reactors: Optional[Sequence[types.MessageReactor]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AvailableReaction(TLObject):
    """
    [Read `availableReaction` docs](https://core.telegram.org/constructor/availableReaction).

    Generated from the following TL definition:
    ```tl
    availableReaction#c077ec01 flags:# inactive:flags.0?true premium:flags.2?true reaction:string title:string static_icon:Document appear_animation:Document select_animation:Document activate_animation:Document effect_animation:Document around_animation:flags.1?Document center_icon:flags.1?Document = AvailableReaction
    ```
    """
    def __new__(
        cls,
        inactive: bool,
        premium: bool,
        reaction: str,
        title: str,
        static_icon: types.DocumentEmpty | types.Document,
        appear_animation: types.DocumentEmpty | types.Document,
        select_animation: types.DocumentEmpty | types.Document,
        activate_animation: types.DocumentEmpty | types.Document,
        effect_animation: types.DocumentEmpty | types.Document,
        around_animation: Optional[types.DocumentEmpty | types.Document],
        center_icon: Optional[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessagePeerReaction(TLObject):
    """
    [Read `messagePeerReaction` docs](https://core.telegram.org/constructor/messagePeerReaction).

    Generated from the following TL definition:
    ```tl
    messagePeerReaction#8c79b63c flags:# big:flags.0?true unread:flags.1?true my:flags.2?true peer_id:Peer date:int reaction:Reaction = MessagePeerReaction
    ```
    """
    def __new__(
        cls,
        big: bool,
        unread: bool,
        my: bool,
        peer_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        date: int,
        reaction: types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupCallStreamChannel(TLObject):
    """
    [Read `groupCallStreamChannel` docs](https://core.telegram.org/constructor/groupCallStreamChannel).

    Generated from the following TL definition:
    ```tl
    groupCallStreamChannel#80eb48af channel:int scale:int last_timestamp_ms:long = GroupCallStreamChannel
    ```
    """
    def __new__(
        cls,
        channel: int,
        scale: int,
        last_timestamp_ms: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AttachMenuBotIconColor(TLObject):
    """
    [Read `attachMenuBotIconColor` docs](https://core.telegram.org/constructor/attachMenuBotIconColor).

    Generated from the following TL definition:
    ```tl
    attachMenuBotIconColor#4576f3f0 name:string color:int = AttachMenuBotIconColor
    ```
    """
    def __new__(
        cls,
        name: str,
        color: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AttachMenuBotIcon(TLObject):
    """
    [Read `attachMenuBotIcon` docs](https://core.telegram.org/constructor/attachMenuBotIcon).

    Generated from the following TL definition:
    ```tl
    attachMenuBotIcon#b2a7386b flags:# name:string icon:Document colors:flags.0?Vector<AttachMenuBotIconColor> = AttachMenuBotIcon
    ```
    """
    def __new__(
        cls,
        name: str,
        icon: types.DocumentEmpty | types.Document,
        colors: Optional[Sequence[types.AttachMenuBotIconColor]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AttachMenuBot(TLObject):
    """
    [Read `attachMenuBot` docs](https://core.telegram.org/constructor/attachMenuBot).

    Generated from the following TL definition:
    ```tl
    attachMenuBot#d90d8dfe flags:# inactive:flags.0?true has_settings:flags.1?true request_write_access:flags.2?true show_in_attach_menu:flags.3?true show_in_side_menu:flags.4?true side_menu_disclaimer_needed:flags.5?true bot_id:long short_name:string peer_types:flags.3?Vector<AttachMenuPeerType> icons:Vector<AttachMenuBotIcon> = AttachMenuBot
    ```
    """
    def __new__(
        cls,
        inactive: bool,
        has_settings: bool,
        request_write_access: bool,
        show_in_attach_menu: bool,
        show_in_side_menu: bool,
        side_menu_disclaimer_needed: bool,
        bot_id: int,
        short_name: str,
        peer_types: Optional[Sequence[types.AttachMenuPeerTypeSameBotPm | types.AttachMenuPeerTypeBotPm | types.AttachMenuPeerTypePm | types.AttachMenuPeerTypeChat | types.AttachMenuPeerTypeBroadcast]],
        icons: Sequence[types.AttachMenuBotIcon],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AttachMenuBotsNotModified(TLObject):
    """
    [Read `attachMenuBotsNotModified` docs](https://core.telegram.org/constructor/attachMenuBotsNotModified).

    Generated from the following TL definition:
    ```tl
    attachMenuBotsNotModified#f1d88a5c = AttachMenuBots
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AttachMenuBots(TLObject):
    """
    [Read `attachMenuBots` docs](https://core.telegram.org/constructor/attachMenuBots).

    Generated from the following TL definition:
    ```tl
    attachMenuBots#3c4301c0 hash:long bots:Vector<AttachMenuBot> users:Vector<User> = AttachMenuBots
    ```
    """
    def __new__(
        cls,
        hash: int,
        bots: Sequence[types.AttachMenuBot],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AttachMenuBotsBot(TLObject):
    """
    [Read `attachMenuBotsBot` docs](https://core.telegram.org/constructor/attachMenuBotsBot).

    Generated from the following TL definition:
    ```tl
    attachMenuBotsBot#93bf667f bot:AttachMenuBot users:Vector<User> = AttachMenuBotsBot
    ```
    """
    def __new__(
        cls,
        bot: types.AttachMenuBot,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebViewResultUrl(TLObject):
    """
    [Read `webViewResultUrl` docs](https://core.telegram.org/constructor/webViewResultUrl).

    Generated from the following TL definition:
    ```tl
    webViewResultUrl#4d22ff98 flags:# fullsize:flags.1?true fullscreen:flags.2?true query_id:flags.0?long url:string = WebViewResult
    ```
    """
    def __new__(
        cls,
        fullsize: bool,
        fullscreen: bool,
        query_id: Optional[int],
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebViewMessageSent(TLObject):
    """
    [Read `webViewMessageSent` docs](https://core.telegram.org/constructor/webViewMessageSent).

    Generated from the following TL definition:
    ```tl
    webViewMessageSent#c94511c flags:# msg_id:flags.0?InputBotInlineMessageID = WebViewMessageSent
    ```
    """
    def __new__(
        cls,
        msg_id: Optional[types.InputBotInlineMessageId | types.InputBotInlineMessageId64],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotMenuButtonDefault(TLObject):
    """
    [Read `botMenuButtonDefault` docs](https://core.telegram.org/constructor/botMenuButtonDefault).

    Generated from the following TL definition:
    ```tl
    botMenuButtonDefault#7533a588 = BotMenuButton
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotMenuButtonCommands(TLObject):
    """
    [Read `botMenuButtonCommands` docs](https://core.telegram.org/constructor/botMenuButtonCommands).

    Generated from the following TL definition:
    ```tl
    botMenuButtonCommands#4258c205 = BotMenuButton
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotMenuButton(TLObject):
    """
    [Read `botMenuButton` docs](https://core.telegram.org/constructor/botMenuButton).

    Generated from the following TL definition:
    ```tl
    botMenuButton#c7b57ce6 text:string url:string = BotMenuButton
    ```
    """
    def __new__(
        cls,
        text: str,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class NotificationSoundDefault(TLObject):
    """
    [Read `notificationSoundDefault` docs](https://core.telegram.org/constructor/notificationSoundDefault).

    Generated from the following TL definition:
    ```tl
    notificationSoundDefault#97e8bebe = NotificationSound
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class NotificationSoundNone(TLObject):
    """
    [Read `notificationSoundNone` docs](https://core.telegram.org/constructor/notificationSoundNone).

    Generated from the following TL definition:
    ```tl
    notificationSoundNone#6f0c34df = NotificationSound
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class NotificationSoundLocal(TLObject):
    """
    [Read `notificationSoundLocal` docs](https://core.telegram.org/constructor/notificationSoundLocal).

    Generated from the following TL definition:
    ```tl
    notificationSoundLocal#830b9ae4 title:string data:string = NotificationSound
    ```
    """
    def __new__(
        cls,
        title: str,
        data: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class NotificationSoundRingtone(TLObject):
    """
    [Read `notificationSoundRingtone` docs](https://core.telegram.org/constructor/notificationSoundRingtone).

    Generated from the following TL definition:
    ```tl
    notificationSoundRingtone#ff6c8049 id:long = NotificationSound
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AttachMenuPeerTypeSameBotPm(TLObject):
    """
    [Read `attachMenuPeerTypeSameBotPM` docs](https://core.telegram.org/constructor/attachMenuPeerTypeSameBotPM).

    Generated from the following TL definition:
    ```tl
    attachMenuPeerTypeSameBotPM#7d6be90e = AttachMenuPeerType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AttachMenuPeerTypeBotPm(TLObject):
    """
    [Read `attachMenuPeerTypeBotPM` docs](https://core.telegram.org/constructor/attachMenuPeerTypeBotPM).

    Generated from the following TL definition:
    ```tl
    attachMenuPeerTypeBotPM#c32bfa1a = AttachMenuPeerType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AttachMenuPeerTypePm(TLObject):
    """
    [Read `attachMenuPeerTypePM` docs](https://core.telegram.org/constructor/attachMenuPeerTypePM).

    Generated from the following TL definition:
    ```tl
    attachMenuPeerTypePM#f146d31f = AttachMenuPeerType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AttachMenuPeerTypeChat(TLObject):
    """
    [Read `attachMenuPeerTypeChat` docs](https://core.telegram.org/constructor/attachMenuPeerTypeChat).

    Generated from the following TL definition:
    ```tl
    attachMenuPeerTypeChat#509113f = AttachMenuPeerType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AttachMenuPeerTypeBroadcast(TLObject):
    """
    [Read `attachMenuPeerTypeBroadcast` docs](https://core.telegram.org/constructor/attachMenuPeerTypeBroadcast).

    Generated from the following TL definition:
    ```tl
    attachMenuPeerTypeBroadcast#7bfbdefc = AttachMenuPeerType
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoiceMessage(TLObject):
    """
    [Read `inputInvoiceMessage` docs](https://core.telegram.org/constructor/inputInvoiceMessage).

    Generated from the following TL definition:
    ```tl
    inputInvoiceMessage#c5b56859 peer:InputPeer msg_id:int = InputInvoice
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoiceSlug(TLObject):
    """
    [Read `inputInvoiceSlug` docs](https://core.telegram.org/constructor/inputInvoiceSlug).

    Generated from the following TL definition:
    ```tl
    inputInvoiceSlug#c326caef slug:string = InputInvoice
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoicePremiumGiftCode(TLObject):
    """
    [Read `inputInvoicePremiumGiftCode` docs](https://core.telegram.org/constructor/inputInvoicePremiumGiftCode).

    Generated from the following TL definition:
    ```tl
    inputInvoicePremiumGiftCode#98986c0d purpose:InputStorePaymentPurpose option:PremiumGiftCodeOption = InputInvoice
    ```
    """
    def __new__(
        cls,
        purpose: types.InputStorePaymentPremiumSubscription | types.InputStorePaymentGiftPremium | types.InputStorePaymentPremiumGiftCode | types.InputStorePaymentPremiumGiveaway | types.InputStorePaymentStarsTopup | types.InputStorePaymentStarsGift | types.InputStorePaymentStarsGiveaway | types.InputStorePaymentAuthCode,
        option: types.PremiumGiftCodeOption,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoiceStars(TLObject):
    """
    [Read `inputInvoiceStars` docs](https://core.telegram.org/constructor/inputInvoiceStars).

    Generated from the following TL definition:
    ```tl
    inputInvoiceStars#65f00ce3 purpose:InputStorePaymentPurpose = InputInvoice
    ```
    """
    def __new__(
        cls,
        purpose: types.InputStorePaymentPremiumSubscription | types.InputStorePaymentGiftPremium | types.InputStorePaymentPremiumGiftCode | types.InputStorePaymentPremiumGiveaway | types.InputStorePaymentStarsTopup | types.InputStorePaymentStarsGift | types.InputStorePaymentStarsGiveaway | types.InputStorePaymentAuthCode,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoiceChatInviteSubscription(TLObject):
    """
    [Read `inputInvoiceChatInviteSubscription` docs](https://core.telegram.org/constructor/inputInvoiceChatInviteSubscription).

    Generated from the following TL definition:
    ```tl
    inputInvoiceChatInviteSubscription#34e793f1 hash:string = InputInvoice
    ```
    """
    def __new__(
        cls,
        hash: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoiceStarGift(TLObject):
    """
    [Read `inputInvoiceStarGift` docs](https://core.telegram.org/constructor/inputInvoiceStarGift).

    Generated from the following TL definition:
    ```tl
    inputInvoiceStarGift#e8625e92 flags:# hide_name:flags.0?true include_upgrade:flags.2?true peer:InputPeer gift_id:long message:flags.1?TextWithEntities = InputInvoice
    ```
    """
    def __new__(
        cls,
        hide_name: bool,
        include_upgrade: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        gift_id: int,
        message: Optional[types.TextWithEntities],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoiceStarGiftUpgrade(TLObject):
    """
    [Read `inputInvoiceStarGiftUpgrade` docs](https://core.telegram.org/constructor/inputInvoiceStarGiftUpgrade).

    Generated from the following TL definition:
    ```tl
    inputInvoiceStarGiftUpgrade#4d818d5d flags:# keep_original_details:flags.0?true stargift:InputSavedStarGift = InputInvoice
    ```
    """
    def __new__(
        cls,
        keep_original_details: bool,
        stargift: types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoiceStarGiftTransfer(TLObject):
    """
    [Read `inputInvoiceStarGiftTransfer` docs](https://core.telegram.org/constructor/inputInvoiceStarGiftTransfer).

    Generated from the following TL definition:
    ```tl
    inputInvoiceStarGiftTransfer#4a5f5bd9 stargift:InputSavedStarGift to_id:InputPeer = InputInvoice
    ```
    """
    def __new__(
        cls,
        stargift: types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug,
        to_id: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoicePremiumGiftStars(TLObject):
    """
    [Read `inputInvoicePremiumGiftStars` docs](https://core.telegram.org/constructor/inputInvoicePremiumGiftStars).

    Generated from the following TL definition:
    ```tl
    inputInvoicePremiumGiftStars#dabab2ef flags:# user_id:InputUser months:int message:flags.0?TextWithEntities = InputInvoice
    ```
    """
    def __new__(
        cls,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        months: int,
        message: Optional[types.TextWithEntities],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoiceBusinessBotTransferStars(TLObject):
    """
    [Read `inputInvoiceBusinessBotTransferStars` docs](https://core.telegram.org/constructor/inputInvoiceBusinessBotTransferStars).

    Generated from the following TL definition:
    ```tl
    inputInvoiceBusinessBotTransferStars#f4997e42 bot:InputUser stars:long = InputInvoice
    ```
    """
    def __new__(
        cls,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        stars: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoiceStarGiftResale(TLObject):
    """
    [Read `inputInvoiceStarGiftResale` docs](https://core.telegram.org/constructor/inputInvoiceStarGiftResale).

    Generated from the following TL definition:
    ```tl
    inputInvoiceStarGiftResale#c39f5324 flags:# ton:flags.0?true slug:string to_id:InputPeer = InputInvoice
    ```
    """
    def __new__(
        cls,
        ton: bool,
        slug: str,
        to_id: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoiceStarGiftPrepaidUpgrade(TLObject):
    """
    [Read `inputInvoiceStarGiftPrepaidUpgrade` docs](https://core.telegram.org/constructor/inputInvoiceStarGiftPrepaidUpgrade).

    Generated from the following TL definition:
    ```tl
    inputInvoiceStarGiftPrepaidUpgrade#9a0b48b8 peer:InputPeer hash:string = InputInvoice
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        hash: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoicePremiumAuthCode(TLObject):
    """
    [Read `inputInvoicePremiumAuthCode` docs](https://core.telegram.org/constructor/inputInvoicePremiumAuthCode).

    Generated from the following TL definition:
    ```tl
    inputInvoicePremiumAuthCode#3e77f614 purpose:InputStorePaymentPurpose = InputInvoice
    ```
    """
    def __new__(
        cls,
        purpose: types.InputStorePaymentPremiumSubscription | types.InputStorePaymentGiftPremium | types.InputStorePaymentPremiumGiftCode | types.InputStorePaymentPremiumGiveaway | types.InputStorePaymentStarsTopup | types.InputStorePaymentStarsGift | types.InputStorePaymentStarsGiveaway | types.InputStorePaymentAuthCode,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoiceStarGiftDropOriginalDetails(TLObject):
    """
    [Read `inputInvoiceStarGiftDropOriginalDetails` docs](https://core.telegram.org/constructor/inputInvoiceStarGiftDropOriginalDetails).

    Generated from the following TL definition:
    ```tl
    inputInvoiceStarGiftDropOriginalDetails#923d8d1 stargift:InputSavedStarGift = InputInvoice
    ```
    """
    def __new__(
        cls,
        stargift: types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputInvoiceStarGiftAuctionBid(TLObject):
    """
    [Read `inputInvoiceStarGiftAuctionBid` docs](https://core.telegram.org/constructor/inputInvoiceStarGiftAuctionBid).

    Generated from the following TL definition:
    ```tl
    inputInvoiceStarGiftAuctionBid#1ecafa10 flags:# hide_name:flags.0?true update_bid:flags.2?true peer:flags.3?InputPeer gift_id:long bid_amount:long message:flags.1?TextWithEntities = InputInvoice
    ```
    """
    def __new__(
        cls,
        hide_name: bool,
        update_bid: bool,
        peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        gift_id: int,
        bid_amount: int,
        message: Optional[types.TextWithEntities],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStorePaymentPremiumSubscription(TLObject):
    """
    [Read `inputStorePaymentPremiumSubscription` docs](https://core.telegram.org/constructor/inputStorePaymentPremiumSubscription).

    Generated from the following TL definition:
    ```tl
    inputStorePaymentPremiumSubscription#a6751e66 flags:# restore:flags.0?true upgrade:flags.1?true = InputStorePaymentPurpose
    ```
    """
    def __new__(
        cls,
        restore: bool,
        upgrade: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStorePaymentGiftPremium(TLObject):
    """
    [Read `inputStorePaymentGiftPremium` docs](https://core.telegram.org/constructor/inputStorePaymentGiftPremium).

    Generated from the following TL definition:
    ```tl
    inputStorePaymentGiftPremium#616f7fe8 user_id:InputUser currency:string amount:long = InputStorePaymentPurpose
    ```
    """
    def __new__(
        cls,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        currency: str,
        amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStorePaymentPremiumGiftCode(TLObject):
    """
    [Read `inputStorePaymentPremiumGiftCode` docs](https://core.telegram.org/constructor/inputStorePaymentPremiumGiftCode).

    Generated from the following TL definition:
    ```tl
    inputStorePaymentPremiumGiftCode#fb790393 flags:# users:Vector<InputUser> boost_peer:flags.0?InputPeer currency:string amount:long message:flags.1?TextWithEntities = InputStorePaymentPurpose
    ```
    """
    def __new__(
        cls,
        users: Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
        boost_peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        currency: str,
        amount: int,
        message: Optional[types.TextWithEntities],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStorePaymentPremiumGiveaway(TLObject):
    """
    [Read `inputStorePaymentPremiumGiveaway` docs](https://core.telegram.org/constructor/inputStorePaymentPremiumGiveaway).

    Generated from the following TL definition:
    ```tl
    inputStorePaymentPremiumGiveaway#160544ca flags:# only_new_subscribers:flags.0?true winners_are_visible:flags.3?true boost_peer:InputPeer additional_peers:flags.1?Vector<InputPeer> countries_iso2:flags.2?Vector<string> prize_description:flags.4?string random_id:long until_date:int currency:string amount:long = InputStorePaymentPurpose
    ```
    """
    def __new__(
        cls,
        only_new_subscribers: bool,
        winners_are_visible: bool,
        boost_peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        additional_peers: Optional[Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage]],
        countries_iso2: Optional[Sequence[str]],
        prize_description: Optional[str],
        random_id: int,
        until_date: int,
        currency: str,
        amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStorePaymentStarsTopup(TLObject):
    """
    [Read `inputStorePaymentStarsTopup` docs](https://core.telegram.org/constructor/inputStorePaymentStarsTopup).

    Generated from the following TL definition:
    ```tl
    inputStorePaymentStarsTopup#f9a2a6cb flags:# stars:long currency:string amount:long spend_purpose_peer:flags.0?InputPeer = InputStorePaymentPurpose
    ```
    """
    def __new__(
        cls,
        stars: int,
        currency: str,
        amount: int,
        spend_purpose_peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStorePaymentStarsGift(TLObject):
    """
    [Read `inputStorePaymentStarsGift` docs](https://core.telegram.org/constructor/inputStorePaymentStarsGift).

    Generated from the following TL definition:
    ```tl
    inputStorePaymentStarsGift#1d741ef7 user_id:InputUser stars:long currency:string amount:long = InputStorePaymentPurpose
    ```
    """
    def __new__(
        cls,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        stars: int,
        currency: str,
        amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStorePaymentStarsGiveaway(TLObject):
    """
    [Read `inputStorePaymentStarsGiveaway` docs](https://core.telegram.org/constructor/inputStorePaymentStarsGiveaway).

    Generated from the following TL definition:
    ```tl
    inputStorePaymentStarsGiveaway#751f08fa flags:# only_new_subscribers:flags.0?true winners_are_visible:flags.3?true stars:long boost_peer:InputPeer additional_peers:flags.1?Vector<InputPeer> countries_iso2:flags.2?Vector<string> prize_description:flags.4?string random_id:long until_date:int currency:string amount:long users:int = InputStorePaymentPurpose
    ```
    """
    def __new__(
        cls,
        only_new_subscribers: bool,
        winners_are_visible: bool,
        stars: int,
        boost_peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        additional_peers: Optional[Sequence[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage]],
        countries_iso2: Optional[Sequence[str]],
        prize_description: Optional[str],
        random_id: int,
        until_date: int,
        currency: str,
        amount: int,
        users: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStorePaymentAuthCode(TLObject):
    """
    [Read `inputStorePaymentAuthCode` docs](https://core.telegram.org/constructor/inputStorePaymentAuthCode).

    Generated from the following TL definition:
    ```tl
    inputStorePaymentAuthCode#9bb2636d flags:# restore:flags.0?true phone_number:string phone_code_hash:string currency:string amount:long = InputStorePaymentPurpose
    ```
    """
    def __new__(
        cls,
        restore: bool,
        phone_number: str,
        phone_code_hash: str,
        currency: str,
        amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaymentFormMethod(TLObject):
    """
    [Read `paymentFormMethod` docs](https://core.telegram.org/constructor/paymentFormMethod).

    Generated from the following TL definition:
    ```tl
    paymentFormMethod#88f8f21b url:string title:string = PaymentFormMethod
    ```
    """
    def __new__(
        cls,
        url: str,
        title: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiStatusEmpty(TLObject):
    """
    [Read `emojiStatusEmpty` docs](https://core.telegram.org/constructor/emojiStatusEmpty).

    Generated from the following TL definition:
    ```tl
    emojiStatusEmpty#2de11aae = EmojiStatus
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiStatus(TLObject):
    """
    [Read `emojiStatus` docs](https://core.telegram.org/constructor/emojiStatus).

    Generated from the following TL definition:
    ```tl
    emojiStatus#e7ff068a flags:# document_id:long until:flags.0?int = EmojiStatus
    ```
    """
    def __new__(
        cls,
        document_id: int,
        until: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiStatusCollectible(TLObject):
    """
    [Read `emojiStatusCollectible` docs](https://core.telegram.org/constructor/emojiStatusCollectible).

    Generated from the following TL definition:
    ```tl
    emojiStatusCollectible#7184603b flags:# collectible_id:long document_id:long title:string slug:string pattern_document_id:long center_color:int edge_color:int pattern_color:int text_color:int until:flags.0?int = EmojiStatus
    ```
    """
    def __new__(
        cls,
        collectible_id: int,
        document_id: int,
        title: str,
        slug: str,
        pattern_document_id: int,
        center_color: int,
        edge_color: int,
        pattern_color: int,
        text_color: int,
        until: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputEmojiStatusCollectible(TLObject):
    """
    [Read `inputEmojiStatusCollectible` docs](https://core.telegram.org/constructor/inputEmojiStatusCollectible).

    Generated from the following TL definition:
    ```tl
    inputEmojiStatusCollectible#7141dbf flags:# collectible_id:long until:flags.0?int = EmojiStatus
    ```
    """
    def __new__(
        cls,
        collectible_id: int,
        until: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReactionEmpty(TLObject):
    """
    [Read `reactionEmpty` docs](https://core.telegram.org/constructor/reactionEmpty).

    Generated from the following TL definition:
    ```tl
    reactionEmpty#79f5d419 = Reaction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReactionEmoji(TLObject):
    """
    [Read `reactionEmoji` docs](https://core.telegram.org/constructor/reactionEmoji).

    Generated from the following TL definition:
    ```tl
    reactionEmoji#1b2286b8 emoticon:string = Reaction
    ```
    """
    def __new__(
        cls,
        emoticon: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReactionCustomEmoji(TLObject):
    """
    [Read `reactionCustomEmoji` docs](https://core.telegram.org/constructor/reactionCustomEmoji).

    Generated from the following TL definition:
    ```tl
    reactionCustomEmoji#8935fc73 document_id:long = Reaction
    ```
    """
    def __new__(
        cls,
        document_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReactionPaid(TLObject):
    """
    [Read `reactionPaid` docs](https://core.telegram.org/constructor/reactionPaid).

    Generated from the following TL definition:
    ```tl
    reactionPaid#523da4eb = Reaction
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatReactionsNone(TLObject):
    """
    [Read `chatReactionsNone` docs](https://core.telegram.org/constructor/chatReactionsNone).

    Generated from the following TL definition:
    ```tl
    chatReactionsNone#eafc32bc = ChatReactions
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatReactionsAll(TLObject):
    """
    [Read `chatReactionsAll` docs](https://core.telegram.org/constructor/chatReactionsAll).

    Generated from the following TL definition:
    ```tl
    chatReactionsAll#52928bca flags:# allow_custom:flags.0?true = ChatReactions
    ```
    """
    def __new__(
        cls,
        allow_custom: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChatReactionsSome(TLObject):
    """
    [Read `chatReactionsSome` docs](https://core.telegram.org/constructor/chatReactionsSome).

    Generated from the following TL definition:
    ```tl
    chatReactionsSome#661d4037 reactions:Vector<Reaction> = ChatReactions
    ```
    """
    def __new__(
        cls,
        reactions: Sequence[types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmailVerifyPurposeLoginSetup(TLObject):
    """
    [Read `emailVerifyPurposeLoginSetup` docs](https://core.telegram.org/constructor/emailVerifyPurposeLoginSetup).

    Generated from the following TL definition:
    ```tl
    emailVerifyPurposeLoginSetup#4345be73 phone_number:string phone_code_hash:string = EmailVerifyPurpose
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        phone_code_hash: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmailVerifyPurposeLoginChange(TLObject):
    """
    [Read `emailVerifyPurposeLoginChange` docs](https://core.telegram.org/constructor/emailVerifyPurposeLoginChange).

    Generated from the following TL definition:
    ```tl
    emailVerifyPurposeLoginChange#527d22eb = EmailVerifyPurpose
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmailVerifyPurposePassport(TLObject):
    """
    [Read `emailVerifyPurposePassport` docs](https://core.telegram.org/constructor/emailVerifyPurposePassport).

    Generated from the following TL definition:
    ```tl
    emailVerifyPurposePassport#bbf51685 = EmailVerifyPurpose
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmailVerificationCode(TLObject):
    """
    [Read `emailVerificationCode` docs](https://core.telegram.org/constructor/emailVerificationCode).

    Generated from the following TL definition:
    ```tl
    emailVerificationCode#922e55a9 code:string = EmailVerification
    ```
    """
    def __new__(
        cls,
        code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmailVerificationGoogle(TLObject):
    """
    [Read `emailVerificationGoogle` docs](https://core.telegram.org/constructor/emailVerificationGoogle).

    Generated from the following TL definition:
    ```tl
    emailVerificationGoogle#db909ec2 token:string = EmailVerification
    ```
    """
    def __new__(
        cls,
        token: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmailVerificationApple(TLObject):
    """
    [Read `emailVerificationApple` docs](https://core.telegram.org/constructor/emailVerificationApple).

    Generated from the following TL definition:
    ```tl
    emailVerificationApple#96d074fd token:string = EmailVerification
    ```
    """
    def __new__(
        cls,
        token: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PremiumSubscriptionOption(TLObject):
    """
    [Read `premiumSubscriptionOption` docs](https://core.telegram.org/constructor/premiumSubscriptionOption).

    Generated from the following TL definition:
    ```tl
    premiumSubscriptionOption#5f2d1df2 flags:# current:flags.1?true can_purchase_upgrade:flags.2?true transaction:flags.3?string months:int currency:string amount:long bot_url:string store_product:flags.0?string = PremiumSubscriptionOption
    ```
    """
    def __new__(
        cls,
        current: bool,
        can_purchase_upgrade: bool,
        transaction: Optional[str],
        months: int,
        currency: str,
        amount: int,
        bot_url: str,
        store_product: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendAsPeer(TLObject):
    """
    [Read `sendAsPeer` docs](https://core.telegram.org/constructor/sendAsPeer).

    Generated from the following TL definition:
    ```tl
    sendAsPeer#b81c7034 flags:# premium_required:flags.0?true peer:Peer = SendAsPeer
    ```
    """
    def __new__(
        cls,
        premium_required: bool,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageExtendedMediaPreview(TLObject):
    """
    [Read `messageExtendedMediaPreview` docs](https://core.telegram.org/constructor/messageExtendedMediaPreview).

    Generated from the following TL definition:
    ```tl
    messageExtendedMediaPreview#ad628cc8 flags:# w:flags.0?int h:flags.0?int thumb:flags.1?PhotoSize video_duration:flags.2?int = MessageExtendedMedia
    ```
    """
    def __new__(
        cls,
        w: Optional[int],
        h: Optional[int],
        thumb: Optional[types.PhotoSizeEmpty | types.PhotoSize | types.PhotoCachedSize | types.PhotoStrippedSize | types.PhotoSizeProgressive | types.PhotoPathSize],
        video_duration: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageExtendedMedia(TLObject):
    """
    [Read `messageExtendedMedia` docs](https://core.telegram.org/constructor/messageExtendedMedia).

    Generated from the following TL definition:
    ```tl
    messageExtendedMedia#ee479c64 media:MessageMedia = MessageExtendedMedia
    ```
    """
    def __new__(
        cls,
        media: types.MessageMediaEmpty | types.MessageMediaPhoto | types.MessageMediaGeo | types.MessageMediaContact | types.MessageMediaUnsupported | types.MessageMediaDocument | types.MessageMediaWebPage | types.MessageMediaVenue | types.MessageMediaGame | types.MessageMediaInvoice | types.MessageMediaGeoLive | types.MessageMediaPoll | types.MessageMediaDice | types.MessageMediaStory | types.MessageMediaGiveaway | types.MessageMediaGiveawayResults | types.MessageMediaPaidMedia | types.MessageMediaToDo | types.MessageMediaVideoStream,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StickerKeyword(TLObject):
    """
    [Read `stickerKeyword` docs](https://core.telegram.org/constructor/stickerKeyword).

    Generated from the following TL definition:
    ```tl
    stickerKeyword#fcfeb29c document_id:long keyword:Vector<string> = StickerKeyword
    ```
    """
    def __new__(
        cls,
        document_id: int,
        keyword: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Username(TLObject):
    """
    [Read `username` docs](https://core.telegram.org/constructor/username).

    Generated from the following TL definition:
    ```tl
    username#b4073647 flags:# editable:flags.0?true active:flags.1?true username:string = Username
    ```
    """
    def __new__(
        cls,
        editable: bool,
        active: bool,
        username: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ForumTopicDeleted(TLObject):
    """
    [Read `forumTopicDeleted` docs](https://core.telegram.org/constructor/forumTopicDeleted).

    Generated from the following TL definition:
    ```tl
    forumTopicDeleted#23f109b id:int = ForumTopic
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ForumTopic(TLObject):
    """
    [Read `forumTopic` docs](https://core.telegram.org/constructor/forumTopic).

    Generated from the following TL definition:
    ```tl
    forumTopic#cdff0eca flags:# my:flags.1?true closed:flags.2?true pinned:flags.3?true short:flags.5?true hidden:flags.6?true title_missing:flags.7?true id:int date:int peer:Peer title:string icon_color:int icon_emoji_id:flags.0?long top_message:int read_inbox_max_id:int read_outbox_max_id:int unread_count:int unread_mentions_count:int unread_reactions_count:int from_id:Peer notify_settings:PeerNotifySettings draft:flags.4?DraftMessage = ForumTopic
    ```
    """
    def __new__(
        cls,
        my: bool,
        closed: bool,
        pinned: bool,
        short: bool,
        hidden: bool,
        title_missing: bool,
        id: int,
        date: int,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        title: str,
        icon_color: int,
        icon_emoji_id: Optional[int],
        top_message: int,
        read_inbox_max_id: int,
        read_outbox_max_id: int,
        unread_count: int,
        unread_mentions_count: int,
        unread_reactions_count: int,
        from_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        notify_settings: types.PeerNotifySettings,
        draft: Optional[types.DraftMessageEmpty | types.DraftMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DefaultHistoryTtl(TLObject):
    """
    [Read `defaultHistoryTTL` docs](https://core.telegram.org/constructor/defaultHistoryTTL).

    Generated from the following TL definition:
    ```tl
    defaultHistoryTTL#43b46b20 period:int = DefaultHistoryTTL
    ```
    """
    def __new__(
        cls,
        period: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportedContactToken(TLObject):
    """
    [Read `exportedContactToken` docs](https://core.telegram.org/constructor/exportedContactToken).

    Generated from the following TL definition:
    ```tl
    exportedContactToken#41bf109b url:string expires:int = ExportedContactToken
    ```
    """
    def __new__(
        cls,
        url: str,
        expires: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestPeerTypeUser(TLObject):
    """
    [Read `requestPeerTypeUser` docs](https://core.telegram.org/constructor/requestPeerTypeUser).

    Generated from the following TL definition:
    ```tl
    requestPeerTypeUser#5f3b8a00 flags:# bot:flags.0?Bool premium:flags.1?Bool = RequestPeerType
    ```
    """
    def __new__(
        cls,
        bot: Optional[bool],
        premium: Optional[bool],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestPeerTypeChat(TLObject):
    """
    [Read `requestPeerTypeChat` docs](https://core.telegram.org/constructor/requestPeerTypeChat).

    Generated from the following TL definition:
    ```tl
    requestPeerTypeChat#c9f06e1b flags:# creator:flags.0?true bot_participant:flags.5?true has_username:flags.3?Bool forum:flags.4?Bool user_admin_rights:flags.1?ChatAdminRights bot_admin_rights:flags.2?ChatAdminRights = RequestPeerType
    ```
    """
    def __new__(
        cls,
        creator: bool,
        bot_participant: bool,
        has_username: Optional[bool],
        forum: Optional[bool],
        user_admin_rights: Optional[types.ChatAdminRights],
        bot_admin_rights: Optional[types.ChatAdminRights],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestPeerTypeBroadcast(TLObject):
    """
    [Read `requestPeerTypeBroadcast` docs](https://core.telegram.org/constructor/requestPeerTypeBroadcast).

    Generated from the following TL definition:
    ```tl
    requestPeerTypeBroadcast#339bef6c flags:# creator:flags.0?true has_username:flags.3?Bool user_admin_rights:flags.1?ChatAdminRights bot_admin_rights:flags.2?ChatAdminRights = RequestPeerType
    ```
    """
    def __new__(
        cls,
        creator: bool,
        has_username: Optional[bool],
        user_admin_rights: Optional[types.ChatAdminRights],
        bot_admin_rights: Optional[types.ChatAdminRights],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiListNotModified(TLObject):
    """
    [Read `emojiListNotModified` docs](https://core.telegram.org/constructor/emojiListNotModified).

    Generated from the following TL definition:
    ```tl
    emojiListNotModified#481eadfa = EmojiList
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiList(TLObject):
    """
    [Read `emojiList` docs](https://core.telegram.org/constructor/emojiList).

    Generated from the following TL definition:
    ```tl
    emojiList#7a1e11d1 hash:long document_id:Vector<long> = EmojiList
    ```
    """
    def __new__(
        cls,
        hash: int,
        document_id: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiGroup(TLObject):
    """
    [Read `emojiGroup` docs](https://core.telegram.org/constructor/emojiGroup).

    Generated from the following TL definition:
    ```tl
    emojiGroup#7a9abda9 title:string icon_emoji_id:long emoticons:Vector<string> = EmojiGroup
    ```
    """
    def __new__(
        cls,
        title: str,
        icon_emoji_id: int,
        emoticons: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiGroupGreeting(TLObject):
    """
    [Read `emojiGroupGreeting` docs](https://core.telegram.org/constructor/emojiGroupGreeting).

    Generated from the following TL definition:
    ```tl
    emojiGroupGreeting#80d26cc7 title:string icon_emoji_id:long emoticons:Vector<string> = EmojiGroup
    ```
    """
    def __new__(
        cls,
        title: str,
        icon_emoji_id: int,
        emoticons: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EmojiGroupPremium(TLObject):
    """
    [Read `emojiGroupPremium` docs](https://core.telegram.org/constructor/emojiGroupPremium).

    Generated from the following TL definition:
    ```tl
    emojiGroupPremium#93bcf34 title:string icon_emoji_id:long = EmojiGroup
    ```
    """
    def __new__(
        cls,
        title: str,
        icon_emoji_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TextWithEntities(TLObject):
    """
    [Read `textWithEntities` docs](https://core.telegram.org/constructor/textWithEntities).

    Generated from the following TL definition:
    ```tl
    textWithEntities#751f3146 text:string entities:Vector<MessageEntity> = TextWithEntities
    ```
    """
    def __new__(
        cls,
        text: str,
        entities: Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AutoSaveSettings(TLObject):
    """
    [Read `autoSaveSettings` docs](https://core.telegram.org/constructor/autoSaveSettings).

    Generated from the following TL definition:
    ```tl
    autoSaveSettings#c84834ce flags:# photos:flags.0?true videos:flags.1?true video_max_size:flags.2?long = AutoSaveSettings
    ```
    """
    def __new__(
        cls,
        photos: bool,
        videos: bool,
        video_max_size: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AutoSaveException(TLObject):
    """
    [Read `autoSaveException` docs](https://core.telegram.org/constructor/autoSaveException).

    Generated from the following TL definition:
    ```tl
    autoSaveException#81602d47 peer:Peer settings:AutoSaveSettings = AutoSaveException
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        settings: types.AutoSaveSettings,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotAppId(TLObject):
    """
    [Read `inputBotAppID` docs](https://core.telegram.org/constructor/inputBotAppID).

    Generated from the following TL definition:
    ```tl
    inputBotAppID#a920bd7a id:long access_hash:long = InputBotApp
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBotAppShortName(TLObject):
    """
    [Read `inputBotAppShortName` docs](https://core.telegram.org/constructor/inputBotAppShortName).

    Generated from the following TL definition:
    ```tl
    inputBotAppShortName#908c0407 bot_id:InputUser short_name:string = InputBotApp
    ```
    """
    def __new__(
        cls,
        bot_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        short_name: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotAppNotModified(TLObject):
    """
    [Read `botAppNotModified` docs](https://core.telegram.org/constructor/botAppNotModified).

    Generated from the following TL definition:
    ```tl
    botAppNotModified#5da674b7 = BotApp
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotApp(TLObject):
    """
    [Read `botApp` docs](https://core.telegram.org/constructor/botApp).

    Generated from the following TL definition:
    ```tl
    botApp#95fcd1d6 flags:# id:long access_hash:long short_name:string title:string description:string photo:Photo document:flags.0?Document hash:long = BotApp
    ```
    """
    def __new__(
        cls,
        id: int,
        access_hash: int,
        short_name: str,
        title: str,
        description: str,
        photo: types.PhotoEmpty | types.Photo,
        document: Optional[types.DocumentEmpty | types.Document],
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InlineBotWebView(TLObject):
    """
    [Read `inlineBotWebView` docs](https://core.telegram.org/constructor/inlineBotWebView).

    Generated from the following TL definition:
    ```tl
    inlineBotWebView#b57295d5 text:string url:string = InlineBotWebView
    ```
    """
    def __new__(
        cls,
        text: str,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReadParticipantDate(TLObject):
    """
    [Read `readParticipantDate` docs](https://core.telegram.org/constructor/readParticipantDate).

    Generated from the following TL definition:
    ```tl
    readParticipantDate#4a4ff172 user_id:long date:int = ReadParticipantDate
    ```
    """
    def __new__(
        cls,
        user_id: int,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputChatlistDialogFilter(TLObject):
    """
    [Read `inputChatlistDialogFilter` docs](https://core.telegram.org/constructor/inputChatlistDialogFilter).

    Generated from the following TL definition:
    ```tl
    inputChatlistDialogFilter#f3e0da33 filter_id:int = InputChatlist
    ```
    """
    def __new__(
        cls,
        filter_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportedChatlistInvite(TLObject):
    """
    [Read `exportedChatlistInvite` docs](https://core.telegram.org/constructor/exportedChatlistInvite).

    Generated from the following TL definition:
    ```tl
    exportedChatlistInvite#c5181ac flags:# title:string url:string peers:Vector<Peer> = ExportedChatlistInvite
    ```
    """
    def __new__(
        cls,
        title: str,
        url: str,
        peers: Sequence[types.PeerUser | types.PeerChat | types.PeerChannel],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessagePeerVote(TLObject):
    """
    [Read `messagePeerVote` docs](https://core.telegram.org/constructor/messagePeerVote).

    Generated from the following TL definition:
    ```tl
    messagePeerVote#b6cc2d5c peer:Peer option:bytes date:int = MessagePeerVote
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        option: bytes,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessagePeerVoteInputOption(TLObject):
    """
    [Read `messagePeerVoteInputOption` docs](https://core.telegram.org/constructor/messagePeerVoteInputOption).

    Generated from the following TL definition:
    ```tl
    messagePeerVoteInputOption#74cda504 peer:Peer date:int = MessagePeerVote
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessagePeerVoteMultiple(TLObject):
    """
    [Read `messagePeerVoteMultiple` docs](https://core.telegram.org/constructor/messagePeerVoteMultiple).

    Generated from the following TL definition:
    ```tl
    messagePeerVoteMultiple#4628f6e6 peer:Peer options:Vector<bytes> date:int = MessagePeerVote
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        options: Sequence[bytes],
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryViews(TLObject):
    """
    [Read `storyViews` docs](https://core.telegram.org/constructor/storyViews).

    Generated from the following TL definition:
    ```tl
    storyViews#8d595cd6 flags:# has_viewers:flags.1?true views_count:int forwards_count:flags.2?int reactions:flags.3?Vector<ReactionCount> reactions_count:flags.4?int recent_viewers:flags.0?Vector<long> = StoryViews
    ```
    """
    def __new__(
        cls,
        has_viewers: bool,
        views_count: int,
        forwards_count: Optional[int],
        reactions: Optional[Sequence[types.ReactionCount]],
        reactions_count: Optional[int],
        recent_viewers: Optional[Sequence[int]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryItemDeleted(TLObject):
    """
    [Read `storyItemDeleted` docs](https://core.telegram.org/constructor/storyItemDeleted).

    Generated from the following TL definition:
    ```tl
    storyItemDeleted#51e6ee4f id:int = StoryItem
    ```
    """
    def __new__(
        cls,
        id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryItemSkipped(TLObject):
    """
    [Read `storyItemSkipped` docs](https://core.telegram.org/constructor/storyItemSkipped).

    Generated from the following TL definition:
    ```tl
    storyItemSkipped#ffadc913 flags:# close_friends:flags.8?true live:flags.9?true id:int date:int expire_date:int = StoryItem
    ```
    """
    def __new__(
        cls,
        close_friends: bool,
        live: bool,
        id: int,
        date: int,
        expire_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryItem(TLObject):
    """
    [Read `storyItem` docs](https://core.telegram.org/constructor/storyItem).

    Generated from the following TL definition:
    ```tl
    storyItem#edf164f1 flags:# pinned:flags.5?true public:flags.7?true close_friends:flags.8?true min:flags.9?true noforwards:flags.10?true edited:flags.11?true contacts:flags.12?true selected_contacts:flags.13?true out:flags.16?true id:int date:int from_id:flags.18?Peer fwd_from:flags.17?StoryFwdHeader expire_date:int caption:flags.0?string entities:flags.1?Vector<MessageEntity> media:MessageMedia media_areas:flags.14?Vector<MediaArea> privacy:flags.2?Vector<PrivacyRule> views:flags.3?StoryViews sent_reaction:flags.15?Reaction albums:flags.19?Vector<int> = StoryItem
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        public: bool,
        close_friends: bool,
        min: bool,
        noforwards: bool,
        edited: bool,
        contacts: bool,
        selected_contacts: bool,
        out: bool,
        id: int,
        date: int,
        from_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        fwd_from: Optional[types.StoryFwdHeader],
        expire_date: int,
        caption: Optional[str],
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        media: types.MessageMediaEmpty | types.MessageMediaPhoto | types.MessageMediaGeo | types.MessageMediaContact | types.MessageMediaUnsupported | types.MessageMediaDocument | types.MessageMediaWebPage | types.MessageMediaVenue | types.MessageMediaGame | types.MessageMediaInvoice | types.MessageMediaGeoLive | types.MessageMediaPoll | types.MessageMediaDice | types.MessageMediaStory | types.MessageMediaGiveaway | types.MessageMediaGiveawayResults | types.MessageMediaPaidMedia | types.MessageMediaToDo | types.MessageMediaVideoStream,
        media_areas: Optional[Sequence[types.MediaAreaVenue | types.InputMediaAreaVenue | types.MediaAreaGeoPoint | types.MediaAreaSuggestedReaction | types.MediaAreaChannelPost | types.InputMediaAreaChannelPost | types.MediaAreaUrl | types.MediaAreaWeather | types.MediaAreaStarGift]],
        privacy: Optional[Sequence[types.PrivacyValueAllowContacts | types.PrivacyValueAllowAll | types.PrivacyValueAllowUsers | types.PrivacyValueDisallowContacts | types.PrivacyValueDisallowAll | types.PrivacyValueDisallowUsers | types.PrivacyValueAllowChatParticipants | types.PrivacyValueDisallowChatParticipants | types.PrivacyValueAllowCloseFriends | types.PrivacyValueAllowPremium | types.PrivacyValueAllowBots | types.PrivacyValueDisallowBots]],
        views: Optional[types.StoryViews],
        sent_reaction: Optional[types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid],
        albums: Optional[Sequence[int]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryView(TLObject):
    """
    [Read `storyView` docs](https://core.telegram.org/constructor/storyView).

    Generated from the following TL definition:
    ```tl
    storyView#b0bdeac5 flags:# blocked:flags.0?true blocked_my_stories_from:flags.1?true user_id:long date:int reaction:flags.2?Reaction = StoryView
    ```
    """
    def __new__(
        cls,
        blocked: bool,
        blocked_my_stories_from: bool,
        user_id: int,
        date: int,
        reaction: Optional[types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryViewPublicForward(TLObject):
    """
    [Read `storyViewPublicForward` docs](https://core.telegram.org/constructor/storyViewPublicForward).

    Generated from the following TL definition:
    ```tl
    storyViewPublicForward#9083670b flags:# blocked:flags.0?true blocked_my_stories_from:flags.1?true message:Message = StoryView
    ```
    """
    def __new__(
        cls,
        blocked: bool,
        blocked_my_stories_from: bool,
        message: types.MessageEmpty | types.Message | types.MessageService,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryViewPublicRepost(TLObject):
    """
    [Read `storyViewPublicRepost` docs](https://core.telegram.org/constructor/storyViewPublicRepost).

    Generated from the following TL definition:
    ```tl
    storyViewPublicRepost#bd74cf49 flags:# blocked:flags.0?true blocked_my_stories_from:flags.1?true peer_id:Peer story:StoryItem = StoryView
    ```
    """
    def __new__(
        cls,
        blocked: bool,
        blocked_my_stories_from: bool,
        peer_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        story: types.StoryItemDeleted | types.StoryItemSkipped | types.StoryItem,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReplyToMessage(TLObject):
    """
    [Read `inputReplyToMessage` docs](https://core.telegram.org/constructor/inputReplyToMessage).

    Generated from the following TL definition:
    ```tl
    inputReplyToMessage#869fbe10 flags:# reply_to_msg_id:int top_msg_id:flags.0?int reply_to_peer_id:flags.1?InputPeer quote_text:flags.2?string quote_entities:flags.3?Vector<MessageEntity> quote_offset:flags.4?int monoforum_peer_id:flags.5?InputPeer todo_item_id:flags.6?int = InputReplyTo
    ```
    """
    def __new__(
        cls,
        reply_to_msg_id: int,
        top_msg_id: Optional[int],
        reply_to_peer_id: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        quote_text: Optional[str],
        quote_entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        quote_offset: Optional[int],
        monoforum_peer_id: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
        todo_item_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReplyToStory(TLObject):
    """
    [Read `inputReplyToStory` docs](https://core.telegram.org/constructor/inputReplyToStory).

    Generated from the following TL definition:
    ```tl
    inputReplyToStory#5881323a peer:InputPeer story_id:int = InputReplyTo
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        story_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputReplyToMonoForum(TLObject):
    """
    [Read `inputReplyToMonoForum` docs](https://core.telegram.org/constructor/inputReplyToMonoForum).

    Generated from the following TL definition:
    ```tl
    inputReplyToMonoForum#69d66c45 monoforum_peer_id:InputPeer = InputReplyTo
    ```
    """
    def __new__(
        cls,
        monoforum_peer_id: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportedStoryLink(TLObject):
    """
    [Read `exportedStoryLink` docs](https://core.telegram.org/constructor/exportedStoryLink).

    Generated from the following TL definition:
    ```tl
    exportedStoryLink#3fc9053b link:string = ExportedStoryLink
    ```
    """
    def __new__(
        cls,
        link: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoriesStealthMode(TLObject):
    """
    [Read `storiesStealthMode` docs](https://core.telegram.org/constructor/storiesStealthMode).

    Generated from the following TL definition:
    ```tl
    storiesStealthMode#712e27fd flags:# active_until_date:flags.0?int cooldown_until_date:flags.1?int = StoriesStealthMode
    ```
    """
    def __new__(
        cls,
        active_until_date: Optional[int],
        cooldown_until_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MediaAreaCoordinates(TLObject):
    """
    [Read `mediaAreaCoordinates` docs](https://core.telegram.org/constructor/mediaAreaCoordinates).

    Generated from the following TL definition:
    ```tl
    mediaAreaCoordinates#cfc9e002 flags:# x:double y:double w:double h:double rotation:double radius:flags.0?double = MediaAreaCoordinates
    ```
    """
    def __new__(
        cls,
        x: float,
        y: float,
        w: float,
        h: float,
        rotation: float,
        radius: Optional[float],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MediaAreaVenue(TLObject):
    """
    [Read `mediaAreaVenue` docs](https://core.telegram.org/constructor/mediaAreaVenue).

    Generated from the following TL definition:
    ```tl
    mediaAreaVenue#be82db9c coordinates:MediaAreaCoordinates geo:GeoPoint title:string address:string provider:string venue_id:string venue_type:string = MediaArea
    ```
    """
    def __new__(
        cls,
        coordinates: types.MediaAreaCoordinates,
        geo: types.GeoPointEmpty | types.GeoPoint,
        title: str,
        address: str,
        provider: str,
        venue_id: str,
        venue_type: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaAreaVenue(TLObject):
    """
    [Read `inputMediaAreaVenue` docs](https://core.telegram.org/constructor/inputMediaAreaVenue).

    Generated from the following TL definition:
    ```tl
    inputMediaAreaVenue#b282217f coordinates:MediaAreaCoordinates query_id:long result_id:string = MediaArea
    ```
    """
    def __new__(
        cls,
        coordinates: types.MediaAreaCoordinates,
        query_id: int,
        result_id: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MediaAreaGeoPoint(TLObject):
    """
    [Read `mediaAreaGeoPoint` docs](https://core.telegram.org/constructor/mediaAreaGeoPoint).

    Generated from the following TL definition:
    ```tl
    mediaAreaGeoPoint#cad5452d flags:# coordinates:MediaAreaCoordinates geo:GeoPoint address:flags.0?GeoPointAddress = MediaArea
    ```
    """
    def __new__(
        cls,
        coordinates: types.MediaAreaCoordinates,
        geo: types.GeoPointEmpty | types.GeoPoint,
        address: Optional[types.GeoPointAddress],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MediaAreaSuggestedReaction(TLObject):
    """
    [Read `mediaAreaSuggestedReaction` docs](https://core.telegram.org/constructor/mediaAreaSuggestedReaction).

    Generated from the following TL definition:
    ```tl
    mediaAreaSuggestedReaction#14455871 flags:# dark:flags.0?true flipped:flags.1?true coordinates:MediaAreaCoordinates reaction:Reaction = MediaArea
    ```
    """
    def __new__(
        cls,
        dark: bool,
        flipped: bool,
        coordinates: types.MediaAreaCoordinates,
        reaction: types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MediaAreaChannelPost(TLObject):
    """
    [Read `mediaAreaChannelPost` docs](https://core.telegram.org/constructor/mediaAreaChannelPost).

    Generated from the following TL definition:
    ```tl
    mediaAreaChannelPost#770416af coordinates:MediaAreaCoordinates channel_id:long msg_id:int = MediaArea
    ```
    """
    def __new__(
        cls,
        coordinates: types.MediaAreaCoordinates,
        channel_id: int,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputMediaAreaChannelPost(TLObject):
    """
    [Read `inputMediaAreaChannelPost` docs](https://core.telegram.org/constructor/inputMediaAreaChannelPost).

    Generated from the following TL definition:
    ```tl
    inputMediaAreaChannelPost#2271f2bf coordinates:MediaAreaCoordinates channel:InputChannel msg_id:int = MediaArea
    ```
    """
    def __new__(
        cls,
        coordinates: types.MediaAreaCoordinates,
        channel: types.InputChannelEmpty | types.InputChannel | types.InputChannelFromMessage,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MediaAreaUrl(TLObject):
    """
    [Read `mediaAreaUrl` docs](https://core.telegram.org/constructor/mediaAreaUrl).

    Generated from the following TL definition:
    ```tl
    mediaAreaUrl#37381085 coordinates:MediaAreaCoordinates url:string = MediaArea
    ```
    """
    def __new__(
        cls,
        coordinates: types.MediaAreaCoordinates,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MediaAreaWeather(TLObject):
    """
    [Read `mediaAreaWeather` docs](https://core.telegram.org/constructor/mediaAreaWeather).

    Generated from the following TL definition:
    ```tl
    mediaAreaWeather#49a6549c coordinates:MediaAreaCoordinates emoji:string temperature_c:double color:int = MediaArea
    ```
    """
    def __new__(
        cls,
        coordinates: types.MediaAreaCoordinates,
        emoji: str,
        temperature_c: float,
        color: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MediaAreaStarGift(TLObject):
    """
    [Read `mediaAreaStarGift` docs](https://core.telegram.org/constructor/mediaAreaStarGift).

    Generated from the following TL definition:
    ```tl
    mediaAreaStarGift#5787686d coordinates:MediaAreaCoordinates slug:string = MediaArea
    ```
    """
    def __new__(
        cls,
        coordinates: types.MediaAreaCoordinates,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerStories(TLObject):
    """
    [Read `peerStories` docs](https://core.telegram.org/constructor/peerStories).

    Generated from the following TL definition:
    ```tl
    peerStories#9a35e999 flags:# peer:Peer max_read_id:flags.0?int stories:Vector<StoryItem> = PeerStories
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        max_read_id: Optional[int],
        stories: Sequence[types.StoryItemDeleted | types.StoryItemSkipped | types.StoryItem],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PremiumGiftCodeOption(TLObject):
    """
    [Read `premiumGiftCodeOption` docs](https://core.telegram.org/constructor/premiumGiftCodeOption).

    Generated from the following TL definition:
    ```tl
    premiumGiftCodeOption#257e962b flags:# users:int months:int store_product:flags.0?string store_quantity:flags.1?int currency:string amount:long = PremiumGiftCodeOption
    ```
    """
    def __new__(
        cls,
        users: int,
        months: int,
        store_product: Optional[str],
        store_quantity: Optional[int],
        currency: str,
        amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrepaidGiveaway(TLObject):
    """
    [Read `prepaidGiveaway` docs](https://core.telegram.org/constructor/prepaidGiveaway).

    Generated from the following TL definition:
    ```tl
    prepaidGiveaway#b2539d54 id:long months:int quantity:int date:int = PrepaidGiveaway
    ```
    """
    def __new__(
        cls,
        id: int,
        months: int,
        quantity: int,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PrepaidStarsGiveaway(TLObject):
    """
    [Read `prepaidStarsGiveaway` docs](https://core.telegram.org/constructor/prepaidStarsGiveaway).

    Generated from the following TL definition:
    ```tl
    prepaidStarsGiveaway#9a9d77e0 id:long stars:long quantity:int boosts:int date:int = PrepaidGiveaway
    ```
    """
    def __new__(
        cls,
        id: int,
        stars: int,
        quantity: int,
        boosts: int,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Boost(TLObject):
    """
    [Read `boost` docs](https://core.telegram.org/constructor/boost).

    Generated from the following TL definition:
    ```tl
    boost#4b3e14d6 flags:# gift:flags.1?true giveaway:flags.2?true unclaimed:flags.3?true id:string user_id:flags.0?long giveaway_msg_id:flags.2?int date:int expires:int used_gift_slug:flags.4?string multiplier:flags.5?int stars:flags.6?long = Boost
    ```
    """
    def __new__(
        cls,
        gift: bool,
        giveaway: bool,
        unclaimed: bool,
        id: str,
        user_id: Optional[int],
        giveaway_msg_id: Optional[int],
        date: int,
        expires: int,
        used_gift_slug: Optional[str],
        multiplier: Optional[int],
        stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MyBoost(TLObject):
    """
    [Read `myBoost` docs](https://core.telegram.org/constructor/myBoost).

    Generated from the following TL definition:
    ```tl
    myBoost#c448415c flags:# slot:int peer:flags.0?Peer date:int expires:int cooldown_until_date:flags.1?int = MyBoost
    ```
    """
    def __new__(
        cls,
        slot: int,
        peer: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        date: int,
        expires: int,
        cooldown_until_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryFwdHeader(TLObject):
    """
    [Read `storyFwdHeader` docs](https://core.telegram.org/constructor/storyFwdHeader).

    Generated from the following TL definition:
    ```tl
    storyFwdHeader#b826e150 flags:# modified:flags.3?true from:flags.0?Peer from_name:flags.1?string story_id:flags.2?int = StoryFwdHeader
    ```
    """
    def __new__(
        cls,
        modified: bool,
        from: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        from_name: Optional[str],
        story_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PostInteractionCountersMessage(TLObject):
    """
    [Read `postInteractionCountersMessage` docs](https://core.telegram.org/constructor/postInteractionCountersMessage).

    Generated from the following TL definition:
    ```tl
    postInteractionCountersMessage#e7058e7f msg_id:int views:int forwards:int reactions:int = PostInteractionCounters
    ```
    """
    def __new__(
        cls,
        msg_id: int,
        views: int,
        forwards: int,
        reactions: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PostInteractionCountersStory(TLObject):
    """
    [Read `postInteractionCountersStory` docs](https://core.telegram.org/constructor/postInteractionCountersStory).

    Generated from the following TL definition:
    ```tl
    postInteractionCountersStory#8a480e27 story_id:int views:int forwards:int reactions:int = PostInteractionCounters
    ```
    """
    def __new__(
        cls,
        story_id: int,
        views: int,
        forwards: int,
        reactions: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PublicForwardMessage(TLObject):
    """
    [Read `publicForwardMessage` docs](https://core.telegram.org/constructor/publicForwardMessage).

    Generated from the following TL definition:
    ```tl
    publicForwardMessage#1f2bf4a message:Message = PublicForward
    ```
    """
    def __new__(
        cls,
        message: types.MessageEmpty | types.Message | types.MessageService,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PublicForwardStory(TLObject):
    """
    [Read `publicForwardStory` docs](https://core.telegram.org/constructor/publicForwardStory).

    Generated from the following TL definition:
    ```tl
    publicForwardStory#edf3add0 peer:Peer story:StoryItem = PublicForward
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        story: types.StoryItemDeleted | types.StoryItemSkipped | types.StoryItem,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerColor(TLObject):
    """
    [Read `peerColor` docs](https://core.telegram.org/constructor/peerColor).

    Generated from the following TL definition:
    ```tl
    peerColor#b54b5acf flags:# color:flags.0?int background_emoji_id:flags.1?long = PeerColor
    ```
    """
    def __new__(
        cls,
        color: Optional[int],
        background_emoji_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerColorCollectible(TLObject):
    """
    [Read `peerColorCollectible` docs](https://core.telegram.org/constructor/peerColorCollectible).

    Generated from the following TL definition:
    ```tl
    peerColorCollectible#b9c0639a flags:# collectible_id:long gift_emoji_id:long background_emoji_id:long accent_color:int colors:Vector<int> dark_accent_color:flags.0?int dark_colors:flags.1?Vector<int> = PeerColor
    ```
    """
    def __new__(
        cls,
        collectible_id: int,
        gift_emoji_id: int,
        background_emoji_id: int,
        accent_color: int,
        colors: Sequence[int],
        dark_accent_color: Optional[int],
        dark_colors: Optional[Sequence[int]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPeerColorCollectible(TLObject):
    """
    [Read `inputPeerColorCollectible` docs](https://core.telegram.org/constructor/inputPeerColorCollectible).

    Generated from the following TL definition:
    ```tl
    inputPeerColorCollectible#b8ea86a9 collectible_id:long = PeerColor
    ```
    """
    def __new__(
        cls,
        collectible_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryReaction(TLObject):
    """
    [Read `storyReaction` docs](https://core.telegram.org/constructor/storyReaction).

    Generated from the following TL definition:
    ```tl
    storyReaction#6090d6d5 peer_id:Peer date:int reaction:Reaction = StoryReaction
    ```
    """
    def __new__(
        cls,
        peer_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        date: int,
        reaction: types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryReactionPublicForward(TLObject):
    """
    [Read `storyReactionPublicForward` docs](https://core.telegram.org/constructor/storyReactionPublicForward).

    Generated from the following TL definition:
    ```tl
    storyReactionPublicForward#bbab2643 message:Message = StoryReaction
    ```
    """
    def __new__(
        cls,
        message: types.MessageEmpty | types.Message | types.MessageService,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryReactionPublicRepost(TLObject):
    """
    [Read `storyReactionPublicRepost` docs](https://core.telegram.org/constructor/storyReactionPublicRepost).

    Generated from the following TL definition:
    ```tl
    storyReactionPublicRepost#cfcd0f13 peer_id:Peer story:StoryItem = StoryReaction
    ```
    """
    def __new__(
        cls,
        peer_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        story: types.StoryItemDeleted | types.StoryItemSkipped | types.StoryItem,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedDialog(TLObject):
    """
    [Read `savedDialog` docs](https://core.telegram.org/constructor/savedDialog).

    Generated from the following TL definition:
    ```tl
    savedDialog#bd87cb6c flags:# pinned:flags.2?true peer:Peer top_message:int = SavedDialog
    ```
    """
    def __new__(
        cls,
        pinned: bool,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        top_message: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MonoForumDialog(TLObject):
    """
    [Read `monoForumDialog` docs](https://core.telegram.org/constructor/monoForumDialog).

    Generated from the following TL definition:
    ```tl
    monoForumDialog#64407ea7 flags:# unread_mark:flags.3?true nopaid_messages_exception:flags.4?true peer:Peer top_message:int read_inbox_max_id:int read_outbox_max_id:int unread_count:int unread_reactions_count:int draft:flags.1?DraftMessage = SavedDialog
    ```
    """
    def __new__(
        cls,
        unread_mark: bool,
        nopaid_messages_exception: bool,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        top_message: int,
        read_inbox_max_id: int,
        read_outbox_max_id: int,
        unread_count: int,
        unread_reactions_count: int,
        draft: Optional[types.DraftMessageEmpty | types.DraftMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedReactionTag(TLObject):
    """
    [Read `savedReactionTag` docs](https://core.telegram.org/constructor/savedReactionTag).

    Generated from the following TL definition:
    ```tl
    savedReactionTag#cb6ff828 flags:# reaction:Reaction title:flags.0?string count:int = SavedReactionTag
    ```
    """
    def __new__(
        cls,
        reaction: types.ReactionEmpty | types.ReactionEmoji | types.ReactionCustomEmoji | types.ReactionPaid,
        title: Optional[str],
        count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class OutboxReadDate(TLObject):
    """
    [Read `outboxReadDate` docs](https://core.telegram.org/constructor/outboxReadDate).

    Generated from the following TL definition:
    ```tl
    outboxReadDate#3bb842ac date:int = OutboxReadDate
    ```
    """
    def __new__(
        cls,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SmsJob(TLObject):
    """
    [Read `smsJob` docs](https://core.telegram.org/constructor/smsJob).

    Generated from the following TL definition:
    ```tl
    smsJob#e6a1eeb8 job_id:string phone_number:string text:string = SmsJob
    ```
    """
    def __new__(
        cls,
        job_id: str,
        phone_number: str,
        text: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessWeeklyOpen(TLObject):
    """
    [Read `businessWeeklyOpen` docs](https://core.telegram.org/constructor/businessWeeklyOpen).

    Generated from the following TL definition:
    ```tl
    businessWeeklyOpen#120b1ab9 start_minute:int end_minute:int = BusinessWeeklyOpen
    ```
    """
    def __new__(
        cls,
        start_minute: int,
        end_minute: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessWorkHours(TLObject):
    """
    [Read `businessWorkHours` docs](https://core.telegram.org/constructor/businessWorkHours).

    Generated from the following TL definition:
    ```tl
    businessWorkHours#8c92b098 flags:# open_now:flags.0?true timezone_id:string weekly_open:Vector<BusinessWeeklyOpen> = BusinessWorkHours
    ```
    """
    def __new__(
        cls,
        open_now: bool,
        timezone_id: str,
        weekly_open: Sequence[types.BusinessWeeklyOpen],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessLocation(TLObject):
    """
    [Read `businessLocation` docs](https://core.telegram.org/constructor/businessLocation).

    Generated from the following TL definition:
    ```tl
    businessLocation#ac5c1af7 flags:# geo_point:flags.0?GeoPoint address:string = BusinessLocation
    ```
    """
    def __new__(
        cls,
        geo_point: Optional[types.GeoPointEmpty | types.GeoPoint],
        address: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBusinessRecipients(TLObject):
    """
    [Read `inputBusinessRecipients` docs](https://core.telegram.org/constructor/inputBusinessRecipients).

    Generated from the following TL definition:
    ```tl
    inputBusinessRecipients#6f8b32aa flags:# existing_chats:flags.0?true new_chats:flags.1?true contacts:flags.2?true non_contacts:flags.3?true exclude_selected:flags.5?true users:flags.4?Vector<InputUser> = InputBusinessRecipients
    ```
    """
    def __new__(
        cls,
        existing_chats: bool,
        new_chats: bool,
        contacts: bool,
        non_contacts: bool,
        exclude_selected: bool,
        users: Optional[Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessRecipients(TLObject):
    """
    [Read `businessRecipients` docs](https://core.telegram.org/constructor/businessRecipients).

    Generated from the following TL definition:
    ```tl
    businessRecipients#21108ff7 flags:# existing_chats:flags.0?true new_chats:flags.1?true contacts:flags.2?true non_contacts:flags.3?true exclude_selected:flags.5?true users:flags.4?Vector<long> = BusinessRecipients
    ```
    """
    def __new__(
        cls,
        existing_chats: bool,
        new_chats: bool,
        contacts: bool,
        non_contacts: bool,
        exclude_selected: bool,
        users: Optional[Sequence[int]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessAwayMessageScheduleAlways(TLObject):
    """
    [Read `businessAwayMessageScheduleAlways` docs](https://core.telegram.org/constructor/businessAwayMessageScheduleAlways).

    Generated from the following TL definition:
    ```tl
    businessAwayMessageScheduleAlways#c9b9e2b9 = BusinessAwayMessageSchedule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessAwayMessageScheduleOutsideWorkHours(TLObject):
    """
    [Read `businessAwayMessageScheduleOutsideWorkHours` docs](https://core.telegram.org/constructor/businessAwayMessageScheduleOutsideWorkHours).

    Generated from the following TL definition:
    ```tl
    businessAwayMessageScheduleOutsideWorkHours#c3f2f501 = BusinessAwayMessageSchedule
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessAwayMessageScheduleCustom(TLObject):
    """
    [Read `businessAwayMessageScheduleCustom` docs](https://core.telegram.org/constructor/businessAwayMessageScheduleCustom).

    Generated from the following TL definition:
    ```tl
    businessAwayMessageScheduleCustom#cc4d9ecc start_date:int end_date:int = BusinessAwayMessageSchedule
    ```
    """
    def __new__(
        cls,
        start_date: int,
        end_date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBusinessGreetingMessage(TLObject):
    """
    [Read `inputBusinessGreetingMessage` docs](https://core.telegram.org/constructor/inputBusinessGreetingMessage).

    Generated from the following TL definition:
    ```tl
    inputBusinessGreetingMessage#194cb3b shortcut_id:int recipients:InputBusinessRecipients no_activity_days:int = InputBusinessGreetingMessage
    ```
    """
    def __new__(
        cls,
        shortcut_id: int,
        recipients: types.InputBusinessRecipients,
        no_activity_days: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessGreetingMessage(TLObject):
    """
    [Read `businessGreetingMessage` docs](https://core.telegram.org/constructor/businessGreetingMessage).

    Generated from the following TL definition:
    ```tl
    businessGreetingMessage#e519abab shortcut_id:int recipients:BusinessRecipients no_activity_days:int = BusinessGreetingMessage
    ```
    """
    def __new__(
        cls,
        shortcut_id: int,
        recipients: types.BusinessRecipients,
        no_activity_days: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBusinessAwayMessage(TLObject):
    """
    [Read `inputBusinessAwayMessage` docs](https://core.telegram.org/constructor/inputBusinessAwayMessage).

    Generated from the following TL definition:
    ```tl
    inputBusinessAwayMessage#832175e0 flags:# offline_only:flags.0?true shortcut_id:int schedule:BusinessAwayMessageSchedule recipients:InputBusinessRecipients = InputBusinessAwayMessage
    ```
    """
    def __new__(
        cls,
        offline_only: bool,
        shortcut_id: int,
        schedule: types.BusinessAwayMessageScheduleAlways | types.BusinessAwayMessageScheduleOutsideWorkHours | types.BusinessAwayMessageScheduleCustom,
        recipients: types.InputBusinessRecipients,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessAwayMessage(TLObject):
    """
    [Read `businessAwayMessage` docs](https://core.telegram.org/constructor/businessAwayMessage).

    Generated from the following TL definition:
    ```tl
    businessAwayMessage#ef156a5c flags:# offline_only:flags.0?true shortcut_id:int schedule:BusinessAwayMessageSchedule recipients:BusinessRecipients = BusinessAwayMessage
    ```
    """
    def __new__(
        cls,
        offline_only: bool,
        shortcut_id: int,
        schedule: types.BusinessAwayMessageScheduleAlways | types.BusinessAwayMessageScheduleOutsideWorkHours | types.BusinessAwayMessageScheduleCustom,
        recipients: types.BusinessRecipients,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Timezone(TLObject):
    """
    [Read `timezone` docs](https://core.telegram.org/constructor/timezone).

    Generated from the following TL definition:
    ```tl
    timezone#ff9289f5 id:string name:string utc_offset:int = Timezone
    ```
    """
    def __new__(
        cls,
        id: str,
        name: str,
        utc_offset: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class QuickReply(TLObject):
    """
    [Read `quickReply` docs](https://core.telegram.org/constructor/quickReply).

    Generated from the following TL definition:
    ```tl
    quickReply#697102b shortcut_id:int shortcut:string top_message:int count:int = QuickReply
    ```
    """
    def __new__(
        cls,
        shortcut_id: int,
        shortcut: str,
        top_message: int,
        count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputQuickReplyShortcut(TLObject):
    """
    [Read `inputQuickReplyShortcut` docs](https://core.telegram.org/constructor/inputQuickReplyShortcut).

    Generated from the following TL definition:
    ```tl
    inputQuickReplyShortcut#24596d41 shortcut:string = InputQuickReplyShortcut
    ```
    """
    def __new__(
        cls,
        shortcut: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputQuickReplyShortcutId(TLObject):
    """
    [Read `inputQuickReplyShortcutId` docs](https://core.telegram.org/constructor/inputQuickReplyShortcutId).

    Generated from the following TL definition:
    ```tl
    inputQuickReplyShortcutId#1190cf1 shortcut_id:int = InputQuickReplyShortcut
    ```
    """
    def __new__(
        cls,
        shortcut_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ConnectedBot(TLObject):
    """
    [Read `connectedBot` docs](https://core.telegram.org/constructor/connectedBot).

    Generated from the following TL definition:
    ```tl
    connectedBot#cd64636c flags:# bot_id:long recipients:BusinessBotRecipients rights:BusinessBotRights = ConnectedBot
    ```
    """
    def __new__(
        cls,
        bot_id: int,
        recipients: types.BusinessBotRecipients,
        rights: types.BusinessBotRights,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Birthday(TLObject):
    """
    [Read `birthday` docs](https://core.telegram.org/constructor/birthday).

    Generated from the following TL definition:
    ```tl
    birthday#6c8e1e06 flags:# day:int month:int year:flags.0?int = Birthday
    ```
    """
    def __new__(
        cls,
        day: int,
        month: int,
        year: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotBusinessConnection(TLObject):
    """
    [Read `botBusinessConnection` docs](https://core.telegram.org/constructor/botBusinessConnection).

    Generated from the following TL definition:
    ```tl
    botBusinessConnection#8f34b2f5 flags:# disabled:flags.1?true connection_id:string user_id:long dc_id:int date:int rights:flags.2?BusinessBotRights = BotBusinessConnection
    ```
    """
    def __new__(
        cls,
        disabled: bool,
        connection_id: str,
        user_id: int,
        dc_id: int,
        date: int,
        rights: Optional[types.BusinessBotRights],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBusinessIntro(TLObject):
    """
    [Read `inputBusinessIntro` docs](https://core.telegram.org/constructor/inputBusinessIntro).

    Generated from the following TL definition:
    ```tl
    inputBusinessIntro#9c469cd flags:# title:string description:string sticker:flags.0?InputDocument = InputBusinessIntro
    ```
    """
    def __new__(
        cls,
        title: str,
        description: str,
        sticker: Optional[types.InputDocumentEmpty | types.InputDocument],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessIntro(TLObject):
    """
    [Read `businessIntro` docs](https://core.telegram.org/constructor/businessIntro).

    Generated from the following TL definition:
    ```tl
    businessIntro#5a0a066d flags:# title:string description:string sticker:flags.0?Document = BusinessIntro
    ```
    """
    def __new__(
        cls,
        title: str,
        description: str,
        sticker: Optional[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputCollectibleUsername(TLObject):
    """
    [Read `inputCollectibleUsername` docs](https://core.telegram.org/constructor/inputCollectibleUsername).

    Generated from the following TL definition:
    ```tl
    inputCollectibleUsername#e39460a9 username:string = InputCollectible
    ```
    """
    def __new__(
        cls,
        username: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputCollectiblePhone(TLObject):
    """
    [Read `inputCollectiblePhone` docs](https://core.telegram.org/constructor/inputCollectiblePhone).

    Generated from the following TL definition:
    ```tl
    inputCollectiblePhone#a2e214a4 phone:string = InputCollectible
    ```
    """
    def __new__(
        cls,
        phone: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBusinessBotRecipients(TLObject):
    """
    [Read `inputBusinessBotRecipients` docs](https://core.telegram.org/constructor/inputBusinessBotRecipients).

    Generated from the following TL definition:
    ```tl
    inputBusinessBotRecipients#c4e5921e flags:# existing_chats:flags.0?true new_chats:flags.1?true contacts:flags.2?true non_contacts:flags.3?true exclude_selected:flags.5?true users:flags.4?Vector<InputUser> exclude_users:flags.6?Vector<InputUser> = InputBusinessBotRecipients
    ```
    """
    def __new__(
        cls,
        existing_chats: bool,
        new_chats: bool,
        contacts: bool,
        non_contacts: bool,
        exclude_selected: bool,
        users: Optional[Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage]],
        exclude_users: Optional[Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessBotRecipients(TLObject):
    """
    [Read `businessBotRecipients` docs](https://core.telegram.org/constructor/businessBotRecipients).

    Generated from the following TL definition:
    ```tl
    businessBotRecipients#b88cf373 flags:# existing_chats:flags.0?true new_chats:flags.1?true contacts:flags.2?true non_contacts:flags.3?true exclude_selected:flags.5?true users:flags.4?Vector<long> exclude_users:flags.6?Vector<long> = BusinessBotRecipients
    ```
    """
    def __new__(
        cls,
        existing_chats: bool,
        new_chats: bool,
        contacts: bool,
        non_contacts: bool,
        exclude_selected: bool,
        users: Optional[Sequence[int]],
        exclude_users: Optional[Sequence[int]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ContactBirthday(TLObject):
    """
    [Read `contactBirthday` docs](https://core.telegram.org/constructor/contactBirthday).

    Generated from the following TL definition:
    ```tl
    contactBirthday#1d998733 contact_id:long birthday:Birthday = ContactBirthday
    ```
    """
    def __new__(
        cls,
        contact_id: int,
        birthday: types.Birthday,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MissingInvitee(TLObject):
    """
    [Read `missingInvitee` docs](https://core.telegram.org/constructor/missingInvitee).

    Generated from the following TL definition:
    ```tl
    missingInvitee#628c9224 flags:# premium_would_allow_invite:flags.0?true premium_required_for_pm:flags.1?true user_id:long = MissingInvitee
    ```
    """
    def __new__(
        cls,
        premium_would_allow_invite: bool,
        premium_required_for_pm: bool,
        user_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputBusinessChatLink(TLObject):
    """
    [Read `inputBusinessChatLink` docs](https://core.telegram.org/constructor/inputBusinessChatLink).

    Generated from the following TL definition:
    ```tl
    inputBusinessChatLink#11679fa7 flags:# message:string entities:flags.0?Vector<MessageEntity> title:flags.1?string = InputBusinessChatLink
    ```
    """
    def __new__(
        cls,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        title: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessChatLink(TLObject):
    """
    [Read `businessChatLink` docs](https://core.telegram.org/constructor/businessChatLink).

    Generated from the following TL definition:
    ```tl
    businessChatLink#b4ae666f flags:# link:string message:string entities:flags.0?Vector<MessageEntity> title:flags.1?string views:int = BusinessChatLink
    ```
    """
    def __new__(
        cls,
        link: str,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
        title: Optional[str],
        views: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestedPeerUser(TLObject):
    """
    [Read `requestedPeerUser` docs](https://core.telegram.org/constructor/requestedPeerUser).

    Generated from the following TL definition:
    ```tl
    requestedPeerUser#d62ff46a flags:# user_id:long first_name:flags.0?string last_name:flags.0?string username:flags.1?string photo:flags.2?Photo = RequestedPeer
    ```
    """
    def __new__(
        cls,
        user_id: int,
        first_name: Optional[str],
        last_name: Optional[str],
        username: Optional[str],
        photo: Optional[types.PhotoEmpty | types.Photo],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestedPeerChat(TLObject):
    """
    [Read `requestedPeerChat` docs](https://core.telegram.org/constructor/requestedPeerChat).

    Generated from the following TL definition:
    ```tl
    requestedPeerChat#7307544f flags:# chat_id:long title:flags.0?string photo:flags.2?Photo = RequestedPeer
    ```
    """
    def __new__(
        cls,
        chat_id: int,
        title: Optional[str],
        photo: Optional[types.PhotoEmpty | types.Photo],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequestedPeerChannel(TLObject):
    """
    [Read `requestedPeerChannel` docs](https://core.telegram.org/constructor/requestedPeerChannel).

    Generated from the following TL definition:
    ```tl
    requestedPeerChannel#8ba403e4 flags:# channel_id:long title:flags.0?string username:flags.1?string photo:flags.2?Photo = RequestedPeer
    ```
    """
    def __new__(
        cls,
        channel_id: int,
        title: Optional[str],
        username: Optional[str],
        photo: Optional[types.PhotoEmpty | types.Photo],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SponsoredMessageReportOption(TLObject):
    """
    [Read `sponsoredMessageReportOption` docs](https://core.telegram.org/constructor/sponsoredMessageReportOption).

    Generated from the following TL definition:
    ```tl
    sponsoredMessageReportOption#430d3150 text:string option:bytes = SponsoredMessageReportOption
    ```
    """
    def __new__(
        cls,
        text: str,
        option: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReactionNotificationsFromContacts(TLObject):
    """
    [Read `reactionNotificationsFromContacts` docs](https://core.telegram.org/constructor/reactionNotificationsFromContacts).

    Generated from the following TL definition:
    ```tl
    reactionNotificationsFromContacts#bac3a61a = ReactionNotificationsFrom
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReactionNotificationsFromAll(TLObject):
    """
    [Read `reactionNotificationsFromAll` docs](https://core.telegram.org/constructor/reactionNotificationsFromAll).

    Generated from the following TL definition:
    ```tl
    reactionNotificationsFromAll#4b9e22a0 = ReactionNotificationsFrom
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReactionsNotifySettings(TLObject):
    """
    [Read `reactionsNotifySettings` docs](https://core.telegram.org/constructor/reactionsNotifySettings).

    Generated from the following TL definition:
    ```tl
    reactionsNotifySettings#56e34970 flags:# messages_notify_from:flags.0?ReactionNotificationsFrom stories_notify_from:flags.1?ReactionNotificationsFrom sound:NotificationSound show_previews:Bool = ReactionsNotifySettings
    ```
    """
    def __new__(
        cls,
        messages_notify_from: Optional[types.ReactionNotificationsFromContacts | types.ReactionNotificationsFromAll],
        stories_notify_from: Optional[types.ReactionNotificationsFromContacts | types.ReactionNotificationsFromAll],
        sound: types.NotificationSoundDefault | types.NotificationSoundNone | types.NotificationSoundLocal | types.NotificationSoundRingtone,
        show_previews: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AvailableEffect(TLObject):
    """
    [Read `availableEffect` docs](https://core.telegram.org/constructor/availableEffect).

    Generated from the following TL definition:
    ```tl
    availableEffect#93c3e27e flags:# premium_required:flags.2?true id:long emoticon:string static_icon_id:flags.0?long effect_sticker_id:long effect_animation_id:flags.1?long = AvailableEffect
    ```
    """
    def __new__(
        cls,
        premium_required: bool,
        id: int,
        emoticon: str,
        static_icon_id: Optional[int],
        effect_sticker_id: int,
        effect_animation_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FactCheck(TLObject):
    """
    [Read `factCheck` docs](https://core.telegram.org/constructor/factCheck).

    Generated from the following TL definition:
    ```tl
    factCheck#b89bfccf flags:# need_check:flags.0?true country:flags.1?string text:flags.1?TextWithEntities hash:long = FactCheck
    ```
    """
    def __new__(
        cls,
        need_check: bool,
        country: Optional[str],
        text: Optional[types.TextWithEntities],
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsTransactionPeerUnsupported(TLObject):
    """
    [Read `starsTransactionPeerUnsupported` docs](https://core.telegram.org/constructor/starsTransactionPeerUnsupported).

    Generated from the following TL definition:
    ```tl
    starsTransactionPeerUnsupported#95f2bfe4 = StarsTransactionPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsTransactionPeerAppStore(TLObject):
    """
    [Read `starsTransactionPeerAppStore` docs](https://core.telegram.org/constructor/starsTransactionPeerAppStore).

    Generated from the following TL definition:
    ```tl
    starsTransactionPeerAppStore#b457b375 = StarsTransactionPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsTransactionPeerPlayMarket(TLObject):
    """
    [Read `starsTransactionPeerPlayMarket` docs](https://core.telegram.org/constructor/starsTransactionPeerPlayMarket).

    Generated from the following TL definition:
    ```tl
    starsTransactionPeerPlayMarket#7b560a0b = StarsTransactionPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsTransactionPeerPremiumBot(TLObject):
    """
    [Read `starsTransactionPeerPremiumBot` docs](https://core.telegram.org/constructor/starsTransactionPeerPremiumBot).

    Generated from the following TL definition:
    ```tl
    starsTransactionPeerPremiumBot#250dbaf8 = StarsTransactionPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsTransactionPeerFragment(TLObject):
    """
    [Read `starsTransactionPeerFragment` docs](https://core.telegram.org/constructor/starsTransactionPeerFragment).

    Generated from the following TL definition:
    ```tl
    starsTransactionPeerFragment#e92fd902 = StarsTransactionPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsTransactionPeer(TLObject):
    """
    [Read `starsTransactionPeer` docs](https://core.telegram.org/constructor/starsTransactionPeer).

    Generated from the following TL definition:
    ```tl
    starsTransactionPeer#d80da15d peer:Peer = StarsTransactionPeer
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsTransactionPeerAds(TLObject):
    """
    [Read `starsTransactionPeerAds` docs](https://core.telegram.org/constructor/starsTransactionPeerAds).

    Generated from the following TL definition:
    ```tl
    starsTransactionPeerAds#60682812 = StarsTransactionPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsTransactionPeerApi(TLObject):
    """
    [Read `starsTransactionPeerAPI` docs](https://core.telegram.org/constructor/starsTransactionPeerAPI).

    Generated from the following TL definition:
    ```tl
    starsTransactionPeerAPI#f9677aad = StarsTransactionPeer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsTopupOption(TLObject):
    """
    [Read `starsTopupOption` docs](https://core.telegram.org/constructor/starsTopupOption).

    Generated from the following TL definition:
    ```tl
    starsTopupOption#bd915c0 flags:# extended:flags.1?true stars:long store_product:flags.0?string currency:string amount:long = StarsTopupOption
    ```
    """
    def __new__(
        cls,
        extended: bool,
        stars: int,
        store_product: Optional[str],
        currency: str,
        amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsTransaction(TLObject):
    """
    [Read `starsTransaction` docs](https://core.telegram.org/constructor/starsTransaction).

    Generated from the following TL definition:
    ```tl
    starsTransaction#13659eb0 flags:# refund:flags.3?true pending:flags.4?true failed:flags.6?true gift:flags.10?true reaction:flags.11?true stargift_upgrade:flags.18?true business_transfer:flags.21?true stargift_resale:flags.22?true posts_search:flags.24?true stargift_prepaid_upgrade:flags.25?true stargift_drop_original_details:flags.26?true phonegroup_message:flags.27?true stargift_auction_bid:flags.28?true offer:flags.29?true id:string amount:StarsAmount date:int peer:StarsTransactionPeer title:flags.0?string description:flags.1?string photo:flags.2?WebDocument transaction_date:flags.5?int transaction_url:flags.5?string bot_payload:flags.7?bytes msg_id:flags.8?int extended_media:flags.9?Vector<MessageMedia> subscription_period:flags.12?int giveaway_post_id:flags.13?int stargift:flags.14?StarGift floodskip_number:flags.15?int starref_commission_permille:flags.16?int starref_peer:flags.17?Peer starref_amount:flags.17?StarsAmount paid_messages:flags.19?int premium_gift_months:flags.20?int ads_proceeds_from_date:flags.23?int ads_proceeds_to_date:flags.23?int = StarsTransaction
    ```
    """
    def __new__(
        cls,
        refund: bool,
        pending: bool,
        failed: bool,
        gift: bool,
        reaction: bool,
        stargift_upgrade: bool,
        business_transfer: bool,
        stargift_resale: bool,
        posts_search: bool,
        stargift_prepaid_upgrade: bool,
        stargift_drop_original_details: bool,
        phonegroup_message: bool,
        stargift_auction_bid: bool,
        offer: bool,
        id: str,
        amount: types.StarsAmount | types.StarsTonAmount,
        date: int,
        peer: types.StarsTransactionPeerUnsupported | types.StarsTransactionPeerAppStore | types.StarsTransactionPeerPlayMarket | types.StarsTransactionPeerPremiumBot | types.StarsTransactionPeerFragment | types.StarsTransactionPeer | types.StarsTransactionPeerAds | types.StarsTransactionPeerApi,
        title: Optional[str],
        description: Optional[str],
        photo: Optional[types.WebDocument | types.WebDocumentNoProxy],
        transaction_date: Optional[int],
        transaction_url: Optional[str],
        bot_payload: Optional[bytes],
        msg_id: Optional[int],
        extended_media: Optional[Sequence[types.MessageMediaEmpty | types.MessageMediaPhoto | types.MessageMediaGeo | types.MessageMediaContact | types.MessageMediaUnsupported | types.MessageMediaDocument | types.MessageMediaWebPage | types.MessageMediaVenue | types.MessageMediaGame | types.MessageMediaInvoice | types.MessageMediaGeoLive | types.MessageMediaPoll | types.MessageMediaDice | types.MessageMediaStory | types.MessageMediaGiveaway | types.MessageMediaGiveawayResults | types.MessageMediaPaidMedia | types.MessageMediaToDo | types.MessageMediaVideoStream]],
        subscription_period: Optional[int],
        giveaway_post_id: Optional[int],
        stargift: Optional[types.StarGift | types.StarGiftUnique],
        floodskip_number: Optional[int],
        starref_commission_permille: Optional[int],
        starref_peer: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        starref_amount: Optional[types.StarsAmount | types.StarsTonAmount],
        paid_messages: Optional[int],
        premium_gift_months: Optional[int],
        ads_proceeds_from_date: Optional[int],
        ads_proceeds_to_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FoundStory(TLObject):
    """
    [Read `foundStory` docs](https://core.telegram.org/constructor/foundStory).

    Generated from the following TL definition:
    ```tl
    foundStory#e87acbc0 peer:Peer story:StoryItem = FoundStory
    ```
    """
    def __new__(
        cls,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        story: types.StoryItemDeleted | types.StoryItemSkipped | types.StoryItem,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GeoPointAddress(TLObject):
    """
    [Read `geoPointAddress` docs](https://core.telegram.org/constructor/geoPointAddress).

    Generated from the following TL definition:
    ```tl
    geoPointAddress#de4c5d93 flags:# country_iso2:string state:flags.0?string city:flags.1?string street:flags.2?string = GeoPointAddress
    ```
    """
    def __new__(
        cls,
        country_iso2: str,
        state: Optional[str],
        city: Optional[str],
        street: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsRevenueStatus(TLObject):
    """
    [Read `starsRevenueStatus` docs](https://core.telegram.org/constructor/starsRevenueStatus).

    Generated from the following TL definition:
    ```tl
    starsRevenueStatus#febe5491 flags:# withdrawal_enabled:flags.0?true current_balance:StarsAmount available_balance:StarsAmount overall_revenue:StarsAmount next_withdrawal_at:flags.1?int = StarsRevenueStatus
    ```
    """
    def __new__(
        cls,
        withdrawal_enabled: bool,
        current_balance: types.StarsAmount | types.StarsTonAmount,
        available_balance: types.StarsAmount | types.StarsTonAmount,
        overall_revenue: types.StarsAmount | types.StarsTonAmount,
        next_withdrawal_at: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStarsTransaction(TLObject):
    """
    [Read `inputStarsTransaction` docs](https://core.telegram.org/constructor/inputStarsTransaction).

    Generated from the following TL definition:
    ```tl
    inputStarsTransaction#206ae6d1 flags:# refund:flags.0?true id:string = InputStarsTransaction
    ```
    """
    def __new__(
        cls,
        refund: bool,
        id: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsGiftOption(TLObject):
    """
    [Read `starsGiftOption` docs](https://core.telegram.org/constructor/starsGiftOption).

    Generated from the following TL definition:
    ```tl
    starsGiftOption#5e0589f1 flags:# extended:flags.1?true stars:long store_product:flags.0?string currency:string amount:long = StarsGiftOption
    ```
    """
    def __new__(
        cls,
        extended: bool,
        stars: int,
        store_product: Optional[str],
        currency: str,
        amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotPreviewMedia(TLObject):
    """
    [Read `botPreviewMedia` docs](https://core.telegram.org/constructor/botPreviewMedia).

    Generated from the following TL definition:
    ```tl
    botPreviewMedia#23e91ba3 date:int media:MessageMedia = BotPreviewMedia
    ```
    """
    def __new__(
        cls,
        date: int,
        media: types.MessageMediaEmpty | types.MessageMediaPhoto | types.MessageMediaGeo | types.MessageMediaContact | types.MessageMediaUnsupported | types.MessageMediaDocument | types.MessageMediaWebPage | types.MessageMediaVenue | types.MessageMediaGame | types.MessageMediaInvoice | types.MessageMediaGeoLive | types.MessageMediaPoll | types.MessageMediaDice | types.MessageMediaStory | types.MessageMediaGiveaway | types.MessageMediaGiveawayResults | types.MessageMediaPaidMedia | types.MessageMediaToDo | types.MessageMediaVideoStream,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsSubscriptionPricing(TLObject):
    """
    [Read `starsSubscriptionPricing` docs](https://core.telegram.org/constructor/starsSubscriptionPricing).

    Generated from the following TL definition:
    ```tl
    starsSubscriptionPricing#5416d58 period:int amount:long = StarsSubscriptionPricing
    ```
    """
    def __new__(
        cls,
        period: int,
        amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsSubscription(TLObject):
    """
    [Read `starsSubscription` docs](https://core.telegram.org/constructor/starsSubscription).

    Generated from the following TL definition:
    ```tl
    starsSubscription#2e6eab1a flags:# canceled:flags.0?true can_refulfill:flags.1?true missing_balance:flags.2?true bot_canceled:flags.7?true id:string peer:Peer until_date:int pricing:StarsSubscriptionPricing chat_invite_hash:flags.3?string title:flags.4?string photo:flags.5?WebDocument invoice_slug:flags.6?string = StarsSubscription
    ```
    """
    def __new__(
        cls,
        canceled: bool,
        can_refulfill: bool,
        missing_balance: bool,
        bot_canceled: bool,
        id: str,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        until_date: int,
        pricing: types.StarsSubscriptionPricing,
        chat_invite_hash: Optional[str],
        title: Optional[str],
        photo: Optional[types.WebDocument | types.WebDocumentNoProxy],
        invoice_slug: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageReactor(TLObject):
    """
    [Read `messageReactor` docs](https://core.telegram.org/constructor/messageReactor).

    Generated from the following TL definition:
    ```tl
    messageReactor#4ba3a95a flags:# top:flags.0?true my:flags.1?true anonymous:flags.2?true peer_id:flags.3?Peer count:int = MessageReactor
    ```
    """
    def __new__(
        cls,
        top: bool,
        my: bool,
        anonymous: bool,
        peer_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsGiveawayOption(TLObject):
    """
    [Read `starsGiveawayOption` docs](https://core.telegram.org/constructor/starsGiveawayOption).

    Generated from the following TL definition:
    ```tl
    starsGiveawayOption#94ce852a flags:# extended:flags.0?true default:flags.1?true stars:long yearly_boosts:int store_product:flags.2?string currency:string amount:long winners:Vector<StarsGiveawayWinnersOption> = StarsGiveawayOption
    ```
    """
    def __new__(
        cls,
        extended: bool,
        default: bool,
        stars: int,
        yearly_boosts: int,
        store_product: Optional[str],
        currency: str,
        amount: int,
        winners: Sequence[types.StarsGiveawayWinnersOption],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsGiveawayWinnersOption(TLObject):
    """
    [Read `starsGiveawayWinnersOption` docs](https://core.telegram.org/constructor/starsGiveawayWinnersOption).

    Generated from the following TL definition:
    ```tl
    starsGiveawayWinnersOption#54236209 flags:# default:flags.0?true users:int per_user_stars:long = StarsGiveawayWinnersOption
    ```
    """
    def __new__(
        cls,
        default: bool,
        users: int,
        per_user_stars: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGift(TLObject):
    """
    [Read `starGift` docs](https://core.telegram.org/constructor/starGift).

    Generated from the following TL definition:
    ```tl
    starGift#313a9547 flags:# limited:flags.0?true sold_out:flags.1?true birthday:flags.2?true require_premium:flags.7?true limited_per_user:flags.8?true peer_color_available:flags.10?true auction:flags.11?true id:long sticker:Document stars:long availability_remains:flags.0?int availability_total:flags.0?int availability_resale:flags.4?long convert_stars:long first_sale_date:flags.1?int last_sale_date:flags.1?int upgrade_stars:flags.3?long resell_min_stars:flags.4?long title:flags.5?string released_by:flags.6?Peer per_user_total:flags.8?int per_user_remains:flags.8?int locked_until_date:flags.9?int auction_slug:flags.11?string gifts_per_round:flags.11?int auction_start_date:flags.11?int upgrade_variants:flags.12?int background:flags.13?StarGiftBackground = StarGift
    ```
    """
    def __new__(
        cls,
        limited: bool,
        sold_out: bool,
        birthday: bool,
        require_premium: bool,
        limited_per_user: bool,
        peer_color_available: bool,
        auction: bool,
        id: int,
        sticker: types.DocumentEmpty | types.Document,
        stars: int,
        availability_remains: Optional[int],
        availability_total: Optional[int],
        availability_resale: Optional[int],
        convert_stars: int,
        first_sale_date: Optional[int],
        last_sale_date: Optional[int],
        upgrade_stars: Optional[int],
        resell_min_stars: Optional[int],
        title: Optional[str],
        released_by: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        per_user_total: Optional[int],
        per_user_remains: Optional[int],
        locked_until_date: Optional[int],
        auction_slug: Optional[str],
        gifts_per_round: Optional[int],
        auction_start_date: Optional[int],
        upgrade_variants: Optional[int],
        background: Optional[types.StarGiftBackground],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftUnique(TLObject):
    """
    [Read `starGiftUnique` docs](https://core.telegram.org/constructor/starGiftUnique).

    Generated from the following TL definition:
    ```tl
    starGiftUnique#569d64c9 flags:# require_premium:flags.6?true resale_ton_only:flags.7?true theme_available:flags.9?true id:long gift_id:long title:string slug:string num:int owner_id:flags.0?Peer owner_name:flags.1?string owner_address:flags.2?string attributes:Vector<StarGiftAttribute> availability_issued:int availability_total:int gift_address:flags.3?string resell_amount:flags.4?Vector<StarsAmount> released_by:flags.5?Peer value_amount:flags.8?long value_currency:flags.8?string value_usd_amount:flags.8?long theme_peer:flags.10?Peer peer_color:flags.11?PeerColor host_id:flags.12?Peer offer_min_stars:flags.13?int = StarGift
    ```
    """
    def __new__(
        cls,
        require_premium: bool,
        resale_ton_only: bool,
        theme_available: bool,
        id: int,
        gift_id: int,
        title: str,
        slug: str,
        num: int,
        owner_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        owner_name: Optional[str],
        owner_address: Optional[str],
        attributes: Sequence[types.StarGiftAttributeModel | types.StarGiftAttributePattern | types.StarGiftAttributeBackdrop | types.StarGiftAttributeOriginalDetails],
        availability_issued: int,
        availability_total: int,
        gift_address: Optional[str],
        resell_amount: Optional[Sequence[types.StarsAmount | types.StarsTonAmount]],
        released_by: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        value_amount: Optional[int],
        value_currency: Optional[str],
        value_usd_amount: Optional[int],
        theme_peer: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        peer_color: Optional[types.PeerColor | types.PeerColorCollectible | types.InputPeerColorCollectible],
        host_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        offer_min_stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MessageReportOption(TLObject):
    """
    [Read `messageReportOption` docs](https://core.telegram.org/constructor/messageReportOption).

    Generated from the following TL definition:
    ```tl
    messageReportOption#7903e3d9 text:string option:bytes = MessageReportOption
    ```
    """
    def __new__(
        cls,
        text: str,
        option: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportResultChooseOption(TLObject):
    """
    [Read `reportResultChooseOption` docs](https://core.telegram.org/constructor/reportResultChooseOption).

    Generated from the following TL definition:
    ```tl
    reportResultChooseOption#f0e4e0b6 title:string options:Vector<MessageReportOption> = ReportResult
    ```
    """
    def __new__(
        cls,
        title: str,
        options: Sequence[types.MessageReportOption],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportResultAddComment(TLObject):
    """
    [Read `reportResultAddComment` docs](https://core.telegram.org/constructor/reportResultAddComment).

    Generated from the following TL definition:
    ```tl
    reportResultAddComment#6f09ac31 flags:# optional:flags.0?true option:bytes = ReportResult
    ```
    """
    def __new__(
        cls,
        optional: bool,
        option: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReportResultReported(TLObject):
    """
    [Read `reportResultReported` docs](https://core.telegram.org/constructor/reportResultReported).

    Generated from the following TL definition:
    ```tl
    reportResultReported#8db33c4b = ReportResult
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotAppSettings(TLObject):
    """
    [Read `botAppSettings` docs](https://core.telegram.org/constructor/botAppSettings).

    Generated from the following TL definition:
    ```tl
    botAppSettings#c99b1950 flags:# placeholder_path:flags.0?bytes background_color:flags.1?int background_dark_color:flags.2?int header_color:flags.3?int header_dark_color:flags.4?int = BotAppSettings
    ```
    """
    def __new__(
        cls,
        placeholder_path: Optional[bytes],
        background_color: Optional[int],
        background_dark_color: Optional[int],
        header_color: Optional[int],
        header_dark_color: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarRefProgram(TLObject):
    """
    [Read `starRefProgram` docs](https://core.telegram.org/constructor/starRefProgram).

    Generated from the following TL definition:
    ```tl
    starRefProgram#dd0c66f2 flags:# bot_id:long commission_permille:int duration_months:flags.0?int end_date:flags.1?int daily_revenue_per_user:flags.2?StarsAmount = StarRefProgram
    ```
    """
    def __new__(
        cls,
        bot_id: int,
        commission_permille: int,
        duration_months: Optional[int],
        end_date: Optional[int],
        daily_revenue_per_user: Optional[types.StarsAmount | types.StarsTonAmount],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ConnectedBotStarRef(TLObject):
    """
    [Read `connectedBotStarRef` docs](https://core.telegram.org/constructor/connectedBotStarRef).

    Generated from the following TL definition:
    ```tl
    connectedBotStarRef#19a13f71 flags:# revoked:flags.1?true url:string date:int bot_id:long commission_permille:int duration_months:flags.0?int participants:long revenue:long = ConnectedBotStarRef
    ```
    """
    def __new__(
        cls,
        revoked: bool,
        url: str,
        date: int,
        bot_id: int,
        commission_permille: int,
        duration_months: Optional[int],
        participants: int,
        revenue: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsAmount(TLObject):
    """
    [Read `starsAmount` docs](https://core.telegram.org/constructor/starsAmount).

    Generated from the following TL definition:
    ```tl
    starsAmount#bbb6b4a3 amount:long nanos:int = StarsAmount
    ```
    """
    def __new__(
        cls,
        amount: int,
        nanos: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsTonAmount(TLObject):
    """
    [Read `starsTonAmount` docs](https://core.telegram.org/constructor/starsTonAmount).

    Generated from the following TL definition:
    ```tl
    starsTonAmount#74aee3e0 amount:long = StarsAmount
    ```
    """
    def __new__(
        cls,
        amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotVerifierSettings(TLObject):
    """
    [Read `botVerifierSettings` docs](https://core.telegram.org/constructor/botVerifierSettings).

    Generated from the following TL definition:
    ```tl
    botVerifierSettings#b0cd6617 flags:# can_modify_custom_description:flags.1?true icon:long company:string custom_description:flags.0?string = BotVerifierSettings
    ```
    """
    def __new__(
        cls,
        can_modify_custom_description: bool,
        icon: int,
        company: str,
        custom_description: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotVerification(TLObject):
    """
    [Read `botVerification` docs](https://core.telegram.org/constructor/botVerification).

    Generated from the following TL definition:
    ```tl
    botVerification#f93cd45c bot_id:long icon:long description:string = BotVerification
    ```
    """
    def __new__(
        cls,
        bot_id: int,
        icon: int,
        description: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAttributeModel(TLObject):
    """
    [Read `starGiftAttributeModel` docs](https://core.telegram.org/constructor/starGiftAttributeModel).

    Generated from the following TL definition:
    ```tl
    starGiftAttributeModel#39d99013 name:string document:Document rarity_permille:int = StarGiftAttribute
    ```
    """
    def __new__(
        cls,
        name: str,
        document: types.DocumentEmpty | types.Document,
        rarity_permille: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAttributePattern(TLObject):
    """
    [Read `starGiftAttributePattern` docs](https://core.telegram.org/constructor/starGiftAttributePattern).

    Generated from the following TL definition:
    ```tl
    starGiftAttributePattern#13acff19 name:string document:Document rarity_permille:int = StarGiftAttribute
    ```
    """
    def __new__(
        cls,
        name: str,
        document: types.DocumentEmpty | types.Document,
        rarity_permille: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAttributeBackdrop(TLObject):
    """
    [Read `starGiftAttributeBackdrop` docs](https://core.telegram.org/constructor/starGiftAttributeBackdrop).

    Generated from the following TL definition:
    ```tl
    starGiftAttributeBackdrop#d93d859c name:string backdrop_id:int center_color:int edge_color:int pattern_color:int text_color:int rarity_permille:int = StarGiftAttribute
    ```
    """
    def __new__(
        cls,
        name: str,
        backdrop_id: int,
        center_color: int,
        edge_color: int,
        pattern_color: int,
        text_color: int,
        rarity_permille: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAttributeOriginalDetails(TLObject):
    """
    [Read `starGiftAttributeOriginalDetails` docs](https://core.telegram.org/constructor/starGiftAttributeOriginalDetails).

    Generated from the following TL definition:
    ```tl
    starGiftAttributeOriginalDetails#e0bff26c flags:# sender_id:flags.0?Peer recipient_id:Peer date:int message:flags.1?TextWithEntities = StarGiftAttribute
    ```
    """
    def __new__(
        cls,
        sender_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        recipient_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        date: int,
        message: Optional[types.TextWithEntities],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedStarGift(TLObject):
    """
    [Read `savedStarGift` docs](https://core.telegram.org/constructor/savedStarGift).

    Generated from the following TL definition:
    ```tl
    savedStarGift#ead6805e flags:# name_hidden:flags.0?true unsaved:flags.5?true refunded:flags.9?true can_upgrade:flags.10?true pinned_to_top:flags.12?true upgrade_separate:flags.17?true from_id:flags.1?Peer date:int gift:StarGift message:flags.2?TextWithEntities msg_id:flags.3?int saved_id:flags.11?long convert_stars:flags.4?long upgrade_stars:flags.6?long can_export_at:flags.7?int transfer_stars:flags.8?long can_transfer_at:flags.13?int can_resell_at:flags.14?int collection_id:flags.15?Vector<int> prepaid_upgrade_hash:flags.16?string drop_original_details_stars:flags.18?long gift_num:flags.19?int = SavedStarGift
    ```
    """
    def __new__(
        cls,
        name_hidden: bool,
        unsaved: bool,
        refunded: bool,
        can_upgrade: bool,
        pinned_to_top: bool,
        upgrade_separate: bool,
        from_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        date: int,
        gift: types.StarGift | types.StarGiftUnique,
        message: Optional[types.TextWithEntities],
        msg_id: Optional[int],
        saved_id: Optional[int],
        convert_stars: Optional[int],
        upgrade_stars: Optional[int],
        can_export_at: Optional[int],
        transfer_stars: Optional[int],
        can_transfer_at: Optional[int],
        can_resell_at: Optional[int],
        collection_id: Optional[Sequence[int]],
        prepaid_upgrade_hash: Optional[str],
        drop_original_details_stars: Optional[int],
        gift_num: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputSavedStarGiftUser(TLObject):
    """
    [Read `inputSavedStarGiftUser` docs](https://core.telegram.org/constructor/inputSavedStarGiftUser).

    Generated from the following TL definition:
    ```tl
    inputSavedStarGiftUser#69279795 msg_id:int = InputSavedStarGift
    ```
    """
    def __new__(
        cls,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputSavedStarGiftChat(TLObject):
    """
    [Read `inputSavedStarGiftChat` docs](https://core.telegram.org/constructor/inputSavedStarGiftChat).

    Generated from the following TL definition:
    ```tl
    inputSavedStarGiftChat#f101aa7f peer:InputPeer saved_id:long = InputSavedStarGift
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        saved_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputSavedStarGiftSlug(TLObject):
    """
    [Read `inputSavedStarGiftSlug` docs](https://core.telegram.org/constructor/inputSavedStarGiftSlug).

    Generated from the following TL definition:
    ```tl
    inputSavedStarGiftSlug#2085c238 slug:string = InputSavedStarGift
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaidReactionPrivacyDefault(TLObject):
    """
    [Read `paidReactionPrivacyDefault` docs](https://core.telegram.org/constructor/paidReactionPrivacyDefault).

    Generated from the following TL definition:
    ```tl
    paidReactionPrivacyDefault#206ad49e = PaidReactionPrivacy
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaidReactionPrivacyAnonymous(TLObject):
    """
    [Read `paidReactionPrivacyAnonymous` docs](https://core.telegram.org/constructor/paidReactionPrivacyAnonymous).

    Generated from the following TL definition:
    ```tl
    paidReactionPrivacyAnonymous#1f0c1ad9 = PaidReactionPrivacy
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaidReactionPrivacyPeer(TLObject):
    """
    [Read `paidReactionPrivacyPeer` docs](https://core.telegram.org/constructor/paidReactionPrivacyPeer).

    Generated from the following TL definition:
    ```tl
    paidReactionPrivacyPeer#dc6cfcf0 peer:InputPeer = PaidReactionPrivacy
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequirementToContactEmpty(TLObject):
    """
    [Read `requirementToContactEmpty` docs](https://core.telegram.org/constructor/requirementToContactEmpty).

    Generated from the following TL definition:
    ```tl
    requirementToContactEmpty#50a9839 = RequirementToContact
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequirementToContactPremium(TLObject):
    """
    [Read `requirementToContactPremium` docs](https://core.telegram.org/constructor/requirementToContactPremium).

    Generated from the following TL definition:
    ```tl
    requirementToContactPremium#e581e4e9 = RequirementToContact
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RequirementToContactPaidMessages(TLObject):
    """
    [Read `requirementToContactPaidMessages` docs](https://core.telegram.org/constructor/requirementToContactPaidMessages).

    Generated from the following TL definition:
    ```tl
    requirementToContactPaidMessages#b4f67e93 stars_amount:long = RequirementToContact
    ```
    """
    def __new__(
        cls,
        stars_amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BusinessBotRights(TLObject):
    """
    [Read `businessBotRights` docs](https://core.telegram.org/constructor/businessBotRights).

    Generated from the following TL definition:
    ```tl
    businessBotRights#a0624cf7 flags:# reply:flags.0?true read_messages:flags.1?true delete_sent_messages:flags.2?true delete_received_messages:flags.3?true edit_name:flags.4?true edit_bio:flags.5?true edit_profile_photo:flags.6?true edit_username:flags.7?true view_gifts:flags.8?true sell_gifts:flags.9?true change_gift_settings:flags.10?true transfer_and_upgrade_gifts:flags.11?true transfer_stars:flags.12?true manage_stories:flags.13?true = BusinessBotRights
    ```
    """
    def __new__(
        cls,
        reply: bool,
        read_messages: bool,
        delete_sent_messages: bool,
        delete_received_messages: bool,
        edit_name: bool,
        edit_bio: bool,
        edit_profile_photo: bool,
        edit_username: bool,
        view_gifts: bool,
        sell_gifts: bool,
        change_gift_settings: bool,
        transfer_and_upgrade_gifts: bool,
        transfer_stars: bool,
        manage_stories: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DisallowedGiftsSettings(TLObject):
    """
    [Read `disallowedGiftsSettings` docs](https://core.telegram.org/constructor/disallowedGiftsSettings).

    Generated from the following TL definition:
    ```tl
    disallowedGiftsSettings#71f276c4 flags:# disallow_unlimited_stargifts:flags.0?true disallow_limited_stargifts:flags.1?true disallow_unique_stargifts:flags.2?true disallow_premium_gifts:flags.3?true disallow_stargifts_from_channels:flags.4?true = DisallowedGiftsSettings
    ```
    """
    def __new__(
        cls,
        disallow_unlimited_stargifts: bool,
        disallow_limited_stargifts: bool,
        disallow_unique_stargifts: bool,
        disallow_premium_gifts: bool,
        disallow_stargifts_from_channels: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SponsoredPeer(TLObject):
    """
    [Read `sponsoredPeer` docs](https://core.telegram.org/constructor/sponsoredPeer).

    Generated from the following TL definition:
    ```tl
    sponsoredPeer#c69708d3 flags:# random_id:bytes peer:Peer sponsor_info:flags.0?string additional_info:flags.1?string = SponsoredPeer
    ```
    """
    def __new__(
        cls,
        random_id: bytes,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        sponsor_info: Optional[str],
        additional_info: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAttributeIdModel(TLObject):
    """
    [Read `starGiftAttributeIdModel` docs](https://core.telegram.org/constructor/starGiftAttributeIdModel).

    Generated from the following TL definition:
    ```tl
    starGiftAttributeIdModel#48aaae3c document_id:long = StarGiftAttributeId
    ```
    """
    def __new__(
        cls,
        document_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAttributeIdPattern(TLObject):
    """
    [Read `starGiftAttributeIdPattern` docs](https://core.telegram.org/constructor/starGiftAttributeIdPattern).

    Generated from the following TL definition:
    ```tl
    starGiftAttributeIdPattern#4a162433 document_id:long = StarGiftAttributeId
    ```
    """
    def __new__(
        cls,
        document_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAttributeIdBackdrop(TLObject):
    """
    [Read `starGiftAttributeIdBackdrop` docs](https://core.telegram.org/constructor/starGiftAttributeIdBackdrop).

    Generated from the following TL definition:
    ```tl
    starGiftAttributeIdBackdrop#1f01c757 backdrop_id:int = StarGiftAttributeId
    ```
    """
    def __new__(
        cls,
        backdrop_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAttributeCounter(TLObject):
    """
    [Read `starGiftAttributeCounter` docs](https://core.telegram.org/constructor/starGiftAttributeCounter).

    Generated from the following TL definition:
    ```tl
    starGiftAttributeCounter#2eb1b658 attribute:StarGiftAttributeId count:int = StarGiftAttributeCounter
    ```
    """
    def __new__(
        cls,
        attribute: types.StarGiftAttributeIdModel | types.StarGiftAttributeIdPattern | types.StarGiftAttributeIdBackdrop,
        count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PendingSuggestion(TLObject):
    """
    [Read `pendingSuggestion` docs](https://core.telegram.org/constructor/pendingSuggestion).

    Generated from the following TL definition:
    ```tl
    pendingSuggestion#e7e82e12 suggestion:string title:TextWithEntities description:TextWithEntities url:string = PendingSuggestion
    ```
    """
    def __new__(
        cls,
        suggestion: str,
        title: types.TextWithEntities,
        description: types.TextWithEntities,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TodoItem(TLObject):
    """
    [Read `todoItem` docs](https://core.telegram.org/constructor/todoItem).

    Generated from the following TL definition:
    ```tl
    todoItem#cba9a52f id:int title:TextWithEntities = TodoItem
    ```
    """
    def __new__(
        cls,
        id: int,
        title: types.TextWithEntities,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TodoList(TLObject):
    """
    [Read `todoList` docs](https://core.telegram.org/constructor/todoList).

    Generated from the following TL definition:
    ```tl
    todoList#49b92a26 flags:# others_can_append:flags.0?true others_can_complete:flags.1?true title:TextWithEntities list:Vector<TodoItem> = TodoList
    ```
    """
    def __new__(
        cls,
        others_can_append: bool,
        others_can_complete: bool,
        title: types.TextWithEntities,
        list: Sequence[types.TodoItem],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TodoCompletion(TLObject):
    """
    [Read `todoCompletion` docs](https://core.telegram.org/constructor/todoCompletion).

    Generated from the following TL definition:
    ```tl
    todoCompletion#221bb5e4 id:int completed_by:Peer date:int = TodoCompletion
    ```
    """
    def __new__(
        cls,
        id: int,
        completed_by: types.PeerUser | types.PeerChat | types.PeerChannel,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SuggestedPost(TLObject):
    """
    [Read `suggestedPost` docs](https://core.telegram.org/constructor/suggestedPost).

    Generated from the following TL definition:
    ```tl
    suggestedPost#e8e37e5 flags:# accepted:flags.1?true rejected:flags.2?true price:flags.3?StarsAmount schedule_date:flags.0?int = SuggestedPost
    ```
    """
    def __new__(
        cls,
        accepted: bool,
        rejected: bool,
        price: Optional[types.StarsAmount | types.StarsTonAmount],
        schedule_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsRating(TLObject):
    """
    [Read `starsRating` docs](https://core.telegram.org/constructor/starsRating).

    Generated from the following TL definition:
    ```tl
    starsRating#1b0e4f07 flags:# level:int current_level_stars:long stars:long next_level_stars:flags.0?long = StarsRating
    ```
    """
    def __new__(
        cls,
        level: int,
        current_level_stars: int,
        stars: int,
        next_level_stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftCollection(TLObject):
    """
    [Read `starGiftCollection` docs](https://core.telegram.org/constructor/starGiftCollection).

    Generated from the following TL definition:
    ```tl
    starGiftCollection#9d6b13b0 flags:# collection_id:int title:string icon:flags.0?Document gifts_count:int hash:long = StarGiftCollection
    ```
    """
    def __new__(
        cls,
        collection_id: int,
        title: str,
        icon: Optional[types.DocumentEmpty | types.Document],
        gifts_count: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StoryAlbum(TLObject):
    """
    [Read `storyAlbum` docs](https://core.telegram.org/constructor/storyAlbum).

    Generated from the following TL definition:
    ```tl
    storyAlbum#9325705a flags:# album_id:int title:string icon_photo:flags.0?Photo icon_video:flags.1?Document = StoryAlbum
    ```
    """
    def __new__(
        cls,
        album_id: int,
        title: str,
        icon_photo: Optional[types.PhotoEmpty | types.Photo],
        icon_video: Optional[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SearchPostsFlood(TLObject):
    """
    [Read `searchPostsFlood` docs](https://core.telegram.org/constructor/searchPostsFlood).

    Generated from the following TL definition:
    ```tl
    searchPostsFlood#3e0b5b6a flags:# query_is_free:flags.0?true total_daily:int remains:int wait_till:flags.1?int stars_amount:long = SearchPostsFlood
    ```
    """
    def __new__(
        cls,
        query_is_free: bool,
        total_daily: int,
        remains: int,
        wait_till: Optional[int],
        stars_amount: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ProfileTabPosts(TLObject):
    """
    [Read `profileTabPosts` docs](https://core.telegram.org/constructor/profileTabPosts).

    Generated from the following TL definition:
    ```tl
    profileTabPosts#b98cd696 = ProfileTab
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ProfileTabGifts(TLObject):
    """
    [Read `profileTabGifts` docs](https://core.telegram.org/constructor/profileTabGifts).

    Generated from the following TL definition:
    ```tl
    profileTabGifts#4d4bd46a = ProfileTab
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ProfileTabMedia(TLObject):
    """
    [Read `profileTabMedia` docs](https://core.telegram.org/constructor/profileTabMedia).

    Generated from the following TL definition:
    ```tl
    profileTabMedia#72c64955 = ProfileTab
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ProfileTabFiles(TLObject):
    """
    [Read `profileTabFiles` docs](https://core.telegram.org/constructor/profileTabFiles).

    Generated from the following TL definition:
    ```tl
    profileTabFiles#ab339c00 = ProfileTab
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ProfileTabMusic(TLObject):
    """
    [Read `profileTabMusic` docs](https://core.telegram.org/constructor/profileTabMusic).

    Generated from the following TL definition:
    ```tl
    profileTabMusic#9f27d26e = ProfileTab
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ProfileTabVoice(TLObject):
    """
    [Read `profileTabVoice` docs](https://core.telegram.org/constructor/profileTabVoice).

    Generated from the following TL definition:
    ```tl
    profileTabVoice#e477092e = ProfileTab
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ProfileTabLinks(TLObject):
    """
    [Read `profileTabLinks` docs](https://core.telegram.org/constructor/profileTabLinks).

    Generated from the following TL definition:
    ```tl
    profileTabLinks#d3656499 = ProfileTab
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ProfileTabGifs(TLObject):
    """
    [Read `profileTabGifs` docs](https://core.telegram.org/constructor/profileTabGifs).

    Generated from the following TL definition:
    ```tl
    profileTabGifs#a2c0f695 = ProfileTab
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputChatThemeEmpty(TLObject):
    """
    [Read `inputChatThemeEmpty` docs](https://core.telegram.org/constructor/inputChatThemeEmpty).

    Generated from the following TL definition:
    ```tl
    inputChatThemeEmpty#83268483 = InputChatTheme
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputChatTheme(TLObject):
    """
    [Read `inputChatTheme` docs](https://core.telegram.org/constructor/inputChatTheme).

    Generated from the following TL definition:
    ```tl
    inputChatTheme#c93de95c emoticon:string = InputChatTheme
    ```
    """
    def __new__(
        cls,
        emoticon: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputChatThemeUniqueGift(TLObject):
    """
    [Read `inputChatThemeUniqueGift` docs](https://core.telegram.org/constructor/inputChatThemeUniqueGift).

    Generated from the following TL definition:
    ```tl
    inputChatThemeUniqueGift#87e5dfe4 slug:string = InputChatTheme
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftUpgradePrice(TLObject):
    """
    [Read `starGiftUpgradePrice` docs](https://core.telegram.org/constructor/starGiftUpgradePrice).

    Generated from the following TL definition:
    ```tl
    starGiftUpgradePrice#99ea331d date:int upgrade_stars:long = StarGiftUpgradePrice
    ```
    """
    def __new__(
        cls,
        date: int,
        upgrade_stars: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupCallMessage(TLObject):
    """
    [Read `groupCallMessage` docs](https://core.telegram.org/constructor/groupCallMessage).

    Generated from the following TL definition:
    ```tl
    groupCallMessage#1a8afc7e flags:# from_admin:flags.1?true id:int from_id:Peer date:int message:TextWithEntities paid_message_stars:flags.0?long = GroupCallMessage
    ```
    """
    def __new__(
        cls,
        from_admin: bool,
        id: int,
        from_id: types.PeerUser | types.PeerChat | types.PeerChannel,
        date: int,
        message: types.TextWithEntities,
        paid_message_stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GroupCallDonor(TLObject):
    """
    [Read `groupCallDonor` docs](https://core.telegram.org/constructor/groupCallDonor).

    Generated from the following TL definition:
    ```tl
    groupCallDonor#ee430c85 flags:# top:flags.0?true my:flags.1?true peer_id:flags.3?Peer stars:long = GroupCallDonor
    ```
    """
    def __new__(
        cls,
        top: bool,
        my: bool,
        peer_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        stars: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RecentStory(TLObject):
    """
    [Read `recentStory` docs](https://core.telegram.org/constructor/recentStory).

    Generated from the following TL definition:
    ```tl
    recentStory#711d692d flags:# live:flags.0?true max_id:flags.1?int = RecentStory
    ```
    """
    def __new__(
        cls,
        live: bool,
        max_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AuctionBidLevel(TLObject):
    """
    [Read `auctionBidLevel` docs](https://core.telegram.org/constructor/auctionBidLevel).

    Generated from the following TL definition:
    ```tl
    auctionBidLevel#310240cc pos:int amount:long date:int = AuctionBidLevel
    ```
    """
    def __new__(
        cls,
        pos: int,
        amount: int,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAuctionStateNotModified(TLObject):
    """
    [Read `starGiftAuctionStateNotModified` docs](https://core.telegram.org/constructor/starGiftAuctionStateNotModified).

    Generated from the following TL definition:
    ```tl
    starGiftAuctionStateNotModified#fe333952 = StarGiftAuctionState
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAuctionState(TLObject):
    """
    [Read `starGiftAuctionState` docs](https://core.telegram.org/constructor/starGiftAuctionState).

    Generated from the following TL definition:
    ```tl
    starGiftAuctionState#771a4e66 version:int start_date:int end_date:int min_bid_amount:long bid_levels:Vector<AuctionBidLevel> top_bidders:Vector<long> next_round_at:int last_gift_num:int gifts_left:int current_round:int total_rounds:int rounds:Vector<StarGiftAuctionRound> = StarGiftAuctionState
    ```
    """
    def __new__(
        cls,
        version: int,
        start_date: int,
        end_date: int,
        min_bid_amount: int,
        bid_levels: Sequence[types.AuctionBidLevel],
        top_bidders: Sequence[int],
        next_round_at: int,
        last_gift_num: int,
        gifts_left: int,
        current_round: int,
        total_rounds: int,
        rounds: Sequence[types.StarGiftAuctionRound | types.StarGiftAuctionRoundExtendable],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAuctionStateFinished(TLObject):
    """
    [Read `starGiftAuctionStateFinished` docs](https://core.telegram.org/constructor/starGiftAuctionStateFinished).

    Generated from the following TL definition:
    ```tl
    starGiftAuctionStateFinished#972dabbf flags:# start_date:int end_date:int average_price:long listed_count:flags.0?int fragment_listed_count:flags.1?int fragment_listed_url:flags.1?string = StarGiftAuctionState
    ```
    """
    def __new__(
        cls,
        start_date: int,
        end_date: int,
        average_price: int,
        listed_count: Optional[int],
        fragment_listed_count: Optional[int],
        fragment_listed_url: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAuctionUserState(TLObject):
    """
    [Read `starGiftAuctionUserState` docs](https://core.telegram.org/constructor/starGiftAuctionUserState).

    Generated from the following TL definition:
    ```tl
    starGiftAuctionUserState#2eeed1c4 flags:# returned:flags.1?true bid_amount:flags.0?long bid_date:flags.0?int min_bid_amount:flags.0?long bid_peer:flags.0?Peer acquired_count:int = StarGiftAuctionUserState
    ```
    """
    def __new__(
        cls,
        returned: bool,
        bid_amount: Optional[int],
        bid_date: Optional[int],
        min_bid_amount: Optional[int],
        bid_peer: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        acquired_count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAuctionAcquiredGift(TLObject):
    """
    [Read `starGiftAuctionAcquiredGift` docs](https://core.telegram.org/constructor/starGiftAuctionAcquiredGift).

    Generated from the following TL definition:
    ```tl
    starGiftAuctionAcquiredGift#42b00348 flags:# name_hidden:flags.0?true peer:Peer date:int bid_amount:long round:int pos:int message:flags.1?TextWithEntities gift_num:flags.2?int = StarGiftAuctionAcquiredGift
    ```
    """
    def __new__(
        cls,
        name_hidden: bool,
        peer: types.PeerUser | types.PeerChat | types.PeerChannel,
        date: int,
        bid_amount: int,
        round: int,
        pos: int,
        message: Optional[types.TextWithEntities],
        gift_num: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftActiveAuctionState(TLObject):
    """
    [Read `starGiftActiveAuctionState` docs](https://core.telegram.org/constructor/starGiftActiveAuctionState).

    Generated from the following TL definition:
    ```tl
    starGiftActiveAuctionState#d31bc45d gift:StarGift state:StarGiftAuctionState user_state:StarGiftAuctionUserState = StarGiftActiveAuctionState
    ```
    """
    def __new__(
        cls,
        gift: types.StarGift | types.StarGiftUnique,
        state: types.StarGiftAuctionStateNotModified | types.StarGiftAuctionState | types.StarGiftAuctionStateFinished,
        user_state: types.StarGiftAuctionUserState,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStarGiftAuction(TLObject):
    """
    [Read `inputStarGiftAuction` docs](https://core.telegram.org/constructor/inputStarGiftAuction).

    Generated from the following TL definition:
    ```tl
    inputStarGiftAuction#2e16c98 gift_id:long = InputStarGiftAuction
    ```
    """
    def __new__(
        cls,
        gift_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputStarGiftAuctionSlug(TLObject):
    """
    [Read `inputStarGiftAuctionSlug` docs](https://core.telegram.org/constructor/inputStarGiftAuctionSlug).

    Generated from the following TL definition:
    ```tl
    inputStarGiftAuctionSlug#7ab58308 slug:string = InputStarGiftAuction
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Passkey(TLObject):
    """
    [Read `passkey` docs](https://core.telegram.org/constructor/passkey).

    Generated from the following TL definition:
    ```tl
    passkey#98613ebf flags:# id:string name:string date:int software_emoji_id:flags.0?long last_usage_date:flags.1?int = Passkey
    ```
    """
    def __new__(
        cls,
        id: str,
        name: str,
        date: int,
        software_emoji_id: Optional[int],
        last_usage_date: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPasskeyResponseRegister(TLObject):
    """
    [Read `inputPasskeyResponseRegister` docs](https://core.telegram.org/constructor/inputPasskeyResponseRegister).

    Generated from the following TL definition:
    ```tl
    inputPasskeyResponseRegister#3e63935c client_data:DataJSON attestation_data:bytes = InputPasskeyResponse
    ```
    """
    def __new__(
        cls,
        client_data: types.DataJson,
        attestation_data: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPasskeyResponseLogin(TLObject):
    """
    [Read `inputPasskeyResponseLogin` docs](https://core.telegram.org/constructor/inputPasskeyResponseLogin).

    Generated from the following TL definition:
    ```tl
    inputPasskeyResponseLogin#c31fc14a client_data:DataJSON authenticator_data:bytes signature:bytes user_handle:string = InputPasskeyResponse
    ```
    """
    def __new__(
        cls,
        client_data: types.DataJson,
        authenticator_data: bytes,
        signature: bytes,
        user_handle: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPasskeyCredentialPublicKey(TLObject):
    """
    [Read `inputPasskeyCredentialPublicKey` docs](https://core.telegram.org/constructor/inputPasskeyCredentialPublicKey).

    Generated from the following TL definition:
    ```tl
    inputPasskeyCredentialPublicKey#3c27b78f id:string raw_id:string response:InputPasskeyResponse = InputPasskeyCredential
    ```
    """
    def __new__(
        cls,
        id: str,
        raw_id: str,
        response: types.InputPasskeyResponseRegister | types.InputPasskeyResponseLogin,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InputPasskeyCredentialFirebasePnv(TLObject):
    """
    [Read `inputPasskeyCredentialFirebasePNV` docs](https://core.telegram.org/constructor/inputPasskeyCredentialFirebasePNV).

    Generated from the following TL definition:
    ```tl
    inputPasskeyCredentialFirebasePNV#5b1ccb28 pnv_token:string = InputPasskeyCredential
    ```
    """
    def __new__(
        cls,
        pnv_token: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftBackground(TLObject):
    """
    [Read `starGiftBackground` docs](https://core.telegram.org/constructor/starGiftBackground).

    Generated from the following TL definition:
    ```tl
    starGiftBackground#aff56398 center_color:int edge_color:int text_color:int = StarGiftBackground
    ```
    """
    def __new__(
        cls,
        center_color: int,
        edge_color: int,
        text_color: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAuctionRound(TLObject):
    """
    [Read `starGiftAuctionRound` docs](https://core.telegram.org/constructor/starGiftAuctionRound).

    Generated from the following TL definition:
    ```tl
    starGiftAuctionRound#3aae0528 num:int duration:int = StarGiftAuctionRound
    ```
    """
    def __new__(
        cls,
        num: int,
        duration: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAuctionRoundExtendable(TLObject):
    """
    [Read `starGiftAuctionRoundExtendable` docs](https://core.telegram.org/constructor/starGiftAuctionRoundExtendable).

    Generated from the following TL definition:
    ```tl
    starGiftAuctionRoundExtendable#aa021e5 num:int duration:int extend_top:int extend_window:int = StarGiftAuctionRound
    ```
    """
    def __new__(
        cls,
        num: int,
        duration: int,
        extend_top: int,
        extend_window: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResPq(TLObject):
    """
    [Read `resPQ` docs](https://core.telegram.org/constructor/resPQ).

    Generated from the following TL definition:
    ```tl
    resPQ#5162463 nonce:int128 server_nonce:int128 pq:bytes server_public_key_fingerprints:Vector<long> = ResPQ
    ```
    """
    def __new__(
        cls,
        nonce: int,
        server_nonce: int,
        pq: bytes,
        server_public_key_fingerprints: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PQInnerData(TLObject):
    """
    [Read `p_q_inner_data` docs](https://core.telegram.org/constructor/p_q_inner_data).

    Generated from the following TL definition:
    ```tl
    p_q_inner_data#83c95aec pq:bytes p:bytes q:bytes nonce:int128 server_nonce:int128 new_nonce:int256 = P_Q_inner_data
    ```
    """
    def __new__(
        cls,
        pq: bytes,
        p: bytes,
        q: bytes,
        nonce: int,
        server_nonce: int,
        new_nonce: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PQInnerDataDc(TLObject):
    """
    [Read `p_q_inner_data_dc` docs](https://core.telegram.org/constructor/p_q_inner_data_dc).

    Generated from the following TL definition:
    ```tl
    p_q_inner_data_dc#a9f55f95 pq:bytes p:bytes q:bytes nonce:int128 server_nonce:int128 new_nonce:int256 dc:int = P_Q_inner_data
    ```
    """
    def __new__(
        cls,
        pq: bytes,
        p: bytes,
        q: bytes,
        nonce: int,
        server_nonce: int,
        new_nonce: int,
        dc: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PQInnerDataTemp(TLObject):
    """
    [Read `p_q_inner_data_temp` docs](https://core.telegram.org/constructor/p_q_inner_data_temp).

    Generated from the following TL definition:
    ```tl
    p_q_inner_data_temp#3c6a84d4 pq:bytes p:bytes q:bytes nonce:int128 server_nonce:int128 new_nonce:int256 expires_in:int = P_Q_inner_data
    ```
    """
    def __new__(
        cls,
        pq: bytes,
        p: bytes,
        q: bytes,
        nonce: int,
        server_nonce: int,
        new_nonce: int,
        expires_in: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PQInnerDataTempDc(TLObject):
    """
    [Read `p_q_inner_data_temp_dc` docs](https://core.telegram.org/constructor/p_q_inner_data_temp_dc).

    Generated from the following TL definition:
    ```tl
    p_q_inner_data_temp_dc#56fddf88 pq:bytes p:bytes q:bytes nonce:int128 server_nonce:int128 new_nonce:int256 dc:int expires_in:int = P_Q_inner_data
    ```
    """
    def __new__(
        cls,
        pq: bytes,
        p: bytes,
        q: bytes,
        nonce: int,
        server_nonce: int,
        new_nonce: int,
        dc: int,
        expires_in: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BindAuthKeyInner(TLObject):
    """
    [Read `bind_auth_key_inner` docs](https://core.telegram.org/constructor/bind_auth_key_inner).

    Generated from the following TL definition:
    ```tl
    bind_auth_key_inner#75a3f765 nonce:long temp_auth_key_id:long perm_auth_key_id:long temp_session_id:long expires_at:int = BindAuthKeyInner
    ```
    """
    def __new__(
        cls,
        nonce: int,
        temp_auth_key_id: int,
        perm_auth_key_id: int,
        temp_session_id: int,
        expires_at: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ServerDhParamsFail(TLObject):
    """
    [Read `server_DH_params_fail` docs](https://core.telegram.org/constructor/server_DH_params_fail).

    Generated from the following TL definition:
    ```tl
    server_DH_params_fail#79cb045d nonce:int128 server_nonce:int128 new_nonce_hash:int128 = Server_DH_Params
    ```
    """
    def __new__(
        cls,
        nonce: int,
        server_nonce: int,
        new_nonce_hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ServerDhParamsOk(TLObject):
    """
    [Read `server_DH_params_ok` docs](https://core.telegram.org/constructor/server_DH_params_ok).

    Generated from the following TL definition:
    ```tl
    server_DH_params_ok#d0e8075c nonce:int128 server_nonce:int128 encrypted_answer:bytes = Server_DH_Params
    ```
    """
    def __new__(
        cls,
        nonce: int,
        server_nonce: int,
        encrypted_answer: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ServerDhInnerData(TLObject):
    """
    [Read `server_DH_inner_data` docs](https://core.telegram.org/constructor/server_DH_inner_data).

    Generated from the following TL definition:
    ```tl
    server_DH_inner_data#b5890dba nonce:int128 server_nonce:int128 g:int dh_prime:bytes g_a:bytes server_time:int = Server_DH_inner_data
    ```
    """
    def __new__(
        cls,
        nonce: int,
        server_nonce: int,
        g: int,
        dh_prime: bytes,
        g_a: bytes,
        server_time: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ClientDhInnerData(TLObject):
    """
    [Read `client_DH_inner_data` docs](https://core.telegram.org/constructor/client_DH_inner_data).

    Generated from the following TL definition:
    ```tl
    client_DH_inner_data#6643b654 nonce:int128 server_nonce:int128 retry_id:long g_b:bytes = Client_DH_Inner_Data
    ```
    """
    def __new__(
        cls,
        nonce: int,
        server_nonce: int,
        retry_id: int,
        g_b: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DhGenOk(TLObject):
    """
    [Read `dh_gen_ok` docs](https://core.telegram.org/constructor/dh_gen_ok).

    Generated from the following TL definition:
    ```tl
    dh_gen_ok#3bcbf734 nonce:int128 server_nonce:int128 new_nonce_hash1:int128 = Set_client_DH_params_answer
    ```
    """
    def __new__(
        cls,
        nonce: int,
        server_nonce: int,
        new_nonce_hash1: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DhGenRetry(TLObject):
    """
    [Read `dh_gen_retry` docs](https://core.telegram.org/constructor/dh_gen_retry).

    Generated from the following TL definition:
    ```tl
    dh_gen_retry#46dc1fb9 nonce:int128 server_nonce:int128 new_nonce_hash2:int128 = Set_client_DH_params_answer
    ```
    """
    def __new__(
        cls,
        nonce: int,
        server_nonce: int,
        new_nonce_hash2: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DhGenFail(TLObject):
    """
    [Read `dh_gen_fail` docs](https://core.telegram.org/constructor/dh_gen_fail).

    Generated from the following TL definition:
    ```tl
    dh_gen_fail#a69dae02 nonce:int128 server_nonce:int128 new_nonce_hash3:int128 = Set_client_DH_params_answer
    ```
    """
    def __new__(
        cls,
        nonce: int,
        server_nonce: int,
        new_nonce_hash3: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DestroyAuthKeyOk(TLObject):
    """
    [Read `destroy_auth_key_ok` docs](https://core.telegram.org/constructor/destroy_auth_key_ok).

    Generated from the following TL definition:
    ```tl
    destroy_auth_key_ok#f660e1d4 = DestroyAuthKeyRes
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DestroyAuthKeyNone(TLObject):
    """
    [Read `destroy_auth_key_none` docs](https://core.telegram.org/constructor/destroy_auth_key_none).

    Generated from the following TL definition:
    ```tl
    destroy_auth_key_none#a9f2259 = DestroyAuthKeyRes
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DestroyAuthKeyFail(TLObject):
    """
    [Read `destroy_auth_key_fail` docs](https://core.telegram.org/constructor/destroy_auth_key_fail).

    Generated from the following TL definition:
    ```tl
    destroy_auth_key_fail#ea109b13 = DestroyAuthKeyRes
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MsgsAck(TLObject):
    """
    [Read `msgs_ack` docs](https://core.telegram.org/constructor/msgs_ack).

    Generated from the following TL definition:
    ```tl
    msgs_ack#62d6b459 msg_ids:Vector<long> = MsgsAck
    ```
    """
    def __new__(
        cls,
        msg_ids: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BadMsgNotification(TLObject):
    """
    [Read `bad_msg_notification` docs](https://core.telegram.org/constructor/bad_msg_notification).

    Generated from the following TL definition:
    ```tl
    bad_msg_notification#a7eff811 bad_msg_id:long bad_msg_seqno:int error_code:int = BadMsgNotification
    ```
    """
    def __new__(
        cls,
        bad_msg_id: int,
        bad_msg_seqno: int,
        error_code: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BadServerSalt(TLObject):
    """
    [Read `bad_server_salt` docs](https://core.telegram.org/constructor/bad_server_salt).

    Generated from the following TL definition:
    ```tl
    bad_server_salt#edab447b bad_msg_id:long bad_msg_seqno:int error_code:int new_server_salt:long = BadMsgNotification
    ```
    """
    def __new__(
        cls,
        bad_msg_id: int,
        bad_msg_seqno: int,
        error_code: int,
        new_server_salt: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MsgsStateReq(TLObject):
    """
    [Read `msgs_state_req` docs](https://core.telegram.org/constructor/msgs_state_req).

    Generated from the following TL definition:
    ```tl
    msgs_state_req#da69fb52 msg_ids:Vector<long> = MsgsStateReq
    ```
    """
    def __new__(
        cls,
        msg_ids: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MsgsStateInfo(TLObject):
    """
    [Read `msgs_state_info` docs](https://core.telegram.org/constructor/msgs_state_info).

    Generated from the following TL definition:
    ```tl
    msgs_state_info#4deb57d req_msg_id:long info:bytes = MsgsStateInfo
    ```
    """
    def __new__(
        cls,
        req_msg_id: int,
        info: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MsgsAllInfo(TLObject):
    """
    [Read `msgs_all_info` docs](https://core.telegram.org/constructor/msgs_all_info).

    Generated from the following TL definition:
    ```tl
    msgs_all_info#8cc0d131 msg_ids:Vector<long> info:bytes = MsgsAllInfo
    ```
    """
    def __new__(
        cls,
        msg_ids: Sequence[int],
        info: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MsgDetailedInfo(TLObject):
    """
    [Read `msg_detailed_info` docs](https://core.telegram.org/constructor/msg_detailed_info).

    Generated from the following TL definition:
    ```tl
    msg_detailed_info#276d3ec6 msg_id:long answer_msg_id:long bytes:int status:int = MsgDetailedInfo
    ```
    """
    def __new__(
        cls,
        msg_id: int,
        answer_msg_id: int,
        bytes: int,
        status: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MsgNewDetailedInfo(TLObject):
    """
    [Read `msg_new_detailed_info` docs](https://core.telegram.org/constructor/msg_new_detailed_info).

    Generated from the following TL definition:
    ```tl
    msg_new_detailed_info#809db6df answer_msg_id:long bytes:int status:int = MsgDetailedInfo
    ```
    """
    def __new__(
        cls,
        answer_msg_id: int,
        bytes: int,
        status: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MsgResendReq(TLObject):
    """
    [Read `msg_resend_req` docs](https://core.telegram.org/constructor/msg_resend_req).

    Generated from the following TL definition:
    ```tl
    msg_resend_req#7d861a08 msg_ids:Vector<long> = MsgResendReq
    ```
    """
    def __new__(
        cls,
        msg_ids: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class MsgResendAnsReq(TLObject):
    """
    [Read `msg_resend_ans_req` docs](https://core.telegram.org/constructor/msg_resend_ans_req).

    Generated from the following TL definition:
    ```tl
    msg_resend_ans_req#8610baeb msg_ids:Vector<long> = MsgResendReq
    ```
    """
    def __new__(
        cls,
        msg_ids: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RpcError(TLObject):
    """
    [Read `rpc_error` docs](https://core.telegram.org/constructor/rpc_error).

    Generated from the following TL definition:
    ```tl
    rpc_error#2144ca19 error_code:int error_message:string = RpcError
    ```
    """
    def __new__(
        cls,
        error_code: int,
        error_message: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RpcAnswerUnknown(TLObject):
    """
    [Read `rpc_answer_unknown` docs](https://core.telegram.org/constructor/rpc_answer_unknown).

    Generated from the following TL definition:
    ```tl
    rpc_answer_unknown#5e2ad36e = RpcDropAnswer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RpcAnswerDroppedRunning(TLObject):
    """
    [Read `rpc_answer_dropped_running` docs](https://core.telegram.org/constructor/rpc_answer_dropped_running).

    Generated from the following TL definition:
    ```tl
    rpc_answer_dropped_running#cd78e586 = RpcDropAnswer
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RpcAnswerDropped(TLObject):
    """
    [Read `rpc_answer_dropped` docs](https://core.telegram.org/constructor/rpc_answer_dropped).

    Generated from the following TL definition:
    ```tl
    rpc_answer_dropped#a43ad8b7 msg_id:long seq_no:int bytes:int = RpcDropAnswer
    ```
    """
    def __new__(
        cls,
        msg_id: int,
        seq_no: int,
        bytes: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FutureSalt(TLObject):
    """
    [Read `future_salt` docs](https://core.telegram.org/constructor/future_salt).

    Generated from the following TL definition:
    ```tl
    future_salt#949d9dc valid_since:int valid_until:int salt:long = FutureSalt
    ```
    """
    def __new__(
        cls,
        valid_since: int,
        valid_until: int,
        salt: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FutureSalts(TLObject):
    """
    [Read `future_salts` docs](https://core.telegram.org/constructor/future_salts).

    Generated from the following TL definition:
    ```tl
    future_salts#ae500895 req_msg_id:long now:int salts:vector<future_salt> = FutureSalts
    ```
    """
    def __new__(
        cls,
        req_msg_id: int,
        now: int,
        salts: Sequence[types.FutureSalt],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Pong(TLObject):
    """
    [Read `pong` docs](https://core.telegram.org/constructor/pong).

    Generated from the following TL definition:
    ```tl
    pong#347773c5 msg_id:long ping_id:long = Pong
    ```
    """
    def __new__(
        cls,
        msg_id: int,
        ping_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DestroySessionOk(TLObject):
    """
    [Read `destroy_session_ok` docs](https://core.telegram.org/constructor/destroy_session_ok).

    Generated from the following TL definition:
    ```tl
    destroy_session_ok#e22045fc session_id:long = DestroySessionRes
    ```
    """
    def __new__(
        cls,
        session_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DestroySessionNone(TLObject):
    """
    [Read `destroy_session_none` docs](https://core.telegram.org/constructor/destroy_session_none).

    Generated from the following TL definition:
    ```tl
    destroy_session_none#62d350c9 session_id:long = DestroySessionRes
    ```
    """
    def __new__(
        cls,
        session_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class NewSessionCreated(TLObject):
    """
    [Read `new_session_created` docs](https://core.telegram.org/constructor/new_session_created).

    Generated from the following TL definition:
    ```tl
    new_session_created#9ec20908 first_msg_id:long unique_id:long server_salt:long = NewSession
    ```
    """
    def __new__(
        cls,
        first_msg_id: int,
        unique_id: int,
        server_salt: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class HttpWait(TLObject):
    """
    [Read `http_wait` docs](https://core.telegram.org/constructor/http_wait).

    Generated from the following TL definition:
    ```tl
    http_wait#9299359f max_delay:int wait_after:int max_wait:int = HttpWait
    ```
    """
    def __new__(
        cls,
        max_delay: int,
        wait_after: int,
        max_wait: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class IpPort(TLObject):
    """
    [Read `ipPort` docs](https://core.telegram.org/constructor/ipPort).

    Generated from the following TL definition:
    ```tl
    ipPort#d433ad73 ipv4:int port:int = IpPort
    ```
    """
    def __new__(
        cls,
        ipv4: int,
        port: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class IpPortSecret(TLObject):
    """
    [Read `ipPortSecret` docs](https://core.telegram.org/constructor/ipPortSecret).

    Generated from the following TL definition:
    ```tl
    ipPortSecret#37982646 ipv4:int port:int secret:bytes = IpPort
    ```
    """
    def __new__(
        cls,
        ipv4: int,
        port: int,
        secret: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AccessPointRule(TLObject):
    """
    [Read `accessPointRule` docs](https://core.telegram.org/constructor/accessPointRule).

    Generated from the following TL definition:
    ```tl
    accessPointRule#4679b65f phone_prefix_rules:bytes dc_id:int ips:vector<IpPort> = AccessPointRule
    ```
    """
    def __new__(
        cls,
        phone_prefix_rules: bytes,
        dc_id: int,
        ips: Sequence[types.IpPort | types.IpPortSecret],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TlsClientHello(TLObject):
    """
    [Read `tlsClientHello` docs](https://core.telegram.org/constructor/tlsClientHello).

    Generated from the following TL definition:
    ```tl
    tlsClientHello#6c52c484 blocks:vector<TlsBlock> = TlsClientHello
    ```
    """
    def __new__(
        cls,
        blocks: Sequence[types.TlsBlockString | types.TlsBlockRandom | types.TlsBlockZero | types.TlsBlockDomain | types.TlsBlockGrease | types.TlsBlockPublicKey | types.TlsBlockScope],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TlsBlockString(TLObject):
    """
    [Read `tlsBlockString` docs](https://core.telegram.org/constructor/tlsBlockString).

    Generated from the following TL definition:
    ```tl
    tlsBlockString#b2b51dca data:bytes = TlsBlock
    ```
    """
    def __new__(
        cls,
        data: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TlsBlockRandom(TLObject):
    """
    [Read `tlsBlockRandom` docs](https://core.telegram.org/constructor/tlsBlockRandom).

    Generated from the following TL definition:
    ```tl
    tlsBlockRandom#4d4dc41e length:int = TlsBlock
    ```
    """
    def __new__(
        cls,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TlsBlockZero(TLObject):
    """
    [Read `tlsBlockZero` docs](https://core.telegram.org/constructor/tlsBlockZero).

    Generated from the following TL definition:
    ```tl
    tlsBlockZero#9333afb length:int = TlsBlock
    ```
    """
    def __new__(
        cls,
        length: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TlsBlockDomain(TLObject):
    """
    [Read `tlsBlockDomain` docs](https://core.telegram.org/constructor/tlsBlockDomain).

    Generated from the following TL definition:
    ```tl
    tlsBlockDomain#10e8636f = TlsBlock
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TlsBlockGrease(TLObject):
    """
    [Read `tlsBlockGrease` docs](https://core.telegram.org/constructor/tlsBlockGrease).

    Generated from the following TL definition:
    ```tl
    tlsBlockGrease#e675a1c1 seed:int = TlsBlock
    ```
    """
    def __new__(
        cls,
        seed: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TlsBlockPublicKey(TLObject):
    """
    [Read `tlsBlockPublicKey` docs](https://core.telegram.org/constructor/tlsBlockPublicKey).

    Generated from the following TL definition:
    ```tl
    tlsBlockPublicKey#9eb95b5c = TlsBlock
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TlsBlockScope(TLObject):
    """
    [Read `tlsBlockScope` docs](https://core.telegram.org/constructor/tlsBlockScope).

    Generated from the following TL definition:
    ```tl
    tlsBlockScope#e725d44f entries:Vector<TlsBlock> = TlsBlock
    ```
    """
    def __new__(
        cls,
        entries: Sequence[types.TlsBlockString | types.TlsBlockRandom | types.TlsBlockZero | types.TlsBlockDomain | types.TlsBlockGrease | types.TlsBlockPublicKey | types.TlsBlockScope],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

