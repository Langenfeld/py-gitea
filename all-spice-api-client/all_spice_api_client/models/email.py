from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Email")


@attr.s(auto_attribs=True)
class Email:
    """Email an email address belonging to a user

    Attributes:
        email (Union[Unset, str]):
        primary (Union[Unset, bool]):
        verified (Union[Unset, bool]):
    """

    email: Union[Unset, str] = UNSET
    primary: Union[Unset, bool] = UNSET
    verified: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        primary = self.primary
        verified = self.verified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if primary is not UNSET:
            field_dict["primary"] = primary
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        primary = d.pop("primary", UNSET)

        verified = d.pop("verified", UNSET)

        email = cls(
            email=email,
            primary=primary,
            verified=verified,
        )

        email.additional_properties = d
        return email

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
