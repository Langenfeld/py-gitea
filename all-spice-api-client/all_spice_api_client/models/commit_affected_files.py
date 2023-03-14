from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitAffectedFiles")


@attr.s(auto_attribs=True)
class CommitAffectedFiles:
    """CommitAffectedFiles store information about files affected by the commit

    Attributes:
        filename (Union[Unset, str]):
    """

    filename: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filename = self.filename

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filename = d.pop("filename", UNSET)

        commit_affected_files = cls(
            filename=filename,
        )

        commit_affected_files.additional_properties = d
        return commit_affected_files

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
