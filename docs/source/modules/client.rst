.. _grammers-client:

=======
Client
=======

.. currentmodule:: grammers.client

**In short, to create a client you can use:**

.. code-block:: python

    from grammers import Client

    client = Client(name, api_id, api_hash)

    async def main():
        async client:
            # Now you can use all client methods listed below, like for example...
            await client.send_message('me', 'Hello to myself!')

    client.run(main())

See :ref:`client-ref` for a short summary.

.. automodule:: grammers.client
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: grammers._rs.client
    :members:
    :undoc-members:
    :show-inheritance:
