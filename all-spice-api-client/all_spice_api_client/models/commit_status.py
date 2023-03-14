import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="CommitStatus")


@attr.s(auto_attribs=True)
class CommitStatus:
    """CommitStatus holds a single status of a single Commit

    Attributes:
        context (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        creator (Union[Unset, User]): User represents a user
        description (Union[Unset, str]):
        id (Union[Unset, int]):
        status (Union[Unset, str]): CommitStatusState holds the state of a CommitStatus
            It can be "pending", "success", "error", "failure", and "warning"
        target_url (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        url (Union[Unset, str]):
    """

    context: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    creator: Union[Unset, "User"] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    target_url: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        creator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        description = self.description
        id = self.id
        status = self.status
        target_url = self.target_url
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context is not UNSET:
            field_dict["context"] = context
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if creator is not UNSET:
            field_dict["creator"] = creator
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if target_url is not UNSET:
            field_dict["target_url"] = target_url
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user import User

        d = src_dict.copy()
        context = d.pop("context", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _creator = d.pop("creator", UNSET)
        creator: Union[Unset, User]
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = User.from_dict(_creator)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        target_url = d.pop("target_url", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        url = d.pop("url", UNSET)

        commit_status = cls(
            context=context,
            created_at=created_at,
            creator=creator,
            description=description,
            id=id,
            status=status,
            target_url=target_url,
            updated_at=updated_at,
            url=url,
        )

        commit_status.additional_properties = d
        return commit_status

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
