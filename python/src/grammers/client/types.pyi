from . import Client
from .. import types, hints
from ..sessions import PeerId, PeerAuth
from ..tl import TLObject
from typing import Self, final
from datetime import datetime

class LoginToken:
    def __new__(cls, phone: str, phone_code_hash: str) -> Self: ...
    @property
    def phone(self) -> str: ...
    @property
    def phone_code_hash(self) -> str: ...
    def __repr__(self) -> str: ...

class SignInError(Exception):
    """Login-related errors."""

    ...

class PaymentRequiredError(SignInError):
    """
    Indicating that due to the high cost of SMS verification codes for the user's country/provider, the user must purchase a Telegram Premium subscription in order to proceed with the login/signup.
    """

    ...

class SignUpRequiredError(SignInError):
    """
    Sign-up with an official client is required. (Third-party applications cannot be used to register new accounts.)
    """

    ...

class PasswordRequiredError(SignInError):
    """
    The account has 2FA enabled, and the password is required.
    """

    ...

class InvalidCodeError(SignInError):
    """
    The code used to complete login was not valid.
    """

    ...

class InvalidPasswordError(SignInError):
    """
    The 2FA password used to complete login was not valid.
    """

    ...

class Platform:
    """
    Platform Identifier referenced only by [`RestrictionReason`].
    """
    @final
    class All(Platform):
        def __new__(cls) -> Self: ...

    @final
    class Android(Platform):
        def __new__(cls) -> Self: ...

    @final
    class Ios(Platform):
        def __new__(cls) -> Self: ...

    @final
    class WindowsPhone(Platform):
        def __new__(cls) -> Self: ...

    @final
    class Other(Platform):
        def __new__(cls, other: str) -> Self: ...

    def __repr__(self) -> str: ...

@final
class RestrictionReason:
    """
    Reason why a user is globally restricted.
    """
    def __new__(cls, reason: types.RestrictionReason): ...
    @property
    def platforms(self) -> list[Platform]: ...
    @property
    def reason(self) -> str: ...
    @property
    def text(self) -> str: ...
    def __repr__(self) -> str: ...

class User(TLObject):
    """
    A user.

    Users include your contacts, members of a group, bot accounts created by [@BotFather], or
    anyone with a Telegram account.

    A "normal" (non-bot) user may also behave like a "bot" without actually being one, for
    example, when controlled with a program as opposed to being controlled by a human through
    a Telegram application. These are commonly known as "userbots", and some people use them
    to enhance their Telegram experience (for example, creating "commands" so that the program
    automatically reacts to them, like translating messages).

    [@BotFather]: https://t.me/BotFather
    """
    def __new__(cls, user: types.User | types.UserEmpty): ...
    @property
    def id(self) -> PeerId: ...
    @property
    def access_hash(self) -> PeerAuth | None: ...
    @property
    def bot(self) -> bool: ...
    @property
    def is_self(self) -> bool: ...
    @property
    def restriction_reason(self) -> RestrictionReason: ...
    @property
    def contact(self) -> bool: ...
    @property
    def mutual_contact(self) -> bool: ...
    @property
    def deleted(self) -> bool: ...
    @property
    def bot_chat_history(self) -> bool: ...
    @property
    def bot_nochats(self) -> bool: ...
    @property
    def verified(self) -> bool: ...
    @property
    def restricted(self) -> bool: ...
    @property
    def min(self) -> bool: ...
    @property
    def bot_inline_geo(self) -> bool: ...
    @property
    def support(self) -> bool: ...
    @property
    def scam(self) -> bool: ...
    @property
    def apply_min_photo(self) -> bool: ...
    @property
    def fake(self) -> bool: ...
    @property
    def bot_attach_menu(self) -> bool: ...
    @property
    def premium(self) -> bool: ...
    @property
    def attach_menu_enabled(self) -> bool: ...
    @property
    def bot_can_edit(self) -> bool: ...
    @property
    def close_friend(self) -> bool: ...
    @property
    def stories_hidden(self) -> bool: ...
    @property
    def stories_unavailable(self) -> bool: ...
    @property
    def contact_require_premium(self) -> bool: ...
    @property
    def bot_business(self) -> bool: ...
    @property
    def bot_has_main_app(self) -> bool: ...
    @property
    def bot_forum_view(self) -> bool: ...
    @property
    def first_name(self) -> str | None: ...
    @property
    def last_name(self) -> str | None: ...
    @property
    def username(self) -> str | None: ...
    @property
    def phone(self) -> str | None: ...
    @property
    def photo(self) -> types.UserProfilePhoto | None: ...
    @property
    def status(self) -> types.UserStatus | None: ...
    @property
    def bot_info_version(self) -> int | None: ...
    @property
    def bot_inline_placeholder(self) -> str | None: ...
    @property
    def lang_code(self) -> str | None: ...
    @property
    def emoji_status(self) -> types.EmojiStatus | None: ...
    @property
    def usernames(self) -> list[types.Username]: ...
    @property
    def stories_max_id(self) -> types.RecentStory | None: ...
    @property
    def color(self) -> types.PeerColor | None: ...
    @property
    def profile_color(self) -> types.PeerColor | None: ...
    @property
    def bot_active_users(self):
        (int | None,)
    @property
    def bot_verification_icon(self):
        (int | None,)
    @property
    def send_paid_messages_stars(self):
        (int | None,)

class Group(TLObject):
    """
    A group chat.

    Telegram's API internally distinguishes between "small group chats" and "megagroups", also
    known as "supergroups" in the UI of Telegram applications.

    Small group chats are the default, and offer less features than megagroups, but you can
    join more of them. Certain actions in official clients, like setting a chat's username,
    silently upgrade the chat to a megagroup.
    """
    def __new__(
        cls,
        group: types.Chat
        | types.ChatEmpty
        | types.ChatForbidden
        | types.Channel
        | types.ChannelForbidden,
    ) -> Self: ...
    @property
    def id(self) -> PeerId:
        """
        Return the unique identifier for this group.

        Note that if this group is migrated to a megagroup, both this group and the new one will
        exist as separate chats, with different identifiers.
        """
        ...
    @property
    def title(self) -> str | None:
        """
        Return the title of this group.

        The title may be the empty string if the group is not accessible.
        """
        ...
    @property
    def date(self) -> datetime | None:
        """
        Date when the user joined the supergroup/channel,
        or if the user isn't a member, its creation date.
        """
        ...
    @property
    def date_timestamp(self) -> int | None:
        """
        `date` origin data.
        """
        ...
    @property
    def access_hash(self) -> PeerAuth | None: ...
    @property
    def broadcast(self) -> bool | None:
        """
        Whether this is a channel, always false.
        """
        ...
    @property
    def megagroup(self) -> bool | None:
        """
        Whether this is a supergroup, always true.
        """
        ...
    @property
    def until_date(self) -> datetime | None:
        """
        The ban is valid until the specified date.
        """
        ...
    @property
    def until_date_timestamp(self) -> int | None:
        """
        `until_date` origin data.
        """
        ...
    @property
    def creator(self) -> bool | None:
        """
        Whether the current user is the creator of this channel.
        """
        ...
    @property
    def left(self) -> bool | None:
        """
        Whether the current user has left or is not a member of this channel.
        """
        ...
    @property
    def deactivated(self) -> bool | None: ...
    @property
    def call_active(self) -> bool | None: ...
    @property
    def call_not_empty(self) -> bool | None: ...
    @property
    def noforwards(self) -> bool | None:
        """
        Whether this channel or group is protected, thus does not allow forwarding messages from it.
        """
        ...
    @property
    def photo(self) -> types.ChatPhoto | None: ...
    @property
    def participants_count(self) -> int | None: ...
    @property
    def version(self) -> int | None: ...
    @property
    def migrated_to(self) -> types.InputChannel | None: ...
    @property
    def admin_rights(self) -> types.ChatAdminRights | None: ...
    @property
    def default_banned_rights(self) -> types.ChatBannedRights | None: ...
    @property
    def verified(self) -> bool | None:
        """
        Whether this channel is verified by telegram.
        """
        ...
    @property
    def restricted(self) -> bool | None: ...
    @property
    def signatures(self) -> bool | None: ...
    @property
    def min(self) -> bool | None: ...
    @property
    def scam(self) -> bool | None: ...
    @property
    def has_link(self) -> bool | None: ...
    @property
    def has_geo(self) -> bool | None: ...
    @property
    def slowmode_enabled(self) -> bool | None: ...
    @property
    def fake(self) -> bool | None: ...
    @property
    def gigagroup(self) -> bool | None:
        """
        Whether this supergroup is a gigagroup.
        """
        ...
    @property
    def join_to_send(self) -> bool | None:
        """
        Whether a user needs to join the supergroup before they can send messages:
        can be false only for discussion groups.
        toggle using `channels.toggleJoinToSend`
        """
        ...
    @property
    def join_request(self) -> bool | None: ...
    @property
    def forum(self) -> bool | None: ...
    @property
    def stories_hidden(self) -> bool | None: ...
    @property
    def stories_hidden_min(self) -> bool | None: ...
    @property
    def stories_unavailable(self) -> bool | None: ...
    @property
    def signature_profiles(self) -> bool | None: ...
    @property
    def autotranslation(self) -> bool | None: ...
    @property
    def broadcast_messages_allowed(self) -> bool | None: ...
    @property
    def monoforum(self) -> bool | None: ...
    @property
    def forum_tabs(self) -> bool | None: ...
    @property
    def username(self) -> str | None: ...
    @property
    def restriction_reason(self) -> list[RestrictionReason] | None: ...
    @property
    def banned_rights(self) -> types.ChatBannedRights | None: ...
    @property
    def usernames(self) -> list[types.Username]: ...
    @property
    def stories_max_id(self) -> types.RecentStory | None: ...
    @property
    def color(self) -> types.PeerColor | None: ...
    @property
    def profile_color(self) -> types.PeerColor | None: ...
    @property
    def emoji_status(self) -> types.EmojiStatus | None: ...
    @property
    def level(self) -> int | None: ...
    @property
    def subscription_until_date(self) -> datetime | None: ...
    @property
    def subscription_until_date_timestamp(self) -> int | None: ...
    @property
    def bot_verification_icon(self) -> int | None: ...
    @property
    def send_paid_messages_stars(self) -> int | None: ...
    @property
    def linked_monoforum_id(self) -> int | None: ...

class Channel(TLObject):
    """
    A broadcast channel.

    In a broadcast channel, only administrators can broadcast messages to all the subscribers.
    The rest of users can only join and see messages.

    Broadcast channels and megagroups both are treated as "channels" by Telegram's API, but
    this variant will always represent a broadcast channel. The only difference between a
    broadcast channel and a megagroup are the permissions (default, and available).
    """
    def __new__(cls, channel: types.Channel | types.ChannelForbidden) -> Self: ...
    @property
    def id(self) -> PeerId: ...
    @property
    def title(self) -> str:
        """
        Return the title of this channel.
        """
        ...

    @property
    def access_hash(self) -> PeerAuth | None: ...
    @property
    def username(self) -> str | None:
        """
        Return the deflic @username of this channel, if any.

        The returned username does not contain the "@" prefix.

        Outside of the application, people may link to this user with one of Telegram's URLs, such
        as https://t.me/username.
        """
        ...

    @property
    def usernames(self) -> list[types.Username]:
        """
        Return collectible usernames of this channel, if any.

        The returned usernames do not contain the "@" prefix.

        Outside of the application, people may link to this user with one of its username, such
        as https://t.me/username.
        """
        ...

    @property
    def photo(self) -> types.ChatPhoto | None:
        """
        Return the photo of this channel, if any.
        """
        ...

    @property
    def date(self) -> datetime | None: ...
    @property
    def date_timestamp(self) -> int | None: ...
    @property
    def until_date(self) -> datetime | None: ...
    @property
    def until_date_timestamp(self) -> int | None: ...
    @property
    def broadcast(self) -> bool: ...
    @property
    def megagroup(self) -> bool: ...
    @property
    def creator(self) -> bool | None: ...
    @property
    def left(self) -> bool | None: ...
    @property
    def verified(self) -> bool | None: ...
    @property
    def restricted(self) -> bool | None: ...
    @property
    def signatures(self) -> bool | None: ...
    @property
    def min(self) -> bool | None: ...
    @property
    def scam(self) -> bool | None: ...
    @property
    def has_link(self) -> bool | None: ...
    @property
    def has_geo(self) -> bool | None: ...
    @property
    def slowmode_enabled(self) -> bool | None: ...
    @property
    def call_active(self) -> bool | None: ...
    @property
    def call_not_empty(self) -> bool | None: ...
    @property
    def fake(self) -> bool | None: ...
    @property
    def gigagroup(self) -> bool | None: ...
    @property
    def noforwards(self) -> bool | None: ...
    @property
    def join_to_send(self) -> bool | None: ...
    @property
    def join_request(self) -> bool | None: ...
    @property
    def forum(self) -> bool | None: ...
    @property
    def stories_hidden(self) -> bool | None: ...
    @property
    def stories_hidden_min(self) -> bool | None: ...
    @property
    def stories_unavailable(self) -> bool | None: ...
    @property
    def signature_profiles(self) -> bool | None: ...
    @property
    def autotranslation(self) -> bool | None: ...
    @property
    def broadcast_messages_allowed(self) -> bool | None: ...
    @property
    def monoforum(self) -> bool | None: ...
    @property
    def forum_tabs(self) -> bool | None: ...
    @property
    def restriction_reason(self) -> list[RestrictionReason]: ...
    @property
    def admin_rights(self) -> types.ChatAdminRights | None: ...
    @property
    def banned_rights(self) -> types.ChatBannedRights | None: ...
    @property
    def default_banned_rights(self) -> types.ChatBannedRights | None: ...
    @property
    def participants_count(self) -> int | None: ...
    @property
    def stories_max_id(self) -> types.RecentStory | None: ...
    @property
    def color(self) -> types.PeerColor | None: ...
    @property
    def profile_color(self) -> types.PeerColor | None: ...
    @property
    def emoji_status(self) -> types.EmojiStatus | None: ...
    @property
    def level(self) -> int | None: ...
    @property
    def subscription_until_date(self) -> datetime | None: ...
    @property
    def subscription_until_date_timestamp(self) -> int | None: ...
    @property
    def bot_verification_icon(self) -> int | None: ...
    @property
    def send_paid_messages_stars(self) -> int | None: ...
    @property
    def linked_monoforum_id(self) -> int | None: ...

class PeerMap: ...

class Message(TLObject):
    """
    Represents a Telegram message, which includes text messages, messages with media, and service
    messages.

    This message should be treated as a snapshot in time, that is, if the message is edited while
    using this object, those changes won't alter this structure.
    """
    def __new__(
        cls, client: Client, message: hints.Message, peers: PeerMap
    ) -> Self: ...
    @property
    def id(self) -> int:
        """
        The ID of this message.

        Message identifiers are counters that start at 1 and grow by 1 for each message produced.

        Every channel has its own unique message counter. This counter is the same for all users,
        but unique to each channel.

        Every account has another unique message counter which is used for private conversations
        and small group chats. This means different accounts will likely have different message
        identifiers for the same message in a private conversation or small group chat. This also
        implies that the message identifier alone is enough to uniquely identify the message,
        without the need to know the chat ID.

        **You cannot use the message ID of User A when running as User B**, unless this message
        belongs to a megagroup or broadcast channel. Beware of this when using methods like
        [`Client::delete_messages`], which **cannot** validate the peer where the message
        should be deleted for those cases.
        """
        ...
    @property
    def peer_id(self) -> PeerId | None:
        """
        The [`Self.peer`]'s identifier.
        """
        ...
    @property
    def peer(self) -> types.Peer | None:
        """
        The peer where this message was sent to.

        This might be the user you're talking to for private conversations, or the group or
        channel where the message was sent.
        """
        ...
    @property
    def sender_id(self) -> PeerId | None:
        """
        The [`Self.sender`]'s identifier, if there is a sender.
        """
        ...
    @property
    def sender(self) -> types.Peer | None:
        """
        The sender of this message, if there is a sender **and** the sender is in cache.
        """
        ...
    @property
    def out(self) -> bool | None:
        """
        Whether the message is outgoing (i.e. you sent this message to some other peer) or
        incoming (i.e. someone else sent it to you or the peer).
        """
        ...
    @property
    def mentioned(self) -> bool | None:
        """
        Whether you were mentioned in this message or not.

        This includes @username mentions, text mentions, and messages replying to one of your
        previous messages (even if it contains no mention in the message text).
        """
        ...
    @property
    def media_unread(self) -> bool | None:
        """
        Whether you have read the media in this message or not.

        Most commonly, these are voice notes that you have not played yet.
        """
        ...
    @property
    def reactions_are_possible(self) -> bool | None:
        """
        Whether you can react to this message.

        MessageService only.
        """
        ...
    @property
    def silent(self) -> bool | None:
        """
        Whether the message should notify people with sound or not.
        """
        ...
    @property
    def post(self) -> bool | None:
        """
        Whether this message is a post in a broadcast channel or not.
        """
        ...
    @property
    def from_scheduled(self) -> bool | None:
        """
        Whether this message was originated from a previously-scheduled message or not.
        """
        ...
    @property
    def legacy(self) -> bool | None:
        """
        Whether this is a legacy message: it has to be refetched with the new layer.
        """
        ...
    @property
    def edit_hide(self) -> bool | None:
        """
        Whether the edited mark of this message is edited should be hidden (e.g. in GUI clients)
        or shown.
        """
        ...
    @property
    def pinned(self) -> bool | None:
        """
        Whether this message is currently pinned or not.
        """
        ...
    @property
    def noforwards(self) -> bool | None:
        """
        Whether this message is protected and thus cannot be forwarded; clients should also
        prevent users from saving attached media (i.e. videos should only be streamed,
        photos should be kept in RAM, et cetera).
        """
        ...
    @property
    def invert_media(self) -> bool | None:
        """
        If set, any eventual webpage preview will be shown on top of the message instead of at the bottom.
        """
        ...
    @property
    def offline(self) -> bool | None:
        """
        If set, the message was sent because of a scheduled action by the message sender,
        for example, as away, or a greeting service message.
        """
        ...
    @property
    def video_processing_pending(self) -> bool | None:
        """
        The video contained in the message is currently being processed by the server
        (i.e. to generate alternative qualities, that will be contained in the final messageMediaDocument.alt_document)
        """
        ...
    @property
    def paid_suggested_post_stars(self) -> bool | None:
        """
        Set if this is a suggested channel post that was paid using Telegram Stars.
        """
        ...
    @property
    def paid_suggested_post_ton(self) -> bool | None:
        """
        Set if this is a suggested channel post that was paid using Toncoins.
        """
        ...
    @property
    def from_id(self) -> PeerId | None:
        """
        Raw from_id, generally use `sender_id` instead.
        """
        ...
    @property
    def from_boosts_applied(self) -> int | None:
        """
        Supergroups only, contains the number of boosts this user has given the current supergroup.
        """
        ...
    @property
    def saved_peer_id(self) -> PeerId | None:
        """
        Messages from a saved messages dialog will have peer=inputPeerSelf and the saved_peer_id flag set to the ID of the saved dialog.
        Messages from a monoforum will have peer=ID of the monoforum and the saved_peer_id flag set to the ID of a topic.
        """
        ...
    @property
    def fwd_from(self) -> types.MessageFwdHeader | None:
        """
        Info about forwarded messages.
        """
        ...
    @property
    def via_bot_id(self) -> int | None:
        """
        If this message was sent @via some inline bot, return the bot's user identifier.
        """
        ...
    @property
    def via_business_bot_id(self) -> int | None:
        """
        Whether the message was sent by the business bot specified in via_bot_id on behalf of the user.
        """
        ...
    @property
    def reply_to(self) -> hints.MessageReplyHeader | None:
        """
        If this message is replying to a previous message, return the header with information
        about that reply.
        If you want get the reply to `Message`, use `async Message.get_reply_to()` instead.
        """
        ...
    @property
    def date(self) -> datetime | None:
        """
        The date when this message was produced.
        """
        ...
    @property
    def date_timestamp(self) -> int | None:
        """
        raw date timestamp data from telegram.
        """
        ...
    @property
    def action(self) -> types.MessageAction | None:
        """
        Event connected with the service message.

        MessageService only.
        """
        ...
    @property
    def message(self) -> str | None:
        """
        The message's text.

        For service or empty messages, this will be None.

        If the message has media, this text is the caption commonly displayed underneath it.
        """
        ...
    @property
    def media(self) -> hints.MessageMedia | None:
        """
        The media displayed by this message, if any.

        This not only includes photos or videos, but also contacts, polls, documents, locations
        and many other types.
        """
        ...
    @property
    def reply_markup(self) -> hints.ReplyMarkup | None:
        """
        If the message has a reply markup (which can happen for messages produced by bots),
        returns said markup.
        """
        ...
    @property
    def entities(self) -> hints.MessageEntity | None:
        """
        Message entities for styled text
        """
        ...
    @property
    def views(self) -> int | None:
        """
        How many views does this message have, when applicable.

        The same user account can contribute to increment this counter indefinitedly, however
        there is a server-side cooldown limitting how fast it can happen (several hours).
        """
        ...
    @property
    def forwards(self) -> int | None:
        """
        How many times has this message been forwarded, when applicable.
        """
        ...
    @property
    def replies(self) -> types.MessageReplies | None:
        """
        How many replies does this message have, when applicable.
        """
        ...
    @property
    def edit_date(self) -> int | None:
        """
        The date when this message was last edited.
        """
        ...
    @property
    def post_author(self) -> str | None:
        """
        If this message was sent to a channel, return the name used by the author to post it.
        """
        ...
    @property
    def grouped_id(self) -> int | None:
        """
         If this message belongs to a group of messages, return the unique identifier for that
         group.

        This applies to albums of media, such as multiple photos grouped together.

         Note that there may be messages sent in between the messages forming a group.
        """
        ...
    @property
    def reactions(self) -> types.MessageReactions | None:
        """
        Reactions to this message
        """
        ...
    @property
    def restriction_reason(self) -> list[types.RestrictionReason] | None:
        """
        A list of reasons on why this message is restricted.

        The message is not restricted if the return value is `None`.
        """
        ...
    @property
    def ttl_period(self) -> int | None:
        """
        Time To Live of the message, once message.date+message.ttl_period === time(), the message will be deleted on the server, and must be deleted locally as well.
        """
        ...
    @property
    def quick_reply_shortcut_id(self) -> int | None:
        """
        If set, this message is a quick reply shortcut message » (note that quick reply shortcut messages sent to a private chat will not have this field set).
        """
        ...
    @property
    def effect(self) -> int | None:
        """
        A message effect that should be played as specified here.
        """
        ...
    @property
    def factcheck(self) -> types.FactCheck | None:
        """
        Represents a fact-check.
        """
        ...
    @property
    def report_delivery_until_date(self) -> int | None:
        """
        Used for Telegram Gateway verification messages: if set and the current unixtime is bigger than the specified unixtime, invoke messages.reportMessagesDelivery passing the ID and the peer of this message as soon as it is received by the client (optionally batching requests for the same peer).
        """
        ...
    @property
    def paid_message_stars(self) -> int | None:
        """
        The amount of stars the sender has paid to send the message.
        """
        ...
    @property
    def suggested_post(self) -> int | None:
        """
        Used to suggest a post to a channel.
        """
        ...
    @property
    def schedule_repeat_period(self) -> int | None: ...
    @property
    def summary_from_language(self) -> str | None: ...
    def to_dict(self) -> dict: ...

class HistoryMessageIter:
    """
    Create by `Client.iter_history_messages`.
    """
    def __new__(
        cls,
        client: Client,
        peer: hints.InputPeerLike,
        *,
        offset_id: int = 0,
        offset_date: int = 0,
        add_offset: int = 0,
        limit: int | None = None,
        page_limit: int = 0,
        max_id: int = 0,
        min_id: int = 0,
    ) -> Self: ...
    def __aiter__(self): ...
    def __anext__(self): ...
    async def init(self): ...
    async def total(self) -> int:
        """
        /// Determines how many messages there are in total.

        This only performs a network call if `next` has not been called before.
        """
        ...
    async def next(self) -> Message:
        """
        /// Returns the next `Message` from the internal buffer, filling the buffer previously if it's
        empty.

        Returns `None` if the `limit` is reached or there are no messages left.
        """
        ...
