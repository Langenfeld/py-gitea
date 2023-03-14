from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_contains_information_generated_from_a_git_commit import (
        CommitContainsInformationGeneratedFromAGitCommit,
    )


T = TypeVar("T", bound="Note")


@attr.s(auto_attribs=True)
class Note:
    """Note contains information related to a git note

    Attributes:
        commit (Union[Unset, CommitContainsInformationGeneratedFromAGitCommit]):
        message (Union[Unset, str]):
    """

    commit: Union[Unset, "CommitContainsInformationGeneratedFromAGitCommit"] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit is not UNSET:
            field_dict["commit"] = commit
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commit_contains_information_generated_from_a_git_commit import (
            CommitContainsInformationGeneratedFromAGitCommit,
        )

        d = src_dict.copy()
        _commit = d.pop("commit", UNSET)
        commit: Union[Unset, CommitContainsInformationGeneratedFromAGitCommit]
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = CommitContainsInformationGeneratedFromAGitCommit.from_dict(_commit)

        message = d.pop("message", UNSET)

        note = cls(
            commit=commit,
            message=message,
        )

        note.additional_properties = d
        return note

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
