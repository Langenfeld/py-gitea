from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationPermissions")


@attr.s(auto_attribs=True)
class OrganizationPermissions:
    """OrganizationPermissions list different users permissions on an organization

    Attributes:
        can_create_repository (Union[Unset, bool]):
        can_read (Union[Unset, bool]):
        can_write (Union[Unset, bool]):
        is_admin (Union[Unset, bool]):
        is_owner (Union[Unset, bool]):
    """

    can_create_repository: Union[Unset, bool] = UNSET
    can_read: Union[Unset, bool] = UNSET
    can_write: Union[Unset, bool] = UNSET
    is_admin: Union[Unset, bool] = UNSET
    is_owner: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_create_repository = self.can_create_repository
        can_read = self.can_read
        can_write = self.can_write
        is_admin = self.is_admin
        is_owner = self.is_owner

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_create_repository is not UNSET:
            field_dict["can_create_repository"] = can_create_repository
        if can_read is not UNSET:
            field_dict["can_read"] = can_read
        if can_write is not UNSET:
            field_dict["can_write"] = can_write
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin
        if is_owner is not UNSET:
            field_dict["is_owner"] = is_owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        can_create_repository = d.pop("can_create_repository", UNSET)

        can_read = d.pop("can_read", UNSET)

        can_write = d.pop("can_write", UNSET)

        is_admin = d.pop("is_admin", UNSET)

        is_owner = d.pop("is_owner", UNSET)

        organization_permissions = cls(
            can_create_repository=can_create_repository,
            can_read=can_read,
            can_write=can_write,
            is_admin=is_admin,
            is_owner=is_owner,
        )

        organization_permissions.additional_properties = d
        return organization_permissions

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
