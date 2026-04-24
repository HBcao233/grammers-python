from .tl import types
from .sessions import PeerIdLike

Phone = str
Username = str
InviteLink = str
InputPeerLike = Phone | Username | types.InputPeer | PeerIdLike

Message = types.MessageEmpty | types.Message | types.MessageService
MessageReplyHeader = types.MessageReplyHeader | types.MessageReplyStoryHeader
MessageMedia = (
    types.MessageMediaEmpty
    | types.MessageMediaPhoto
    | types.MessageMediaGeo
    | types.MessageMediaContact
    | types.MessageMediaUnsupported
    | types.MessageMediaDocument
    | types.MessageMediaWebPage
    | types.MessageMediaVenue
    | types.MessageMediaGame
    | types.MessageMediaInvoice
    | types.MessageMediaGeoLive
    | types.MessageMediaPoll
    | types.MessageMediaDice
    | types.MessageMediaStory
    | types.MessageMediaGiveaway
    | types.MessageMediaGiveawayResults
    | types.MessageMediaPaidMedia
    | types.MessageMediaToDo
)
ReplyMarkup = (
    types.ReplyKeyboardHide
    | types.ReplyKeyboardForceReply
    | types.ReplyKeyboardMarkup
    | types.ReplyInlineMarkup
)
MessageEntity = (
    types.MessageEntityUnknown
    | types.MessageEntityMention
    | types.MessageEntityHashtag
    | types.MessageEntityBotCommand
    | types.MessageEntityUrl
    | types.MessageEntityEmail
    | types.MessageEntityBold
    | types.MessageEntityItalic
    | types.MessageEntityCode
    | types.MessageEntityPre
    | types.MessageEntityTextUrl
    | types.MessageEntityMentionName
    | types.InputMessageEntityMentionName
    | types.MessageEntityPhone
    | types.MessageEntityCashtag
    | types.MessageEntityUnderline
    | types.MessageEntityStrike
    | types.MessageEntityBankCard
    | types.MessageEntitySpoiler
    | types.MessageEntityCustomEmoji
    | types.MessageEntityBlockquote
)
