import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_meta_contains_meta_information_of_a_commit_in_terms_of_api import (
        CommitMetaContainsMetaInformationOfACommitInTermsOfAPI,
    )
    from ..models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit import (
        CommitUserContainsInformationOfAUserInTheContextOfACommit,
    )


T = TypeVar("T", bound="FileCommitResponseContainsInformationGeneratedFromAGitCommitForAReposFile")


@attr.s(auto_attribs=True)
class FileCommitResponseContainsInformationGeneratedFromAGitCommitForAReposFile:
    """
    Attributes:
        author (Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]):
        committer (Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]):
        created (Union[Unset, datetime.datetime]):
        html_url (Union[Unset, str]):
        message (Union[Unset, str]):
        parents (Union[Unset, List['CommitMetaContainsMetaInformationOfACommitInTermsOfAPI']]):
        sha (Union[Unset, str]):
        tree (Union[Unset, CommitMetaContainsMetaInformationOfACommitInTermsOfAPI]):
        url (Union[Unset, str]):
    """

    author: Union[Unset, "CommitUserContainsInformationOfAUserInTheContextOfACommit"] = UNSET
    committer: Union[Unset, "CommitUserContainsInformationOfAUserInTheContextOfACommit"] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    html_url: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    parents: Union[Unset, List["CommitMetaContainsMetaInformationOfACommitInTermsOfAPI"]] = UNSET
    sha: Union[Unset, str] = UNSET
    tree: Union[Unset, "CommitMetaContainsMetaInformationOfACommitInTermsOfAPI"] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        committer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.to_dict()

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        html_url = self.html_url
        message = self.message
        parents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parents, Unset):
            parents = []
            for parents_item_data in self.parents:
                parents_item = parents_item_data.to_dict()

                parents.append(parents_item)

        sha = self.sha
        tree: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tree, Unset):
            tree = self.tree.to_dict()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if committer is not UNSET:
            field_dict["committer"] = committer
        if created is not UNSET:
            field_dict["created"] = created
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if message is not UNSET:
            field_dict["message"] = message
        if parents is not UNSET:
            field_dict["parents"] = parents
        if sha is not UNSET:
            field_dict["sha"] = sha
        if tree is not UNSET:
            field_dict["tree"] = tree
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commit_meta_contains_meta_information_of_a_commit_in_terms_of_api import (
            CommitMetaContainsMetaInformationOfACommitInTermsOfAPI,
        )
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

        _committer = d.pop("committer", UNSET)
        committer: Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = CommitUserContainsInformationOfAUserInTheContextOfACommit.from_dict(_committer)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        html_url = d.pop("html_url", UNSET)

        message = d.pop("message", UNSET)

        parents = []
        _parents = d.pop("parents", UNSET)
        for parents_item_data in _parents or []:
            parents_item = CommitMetaContainsMetaInformationOfACommitInTermsOfAPI.from_dict(parents_item_data)

            parents.append(parents_item)

        sha = d.pop("sha", UNSET)

        _tree = d.pop("tree", UNSET)
        tree: Union[Unset, CommitMetaContainsMetaInformationOfACommitInTermsOfAPI]
        if isinstance(_tree, Unset):
            tree = UNSET
        else:
            tree = CommitMetaContainsMetaInformationOfACommitInTermsOfAPI.from_dict(_tree)

        url = d.pop("url", UNSET)

        file_commit_response_contains_information_generated_from_a_git_commit_for_a_repos_file = cls(
            author=author,
            committer=committer,
            created=created,
            html_url=html_url,
            message=message,
            parents=parents,
            sha=sha,
            tree=tree,
            url=url,
        )

        file_commit_response_contains_information_generated_from_a_git_commit_for_a_repos_file.additional_properties = d
        return file_commit_response_contains_information_generated_from_a_git_commit_for_a_repos_file

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
