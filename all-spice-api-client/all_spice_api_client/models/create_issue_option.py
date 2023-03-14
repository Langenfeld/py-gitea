import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateIssueOption")


@attr.s(auto_attribs=True)
class CreateIssueOption:
    """CreateIssueOption options to create one issue

    Attributes:
        title (str):
        assignee (Union[Unset, str]): deprecated
        assignees (Union[Unset, List[str]]):
        body (Union[Unset, str]):
        closed (Union[Unset, bool]):
        due_date (Union[Unset, datetime.datetime]):
        labels (Union[Unset, List[int]]): list of label ids
        milestone (Union[Unset, int]): milestone id
        ref (Union[Unset, str]):
    """

    title: str
    assignee: Union[Unset, str] = UNSET
    assignees: Union[Unset, List[str]] = UNSET
    body: Union[Unset, str] = UNSET
    closed: Union[Unset, bool] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    labels: Union[Unset, List[int]] = UNSET
    milestone: Union[Unset, int] = UNSET
    ref: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        assignee = self.assignee
        assignees: Union[Unset, List[str]] = UNSET
        if not isinstance(self.assignees, Unset):
            assignees = self.assignees

        body = self.body
        closed = self.closed
        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        labels: Union[Unset, List[int]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        milestone = self.milestone
        ref = self.ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if assignees is not UNSET:
            field_dict["assignees"] = assignees
        if body is not UNSET:
            field_dict["body"] = body
        if closed is not UNSET:
            field_dict["closed"] = closed
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if labels is not UNSET:
            field_dict["labels"] = labels
        if milestone is not UNSET:
            field_dict["milestone"] = milestone
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        assignee = d.pop("assignee", UNSET)

        assignees = cast(List[str], d.pop("assignees", UNSET))

        body = d.pop("body", UNSET)

        closed = d.pop("closed", UNSET)

        _due_date = d.pop("due_date", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        labels = cast(List[int], d.pop("labels", UNSET))

        milestone = d.pop("milestone", UNSET)

        ref = d.pop("ref", UNSET)

        create_issue_option = cls(
            title=title,
            assignee=assignee,
            assignees=assignees,
            body=body,
            closed=closed,
            due_date=due_date,
            labels=labels,
            milestone=milestone,
            ref=ref,
        )

        create_issue_option.additional_properties = d
        return create_issue_option

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
