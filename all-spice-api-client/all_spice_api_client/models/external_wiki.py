from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalWiki")


@attr.s(auto_attribs=True)
class ExternalWiki:
    """ExternalWiki represents setting for external wiki

    Attributes:
        external_wiki_url (Union[Unset, str]): URL of external wiki.
    """

    external_wiki_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_wiki_url = self.external_wiki_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_wiki_url is not UNSET:
            field_dict["external_wiki_url"] = external_wiki_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_wiki_url = d.pop("external_wiki_url", UNSET)

        external_wiki = cls(
            external_wiki_url=external_wiki_url,
        )

        external_wiki.additional_properties = d
        return external_wiki

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
