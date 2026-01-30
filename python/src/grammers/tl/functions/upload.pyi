from typing import final, Self
from grammers.tl import TLRequest, types

@final
class SaveFilePart(TLRequest):
    """
    [Read `upload.saveFilePart` docs](https://core.telegram.org/method/upload.saveFilePart).

    Generated from the following TL definition:
    ```tl
    upload.saveFilePart#b304a621 file_id:long file_part:int bytes:bytes = Bool
    ```
    """
    def __new__(
        cls,
        file_id: int,
        file_part: int,
        bytes: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetFile(TLRequest):
    """
    [Read `upload.getFile` docs](https://core.telegram.org/method/upload.getFile).

    Generated from the following TL definition:
    ```tl
    upload.getFile#be5335be flags:# precise:flags.0?true cdn_supported:flags.1?true location:InputFileLocation offset:long limit:int = upload.File
    ```
    """
    def __new__(
        cls,
        precise: bool,
        cdn_supported: bool,
        location: types.InputFileLocation | types.InputEncryptedFileLocation | types.InputDocumentFileLocation | types.InputSecureFileLocation | types.InputTakeoutFileLocation | types.InputPhotoFileLocation | types.InputPhotoLegacyFileLocation | types.InputPeerPhotoFileLocation | types.InputStickerSetThumb | types.InputGroupCallStream,
        offset: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveBigFilePart(TLRequest):
    """
    [Read `upload.saveBigFilePart` docs](https://core.telegram.org/method/upload.saveBigFilePart).

    Generated from the following TL definition:
    ```tl
    upload.saveBigFilePart#de7b673d file_id:long file_part:int file_total_parts:int bytes:bytes = Bool
    ```
    """
    def __new__(
        cls,
        file_id: int,
        file_part: int,
        file_total_parts: int,
        bytes: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetWebFile(TLRequest):
    """
    [Read `upload.getWebFile` docs](https://core.telegram.org/method/upload.getWebFile).

    Generated from the following TL definition:
    ```tl
    upload.getWebFile#24e6818d location:InputWebFileLocation offset:int limit:int = upload.WebFile
    ```
    """
    def __new__(
        cls,
        location: types.InputWebFileLocation | types.InputWebFileGeoPointLocation | types.InputWebFileAudioAlbumThumbLocation,
        offset: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetCdnFile(TLRequest):
    """
    [Read `upload.getCdnFile` docs](https://core.telegram.org/method/upload.getCdnFile).

    Generated from the following TL definition:
    ```tl
    upload.getCdnFile#395f69da file_token:bytes offset:long limit:int = upload.CdnFile
    ```
    """
    def __new__(
        cls,
        file_token: bytes,
        offset: int,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReuploadCdnFile(TLRequest):
    """
    [Read `upload.reuploadCdnFile` docs](https://core.telegram.org/method/upload.reuploadCdnFile).

    Generated from the following TL definition:
    ```tl
    upload.reuploadCdnFile#9b2754a8 file_token:bytes request_token:bytes = Vector<FileHash>
    ```
    """
    def __new__(
        cls,
        file_token: bytes,
        request_token: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetCdnFileHashes(TLRequest):
    """
    [Read `upload.getCdnFileHashes` docs](https://core.telegram.org/method/upload.getCdnFileHashes).

    Generated from the following TL definition:
    ```tl
    upload.getCdnFileHashes#91dc3f31 file_token:bytes offset:long = Vector<FileHash>
    ```
    """
    def __new__(
        cls,
        file_token: bytes,
        offset: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetFileHashes(TLRequest):
    """
    [Read `upload.getFileHashes` docs](https://core.telegram.org/method/upload.getFileHashes).

    Generated from the following TL definition:
    ```tl
    upload.getFileHashes#9156982a location:InputFileLocation offset:long = Vector<FileHash>
    ```
    """
    def __new__(
        cls,
        location: types.InputFileLocation | types.InputEncryptedFileLocation | types.InputDocumentFileLocation | types.InputSecureFileLocation | types.InputTakeoutFileLocation | types.InputPhotoFileLocation | types.InputPhotoLegacyFileLocation | types.InputPeerPhotoFileLocation | types.InputStickerSetThumb | types.InputGroupCallStream,
        offset: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

