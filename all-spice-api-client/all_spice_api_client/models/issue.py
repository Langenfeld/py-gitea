import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label import Label
    from ..models.milestone import Milestone
    from ..models.pull_request_meta import PullRequestMeta
    from ..models.repository_meta import RepositoryMeta
    from ..models.user import User


T = TypeVar("T", bound="Issue")


@attr.s(auto_attribs=True)
class Issue:
    """Issue represents an issue in a repository

    Attributes:
        assignee (Union[Unset, User]): User represents a user
        assignees (Union[Unset, List['User']]):
        body (Union[Unset, str]):
        closed_at (Union[Unset, datetime.datetime]):
        comments (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        due_date (Union[Unset, datetime.datetime]):
        html_url (Union[Unset, str]):
        id (Union[Unset, int]):
        is_locked (Union[Unset, bool]):
        labels (Union[Unset, List['Label']]):
        milestone (Union[Unset, Milestone]): Milestone milestone is a collection of issues on one repository
        number (Union[Unset, int]):
        original_author (Union[Unset, str]):
        original_author_id (Union[Unset, int]):
        pull_request (Union[Unset, PullRequestMeta]): PullRequestMeta PR info if an issue is a PR
        ref (Union[Unset, str]):
        repository (Union[Unset, RepositoryMeta]): RepositoryMeta basic repository information
        state (Union[Unset, str]): StateType issue state type
        title (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        url (Union[Unset, str]):
        user (Union[Unset, User]): User represents a user
    """

    assignee: Union[Unset, "User"] = UNSET
    assignees: Union[Unset, List["User"]] = UNSET
    body: Union[Unset, str] = UNSET
    closed_at: Union[Unset, datetime.datetime] = UNSET
    comments: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_locked: Union[Unset, bool] = UNSET
    labels: Union[Unset, List["Label"]] = UNSET
    milestone: Union[Unset, "Milestone"] = UNSET
    number: Union[Unset, int] = UNSET
    original_author: Union[Unset, str] = UNSET
    original_author_id: Union[Unset, int] = UNSET
    pull_request: Union[Unset, "PullRequestMeta"] = UNSET
    ref: Union[Unset, str] = UNSET
    repository: Union[Unset, "RepositoryMeta"] = UNSET
    state: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    url: Union[Unset, str] = UNSET
    user: Union[Unset, "User"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        assignees: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.assignees, Unset):
            assignees = []
            for assignees_item_data in self.assignees:
                assignees_item = assignees_item_data.to_dict()

                assignees.append(assignees_item)

        body = self.body
        closed_at: Union[Unset, str] = UNSET
        if not isinstance(self.closed_at, Unset):
            closed_at = self.closed_at.isoformat()

        comments = self.comments
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        html_url = self.html_url
        id = self.id
        is_locked = self.is_locked
        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        milestone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.milestone, Unset):
            milestone = self.milestone.to_dict()

        number = self.number
        original_author = self.original_author
        original_author_id = self.original_author_id
        pull_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pull_request, Unset):
            pull_request = self.pull_request.to_dict()

        ref = self.ref
        repository: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

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
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if assignees is not UNSET:
            field_dict["assignees"] = assignees
        if body is not UNSET:
            field_dict["body"] = body
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if comments is not UNSET:
            field_dict["comments"] = comments
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if is_locked is not UNSET:
            field_dict["is_locked"] = is_locked
        if labels is not UNSET:
            field_dict["labels"] = labels
        if milestone is not UNSET:
            field_dict["milestone"] = milestone
        if number is not UNSET:
            field_dict["number"] = number
        if original_author is not UNSET:
            field_dict["original_author"] = original_author
        if original_author_id is not UNSET:
            field_dict["original_author_id"] = original_author_id
        if pull_request is not UNSET:
            field_dict["pull_request"] = pull_request
        if ref is not UNSET:
            field_dict["ref"] = ref
        if repository is not UNSET:
            field_dict["repository"] = repository
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
        from ..models.pull_request_meta import PullRequestMeta
        from ..models.repository_meta import RepositoryMeta
        from ..models.user import User

        d = src_dict.copy()
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

        _due_date = d.pop("due_date", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        is_locked = d.pop("is_locked", UNSET)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = Label.from_dict(labels_item_data)

            labels.append(labels_item)

        _milestone = d.pop("milestone", UNSET)
        milestone: Union[Unset, Milestone]
        if isinstance(_milestone, Unset):
            milestone = UNSET
        else:
            milestone = Milestone.from_dict(_milestone)

        number = d.pop("number", UNSET)

        original_author = d.pop("original_author", UNSET)

        original_author_id = d.pop("original_author_id", UNSET)

        _pull_request = d.pop("pull_request", UNSET)
        pull_request: Union[Unset, PullRequestMeta]
        if isinstance(_pull_request, Unset):
            pull_request = UNSET
        else:
            pull_request = PullRequestMeta.from_dict(_pull_request)

        ref = d.pop("ref", UNSET)

        _repository = d.pop("repository", UNSET)
        repository: Union[Unset, RepositoryMeta]
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = RepositoryMeta.from_dict(_repository)

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

        issue = cls(
            assignee=assignee,
            assignees=assignees,
            body=body,
            closed_at=closed_at,
            comments=comments,
            created_at=created_at,
            due_date=due_date,
            html_url=html_url,
            id=id,
            is_locked=is_locked,
            labels=labels,
            milestone=milestone,
            number=number,
            original_author=original_author,
            original_author_id=original_author_id,
            pull_request=pull_request,
            ref=ref,
            repository=repository,
            state=state,
            title=title,
            updated_at=updated_at,
            url=url,
            user=user,
        )

        issue.additional_properties = d
        return issue

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
