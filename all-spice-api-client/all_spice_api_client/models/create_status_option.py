from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateStatusOption")


@attr.s(auto_attribs=True)
class CreateStatusOption:
    """CreateStatusOption holds the information needed to create a new CommitStatus for a Commit

    Attributes:
        context (Union[Unset, str]):
        description (Union[Unset, str]):
        state (Union[Unset, str]): CommitStatusState holds the state of a CommitStatus
            It can be "pending", "success", "error", "failure", and "warning"
        target_url (Union[Unset, str]):
    """

    context: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    target_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context
        description = self.description
        state = self.state
        target_url = self.target_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context is not UNSET:
            field_dict["context"] = context
        if description is not UNSET:
            field_dict["description"] = description
        if state is not UNSET:
            field_dict["state"] = state
        if target_url is not UNSET:
            field_dict["target_url"] = target_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        context = d.pop("context", UNSET)

        description = d.pop("description", UNSET)

        state = d.pop("state", UNSET)

        target_url = d.pop("target_url", UNSET)

        create_status_option = cls(
            context=context,
            description=description,
            state=state,
            target_url=target_url,
        )

        create_status_option.additional_properties = d
        return create_status_option

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
