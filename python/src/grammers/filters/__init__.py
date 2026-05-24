from __future__ import annotations

import inspect
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from collections.abc import Awaitable
    from grammers.events import EventCommon


class Filter:
    async def __call__(self, event: Any) -> bool:
        raise NotImplementedError

    def __invert__(self) -> InvertFilter:
        return InvertFilter(self)

    def __and__(self, other: Filter) -> AndFilter:
        return AndFilter(self, other)

    def __or__(self, other: Filter) -> OrFilter:
        return OrFilter(self, other)

    def __xor__(self, other: Filter) -> XorFilter:
        return XorFilter(self, other)


class InvertFilter(Filter):
    def __init__(self, base: Filter) -> None:
        self.base = base

    async def __call__(self, event: EventCommon) -> bool:
        x = self.base(event)
        if inspect.isawaitable(x):
            x = await x

        return not x


class AndFilter(Filter):
    def __init__(self, base: Filter, other: Filter) -> None:
        self.base = base
        self.other = other

    async def __call__(self, event: EventCommon) -> bool:
        x = self.base(event)
        if inspect.isawaitable(x):
            x = await x

        if not x:
            return False

        y = self.other(event)
        if inspect.isawaitable(y):
            y = await y

        return bool(x) and bool(y)


class OrFilter(Filter):
    def __init__(self, base: Filter, other: Filter) -> None:
        self.base = base
        self.other = other

    async def __call__(self, event: EventCommon) -> bool:
        x = self.base(event)
        if inspect.isawaitable(x):
            x = await x

        if x:
            return True

        y = self.other(event)
        if inspect.isawaitable(y):
            y = await y

        return bool(x) or bool(y)


class XorFilter(Filter):
    def __init__(self, base: Filter, other: Filter) -> None:
        self.base = base
        self.other = other

    async def __call__(self, event: EventCommon) -> bool:
        x = self.base(event)
        if inspect.isawaitable(x):
            x = await x

        y = self.other(event)
        if inspect.isawaitable(y):
            y = await y

        return bool(x) ^ bool(y)


def create(
    func: Callable[..., bool | Awaitable[bool]],
    name: str | None = None,
    **kwargs: Any,
) -> Filter:
    """Easily create a custom filter.

    Custom filters give you extra control over which updates are allowed or not to be processed
    by your handlers.

    Parameters:
        func (``Callable``):
            A function that accepts three positional arguments *(filter, event)* and
            returns a boolean: True if the update should be handled, False otherwise.
            The *filter* argument refers to the filter itself and can be used to access
            keyword arguments (read below).

        name (``str``, *optional*):
            Your filter's name. Can be anything you like.
            Defaults to "CustomFilter".

        **kwargs (``any``, *optional*):
            Any keyword argument you would like to pass.
    """
    return type(
        name or func.__name__ or 'CustomFilter',
        (Filter,),
        {'__call__': func, **kwargs},
    )()


def all_filter(_: Filter, event: Any) -> bool:
    return True


all = create(all_filter)
"""Filter all messages."""
