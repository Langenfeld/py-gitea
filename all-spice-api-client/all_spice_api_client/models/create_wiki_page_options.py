from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWikiPageOptions")


@attr.s(auto_attribs=True)
class CreateWikiPageOptions:
    """CreateWikiPageOptions form for creating wiki

    Attributes:
        content_base64 (Union[Unset, str]): content must be base64 encoded
        message (Union[Unset, str]): optional commit message summarizing the change
        title (Union[Unset, str]): page title. leave empty to keep unchanged
    """

    content_base64: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_base64 = self.content_base64
        message = self.message
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_base64 is not UNSET:
            field_dict["content_base64"] = content_base64
        if message is not UNSET:
            field_dict["message"] = message
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content_base64 = d.pop("content_base64", UNSET)

        message = d.pop("message", UNSET)

        title = d.pop("title", UNSET)

        create_wiki_page_options = cls(
            content_base64=content_base64,
            message=message,
            title=title,
        )

        create_wiki_page_options.additional_properties = d
        return create_wiki_page_options

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
