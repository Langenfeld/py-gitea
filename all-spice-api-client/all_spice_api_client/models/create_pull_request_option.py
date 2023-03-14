import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePullRequestOption")


@attr.s(auto_attribs=True)
class CreatePullRequestOption:
    """CreatePullRequestOption options when creating a pull request

    Attributes:
        assignee (Union[Unset, str]):
        assignees (Union[Unset, List[str]]):
        base (Union[Unset, str]):
        body (Union[Unset, str]):
        due_date (Union[Unset, datetime.datetime]):
        head (Union[Unset, str]):
        labels (Union[Unset, List[int]]):
        milestone (Union[Unset, int]):
        title (Union[Unset, str]):
    """

    assignee: Union[Unset, str] = UNSET
    assignees: Union[Unset, List[str]] = UNSET
    base: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    head: Union[Unset, str] = UNSET
    labels: Union[Unset, List[int]] = UNSET
    milestone: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assignee = self.assignee
        assignees: Union[Unset, List[str]] = UNSET
        if not isinstance(self.assignees, Unset):
            assignees = self.assignees

        base = self.base
        body = self.body
        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        head = self.head
        labels: Union[Unset, List[int]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        milestone = self.milestone
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if assignees is not UNSET:
            field_dict["assignees"] = assignees
        if base is not UNSET:
            field_dict["base"] = base
        if body is not UNSET:
            field_dict["body"] = body
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if head is not UNSET:
            field_dict["head"] = head
        if labels is not UNSET:
            field_dict["labels"] = labels
        if milestone is not UNSET:
            field_dict["milestone"] = milestone
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        assignee = d.pop("assignee", UNSET)

        assignees = cast(List[str], d.pop("assignees", UNSET))

        base = d.pop("base", UNSET)

        body = d.pop("body", UNSET)

        _due_date = d.pop("due_date", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        head = d.pop("head", UNSET)

        labels = cast(List[int], d.pop("labels", UNSET))

        milestone = d.pop("milestone", UNSET)

        title = d.pop("title", UNSET)

        create_pull_request_option = cls(
            assignee=assignee,
            assignees=assignees,
            base=base,
            body=body,
            due_date=due_date,
            head=head,
            labels=labels,
            milestone=milestone,
            title=title,
        )

        create_pull_request_option.additional_properties = d
        return create_pull_request_option

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
