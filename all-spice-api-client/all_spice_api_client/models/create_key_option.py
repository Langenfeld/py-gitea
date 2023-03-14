from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKeyOption")


@attr.s(auto_attribs=True)
class CreateKeyOption:
    """CreateKeyOption options when creating a key

    Attributes:
        key (str): An armored SSH key to add
        title (str): Title of the key to add
        read_only (Union[Unset, bool]): Describe if the key has only read access or read/write
    """

    key: str
    title: str
    read_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        title = self.title
        read_only = self.read_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "title": title,
            }
        )
        if read_only is not UNSET:
            field_dict["read_only"] = read_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        title = d.pop("title")

        read_only = d.pop("read_only", UNSET)

        create_key_option = cls(
            key=key,
            title=title,
            read_only=read_only,
        )

        create_key_option.additional_properties = d
        return create_key_option

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
