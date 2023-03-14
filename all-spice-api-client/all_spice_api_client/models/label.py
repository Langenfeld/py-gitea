from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Label")


@attr.s(auto_attribs=True)
class Label:
    """Label a label to an issue or a pr

    Attributes:
        color (Union[Unset, str]):  Example: 00aabb.
        description (Union[Unset, str]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    color: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        color = self.color
        description = self.description
        id = self.id
        name = self.name
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        color = d.pop("color", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        label = cls(
            color=color,
            description=description,
            id=id,
            name=name,
            url=url,
        )

        label.additional_properties = d
        return label

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
