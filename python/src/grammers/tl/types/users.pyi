from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class UserFull(TLObject):
    """
    [Read `users.userFull` docs](https://core.telegram.org/constructor/users.userFull).

    Generated from the following TL definition:
    ```tl
    users.userFull#3b6d152e full_user:UserFull chats:Vector<Chat> users:Vector<User> = users.UserFull
    ```
    """
    def __new__(
        cls,
        full_user: types.UserFull,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Users(TLObject):
    """
    [Read `users.users` docs](https://core.telegram.org/constructor/users.users).

    Generated from the following TL definition:
    ```tl
    users.users#62d706b8 users:Vector<User> = users.Users
    ```
    """
    def __new__(
        cls,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UsersSlice(TLObject):
    """
    [Read `users.usersSlice` docs](https://core.telegram.org/constructor/users.usersSlice).

    Generated from the following TL definition:
    ```tl
    users.usersSlice#315a4974 count:int users:Vector<User> = users.Users
    ```
    """
    def __new__(
        cls,
        count: int,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedMusicNotModified(TLObject):
    """
    [Read `users.savedMusicNotModified` docs](https://core.telegram.org/constructor/users.savedMusicNotModified).

    Generated from the following TL definition:
    ```tl
    users.savedMusicNotModified#e3878aa4 count:int = users.SavedMusic
    ```
    """
    def __new__(
        cls,
        count: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedMusic(TLObject):
    """
    [Read `users.savedMusic` docs](https://core.telegram.org/constructor/users.savedMusic).

    Generated from the following TL definition:
    ```tl
    users.savedMusic#34a2f297 count:int documents:Vector<Document> = users.SavedMusic
    ```
    """
    def __new__(
        cls,
        count: int,
        documents: Sequence[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

