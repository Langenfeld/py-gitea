import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="PullReviewComment")


@attr.s(auto_attribs=True)
class PullReviewComment:
    """PullReviewComment represents a comment on a pull request review

    Attributes:
        body (Union[Unset, str]):
        commit_id (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        diff_hunk (Union[Unset, str]):
        html_url (Union[Unset, str]):
        id (Union[Unset, int]):
        original_commit_id (Union[Unset, str]):
        original_position (Union[Unset, int]):
        path (Union[Unset, str]):
        position (Union[Unset, int]):
        pull_request_review_id (Union[Unset, int]):
        pull_request_url (Union[Unset, str]):
        resolver (Union[Unset, User]): User represents a user
        updated_at (Union[Unset, datetime.datetime]):
        user (Union[Unset, User]): User represents a user
    """

    body: Union[Unset, str] = UNSET
    commit_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    diff_hunk: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    original_commit_id: Union[Unset, str] = UNSET
    original_position: Union[Unset, int] = UNSET
    path: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    pull_request_review_id: Union[Unset, int] = UNSET
    pull_request_url: Union[Unset, str] = UNSET
    resolver: Union[Unset, "User"] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, "User"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        commit_id = self.commit_id
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        diff_hunk = self.diff_hunk
        html_url = self.html_url
        id = self.id
        original_commit_id = self.original_commit_id
        original_position = self.original_position
        path = self.path
        position = self.position
        pull_request_review_id = self.pull_request_review_id
        pull_request_url = self.pull_request_url
        resolver: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resolver, Unset):
            resolver = self.resolver.to_dict()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if commit_id is not UNSET:
            field_dict["commit_id"] = commit_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if diff_hunk is not UNSET:
            field_dict["diff_hunk"] = diff_hunk
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if original_commit_id is not UNSET:
            field_dict["original_commit_id"] = original_commit_id
        if original_position is not UNSET:
            field_dict["original_position"] = original_position
        if path is not UNSET:
            field_dict["path"] = path
        if position is not UNSET:
            field_dict["position"] = position
        if pull_request_review_id is not UNSET:
            field_dict["pull_request_review_id"] = pull_request_review_id
        if pull_request_url is not UNSET:
            field_dict["pull_request_url"] = pull_request_url
        if resolver is not UNSET:
            field_dict["resolver"] = resolver
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user import User

        d = src_dict.copy()
        body = d.pop("body", UNSET)

        commit_id = d.pop("commit_id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        diff_hunk = d.pop("diff_hunk", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        original_commit_id = d.pop("original_commit_id", UNSET)

        original_position = d.pop("original_position", UNSET)

        path = d.pop("path", UNSET)

        position = d.pop("position", UNSET)

        pull_request_review_id = d.pop("pull_request_review_id", UNSET)

        pull_request_url = d.pop("pull_request_url", UNSET)

        _resolver = d.pop("resolver", UNSET)
        resolver: Union[Unset, User]
        if isinstance(_resolver, Unset):
            resolver = UNSET
        else:
            resolver = User.from_dict(_resolver)

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

        pull_review_comment = cls(
            body=body,
            commit_id=commit_id,
            created_at=created_at,
            diff_hunk=diff_hunk,
            html_url=html_url,
            id=id,
            original_commit_id=original_commit_id,
            original_position=original_position,
            path=path,
            position=position,
            pull_request_review_id=pull_request_review_id,
            pull_request_url=pull_request_url,
            resolver=resolver,
            updated_at=updated_at,
            user=user,
        )

        pull_review_comment.additional_properties = d
        return pull_review_comment

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
