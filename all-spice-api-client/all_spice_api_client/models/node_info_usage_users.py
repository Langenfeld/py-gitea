from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeInfoUsageUsers")


@attr.s(auto_attribs=True)
class NodeInfoUsageUsers:
    """NodeInfoUsageUsers contains statistics about the users of this server

    Attributes:
        active_halfyear (Union[Unset, int]):
        active_month (Union[Unset, int]):
        total (Union[Unset, int]):
    """

    active_halfyear: Union[Unset, int] = UNSET
    active_month: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active_halfyear = self.active_halfyear
        active_month = self.active_month
        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_halfyear is not UNSET:
            field_dict["activeHalfyear"] = active_halfyear
        if active_month is not UNSET:
            field_dict["activeMonth"] = active_month
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active_halfyear = d.pop("activeHalfyear", UNSET)

        active_month = d.pop("activeMonth", UNSET)

        total = d.pop("total", UNSET)

        node_info_usage_users = cls(
            active_halfyear=active_halfyear,
            active_month=active_month,
            total=total,
        )

        node_info_usage_users.additional_properties = d
        return node_info_usage_users

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
