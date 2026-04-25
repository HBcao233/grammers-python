from . import _rs
import sys

sys.modules['grammers._rs.crypto'] = _rs.crypto
sys.modules['grammers._rs.custom'] = _rs.custom
sys.modules['grammers._rs.errors'] = _rs.errors
sys.modules['grammers._rs.tl'] = _rs.tl
sys.modules['grammers._rs.sessions'] = _rs.sessions
sys.modules['grammers._rs.client'] = _rs.client

from . import crypto, custom, errors, tl
from .client import Client
from .tl import TLObject, TLRequest, types, functions

__all__ = [
    '_rs',
    'crypto',
    'custom',
    'errors',
    'sessions',
    'tl',
    'TLObject',
    'TLRequest',
    'types',
    'functions',
    'Client',
]
