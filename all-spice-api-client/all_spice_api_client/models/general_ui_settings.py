from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeneralUISettings")


@attr.s(auto_attribs=True)
class GeneralUISettings:
    """GeneralUISettings contains global ui settings exposed by API

    Attributes:
        allowed_reactions (Union[Unset, List[str]]):
        custom_emojis (Union[Unset, List[str]]):
        default_theme (Union[Unset, str]):
    """

    allowed_reactions: Union[Unset, List[str]] = UNSET
    custom_emojis: Union[Unset, List[str]] = UNSET
    default_theme: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowed_reactions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_reactions, Unset):
            allowed_reactions = self.allowed_reactions

        custom_emojis: Union[Unset, List[str]] = UNSET
        if not isinstance(self.custom_emojis, Unset):
            custom_emojis = self.custom_emojis

        default_theme = self.default_theme

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_reactions is not UNSET:
            field_dict["allowed_reactions"] = allowed_reactions
        if custom_emojis is not UNSET:
            field_dict["custom_emojis"] = custom_emojis
        if default_theme is not UNSET:
            field_dict["default_theme"] = default_theme

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allowed_reactions = cast(List[str], d.pop("allowed_reactions", UNSET))

        custom_emojis = cast(List[str], d.pop("custom_emojis", UNSET))

        default_theme = d.pop("default_theme", UNSET)

        general_ui_settings = cls(
            allowed_reactions=allowed_reactions,
            custom_emojis=custom_emojis,
            default_theme=default_theme,
        )

        general_ui_settings.additional_properties = d
        return general_ui_settings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
