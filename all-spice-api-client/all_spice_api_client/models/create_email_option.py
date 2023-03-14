from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEmailOption")


@attr.s(auto_attribs=True)
class CreateEmailOption:
    """CreateEmailOption options when creating email addresses

    Attributes:
        emails (Union[Unset, List[str]]): email addresses to add
    """

    emails: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if emails is not UNSET:
            field_dict["emails"] = emails

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        emails = cast(List[str], d.pop("emails", UNSET))

        create_email_option = cls(
            emails=emails,
        )

        create_email_option.additional_properties = d
        return create_email_option

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
