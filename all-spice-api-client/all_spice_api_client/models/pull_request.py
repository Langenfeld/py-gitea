import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label import Label
    from ..models.milestone import Milestone
    from ..models.pr_branch_info import PRBranchInfo
    from ..models.user import User


T = TypeVar("T", bound="PullRequest")


@attr.s(auto_attribs=True)
class PullRequest:
    """PullRequest represents a pull request

    Attributes:
        allow_maintainer_edit (Union[Unset, bool]):
        assignee (Union[Unset, User]): User represents a user
        assignees (Union[Unset, List['User']]):
        base (Union[Unset, PRBranchInfo]): PRBranchInfo information about a branch
        body (Union[Unset, str]):
        closed_at (Union[Unset, datetime.datetime]):
        comments (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        diff_url (Union[Unset, str]):
        due_date (Union[Unset, datetime.datetime]):
        head (Union[Unset, PRBranchInfo]): PRBranchInfo information about a branch
        html_url (Union[Unset, str]):
        id (Union[Unset, int]):
        is_locked (Union[Unset, bool]):
        labels (Union[Unset, List['Label']]):
        merge_base (Union[Unset, str]):
        merge_commit_sha (Union[Unset, str]):
        mergeable (Union[Unset, bool]):
        merged (Union[Unset, bool]):
        merged_at (Union[Unset, datetime.datetime]):
        merged_by (Union[Unset, User]): User represents a user
        milestone (Union[Unset, Milestone]): Milestone milestone is a collection of issues on one repository
        number (Union[Unset, int]):
        patch_url (Union[Unset, str]):
        state (Union[Unset, str]): StateType issue state type
        title (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        url (Union[Unset, str]):
        user (Union[Unset, User]): User represents a user
    """

    allow_maintainer_edit: Union[Unset, bool] = UNSET
    assignee: Union[Unset, "User"] = UNSET
    assignees: Union[Unset, List["User"]] = UNSET
    base: Union[Unset, "PRBranchInfo"] = UNSET
    body: Union[Unset, str] = UNSET
    closed_at: Union[Unset, datetime.datetime] = UNSET
    comments: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    diff_url: Union[Unset, str] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    head: Union[Unset, "PRBranchInfo"] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_locked: Union[Unset, bool] = UNSET
    labels: Union[Unset, List["Label"]] = UNSET
    merge_base: Union[Unset, str] = UNSET
    merge_commit_sha: Union[Unset, str] = UNSET
    mergeable: Union[Unset, bool] = UNSET
    merged: Union[Unset, bool] = UNSET
    merged_at: Union[Unset, datetime.datetime] = UNSET
    merged_by: Union[Unset, "User"] = UNSET
    milestone: Union[Unset, "Milestone"] = UNSET
    number: Union[Unset, int] = UNSET
    patch_url: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    url: Union[Unset, str] = UNSET
    user: Union[Unset, "User"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_maintainer_edit = self.allow_maintainer_edit
        assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        assignees: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.assignees, Unset):
            assignees = []
            for assignees_item_data in self.assignees:
                assignees_item = assignees_item_data.to_dict()

                assignees.append(assignees_item)

        base: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.base, Unset):
            base = self.base.to_dict()

        body = self.body
        closed_at: Union[Unset, str] = UNSET
        if not isinstance(self.closed_at, Unset):
            closed_at = self.closed_at.isoformat()

        comments = self.comments
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        diff_url = self.diff_url
        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        head: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.head, Unset):
            head = self.head.to_dict()

        html_url = self.html_url
        id = self.id
        is_locked = self.is_locked
        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        merge_base = self.merge_base
        merge_commit_sha = self.merge_commit_sha
        mergeable = self.mergeable
        merged = self.merged
        merged_at: Union[Unset, str] = UNSET
        if not isinstance(self.merged_at, Unset):
            merged_at = self.merged_at.isoformat()

        merged_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.merged_by, Unset):
            merged_by = self.merged_by.to_dict()

        milestone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.milestone, Unset):
            milestone = self.milestone.to_dict()

        number = self.number
        patch_url = self.patch_url
        state = self.state
        title = self.title
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        url = self.url
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_maintainer_edit is not UNSET:
            field_dict["allow_maintainer_edit"] = allow_maintainer_edit
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if assignees is not UNSET:
            field_dict["assignees"] = assignees
        if base is not UNSET:
            field_dict["base"] = base
        if body is not UNSET:
            field_dict["body"] = body
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if comments is not UNSET:
            field_dict["comments"] = comments
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if diff_url is not UNSET:
            field_dict["diff_url"] = diff_url
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if head is not UNSET:
            field_dict["head"] = head
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if is_locked is not UNSET:
            field_dict["is_locked"] = is_locked
        if labels is not UNSET:
            field_dict["labels"] = labels
        if merge_base is not UNSET:
            field_dict["merge_base"] = merge_base
        if merge_commit_sha is not UNSET:
            field_dict["merge_commit_sha"] = merge_commit_sha
        if mergeable is not UNSET:
            field_dict["mergeable"] = mergeable
        if merged is not UNSET:
            field_dict["merged"] = merged
        if merged_at is not UNSET:
            field_dict["merged_at"] = merged_at
        if merged_by is not UNSET:
            field_dict["merged_by"] = merged_by
        if milestone is not UNSET:
            field_dict["milestone"] = milestone
        if number is not UNSET:
            field_dict["number"] = number
        if patch_url is not UNSET:
            field_dict["patch_url"] = patch_url
        if state is not UNSET:
            field_dict["state"] = state
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.label import Label
        from ..models.milestone import Milestone
        from ..models.pr_branch_info import PRBranchInfo
        from ..models.user import User

        d = src_dict.copy()
        allow_maintainer_edit = d.pop("allow_maintainer_edit", UNSET)

        _assignee = d.pop("assignee", UNSET)
        assignee: Union[Unset, User]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = User.from_dict(_assignee)

        assignees = []
        _assignees = d.pop("assignees", UNSET)
        for assignees_item_data in _assignees or []:
            assignees_item = User.from_dict(assignees_item_data)

            assignees.append(assignees_item)

        _base = d.pop("base", UNSET)
        base: Union[Unset, PRBranchInfo]
        if isinstance(_base, Unset):
            base = UNSET
        else:
            base = PRBranchInfo.from_dict(_base)

        body = d.pop("body", UNSET)

        _closed_at = d.pop("closed_at", UNSET)
        closed_at: Union[Unset, datetime.datetime]
        if isinstance(_closed_at, Unset):
            closed_at = UNSET
        else:
            closed_at = isoparse(_closed_at)

        comments = d.pop("comments", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        diff_url = d.pop("diff_url", UNSET)

        _due_date = d.pop("due_date", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        _head = d.pop("head", UNSET)
        head: Union[Unset, PRBranchInfo]
        if isinstance(_head, Unset):
            head = UNSET
        else:
            head = PRBranchInfo.from_dict(_head)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        is_locked = d.pop("is_locked", UNSET)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = Label.from_dict(labels_item_data)

            labels.append(labels_item)

        merge_base = d.pop("merge_base", UNSET)

        merge_commit_sha = d.pop("merge_commit_sha", UNSET)

        mergeable = d.pop("mergeable", UNSET)

        merged = d.pop("merged", UNSET)

        _merged_at = d.pop("merged_at", UNSET)
        merged_at: Union[Unset, datetime.datetime]
        if isinstance(_merged_at, Unset):
            merged_at = UNSET
        else:
            merged_at = isoparse(_merged_at)

        _merged_by = d.pop("merged_by", UNSET)
        merged_by: Union[Unset, User]
        if isinstance(_merged_by, Unset):
            merged_by = UNSET
        else:
            merged_by = User.from_dict(_merged_by)

        _milestone = d.pop("milestone", UNSET)
        milestone: Union[Unset, Milestone]
        if isinstance(_milestone, Unset):
            milestone = UNSET
        else:
            milestone = Milestone.from_dict(_milestone)

        number = d.pop("number", UNSET)

        patch_url = d.pop("patch_url", UNSET)

        state = d.pop("state", UNSET)

        title = d.pop("title", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        url = d.pop("url", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        pull_request = cls(
            allow_maintainer_edit=allow_maintainer_edit,
            assignee=assignee,
            assignees=assignees,
            base=base,
            body=body,
            closed_at=closed_at,
            comments=comments,
            created_at=created_at,
            diff_url=diff_url,
            due_date=due_date,
            head=head,
            html_url=html_url,
            id=id,
            is_locked=is_locked,
            labels=labels,
            merge_base=merge_base,
            merge_commit_sha=merge_commit_sha,
            mergeable=mergeable,
            merged=merged,
            merged_at=merged_at,
            merged_by=merged_by,
            milestone=milestone,
            number=number,
            patch_url=patch_url,
            state=state,
            title=title,
            updated_at=updated_at,
            url=url,
            user=user,
        )

        pull_request.additional_properties = d
        return pull_request

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
