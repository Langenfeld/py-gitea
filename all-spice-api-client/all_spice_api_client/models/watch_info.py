import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.watch_info_reason import WatchInfoReason


T = TypeVar("T", bound="WatchInfo")


@attr.s(auto_attribs=True)
class WatchInfo:
    """WatchInfo represents an API watch status of one repository

    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        ignored (Union[Unset, bool]):
        reason (Union[Unset, WatchInfoReason]):
        repository_url (Union[Unset, str]):
        subscribed (Union[Unset, bool]):
        url (Union[Unset, str]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    ignored: Union[Unset, bool] = UNSET
    reason: Union[Unset, "WatchInfoReason"] = UNSET
    repository_url: Union[Unset, str] = UNSET
    subscribed: Union[Unset, bool] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        ignored = self.ignored
        reason: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        repository_url = self.repository_url
        subscribed = self.subscribed
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if ignored is not UNSET:
            field_dict["ignored"] = ignored
        if reason is not UNSET:
            field_dict["reason"] = reason
        if repository_url is not UNSET:
            field_dict["repository_url"] = repository_url
        if subscribed is not UNSET:
            field_dict["subscribed"] = subscribed
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.watch_info_reason import WatchInfoReason

        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        ignored = d.pop("ignored", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, WatchInfoReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = WatchInfoReason.from_dict(_reason)

        repository_url = d.pop("repository_url", UNSET)

        subscribed = d.pop("subscribed", UNSET)

        url = d.pop("url", UNSET)

        watch_info = cls(
            created_at=created_at,
            ignored=ignored,
            reason=reason,
            repository_url=repository_url,
            subscribed=subscribed,
            url=url,
        )

        watch_info.additional_properties = d
        return watch_info

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
