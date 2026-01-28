from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class GetPaymentForm(TLRequest):
    """
    [Read `payments.getPaymentForm` docs](https://core.telegram.org/method/payments.getPaymentForm).

    Generated from the following TL definition:
    ```tl
    payments.getPaymentForm#37148dbb flags:# invoice:InputInvoice theme_params:flags.0?DataJSON = payments.PaymentForm
    ```
    """
    def __new__(
        cls,
        invoice: types.InputInvoiceMessage | types.InputInvoiceSlug | types.InputInvoicePremiumGiftCode | types.InputInvoiceStars | types.InputInvoiceChatInviteSubscription | types.InputInvoiceStarGift | types.InputInvoiceStarGiftUpgrade | types.InputInvoiceStarGiftTransfer | types.InputInvoicePremiumGiftStars | types.InputInvoiceBusinessBotTransferStars | types.InputInvoiceStarGiftResale | types.InputInvoiceStarGiftPrepaidUpgrade | types.InputInvoicePremiumAuthCode | types.InputInvoiceStarGiftDropOriginalDetails | types.InputInvoiceStarGiftAuctionBid,
        theme_params: Optional[types.DataJson],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPaymentReceipt(TLRequest):
    """
    [Read `payments.getPaymentReceipt` docs](https://core.telegram.org/method/payments.getPaymentReceipt).

    Generated from the following TL definition:
    ```tl
    payments.getPaymentReceipt#2478d1cc peer:InputPeer msg_id:int = payments.PaymentReceipt
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ValidateRequestedInfo(TLRequest):
    """
    [Read `payments.validateRequestedInfo` docs](https://core.telegram.org/method/payments.validateRequestedInfo).

    Generated from the following TL definition:
    ```tl
    payments.validateRequestedInfo#b6c8f12b flags:# save:flags.0?true invoice:InputInvoice info:PaymentRequestedInfo = payments.ValidatedRequestedInfo
    ```
    """
    def __new__(
        cls,
        save: bool,
        invoice: types.InputInvoiceMessage | types.InputInvoiceSlug | types.InputInvoicePremiumGiftCode | types.InputInvoiceStars | types.InputInvoiceChatInviteSubscription | types.InputInvoiceStarGift | types.InputInvoiceStarGiftUpgrade | types.InputInvoiceStarGiftTransfer | types.InputInvoicePremiumGiftStars | types.InputInvoiceBusinessBotTransferStars | types.InputInvoiceStarGiftResale | types.InputInvoiceStarGiftPrepaidUpgrade | types.InputInvoicePremiumAuthCode | types.InputInvoiceStarGiftDropOriginalDetails | types.InputInvoiceStarGiftAuctionBid,
        info: types.PaymentRequestedInfo,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendPaymentForm(TLRequest):
    """
    [Read `payments.sendPaymentForm` docs](https://core.telegram.org/method/payments.sendPaymentForm).

    Generated from the following TL definition:
    ```tl
    payments.sendPaymentForm#2d03522f flags:# form_id:long invoice:InputInvoice requested_info_id:flags.0?string shipping_option_id:flags.1?string credentials:InputPaymentCredentials tip_amount:flags.2?long = payments.PaymentResult
    ```
    """
    def __new__(
        cls,
        form_id: int,
        invoice: types.InputInvoiceMessage | types.InputInvoiceSlug | types.InputInvoicePremiumGiftCode | types.InputInvoiceStars | types.InputInvoiceChatInviteSubscription | types.InputInvoiceStarGift | types.InputInvoiceStarGiftUpgrade | types.InputInvoiceStarGiftTransfer | types.InputInvoicePremiumGiftStars | types.InputInvoiceBusinessBotTransferStars | types.InputInvoiceStarGiftResale | types.InputInvoiceStarGiftPrepaidUpgrade | types.InputInvoicePremiumAuthCode | types.InputInvoiceStarGiftDropOriginalDetails | types.InputInvoiceStarGiftAuctionBid,
        requested_info_id: Optional[str],
        shipping_option_id: Optional[str],
        credentials: types.InputPaymentCredentialsSaved | types.InputPaymentCredentials | types.InputPaymentCredentialsApplePay | types.InputPaymentCredentialsGooglePay,
        tip_amount: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSavedInfo(TLRequest):
    """
    [Read `payments.getSavedInfo` docs](https://core.telegram.org/method/payments.getSavedInfo).

    Generated from the following TL definition:
    ```tl
    payments.getSavedInfo#227d824b = payments.SavedInfo
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ClearSavedInfo(TLRequest):
    """
    [Read `payments.clearSavedInfo` docs](https://core.telegram.org/method/payments.clearSavedInfo).

    Generated from the following TL definition:
    ```tl
    payments.clearSavedInfo#d83d70c1 flags:# credentials:flags.0?true info:flags.1?true = Bool
    ```
    """
    def __new__(
        cls,
        credentials: bool,
        info: bool,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetBankCardData(TLRequest):
    """
    [Read `payments.getBankCardData` docs](https://core.telegram.org/method/payments.getBankCardData).

    Generated from the following TL definition:
    ```tl
    payments.getBankCardData#2e79d779 number:string = payments.BankCardData
    ```
    """
    def __new__(
        cls,
        number: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ExportInvoice(TLRequest):
    """
    [Read `payments.exportInvoice` docs](https://core.telegram.org/method/payments.exportInvoice).

    Generated from the following TL definition:
    ```tl
    payments.exportInvoice#f91b065 invoice_media:InputMedia = payments.ExportedInvoice
    ```
    """
    def __new__(
        cls,
        invoice_media: types.InputMediaEmpty | types.InputMediaUploadedPhoto | types.InputMediaPhoto | types.InputMediaGeoPoint | types.InputMediaContact | types.InputMediaUploadedDocument | types.InputMediaDocument | types.InputMediaVenue | types.InputMediaPhotoExternal | types.InputMediaDocumentExternal | types.InputMediaGame | types.InputMediaInvoice | types.InputMediaGeoLive | types.InputMediaPoll | types.InputMediaDice | types.InputMediaStory | types.InputMediaWebPage | types.InputMediaPaidMedia | types.InputMediaTodo | types.InputMediaStakeDice,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AssignAppStoreTransaction(TLRequest):
    """
    [Read `payments.assignAppStoreTransaction` docs](https://core.telegram.org/method/payments.assignAppStoreTransaction).

    Generated from the following TL definition:
    ```tl
    payments.assignAppStoreTransaction#80ed747d receipt:bytes purpose:InputStorePaymentPurpose = Updates
    ```
    """
    def __new__(
        cls,
        receipt: bytes,
        purpose: types.InputStorePaymentPremiumSubscription | types.InputStorePaymentGiftPremium | types.InputStorePaymentPremiumGiftCode | types.InputStorePaymentPremiumGiveaway | types.InputStorePaymentStarsTopup | types.InputStorePaymentStarsGift | types.InputStorePaymentStarsGiveaway | types.InputStorePaymentAuthCode,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AssignPlayMarketTransaction(TLRequest):
    """
    [Read `payments.assignPlayMarketTransaction` docs](https://core.telegram.org/method/payments.assignPlayMarketTransaction).

    Generated from the following TL definition:
    ```tl
    payments.assignPlayMarketTransaction#dffd50d3 receipt:DataJSON purpose:InputStorePaymentPurpose = Updates
    ```
    """
    def __new__(
        cls,
        receipt: types.DataJson,
        purpose: types.InputStorePaymentPremiumSubscription | types.InputStorePaymentGiftPremium | types.InputStorePaymentPremiumGiftCode | types.InputStorePaymentPremiumGiveaway | types.InputStorePaymentStarsTopup | types.InputStorePaymentStarsGift | types.InputStorePaymentStarsGiveaway | types.InputStorePaymentAuthCode,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPremiumGiftCodeOptions(TLRequest):
    """
    [Read `payments.getPremiumGiftCodeOptions` docs](https://core.telegram.org/method/payments.getPremiumGiftCodeOptions).

    Generated from the following TL definition:
    ```tl
    payments.getPremiumGiftCodeOptions#2757ba54 flags:# boost_peer:flags.0?InputPeer = Vector<PremiumGiftCodeOption>
    ```
    """
    def __new__(
        cls,
        boost_peer: Optional[types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckGiftCode(TLRequest):
    """
    [Read `payments.checkGiftCode` docs](https://core.telegram.org/method/payments.checkGiftCode).

    Generated from the following TL definition:
    ```tl
    payments.checkGiftCode#8e51b4c1 slug:string = payments.CheckedGiftCode
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ApplyGiftCode(TLRequest):
    """
    [Read `payments.applyGiftCode` docs](https://core.telegram.org/method/payments.applyGiftCode).

    Generated from the following TL definition:
    ```tl
    payments.applyGiftCode#f6e26854 slug:string = Updates
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetGiveawayInfo(TLRequest):
    """
    [Read `payments.getGiveawayInfo` docs](https://core.telegram.org/method/payments.getGiveawayInfo).

    Generated from the following TL definition:
    ```tl
    payments.getGiveawayInfo#f4239425 peer:InputPeer msg_id:int = payments.GiveawayInfo
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class LaunchPrepaidGiveaway(TLRequest):
    """
    [Read `payments.launchPrepaidGiveaway` docs](https://core.telegram.org/method/payments.launchPrepaidGiveaway).

    Generated from the following TL definition:
    ```tl
    payments.launchPrepaidGiveaway#5ff58f20 peer:InputPeer giveaway_id:long purpose:InputStorePaymentPurpose = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        giveaway_id: int,
        purpose: types.InputStorePaymentPremiumSubscription | types.InputStorePaymentGiftPremium | types.InputStorePaymentPremiumGiftCode | types.InputStorePaymentPremiumGiveaway | types.InputStorePaymentStarsTopup | types.InputStorePaymentStarsGift | types.InputStorePaymentStarsGiveaway | types.InputStorePaymentAuthCode,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarsTopupOptions(TLRequest):
    """
    [Read `payments.getStarsTopupOptions` docs](https://core.telegram.org/method/payments.getStarsTopupOptions).

    Generated from the following TL definition:
    ```tl
    payments.getStarsTopupOptions#c00ec7d3 = Vector<StarsTopupOption>
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarsStatus(TLRequest):
    """
    [Read `payments.getStarsStatus` docs](https://core.telegram.org/method/payments.getStarsStatus).

    Generated from the following TL definition:
    ```tl
    payments.getStarsStatus#4ea9b3bf flags:# ton:flags.0?true peer:InputPeer = payments.StarsStatus
    ```
    """
    def __new__(
        cls,
        ton: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarsTransactions(TLRequest):
    """
    [Read `payments.getStarsTransactions` docs](https://core.telegram.org/method/payments.getStarsTransactions).

    Generated from the following TL definition:
    ```tl
    payments.getStarsTransactions#69da4557 flags:# inbound:flags.0?true outbound:flags.1?true ascending:flags.2?true ton:flags.4?true subscription_id:flags.3?string peer:InputPeer offset:string limit:int = payments.StarsStatus
    ```
    """
    def __new__(
        cls,
        inbound: bool,
        outbound: bool,
        ascending: bool,
        ton: bool,
        subscription_id: Optional[str],
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        offset: str,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendStarsForm(TLRequest):
    """
    [Read `payments.sendStarsForm` docs](https://core.telegram.org/method/payments.sendStarsForm).

    Generated from the following TL definition:
    ```tl
    payments.sendStarsForm#7998c914 form_id:long invoice:InputInvoice = payments.PaymentResult
    ```
    """
    def __new__(
        cls,
        form_id: int,
        invoice: types.InputInvoiceMessage | types.InputInvoiceSlug | types.InputInvoicePremiumGiftCode | types.InputInvoiceStars | types.InputInvoiceChatInviteSubscription | types.InputInvoiceStarGift | types.InputInvoiceStarGiftUpgrade | types.InputInvoiceStarGiftTransfer | types.InputInvoicePremiumGiftStars | types.InputInvoiceBusinessBotTransferStars | types.InputInvoiceStarGiftResale | types.InputInvoiceStarGiftPrepaidUpgrade | types.InputInvoicePremiumAuthCode | types.InputInvoiceStarGiftDropOriginalDetails | types.InputInvoiceStarGiftAuctionBid,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RefundStarsCharge(TLRequest):
    """
    [Read `payments.refundStarsCharge` docs](https://core.telegram.org/method/payments.refundStarsCharge).

    Generated from the following TL definition:
    ```tl
    payments.refundStarsCharge#25ae8f4a user_id:InputUser charge_id:string = Updates
    ```
    """
    def __new__(
        cls,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        charge_id: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarsRevenueStats(TLRequest):
    """
    [Read `payments.getStarsRevenueStats` docs](https://core.telegram.org/method/payments.getStarsRevenueStats).

    Generated from the following TL definition:
    ```tl
    payments.getStarsRevenueStats#d91ffad6 flags:# dark:flags.0?true ton:flags.1?true peer:InputPeer = payments.StarsRevenueStats
    ```
    """
    def __new__(
        cls,
        dark: bool,
        ton: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarsRevenueWithdrawalUrl(TLRequest):
    """
    [Read `payments.getStarsRevenueWithdrawalUrl` docs](https://core.telegram.org/method/payments.getStarsRevenueWithdrawalUrl).

    Generated from the following TL definition:
    ```tl
    payments.getStarsRevenueWithdrawalUrl#2433dc92 flags:# ton:flags.0?true peer:InputPeer amount:flags.1?long password:InputCheckPasswordSRP = payments.StarsRevenueWithdrawalUrl
    ```
    """
    def __new__(
        cls,
        ton: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        amount: Optional[int],
        password: types.InputCheckPasswordEmpty | types.InputCheckPasswordSrp,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarsRevenueAdsAccountUrl(TLRequest):
    """
    [Read `payments.getStarsRevenueAdsAccountUrl` docs](https://core.telegram.org/method/payments.getStarsRevenueAdsAccountUrl).

    Generated from the following TL definition:
    ```tl
    payments.getStarsRevenueAdsAccountUrl#d1d7efc5 peer:InputPeer = payments.StarsRevenueAdsAccountUrl
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarsTransactionsById(TLRequest):
    """
    [Read `payments.getStarsTransactionsByID` docs](https://core.telegram.org/method/payments.getStarsTransactionsByID).

    Generated from the following TL definition:
    ```tl
    payments.getStarsTransactionsByID#2dca16b8 flags:# ton:flags.0?true peer:InputPeer id:Vector<InputStarsTransaction> = payments.StarsStatus
    ```
    """
    def __new__(
        cls,
        ton: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        id: Sequence[types.InputStarsTransaction],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarsGiftOptions(TLRequest):
    """
    [Read `payments.getStarsGiftOptions` docs](https://core.telegram.org/method/payments.getStarsGiftOptions).

    Generated from the following TL definition:
    ```tl
    payments.getStarsGiftOptions#d3c96bc8 flags:# user_id:flags.0?InputUser = Vector<StarsGiftOption>
    ```
    """
    def __new__(
        cls,
        user_id: Optional[types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarsSubscriptions(TLRequest):
    """
    [Read `payments.getStarsSubscriptions` docs](https://core.telegram.org/method/payments.getStarsSubscriptions).

    Generated from the following TL definition:
    ```tl
    payments.getStarsSubscriptions#32512c5 flags:# missing_balance:flags.0?true peer:InputPeer offset:string = payments.StarsStatus
    ```
    """
    def __new__(
        cls,
        missing_balance: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        offset: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ChangeStarsSubscription(TLRequest):
    """
    [Read `payments.changeStarsSubscription` docs](https://core.telegram.org/method/payments.changeStarsSubscription).

    Generated from the following TL definition:
    ```tl
    payments.changeStarsSubscription#c7770878 flags:# peer:InputPeer subscription_id:string canceled:flags.0?Bool = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        subscription_id: str,
        canceled: Optional[bool],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class FulfillStarsSubscription(TLRequest):
    """
    [Read `payments.fulfillStarsSubscription` docs](https://core.telegram.org/method/payments.fulfillStarsSubscription).

    Generated from the following TL definition:
    ```tl
    payments.fulfillStarsSubscription#cc5bebb3 peer:InputPeer subscription_id:string = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        subscription_id: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarsGiveawayOptions(TLRequest):
    """
    [Read `payments.getStarsGiveawayOptions` docs](https://core.telegram.org/method/payments.getStarsGiveawayOptions).

    Generated from the following TL definition:
    ```tl
    payments.getStarsGiveawayOptions#bd1efd3e = Vector<StarsGiveawayOption>
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarGifts(TLRequest):
    """
    [Read `payments.getStarGifts` docs](https://core.telegram.org/method/payments.getStarGifts).

    Generated from the following TL definition:
    ```tl
    payments.getStarGifts#c4563590 hash:int = payments.StarGifts
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveStarGift(TLRequest):
    """
    [Read `payments.saveStarGift` docs](https://core.telegram.org/method/payments.saveStarGift).

    Generated from the following TL definition:
    ```tl
    payments.saveStarGift#2a2a697c flags:# unsave:flags.0?true stargift:InputSavedStarGift = Bool
    ```
    """
    def __new__(
        cls,
        unsave: bool,
        stargift: types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ConvertStarGift(TLRequest):
    """
    [Read `payments.convertStarGift` docs](https://core.telegram.org/method/payments.convertStarGift).

    Generated from the following TL definition:
    ```tl
    payments.convertStarGift#74bf076b stargift:InputSavedStarGift = Bool
    ```
    """
    def __new__(
        cls,
        stargift: types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class BotCancelStarsSubscription(TLRequest):
    """
    [Read `payments.botCancelStarsSubscription` docs](https://core.telegram.org/method/payments.botCancelStarsSubscription).

    Generated from the following TL definition:
    ```tl
    payments.botCancelStarsSubscription#6dfa0622 flags:# restore:flags.0?true user_id:InputUser charge_id:string = Bool
    ```
    """
    def __new__(
        cls,
        restore: bool,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        charge_id: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetConnectedStarRefBots(TLRequest):
    """
    [Read `payments.getConnectedStarRefBots` docs](https://core.telegram.org/method/payments.getConnectedStarRefBots).

    Generated from the following TL definition:
    ```tl
    payments.getConnectedStarRefBots#5869a553 flags:# peer:InputPeer offset_date:flags.2?int offset_link:flags.2?string limit:int = payments.ConnectedStarRefBots
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        offset_date: Optional[int],
        offset_link: Optional[str],
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetConnectedStarRefBot(TLRequest):
    """
    [Read `payments.getConnectedStarRefBot` docs](https://core.telegram.org/method/payments.getConnectedStarRefBot).

    Generated from the following TL definition:
    ```tl
    payments.getConnectedStarRefBot#b7d998f0 peer:InputPeer bot:InputUser = payments.ConnectedStarRefBots
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSuggestedStarRefBots(TLRequest):
    """
    [Read `payments.getSuggestedStarRefBots` docs](https://core.telegram.org/method/payments.getSuggestedStarRefBots).

    Generated from the following TL definition:
    ```tl
    payments.getSuggestedStarRefBots#d6b48f7 flags:# order_by_revenue:flags.0?true order_by_date:flags.1?true peer:InputPeer offset:string limit:int = payments.SuggestedStarRefBots
    ```
    """
    def __new__(
        cls,
        order_by_revenue: bool,
        order_by_date: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        offset: str,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ConnectStarRefBot(TLRequest):
    """
    [Read `payments.connectStarRefBot` docs](https://core.telegram.org/method/payments.connectStarRefBot).

    Generated from the following TL definition:
    ```tl
    payments.connectStarRefBot#7ed5348a peer:InputPeer bot:InputUser = payments.ConnectedStarRefBots
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        bot: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditConnectedStarRefBot(TLRequest):
    """
    [Read `payments.editConnectedStarRefBot` docs](https://core.telegram.org/method/payments.editConnectedStarRefBot).

    Generated from the following TL definition:
    ```tl
    payments.editConnectedStarRefBot#e4fca4a3 flags:# revoked:flags.0?true peer:InputPeer link:string = payments.ConnectedStarRefBots
    ```
    """
    def __new__(
        cls,
        revoked: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        link: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarGiftUpgradePreview(TLRequest):
    """
    [Read `payments.getStarGiftUpgradePreview` docs](https://core.telegram.org/method/payments.getStarGiftUpgradePreview).

    Generated from the following TL definition:
    ```tl
    payments.getStarGiftUpgradePreview#9c9abcb1 gift_id:long = payments.StarGiftUpgradePreview
    ```
    """
    def __new__(
        cls,
        gift_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpgradeStarGift(TLRequest):
    """
    [Read `payments.upgradeStarGift` docs](https://core.telegram.org/method/payments.upgradeStarGift).

    Generated from the following TL definition:
    ```tl
    payments.upgradeStarGift#aed6e4f5 flags:# keep_original_details:flags.0?true stargift:InputSavedStarGift = Updates
    ```
    """
    def __new__(
        cls,
        keep_original_details: bool,
        stargift: types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TransferStarGift(TLRequest):
    """
    [Read `payments.transferStarGift` docs](https://core.telegram.org/method/payments.transferStarGift).

    Generated from the following TL definition:
    ```tl
    payments.transferStarGift#7f18176a stargift:InputSavedStarGift to_id:InputPeer = Updates
    ```
    """
    def __new__(
        cls,
        stargift: types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug,
        to_id: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetUniqueStarGift(TLRequest):
    """
    [Read `payments.getUniqueStarGift` docs](https://core.telegram.org/method/payments.getUniqueStarGift).

    Generated from the following TL definition:
    ```tl
    payments.getUniqueStarGift#a1974d72 slug:string = payments.UniqueStarGift
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSavedStarGifts(TLRequest):
    """
    [Read `payments.getSavedStarGifts` docs](https://core.telegram.org/method/payments.getSavedStarGifts).

    Generated from the following TL definition:
    ```tl
    payments.getSavedStarGifts#a319e569 flags:# exclude_unsaved:flags.0?true exclude_saved:flags.1?true exclude_unlimited:flags.2?true exclude_unique:flags.4?true sort_by_value:flags.5?true exclude_upgradable:flags.7?true exclude_unupgradable:flags.8?true peer_color_available:flags.9?true exclude_hosted:flags.10?true peer:InputPeer collection_id:flags.6?int offset:string limit:int = payments.SavedStarGifts
    ```
    """
    def __new__(
        cls,
        exclude_unsaved: bool,
        exclude_saved: bool,
        exclude_unlimited: bool,
        exclude_unique: bool,
        sort_by_value: bool,
        exclude_upgradable: bool,
        exclude_unupgradable: bool,
        peer_color_available: bool,
        exclude_hosted: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        collection_id: Optional[int],
        offset: str,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSavedStarGift(TLRequest):
    """
    [Read `payments.getSavedStarGift` docs](https://core.telegram.org/method/payments.getSavedStarGift).

    Generated from the following TL definition:
    ```tl
    payments.getSavedStarGift#b455a106 stargift:Vector<InputSavedStarGift> = payments.SavedStarGifts
    ```
    """
    def __new__(
        cls,
        stargift: Sequence[types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarGiftWithdrawalUrl(TLRequest):
    """
    [Read `payments.getStarGiftWithdrawalUrl` docs](https://core.telegram.org/method/payments.getStarGiftWithdrawalUrl).

    Generated from the following TL definition:
    ```tl
    payments.getStarGiftWithdrawalUrl#d06e93a8 stargift:InputSavedStarGift password:InputCheckPasswordSRP = payments.StarGiftWithdrawalUrl
    ```
    """
    def __new__(
        cls,
        stargift: types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug,
        password: types.InputCheckPasswordEmpty | types.InputCheckPasswordSrp,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleChatStarGiftNotifications(TLRequest):
    """
    [Read `payments.toggleChatStarGiftNotifications` docs](https://core.telegram.org/method/payments.toggleChatStarGiftNotifications).

    Generated from the following TL definition:
    ```tl
    payments.toggleChatStarGiftNotifications#60eaefa1 flags:# enabled:flags.0?true peer:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        enabled: bool,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ToggleStarGiftsPinnedToTop(TLRequest):
    """
    [Read `payments.toggleStarGiftsPinnedToTop` docs](https://core.telegram.org/method/payments.toggleStarGiftsPinnedToTop).

    Generated from the following TL definition:
    ```tl
    payments.toggleStarGiftsPinnedToTop#1513e7b0 peer:InputPeer stargift:Vector<InputSavedStarGift> = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        stargift: Sequence[types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CanPurchaseStore(TLRequest):
    """
    [Read `payments.canPurchaseStore` docs](https://core.telegram.org/method/payments.canPurchaseStore).

    Generated from the following TL definition:
    ```tl
    payments.canPurchaseStore#4fdc5ea7 purpose:InputStorePaymentPurpose = Bool
    ```
    """
    def __new__(
        cls,
        purpose: types.InputStorePaymentPremiumSubscription | types.InputStorePaymentGiftPremium | types.InputStorePaymentPremiumGiftCode | types.InputStorePaymentPremiumGiveaway | types.InputStorePaymentStarsTopup | types.InputStorePaymentStarsGift | types.InputStorePaymentStarsGiveaway | types.InputStorePaymentAuthCode,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetResaleStarGifts(TLRequest):
    """
    [Read `payments.getResaleStarGifts` docs](https://core.telegram.org/method/payments.getResaleStarGifts).

    Generated from the following TL definition:
    ```tl
    payments.getResaleStarGifts#7a5fa236 flags:# sort_by_price:flags.1?true sort_by_num:flags.2?true attributes_hash:flags.0?long gift_id:long attributes:flags.3?Vector<StarGiftAttributeId> offset:string limit:int = payments.ResaleStarGifts
    ```
    """
    def __new__(
        cls,
        sort_by_price: bool,
        sort_by_num: bool,
        attributes_hash: Optional[int],
        gift_id: int,
        attributes: Optional[Sequence[types.StarGiftAttributeIdModel | types.StarGiftAttributeIdPattern | types.StarGiftAttributeIdBackdrop]],
        offset: str,
        limit: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStarGiftPrice(TLRequest):
    """
    [Read `payments.updateStarGiftPrice` docs](https://core.telegram.org/method/payments.updateStarGiftPrice).

    Generated from the following TL definition:
    ```tl
    payments.updateStarGiftPrice#edbe6ccb stargift:InputSavedStarGift resell_amount:StarsAmount = Updates
    ```
    """
    def __new__(
        cls,
        stargift: types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug,
        resell_amount: types.StarsAmount | types.StarsTonAmount,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CreateStarGiftCollection(TLRequest):
    """
    [Read `payments.createStarGiftCollection` docs](https://core.telegram.org/method/payments.createStarGiftCollection).

    Generated from the following TL definition:
    ```tl
    payments.createStarGiftCollection#1f4a0e87 peer:InputPeer title:string stargift:Vector<InputSavedStarGift> = StarGiftCollection
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        title: str,
        stargift: Sequence[types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UpdateStarGiftCollection(TLRequest):
    """
    [Read `payments.updateStarGiftCollection` docs](https://core.telegram.org/method/payments.updateStarGiftCollection).

    Generated from the following TL definition:
    ```tl
    payments.updateStarGiftCollection#4fddbee7 flags:# peer:InputPeer collection_id:int title:flags.0?string delete_stargift:flags.1?Vector<InputSavedStarGift> add_stargift:flags.2?Vector<InputSavedStarGift> order:flags.3?Vector<InputSavedStarGift> = StarGiftCollection
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        collection_id: int,
        title: Optional[str],
        delete_stargift: Optional[Sequence[types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug]],
        add_stargift: Optional[Sequence[types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug]],
        order: Optional[Sequence[types.InputSavedStarGiftUser | types.InputSavedStarGiftChat | types.InputSavedStarGiftSlug]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ReorderStarGiftCollections(TLRequest):
    """
    [Read `payments.reorderStarGiftCollections` docs](https://core.telegram.org/method/payments.reorderStarGiftCollections).

    Generated from the following TL definition:
    ```tl
    payments.reorderStarGiftCollections#c32af4cc peer:InputPeer order:Vector<int> = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        order: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeleteStarGiftCollection(TLRequest):
    """
    [Read `payments.deleteStarGiftCollection` docs](https://core.telegram.org/method/payments.deleteStarGiftCollection).

    Generated from the following TL definition:
    ```tl
    payments.deleteStarGiftCollection#ad5648e8 peer:InputPeer collection_id:int = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        collection_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarGiftCollections(TLRequest):
    """
    [Read `payments.getStarGiftCollections` docs](https://core.telegram.org/method/payments.getStarGiftCollections).

    Generated from the following TL definition:
    ```tl
    payments.getStarGiftCollections#981b91dd peer:InputPeer hash:long = payments.StarGiftCollections
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetUniqueStarGiftValueInfo(TLRequest):
    """
    [Read `payments.getUniqueStarGiftValueInfo` docs](https://core.telegram.org/method/payments.getUniqueStarGiftValueInfo).

    Generated from the following TL definition:
    ```tl
    payments.getUniqueStarGiftValueInfo#4365af6b slug:string = payments.UniqueStarGiftValueInfo
    ```
    """
    def __new__(
        cls,
        slug: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CheckCanSendGift(TLRequest):
    """
    [Read `payments.checkCanSendGift` docs](https://core.telegram.org/method/payments.checkCanSendGift).

    Generated from the following TL definition:
    ```tl
    payments.checkCanSendGift#c0c4edc9 gift_id:long = payments.CheckCanSendGiftResult
    ```
    """
    def __new__(
        cls,
        gift_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarGiftAuctionState(TLRequest):
    """
    [Read `payments.getStarGiftAuctionState` docs](https://core.telegram.org/method/payments.getStarGiftAuctionState).

    Generated from the following TL definition:
    ```tl
    payments.getStarGiftAuctionState#5c9ff4d6 auction:InputStarGiftAuction version:int = payments.StarGiftAuctionState
    ```
    """
    def __new__(
        cls,
        auction: types.InputStarGiftAuction | types.InputStarGiftAuctionSlug,
        version: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarGiftAuctionAcquiredGifts(TLRequest):
    """
    [Read `payments.getStarGiftAuctionAcquiredGifts` docs](https://core.telegram.org/method/payments.getStarGiftAuctionAcquiredGifts).

    Generated from the following TL definition:
    ```tl
    payments.getStarGiftAuctionAcquiredGifts#6ba2cbec gift_id:long = payments.StarGiftAuctionAcquiredGifts
    ```
    """
    def __new__(
        cls,
        gift_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarGiftActiveAuctions(TLRequest):
    """
    [Read `payments.getStarGiftActiveAuctions` docs](https://core.telegram.org/method/payments.getStarGiftActiveAuctions).

    Generated from the following TL definition:
    ```tl
    payments.getStarGiftActiveAuctions#a5d0514d hash:long = payments.StarGiftActiveAuctions
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ResolveStarGiftOffer(TLRequest):
    """
    [Read `payments.resolveStarGiftOffer` docs](https://core.telegram.org/method/payments.resolveStarGiftOffer).

    Generated from the following TL definition:
    ```tl
    payments.resolveStarGiftOffer#e9ce781c flags:# decline:flags.0?true offer_msg_id:int = Updates
    ```
    """
    def __new__(
        cls,
        decline: bool,
        offer_msg_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SendStarGiftOffer(TLRequest):
    """
    [Read `payments.sendStarGiftOffer` docs](https://core.telegram.org/method/payments.sendStarGiftOffer).

    Generated from the following TL definition:
    ```tl
    payments.sendStarGiftOffer#8fb86b41 flags:# peer:InputPeer slug:string price:StarsAmount duration:int random_id:long allow_paid_stars:flags.0?long = Updates
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        slug: str,
        price: types.StarsAmount | types.StarsTonAmount,
        duration: int,
        random_id: int,
        allow_paid_stars: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStarGiftUpgradeAttributes(TLRequest):
    """
    [Read `payments.getStarGiftUpgradeAttributes` docs](https://core.telegram.org/method/payments.getStarGiftUpgradeAttributes).

    Generated from the following TL definition:
    ```tl
    payments.getStarGiftUpgradeAttributes#6d038b58 gift_id:long = payments.StarGiftUpgradeAttributes
    ```
    """
    def __new__(
        cls,
        gift_id: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

