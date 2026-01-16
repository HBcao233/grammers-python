from grammers import _rs
import sys
sys.modules['grammers._rs.tl.types'] = _rs.tl.types
sys.modules['grammers._rs.tl.functions'] = _rs.tl.functions

from grammers._rs.tl import TLObject, TLRequest
from . import types, functions

__all__ = [
  "TLObject",
  "TLRequest",
  "types",
  "functions",
]