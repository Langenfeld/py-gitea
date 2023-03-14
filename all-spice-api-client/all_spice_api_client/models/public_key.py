import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="PublicKey")


@attr.s(auto_attribs=True)
class PublicKey:
    """PublicKey publickey is a user key to push code to repository

    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        fingerprint (Union[Unset, str]):
        id (Union[Unset, int]):
        key (Union[Unset, str]):
        key_type (Union[Unset, str]):
        read_only (Union[Unset, bool]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
        user (Union[Unset, User]): User represents a user
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    fingerprint: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    key: Union[Unset, str] = UNSET
    key_type: Union[Unset, str] = UNSET
    read_only: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    user: Union[Unset, "User"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        fingerprint = self.fingerprint
        id = self.id
        key = self.key
        key_type = self.key_type
        read_only = self.read_only
        title = self.title
        url = self.url
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user import User

        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        fingerprint = d.pop("fingerprint", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        key_type = d.pop("key_type", UNSET)

        read_only = d.pop("read_only", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        public_key = cls(
            created_at=created_at,
            fingerprint=fingerprint,
            id=id,
            key=key,
            key_type=key_type,
            read_only=read_only,
            title=title,
            url=url,
            user=user,
        )

        public_key.additional_properties = d
        return public_key

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
