import grammers.tl
from typing import Optional
from . import _rs
from . import errors
from . import crypto
from . import tl
from . import sessions
from .tl import TLObject, TLRequest, types, functions

__all__ = [
    '_rs',
    'crypto',
    'errors',
    'sessions',
    'tl',
    'TLObject',
    'TLRequest',
    'types',
    'functions',
    'Client',
]

class Client:
    @property
    def session(self) -> str: ...
    @property
    def me(self) -> sessions.Session: ...
    @property
    def api_id(self) -> int: ...
    @property
    def api_hash(self) -> str: ...
    @property
    def bot_token(self) -> Optional[str]: ...
    @property
    def use_ipv6(self) -> bool: ...
    @property
    def system_lang_code(self) -> str: ...
    @property
    def lang_code(self) -> str: ...
    async def is_authorized(self) -> bool: ...
    async def authorize(self) -> bool:
        """
        Terminal interactive login.
        """
        ...

    async def bot_sign_in(self) -> types.User: ...
    async def sign_out(self) -> types.auth.LoggedOut: ...
    async def disconnect(self) -> None: ...
    def __new__(
        cls,
        session: str,
        api_id: int | str,
        api_hash: str,
        *,
        bot_token: Optional[str] = None,
        app_version: Optional[str] = None,
        device_model: Optional[str] = None,
        system_version: Optional[str] = None,
        lang_code: Optional[str] = 'en',
        system_lang_code: Optional[str] = 'en',
        use_ipv6: bool = False,
    ) -> Client:
        r"""
        Create client instanse.

        Args:
            name (``str``):
                A name for the client, e.g.: "my_account".

            api_id (``int`` | ``str``, *optional*):
                The *api_id* part of the Telegram API key, as integer or string.
                E.g.: 12345 or "12345".

            api_hash (``str``, *optional*):
                The *api_hash* part of the Telegram API key, as string.
                E.g.: "0123456789abcdef0123456789abcdef".
        """
    async def invoke(self, request: grammers.tl.TLRequest) -> grammers.tl.TLObject: ...
    async def start(self) -> None:
        r"""
        Start login in to telegram
        """
    async def stop(self) -> None:
        r"""
        Stop client
        Calling clent's methods after stopping will raise ClientStoppedError.
        """
