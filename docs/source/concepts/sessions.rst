.. _sessions:

==============
Session Files
==============

.. contents::

They are an important part for the library to be efficient, such as caching
and handling your authorization key (or you would have to login every time!).

What are Sessions?
==================

The first parameter you pass to the constructor of the
:ref:`Client <grammers-client>` is
the ``session``, and defaults to be the session name (or full path). That is,
if you create a ``Client('anon')`` instance and connect, an
``anon.session`` file will be created in the working directory.

Note that if you pass a string it will be a file in the current working
directory, although you can also pass absolute paths.

The session file contains enough information for you to login without
re-sending the code, so if you have to enter the code more than once,
maybe you're changing the working directory, renaming or removing the
file, or using random names.

These database files using ``sqlite3`` contain the required information to
talk to the Telegram servers, such as to which IP the client should connect,
port, authorization key so that messages can be encrypted, and so on.

These files will by default also save all the input entities that you've seen,
so that you can get information about a user or channel by just their ID.
Telegram will **not** send their ``access_hash`` required to retrieve more
information about them, if it thinks you have already seem them. For this
reason, the library needs to store this information offline.

The library will by default too save all the entities (chats and channels
with their name and username, and users with the phone too) in the session
file, so that you can quickly access them by username or phone number.

.. 
    If you're not going to work with updates, or don't need to cache the
    ``access_hash`` associated with the entities' ID, you can disable this
    by setting ``client.session.save_entities = False``.


Different Session Storage
=========================

If you don't want to use the default SQLite session storage, you can also
use one of the other implementations or implement your own storage.

While it's often not the case, it's possible that SQLite is slow enough to
be noticeable, in which case you can also use a different storage. Note that
this is rare and most people won't have this issue, but it's worth a mention.

To use a custom session storage, simply pass the custom session instance to
:ref:`Client <grammers-client>` instead of
the session name.

grammers-python contains three implementations of the abstract ``Session`` class:

.. currentmodule:: grammers.sessions

* `SQLiteSession <SQLiteSession>`: stores sessions within on-disk SQLite databases. Default.

You can import these ``from grammers.sessions``. For example, using the
`SQLiteSession <SQLiteSession>` is done as follows:

.. code-block:: python

    from grammers import Client
    from grammers.sessions import SQLiteSession

    session = SQLiteSession('anon.session')
    client = Client(session, api_id, api_hash)


String Sessions
===============

`SQLiteSession.from_telethon_string() <SQLiteSession.from_telethon_string>` are a convenient way to embed your
login credentials directly into your code for extremely easy portability,
since all they take is a string to be able to login without asking for your
phone and code (or faster start if you're using a bot token).

The easiest way to generate a string session is as follows:

.. code-block:: python

    from grammers import Client
    from grammers.sessions import StringSession

    string = '1aaNk8EX-YRfwoRsebUkugFvht6DUPi_Q25UOCzOAqzc...'
    session = SQLiteSession.from_telethon_string(string)
    client = Client(session, api_id, api_hash)


Think of this as a way to export your authorization key (what's needed
to login into your account). This will print a string in the standard
output (likely your terminal).

.. warning::

    **Keep this string safe!** Anyone with this string can use it
    to login into your account and do anything they want to.

    This is similar to leaking your ``*.session`` files online,
    but it is easier to leak a string than it is to leak a file.


Once you have the string (which is a bit long), load it into your script
somehow. You can use a normal text file and ``open(...).read()`` it or
you can save it in a variable directly:

These strings are really convenient for using in places like Heroku since
their ephemeral filesystem will delete external files once your application
is over.
