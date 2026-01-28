from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class Photos(TLObject):
    """
    [Read `photos.photos` docs](https://core.telegram.org/constructor/photos.photos).

    Generated from the following TL definition:
    ```tl
    photos.photos#8dca6aa5 photos:Vector<Photo> users:Vector<User> = photos.Photos
    ```
    """
    def __new__(
        cls,
        photos: Sequence[types.PhotoEmpty | types.Photo],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PhotosSlice(TLObject):
    """
    [Read `photos.photosSlice` docs](https://core.telegram.org/constructor/photos.photosSlice).

    Generated from the following TL definition:
    ```tl
    photos.photosSlice#15051f54 count:int photos:Vector<Photo> users:Vector<User> = photos.Photos
    ```
    """
    def __new__(
        cls,
        count: int,
        photos: Sequence[types.PhotoEmpty | types.Photo],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Photo(TLObject):
    """
    [Read `photos.photo` docs](https://core.telegram.org/constructor/photos.photo).

    Generated from the following TL definition:
    ```tl
    photos.photo#20212ca8 photo:Photo users:Vector<User> = photos.Photo
    ```
    """
    def __new__(
        cls,
        photo: types.PhotoEmpty | types.Photo,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

