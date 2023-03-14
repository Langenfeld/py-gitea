import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team import Team
    from ..models.user import User


T = TypeVar("T", bound="PullReview")


@attr.s(auto_attribs=True)
class PullReview:
    """PullReview represents a pull request review

    Attributes:
        body (Union[Unset, str]):
        comments_count (Union[Unset, int]):
        commit_id (Union[Unset, str]):
        dismissed (Union[Unset, bool]):
        html_url (Union[Unset, str]):
        id (Union[Unset, int]):
        official (Union[Unset, bool]):
        pull_request_url (Union[Unset, str]):
        stale (Union[Unset, bool]):
        state (Union[Unset, str]): ReviewStateType review state type
        submitted_at (Union[Unset, datetime.datetime]):
        team (Union[Unset, Team]): Team represents a team in an organization
        user (Union[Unset, User]): User represents a user
    """

    body: Union[Unset, str] = UNSET
    comments_count: Union[Unset, int] = UNSET
    commit_id: Union[Unset, str] = UNSET
    dismissed: Union[Unset, bool] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    official: Union[Unset, bool] = UNSET
    pull_request_url: Union[Unset, str] = UNSET
    stale: Union[Unset, bool] = UNSET
    state: Union[Unset, str] = UNSET
    submitted_at: Union[Unset, datetime.datetime] = UNSET
    team: Union[Unset, "Team"] = UNSET
    user: Union[Unset, "User"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        comments_count = self.comments_count
        commit_id = self.commit_id
        dismissed = self.dismissed
        html_url = self.html_url
        id = self.id
        official = self.official
        pull_request_url = self.pull_request_url
        stale = self.stale
        state = self.state
        submitted_at: Union[Unset, str] = UNSET
        if not isinstance(self.submitted_at, Unset):
            submitted_at = self.submitted_at.isoformat()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if comments_count is not UNSET:
            field_dict["comments_count"] = comments_count
        if commit_id is not UNSET:
            field_dict["commit_id"] = commit_id
        if dismissed is not UNSET:
            field_dict["dismissed"] = dismissed
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if official is not UNSET:
            field_dict["official"] = official
        if pull_request_url is not UNSET:
            field_dict["pull_request_url"] = pull_request_url
        if stale is not UNSET:
            field_dict["stale"] = stale
        if state is not UNSET:
            field_dict["state"] = state
        if submitted_at is not UNSET:
            field_dict["submitted_at"] = submitted_at
        if team is not UNSET:
            field_dict["team"] = team
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team import Team
        from ..models.user import User

        d = src_dict.copy()
        body = d.pop("body", UNSET)

        comments_count = d.pop("comments_count", UNSET)

        commit_id = d.pop("commit_id", UNSET)

        dismissed = d.pop("dismissed", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        official = d.pop("official", UNSET)

        pull_request_url = d.pop("pull_request_url", UNSET)

        stale = d.pop("stale", UNSET)

        state = d.pop("state", UNSET)

        _submitted_at = d.pop("submitted_at", UNSET)
        submitted_at: Union[Unset, datetime.datetime]
        if isinstance(_submitted_at, Unset):
            submitted_at = UNSET
        else:
            submitted_at = isoparse(_submitted_at)

        _team = d.pop("team", UNSET)
        team: Union[Unset, Team]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Team.from_dict(_team)

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        pull_review = cls(
            body=body,
            comments_count=comments_count,
            commit_id=commit_id,
            dismissed=dismissed,
            html_url=html_url,
            id=id,
            official=official,
            pull_request_url=pull_request_url,
            stale=stale,
            state=state,
            submitted_at=submitted_at,
            team=team,
            user=user,
        )

        pull_review.additional_properties = d
        return pull_review

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
