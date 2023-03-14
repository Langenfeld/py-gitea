import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddTimeOption")


@attr.s(auto_attribs=True)
class AddTimeOption:
    """AddTimeOption options for adding time to an issue

    Attributes:
        time (int): time in seconds
        created (Union[Unset, datetime.datetime]):
        user_name (Union[Unset, str]): User who spent the time (optional)
    """

    time: int
    created: Union[Unset, datetime.datetime] = UNSET
    user_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        user_name = self.user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created
        if user_name is not UNSET:
            field_dict["user_name"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = d.pop("time")

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        user_name = d.pop("user_name", UNSET)

        add_time_option = cls(
            time=time,
            created=created,
            user_name=user_name,
        )

        add_time_option.additional_properties = d
        return add_time_option

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
