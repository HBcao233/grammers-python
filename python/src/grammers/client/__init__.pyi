from typing import Optional
from . import tl
from .tl import types
from ..sessions import Session

class Client:
    @property
    def session(self) -> Session: ...
    @property
    def me(self) -> types.User | None:
        """
        the information about the currently logged-in user,
        `client.authorize()` will set this attribute once
        """
        ...

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

    # ===== auth methods =====

    async def is_authorized(self) -> bool:
        """
        Returns `true` if the current account is authorized. Otherwise,
        logging in will be required before being able to invoke requests.

        This will likely be the first method you want to call on a connected [`Client`]. After you
        determine if the account is authorized or not, you will likely want to use either
        [`Client.bot_sign_in`] or [`Client.request_login_code`].

        # Examples

        ```
        if await client.is_authorized():
            print('Client already authorized and ready to use!')
        else:
            print('Client is not authorized, you will need to sign_in!')
        ```
        """
        ...
    async def authorize(self) -> bool:
        """
        Terminal interactive login.
        """
        ...
    async def bot_sign_in(self) -> types.User:
        """
        Signs in to the bot account associated with this token.

        This is the method you need to call to use the client under a bot account.

        It is recommended to save the session on successful login. Some session storages will do this
        automatically. If saving fails, it is recommended to [`Client::sign_out`]. If the session is never
        saved post-login, then the authorization will be "lost" in the list of logged-in clients, since it
        is unaccessible.

        # Examples

        ```
        # Note: these values are obviously fake.
        # Obtain your own with the developer's phone at https://my.telegram.org.
        API_HASH: str = "514727c32270b9eb8cc16daf17e21e57"
        # Obtain your own by talking to @BotFather via a Telegram app.
        BOT_TOKEN: str = "776609994:AAFXAy5-PawQlnYywUlZ_b_GOXgarR3ah_yq"

        client = Client('bot', API_ID, API_HASH, bot_token=BOT_TOKEN)
        async def main():
            user = await client.bot_sign_in()
            print('Signed in as {user.first_name}')

        asyncio.run(main())
        ```
        """
        ...
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
        lang_code: Optional[str] = None,
        system_lang_code: Optional[str] = None,
        use_ipv6: bool = False,
    ) -> Client:
        """
        Create client instanse.

        Args:
            session (``str`` | ``Session``):
                A name for the client or a instanse of Session,
                e.g.: 'my_account', SqliteSession('my_account.session').

            api_id (``int`` | ``str``, *optional*):
                The *api_id* part of the Telegram API key, as integer or string.
                E.g.: 12345 or '12345'.

            api_hash (``str``, *optional*):
                The *api_hash* part of the Telegram API key, as string.
                E.g.: '0123456789abcdef0123456789abcdef'.
        """
    async def invoke(self, request: tl.TLRequest) -> tl.TLObject:
        """
        Invoke a raw API call. This directly sends the request to Telegram's servers.

        Using function definitions corresponding to a different layer is likely to cause the
        responses to the request to not be understood.

        # Examples

        ```
        from grammers import functions

        await client.invoke(functions.Ping(ping_id=0))
        ```
        """
        ...
    async def start(self) -> None:
        """
        Start login in to telegram
        """
    async def stop(self) -> None:
        """
        Stop client
        Calling clent's methods after stopping will raise ClientStoppedError.
        """
