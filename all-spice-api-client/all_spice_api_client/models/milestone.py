import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Milestone")


@attr.s(auto_attribs=True)
class Milestone:
    """Milestone milestone is a collection of issues on one repository

    Attributes:
        closed_at (Union[Unset, datetime.datetime]):
        closed_issues (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        due_on (Union[Unset, datetime.datetime]):
        id (Union[Unset, int]):
        open_issues (Union[Unset, int]):
        state (Union[Unset, str]): StateType issue state type
        title (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    closed_at: Union[Unset, datetime.datetime] = UNSET
    closed_issues: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    due_on: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    open_issues: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        closed_at: Union[Unset, str] = UNSET
        if not isinstance(self.closed_at, Unset):
            closed_at = self.closed_at.isoformat()

        closed_issues = self.closed_issues
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description
        due_on: Union[Unset, str] = UNSET
        if not isinstance(self.due_on, Unset):
            due_on = self.due_on.isoformat()

        id = self.id
        open_issues = self.open_issues
        state = self.state
        title = self.title
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if closed_issues is not UNSET:
            field_dict["closed_issues"] = closed_issues
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if due_on is not UNSET:
            field_dict["due_on"] = due_on
        if id is not UNSET:
            field_dict["id"] = id
        if open_issues is not UNSET:
            field_dict["open_issues"] = open_issues
        if state is not UNSET:
            field_dict["state"] = state
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _closed_at = d.pop("closed_at", UNSET)
        closed_at: Union[Unset, datetime.datetime]
        if isinstance(_closed_at, Unset):
            closed_at = UNSET
        else:
            closed_at = isoparse(_closed_at)

        closed_issues = d.pop("closed_issues", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        description = d.pop("description", UNSET)

        _due_on = d.pop("due_on", UNSET)
        due_on: Union[Unset, datetime.datetime]
        if isinstance(_due_on, Unset):
            due_on = UNSET
        else:
            due_on = isoparse(_due_on)

        id = d.pop("id", UNSET)

        open_issues = d.pop("open_issues", UNSET)

        state = d.pop("state", UNSET)

        title = d.pop("title", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        milestone = cls(
            closed_at=closed_at,
            closed_issues=closed_issues,
            created_at=created_at,
            description=description,
            due_on=due_on,
            id=id,
            open_issues=open_issues,
            state=state,
            title=title,
            updated_at=updated_at,
        )

        milestone.additional_properties = d
        return milestone

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
