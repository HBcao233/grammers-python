from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class PaymentForm(TLObject):
    """
    [Read `payments.paymentForm` docs](https://core.telegram.org/constructor/payments.paymentForm).

    Generated from the following TL definition:
    ```tl
    payments.paymentForm#a0058751 flags:# can_save_credentials:flags.2?true password_missing:flags.3?true form_id:long bot_id:long title:string description:string photo:flags.5?WebDocument invoice:Invoice provider_id:long url:string native_provider:flags.4?string native_params:flags.4?DataJSON additional_methods:flags.6?Vector<PaymentFormMethod> saved_info:flags.0?PaymentRequestedInfo saved_credentials:flags.1?Vector<PaymentSavedCredentials> users:Vector<User> = payments.PaymentForm
    ```
    """
    def __new__(
        cls,
        can_save_credentials: bool,
        password_missing: bool,
        form_id: int,
        bot_id: int,
        title: str,
        description: str,
        photo: Optional[types.WebDocument | types.WebDocumentNoProxy],
        invoice: types.Invoice,
        provider_id: int,
        url: str,
        native_provider: Optional[str],
        native_params: Optional[types.DataJson],
        additional_methods: Optional[Sequence[types.PaymentFormMethod]],
        saved_info: Optional[types.PaymentRequestedInfo],
        saved_credentials: Optional[Sequence[types.PaymentSavedCredentialsCard]],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaymentFormStars(TLObject):
    """
    [Read `payments.paymentFormStars` docs](https://core.telegram.org/constructor/payments.paymentFormStars).

    Generated from the following TL definition:
    ```tl
    payments.paymentFormStars#7bf6b15c flags:# form_id:long bot_id:long title:string description:string photo:flags.5?WebDocument invoice:Invoice users:Vector<User> = payments.PaymentForm
    ```
    """
    def __new__(
        cls,
        form_id: int,
        bot_id: int,
        title: str,
        description: str,
        photo: Optional[types.WebDocument | types.WebDocumentNoProxy],
        invoice: types.Invoice,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaymentFormStarGift(TLObject):
    """
    [Read `payments.paymentFormStarGift` docs](https://core.telegram.org/constructor/payments.paymentFormStarGift).

    Generated from the following TL definition:
    ```tl
    payments.paymentFormStarGift#b425cfe1 form_id:long invoice:Invoice = payments.PaymentForm
    ```
    """
    def __new__(
        cls,
        form_id: int,
        invoice: types.Invoice,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ValidatedRequestedInfo(TLObject):
    """
    [Read `payments.validatedRequestedInfo` docs](https://core.telegram.org/constructor/payments.validatedRequestedInfo).

    Generated from the following TL definition:
    ```tl
    payments.validatedRequestedInfo#d1451883 flags:# id:flags.0?string shipping_options:flags.1?Vector<ShippingOption> = payments.ValidatedRequestedInfo
    ```
    """
    def __new__(
        cls,
        id: Optional[str],
        shipping_options: Optional[Sequence[types.ShippingOption]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaymentResult(TLObject):
    """
    [Read `payments.paymentResult` docs](https://core.telegram.org/constructor/payments.paymentResult).

    Generated from the following TL definition:
    ```tl
    payments.paymentResult#4e5f810d updates:Updates = payments.PaymentResult
    ```
    """
    def __new__(
        cls,
        updates: types.UpdatesTooLong | types.UpdateShortMessage | types.UpdateShortChatMessage | types.UpdateShort | types.UpdatesCombined | types.Updates | types.UpdateShortSentMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaymentVerificationNeeded(TLObject):
    """
    [Read `payments.paymentVerificationNeeded` docs](https://core.telegram.org/constructor/payments.paymentVerificationNeeded).

    Generated from the following TL definition:
    ```tl
    payments.paymentVerificationNeeded#d8411139 url:string = payments.PaymentResult
    ```
    """
    def __new__(
        cls,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaymentReceipt(TLObject):
    """
    [Read `payments.paymentReceipt` docs](https://core.telegram.org/constructor/payments.paymentReceipt).

    Generated from the following TL definition:
    ```tl
    payments.paymentReceipt#70c4fe03 flags:# date:int bot_id:long provider_id:long title:string description:string photo:flags.2?WebDocument invoice:Invoice info:flags.0?PaymentRequestedInfo shipping:flags.1?ShippingOption tip_amount:flags.3?long currency:string total_amount:long credentials_title:string users:Vector<User> = payments.PaymentReceipt
    ```
    """
    def __new__(
        cls,
        date: int,
        bot_id: int,
        provider_id: int,
        title: str,
        description: str,
        photo: Optional[types.WebDocument | types.WebDocumentNoProxy],
        invoice: types.Invoice,
        info: Optional[types.PaymentRequestedInfo],
        shipping: Optional[types.ShippingOption],
        tip_amount: Optional[int],
        currency: str,
        total_amount: int,
        credentials_title: str,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PaymentReceiptStars(TLObject):
    """
    [Read `payments.paymentReceiptStars` docs](https://core.telegram.org/constructor/payments.paymentReceiptStars).

    Generated from the following TL definition:
    ```tl
    payments.paymentReceiptStars#dabbf83a flags:# date:int bot_id:long title:string description:string photo:flags.2?WebDocument invoice:Invoice currency:string total_amount:long transaction_id:string users:Vector<User> = payments.PaymentReceipt
    ```
    """
    def __new__(
        cls,
        date: int,
        bot_id: int,
        title: str,
        description: str,
        photo: Optional[types.WebDocument | types.WebDocumentNoProxy],
        invoice: types.Invoice,
        currency: str,
        total_amount: int,
        transaction_id: str,
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedInfo(TLObject):
    """
    [Read `payments.savedInfo` docs](https://core.telegram.org/constructor/payments.savedInfo).

    Generated from the following TL definition:
    ```tl
    payments.savedInfo#fb8fe43c flags:# has_saved_credentials:flags.1?true saved_info:flags.0?PaymentRequestedInfo = payments.SavedInfo
    ```
    """
    def __new__(
        cls,
        has_saved_credentials: bool,
        saved_info: Optional[types.PaymentRequestedInfo],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BankCardData(TLObject):
    """
    [Read `payments.bankCardData` docs](https://core.telegram.org/constructor/payments.bankCardData).

    Generated from the following TL definition:
    ```tl
    payments.bankCardData#3e24e573 title:string open_urls:Vector<BankCardOpenUrl> = payments.BankCardData
    ```
    """
    def __new__(
        cls,
        title: str,
        open_urls: Sequence[types.BankCardOpenUrl],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportedInvoice(TLObject):
    """
    [Read `payments.exportedInvoice` docs](https://core.telegram.org/constructor/payments.exportedInvoice).

    Generated from the following TL definition:
    ```tl
    payments.exportedInvoice#aed0cbd9 url:string = payments.ExportedInvoice
    ```
    """
    def __new__(
        cls,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckedGiftCode(TLObject):
    """
    [Read `payments.checkedGiftCode` docs](https://core.telegram.org/constructor/payments.checkedGiftCode).

    Generated from the following TL definition:
    ```tl
    payments.checkedGiftCode#eb983f8f flags:# via_giveaway:flags.2?true from_id:flags.4?Peer giveaway_msg_id:flags.3?int to_id:flags.0?long date:int days:int used_date:flags.1?int chats:Vector<Chat> users:Vector<User> = payments.CheckedGiftCode
    ```
    """
    def __new__(
        cls,
        via_giveaway: bool,
        from_id: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        giveaway_msg_id: Optional[int],
        to_id: Optional[int],
        date: int,
        days: int,
        used_date: Optional[int],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GiveawayInfo(TLObject):
    """
    [Read `payments.giveawayInfo` docs](https://core.telegram.org/constructor/payments.giveawayInfo).

    Generated from the following TL definition:
    ```tl
    payments.giveawayInfo#4367daa0 flags:# participating:flags.0?true preparing_results:flags.3?true start_date:int joined_too_early_date:flags.1?int admin_disallowed_chat_id:flags.2?long disallowed_country:flags.4?string = payments.GiveawayInfo
    ```
    """
    def __new__(
        cls,
        participating: bool,
        preparing_results: bool,
        start_date: int,
        joined_too_early_date: Optional[int],
        admin_disallowed_chat_id: Optional[int],
        disallowed_country: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GiveawayInfoResults(TLObject):
    """
    [Read `payments.giveawayInfoResults` docs](https://core.telegram.org/constructor/payments.giveawayInfoResults).

    Generated from the following TL definition:
    ```tl
    payments.giveawayInfoResults#e175e66f flags:# winner:flags.0?true refunded:flags.1?true start_date:int gift_code_slug:flags.3?string stars_prize:flags.4?long finish_date:int winners_count:int activated_count:flags.2?int = payments.GiveawayInfo
    ```
    """
    def __new__(
        cls,
        winner: bool,
        refunded: bool,
        start_date: int,
        gift_code_slug: Optional[str],
        stars_prize: Optional[int],
        finish_date: int,
        winners_count: int,
        activated_count: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsStatus(TLObject):
    """
    [Read `payments.starsStatus` docs](https://core.telegram.org/constructor/payments.starsStatus).

    Generated from the following TL definition:
    ```tl
    payments.starsStatus#6c9ce8ed flags:# balance:StarsAmount subscriptions:flags.1?Vector<StarsSubscription> subscriptions_next_offset:flags.2?string subscriptions_missing_balance:flags.4?long history:flags.3?Vector<StarsTransaction> next_offset:flags.0?string chats:Vector<Chat> users:Vector<User> = payments.StarsStatus
    ```
    """
    def __new__(
        cls,
        balance: types.StarsAmount | types.StarsTonAmount,
        subscriptions: Optional[Sequence[types.StarsSubscription]],
        subscriptions_next_offset: Optional[str],
        subscriptions_missing_balance: Optional[int],
        history: Optional[Sequence[types.StarsTransaction]],
        next_offset: Optional[str],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsRevenueStats(TLObject):
    """
    [Read `payments.starsRevenueStats` docs](https://core.telegram.org/constructor/payments.starsRevenueStats).

    Generated from the following TL definition:
    ```tl
    payments.starsRevenueStats#6c207376 flags:# top_hours_graph:flags.0?StatsGraph revenue_graph:StatsGraph status:StarsRevenueStatus usd_rate:double = payments.StarsRevenueStats
    ```
    """
    def __new__(
        cls,
        top_hours_graph: Optional[types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph],
        revenue_graph: types.StatsGraphAsync | types.StatsGraphError | types.StatsGraph,
        status: types.StarsRevenueStatus,
        usd_rate: float,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsRevenueWithdrawalUrl(TLObject):
    """
    [Read `payments.starsRevenueWithdrawalUrl` docs](https://core.telegram.org/constructor/payments.starsRevenueWithdrawalUrl).

    Generated from the following TL definition:
    ```tl
    payments.starsRevenueWithdrawalUrl#1dab80b7 url:string = payments.StarsRevenueWithdrawalUrl
    ```
    """
    def __new__(
        cls,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarsRevenueAdsAccountUrl(TLObject):
    """
    [Read `payments.starsRevenueAdsAccountUrl` docs](https://core.telegram.org/constructor/payments.starsRevenueAdsAccountUrl).

    Generated from the following TL definition:
    ```tl
    payments.starsRevenueAdsAccountUrl#394e7f21 url:string = payments.StarsRevenueAdsAccountUrl
    ```
    """
    def __new__(
        cls,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftsNotModified(TLObject):
    """
    [Read `payments.starGiftsNotModified` docs](https://core.telegram.org/constructor/payments.starGiftsNotModified).

    Generated from the following TL definition:
    ```tl
    payments.starGiftsNotModified#a388a368 = payments.StarGifts
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGifts(TLObject):
    """
    [Read `payments.starGifts` docs](https://core.telegram.org/constructor/payments.starGifts).

    Generated from the following TL definition:
    ```tl
    payments.starGifts#2ed82995 hash:int gifts:Vector<StarGift> chats:Vector<Chat> users:Vector<User> = payments.StarGifts
    ```
    """
    def __new__(
        cls,
        hash: int,
        gifts: Sequence[types.StarGift | types.StarGiftUnique],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ConnectedStarRefBots(TLObject):
    """
    [Read `payments.connectedStarRefBots` docs](https://core.telegram.org/constructor/payments.connectedStarRefBots).

    Generated from the following TL definition:
    ```tl
    payments.connectedStarRefBots#98d5ea1d count:int connected_bots:Vector<ConnectedBotStarRef> users:Vector<User> = payments.ConnectedStarRefBots
    ```
    """
    def __new__(
        cls,
        count: int,
        connected_bots: Sequence[types.ConnectedBotStarRef],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SuggestedStarRefBots(TLObject):
    """
    [Read `payments.suggestedStarRefBots` docs](https://core.telegram.org/constructor/payments.suggestedStarRefBots).

    Generated from the following TL definition:
    ```tl
    payments.suggestedStarRefBots#b4d5d859 flags:# count:int suggested_bots:Vector<StarRefProgram> users:Vector<User> next_offset:flags.0?string = payments.SuggestedStarRefBots
    ```
    """
    def __new__(
        cls,
        count: int,
        suggested_bots: Sequence[types.StarRefProgram],
        users: Sequence[types.UserEmpty | types.User],
        next_offset: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftUpgradePreview(TLObject):
    """
    [Read `payments.starGiftUpgradePreview` docs](https://core.telegram.org/constructor/payments.starGiftUpgradePreview).

    Generated from the following TL definition:
    ```tl
    payments.starGiftUpgradePreview#3de1dfed sample_attributes:Vector<StarGiftAttribute> prices:Vector<StarGiftUpgradePrice> next_prices:Vector<StarGiftUpgradePrice> = payments.StarGiftUpgradePreview
    ```
    """
    def __new__(
        cls,
        sample_attributes: Sequence[types.StarGiftAttributeModel | types.StarGiftAttributePattern | types.StarGiftAttributeBackdrop | types.StarGiftAttributeOriginalDetails],
        prices: Sequence[types.StarGiftUpgradePrice],
        next_prices: Sequence[types.StarGiftUpgradePrice],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UniqueStarGift(TLObject):
    """
    [Read `payments.uniqueStarGift` docs](https://core.telegram.org/constructor/payments.uniqueStarGift).

    Generated from the following TL definition:
    ```tl
    payments.uniqueStarGift#416c56e8 gift:StarGift chats:Vector<Chat> users:Vector<User> = payments.UniqueStarGift
    ```
    """
    def __new__(
        cls,
        gift: types.StarGift | types.StarGiftUnique,
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SavedStarGifts(TLObject):
    """
    [Read `payments.savedStarGifts` docs](https://core.telegram.org/constructor/payments.savedStarGifts).

    Generated from the following TL definition:
    ```tl
    payments.savedStarGifts#95f389b1 flags:# count:int chat_notifications_enabled:flags.1?Bool gifts:Vector<SavedStarGift> next_offset:flags.0?string chats:Vector<Chat> users:Vector<User> = payments.SavedStarGifts
    ```
    """
    def __new__(
        cls,
        count: int,
        chat_notifications_enabled: Optional[bool],
        gifts: Sequence[types.SavedStarGift],
        next_offset: Optional[str],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftWithdrawalUrl(TLObject):
    """
    [Read `payments.starGiftWithdrawalUrl` docs](https://core.telegram.org/constructor/payments.starGiftWithdrawalUrl).

    Generated from the following TL definition:
    ```tl
    payments.starGiftWithdrawalUrl#84aa3a9c url:string = payments.StarGiftWithdrawalUrl
    ```
    """
    def __new__(
        cls,
        url: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResaleStarGifts(TLObject):
    """
    [Read `payments.resaleStarGifts` docs](https://core.telegram.org/constructor/payments.resaleStarGifts).

    Generated from the following TL definition:
    ```tl
    payments.resaleStarGifts#947a12df flags:# count:int gifts:Vector<StarGift> next_offset:flags.0?string attributes:flags.1?Vector<StarGiftAttribute> attributes_hash:flags.1?long chats:Vector<Chat> counters:flags.2?Vector<StarGiftAttributeCounter> users:Vector<User> = payments.ResaleStarGifts
    ```
    """
    def __new__(
        cls,
        count: int,
        gifts: Sequence[types.StarGift | types.StarGiftUnique],
        next_offset: Optional[str],
        attributes: Optional[Sequence[types.StarGiftAttributeModel | types.StarGiftAttributePattern | types.StarGiftAttributeBackdrop | types.StarGiftAttributeOriginalDetails]],
        attributes_hash: Optional[int],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        counters: Optional[Sequence[types.StarGiftAttributeCounter]],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftCollectionsNotModified(TLObject):
    """
    [Read `payments.starGiftCollectionsNotModified` docs](https://core.telegram.org/constructor/payments.starGiftCollectionsNotModified).

    Generated from the following TL definition:
    ```tl
    payments.starGiftCollectionsNotModified#a0ba4f17 = payments.StarGiftCollections
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftCollections(TLObject):
    """
    [Read `payments.starGiftCollections` docs](https://core.telegram.org/constructor/payments.starGiftCollections).

    Generated from the following TL definition:
    ```tl
    payments.starGiftCollections#8a2932f3 collections:Vector<StarGiftCollection> = payments.StarGiftCollections
    ```
    """
    def __new__(
        cls,
        collections: Sequence[types.StarGiftCollection],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UniqueStarGiftValueInfo(TLObject):
    """
    [Read `payments.uniqueStarGiftValueInfo` docs](https://core.telegram.org/constructor/payments.uniqueStarGiftValueInfo).

    Generated from the following TL definition:
    ```tl
    payments.uniqueStarGiftValueInfo#512fe446 flags:# last_sale_on_fragment:flags.1?true value_is_average:flags.6?true currency:string value:long initial_sale_date:int initial_sale_stars:long initial_sale_price:long last_sale_date:flags.0?int last_sale_price:flags.0?long floor_price:flags.2?long average_price:flags.3?long listed_count:flags.4?int fragment_listed_count:flags.5?int fragment_listed_url:flags.5?string = payments.UniqueStarGiftValueInfo
    ```
    """
    def __new__(
        cls,
        last_sale_on_fragment: bool,
        value_is_average: bool,
        currency: str,
        value: int,
        initial_sale_date: int,
        initial_sale_stars: int,
        initial_sale_price: int,
        last_sale_date: Optional[int],
        last_sale_price: Optional[int],
        floor_price: Optional[int],
        average_price: Optional[int],
        listed_count: Optional[int],
        fragment_listed_count: Optional[int],
        fragment_listed_url: Optional[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckCanSendGiftResultOk(TLObject):
    """
    [Read `payments.checkCanSendGiftResultOk` docs](https://core.telegram.org/constructor/payments.checkCanSendGiftResultOk).

    Generated from the following TL definition:
    ```tl
    payments.checkCanSendGiftResultOk#374fa7ad = payments.CheckCanSendGiftResult
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckCanSendGiftResultFail(TLObject):
    """
    [Read `payments.checkCanSendGiftResultFail` docs](https://core.telegram.org/constructor/payments.checkCanSendGiftResultFail).

    Generated from the following TL definition:
    ```tl
    payments.checkCanSendGiftResultFail#d5e58274 reason:TextWithEntities = payments.CheckCanSendGiftResult
    ```
    """
    def __new__(
        cls,
        reason: types.TextWithEntities,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAuctionState(TLObject):
    """
    [Read `payments.starGiftAuctionState` docs](https://core.telegram.org/constructor/payments.starGiftAuctionState).

    Generated from the following TL definition:
    ```tl
    payments.starGiftAuctionState#6b39f4ec gift:StarGift state:StarGiftAuctionState user_state:StarGiftAuctionUserState timeout:int users:Vector<User> chats:Vector<Chat> = payments.StarGiftAuctionState
    ```
    """
    def __new__(
        cls,
        gift: types.StarGift | types.StarGiftUnique,
        state: types.StarGiftAuctionStateNotModified | types.StarGiftAuctionState | types.StarGiftAuctionStateFinished,
        user_state: types.StarGiftAuctionUserState,
        timeout: int,
        users: Sequence[types.UserEmpty | types.User],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftAuctionAcquiredGifts(TLObject):
    """
    [Read `payments.starGiftAuctionAcquiredGifts` docs](https://core.telegram.org/constructor/payments.starGiftAuctionAcquiredGifts).

    Generated from the following TL definition:
    ```tl
    payments.starGiftAuctionAcquiredGifts#7d5bd1f0 gifts:Vector<StarGiftAuctionAcquiredGift> users:Vector<User> chats:Vector<Chat> = payments.StarGiftAuctionAcquiredGifts
    ```
    """
    def __new__(
        cls,
        gifts: Sequence[types.StarGiftAuctionAcquiredGift],
        users: Sequence[types.UserEmpty | types.User],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftActiveAuctionsNotModified(TLObject):
    """
    [Read `payments.starGiftActiveAuctionsNotModified` docs](https://core.telegram.org/constructor/payments.starGiftActiveAuctionsNotModified).

    Generated from the following TL definition:
    ```tl
    payments.starGiftActiveAuctionsNotModified#db33dad0 = payments.StarGiftActiveAuctions
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftActiveAuctions(TLObject):
    """
    [Read `payments.starGiftActiveAuctions` docs](https://core.telegram.org/constructor/payments.starGiftActiveAuctions).

    Generated from the following TL definition:
    ```tl
    payments.starGiftActiveAuctions#aef6abbc auctions:Vector<StarGiftActiveAuctionState> users:Vector<User> chats:Vector<Chat> = payments.StarGiftActiveAuctions
    ```
    """
    def __new__(
        cls,
        auctions: Sequence[types.StarGiftActiveAuctionState],
        users: Sequence[types.UserEmpty | types.User],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class StarGiftUpgradeAttributes(TLObject):
    """
    [Read `payments.starGiftUpgradeAttributes` docs](https://core.telegram.org/constructor/payments.starGiftUpgradeAttributes).

    Generated from the following TL definition:
    ```tl
    payments.starGiftUpgradeAttributes#46c6e36f attributes:Vector<StarGiftAttribute> = payments.StarGiftUpgradeAttributes
    ```
    """
    def __new__(
        cls,
        attributes: Sequence[types.StarGiftAttributeModel | types.StarGiftAttributePattern | types.StarGiftAttributeBackdrop | types.StarGiftAttributeOriginalDetails],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

