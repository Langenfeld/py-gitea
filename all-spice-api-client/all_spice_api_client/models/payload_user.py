from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PayloadUser")


@attr.s(auto_attribs=True)
class PayloadUser:
    """PayloadUser represents the author or committer of a commit

    Attributes:
        email (Union[Unset, str]):
        name (Union[Unset, str]): Full name of the commit author
        username (Union[Unset, str]):
    """

    email: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        name = self.name
        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        name = d.pop("name", UNSET)

        username = d.pop("username", UNSET)

        payload_user = cls(
            email=email,
            name=name,
            username=username,
        )

        payload_user.additional_properties = d
        return payload_user

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
