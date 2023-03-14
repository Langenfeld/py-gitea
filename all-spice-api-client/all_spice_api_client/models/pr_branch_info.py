from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository import Repository


T = TypeVar("T", bound="PRBranchInfo")


@attr.s(auto_attribs=True)
class PRBranchInfo:
    """PRBranchInfo information about a branch

    Attributes:
        label (Union[Unset, str]):
        ref (Union[Unset, str]):
        repo (Union[Unset, Repository]): Repository represents a repository
        repo_id (Union[Unset, int]):
        sha (Union[Unset, str]):
    """

    label: Union[Unset, str] = UNSET
    ref: Union[Unset, str] = UNSET
    repo: Union[Unset, "Repository"] = UNSET
    repo_id: Union[Unset, int] = UNSET
    sha: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        ref = self.ref
        repo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repo, Unset):
            repo = self.repo.to_dict()

        repo_id = self.repo_id
        sha = self.sha

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if ref is not UNSET:
            field_dict["ref"] = ref
        if repo is not UNSET:
            field_dict["repo"] = repo
        if repo_id is not UNSET:
            field_dict["repo_id"] = repo_id
        if sha is not UNSET:
            field_dict["sha"] = sha

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.repository import Repository

        d = src_dict.copy()
        label = d.pop("label", UNSET)

        ref = d.pop("ref", UNSET)

        _repo = d.pop("repo", UNSET)
        repo: Union[Unset, Repository]
        if isinstance(_repo, Unset):
            repo = UNSET
        else:
            repo = Repository.from_dict(_repo)

        repo_id = d.pop("repo_id", UNSET)

        sha = d.pop("sha", UNSET)

        pr_branch_info = cls(
            label=label,
            ref=ref,
            repo=repo,
            repo_id=repo_id,
            sha=sha,
        )

        pr_branch_info.additional_properties = d
        return pr_branch_info

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
