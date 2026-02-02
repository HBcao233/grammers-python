from ..sessions import Session, SqliteSession
from .. import tl
from grammers._rs.client import Client
from .types import (
    User,
    Group,
    Channel,
    LoginToken,
    SignInError,
    PaymentRequiredError,
    SignUpRequiredError,
    PasswordRequiredError,
    InvalidCodeError,
    InvalidPasswordError,
)
from typing import Callable, Protocol, Awaitable, Optional
from getpass import getpass
import asyncio
import signal

__all__ = [
    'Client',
    'LoginToken',
    'SignInError',
    'PaymentRequiredError',
    'SignUpRequiredError',
    'PasswordRequiredError',
    'InvalidCodeError',
    'InvalidPasswordError',
    'User',
    'Group',
    'Channel',
]


class PasswordCallback(Protocol):
    def __call__(self, hint: str) -> str | Awaitable[str]: ...


def default_phone_callback():
    first_empty = True
    while True:
        res = input('Please enter your phone: ')
        if res:
            confirm = input('confirm? (y/n)').lower()
            if confirm == 'y':
                return res
        else:
            print('No input.')
            if first_empty:
                first_empty = False
            else:
                raise ValueError('Cancelled')


def default_code_callback():
    return input('Please enter the code you received: ')


def default_password_callback(hint: str):
    return getpass(f'Please enter your password (hint: {hint}): ')


class Client(Client):
    def __new__(
        cls,
        session: str | Session,
        api_id: int | str,
        api_hash: str,
        *,
        phone: Optional[str | Callable[[], str | Awaitable[str]]] = None,
        code: Optional[Callable[[], str | int | Awaitable[str | int]]] = None,
        password: Optional[str | PasswordCallback] = None,
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

        if phone is None:
            phone = default_phone_callback

        if code is None:
            code = default_code_callback
        elif not callable(code):
            raise ValueError(
                'The code parameter needs to be a callable '
                'function that returns the code you received by Telegram.'
            )

        if password is None:
            password = default_password_callback

        return super().__new__(
            cls,
            session,
            api_id,
            api_hash,
            phone=phone,
            code=code,
            password=password,
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

    async def __call__(self, request: tl.TLRequest) -> tl.TLObject:
        """
        Invoke a raw API call. This directly sends the request to Telegram's servers.

        Using function definitions corresponding to a different layer is likely to cause the
        responses to the request to not be understood.

        # Examples

        ```
        from grammers import functions

        await client(functions.Ping(ping_id=0))
        ```
        """
        return await self.invoke(request)

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
