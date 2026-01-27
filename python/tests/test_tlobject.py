from grammers.tl.functions import Ping
from grammers.tl.types import Pong


def test_tlrequest():
    ping = Ping(666)
    assert ping.ping_id == 666
    assert ping.to_json() == '{"_": "Ping", "ping_id": 666}'
    assert ping.to_bytes() == b'\xecw\xbez\x9a\x02\x00\x00\x00\x00\x00\x00'

    pong = Pong(123, 321)
    assert pong.msg_id == 123
    assert pong.ping_id == 321
    assert pong.to_json() == '{"_": "Pong", "msg_id": 123, "ping_id": 321}'
    assert (
        pong.to_bytes() == b'{\x00\x00\x00\x00\x00\x00\x00A\x01\x00\x00\x00\x00\x00\x00'
    )
