from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditLabelOption")


@attr.s(auto_attribs=True)
class EditLabelOption:
    """EditLabelOption options for editing a label

    Attributes:
        color (Union[Unset, str]):
        description (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    color: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        color = self.color
        description = self.description
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        color = d.pop("color", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        edit_label_option = cls(
            color=color,
            description=description,
            name=name,
        )

        edit_label_option.additional_properties = d
        return edit_label_option

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
