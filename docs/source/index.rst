.. grammers-python documentation master file, created by
   sphinx-quickstart on Fri Apr 24 16:04:16 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

================================
grammers-python's documentation
================================

.. code-block:: python

    from grammers import Client

    client = Client(name, api_id, api_hash)

    async def main():
        async client:
            # Now you can use all client methods listed below, like for example...
            await client.send_message('me', 'Hello to myself!')

    client.run(main())


What is this?
-------------

grammers-python is the Python bindings of `gramme.rs <https://codeberg.org/Lonami/grammers>`_. 
This library aims to balance the performance of Rust and the ease of use of Python.


.. toctree::
    :hidden:
    :caption: First Steps

    basic/installation
    basic/signing-in
    basic/quick-start
    basic/updates
    basic/next-steps

.. toctree::
    :hidden:
    :caption: Quick References

    quick-references/client-reference
    quick-references/events-reference
    quick-references/objects-reference

.. toctree::
    :hidden:
    :caption: Concepts

    concepts/strings
    concepts/peers
    concepts/chats-vs-channels
    concepts/updates
    concepts/sessions
    concepts/full-api
    concepts/errors
    concepts/botapi-vs-mtproto
    concepts/asyncio

.. toctree::
    :hidden:
    :caption: Grammers-Python Modules

    modules/client
    modules/events
    modules/custom
    modules/utils
    modules/errors
    modules/sessions
