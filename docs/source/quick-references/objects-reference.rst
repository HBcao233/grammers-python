=================
Objects Reference
=================

This is the quick reference for those objects returned by client methods
or other useful modules that the library has to offer. They are kept in
a separate page to help finding and discovering them.

Remember that this page only shows properties and methods,
**not attributes**. Make sure to open the full documentation
to find out about the attributes.

.. contents::

Message
=======

.. currentmodule:: grammers.custom.Message

The `Message` type is very important, mostly because we are working
with a library for a *messaging* platform, so messages are widely used:
in events, when fetching history, replies, etc.

Properties
----------

.. note::

    We document *custom properties* here, not all the attributes of the
    `Message` (which is the information Telegram actually returns).

.. currentmodule:: grammers.custom.Message

.. autosummary::
    :nosignatures:

    client


Methods
-------

.. autosummary::
    :nosignatures:

    get_reply_to


Utils
=====

The `grammers.utils` module has plenty of methods that make using the
library a lot easier. Only the interesting ones will be listed here.

.. currentmodule:: grammers.utils

.. autosummary::
    :nosignatures:

    parse_phone
    maybe_call
    maybe_await
