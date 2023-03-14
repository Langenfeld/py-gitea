from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTagOption")


@attr.s(auto_attribs=True)
class CreateTagOption:
    """CreateTagOption options when creating a tag

    Attributes:
        tag_name (str):
        message (Union[Unset, str]):
        target (Union[Unset, str]):
    """

    tag_name: str
    message: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag_name = self.tag_name
        message = self.message
        target = self.target

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag_name": tag_name,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag_name = d.pop("tag_name")

        message = d.pop("message", UNSET)

        target = d.pop("target", UNSET)

        create_tag_option = cls(
            tag_name=tag_name,
            message=message,
            target=target,
        )

        create_tag_option.additional_properties = d
        return create_tag_option

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
