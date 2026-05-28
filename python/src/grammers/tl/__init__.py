from grammers import _rs
import sys

sys.modules['grammers._rs.tl.types'] = _rs.tl.types
sys.modules['grammers._rs.tl.functions'] = _rs.tl.functions

from . import types, functions, enums
from .tlobject import TLObject, TLRequest
from .allobjects import LAYER, tlobjects


__all__ = [
    'TLObject',
    'TLRequest',
    'types',
    'functions',
    'enums',
    'LAYER',
    'tlobjects',
]
