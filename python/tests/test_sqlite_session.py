from grammers.sessions import SqliteSession
import pytest


@pytest.mark.asyncio
async def test_sqlite_session():
    session = SqliteSession(':memory:')
    print(await session.home_dc_id())
