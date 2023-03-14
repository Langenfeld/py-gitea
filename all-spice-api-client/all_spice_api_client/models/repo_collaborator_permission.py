from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="RepoCollaboratorPermission")


@attr.s(auto_attribs=True)
class RepoCollaboratorPermission:
    """RepoCollaboratorPermission to get repository permission for a collaborator

    Attributes:
        permission (Union[Unset, str]):
        role_name (Union[Unset, str]):
        user (Union[Unset, User]): User represents a user
    """

    permission: Union[Unset, str] = UNSET
    role_name: Union[Unset, str] = UNSET
    user: Union[Unset, "User"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permission = self.permission
        role_name = self.role_name
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission is not UNSET:
            field_dict["permission"] = permission
        if role_name is not UNSET:
            field_dict["role_name"] = role_name
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user import User

        d = src_dict.copy()
        permission = d.pop("permission", UNSET)

        role_name = d.pop("role_name", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        repo_collaborator_permission = cls(
            permission=permission,
            role_name=role_name,
            user=user,
        )

        repo_collaborator_permission.additional_properties = d
        return repo_collaborator_permission

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
