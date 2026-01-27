from grammers import Client
from grammers.tl.functions import Ping
import pytest
import logging

logger = logging.getLogger('root')

client = Client('me', 4, '')


@pytest.mark.asyncio
async def test_ping():
    assert not await client.is_authorized()

    request = Ping(0)
    response = await client.invoke(request)
    logger.info(response)
    assert request.ping_id == response.ping_id
