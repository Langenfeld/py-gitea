from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeneralAPISettings")


@attr.s(auto_attribs=True)
class GeneralAPISettings:
    """GeneralAPISettings contains global api settings exposed by it

    Attributes:
        default_git_trees_per_page (Union[Unset, int]):
        default_max_blob_size (Union[Unset, int]):
        default_paging_num (Union[Unset, int]):
        max_response_items (Union[Unset, int]):
    """

    default_git_trees_per_page: Union[Unset, int] = UNSET
    default_max_blob_size: Union[Unset, int] = UNSET
    default_paging_num: Union[Unset, int] = UNSET
    max_response_items: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_git_trees_per_page = self.default_git_trees_per_page
        default_max_blob_size = self.default_max_blob_size
        default_paging_num = self.default_paging_num
        max_response_items = self.max_response_items

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_git_trees_per_page is not UNSET:
            field_dict["default_git_trees_per_page"] = default_git_trees_per_page
        if default_max_blob_size is not UNSET:
            field_dict["default_max_blob_size"] = default_max_blob_size
        if default_paging_num is not UNSET:
            field_dict["default_paging_num"] = default_paging_num
        if max_response_items is not UNSET:
            field_dict["max_response_items"] = max_response_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        default_git_trees_per_page = d.pop("default_git_trees_per_page", UNSET)

        default_max_blob_size = d.pop("default_max_blob_size", UNSET)

        default_paging_num = d.pop("default_paging_num", UNSET)

        max_response_items = d.pop("max_response_items", UNSET)

        general_api_settings = cls(
            default_git_trees_per_page=default_git_trees_per_page,
            default_max_blob_size=default_max_blob_size,
            default_paging_num=default_paging_num,
            max_response_items=max_response_items,
        )

        general_api_settings.additional_properties = d
        return general_api_settings

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
