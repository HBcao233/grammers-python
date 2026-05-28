from typing import Any, Sequence
import re
import inspect


def parse_phone(phone: int | str) -> str | None:
    """Parses the given phone, or returns `None` if it's invalid."""
    if isinstance(phone, int):
        return str(phone)
    else:
        phone = re.sub(r'[+()\s-]', '', str(phone))
        if phone.isdigit():
            return phone
    return None


def maybe_call(obj: Any, args: Sequence[Any] | None = None) -> Any:
    if callable(obj):
        if args is None:
            return obj()
        return obj(*args)
    return obj


async def maybe_await(obj: Any) -> Any:
    if inspect.isawaitable(obj):
        return await obj
    return obj
