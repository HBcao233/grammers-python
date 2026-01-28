from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class CreateStickerSet(TLRequest):
    """
    [Read `stickers.createStickerSet` docs](https://core.telegram.org/method/stickers.createStickerSet).

    Generated from the following TL definition:
    ```tl
    stickers.createStickerSet#9021ab67 flags:# masks:flags.0?true emojis:flags.5?true text_color:flags.6?true user_id:InputUser title:string short_name:string thumb:flags.2?InputDocument stickers:Vector<InputStickerSetItem> software:flags.3?string = messages.StickerSet
    ```
    """
    def __new__(
        cls,
        masks: bool,
        emojis: bool,
        text_color: bool,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        title: str,
        short_name: str,
        thumb: Optional[types.InputDocumentEmpty | types.InputDocument],
        stickers: Sequence[types.InputStickerSetItem],
        software: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RemoveStickerFromSet(TLRequest):
    """
    [Read `stickers.removeStickerFromSet` docs](https://core.telegram.org/method/stickers.removeStickerFromSet).

    Generated from the following TL definition:
    ```tl
    stickers.removeStickerFromSet#f7760f51 sticker:InputDocument = messages.StickerSet
    ```
    """
    def __new__(
        cls,
        sticker: types.InputDocumentEmpty | types.InputDocument,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChangeStickerPosition(TLRequest):
    """
    [Read `stickers.changeStickerPosition` docs](https://core.telegram.org/method/stickers.changeStickerPosition).

    Generated from the following TL definition:
    ```tl
    stickers.changeStickerPosition#ffb6d4ca sticker:InputDocument position:int = messages.StickerSet
    ```
    """
    def __new__(
        cls,
        sticker: types.InputDocumentEmpty | types.InputDocument,
        position: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AddStickerToSet(TLRequest):
    """
    [Read `stickers.addStickerToSet` docs](https://core.telegram.org/method/stickers.addStickerToSet).

    Generated from the following TL definition:
    ```tl
    stickers.addStickerToSet#8653febe stickerset:InputStickerSet sticker:InputStickerSetItem = messages.StickerSet
    ```
    """
    def __new__(
        cls,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
        sticker: types.InputStickerSetItem,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetStickerSetThumb(TLRequest):
    """
    [Read `stickers.setStickerSetThumb` docs](https://core.telegram.org/method/stickers.setStickerSetThumb).

    Generated from the following TL definition:
    ```tl
    stickers.setStickerSetThumb#a76a5392 flags:# stickerset:InputStickerSet thumb:flags.0?InputDocument thumb_document_id:flags.1?long = messages.StickerSet
    ```
    """
    def __new__(
        cls,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
        thumb: Optional[types.InputDocumentEmpty | types.InputDocument],
        thumb_document_id: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckShortName(TLRequest):
    """
    [Read `stickers.checkShortName` docs](https://core.telegram.org/method/stickers.checkShortName).

    Generated from the following TL definition:
    ```tl
    stickers.checkShortName#284b3639 short_name:string = Bool
    ```
    """
    def __new__(
        cls,
        short_name: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SuggestShortName(TLRequest):
    """
    [Read `stickers.suggestShortName` docs](https://core.telegram.org/method/stickers.suggestShortName).

    Generated from the following TL definition:
    ```tl
    stickers.suggestShortName#4dafc503 title:string = stickers.SuggestedShortName
    ```
    """
    def __new__(
        cls,
        title: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChangeSticker(TLRequest):
    """
    [Read `stickers.changeSticker` docs](https://core.telegram.org/method/stickers.changeSticker).

    Generated from the following TL definition:
    ```tl
    stickers.changeSticker#f5537ebc flags:# sticker:InputDocument emoji:flags.0?string mask_coords:flags.1?MaskCoords keywords:flags.2?string = messages.StickerSet
    ```
    """
    def __new__(
        cls,
        sticker: types.InputDocumentEmpty | types.InputDocument,
        emoji: Optional[str],
        mask_coords: Optional[types.MaskCoords],
        keywords: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RenameStickerSet(TLRequest):
    """
    [Read `stickers.renameStickerSet` docs](https://core.telegram.org/method/stickers.renameStickerSet).

    Generated from the following TL definition:
    ```tl
    stickers.renameStickerSet#124b1c00 stickerset:InputStickerSet title:string = messages.StickerSet
    ```
    """
    def __new__(
        cls,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
        title: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteStickerSet(TLRequest):
    """
    [Read `stickers.deleteStickerSet` docs](https://core.telegram.org/method/stickers.deleteStickerSet).

    Generated from the following TL definition:
    ```tl
    stickers.deleteStickerSet#87704394 stickerset:InputStickerSet = Bool
    ```
    """
    def __new__(
        cls,
        stickerset: types.InputStickerSetEmpty | types.InputStickerSetId | types.InputStickerSetShortName | types.InputStickerSetAnimatedEmoji | types.InputStickerSetDice | types.InputStickerSetAnimatedEmojiAnimations | types.InputStickerSetPremiumGifts | types.InputStickerSetEmojiGenericAnimations | types.InputStickerSetEmojiDefaultStatuses | types.InputStickerSetEmojiDefaultTopicIcons | types.InputStickerSetEmojiChannelDefaultStatuses | types.InputStickerSetTonGifts,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReplaceSticker(TLRequest):
    """
    [Read `stickers.replaceSticker` docs](https://core.telegram.org/method/stickers.replaceSticker).

    Generated from the following TL definition:
    ```tl
    stickers.replaceSticker#4696459a sticker:InputDocument new_sticker:InputStickerSetItem = messages.StickerSet
    ```
    """
    def __new__(
        cls,
        sticker: types.InputDocumentEmpty | types.InputDocument,
        new_sticker: types.InputStickerSetItem,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

