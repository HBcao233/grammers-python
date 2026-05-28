# ruff: noqa: F401

from grammers import _rs
import sys

sys.modules['grammers._rs.tl.functions.channels'] = _rs.tl.functions.channels
sys.modules['grammers._rs.tl.functions.auth'] = _rs.tl.functions.auth
sys.modules['grammers._rs.tl.functions.account'] = _rs.tl.functions.account
sys.modules['grammers._rs.tl.functions.bots'] = _rs.tl.functions.bots
sys.modules['grammers._rs.tl.functions.langpack'] = _rs.tl.functions.langpack
sys.modules['grammers._rs.tl.functions.help'] = _rs.tl.functions.help
sys.modules['grammers._rs.tl.functions.chatlists'] = _rs.tl.functions.chatlists
sys.modules['grammers._rs.tl.functions.contacts'] = _rs.tl.functions.contacts
sys.modules['grammers._rs.tl.functions.folders'] = _rs.tl.functions.folders
sys.modules['grammers._rs.tl.functions.fragment'] = _rs.tl.functions.fragment
sys.modules['grammers._rs.tl.functions.messages'] = _rs.tl.functions.messages
sys.modules['grammers._rs.tl.functions.payments'] = _rs.tl.functions.payments
sys.modules['grammers._rs.tl.functions.phone'] = _rs.tl.functions.phone
sys.modules['grammers._rs.tl.functions.photos'] = _rs.tl.functions.photos
sys.modules['grammers._rs.tl.functions.premium'] = _rs.tl.functions.premium
sys.modules['grammers._rs.tl.functions.smsjobs'] = _rs.tl.functions.smsjobs
sys.modules['grammers._rs.tl.functions.stats'] = _rs.tl.functions.stats
sys.modules['grammers._rs.tl.functions.stickers'] = _rs.tl.functions.stickers
sys.modules['grammers._rs.tl.functions.stories'] = _rs.tl.functions.stories
sys.modules['grammers._rs.tl.functions.updates'] = _rs.tl.functions.updates
sys.modules['grammers._rs.tl.functions.upload'] = _rs.tl.functions.upload
sys.modules['grammers._rs.tl.functions.users'] = _rs.tl.functions.users
sys.modules['grammers._rs.tl.functions.aicompose'] = _rs.tl.functions.aicompose

from . import (
    channels,
    auth,
    account,
    bots,
    langpack,
    help,
    chatlists,
    contacts,
    folders,
    fragment,
    messages,
    payments,
    phone,
    photos,
    premium,
    smsjobs,
    stats,
    stickers,
    stories,
    updates,
    upload,
    users,
    aicompose,
)
from grammers._rs.tl.functions import *
