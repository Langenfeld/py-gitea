from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitHook")


@attr.s(auto_attribs=True)
class GitHook:
    """GitHook represents a Git repository hook

    Attributes:
        content (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        name (Union[Unset, str]):
    """

    content: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content
        is_active = self.is_active
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content", UNSET)

        is_active = d.pop("is_active", UNSET)

        name = d.pop("name", UNSET)

        git_hook = cls(
            content=content,
            is_active=is_active,
            name=name,
        )

        git_hook.additional_properties = d
        return git_hook

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
