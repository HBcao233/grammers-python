from .session import Session
from .types import (
    DcOption,
    PeerId,
    PeerIdLike,
    PeerInfo,
    PeerAuth,
    PeerKind,
    ChannelKind,
    UpdatesState,
    ChannelState,
    UpdateState,
)
from .dc_options import DEFAULT_DC, KNOWN_DC_OPTIONS
from enum import Enum
from contextlib import asynccontextmanager
from typing import Self, Sequence
import asyncio
import sqlite3
import logging
import base64
import ipaddress
import struct

__all__ = ['SqliteSession', 'VERSION', 'PeerSubtype']
logger = logging.getLogger('SqliteSession')
VERSION = 1

telethon_format = '>B{}sH256s'
telethon_version = '1'


class PeerSubtype(Enum):
    UserSelf = 1
    UserBot = 2
    UserSelfBot = 3
    Megagroup = 4
    Broadcast = 8
    Gigagroup = 12

    def __int__(self):
        return self.value


class SqliteSession(Session):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(
        self,
        database: str | sqlite3.Connection = ':memory:',
        pool_size: int = 5,
    ) -> None:
        if isinstance(database, sqlite3.Connection) or database == ':memory:':
            pool_size = 1

        self.pool_size = pool_size
        self._database = database
        self._pool = None
        self._inited = False
        self.home_dc: int = DEFAULT_DC
        self.dc_options: dict[int, DcOption] = {}

    @staticmethod
    def from_telethon_string(
        string: str,
        path: str = ':memory:',
        pool_size: int = 5,
    ) -> Self:
        if string[0] != telethon_version:
            raise ValueError('Invalid telethon string.')

        string = string[1:]
        ip_len = 4 if 350 <= len(string) <= 352 else 16
        dc_id, ip, port, auth_key = struct.unpack(
            telethon_format.format(ip_len),
            base64.urlsafe_b64decode(string + '=' * (-len(string) % 4)),
        )
        ip = ipaddress.ip_address(ip)
        if ip.version == 4:
            ipv4 = f'{ip.compressed}:{port}'
            ipv6 = f'[::ff:{ip.compressed}]:{port}'
        else:
            _ipv4 = ipaddress.ip_address(ip.packed[-4:]).compressed
            ipv4 = f'{_ipv4}:{port}'
            ipv6 = f'[{ip.compressed}]:{port}'

        conn = sqlite3.connect(path, check_same_thread=False)
        SqliteSession._init(conn)
        conn.execute('DELETE FROM dc_home')
        conn.execute('INSERT INTO dc_home VALUES (?)', (dc_id,))
        conn.execute(
            'INSERT OR REPLACE INTO dc_option VALUES (?, ?, ?, ?)',
            (
                dc_id,
                ipv4,
                ipv6,
                auth_key,
            ),
        )
        conn.commit()

        session = SqliteSession(conn, 1)
        return session

    async def _ensure_pool(self):
        if self._pool is not None:
            return

        self._pool = asyncio.Queue(maxsize=self.pool_size)
        for _ in range(self.pool_size):
            if isinstance(self._database, sqlite3.Connection):
                conn = self._database
            else:
                conn = sqlite3.connect(self._database, check_same_thread=False)
            await self._pool.put(conn)

    @asynccontextmanager
    async def connection(self):
        await self._ensure_pool()
        conn = await self._pool.get()
        try:
            yield conn
        finally:
            await self._pool.put(conn)

    @staticmethod
    def _init(conn: sqlite3.Connection) -> (int, Sequence[DcOption]):
        res = conn.execute('PRAGMA user_version').fetchone()
        user_version = int(res[0]) if res else 0
        if user_version == 0:
            SqliteSession._migrate_v0_to_v1(conn)
            user_version = VERSION

        r = conn.execute('SELECT * FROM dc_home LIMIT 1')
        res = r.fetchone()
        home_dc = int(res[0]) if res else DEFAULT_DC

        r = conn.execute('SELECT * FROM dc_option')
        dc_options = {}
        for i in r.fetchall():
            id_ = int(i[0])
            dc_options[id_] = DcOption(id_, i[1], i[2], i[3])
        return (home_dc, dc_options)

    async def init(self) -> None:
        if self._inited:
            return

        async with self.connection() as conn:
            home_dc, dc_options = SqliteSession._init(conn)
            self.home_dc = home_dc
            self.dc_options = dc_options

        self._inited = True

    @staticmethod
    def _migrate_v0_to_v1(conn) -> None:
        conn.execute("""CREATE TABLE dc_home (
    dc_id INTEGER NOT NULL,
    PRIMARY KEY(dc_id))""")
        conn.execute("""CREATE TABLE dc_option (
    dc_id INTEGER NOT NULL,
    ipv4 TEXT NOT NULL,
    ipv6 TEXT NOT NULL,
    auth_key BLOB,
    PRIMARY KEY (dc_id))""")
        conn.execute("""CREATE TABLE peer_info (
    peer_id INTEGER NOT NULL,
    hash INTEGER,
    subtype INTEGER,
    PRIMARY KEY (peer_id))""")
        conn.execute("""CREATE TABLE update_state (
    pts INTEGER NOT NULL,
    qts INTEGER NOT NULL,
    date INTEGER NOT NULL,
    seq INTEGER NOT NULL)""")
        conn.execute("""CREATE TABLE channel_state (
    peer_id INTEGER NOT NULL,
    pts INTEGER NOT NULL,
    PRIMARY KEY (peer_id))""")
        conn.execute('PRAGMA user_version=1')
        conn.commit()

    async def home_dc_id(self) -> int:
        await self.init()
        return self.home_dc

    async def set_home_dc_id(self, dc_id: int) -> None:
        await self.init()
        self.home_dc = dc_id
        async with self.connection() as conn:
            conn.execute('DELETE FROM dc_home')
            conn.execute('INSERT INTO dc_home VALUES (?)', (dc_id,))
            conn.commit()

    async def dc_option(self, dc_id: int) -> DcOption | None:
        await self.init()
        return self.dc_options.get(dc_id, KNOWN_DC_OPTIONS.get(dc_id, None))

    async def set_dc_option(self, dc_option: DcOption) -> None:
        await self.init()
        self.dc_options[dc_option.id] = dc_option

        async with self.connection() as conn:
            conn.execute(
                'INSERT OR REPLACE INTO dc_option VALUES (?, ?, ?, ?)',
                (
                    dc_option.id,
                    str(dc_option.ipv4),
                    str(dc_option.ipv6),
                    dc_option.auth_key,
                ),
            )
            conn.commit()
        logger.debug(f'set_dc_option: {dc_option}')

    async def peer(self, peer: PeerIdLike) -> PeerInfo | None:
        await self.init()
        peer = PeerId(peer)

        def _parse(res):
            subtype = res[2]
            match peer.kind:
                case PeerKind.User | PeerKind.UserSelf:
                    return PeerInfo.User(
                        id=res[0],
                        auth=PeerAuth(res[1]) if res[1] is not None else None,
                        bot=bool(subtype & PeerSubtype.UserBot.value),
                        is_self=bool(subtype & PeerSubtype.UserSelf.value),
                    )
                case PeerKind.Chat:
                    return PeerInfo.Chat(id=peer.bare_id)
                case PeerKind.Channel:
                    if subtype & PeerSubtype.Gigagroup:
                        kind = ChannelKind.Gigagroup
                    elif subtype & PeerSubtype.Broadcast:
                        kind = ChannelKind.Broadcast
                    elif subtype & PeerSubtype.Megagroup:
                        kind = ChannelKind.Megagroup
                    else:
                        kind = None
                    return PeerInfo.Channel(
                        id=peer.bare_id,
                        auth=PeerAuth(res[1]),
                        kind=kind,
                    )

        async with self.connection() as conn:
            if peer.kind == PeerKind.UserSelf:
                r = conn.execute(
                    'SELECT * FROM peer_info WHERE subtype & ? LIMIT 1',
                    (PeerSubtype.UserSelf.value,),
                )
            else:
                r = conn.execute(
                    'SELECT * FROM peer_info WHERE peer_id = ? LIMIT 1',
                    (peer.bot_api_dialog_id,),
                )

        return _parse(r.fetchone())

    async def cache_peer(self, peer: PeerInfo) -> None:
        await self.init()

        peer_id = peer.bot_api_dialog_id
        hash_ = peer.auth
        if hash_ is not None:
            hash_ = int(hash_)
        subtype = None
        match peer:
            case PeerInfo.User():
                match (bool(peer.bot), bool(peer.is_self)):
                    case (True, True):
                        subtype = PeerSubtype.UserSelfBot
                    case (True, False):
                        subtype = PeerSubtype.UserBot
                    case (False, True):
                        subtype = PeerSubtype.UserSelf
            case PeerInfo.Channel():
                match peer.kind:
                    case ChannelKind.Megagroup:
                        subtype = PeerSubtype.Megagroup
                    case ChannelKind.Broadcast:
                        subtype = PeerSubtype.Broadcast
                    case ChannelKind.Gigagroup:
                        subtype = PeerSubtype.Gigagroup

        if subtype is not None:
            subtype = int(subtype)

        async with self.connection() as conn:
            conn.execute(
                'INSERT OR REPLACE INTO peer_info VALUES (?, ?, ?)',
                (peer_id, hash_, subtype),
            )

    async def updates_state(self) -> UpdatesState:
        await self.init()

        async with self.connection() as conn:
            r = conn.execute('SELECT * FROM update_state LIMIT 1')
            res = r.fetchone()
            if res is None:
                return UpdatesState()

            state = UpdatesState(
                int(res[0]),
                int(res[1]),
                int(res[2]),
                int(res[3]),
                [],
            )
            r = conn.execute('SELECT * FROM channel_state')
            channels = []
            while res := r.fetchone():
                channels.append(
                    ChannelState(
                        int(res[0]),
                        int(res[1]),
                    )
                )
            # `state.channels.append()` cannot modify the value of `state.channels`, Use `state.channels = channels` instead.
            state.channels = channels
            return state

    async def set_update_state(self, update: UpdateState) -> None:
        await self.init()
        
        async with self.connection() as conn:
            match update:
                case UpdateState.All():
                    conn.execute('DELETE FROM update_state')
                    conn.execute(
                        'INSERT INTO update_state VALUES (?, ?, ?, ?)',
                        (update.pts, update.qts, update.date, update.seq),
                    )
                    conn.execute('DELETE FROM channel_state')
                    for i in update.channels:
                        conn.execute(
                            'INSERT INTO channel_state VALUES (?, ?)',
                            (i.id, i.pts),
                        )
                case UpdateState.Primary():
                    previous = conn.execute('SELECT * FROM update_state LIMIT 1')
                    if previous is not None:
                        conn.execute(
                            'UPDATE update_state SET pts = ?, date = ?, seq = ?',
                            (update.pts, update.date, update.seq),
                        )
                    else:
                        conn.execute(
                            'INSERT INTO update_state VALUES (?, 0, ?, ?)',
                            (update.pts, update.date, update.seq),
                        )
                case UpdateState.Secondary():
                    previous = conn.execute('SELECT * FROM update_state LIMIT 1')
                    if previous is not None:
                        conn.execute('UPDATE update_state SET qts = ?', (update.qts,))
                    else:
                        conn.execute(
                            'INSERT INTO update_state VALUES (0, ?, 0, 0)',
                            (update.qts,),
                        )
                case UpdateState.Channel():
                    conn.execute(
                        'INSERT OR REPLACE INTO channel_state VALUES (?, ?)',
                        (update.id, update.pts),
                    )
                case _:
                    raise TypeError(
                        f"update expected UpdateState, got '{getattr(update, '__qualname__', type(update).__qualname__)}'"
                    )

            conn.commit()
