======================
String-based Debugging
======================

Debugging is *really* important. Telegram's API is really big and there
are a lot of things that you should know. Such as, what attributes or fields
does a result have? Well, the easiest thing to do is printing it:

.. code-block:: python

    peer = await client.resolve_username('username')
    print(peer)

That will show a huge **string** similar to the following:

.. code-block:: python

    Channel(
    	id=PeerId(bot_api_dialog_id=-1001066197625, kind=PeerKind.Channel, bare_id=1066197625),
    	title='Telegram Usernames',
    	access_hash=PeerAuth(-867107574443743314),
    	username='username',
    	usernames=[],
    	photo=ChatPhoto(
    		has_video=False,
    		photo_id=4929276344794196832,
    		stripped_thumb=b'\x01\x08\x08\x9b|^_\xf1o\xc7\xebE\x14Wg)\xc7s',
    		dc_id=1
    	),
    	date=datetime.datetime(2016, 12, 16, 15, 15, 43),
    	broadcast=False,
    	megagroup=False,
    	until_date=None,
    	creator=False,
    	left=True,
    	verified=True,
    	restricted=False,
    	signatures=False,
    	min=False,
    	scam=False,
    	has_link=False,
    	has_geo=False,
    	slowmode_enabled=False,
    	call_active=False,
    	call_not_empty=False,
    	fake=False,
    	gigagroup=False,
    	noforwards=False,
    	join_to_send=False,
    	join_request=False,
    	forum=False,
    	stories_hidden=False,
    	stories_hidden_min=True,
    	stories_unavailable=True,
    	signature_profiles=False,
    	autotranslation=False,
    	broadcast_messages_allowed=False,
    	monoforum=False,
    	forum_tabs=False,
    	restriction_reason=[],
    	admin_rights=None,
    	banned_rights=None,
    	default_banned_rights=None,
    	participants_count=None,
    	stories_max_id=None,
    	color=None,
    	profile_color=None,
    	emoji_status=None,
    	level=None,
    	subscription_until_date=None,
    	bot_verification_icon=None,
    	send_paid_messages_stars=None,
    	linked_monoforum_id=None
    )

That's a lot of text. But as you can see, all the properties are there.
So if you want the title you **don't use regex** or anything like
splitting ``str(peer)`` to get what you want. You just access the
attribute you need:

.. code-block:: python

    title = entity.title

Now it's easy to see how we could get, for example,
the ``year`` value. It's inside ``date``:

.. code-block:: python

    channel_year = entity.date.year

You don't need to print everything to see what all the possible values
can be. You can just search in http://tl.telethon.dev/.

Remember that you can use Python's `isinstance
<https://docs.python.org/3/library/functions.html#isinstance>`_
to check the type of something. For example:

.. code-block:: python

    from telethon import types

    if isinstance(entity.photo, types.ChatPhotoEmpty):
        print('Channel has no photo')
