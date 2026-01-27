from grammers.sessions import (
    SqliteSession,
    DcOption,
    PeerInfo,
    UpdatesState,
    ChannelState,
)
import pytest


@pytest.mark.asyncio
async def test_sqlite_session():
    session = SqliteSession(':memory:')
    assert await session.home_dc_id() == 2

    dc_option = DcOption(
        5,
        '91.108.56.104:443',
        None,
        None,
    )
    await session.set_dc_option(dc_option)
    assert await session.dc_option(5) == dc_option

    peer = PeerInfo.User(123456, None, False, True)
    await session.cache_peer(peer)
    assert await session.peer(123456) == peer

    update = UpdatesState(1, 2, 3, 4, [ChannelState(5, 6)])
    await session.set_update_state(update)
    assert await session.updates_state() == update
