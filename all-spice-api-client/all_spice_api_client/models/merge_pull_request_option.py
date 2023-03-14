from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.merge_pull_request_option_do import MergePullRequestOptionDo
from ..types import UNSET, Unset

T = TypeVar("T", bound="MergePullRequestOption")


@attr.s(auto_attribs=True)
class MergePullRequestOption:
    """MergePullRequestForm form for merging Pull Request

    Attributes:
        do (MergePullRequestOptionDo):
        merge_commit_id (Union[Unset, str]):
        merge_message_field (Union[Unset, str]):
        merge_title_field (Union[Unset, str]):
        delete_branch_after_merge (Union[Unset, bool]):
        force_merge (Union[Unset, bool]):
        head_commit_id (Union[Unset, str]):
        merge_when_checks_succeed (Union[Unset, bool]):
    """

    do: MergePullRequestOptionDo
    merge_commit_id: Union[Unset, str] = UNSET
    merge_message_field: Union[Unset, str] = UNSET
    merge_title_field: Union[Unset, str] = UNSET
    delete_branch_after_merge: Union[Unset, bool] = UNSET
    force_merge: Union[Unset, bool] = UNSET
    head_commit_id: Union[Unset, str] = UNSET
    merge_when_checks_succeed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        do = self.do.value

        merge_commit_id = self.merge_commit_id
        merge_message_field = self.merge_message_field
        merge_title_field = self.merge_title_field
        delete_branch_after_merge = self.delete_branch_after_merge
        force_merge = self.force_merge
        head_commit_id = self.head_commit_id
        merge_when_checks_succeed = self.merge_when_checks_succeed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Do": do,
            }
        )
        if merge_commit_id is not UNSET:
            field_dict["MergeCommitID"] = merge_commit_id
        if merge_message_field is not UNSET:
            field_dict["MergeMessageField"] = merge_message_field
        if merge_title_field is not UNSET:
            field_dict["MergeTitleField"] = merge_title_field
        if delete_branch_after_merge is not UNSET:
            field_dict["delete_branch_after_merge"] = delete_branch_after_merge
        if force_merge is not UNSET:
            field_dict["force_merge"] = force_merge
        if head_commit_id is not UNSET:
            field_dict["head_commit_id"] = head_commit_id
        if merge_when_checks_succeed is not UNSET:
            field_dict["merge_when_checks_succeed"] = merge_when_checks_succeed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        do = MergePullRequestOptionDo(d.pop("Do"))

        merge_commit_id = d.pop("MergeCommitID", UNSET)

        merge_message_field = d.pop("MergeMessageField", UNSET)

        merge_title_field = d.pop("MergeTitleField", UNSET)

        delete_branch_after_merge = d.pop("delete_branch_after_merge", UNSET)

        force_merge = d.pop("force_merge", UNSET)

        head_commit_id = d.pop("head_commit_id", UNSET)

        merge_when_checks_succeed = d.pop("merge_when_checks_succeed", UNSET)

        merge_pull_request_option = cls(
            do=do,
            merge_commit_id=merge_commit_id,
            merge_message_field=merge_message_field,
            merge_title_field=merge_title_field,
            delete_branch_after_merge=delete_branch_after_merge,
            force_merge=force_merge,
            head_commit_id=head_commit_id,
            merge_when_checks_succeed=merge_when_checks_succeed,
        )

        merge_pull_request_option.additional_properties = d
        return merge_pull_request_option

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
