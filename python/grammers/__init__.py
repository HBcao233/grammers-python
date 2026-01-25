from . import _rs
from ._rs import Client
import sys

sys.modules['grammers._rs.crypto'] = _rs.crypto
sys.modules['grammers._rs.errors'] = _rs.errors
sys.modules['grammers._rs.tl'] = _rs.tl

from . import crypto, errors, tl
from .tl import TLObject, TLRequest, types, functions
from collections.abc import Awaitable
import sys
import asyncio
import signal

__all__ = [
    '_rs',
    'crypto',
    'errors',
    'tl',
    'TLObject',
    'TLRequest',
    'types',
    'functions',
    'Client',
]


class Client(Client):
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
