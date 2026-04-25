.. _client-ref:

================
Client Reference
================

This page contains a summary of all the important methods and properties that
you may need when using Grammers-Python. They are sorted by relevance and are not in
alphabetical order.

You should use this page to learn about which methods are available, and
if you need a usage example or further description of the arguments, be
sure to follow the links.

.. contents::

Client
==============

This is a summary of the methods and
properties you will find at :ref:`grammers-client`.

Net
------

.. currentmodule:: grammers.client.Client

.. autosummary::
    :nosignatures:

    invoke
    invoke_raw

Utilities
---------

.. currentmodule:: grammers.client.Client

.. autosummary::
    :nosignatures:

    start
    stop
    idle
    run

Auth
----

.. currentmodule:: grammers.client.Client

.. autosummary::
    :nosignatures:

    is_authorized
    authorize
    bot_sign_in
    request_login_code
    sign_in
    get_password_information
    check_password
    sign_out
    disconnect
    _check_password
    _complete_login

Chats 
-----

.. currentmodule:: grammers.client.Client

.. autosummary::
    :nosignatures:

    get_me
    resolve_username
    resolve_phone
    resolve_input_peer
    resolve_peer
    resolve_peer_ref
    check_invite_link
    accept_invite_link

Messages
--------

.. currentmodule:: grammers.client.Client

.. autosummary::
    :nosignatures:

    get_messages_by_id
    iter_history_messages
