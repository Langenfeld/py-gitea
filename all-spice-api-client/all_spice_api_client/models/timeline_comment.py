import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment import Comment
    from ..models.issue import Issue
    from ..models.label import Label
    from ..models.milestone import Milestone
    from ..models.team import Team
    from ..models.tracked_time import TrackedTime
    from ..models.user import User


T = TypeVar("T", bound="TimelineComment")


@attr.s(auto_attribs=True)
class TimelineComment:
    """TimelineComment represents a timeline comment (comment of any type) on a commit or issue

    Attributes:
        assignee (Union[Unset, User]): User represents a user
        assignee_team (Union[Unset, Team]): Team represents a team in an organization
        body (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        dependent_issue (Union[Unset, Issue]): Issue represents an issue in a repository
        html_url (Union[Unset, str]):
        id (Union[Unset, int]):
        issue_url (Union[Unset, str]):
        label (Union[Unset, Label]): Label a label to an issue or a pr
        milestone (Union[Unset, Milestone]): Milestone milestone is a collection of issues on one repository
        new_ref (Union[Unset, str]):
        new_title (Union[Unset, str]):
        old_milestone (Union[Unset, Milestone]): Milestone milestone is a collection of issues on one repository
        old_project_id (Union[Unset, int]):
        old_ref (Union[Unset, str]):
        old_title (Union[Unset, str]):
        project_id (Union[Unset, int]):
        pull_request_url (Union[Unset, str]):
        ref_action (Union[Unset, str]):
        ref_comment (Union[Unset, Comment]): Comment represents a comment on a commit or issue
        ref_commit_sha (Union[Unset, str]): commit SHA where issue/PR was referenced
        ref_issue (Union[Unset, Issue]): Issue represents an issue in a repository
        removed_assignee (Union[Unset, bool]): whether the assignees were removed or added
        resolve_doer (Union[Unset, User]): User represents a user
        review_id (Union[Unset, int]):
        tracked_time (Union[Unset, TrackedTime]): TrackedTime worked time for an issue / pr
        type (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        user (Union[Unset, User]): User represents a user
    """

    assignee: Union[Unset, "User"] = UNSET
    assignee_team: Union[Unset, "Team"] = UNSET
    body: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    dependent_issue: Union[Unset, "Issue"] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    issue_url: Union[Unset, str] = UNSET
    label: Union[Unset, "Label"] = UNSET
    milestone: Union[Unset, "Milestone"] = UNSET
    new_ref: Union[Unset, str] = UNSET
    new_title: Union[Unset, str] = UNSET
    old_milestone: Union[Unset, "Milestone"] = UNSET
    old_project_id: Union[Unset, int] = UNSET
    old_ref: Union[Unset, str] = UNSET
    old_title: Union[Unset, str] = UNSET
    project_id: Union[Unset, int] = UNSET
    pull_request_url: Union[Unset, str] = UNSET
    ref_action: Union[Unset, str] = UNSET
    ref_comment: Union[Unset, "Comment"] = UNSET
    ref_commit_sha: Union[Unset, str] = UNSET
    ref_issue: Union[Unset, "Issue"] = UNSET
    removed_assignee: Union[Unset, bool] = UNSET
    resolve_doer: Union[Unset, "User"] = UNSET
    review_id: Union[Unset, int] = UNSET
    tracked_time: Union[Unset, "TrackedTime"] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, "User"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        assignee_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee_team, Unset):
            assignee_team = self.assignee_team.to_dict()

        body = self.body
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        dependent_issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dependent_issue, Unset):
            dependent_issue = self.dependent_issue.to_dict()

        html_url = self.html_url
        id = self.id
        issue_url = self.issue_url
        label: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()

        milestone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.milestone, Unset):
            milestone = self.milestone.to_dict()

        new_ref = self.new_ref
        new_title = self.new_title
        old_milestone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.old_milestone, Unset):
            old_milestone = self.old_milestone.to_dict()

        old_project_id = self.old_project_id
        old_ref = self.old_ref
        old_title = self.old_title
        project_id = self.project_id
        pull_request_url = self.pull_request_url
        ref_action = self.ref_action
        ref_comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ref_comment, Unset):
            ref_comment = self.ref_comment.to_dict()

        ref_commit_sha = self.ref_commit_sha
        ref_issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ref_issue, Unset):
            ref_issue = self.ref_issue.to_dict()

        removed_assignee = self.removed_assignee
        resolve_doer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resolve_doer, Unset):
            resolve_doer = self.resolve_doer.to_dict()

        review_id = self.review_id
        tracked_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tracked_time, Unset):
            tracked_time = self.tracked_time.to_dict()

        type = self.type
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if assignee_team is not UNSET:
            field_dict["assignee_team"] = assignee_team
        if body is not UNSET:
            field_dict["body"] = body
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if dependent_issue is not UNSET:
            field_dict["dependent_issue"] = dependent_issue
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if issue_url is not UNSET:
            field_dict["issue_url"] = issue_url
        if label is not UNSET:
            field_dict["label"] = label
        if milestone is not UNSET:
            field_dict["milestone"] = milestone
        if new_ref is not UNSET:
            field_dict["new_ref"] = new_ref
        if new_title is not UNSET:
            field_dict["new_title"] = new_title
        if old_milestone is not UNSET:
            field_dict["old_milestone"] = old_milestone
        if old_project_id is not UNSET:
            field_dict["old_project_id"] = old_project_id
        if old_ref is not UNSET:
            field_dict["old_ref"] = old_ref
        if old_title is not UNSET:
            field_dict["old_title"] = old_title
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if pull_request_url is not UNSET:
            field_dict["pull_request_url"] = pull_request_url
        if ref_action is not UNSET:
            field_dict["ref_action"] = ref_action
        if ref_comment is not UNSET:
            field_dict["ref_comment"] = ref_comment
        if ref_commit_sha is not UNSET:
            field_dict["ref_commit_sha"] = ref_commit_sha
        if ref_issue is not UNSET:
            field_dict["ref_issue"] = ref_issue
        if removed_assignee is not UNSET:
            field_dict["removed_assignee"] = removed_assignee
        if resolve_doer is not UNSET:
            field_dict["resolve_doer"] = resolve_doer
        if review_id is not UNSET:
            field_dict["review_id"] = review_id
        if tracked_time is not UNSET:
            field_dict["tracked_time"] = tracked_time
        if type is not UNSET:
            field_dict["type"] = type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comment import Comment
        from ..models.issue import Issue
        from ..models.label import Label
        from ..models.milestone import Milestone
        from ..models.team import Team
        from ..models.tracked_time import TrackedTime
        from ..models.user import User

        d = src_dict.copy()
        _assignee = d.pop("assignee", UNSET)
        assignee: Union[Unset, User]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = User.from_dict(_assignee)

        _assignee_team = d.pop("assignee_team", UNSET)
        assignee_team: Union[Unset, Team]
        if isinstance(_assignee_team, Unset):
            assignee_team = UNSET
        else:
            assignee_team = Team.from_dict(_assignee_team)

        body = d.pop("body", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _dependent_issue = d.pop("dependent_issue", UNSET)
        dependent_issue: Union[Unset, Issue]
        if isinstance(_dependent_issue, Unset):
            dependent_issue = UNSET
        else:
            dependent_issue = Issue.from_dict(_dependent_issue)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        issue_url = d.pop("issue_url", UNSET)

        _label = d.pop("label", UNSET)
        label: Union[Unset, Label]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = Label.from_dict(_label)

        _milestone = d.pop("milestone", UNSET)
        milestone: Union[Unset, Milestone]
        if isinstance(_milestone, Unset):
            milestone = UNSET
        else:
            milestone = Milestone.from_dict(_milestone)

        new_ref = d.pop("new_ref", UNSET)

        new_title = d.pop("new_title", UNSET)

        _old_milestone = d.pop("old_milestone", UNSET)
        old_milestone: Union[Unset, Milestone]
        if isinstance(_old_milestone, Unset):
            old_milestone = UNSET
        else:
            old_milestone = Milestone.from_dict(_old_milestone)

        old_project_id = d.pop("old_project_id", UNSET)

        old_ref = d.pop("old_ref", UNSET)

        old_title = d.pop("old_title", UNSET)

        project_id = d.pop("project_id", UNSET)

        pull_request_url = d.pop("pull_request_url", UNSET)

        ref_action = d.pop("ref_action", UNSET)

        _ref_comment = d.pop("ref_comment", UNSET)
        ref_comment: Union[Unset, Comment]
        if isinstance(_ref_comment, Unset):
            ref_comment = UNSET
        else:
            ref_comment = Comment.from_dict(_ref_comment)

        ref_commit_sha = d.pop("ref_commit_sha", UNSET)

        _ref_issue = d.pop("ref_issue", UNSET)
        ref_issue: Union[Unset, Issue]
        if isinstance(_ref_issue, Unset):
            ref_issue = UNSET
        else:
            ref_issue = Issue.from_dict(_ref_issue)

        removed_assignee = d.pop("removed_assignee", UNSET)

        _resolve_doer = d.pop("resolve_doer", UNSET)
        resolve_doer: Union[Unset, User]
        if isinstance(_resolve_doer, Unset):
            resolve_doer = UNSET
        else:
            resolve_doer = User.from_dict(_resolve_doer)

        review_id = d.pop("review_id", UNSET)

        _tracked_time = d.pop("tracked_time", UNSET)
        tracked_time: Union[Unset, TrackedTime]
        if isinstance(_tracked_time, Unset):
            tracked_time = UNSET
        else:
            tracked_time = TrackedTime.from_dict(_tracked_time)

        type = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        timeline_comment = cls(
            assignee=assignee,
            assignee_team=assignee_team,
            body=body,
            created_at=created_at,
            dependent_issue=dependent_issue,
            html_url=html_url,
            id=id,
            issue_url=issue_url,
            label=label,
            milestone=milestone,
            new_ref=new_ref,
            new_title=new_title,
            old_milestone=old_milestone,
            old_project_id=old_project_id,
            old_ref=old_ref,
            old_title=old_title,
            project_id=project_id,
            pull_request_url=pull_request_url,
            ref_action=ref_action,
            ref_comment=ref_comment,
            ref_commit_sha=ref_commit_sha,
            ref_issue=ref_issue,
            removed_assignee=removed_assignee,
            resolve_doer=resolve_doer,
            review_id=review_id,
            tracked_time=tracked_time,
            type=type,
            updated_at=updated_at,
            user=user,
        )

        timeline_comment.additional_properties = d
        return timeline_comment

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
