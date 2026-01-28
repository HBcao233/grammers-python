from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class File(TLObject):
    """
    [Read `upload.file` docs](https://core.telegram.org/constructor/upload.file).

    Generated from the following TL definition:
    ```tl
    upload.file#96a18d5 type:storage.FileType mtime:int bytes:bytes = upload.File
    ```
    """
    def __new__(
        cls,
        type: types.storage.FileUnknown | types.storage.FilePartial | types.storage.FileJpeg | types.storage.FileGif | types.storage.FilePng | types.storage.FilePdf | types.storage.FileMp3 | types.storage.FileMov | types.storage.FileMp4 | types.storage.FileWebp,
        mtime: int,
        bytes: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FileCdnRedirect(TLObject):
    """
    [Read `upload.fileCdnRedirect` docs](https://core.telegram.org/constructor/upload.fileCdnRedirect).

    Generated from the following TL definition:
    ```tl
    upload.fileCdnRedirect#f18cda44 dc_id:int file_token:bytes encryption_key:bytes encryption_iv:bytes file_hashes:Vector<FileHash> = upload.File
    ```
    """
    def __new__(
        cls,
        dc_id: int,
        file_token: bytes,
        encryption_key: bytes,
        encryption_iv: bytes,
        file_hashes: Sequence[types.FileHash],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class WebFile(TLObject):
    """
    [Read `upload.webFile` docs](https://core.telegram.org/constructor/upload.webFile).

    Generated from the following TL definition:
    ```tl
    upload.webFile#21e753bc size:int mime_type:string file_type:storage.FileType mtime:int bytes:bytes = upload.WebFile
    ```
    """
    def __new__(
        cls,
        size: int,
        mime_type: str,
        file_type: types.storage.FileUnknown | types.storage.FilePartial | types.storage.FileJpeg | types.storage.FileGif | types.storage.FilePng | types.storage.FilePdf | types.storage.FileMp3 | types.storage.FileMov | types.storage.FileMp4 | types.storage.FileWebp,
        mtime: int,
        bytes: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CdnFileReuploadNeeded(TLObject):
    """
    [Read `upload.cdnFileReuploadNeeded` docs](https://core.telegram.org/constructor/upload.cdnFileReuploadNeeded).

    Generated from the following TL definition:
    ```tl
    upload.cdnFileReuploadNeeded#eea8e46e request_token:bytes = upload.CdnFile
    ```
    """
    def __new__(
        cls,
        request_token: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CdnFile(TLObject):
    """
    [Read `upload.cdnFile` docs](https://core.telegram.org/constructor/upload.cdnFile).

    Generated from the following TL definition:
    ```tl
    upload.cdnFile#a99fca4f bytes:bytes = upload.CdnFile
    ```
    """
    def __new__(
        cls,
        bytes: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

