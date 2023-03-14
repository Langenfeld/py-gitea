import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hook_config import HookConfig


T = TypeVar("T", bound="Hook")


@attr.s(auto_attribs=True)
class Hook:
    """Hook a hook is a web hook when one repository changed

    Attributes:
        active (Union[Unset, bool]):
        config (Union[Unset, HookConfig]):
        created_at (Union[Unset, datetime.datetime]):
        events (Union[Unset, List[str]]):
        id (Union[Unset, int]):
        type (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    active: Union[Unset, bool] = UNSET
    config: Union[Unset, "HookConfig"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    events: Union[Unset, List[str]] = UNSET
    id: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        id = self.id
        type = self.type
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if config is not UNSET:
            field_dict["config"] = config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if events is not UNSET:
            field_dict["events"] = events
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hook_config import HookConfig

        d = src_dict.copy()
        active = d.pop("active", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, HookConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = HookConfig.from_dict(_config)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        events = cast(List[str], d.pop("events", UNSET))

        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        hook = cls(
            active=active,
            config=config,
            created_at=created_at,
            events=events,
            id=id,
            type=type,
            updated_at=updated_at,
        )

        hook.additional_properties = d
        return hook

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
