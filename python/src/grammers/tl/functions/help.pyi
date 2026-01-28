from typing import final, Self, Sequence, Optional
from grammers.tl import TLRequest, types

@final
class GetConfig(TLRequest):
    """
    [Read `help.getConfig` docs](https://core.telegram.org/method/help.getConfig).

    Generated from the following TL definition:
    ```tl
    help.getConfig#c4f9186b = Config
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetNearestDc(TLRequest):
    """
    [Read `help.getNearestDc` docs](https://core.telegram.org/method/help.getNearestDc).

    Generated from the following TL definition:
    ```tl
    help.getNearestDc#1fb33026 = NearestDc
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAppUpdate(TLRequest):
    """
    [Read `help.getAppUpdate` docs](https://core.telegram.org/method/help.getAppUpdate).

    Generated from the following TL definition:
    ```tl
    help.getAppUpdate#522d5a7d source:string = help.AppUpdate
    ```
    """
    def __new__(
        cls,
        source: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetInviteText(TLRequest):
    """
    [Read `help.getInviteText` docs](https://core.telegram.org/method/help.getInviteText).

    Generated from the following TL definition:
    ```tl
    help.getInviteText#4d392343 = help.InviteText
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSupport(TLRequest):
    """
    [Read `help.getSupport` docs](https://core.telegram.org/method/help.getSupport).

    Generated from the following TL definition:
    ```tl
    help.getSupport#9cdf08cd = help.Support
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SetBotUpdatesStatus(TLRequest):
    """
    [Read `help.setBotUpdatesStatus` docs](https://core.telegram.org/method/help.setBotUpdatesStatus).

    Generated from the following TL definition:
    ```tl
    help.setBotUpdatesStatus#ec22cfcd pending_updates_count:int message:string = Bool
    ```
    """
    def __new__(
        cls,
        pending_updates_count: int,
        message: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetCdnConfig(TLRequest):
    """
    [Read `help.getCdnConfig` docs](https://core.telegram.org/method/help.getCdnConfig).

    Generated from the following TL definition:
    ```tl
    help.getCdnConfig#52029342 = CdnConfig
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetRecentMeUrls(TLRequest):
    """
    [Read `help.getRecentMeUrls` docs](https://core.telegram.org/method/help.getRecentMeUrls).

    Generated from the following TL definition:
    ```tl
    help.getRecentMeUrls#3dc0f114 referer:string = help.RecentMeUrls
    ```
    """
    def __new__(
        cls,
        referer: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetTermsOfServiceUpdate(TLRequest):
    """
    [Read `help.getTermsOfServiceUpdate` docs](https://core.telegram.org/method/help.getTermsOfServiceUpdate).

    Generated from the following TL definition:
    ```tl
    help.getTermsOfServiceUpdate#2ca51fd1 = help.TermsOfServiceUpdate
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AcceptTermsOfService(TLRequest):
    """
    [Read `help.acceptTermsOfService` docs](https://core.telegram.org/method/help.acceptTermsOfService).

    Generated from the following TL definition:
    ```tl
    help.acceptTermsOfService#ee72f79a id:DataJSON = Bool
    ```
    """
    def __new__(
        cls,
        id: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDeepLinkInfo(TLRequest):
    """
    [Read `help.getDeepLinkInfo` docs](https://core.telegram.org/method/help.getDeepLinkInfo).

    Generated from the following TL definition:
    ```tl
    help.getDeepLinkInfo#3fedc75f path:string = help.DeepLinkInfo
    ```
    """
    def __new__(
        cls,
        path: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetAppConfig(TLRequest):
    """
    [Read `help.getAppConfig` docs](https://core.telegram.org/method/help.getAppConfig).

    Generated from the following TL definition:
    ```tl
    help.getAppConfig#61e3f854 hash:int = help.AppConfig
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SaveAppLog(TLRequest):
    """
    [Read `help.saveAppLog` docs](https://core.telegram.org/method/help.saveAppLog).

    Generated from the following TL definition:
    ```tl
    help.saveAppLog#6f02f748 events:Vector<InputAppEvent> = Bool
    ```
    """
    def __new__(
        cls,
        events: Sequence[types.InputAppEvent],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPassportConfig(TLRequest):
    """
    [Read `help.getPassportConfig` docs](https://core.telegram.org/method/help.getPassportConfig).

    Generated from the following TL definition:
    ```tl
    help.getPassportConfig#c661ad08 hash:int = help.PassportConfig
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetSupportName(TLRequest):
    """
    [Read `help.getSupportName` docs](https://core.telegram.org/method/help.getSupportName).

    Generated from the following TL definition:
    ```tl
    help.getSupportName#d360e72c = help.SupportName
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetUserInfo(TLRequest):
    """
    [Read `help.getUserInfo` docs](https://core.telegram.org/method/help.getUserInfo).

    Generated from the following TL definition:
    ```tl
    help.getUserInfo#38a08d3 user_id:InputUser = help.UserInfo
    ```
    """
    def __new__(
        cls,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class EditUserInfo(TLRequest):
    """
    [Read `help.editUserInfo` docs](https://core.telegram.org/method/help.editUserInfo).

    Generated from the following TL definition:
    ```tl
    help.editUserInfo#66b91b70 user_id:InputUser message:string entities:Vector<MessageEntity> = help.UserInfo
    ```
    """
    def __new__(
        cls,
        user_id: types.InputUserEmpty | types.InputUserSelf | types.InputUser | types.InputUserFromMessage,
        message: str,
        entities: Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPromoData(TLRequest):
    """
    [Read `help.getPromoData` docs](https://core.telegram.org/method/help.getPromoData).

    Generated from the following TL definition:
    ```tl
    help.getPromoData#c0977421 = help.PromoData
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class HidePromoData(TLRequest):
    """
    [Read `help.hidePromoData` docs](https://core.telegram.org/method/help.hidePromoData).

    Generated from the following TL definition:
    ```tl
    help.hidePromoData#1e251c95 peer:InputPeer = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DismissSuggestion(TLRequest):
    """
    [Read `help.dismissSuggestion` docs](https://core.telegram.org/method/help.dismissSuggestion).

    Generated from the following TL definition:
    ```tl
    help.dismissSuggestion#f50dbaa1 peer:InputPeer suggestion:string = Bool
    ```
    """
    def __new__(
        cls,
        peer: types.InputPeerEmpty | types.InputPeerSelf | types.InputPeerChat | types.InputPeerUser | types.InputPeerChannel | types.InputPeerUserFromMessage | types.InputPeerChannelFromMessage,
        suggestion: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetCountriesList(TLRequest):
    """
    [Read `help.getCountriesList` docs](https://core.telegram.org/method/help.getCountriesList).

    Generated from the following TL definition:
    ```tl
    help.getCountriesList#735787a8 lang_code:string hash:int = help.CountriesList
    ```
    """
    def __new__(
        cls,
        lang_code: str,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPremiumPromo(TLRequest):
    """
    [Read `help.getPremiumPromo` docs](https://core.telegram.org/method/help.getPremiumPromo).

    Generated from the following TL definition:
    ```tl
    help.getPremiumPromo#b81b93d4 = help.PremiumPromo
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPeerColors(TLRequest):
    """
    [Read `help.getPeerColors` docs](https://core.telegram.org/method/help.getPeerColors).

    Generated from the following TL definition:
    ```tl
    help.getPeerColors#da80f42f hash:int = help.PeerColors
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetPeerProfileColors(TLRequest):
    """
    [Read `help.getPeerProfileColors` docs](https://core.telegram.org/method/help.getPeerProfileColors).

    Generated from the following TL definition:
    ```tl
    help.getPeerProfileColors#abcfa9fd hash:int = help.PeerColors
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetTimezonesList(TLRequest):
    """
    [Read `help.getTimezonesList` docs](https://core.telegram.org/method/help.getTimezonesList).

    Generated from the following TL definition:
    ```tl
    help.getTimezonesList#49b30240 hash:int = help.TimezonesList
    ```
    """
    def __new__(
        cls,
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

