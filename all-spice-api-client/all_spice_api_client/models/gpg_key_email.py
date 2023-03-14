from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GPGKeyEmail")


@attr.s(auto_attribs=True)
class GPGKeyEmail:
    """GPGKeyEmail an email attached to a GPGKey

    Attributes:
        email (Union[Unset, str]):
        verified (Union[Unset, bool]):
    """

    email: Union[Unset, str] = UNSET
    verified: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        verified = self.verified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        verified = d.pop("verified", UNSET)

        gpg_key_email = cls(
            email=email,
            verified=verified,
        )

        gpg_key_email.additional_properties = d
        return gpg_key_email

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
