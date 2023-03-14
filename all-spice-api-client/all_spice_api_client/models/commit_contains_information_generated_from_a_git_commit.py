import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_affected_files import CommitAffectedFiles
    from ..models.commit_meta_contains_meta_information_of_a_commit_in_terms_of_api import (
        CommitMetaContainsMetaInformationOfACommitInTermsOfAPI,
    )
    from ..models.commit_stats import CommitStats
    from ..models.repo_commit_contains_information_of_a_commit_in_the_context_of_a_repository import (
        RepoCommitContainsInformationOfACommitInTheContextOfARepository,
    )
    from ..models.user import User


T = TypeVar("T", bound="CommitContainsInformationGeneratedFromAGitCommit")


@attr.s(auto_attribs=True)
class CommitContainsInformationGeneratedFromAGitCommit:
    """
    Attributes:
        author (Union[Unset, User]): User represents a user
        commit (Union[Unset, RepoCommitContainsInformationOfACommitInTheContextOfARepository]):
        committer (Union[Unset, User]): User represents a user
        created (Union[Unset, datetime.datetime]):
        files (Union[Unset, List['CommitAffectedFiles']]):
        html_url (Union[Unset, str]):
        parents (Union[Unset, List['CommitMetaContainsMetaInformationOfACommitInTermsOfAPI']]):
        sha (Union[Unset, str]):
        stats (Union[Unset, CommitStats]): CommitStats is statistics for a RepoCommit
        url (Union[Unset, str]):
    """

    author: Union[Unset, "User"] = UNSET
    commit: Union[Unset, "RepoCommitContainsInformationOfACommitInTheContextOfARepository"] = UNSET
    committer: Union[Unset, "User"] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    files: Union[Unset, List["CommitAffectedFiles"]] = UNSET
    html_url: Union[Unset, str] = UNSET
    parents: Union[Unset, List["CommitMetaContainsMetaInformationOfACommitInTermsOfAPI"]] = UNSET
    sha: Union[Unset, str] = UNSET
    stats: Union[Unset, "CommitStats"] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        commit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        committer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.to_dict()

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        files: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()

                files.append(files_item)

        html_url = self.html_url
        parents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parents, Unset):
            parents = []
            for parents_item_data in self.parents:
                parents_item = parents_item_data.to_dict()

                parents.append(parents_item)

        sha = self.sha
        stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if commit is not UNSET:
            field_dict["commit"] = commit
        if committer is not UNSET:
            field_dict["committer"] = committer
        if created is not UNSET:
            field_dict["created"] = created
        if files is not UNSET:
            field_dict["files"] = files
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if parents is not UNSET:
            field_dict["parents"] = parents
        if sha is not UNSET:
            field_dict["sha"] = sha
        if stats is not UNSET:
            field_dict["stats"] = stats
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commit_affected_files import CommitAffectedFiles
        from ..models.commit_meta_contains_meta_information_of_a_commit_in_terms_of_api import (
            CommitMetaContainsMetaInformationOfACommitInTermsOfAPI,
        )
        from ..models.commit_stats import CommitStats
        from ..models.repo_commit_contains_information_of_a_commit_in_the_context_of_a_repository import (
            RepoCommitContainsInformationOfACommitInTheContextOfARepository,
        )
        from ..models.user import User

        d = src_dict.copy()
        _author = d.pop("author", UNSET)
        author: Union[Unset, User]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = User.from_dict(_author)

        _commit = d.pop("commit", UNSET)
        commit: Union[Unset, RepoCommitContainsInformationOfACommitInTheContextOfARepository]
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = RepoCommitContainsInformationOfACommitInTheContextOfARepository.from_dict(_commit)

        _committer = d.pop("committer", UNSET)
        committer: Union[Unset, User]
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = User.from_dict(_committer)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = CommitAffectedFiles.from_dict(files_item_data)

            files.append(files_item)

        html_url = d.pop("html_url", UNSET)

        parents = []
        _parents = d.pop("parents", UNSET)
        for parents_item_data in _parents or []:
            parents_item = CommitMetaContainsMetaInformationOfACommitInTermsOfAPI.from_dict(parents_item_data)

            parents.append(parents_item)

        sha = d.pop("sha", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, CommitStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = CommitStats.from_dict(_stats)

        url = d.pop("url", UNSET)

        commit_contains_information_generated_from_a_git_commit = cls(
            author=author,
            commit=commit,
            committer=committer,
            created=created,
            files=files,
            html_url=html_url,
            parents=parents,
            sha=sha,
            stats=stats,
            url=url,
        )

        commit_contains_information_generated_from_a_git_commit.additional_properties = d
        return commit_contains_information_generated_from_a_git_commit

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
