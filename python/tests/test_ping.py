from grammers import Client
from grammers.tl.functions import Ping
import pytest

client = Client('me', 4, '')


@pytest.mark.asyncio
async def test_ping():
    await client.is_authorized()
    
    request = Ping(0)
    response = await client.invoke(request)
    print(response)
    assert request.ping_id == response.ping_id
