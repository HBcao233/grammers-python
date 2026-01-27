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
    UpdateState,
)
from .dc_options import DEFAULT_DC, KNOWN_DC_OPTIONS
from enum import Enum
import sqlite3

VERSION = 1


class PeerSubtype(Enum):
    UserSelf = 1
    UserBot = 2
    UserSelfBot = 3
    Megagroup = 4
    Broadcast = 8
    Gigagroup = 12


class SqliteSession(Session):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, path: str = ':memory:'):
        self.path = path
        self.conn = sqlite3.connect(path)
        self.init()

        r = self.conn.execute('SELECT * FROM dc_home LIMIT 1')
        res = r.fetchone()
        self.home_dc: int = int(res[0]) if res else DEFAULT_DC

        r = self.conn.execute('SELECT * FROM dc_option')
        res = {}
        for i in r.fetchall():
            id_ = int(i[0])
            res[id_] = DcOption(id_, i[1], i[2], i[3])
        self.dc_options: dict[int, DcOption] = res

    def init(self):
        res = self.conn.execute('PRAGMA user_version').fetchone()
        user_version = int(res[0]) if res else 0
        if user_version == 0:
            self.migrate_v0_to_v1()
            user_version = VERSION

        if user_version == VERSION:
            self.conn.execute(f'PRAGMA user_version={int(user_version)}')
            self.conn.commit()

    def migrate_v0_to_v1(self) -> None:
        self.conn.execute("""CREATE TABLE dc_home (
    dc_id INTEGER NOT NULL,
    PRIMARY KEY(dc_id))""")
        self.conn.execute("""CREATE TABLE dc_option (
    dc_id INTEGER NOT NULL,
    ipv4 TEXT NOT NULL,
    ipv6 TEXT NOT NULL,
    auth_key BLOB,
    PRIMARY KEY (dc_id))""")
        self.conn.execute("""CREATE TABLE peer_info (
    peer_id INTEGER NOT NULL,
    hash INTEGER,
    subtype INTEGER,
    PRIMARY KEY (peer_id))""")
        self.conn.execute("""CREATE TABLE update_state (
    pts INTEGER NOT NULL,
    qts INTEGER NOT NULL,
    date INTEGER NOT NULL,
    seq INTEGER NOT NULL)""")
        self.conn.execute("""CREATE TABLE channel_state (
    peer_id INTEGER NOT NULL,
    pts INTEGER NOT NULL,
    PRIMARY KEY (peer_id))""")
        self.conn.commit()

    async def home_dc_id(self) -> int:
        return self.home_dc

    async def set_home_dc_id(self, dc_id: int) -> None:
        self.home_dc = dc_id
        self.conn.execute('DELETE FROM dc_home')
        self.conn.execute('INSERT INTO dc_home VALUES (?)', (dc_id,))
        self.conn.commit()

    async def dc_option(self, dc_id: int) -> DcOption | None:
        return self.dc_options.get(dc_id, KNOWN_DC_OPTIONS.get(dc_id, None))

    async def set_dc_option(self, dc_option: DcOption) -> None:
        self.dc_options[dc_option.id] = dc_option
        self.conn.execute(
            'INSERT OR REPLACE INTO dc_option VALUES (?, ?, ?, ?)',
            (
                dc_option.id,
                str(dc_option.ipv4),
                str(dc_option.ipv6),
                dc_option.auth_key,
            ),
        )
        self.conn.commit()

    async def peer(self, peer: PeerIdLike) -> PeerInfo | None:
        peer = PeerId(peer)

        def _parse(res):
            subtype = res[2]
            match peer.kind:
                case PeerKind.User | PeerKind.UserSelf:
                    return PeerInfo.User(
                        id=res[0],
                        auth=PeerAuth(res[1]),
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

        if peer.kind == PeerKind.UserSelf:
            r = self.conn.execute(
                'SELECT * FROM peer_info WHERE subtype & ? LIMIT 1',
                (PeerSubtype.UserSelf.value,),
            )
        else:
            r = self.conn.execute(
                'SELECT * FROM peer_info WHERE peer_id = ? LIMIT 1',
                (peer.bot_api_dialog_id),
            )
        return _parse(r.fetchone())

    async def cache_peer(self, peer_info: PeerInfo) -> None:
        pass

    async def updates_state(self) -> UpdatesState:
        pass

    async def set_update_state(self, update: UpdateState) -> None:
        pass
