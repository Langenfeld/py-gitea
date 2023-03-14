from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddCollaboratorOption")


@attr.s(auto_attribs=True)
class AddCollaboratorOption:
    """AddCollaboratorOption options when adding a user as a collaborator of a repository

    Attributes:
        permission (Union[Unset, str]):
    """

    permission: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permission = self.permission

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        permission = d.pop("permission", UNSET)

        add_collaborator_option = cls(
            permission=permission,
        )

        add_collaborator_option.additional_properties = d
        return add_collaborator_option

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
