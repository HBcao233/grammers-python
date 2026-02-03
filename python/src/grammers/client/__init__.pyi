from typing import Awaitable, Callable, Optional, Protocol, Self
from . import tl
from .tl import types
from ..sessions import Session
from .types import (
    LoginToken,
    User,
    Group,
    Channel,
    Peer,
)
from .. import hints

class PasswordCallback(Protocol):
    def __call__(self, hint: str) -> str | Awaitable[str]: ...

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
    def bot_token(self) -> str | None: ...
    @property
    def use_ipv6(self) -> bool: ...
    @property
    def system_lang_code(self) -> str: ...
    @property
    def lang_code(self) -> str: ...
    @property
    def phone(self) -> str | Callable[[], str | Awaitable[str]]: ...
    @property
    def code(self) -> Callable[[], str | int | Awaitable[str | int]]: ...
    @property
    def password(self) -> str | PasswordCallback: ...
    def __new__(
        cls,
        session: str,
        api_id: int | str,
        api_hash: str,
        *,
        phone: str | Callable[[], str | Awaitable[str]],
        code: Callable[[], str | Awaitable[str]],
        password: PasswordCallback,
        bot_token: Optional[str] = None,
        app_version: Optional[str] = None,
        device_model: Optional[str] = None,
        system_version: Optional[str] = None,
        lang_code: Optional[str] = None,
        system_lang_code: Optional[str] = None,
        use_ipv6: bool = False,
    ) -> Self:
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

        Examples

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

    # ========== auth methods ==========

    async def is_authorized(self) -> bool:
        """
        Returns `true` if the current account is authorized. Otherwise,
        logging in will be required before being able to invoke requests.

        This will likely be the first method you want to call on a connected [`Client`]. After you
        determine if the account is authorized or not, you will likely want to use either
        [`Client.bot_sign_in`] or [`Client.request_login_code`].

        Examples

        ```
        if await client.is_authorized():
            print('Client already authorized and ready to use!')
        else:
            print('Client is not authorized, you will need to sign_in!')
        ```
        """
        ...
    async def authorize(self) -> types.User:
        """
        Terminal interactive login.

        Pseudo-code

        ```
        async def authorize(self) -> types.User:
            bot_token = self.bot_token
            if bot_token:
                return await self.bot_sign_in(bot_token)

            # check if session is logined
            session = self.session
            dc_id = await session.home_dc_id()
            dc_option = await session.dc_option(dc_id)
            if dc_option and dc_option.auth_key:
                if x := await self.get_password_information():
                    return await self._check_password(x)

            phone = utils.maybe_call(self.phone)
            phone = await utils.maybe_await(phone)
            if not isinstance(phone, str):
                return ValueError(f"phone excepted str, got '{type(phone).__qualname__}'")

            login_token = await self.request_login_code(phone, self.api_hash)
            code = self.code()
            code = str(await utils.maybe_await(code))

            try:
                return await self.sign_in(login_token, code)
            except PasswordRequiredError:
                return await self._check_password()
        ```
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

        Examples

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
    async def request_login_code(self, phone: str, api_hash: str) -> LoginToken:
        """
        Requests the login code for the account associated to the given phone
        number via another Telegram application or SMS.

        This is the method you need to call before being able to sign in to a user account.
        After you obtain the code and it's inside your program (e.g. ask the user to enter it
        via the console's standard input), you will need to [`Client::sign_in`] to complete the
        process.

        Examples

        ```
        # Note: these values are obviously fake.
        # Obtain your own with the developer's phone at https://my.telegram.org.
        API_HASH: str = "514727c32270b9eb8cc16daf17e21e57"
        # The phone used here does NOT need to be the same as the one used by the developer
        # to obtain the API ID and hash.
        PHONE: str = "+1 415 555 0132"

        if not await client.is_authorized():
            # We're not logged in, so request the login code.
            token = await client.request_login_code(PHONE, API_HASH)
        ```
        """
        ...
    async def sign_in(self, token: LoginToken, code: str) -> types.User:
        """
        Signs in to the user account.

        You must call [`Client.request_login_code`] before using this method in order to obtain
        necessary login token, and also have asked the user for the login code.

        It is recommended to save the session on successful login. Some session storages will do this
        automatically. If saving fails, it is recommended to [`Client.sign_out`]. If the session is never
        saved post-login, then the authorization will be "lost" in the list of logged-in clients, since it
        is unaccessible.

        Examples

        ```
        # API_HASH: str = ""
        # PHONE: str = ""
        def ask_code_to_user() -> str:
            pass

        token = await client.request_login_code(PHONE, API_HASH)
        code = ask_code_to_user()

        try:
            let user = await client.sign_in(token, code)
        except errors.PasswordRequiredError as e:
            token = e.token
            print('Please provide a password)
        except errors.SignUpRequiredError:
            print('Sign up required')
        except errors.RpcError as e:
            print('Failed to sign in as a user:\n', traceback.format_exc(e))

        if user.first_name:
            print(f"Signed in as {user.first_name}!")
        else:
            println!("Signed in!")
        ```
        """
        ...
    async def get_password_information(self) -> types.account.Password:
        """
        Extract information needed for the two-factor authentication
        It's called automatically when we get PasswordRequiredError during sign in.
        """
        ...
    async def check_password(
        self, password_info: types.account.Password, password: str
    ) -> types.User:
        """
        Sign in using two-factor authentication (user password).

        [`password_token`] can be obtained from [`PasswordRequiredError`] error after the
        [`Client.sign_in`] method fails.

        Examples

        ```
        # const API_HASH: &str = "";
        # const PHONE: &str = "";
        def get_user_password(hint: str) -> String:
            pass

        # let token = await client.request_login_code(PHONE, API_HASH)
        # let code = "";

        # ... enter phone number, request login code ...

        try:
            let user = await client.sign_in(token, code)
        except errors.PasswordRequiredError as e:
            password_token = e.password_token
            password = get_user_password(password_token.hint)

            try:
                user = await client.check_password(password_token, password)
            except errors.RpcError as e:
                print('Sign in required')
        except errors.RpcError as e:
            print('Failed to sign in as a user:', traceback.format_exc(e))

        ```
        """
        ...

    async def sign_out(self) -> types.auth.LoggedOut:
        """
        Signs out of the account authorized by this client's session.

        If the client was not logged in, this method raise RpcError.

        The client is not disconnected after signing out.

        Note that after using this method you will have to sign in again. If all you want to do
        is disconnect, simply call `await client.stop()`.

        Examples

        ```
        from grammers import errors

        try:
            await client.sign_out()
        except errors.RpcError:
            print("No user was signed in, so nothing has changed...");
        else:
            print("Signed out successfully!");
        ```
        """
        ...
    async def disconnect(self) -> None:
        """
        Signals all clients sharing the same sender pool to disconnect.
        """
        ...
    async def _check_password(
        self, password_info: types.account.Password | None = None
    ) -> types.User:
        """
        Check password used by `Client.authorize`

        Pseudo-code

        ```
        async def _check_password(self, password_info: types.account.Password | None = None) -> types.User:
            if password_info is None:
                password_info = await self.get_password_information()

            hint = password_info.hint
            password = self.password
            password = utils.maybe_call(password, [hint])
            password = await utils.maybe_await(password)
            if not isinstance(password, str):
                raise ValueError(f"password excepted str, got '{type(password).__qualname__}'")

            return await sekf.check_password(password_info, password)
        ```
        """
        ...
    async def _complete_login(self, auth: types.auth.Authorization) -> types.User:
        """
        Complete login, will cache peer and save update state.

        Pseudo-code

        ```
        async def _complete_login(self, auth: types.auth.Authorization) -> types.User:
            user = auth.user
            user_id = user.id
            bot = getattr(user, 'bot', None)
            session = self.session
            auth = None
            if not getattr(user, 'min', False):
                auth = user.access_hash
            else:
                peer = await session.peer(user_id)
                if peer:
                    auth = peer.auth

            await session.cache_peer(PeerInfo.User(
                user_id,
                auth,
                bot,
                True,
            ))

            try:
                state = await self.client(functions.updates.GetState())
            except errors.RpcError:
                pass
            else:
                await session.set_update_state(UpdateState.All(
                    state.pts,
                    state.qts,
                    state.date,
                    state.seq,
                    [],
                ))

            return user
        ```
        """
        ...

    # ========== chats methods ==========

    async def get_me(self) -> types.User:
        """
        Fetch information about the currently logged-in user.

        Although this method is cheap to call, you might want to cache the results somewhere.

        Examples

        ```
        await client.get_me()
        ```
        """
        ...
    async def resolve_username(self, username: str) -> User | Group | Channel:
        """
        Resolves a username into the peer that owns it, if any.

        Note that this method is expensive to call, and can quickly cause long flood waits.

        # Examples

        ```
        if peer := await client.resolve_username("username"):
            print("Found peer!: {:?}", peer.name)
        ```
        """
        ...
    async def resolve_peer(self, peer: hints.PeerIdLikeExtend) -> Peer:
        """
        Resolves a PeerIdLike or InputPeer into a Peer
        """
        ...
    async def resolve_phone(self, phone: str) -> User:
        """
        Resolves a phone into User.
        """
        ...

    # ========== messages methods ==========
