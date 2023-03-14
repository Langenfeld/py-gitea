from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Permission")


@attr.s(auto_attribs=True)
class Permission:
    """Permission represents a set of permissions

    Attributes:
        admin (Union[Unset, bool]):
        pull (Union[Unset, bool]):
        push (Union[Unset, bool]):
    """

    admin: Union[Unset, bool] = UNSET
    pull: Union[Unset, bool] = UNSET
    push: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        admin = self.admin
        pull = self.pull
        push = self.push

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin is not UNSET:
            field_dict["admin"] = admin
        if pull is not UNSET:
            field_dict["pull"] = pull
        if push is not UNSET:
            field_dict["push"] = push

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        admin = d.pop("admin", UNSET)

        pull = d.pop("pull", UNSET)

        push = d.pop("push", UNSET)

        permission = cls(
            admin=admin,
            pull=pull,
            push=push,
        )

        permission.additional_properties = d
        return permission

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
