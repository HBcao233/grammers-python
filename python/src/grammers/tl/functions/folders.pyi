from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class EditPeerFolders(TLRequest):
    """
    [Read `folders.editPeerFolders` docs](https://core.telegram.org/method/folders.editPeerFolders).

    Generated from the following TL definition:
    ```tl
    folders.editPeerFolders#6847d0ab folder_peers:Vector<InputFolderPeer> = Updates
    ```
    """
    def __new__(
        cls,
        folder_peers: Sequence[types.InputFolderPeer],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

