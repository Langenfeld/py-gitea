import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Cron")


@attr.s(auto_attribs=True)
class Cron:
    """Cron represents a Cron task

    Attributes:
        exec_times (Union[Unset, int]):
        name (Union[Unset, str]):
        next_ (Union[Unset, datetime.datetime]):
        prev (Union[Unset, datetime.datetime]):
        schedule (Union[Unset, str]):
    """

    exec_times: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    next_: Union[Unset, datetime.datetime] = UNSET
    prev: Union[Unset, datetime.datetime] = UNSET
    schedule: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exec_times = self.exec_times
        name = self.name
        next_: Union[Unset, str] = UNSET
        if not isinstance(self.next_, Unset):
            next_ = self.next_.isoformat()

        prev: Union[Unset, str] = UNSET
        if not isinstance(self.prev, Unset):
            prev = self.prev.isoformat()

        schedule = self.schedule

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exec_times is not UNSET:
            field_dict["exec_times"] = exec_times
        if name is not UNSET:
            field_dict["name"] = name
        if next_ is not UNSET:
            field_dict["next"] = next_
        if prev is not UNSET:
            field_dict["prev"] = prev
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        exec_times = d.pop("exec_times", UNSET)

        name = d.pop("name", UNSET)

        _next_ = d.pop("next", UNSET)
        next_: Union[Unset, datetime.datetime]
        if isinstance(_next_, Unset):
            next_ = UNSET
        else:
            next_ = isoparse(_next_)

        _prev = d.pop("prev", UNSET)
        prev: Union[Unset, datetime.datetime]
        if isinstance(_prev, Unset):
            prev = UNSET
        else:
            prev = isoparse(_prev)

        schedule = d.pop("schedule", UNSET)

        cron = cls(
            exec_times=exec_times,
            name=name,
            next_=next_,
            prev=prev,
            schedule=schedule,
        )

        cron.additional_properties = d
        return cron

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
