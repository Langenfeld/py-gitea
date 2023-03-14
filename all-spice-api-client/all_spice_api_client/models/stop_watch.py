import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StopWatch")


@attr.s(auto_attribs=True)
class StopWatch:
    """StopWatch represent a running stopwatch

    Attributes:
        created (Union[Unset, datetime.datetime]):
        duration (Union[Unset, str]):
        issue_index (Union[Unset, int]):
        issue_title (Union[Unset, str]):
        repo_name (Union[Unset, str]):
        repo_owner_name (Union[Unset, str]):
        seconds (Union[Unset, int]):
    """

    created: Union[Unset, datetime.datetime] = UNSET
    duration: Union[Unset, str] = UNSET
    issue_index: Union[Unset, int] = UNSET
    issue_title: Union[Unset, str] = UNSET
    repo_name: Union[Unset, str] = UNSET
    repo_owner_name: Union[Unset, str] = UNSET
    seconds: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        duration = self.duration
        issue_index = self.issue_index
        issue_title = self.issue_title
        repo_name = self.repo_name
        repo_owner_name = self.repo_owner_name
        seconds = self.seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if duration is not UNSET:
            field_dict["duration"] = duration
        if issue_index is not UNSET:
            field_dict["issue_index"] = issue_index
        if issue_title is not UNSET:
            field_dict["issue_title"] = issue_title
        if repo_name is not UNSET:
            field_dict["repo_name"] = repo_name
        if repo_owner_name is not UNSET:
            field_dict["repo_owner_name"] = repo_owner_name
        if seconds is not UNSET:
            field_dict["seconds"] = seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        duration = d.pop("duration", UNSET)

        issue_index = d.pop("issue_index", UNSET)

        issue_title = d.pop("issue_title", UNSET)

        repo_name = d.pop("repo_name", UNSET)

        repo_owner_name = d.pop("repo_owner_name", UNSET)

        seconds = d.pop("seconds", UNSET)

        stop_watch = cls(
            created=created,
            duration=duration,
            issue_index=issue_index,
            issue_title=issue_title,
            repo_name=repo_name,
            repo_owner_name=repo_owner_name,
            seconds=seconds,
        )

        stop_watch.additional_properties = d
        return stop_watch

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
