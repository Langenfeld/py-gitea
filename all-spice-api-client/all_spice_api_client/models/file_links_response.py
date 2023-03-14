from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileLinksResponse")


@attr.s(auto_attribs=True)
class FileLinksResponse:
    """FileLinksResponse contains the links for a repo's file

    Attributes:
        git (Union[Unset, str]):
        html (Union[Unset, str]):
        self_ (Union[Unset, str]):
    """

    git: Union[Unset, str] = UNSET
    html: Union[Unset, str] = UNSET
    self_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        git = self.git
        html = self.html
        self_ = self.self_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if git is not UNSET:
            field_dict["git"] = git
        if html is not UNSET:
            field_dict["html"] = html
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        git = d.pop("git", UNSET)

        html = d.pop("html", UNSET)

        self_ = d.pop("self", UNSET)

        file_links_response = cls(
            git=git,
            html=html,
            self_=self_,
        )

        file_links_response.additional_properties = d
        return file_links_response

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
