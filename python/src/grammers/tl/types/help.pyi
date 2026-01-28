from typing import final, Self, Sequence, Optional
from grammers.tl import TLObject, types

@final
class AppUpdate(TLObject):
    """
    [Read `help.appUpdate` docs](https://core.telegram.org/constructor/help.appUpdate).

    Generated from the following TL definition:
    ```tl
    help.appUpdate#ccbbce30 flags:# can_not_skip:flags.0?true id:int version:string text:string entities:Vector<MessageEntity> document:flags.1?Document url:flags.2?string sticker:flags.3?Document = help.AppUpdate
    ```
    """
    def __new__(
        cls,
        can_not_skip: bool,
        id: int,
        version: str,
        text: str,
        entities: Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote],
        document: Optional[types.DocumentEmpty | types.Document],
        url: Optional[str],
        sticker: Optional[types.DocumentEmpty | types.Document],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class NoAppUpdate(TLObject):
    """
    [Read `help.noAppUpdate` docs](https://core.telegram.org/constructor/help.noAppUpdate).

    Generated from the following TL definition:
    ```tl
    help.noAppUpdate#c45a6536 = help.AppUpdate
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class InviteText(TLObject):
    """
    [Read `help.inviteText` docs](https://core.telegram.org/constructor/help.inviteText).

    Generated from the following TL definition:
    ```tl
    help.inviteText#18cb9f78 message:string = help.InviteText
    ```
    """
    def __new__(
        cls,
        message: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Support(TLObject):
    """
    [Read `help.support` docs](https://core.telegram.org/constructor/help.support).

    Generated from the following TL definition:
    ```tl
    help.support#17c6b5f6 phone_number:string user:User = help.Support
    ```
    """
    def __new__(
        cls,
        phone_number: str,
        user: types.UserEmpty | types.User,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TermsOfService(TLObject):
    """
    [Read `help.termsOfService` docs](https://core.telegram.org/constructor/help.termsOfService).

    Generated from the following TL definition:
    ```tl
    help.termsOfService#780a0310 flags:# popup:flags.0?true id:DataJSON text:string entities:Vector<MessageEntity> min_age_confirm:flags.1?int = help.TermsOfService
    ```
    """
    def __new__(
        cls,
        popup: bool,
        id: types.DataJson,
        text: str,
        entities: Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote],
        min_age_confirm: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class RecentMeUrls(TLObject):
    """
    [Read `help.recentMeUrls` docs](https://core.telegram.org/constructor/help.recentMeUrls).

    Generated from the following TL definition:
    ```tl
    help.recentMeUrls#e0310d7 urls:Vector<RecentMeUrl> chats:Vector<Chat> users:Vector<User> = help.RecentMeUrls
    ```
    """
    def __new__(
        cls,
        urls: Sequence[types.RecentMeUrlUnknown | types.RecentMeUrlUser | types.RecentMeUrlChat | types.RecentMeUrlChatInvite | types.RecentMeUrlStickerSet],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TermsOfServiceUpdateEmpty(TLObject):
    """
    [Read `help.termsOfServiceUpdateEmpty` docs](https://core.telegram.org/constructor/help.termsOfServiceUpdateEmpty).

    Generated from the following TL definition:
    ```tl
    help.termsOfServiceUpdateEmpty#e3309f7f expires:int = help.TermsOfServiceUpdate
    ```
    """
    def __new__(
        cls,
        expires: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TermsOfServiceUpdate(TLObject):
    """
    [Read `help.termsOfServiceUpdate` docs](https://core.telegram.org/constructor/help.termsOfServiceUpdate).

    Generated from the following TL definition:
    ```tl
    help.termsOfServiceUpdate#28ecf961 expires:int terms_of_service:help.TermsOfService = help.TermsOfServiceUpdate
    ```
    """
    def __new__(
        cls,
        expires: int,
        terms_of_service: types.help.TermsOfService,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeepLinkInfoEmpty(TLObject):
    """
    [Read `help.deepLinkInfoEmpty` docs](https://core.telegram.org/constructor/help.deepLinkInfoEmpty).

    Generated from the following TL definition:
    ```tl
    help.deepLinkInfoEmpty#66afa166 = help.DeepLinkInfo
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class DeepLinkInfo(TLObject):
    """
    [Read `help.deepLinkInfo` docs](https://core.telegram.org/constructor/help.deepLinkInfo).

    Generated from the following TL definition:
    ```tl
    help.deepLinkInfo#6a4ee832 flags:# update_app:flags.0?true message:string entities:flags.1?Vector<MessageEntity> = help.DeepLinkInfo
    ```
    """
    def __new__(
        cls,
        update_app: bool,
        message: str,
        entities: Optional[Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PassportConfigNotModified(TLObject):
    """
    [Read `help.passportConfigNotModified` docs](https://core.telegram.org/constructor/help.passportConfigNotModified).

    Generated from the following TL definition:
    ```tl
    help.passportConfigNotModified#bfb9f457 = help.PassportConfig
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PassportConfig(TLObject):
    """
    [Read `help.passportConfig` docs](https://core.telegram.org/constructor/help.passportConfig).

    Generated from the following TL definition:
    ```tl
    help.passportConfig#a098d6af hash:int countries_langs:DataJSON = help.PassportConfig
    ```
    """
    def __new__(
        cls,
        hash: int,
        countries_langs: types.DataJson,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class SupportName(TLObject):
    """
    [Read `help.supportName` docs](https://core.telegram.org/constructor/help.supportName).

    Generated from the following TL definition:
    ```tl
    help.supportName#8c05f1c9 name:string = help.SupportName
    ```
    """
    def __new__(
        cls,
        name: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UserInfoEmpty(TLObject):
    """
    [Read `help.userInfoEmpty` docs](https://core.telegram.org/constructor/help.userInfoEmpty).

    Generated from the following TL definition:
    ```tl
    help.userInfoEmpty#f3ae2eed = help.UserInfo
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class UserInfo(TLObject):
    """
    [Read `help.userInfo` docs](https://core.telegram.org/constructor/help.userInfo).

    Generated from the following TL definition:
    ```tl
    help.userInfo#1eb3758 message:string entities:Vector<MessageEntity> author:string date:int = help.UserInfo
    ```
    """
    def __new__(
        cls,
        message: str,
        entities: Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote],
        author: str,
        date: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PromoDataEmpty(TLObject):
    """
    [Read `help.promoDataEmpty` docs](https://core.telegram.org/constructor/help.promoDataEmpty).

    Generated from the following TL definition:
    ```tl
    help.promoDataEmpty#98f6ac75 expires:int = help.PromoData
    ```
    """
    def __new__(
        cls,
        expires: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PromoData(TLObject):
    """
    [Read `help.promoData` docs](https://core.telegram.org/constructor/help.promoData).

    Generated from the following TL definition:
    ```tl
    help.promoData#8a4d87a flags:# proxy:flags.0?true expires:int peer:flags.3?Peer psa_type:flags.1?string psa_message:flags.2?string pending_suggestions:Vector<string> dismissed_suggestions:Vector<string> custom_pending_suggestion:flags.4?PendingSuggestion chats:Vector<Chat> users:Vector<User> = help.PromoData
    ```
    """
    def __new__(
        cls,
        proxy: bool,
        expires: int,
        peer: Optional[types.PeerUser | types.PeerChat | types.PeerChannel],
        psa_type: Optional[str],
        psa_message: Optional[str],
        pending_suggestions: Sequence[str],
        dismissed_suggestions: Sequence[str],
        custom_pending_suggestion: Optional[types.PendingSuggestion],
        chats: Sequence[types.ChatEmpty | types.Chat | types.ChatForbidden | types.Channel | types.ChannelForbidden],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CountryCode(TLObject):
    """
    [Read `help.countryCode` docs](https://core.telegram.org/constructor/help.countryCode).

    Generated from the following TL definition:
    ```tl
    help.countryCode#4203c5ef flags:# country_code:string prefixes:flags.0?Vector<string> patterns:flags.1?Vector<string> = help.CountryCode
    ```
    """
    def __new__(
        cls,
        country_code: str,
        prefixes: Optional[Sequence[str]],
        patterns: Optional[Sequence[str]],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class Country(TLObject):
    """
    [Read `help.country` docs](https://core.telegram.org/constructor/help.country).

    Generated from the following TL definition:
    ```tl
    help.country#c3878e23 flags:# hidden:flags.0?true iso2:string default_name:string name:flags.1?string country_codes:Vector<help.CountryCode> = help.Country
    ```
    """
    def __new__(
        cls,
        hidden: bool,
        iso2: str,
        default_name: str,
        name: Optional[str],
        country_codes: Sequence[types.help.CountryCode],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CountriesListNotModified(TLObject):
    """
    [Read `help.countriesListNotModified` docs](https://core.telegram.org/constructor/help.countriesListNotModified).

    Generated from the following TL definition:
    ```tl
    help.countriesListNotModified#93cc1f32 = help.CountriesList
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class CountriesList(TLObject):
    """
    [Read `help.countriesList` docs](https://core.telegram.org/constructor/help.countriesList).

    Generated from the following TL definition:
    ```tl
    help.countriesList#87d0759e countries:Vector<help.Country> hash:int = help.CountriesList
    ```
    """
    def __new__(
        cls,
        countries: Sequence[types.help.Country],
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PremiumPromo(TLObject):
    """
    [Read `help.premiumPromo` docs](https://core.telegram.org/constructor/help.premiumPromo).

    Generated from the following TL definition:
    ```tl
    help.premiumPromo#5334759c status_text:string status_entities:Vector<MessageEntity> video_sections:Vector<string> videos:Vector<Document> period_options:Vector<PremiumSubscriptionOption> users:Vector<User> = help.PremiumPromo
    ```
    """
    def __new__(
        cls,
        status_text: str,
        status_entities: Sequence[types.MessageEntityUnknown | types.MessageEntityMention | types.MessageEntityHashtag | types.MessageEntityBotCommand | types.MessageEntityUrl | types.MessageEntityEmail | types.MessageEntityBold | types.MessageEntityItalic | types.MessageEntityCode | types.MessageEntityPre | types.MessageEntityTextUrl | types.MessageEntityMentionName | types.InputMessageEntityMentionName | types.MessageEntityPhone | types.MessageEntityCashtag | types.MessageEntityUnderline | types.MessageEntityStrike | types.MessageEntityBankCard | types.MessageEntitySpoiler | types.MessageEntityCustomEmoji | types.MessageEntityBlockquote],
        video_sections: Sequence[str],
        videos: Sequence[types.DocumentEmpty | types.Document],
        period_options: Sequence[types.PremiumSubscriptionOption],
        users: Sequence[types.UserEmpty | types.User],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AppConfigNotModified(TLObject):
    """
    [Read `help.appConfigNotModified` docs](https://core.telegram.org/constructor/help.appConfigNotModified).

    Generated from the following TL definition:
    ```tl
    help.appConfigNotModified#7cde641d = help.AppConfig
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class AppConfig(TLObject):
    """
    [Read `help.appConfig` docs](https://core.telegram.org/constructor/help.appConfig).

    Generated from the following TL definition:
    ```tl
    help.appConfig#dd18782e hash:int config:JSONValue = help.AppConfig
    ```
    """
    def __new__(
        cls,
        hash: int,
        config: types.JsonNull | types.JsonBool | types.JsonNumber | types.JsonString | types.JsonArray | types.JsonObject,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerColorSet(TLObject):
    """
    [Read `help.peerColorSet` docs](https://core.telegram.org/constructor/help.peerColorSet).

    Generated from the following TL definition:
    ```tl
    help.peerColorSet#26219a58 colors:Vector<int> = help.PeerColorSet
    ```
    """
    def __new__(
        cls,
        colors: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerColorProfileSet(TLObject):
    """
    [Read `help.peerColorProfileSet` docs](https://core.telegram.org/constructor/help.peerColorProfileSet).

    Generated from the following TL definition:
    ```tl
    help.peerColorProfileSet#767d61eb palette_colors:Vector<int> bg_colors:Vector<int> story_colors:Vector<int> = help.PeerColorSet
    ```
    """
    def __new__(
        cls,
        palette_colors: Sequence[int],
        bg_colors: Sequence[int],
        story_colors: Sequence[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerColorOption(TLObject):
    """
    [Read `help.peerColorOption` docs](https://core.telegram.org/constructor/help.peerColorOption).

    Generated from the following TL definition:
    ```tl
    help.peerColorOption#adec6ebe flags:# hidden:flags.0?true color_id:int colors:flags.1?help.PeerColorSet dark_colors:flags.2?help.PeerColorSet channel_min_level:flags.3?int group_min_level:flags.4?int = help.PeerColorOption
    ```
    """
    def __new__(
        cls,
        hidden: bool,
        color_id: int,
        colors: Optional[types.help.PeerColorSet | types.help.PeerColorProfileSet],
        dark_colors: Optional[types.help.PeerColorSet | types.help.PeerColorProfileSet],
        channel_min_level: Optional[int],
        group_min_level: Optional[int],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerColorsNotModified(TLObject):
    """
    [Read `help.peerColorsNotModified` docs](https://core.telegram.org/constructor/help.peerColorsNotModified).

    Generated from the following TL definition:
    ```tl
    help.peerColorsNotModified#2ba1f5ce = help.PeerColors
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class PeerColors(TLObject):
    """
    [Read `help.peerColors` docs](https://core.telegram.org/constructor/help.peerColors).

    Generated from the following TL definition:
    ```tl
    help.peerColors#f8ed08 hash:int colors:Vector<help.PeerColorOption> = help.PeerColors
    ```
    """
    def __new__(
        cls,
        hash: int,
        colors: Sequence[types.help.PeerColorOption],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TimezonesListNotModified(TLObject):
    """
    [Read `help.timezonesListNotModified` docs](https://core.telegram.org/constructor/help.timezonesListNotModified).

    Generated from the following TL definition:
    ```tl
    help.timezonesListNotModified#970708cc = help.TimezonesList
    ```
    """
    def __new__(
        cls,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class TimezonesList(TLObject):
    """
    [Read `help.timezonesList` docs](https://core.telegram.org/constructor/help.timezonesList).

    Generated from the following TL definition:
    ```tl
    help.timezonesList#7b74ed71 timezones:Vector<Timezone> hash:int = help.TimezonesList
    ```
    """
    def __new__(
        cls,
        timezones: Sequence[types.Timezone],
        hash: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class ConfigSimple(TLObject):
    """
    [Read `help.configSimple` docs](https://core.telegram.org/constructor/help.configSimple).

    Generated from the following TL definition:
    ```tl
    help.configSimple#5a592a6c date:int expires:int rules:vector<AccessPointRule> = help.ConfigSimple
    ```
    """
    def __new__(
        cls,
        date: int,
        expires: int,
        rules: Sequence[types.AccessPointRule],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

