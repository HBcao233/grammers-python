from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class GetUsers(TLRequest):
    """
    [Read `users.getUsers` docs](https://core.telegram.org/method/users.getUsers).

    Generated from the following TL definition:
    ```tl
    users.getUsers#d91a548 id:Vector<InputUser> = Vector<User>
    ```
    """
    def __new__(
        cls,
        id: Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetFullUser(TLRequest):
    """
    [Read `users.getFullUser` docs](https://core.telegram.org/method/users.getFullUser).

    Generated from the following TL definition:
    ```tl
    users.getFullUser#b60f5918 id:InputUser = users.UserFull
    ```
    """
    def __new__(
        cls,
        id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetSecureValueErrors(TLRequest):
    """
    [Read `users.setSecureValueErrors` docs](https://core.telegram.org/method/users.setSecureValueErrors).

    Generated from the following TL definition:
    ```tl
    users.setSecureValueErrors#90c894b5 id:InputUser errors:Vector<SecureValueError> = Bool
    ```
    """
    def __new__(
        cls,
        id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        errors: Sequence[types.SecureValueErrorData | types.SecureValueErrorFrontSide | types.SecureValueErrorReverseSide | types.SecureValueErrorSelfie | types.SecureValueErrorFile | types.SecureValueErrorFiles | types.SecureValueError | types.SecureValueErrorTranslationFile | types.SecureValueErrorTranslationFiles],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetRequirementsToContact(TLRequest):
    """
    [Read `users.getRequirementsToContact` docs](https://core.telegram.org/method/users.getRequirementsToContact).

    Generated from the following TL definition:
    ```tl
    users.getRequirementsToContact#d89a83a3 id:Vector<InputUser> = Vector<RequirementToContact>
    ```
    """
    def __new__(
        cls,
        id: Sequence[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSavedMusic(TLRequest):
    """
    [Read `users.getSavedMusic` docs](https://core.telegram.org/method/users.getSavedMusic).

    Generated from the following TL definition:
    ```tl
    users.getSavedMusic#788d7fe3 id:InputUser offset:int limit:int hash:long = users.SavedMusic
    ```
    """
    def __new__(
        cls,
        id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        offset: int,
        limit: int,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSavedMusicById(TLRequest):
    """
    [Read `users.getSavedMusicByID` docs](https://core.telegram.org/method/users.getSavedMusicByID).

    Generated from the following TL definition:
    ```tl
    users.getSavedMusicByID#7573a4e9 id:InputUser documents:Vector<InputDocument> = users.SavedMusic
    ```
    """
    def __new__(
        cls,
        id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        documents: Sequence[types.InputDocumentEmpty | types.InputDocument],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SuggestBirthday(TLRequest):
    """
    [Read `users.suggestBirthday` docs](https://core.telegram.org/method/users.suggestBirthday).

    Generated from the following TL definition:
    ```tl
    users.suggestBirthday#fc533372 id:InputUser birthday:Birthday = Updates
    ```
    """
    def __new__(
        cls,
        id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        birthday: types.Birthday,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

