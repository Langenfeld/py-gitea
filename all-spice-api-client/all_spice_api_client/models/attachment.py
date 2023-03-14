import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Attachment")


@attr.s(auto_attribs=True)
class Attachment:
    """Attachment a generic attachment

    Attributes:
        browser_download_url (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        download_count (Union[Unset, int]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        size (Union[Unset, int]):
        uuid (Union[Unset, str]):
    """

    browser_download_url: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    download_count: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        browser_download_url = self.browser_download_url
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        download_count = self.download_count
        id = self.id
        name = self.name
        size = self.size
        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if browser_download_url is not UNSET:
            field_dict["browser_download_url"] = browser_download_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if download_count is not UNSET:
            field_dict["download_count"] = download_count
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        browser_download_url = d.pop("browser_download_url", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        download_count = d.pop("download_count", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        uuid = d.pop("uuid", UNSET)

        attachment = cls(
            browser_download_url=browser_download_url,
            created_at=created_at,
            download_count=download_count,
            id=id,
            name=name,
            size=size,
            uuid=uuid,
        )

        attachment.additional_properties = d
        return attachment

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
