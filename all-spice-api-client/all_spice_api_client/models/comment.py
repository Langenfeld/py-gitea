import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="Comment")


@attr.s(auto_attribs=True)
class Comment:
    """Comment represents a comment on a commit or issue

    Attributes:
        body (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        html_url (Union[Unset, str]):
        id (Union[Unset, int]):
        issue_url (Union[Unset, str]):
        original_author (Union[Unset, str]):
        original_author_id (Union[Unset, int]):
        pull_request_url (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        user (Union[Unset, User]): User represents a user
    """

    body: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    issue_url: Union[Unset, str] = UNSET
    original_author: Union[Unset, str] = UNSET
    original_author_id: Union[Unset, int] = UNSET
    pull_request_url: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, "User"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        html_url = self.html_url
        id = self.id
        issue_url = self.issue_url
        original_author = self.original_author
        original_author_id = self.original_author_id
        pull_request_url = self.pull_request_url
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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if issue_url is not UNSET:
            field_dict["issue_url"] = issue_url
        if original_author is not UNSET:
            field_dict["original_author"] = original_author
        if original_author_id is not UNSET:
            field_dict["original_author_id"] = original_author_id
        if pull_request_url is not UNSET:
            field_dict["pull_request_url"] = pull_request_url
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

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        issue_url = d.pop("issue_url", UNSET)

        original_author = d.pop("original_author", UNSET)

        original_author_id = d.pop("original_author_id", UNSET)

        pull_request_url = d.pop("pull_request_url", UNSET)

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

        comment = cls(
            body=body,
            created_at=created_at,
            html_url=html_url,
            id=id,
            issue_url=issue_url,
            original_author=original_author,
            original_author_id=original_author_id,
            pull_request_url=pull_request_url,
            updated_at=updated_at,
            user=user,
        )

        comment.additional_properties = d
        return comment

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
