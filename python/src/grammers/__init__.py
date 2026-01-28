from . import _rs
from ._rs import Client
import sys

sys.modules['grammers._rs.crypto'] = _rs.crypto
sys.modules['grammers._rs.errors'] = _rs.errors
sys.modules['grammers._rs.tl'] = _rs.tl
sys.modules['grammers._rs.sessions'] = _rs.sessions

from . import crypto, errors, tl
from .tl import TLObject, TLRequest, types, functions
from .sessions import SqliteSession
from typing import Optional
from collections.abc import Awaitable
import sys
import asyncio
import signal

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


class Client(Client):
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
    ):
        if isinstance(session, str):
            if not session.endswith('.session'):
                session = session + '.session'
            session = SqliteSession(session)

        return super().__new__(
            cls,
            session,
            api_id,
            api_hash,
            bot_token=bot_token,
            app_version=app_version,
            device_model=device_model,
            system_version=system_version,
            lang_code=lang_code,
            system_lang_code=system_lang_code,
            use_ipv6=use_ipv6,
        )

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        await self.stop()
        return False

    """
    async def authorize(self):
      if self.bot_token:
        return await self.sign_in_bot(self.bot_token)
      
      print(f"Welcome to Grammers {__version__}\n")
      
      phone = self.phone
      if callable(phone):
        phone = phone()
        if isinstance(phone, Awaitable):
          phone = await phone
    """

    async def idle(self):
        loop = asyncio.get_running_loop()
        stop_event = asyncio.Event()

        for sig in (
            signal.SIGINT,
            signal.SIGTERM,
            signal.SIGQUIT,
        ):
            loop.add_signal_handler(sig, stop_event.set)

        await stop_event.wait()

    def run(self, coroutine: Awaitable | None = None):
        async def _run():
            async with self:
                await (coroutine or self.idle())

        asyncio.run(_run())
