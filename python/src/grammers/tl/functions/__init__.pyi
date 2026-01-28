from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class InvokeAfterMsg(TLRequest):
    """
    [Read `invokeAfterMsg` docs](https://core.telegram.org/method/invokeAfterMsg).

    Generated from the following TL definition:
    ```tl
    invokeAfterMsg#cb9f372d {X:Type} msg_id:long query:!X = !X
    ```
    """
    def __new__(
        cls,
        msg_id: int,
        query: TLRequest,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InvokeAfterMsgs(TLRequest):
    """
    [Read `invokeAfterMsgs` docs](https://core.telegram.org/method/invokeAfterMsgs).

    Generated from the following TL definition:
    ```tl
    invokeAfterMsgs#3dc4b4f0 {X:Type} msg_ids:Vector<long> query:!X = !X
    ```
    """
    def __new__(
        cls,
        msg_ids: Sequence[int],
        query: TLRequest,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InitConnection(TLRequest):
    """
    [Read `initConnection` docs](https://core.telegram.org/method/initConnection).

    Generated from the following TL definition:
    ```tl
    initConnection#c1cd5ea9 {X:Type} flags:# api_id:int device_model:string system_version:string app_version:string system_lang_code:string lang_pack:string lang_code:string proxy:flags.0?InputClientProxy params:flags.1?JSONValue query:!X = !X
    ```
    """
    def __new__(
        cls,
        api_id: int,
        device_model: str,
        system_version: str,
        app_version: str,
        system_lang_code: str,
        lang_pack: str,
        lang_code: str,
        proxy: Optional[types.InputClientProxy],
        params: Optional[types.JsonNull | types.JsonBool | types.JsonNumber | types.JsonString | types.JsonArray | types.JsonObject],
        query: TLRequest,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InvokeWithLayer(TLRequest):
    """
    [Read `invokeWithLayer` docs](https://core.telegram.org/method/invokeWithLayer).

    Generated from the following TL definition:
    ```tl
    invokeWithLayer#da9b0d0d {X:Type} layer:int query:!X = !X
    ```
    """
    def __new__(
        cls,
        layer: int,
        query: TLRequest,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InvokeWithoutUpdates(TLRequest):
    """
    [Read `invokeWithoutUpdates` docs](https://core.telegram.org/method/invokeWithoutUpdates).

    Generated from the following TL definition:
    ```tl
    invokeWithoutUpdates#bf9459b7 {X:Type} query:!X = !X
    ```
    """
    def __new__(
        cls,
        query: TLRequest,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InvokeWithMessagesRange(TLRequest):
    """
    [Read `invokeWithMessagesRange` docs](https://core.telegram.org/method/invokeWithMessagesRange).

    Generated from the following TL definition:
    ```tl
    invokeWithMessagesRange#365275f2 {X:Type} range:MessageRange query:!X = !X
    ```
    """
    def __new__(
        cls,
        range: types.MessageRange,
        query: TLRequest,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InvokeWithTakeout(TLRequest):
    """
    [Read `invokeWithTakeout` docs](https://core.telegram.org/method/invokeWithTakeout).

    Generated from the following TL definition:
    ```tl
    invokeWithTakeout#aca9fd2e {X:Type} takeout_id:long query:!X = !X
    ```
    """
    def __new__(
        cls,
        takeout_id: int,
        query: TLRequest,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InvokeWithBusinessConnection(TLRequest):
    """
    [Read `invokeWithBusinessConnection` docs](https://core.telegram.org/method/invokeWithBusinessConnection).

    Generated from the following TL definition:
    ```tl
    invokeWithBusinessConnection#dd289f8e {X:Type} connection_id:string query:!X = !X
    ```
    """
    def __new__(
        cls,
        connection_id: str,
        query: TLRequest,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InvokeWithGooglePlayIntegrity(TLRequest):
    """
    [Read `invokeWithGooglePlayIntegrity` docs](https://core.telegram.org/method/invokeWithGooglePlayIntegrity).

    Generated from the following TL definition:
    ```tl
    invokeWithGooglePlayIntegrity#1df92984 {X:Type} nonce:string token:string query:!X = !X
    ```
    """
    def __new__(
        cls,
        nonce: str,
        token: str,
        query: TLRequest,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InvokeWithApnsSecret(TLRequest):
    """
    [Read `invokeWithApnsSecret` docs](https://core.telegram.org/method/invokeWithApnsSecret).

    Generated from the following TL definition:
    ```tl
    invokeWithApnsSecret#dae54f8 {X:Type} nonce:string secret:string query:!X = !X
    ```
    """
    def __new__(
        cls,
        nonce: str,
        secret: str,
        query: TLRequest,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InvokeWithReCaptcha(TLRequest):
    """
    [Read `invokeWithReCaptcha` docs](https://core.telegram.org/method/invokeWithReCaptcha).

    Generated from the following TL definition:
    ```tl
    invokeWithReCaptcha#adbb0f94 {X:Type} token:string query:!X = !X
    ```
    """
    def __new__(
        cls,
        token: str,
        query: TLRequest,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReqPq(TLRequest):
    """
    [Read `req_pq` docs](https://core.telegram.org/method/req_pq).

    Generated from the following TL definition:
    ```tl
    req_pq#60469778 nonce:int128 = ResPQ
    ```
    """
    def __new__(
        cls,
        nonce: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReqPqMulti(TLRequest):
    """
    [Read `req_pq_multi` docs](https://core.telegram.org/method/req_pq_multi).

    Generated from the following TL definition:
    ```tl
    req_pq_multi#be7e8ef1 nonce:int128 = ResPQ
    ```
    """
    def __new__(
        cls,
        nonce: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReqDhParams(TLRequest):
    """
    [Read `req_DH_params` docs](https://core.telegram.org/method/req_DH_params).

    Generated from the following TL definition:
    ```tl
    req_DH_params#d712e4be nonce:int128 server_nonce:int128 p:bytes q:bytes public_key_fingerprint:long encrypted_data:bytes = Server_DH_Params
    ```
    """
    def __new__(
        cls,
        nonce: int,
        server_nonce: int,
        p: bytes,
        q: bytes,
        public_key_fingerprint: int,
        encrypted_data: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetClientDhParams(TLRequest):
    """
    [Read `set_client_DH_params` docs](https://core.telegram.org/method/set_client_DH_params).

    Generated from the following TL definition:
    ```tl
    set_client_DH_params#f5045f1f nonce:int128 server_nonce:int128 encrypted_data:bytes = Set_client_DH_params_answer
    ```
    """
    def __new__(
        cls,
        nonce: int,
        server_nonce: int,
        encrypted_data: bytes,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DestroyAuthKey(TLRequest):
    """
    [Read `destroy_auth_key` docs](https://core.telegram.org/method/destroy_auth_key).

    Generated from the following TL definition:
    ```tl
    destroy_auth_key#d1435160 = DestroyAuthKeyRes
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RpcDropAnswer(TLRequest):
    """
    [Read `rpc_drop_answer` docs](https://core.telegram.org/method/rpc_drop_answer).

    Generated from the following TL definition:
    ```tl
    rpc_drop_answer#58e4a740 req_msg_id:long = RpcDropAnswer
    ```
    """
    def __new__(
        cls,
        req_msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetFutureSalts(TLRequest):
    """
    [Read `get_future_salts` docs](https://core.telegram.org/method/get_future_salts).

    Generated from the following TL definition:
    ```tl
    get_future_salts#b921bd04 num:int = FutureSalts
    ```
    """
    def __new__(
        cls,
        num: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Ping(TLRequest):
    """
    [Read `ping` docs](https://core.telegram.org/method/ping).

    Generated from the following TL definition:
    ```tl
    ping#7abe77ec ping_id:long = Pong
    ```
    """
    def __new__(
        cls,
        ping_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PingDelayDisconnect(TLRequest):
    """
    [Read `ping_delay_disconnect` docs](https://core.telegram.org/method/ping_delay_disconnect).

    Generated from the following TL definition:
    ```tl
    ping_delay_disconnect#f3427b8c ping_id:long disconnect_delay:int = Pong
    ```
    """
    def __new__(
        cls,
        ping_id: int,
        disconnect_delay: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DestroySession(TLRequest):
    """
    [Read `destroy_session` docs](https://core.telegram.org/method/destroy_session).

    Generated from the following TL definition:
    ```tl
    destroy_session#e7512126 session_id:long = DestroySessionRes
    ```
    """
    def __new__(
        cls,
        session_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

