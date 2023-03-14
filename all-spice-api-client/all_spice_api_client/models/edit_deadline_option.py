import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="EditDeadlineOption")


@attr.s(auto_attribs=True)
class EditDeadlineOption:
    """EditDeadlineOption options for creating a deadline

    Attributes:
        due_date (datetime.datetime):
    """

    due_date: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        due_date = self.due_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "due_date": due_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        due_date = isoparse(d.pop("due_date"))

        edit_deadline_option = cls(
            due_date=due_date,
        )

        edit_deadline_option.additional_properties = d
        return edit_deadline_option

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
