from typing import final, Self, Sequence
from grammers.tl import TLRequest

@final
class GetLangPack(TLRequest):
    """
    [Read `langpack.getLangPack` docs](https://core.telegram.org/method/langpack.getLangPack).

    Generated from the following TL definition:
    ```tl
    langpack.getLangPack#f2f2330a lang_pack:string lang_code:string = LangPackDifference
    ```
    """
    def __new__(
        cls,
        lang_pack: str,
        lang_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetStrings(TLRequest):
    """
    [Read `langpack.getStrings` docs](https://core.telegram.org/method/langpack.getStrings).

    Generated from the following TL definition:
    ```tl
    langpack.getStrings#efea3803 lang_pack:string lang_code:string keys:Vector<string> = Vector<LangPackString>
    ```
    """
    def __new__(
        cls,
        lang_pack: str,
        lang_code: str,
        keys: Sequence[str],
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetDifference(TLRequest):
    """
    [Read `langpack.getDifference` docs](https://core.telegram.org/method/langpack.getDifference).

    Generated from the following TL definition:
    ```tl
    langpack.getDifference#cd984aa5 lang_pack:string lang_code:string from_version:int = LangPackDifference
    ```
    """
    def __new__(
        cls,
        lang_pack: str,
        lang_code: str,
        from_version: int,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetLanguages(TLRequest):
    """
    [Read `langpack.getLanguages` docs](https://core.telegram.org/method/langpack.getLanguages).

    Generated from the following TL definition:
    ```tl
    langpack.getLanguages#42c6978f lang_pack:string = Vector<LangPackLanguage>
    ```
    """
    def __new__(
        cls,
        lang_pack: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

@final
class GetLanguage(TLRequest):
    """
    [Read `langpack.getLanguage` docs](https://core.telegram.org/method/langpack.getLanguage).

    Generated from the following TL definition:
    ```tl
    langpack.getLanguage#6a596502 lang_pack:string lang_code:string = LangPackLanguage
    ```
    """
    def __new__(
        cls,
        lang_pack: str,
        lang_code: str,
    ) -> Self: ...
    def to_dict(self) -> dict: ...

