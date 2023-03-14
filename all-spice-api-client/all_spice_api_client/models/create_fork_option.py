from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateForkOption")


@attr.s(auto_attribs=True)
class CreateForkOption:
    """CreateForkOption options for creating a fork

    Attributes:
        name (Union[Unset, str]): name of the forked repository
        organization (Union[Unset, str]): organization name, if forking into an organization
    """

    name: Union[Unset, str] = UNSET
    organization: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        organization = self.organization

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if organization is not UNSET:
            field_dict["organization"] = organization

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        organization = d.pop("organization", UNSET)

        create_fork_option = cls(
            name=name,
            organization=organization,
        )

        create_fork_option.additional_properties = d
        return create_fork_option

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
