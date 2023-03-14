import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullRequestMeta")


@attr.s(auto_attribs=True)
class PullRequestMeta:
    """PullRequestMeta PR info if an issue is a PR

    Attributes:
        merged (Union[Unset, bool]):
        merged_at (Union[Unset, datetime.datetime]):
    """

    merged: Union[Unset, bool] = UNSET
    merged_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        merged = self.merged
        merged_at: Union[Unset, str] = UNSET
        if not isinstance(self.merged_at, Unset):
            merged_at = self.merged_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merged is not UNSET:
            field_dict["merged"] = merged
        if merged_at is not UNSET:
            field_dict["merged_at"] = merged_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        merged = d.pop("merged", UNSET)

        _merged_at = d.pop("merged_at", UNSET)
        merged_at: Union[Unset, datetime.datetime]
        if isinstance(_merged_at, Unset):
            merged_at = UNSET
        else:
            merged_at = isoparse(_merged_at)

        pull_request_meta = cls(
            merged=merged,
            merged_at=merged_at,
        )

        pull_request_meta.additional_properties = d
        return pull_request_meta

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
