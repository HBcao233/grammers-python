================
Events Reference
================

Here you will find a quick summary of all the methods
and properties that you can access when working with events.

You can access the client that creates this event by doing
``event.client``, and you should view the description of the
events to find out what arguments it allows on creation and
its **attributes** (the properties will be shown here).

.. contents::


NewMessage
==========

Occurs whenever a new text message or a message with media arrives.

.. note::

    The new message event **should be treated as** a
    normal `Message <grammers.custom.Message>`, with
    the following exceptions:

    * ``pattern_match`` is the match object returned by ``pattern=``.
    * ``message`` is **not** the message string. It's the `Message
      <grammers.custom.Message>` object.

    Remember, this event is just a proxy over the message, so while
    you won't see its attributes and properties, you can still access
    them. Please see the full documentation for examples.

Full documentation for the `NewMessage
<grammers.events.NewMessage>`_.

Raw
===

Raw events are not actual events. Instead, they are the raw
:tl:`Update` object that Telegram sends. You normally shouldn't
need these.
