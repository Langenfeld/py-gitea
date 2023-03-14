import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.create_milestone_option_state import CreateMilestoneOptionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateMilestoneOption")


@attr.s(auto_attribs=True)
class CreateMilestoneOption:
    """CreateMilestoneOption options for creating a milestone

    Attributes:
        description (Union[Unset, str]):
        due_on (Union[Unset, datetime.datetime]):
        state (Union[Unset, CreateMilestoneOptionState]):
        title (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    due_on: Union[Unset, datetime.datetime] = UNSET
    state: Union[Unset, CreateMilestoneOptionState] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        due_on: Union[Unset, str] = UNSET
        if not isinstance(self.due_on, Unset):
            due_on = self.due_on.isoformat()

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if due_on is not UNSET:
            field_dict["due_on"] = due_on
        if state is not UNSET:
            field_dict["state"] = state
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        _due_on = d.pop("due_on", UNSET)
        due_on: Union[Unset, datetime.datetime]
        if isinstance(_due_on, Unset):
            due_on = UNSET
        else:
            due_on = isoparse(_due_on)

        _state = d.pop("state", UNSET)
        state: Union[Unset, CreateMilestoneOptionState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CreateMilestoneOptionState(_state)

        title = d.pop("title", UNSET)

        create_milestone_option = cls(
            description=description,
            due_on=due_on,
            state=state,
            title=title,
        )

        create_milestone_option.additional_properties = d
        return create_milestone_option

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
