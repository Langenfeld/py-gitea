from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLabelOption")


@attr.s(auto_attribs=True)
class CreateLabelOption:
    """CreateLabelOption options for creating a label

    Attributes:
        color (str):  Example: #00aabb.
        name (str):
        description (Union[Unset, str]):
    """

    color: str
    name: str
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        color = self.color
        name = self.name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        color = d.pop("color")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        create_label_option = cls(
            color=color,
            name=name,
            description=description,
        )

        create_label_option.additional_properties = d
        return create_label_option

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
