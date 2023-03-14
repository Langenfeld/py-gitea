import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue import Issue


T = TypeVar("T", bound="TrackedTime")


@attr.s(auto_attribs=True)
class TrackedTime:
    """TrackedTime worked time for an issue / pr

    Attributes:
        created (Union[Unset, datetime.datetime]):
        id (Union[Unset, int]):
        issue (Union[Unset, Issue]): Issue represents an issue in a repository
        issue_id (Union[Unset, int]): deprecated (only for backwards compatibility)
        time (Union[Unset, int]): Time in seconds
        user_id (Union[Unset, int]): deprecated (only for backwards compatibility)
        user_name (Union[Unset, str]):
    """

    created: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    issue: Union[Unset, "Issue"] = UNSET
    issue_id: Union[Unset, int] = UNSET
    time: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET
    user_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        id = self.id
        issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        issue_id = self.issue_id
        time = self.time
        user_id = self.user_id
        user_name = self.user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if issue is not UNSET:
            field_dict["issue"] = issue
        if issue_id is not UNSET:
            field_dict["issue_id"] = issue_id
        if time is not UNSET:
            field_dict["time"] = time
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_name is not UNSET:
            field_dict["user_name"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.issue import Issue

        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        id = d.pop("id", UNSET)

        _issue = d.pop("issue", UNSET)
        issue: Union[Unset, Issue]
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = Issue.from_dict(_issue)

        issue_id = d.pop("issue_id", UNSET)

        time = d.pop("time", UNSET)

        user_id = d.pop("user_id", UNSET)

        user_name = d.pop("user_name", UNSET)

        tracked_time = cls(
            created=created,
            id=id,
            issue=issue,
            issue_id=issue_id,
            time=time,
            user_id=user_id,
            user_name=user_name,
        )

        tracked_time.additional_properties = d
        return tracked_time

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
