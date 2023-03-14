import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopicResponse")


@attr.s(auto_attribs=True)
class TopicResponse:
    """TopicResponse for returning topics

    Attributes:
        created (Union[Unset, datetime.datetime]):
        id (Union[Unset, int]):
        repo_count (Union[Unset, int]):
        topic_name (Union[Unset, str]):
        updated (Union[Unset, datetime.datetime]):
    """

    created: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    repo_count: Union[Unset, int] = UNSET
    topic_name: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        id = self.id
        repo_count = self.repo_count
        topic_name = self.topic_name
        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if repo_count is not UNSET:
            field_dict["repo_count"] = repo_count
        if topic_name is not UNSET:
            field_dict["topic_name"] = topic_name
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        id = d.pop("id", UNSET)

        repo_count = d.pop("repo_count", UNSET)

        topic_name = d.pop("topic_name", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        topic_response = cls(
            created=created,
            id=id,
            repo_count=repo_count,
            topic_name=topic_name,
            updated=updated,
        )

        topic_response.additional_properties = d
        return topic_response

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
