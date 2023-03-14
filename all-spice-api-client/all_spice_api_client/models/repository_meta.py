from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryMeta")


@attr.s(auto_attribs=True)
class RepositoryMeta:
    """RepositoryMeta basic repository information

    Attributes:
        full_name (Union[Unset, str]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        owner (Union[Unset, str]):
    """

    full_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        full_name = self.full_name
        id = self.id
        name = self.name
        owner = self.owner

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        full_name = d.pop("full_name", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        owner = d.pop("owner", UNSET)

        repository_meta = cls(
            full_name=full_name,
            id=id,
            name=name,
            owner=owner,
        )

        repository_meta.additional_properties = d
        return repository_meta

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
