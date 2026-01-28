from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class UpdateProfilePhoto(TLRequest):
    """
    [Read `photos.updateProfilePhoto` docs](https://core.telegram.org/method/photos.updateProfilePhoto).

    Generated from the following TL definition:
    ```tl
    photos.updateProfilePhoto#9e82039 flags:# fallback:flags.0?true bot:flags.1?InputUser id:InputPhoto = photos.Photo
    ```
    """
    def __new__(
        cls,
        fallback: bool,
        bot: Optional[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
        id: types.InputPhotoEmpty | types.InputPhoto,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UploadProfilePhoto(TLRequest):
    """
    [Read `photos.uploadProfilePhoto` docs](https://core.telegram.org/method/photos.uploadProfilePhoto).

    Generated from the following TL definition:
    ```tl
    photos.uploadProfilePhoto#388a3b5 flags:# fallback:flags.3?true bot:flags.5?InputUser file:flags.0?InputFile video:flags.1?InputFile video_start_ts:flags.2?double video_emoji_markup:flags.4?VideoSize = photos.Photo
    ```
    """
    def __new__(
        cls,
        fallback: bool,
        bot: Optional[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
        file: Optional[types.InputFile | types.InputFileBig | types.InputFileStoryDocument],
        video: Optional[types.InputFile | types.InputFileBig | types.InputFileStoryDocument],
        video_start_ts: Optional[float],
        video_emoji_markup: Optional[types.VideoSize | types.VideoSizeEmojiMarkup | types.VideoSizeStickerMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeletePhotos(TLRequest):
    """
    [Read `photos.deletePhotos` docs](https://core.telegram.org/method/photos.deletePhotos).

    Generated from the following TL definition:
    ```tl
    photos.deletePhotos#87cf7f2f id:Vector<InputPhoto> = Vector<long>
    ```
    """
    def __new__(
        cls,
        id: Sequence[types.InputPhotoEmpty | types.InputPhoto],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetUserPhotos(TLRequest):
    """
    [Read `photos.getUserPhotos` docs](https://core.telegram.org/method/photos.getUserPhotos).

    Generated from the following TL definition:
    ```tl
    photos.getUserPhotos#91cd32a8 user_id:InputUser offset:int max_id:long limit:int = photos.Photos
    ```
    """
    def __new__(
        cls,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        offset: int,
        max_id: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UploadContactProfilePhoto(TLRequest):
    """
    [Read `photos.uploadContactProfilePhoto` docs](https://core.telegram.org/method/photos.uploadContactProfilePhoto).

    Generated from the following TL definition:
    ```tl
    photos.uploadContactProfilePhoto#e14c4a71 flags:# suggest:flags.3?true save:flags.4?true user_id:InputUser file:flags.0?InputFile video:flags.1?InputFile video_start_ts:flags.2?double video_emoji_markup:flags.5?VideoSize = photos.Photo
    ```
    """
    def __new__(
        cls,
        suggest: bool,
        save: bool,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        file: Optional[types.InputFile | types.InputFileBig | types.InputFileStoryDocument],
        video: Optional[types.InputFile | types.InputFileBig | types.InputFileStoryDocument],
        video_start_ts: Optional[float],
        video_emoji_markup: Optional[types.VideoSize | types.VideoSizeEmojiMarkup | types.VideoSizeStickerMarkup],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

