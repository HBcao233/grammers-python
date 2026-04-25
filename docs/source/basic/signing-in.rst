.. _signing-in:

==========
Signing In
==========

Before working with Telegram's API, you need to get your own API ID and hash:

1. `Login to your Telegram account <https://my.telegram.org/>`_ with the
   phone number of the developer account to use.

2. Click under API Development tools.

3. A *Create new application* window will appear. Fill in your application
   details. There is no need to enter any *URL*, and only the first two
   fields (*App title* and *Short name*) can currently be changed later.

4. Click on *Create application* at the end. Remember that your
   **API hash is secret** and Telegram won't let you revoke it.
   Don't post it anywhere!

.. note::

    This API ID and hash is the one used by *your application*, not your
    phone number. You can use this API ID and hash with *any* phone number
    or even for bot accounts.


Editing the Code
================

This is a little introduction for those new to Python programming in general.

We will write our code inside ``hello.py``, so you can use any text
editor that you like. To run the code, use ``python3 hello.py`` from
the terminal.

.. important::

    Don't call your script ``telethon.py``! Python will try to import
    the client from there and it will fail with an error such as
    "ImportError: cannot import name 'TelegramClient' ...".


Signing In
==========

We can finally write some code to log into our account!

.. code-block:: python

    from grammers import Client

    # Use your own values from my.telegram.org
    api_id = 12345
    api_hash = '0123456789abcdef0123456789abcdef'

    # The first parameter is the .session file name (absolute paths allowed)
    client = Client('anon', api_id, api_hash)
    
    async def main():
        await client.send_message('me', 'Hello, myself!')
    
    client.run(main())


In the first line, we import the class name so we can create an instance
of the client. Then, we define variables to store our API ID and hash
conveniently.

At last, we create a new `Client <grammers.Client>`_
instance and call it ``client``. We can now use the client variable
for anything that we want, such as sending a message to ourselves.

.. note::

    Since Grammers is an asynchronous library, you need to ``await``
    coroutine functions to have them run (or otherwise, run the loop
    until they are complete). In this tiny example, we don't bother
    making an ``async def main()``.

    See :ref:`mastering-asyncio` to find out more.


If the ``.session`` file already existed, it will not login
again, so be aware of this if you move or rename the file!


Signing In as a Bot Account
===========================

You can also use Grammers for your bots (normal bot accounts, not users).
You will still need an API ID and hash, but the process is very similar:


.. code-block:: python

    from grammers import Client

    api_id = 12345
    api_hash = '0123456789abcdef0123456789abcdef'
    bot_token = '12345:0123456789abcdef0123456789abcdef'

    bot = Client(
        'bot',
        api_id,
        api_hash,
        bot_token=bot_token
    )

    # But then we can use the client instance as usual
    async def main():
        ...

    bot.run(main())


To get a bot account, you need to talk
with `@BotFather <https://t.me/BotFather>`_.


Signing In behind a Proxy
=========================

.. warning::
    TODO

If you need to use a proxy to access Telegram,
you will need to pass a proxy argument to the client:

.. code-block:: python

    Client('anon', api_id, api_hash, proxy=...)

The ``proxy=`` argument should be a dict with the following properties:

.. code-block:: python

    proxy = {
        'proxy_type': 'socks5', # (mandatory) protocol to use (see above)
        'addr': '1.1.1.1',      # (mandatory) proxy IP address
        'port': 5555,           # (mandatory) proxy port number
        'username': 'foo',      # (optional) username if the proxy requires auth
        'password': 'bar',      # (optional) password if the proxy requires auth
        'rdns': True            # (optional) whether to use remote or local resolve, default remote
    }


Using MTProto Proxies
=====================

.. warning::
    TODO

MTProto Proxies are Telegram's alternative to normal proxies,
and work a bit differently. The following protocols are available:

* ``ConnectionTcpMTProxyAbridged``
* ``ConnectionTcpMTProxyIntermediate``
* ``ConnectionTcpMTProxyRandomizedIntermediate`` (preferred)

For now, you need to manually specify these special connection modes
if you want to use a MTProto Proxy. Your code would look like this:

.. code-block:: python

    from grammers import Client, connection
    # we need to change the connection ^^^^^^^^^^

    client = Client(
        'anon',
        api_id,
        api_hash,

        # Use one of the available connection modes.
        # Normally, this one works with most proxies.
        connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,

        # Then, pass the proxy details as a tuple:
        #     (host name, port, proxy secret)
        #
        # If the proxy has no secret, the secret must be:
        #     '00000000000000000000000000000000'
        proxy=('mtproxy.example.com', 2002, 'secret')
    )

In future updates, we may make it easier to use MTProto Proxies
(such as avoiding the need to manually pass ``connection=``).

In short, the same code above but without comments to make it clearer:

.. code-block:: python

    from grammers import Client, connection

    client = Client(
        'anon', api_id, api_hash,
        connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
        proxy=('mtproxy.example.com', 2002, 'secret')
    )
