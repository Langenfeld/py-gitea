from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitObjectRepresentsAGitObject")


@attr.s(auto_attribs=True)
class GitObjectRepresentsAGitObject:
    """
    Attributes:
        sha (Union[Unset, str]):
        type (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    sha: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sha = self.sha
        type = self.type
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sha is not UNSET:
            field_dict["sha"] = sha
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sha = d.pop("sha", UNSET)

        type = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        git_object_represents_a_git_object = cls(
            sha=sha,
            type=type,
            url=url,
        )

        git_object_represents_a_git_object.additional_properties = d
        return git_object_represents_a_git_object

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
