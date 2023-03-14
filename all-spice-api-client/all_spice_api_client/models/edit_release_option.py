from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditReleaseOption")


@attr.s(auto_attribs=True)
class EditReleaseOption:
    """EditReleaseOption options when editing a release

    Attributes:
        body (Union[Unset, str]):
        draft (Union[Unset, bool]):
        name (Union[Unset, str]):
        prerelease (Union[Unset, bool]):
        tag_name (Union[Unset, str]):
        target_commitish (Union[Unset, str]):
    """

    body: Union[Unset, str] = UNSET
    draft: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    prerelease: Union[Unset, bool] = UNSET
    tag_name: Union[Unset, str] = UNSET
    target_commitish: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        draft = self.draft
        name = self.name
        prerelease = self.prerelease
        tag_name = self.tag_name
        target_commitish = self.target_commitish

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if draft is not UNSET:
            field_dict["draft"] = draft
        if name is not UNSET:
            field_dict["name"] = name
        if prerelease is not UNSET:
            field_dict["prerelease"] = prerelease
        if tag_name is not UNSET:
            field_dict["tag_name"] = tag_name
        if target_commitish is not UNSET:
            field_dict["target_commitish"] = target_commitish

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        body = d.pop("body", UNSET)

        draft = d.pop("draft", UNSET)

        name = d.pop("name", UNSET)

        prerelease = d.pop("prerelease", UNSET)

        tag_name = d.pop("tag_name", UNSET)

        target_commitish = d.pop("target_commitish", UNSET)

        edit_release_option = cls(
            body=body,
            draft=draft,
            name=name,
            prerelease=prerelease,
            tag_name=tag_name,
            target_commitish=target_commitish,
        )

        edit_release_option.additional_properties = d
        return edit_release_option

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
