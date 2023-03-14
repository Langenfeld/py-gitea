from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitEntry")


@attr.s(auto_attribs=True)
class GitEntry:
    """GitEntry represents a git tree

    Attributes:
        mode (Union[Unset, str]):
        path (Union[Unset, str]):
        sha (Union[Unset, str]):
        size (Union[Unset, int]):
        type (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    mode: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    sha: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mode = self.mode
        path = self.path
        sha = self.sha
        size = self.size
        type = self.type
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if path is not UNSET:
            field_dict["path"] = path
        if sha is not UNSET:
            field_dict["sha"] = sha
        if size is not UNSET:
            field_dict["size"] = size
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mode = d.pop("mode", UNSET)

        path = d.pop("path", UNSET)

        sha = d.pop("sha", UNSET)

        size = d.pop("size", UNSET)

        type = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        git_entry = cls(
            mode=mode,
            path=path,
            sha=sha,
            size=size,
            type=type,
            url=url,
        )

        git_entry.additional_properties = d
        return git_entry

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
