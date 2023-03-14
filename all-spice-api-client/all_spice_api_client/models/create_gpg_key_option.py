from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateGPGKeyOption")


@attr.s(auto_attribs=True)
class CreateGPGKeyOption:
    """CreateGPGKeyOption options create user GPG key

    Attributes:
        armored_public_key (str): An armored GPG key to add
        armored_signature (Union[Unset, str]):
    """

    armored_public_key: str
    armored_signature: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        armored_public_key = self.armored_public_key
        armored_signature = self.armored_signature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "armored_public_key": armored_public_key,
            }
        )
        if armored_signature is not UNSET:
            field_dict["armored_signature"] = armored_signature

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        armored_public_key = d.pop("armored_public_key")

        armored_signature = d.pop("armored_signature", UNSET)

        create_gpg_key_option = cls(
            armored_public_key=armored_public_key,
            armored_signature=armored_signature,
        )

        create_gpg_key_option.additional_properties = d
        return create_gpg_key_option

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
