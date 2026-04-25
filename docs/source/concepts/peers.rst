.. _entities:

========
Peers
========

The library widely uses the concept of "entities". An entity will refer
to any `User <https:://tl.telethon.dev/?q=User>`, `Chat <https:://tl.telethon.dev/?q=Chat>`
or `Channel <https:://tl.telethon.dev/?q=Channel>` object that the API may return
in response to certain methods, such as `functions.GetUsers <grammers.functions.GetUsers>`.

.. note::

    When something "entity-like" is required, it means that you need to
    provide something that can be turned into an entity. These things include,
    but are not limited to, usernames, exact titles, IDs, `Peer` objects,
    or even entire `User`, `Chat` and `Channel` objects and even
    phone numbers **from people you have in your contact list**.

    To "encounter" an ID, you would have to "find it" like you would in the
    normal app. 
    If the peer is someone in a group, you would similarly
    `client.get_participants(group) <grammers.Client.get_participants>`.

    Once you have encountered an ID, the library will (by default) have saved
    their ``access_hash`` for you, which is needed to invoke most methods.
    This is why sometimes you might encounter this error when working with
    the library. You should ``except ValueError`` and run code that you know
    should work to find the entity.


.. contents::


What is a InputPeerLike?
========================

A lot of methods and requests require *entities* to work. For example,
you send a message to an *entity*, get the username of an *entity*, and
so on.

There are a lot of things that work as entities: usernames, phone numbers,
chat links, invite links, IDs, and the types themselves. That is, you can
use any of those when you see an "entity" is needed.

.. note::

    Remember that the phone number must be in your contact list before you
    can use it.

You should use, **from better to worse**:

2. Peer. For example, if you had to get someone's
   username, you can just use ``user`` or ``channel``.
   It will work. Only use this option if you already have the entity!

3. IDs. This will always look the entity up from the
   cache (the ``*.session`` file caches seen entities).

4. Usernames, phone numbers and links. The cache will be
   used too (unless you force a `client.get_entity()
   <telethon.client.users.UserMethods.get_entity>`),
   but may make a request if the username, phone or link
   has not been found yet.

In recent versions of the library, the following two are equivalent:

.. code-block:: python

    async def handler(event):
        await client.send_message(event.sender_id, 'Hi')
        await client.send_message(event.sender, 'Hi')


If you need to be 99% sure that the code will work (sometimes it's
simply impossible for the library to find the input entity), or if
you will reuse the chat a lot, consider using the following instead:

.. code-block:: python

    async def handler(event):
        # This method may make a network request to find the input sender.
        # Properties can't make network requests, so we need a method.
        sender = await event.get_input_sender()
        await client.send_message(sender, 'Hi')
        await client.send_message(sender, 'Hi')


Getting Entities
================

Through the use of the :ref:`sessions`, the library will automatically
remember the ID and hash pair, along with some extra information, so
you're able to just do this:

.. code-block:: python

    # All of these work and do the same.
    username = await client.get_entity('username')
    username = await client.get_entity('t.me/username')
    username = await client.get_entity('https://telegram.dog/username')

    # Other kind of entities.
    channel = await client.get_entity('telegram.me/joinchat/AAAAAEkk2WdoDrB4-Q8-gg')
    contact = await client.get_entity('+34xxxxxxxxx')
    friend  = await client.get_entity(friend_id)

    # Getting entities through their ID (User, Chat or Channel)
    entity = await client.get_entity(some_id)

    # You can be more explicit about the type for said ID by wrapping
    # it inside a Peer instance. This is recommended but not necessary.
    from telethon.tl.types import PeerUser, PeerChat, PeerChannel

    my_user    = await client.get_entity(PeerUser(some_id))
    my_chat    = await client.get_entity(PeerChat(some_id))
    my_channel = await client.get_entity(PeerChannel(some_id))


.. note::

    You **don't** need to get the entity before using it! Just let the
    library do its job. Use a phone from your contacts, username, ID or
    input entity (preferred but not necessary), whatever you already have.

All methods in the :ref:`grammers-client` call `.get_input_entity()
<grammers.Client.get_input_entity>` prior
to sending the request to save you from the hassle of doing so manually.
That way, convenience calls such as `client.send_message('username', 'hi!')
<grammers.Client.send_message>`
become possible.

Every entity the library encounters (in any response to any call) will by
default be cached in the ``.session`` file (an SQLite database), to avoid
performing unnecessary API calls. If the entity cannot be found, additonal
calls like `ResolveUsernameRequest` or `GetContactsRequest` may be
made to obtain the required information.


FullPeer
=============

In addition to `PeerUser`, `InputPeerUser`, `User` (and its
variants for chats and channels), there is also the concept of `UserFull`.

This full variant has additional information such as whether the user is
blocked, its notification settings, the bio or about of the user, etc.

There is also `messages.ChatFull` which is the equivalent of full entities
for chats and channels, with also the about section of the channel. Note that
the ``users`` field only contains bots for the channel (so that clients can
suggest commands to use).

You can get both of these by invoking `GetFullUser`, `GetFullChat`
and `GetFullChannel` respectively.


Summary
=======

TL;DR; If you're here because of *"Could not find the input entity for"*,
you must ask yourself "how did I find this entity through official
applications"? Now do the same with the library. Use what applies:

.. code-block:: python

    # (These examples assume you are inside an "async def")
    async with client:
        # Does it have a username? Use it!
        entity = await client.get_entity(username)

        # Are they participant of some group? Get them.
        await client.get_participants('username')

        # Is the entity the original sender of a forwarded message? Get it.
        await client.get_messages('username', 100)

        # NOW you can use the ID, anywhere!
        await client.send_message(123456, 'Hi!')

        entity = await client.get_entity(123456)
        print(entity)

Once the library has "seen" the entity, you can use their **integer** ID.
You can't use entities from IDs the library hasn't seen. You must make the
library see them *at least once* and disconnect properly. You know where
the entities are and you must tell the library. It won't guess for you.
