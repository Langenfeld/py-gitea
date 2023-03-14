import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository import Repository


T = TypeVar("T", bound="DeployKey")


@attr.s(auto_attribs=True)
class DeployKey:
    """DeployKey a deploy key

    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        fingerprint (Union[Unset, str]):
        id (Union[Unset, int]):
        key (Union[Unset, str]):
        key_id (Union[Unset, int]):
        read_only (Union[Unset, bool]):
        repository (Union[Unset, Repository]): Repository represents a repository
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    fingerprint: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    key: Union[Unset, str] = UNSET
    key_id: Union[Unset, int] = UNSET
    read_only: Union[Unset, bool] = UNSET
    repository: Union[Unset, "Repository"] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        fingerprint = self.fingerprint
        id = self.id
        key = self.key
        key_id = self.key_id
        read_only = self.read_only
        repository: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        title = self.title
        url = self.url

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
        if key_id is not UNSET:
            field_dict["key_id"] = key_id
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if repository is not UNSET:
            field_dict["repository"] = repository
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.repository import Repository

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

        key_id = d.pop("key_id", UNSET)

        read_only = d.pop("read_only", UNSET)

        _repository = d.pop("repository", UNSET)
        repository: Union[Unset, Repository]
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        deploy_key = cls(
            created_at=created_at,
            fingerprint=fingerprint,
            id=id,
            key=key,
            key_id=key_id,
            read_only=read_only,
            repository=repository,
            title=title,
            url=url,
        )

        deploy_key.additional_properties = d
        return deploy_key

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
