from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitUserContainsInformationOfAUserInTheContextOfACommit")


@attr.s(auto_attribs=True)
class CommitUserContainsInformationOfAUserInTheContextOfACommit:
    """
    Attributes:
        date (Union[Unset, str]):
        email (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    date: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        email = self.email
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date", UNSET)

        email = d.pop("email", UNSET)

        name = d.pop("name", UNSET)

        commit_user_contains_information_of_a_user_in_the_context_of_a_commit = cls(
            date=date,
            email=email,
            name=name,
        )

        commit_user_contains_information_of_a_user_in_the_context_of_a_commit.additional_properties = d
        return commit_user_contains_information_of_a_user_in_the_context_of_a_commit

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
