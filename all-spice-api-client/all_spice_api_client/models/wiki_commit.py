from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit import (
        CommitUserContainsInformationOfAUserInTheContextOfACommit,
    )


T = TypeVar("T", bound="WikiCommit")


@attr.s(auto_attribs=True)
class WikiCommit:
    """WikiCommit page commit/revision

    Attributes:
        author (Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]):
        commiter (Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]):
        message (Union[Unset, str]):
        sha (Union[Unset, str]):
    """

    author: Union[Unset, "CommitUserContainsInformationOfAUserInTheContextOfACommit"] = UNSET
    commiter: Union[Unset, "CommitUserContainsInformationOfAUserInTheContextOfACommit"] = UNSET
    message: Union[Unset, str] = UNSET
    sha: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        commiter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commiter, Unset):
            commiter = self.commiter.to_dict()

        message = self.message
        sha = self.sha

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if commiter is not UNSET:
            field_dict["commiter"] = commiter
        if message is not UNSET:
            field_dict["message"] = message
        if sha is not UNSET:
            field_dict["sha"] = sha

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit import (
            CommitUserContainsInformationOfAUserInTheContextOfACommit,
        )

        d = src_dict.copy()
        _author = d.pop("author", UNSET)
        author: Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = CommitUserContainsInformationOfAUserInTheContextOfACommit.from_dict(_author)

        _commiter = d.pop("commiter", UNSET)
        commiter: Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]
        if isinstance(_commiter, Unset):
            commiter = UNSET
        else:
            commiter = CommitUserContainsInformationOfAUserInTheContextOfACommit.from_dict(_commiter)

        message = d.pop("message", UNSET)

        sha = d.pop("sha", UNSET)

        wiki_commit = cls(
            author=author,
            commiter=commiter,
            message=message,
            sha=sha,
        )

        wiki_commit.additional_properties = d
        return wiki_commit

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
