from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_meta_contains_meta_information_of_a_commit_in_terms_of_api import (
        CommitMetaContainsMetaInformationOfACommitInTermsOfAPI,
    )
    from ..models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit import (
        CommitUserContainsInformationOfAUserInTheContextOfACommit,
    )
    from ..models.payload_commit_verification import PayloadCommitVerification


T = TypeVar("T", bound="RepoCommitContainsInformationOfACommitInTheContextOfARepository")


@attr.s(auto_attribs=True)
class RepoCommitContainsInformationOfACommitInTheContextOfARepository:
    """
    Attributes:
        author (Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]):
        committer (Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]):
        message (Union[Unset, str]):
        tree (Union[Unset, CommitMetaContainsMetaInformationOfACommitInTermsOfAPI]):
        url (Union[Unset, str]):
        verification (Union[Unset, PayloadCommitVerification]): PayloadCommitVerification represents the GPG
            verification of a commit
    """

    author: Union[Unset, "CommitUserContainsInformationOfAUserInTheContextOfACommit"] = UNSET
    committer: Union[Unset, "CommitUserContainsInformationOfAUserInTheContextOfACommit"] = UNSET
    message: Union[Unset, str] = UNSET
    tree: Union[Unset, "CommitMetaContainsMetaInformationOfACommitInTermsOfAPI"] = UNSET
    url: Union[Unset, str] = UNSET
    verification: Union[Unset, "PayloadCommitVerification"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        committer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.to_dict()

        message = self.message
        tree: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tree, Unset):
            tree = self.tree.to_dict()

        url = self.url
        verification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if committer is not UNSET:
            field_dict["committer"] = committer
        if message is not UNSET:
            field_dict["message"] = message
        if tree is not UNSET:
            field_dict["tree"] = tree
        if url is not UNSET:
            field_dict["url"] = url
        if verification is not UNSET:
            field_dict["verification"] = verification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commit_meta_contains_meta_information_of_a_commit_in_terms_of_api import (
            CommitMetaContainsMetaInformationOfACommitInTermsOfAPI,
        )
        from ..models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit import (
            CommitUserContainsInformationOfAUserInTheContextOfACommit,
        )
        from ..models.payload_commit_verification import PayloadCommitVerification

        d = src_dict.copy()
        _author = d.pop("author", UNSET)
        author: Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = CommitUserContainsInformationOfAUserInTheContextOfACommit.from_dict(_author)

        _committer = d.pop("committer", UNSET)
        committer: Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = CommitUserContainsInformationOfAUserInTheContextOfACommit.from_dict(_committer)

        message = d.pop("message", UNSET)

        _tree = d.pop("tree", UNSET)
        tree: Union[Unset, CommitMetaContainsMetaInformationOfACommitInTermsOfAPI]
        if isinstance(_tree, Unset):
            tree = UNSET
        else:
            tree = CommitMetaContainsMetaInformationOfACommitInTermsOfAPI.from_dict(_tree)

        url = d.pop("url", UNSET)

        _verification = d.pop("verification", UNSET)
        verification: Union[Unset, PayloadCommitVerification]
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = PayloadCommitVerification.from_dict(_verification)

        repo_commit_contains_information_of_a_commit_in_the_context_of_a_repository = cls(
            author=author,
            committer=committer,
            message=message,
            tree=tree,
            url=url,
            verification=verification,
        )

        repo_commit_contains_information_of_a_commit_in_the_context_of_a_repository.additional_properties = d
        return repo_commit_contains_information_of_a_commit_in_the_context_of_a_repository

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
