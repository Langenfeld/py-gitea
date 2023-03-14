from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contents_response import ContentsResponse
    from ..models.file_commit_response_contains_information_generated_from_a_git_commit_for_a_repos_file import (
        FileCommitResponseContainsInformationGeneratedFromAGitCommitForAReposFile,
    )
    from ..models.payload_commit_verification import PayloadCommitVerification


T = TypeVar("T", bound="FileResponse")


@attr.s(auto_attribs=True)
class FileResponse:
    """FileResponse contains information about a repo's file

    Attributes:
        commit (Union[Unset, FileCommitResponseContainsInformationGeneratedFromAGitCommitForAReposFile]):
        content (Union[Unset, ContentsResponse]): ContentsResponse contains information about a repo's entry's (dir,
            file, symlink, submodule) metadata and content
        verification (Union[Unset, PayloadCommitVerification]): PayloadCommitVerification represents the GPG
            verification of a commit
    """

    commit: Union[Unset, "FileCommitResponseContainsInformationGeneratedFromAGitCommitForAReposFile"] = UNSET
    content: Union[Unset, "ContentsResponse"] = UNSET
    verification: Union[Unset, "PayloadCommitVerification"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        verification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit is not UNSET:
            field_dict["commit"] = commit
        if content is not UNSET:
            field_dict["content"] = content
        if verification is not UNSET:
            field_dict["verification"] = verification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contents_response import ContentsResponse
        from ..models.file_commit_response_contains_information_generated_from_a_git_commit_for_a_repos_file import (
            FileCommitResponseContainsInformationGeneratedFromAGitCommitForAReposFile,
        )
        from ..models.payload_commit_verification import PayloadCommitVerification

        d = src_dict.copy()
        _commit = d.pop("commit", UNSET)
        commit: Union[Unset, FileCommitResponseContainsInformationGeneratedFromAGitCommitForAReposFile]
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = FileCommitResponseContainsInformationGeneratedFromAGitCommitForAReposFile.from_dict(_commit)

        _content = d.pop("content", UNSET)
        content: Union[Unset, ContentsResponse]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ContentsResponse.from_dict(_content)

        _verification = d.pop("verification", UNSET)
        verification: Union[Unset, PayloadCommitVerification]
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = PayloadCommitVerification.from_dict(_verification)

        file_response = cls(
            commit=commit,
            content=content,
            verification=verification,
        )

        file_response.additional_properties = d
        return file_response

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
