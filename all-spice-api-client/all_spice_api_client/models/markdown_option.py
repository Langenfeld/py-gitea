from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkdownOption")


@attr.s(auto_attribs=True)
class MarkdownOption:
    """MarkdownOption markdown options

    Attributes:
        context (Union[Unset, str]): Context to render

            in: body
        mode (Union[Unset, str]): Mode to render

            in: body
        text (Union[Unset, str]): Text markdown to render

            in: body
        wiki (Union[Unset, bool]): Is it a wiki page ?

            in: body
    """

    context: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    wiki: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context
        mode = self.mode
        text = self.text
        wiki = self.wiki

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context is not UNSET:
            field_dict["Context"] = context
        if mode is not UNSET:
            field_dict["Mode"] = mode
        if text is not UNSET:
            field_dict["Text"] = text
        if wiki is not UNSET:
            field_dict["Wiki"] = wiki

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        context = d.pop("Context", UNSET)

        mode = d.pop("Mode", UNSET)

        text = d.pop("Text", UNSET)

        wiki = d.pop("Wiki", UNSET)

        markdown_option = cls(
            context=context,
            mode=mode,
            text=text,
            wiki=wiki,
        )

        markdown_option.additional_properties = d
        return markdown_option

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
