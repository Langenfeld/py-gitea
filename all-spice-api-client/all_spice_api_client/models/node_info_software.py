from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeInfoSoftware")


@attr.s(auto_attribs=True)
class NodeInfoSoftware:
    """NodeInfoSoftware contains Metadata about server software in use

    Attributes:
        homepage (Union[Unset, str]):
        name (Union[Unset, str]):
        repository (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    homepage: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    repository: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        homepage = self.homepage
        name = self.name
        repository = self.repository
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if name is not UNSET:
            field_dict["name"] = name
        if repository is not UNSET:
            field_dict["repository"] = repository
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        homepage = d.pop("homepage", UNSET)

        name = d.pop("name", UNSET)

        repository = d.pop("repository", UNSET)

        version = d.pop("version", UNSET)

        node_info_software = cls(
            homepage=homepage,
            name=name,
            repository=repository,
            version=version,
        )

        node_info_software.additional_properties = d
        return node_info_software

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
