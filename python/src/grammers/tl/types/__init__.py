# ruff: noqa: F401

from grammers import _rs
import sys

sys.modules['grammers._rs.tl.types.chatlists'] = _rs.tl.types.chatlists
sys.modules['grammers._rs.tl.types.phone'] = _rs.tl.types.phone
sys.modules['grammers._rs.tl.types.storage'] = _rs.tl.types.storage
sys.modules['grammers._rs.tl.types.account'] = _rs.tl.types.account
sys.modules['grammers._rs.tl.types.contacts'] = _rs.tl.types.contacts
sys.modules['grammers._rs.tl.types.photos'] = _rs.tl.types.photos
sys.modules['grammers._rs.tl.types.stories'] = _rs.tl.types.stories
sys.modules['grammers._rs.tl.types.aicompose'] = _rs.tl.types.aicompose
sys.modules['grammers._rs.tl.types.fragment'] = _rs.tl.types.fragment
sys.modules['grammers._rs.tl.types.premium'] = _rs.tl.types.premium
sys.modules['grammers._rs.tl.types.updates'] = _rs.tl.types.updates
sys.modules['grammers._rs.tl.types.auth'] = _rs.tl.types.auth
sys.modules['grammers._rs.tl.types.help'] = _rs.tl.types.help
sys.modules['grammers._rs.tl.types.smsjobs'] = _rs.tl.types.smsjobs
sys.modules['grammers._rs.tl.types.upload'] = _rs.tl.types.upload
sys.modules['grammers._rs.tl.types.bots'] = _rs.tl.types.bots
sys.modules['grammers._rs.tl.types.messages'] = _rs.tl.types.messages
sys.modules['grammers._rs.tl.types.stats'] = _rs.tl.types.stats
sys.modules['grammers._rs.tl.types.users'] = _rs.tl.types.users
sys.modules['grammers._rs.tl.types.channels'] = _rs.tl.types.channels
sys.modules['grammers._rs.tl.types.payments'] = _rs.tl.types.payments
sys.modules['grammers._rs.tl.types.stickers'] = _rs.tl.types.stickers

from . import (
    chatlists,
    phone,
    storage,
    account,
    contacts,
    photos,
    stories,
    aicompose,
    fragment,
    premium,
    updates,
    auth,
    help,
    smsjobs,
    upload,
    bots,
    messages,
    stats,
    users,
    channels,
    payments,
    stickers,
)
from grammers._rs.tl.types import *
