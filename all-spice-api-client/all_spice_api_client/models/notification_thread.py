import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_subject import NotificationSubject
    from ..models.repository import Repository


T = TypeVar("T", bound="NotificationThread")


@attr.s(auto_attribs=True)
class NotificationThread:
    """NotificationThread expose Notification on API

    Attributes:
        id (Union[Unset, int]):
        pinned (Union[Unset, bool]):
        repository (Union[Unset, Repository]): Repository represents a repository
        subject (Union[Unset, NotificationSubject]): NotificationSubject contains the notification subject
            (Issue/Pull/Commit)
        unread (Union[Unset, bool]):
        updated_at (Union[Unset, datetime.datetime]):
        url (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    pinned: Union[Unset, bool] = UNSET
    repository: Union[Unset, "Repository"] = UNSET
    subject: Union[Unset, "NotificationSubject"] = UNSET
    unread: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        pinned = self.pinned
        repository: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        subject: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject.to_dict()

        unread = self.unread
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if pinned is not UNSET:
            field_dict["pinned"] = pinned
        if repository is not UNSET:
            field_dict["repository"] = repository
        if subject is not UNSET:
            field_dict["subject"] = subject
        if unread is not UNSET:
            field_dict["unread"] = unread
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_subject import NotificationSubject
        from ..models.repository import Repository

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        pinned = d.pop("pinned", UNSET)

        _repository = d.pop("repository", UNSET)
        repository: Union[Unset, Repository]
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        _subject = d.pop("subject", UNSET)
        subject: Union[Unset, NotificationSubject]
        if isinstance(_subject, Unset):
            subject = UNSET
        else:
            subject = NotificationSubject.from_dict(_subject)

        unread = d.pop("unread", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        url = d.pop("url", UNSET)

        notification_thread = cls(
            id=id,
            pinned=pinned,
            repository=repository,
            subject=subject,
            unread=unread,
            updated_at=updated_at,
            url=url,
        )

        notification_thread.additional_properties = d
        return notification_thread

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
