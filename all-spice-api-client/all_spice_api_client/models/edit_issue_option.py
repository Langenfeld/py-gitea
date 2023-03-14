import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditIssueOption")


@attr.s(auto_attribs=True)
class EditIssueOption:
    """EditIssueOption options for editing an issue

    Attributes:
        assignee (Union[Unset, str]): deprecated
        assignees (Union[Unset, List[str]]):
        body (Union[Unset, str]):
        due_date (Union[Unset, datetime.datetime]):
        milestone (Union[Unset, int]):
        ref (Union[Unset, str]):
        state (Union[Unset, str]):
        title (Union[Unset, str]):
        unset_due_date (Union[Unset, bool]):
    """

    assignee: Union[Unset, str] = UNSET
    assignees: Union[Unset, List[str]] = UNSET
    body: Union[Unset, str] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    milestone: Union[Unset, int] = UNSET
    ref: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    unset_due_date: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assignee = self.assignee
        assignees: Union[Unset, List[str]] = UNSET
        if not isinstance(self.assignees, Unset):
            assignees = self.assignees

        body = self.body
        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        milestone = self.milestone
        ref = self.ref
        state = self.state
        title = self.title
        unset_due_date = self.unset_due_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if assignees is not UNSET:
            field_dict["assignees"] = assignees
        if body is not UNSET:
            field_dict["body"] = body
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if milestone is not UNSET:
            field_dict["milestone"] = milestone
        if ref is not UNSET:
            field_dict["ref"] = ref
        if state is not UNSET:
            field_dict["state"] = state
        if title is not UNSET:
            field_dict["title"] = title
        if unset_due_date is not UNSET:
            field_dict["unset_due_date"] = unset_due_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        assignee = d.pop("assignee", UNSET)

        assignees = cast(List[str], d.pop("assignees", UNSET))

        body = d.pop("body", UNSET)

        _due_date = d.pop("due_date", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        milestone = d.pop("milestone", UNSET)

        ref = d.pop("ref", UNSET)

        state = d.pop("state", UNSET)

        title = d.pop("title", UNSET)

        unset_due_date = d.pop("unset_due_date", UNSET)

        edit_issue_option = cls(
            assignee=assignee,
            assignees=assignees,
            body=body,
            due_date=due_date,
            milestone=milestone,
            ref=ref,
            state=state,
            title=title,
            unset_due_date=unset_due_date,
        )

        edit_issue_option.additional_properties = d
        return edit_issue_option

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
