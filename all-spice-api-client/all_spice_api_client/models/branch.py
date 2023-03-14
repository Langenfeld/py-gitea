from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payload_commit import PayloadCommit


T = TypeVar("T", bound="Branch")


@attr.s(auto_attribs=True)
class Branch:
    """Branch represents a repository branch

    Attributes:
        commit (Union[Unset, PayloadCommit]): PayloadCommit represents a commit
        effective_branch_protection_name (Union[Unset, str]):
        enable_status_check (Union[Unset, bool]):
        name (Union[Unset, str]):
        protected (Union[Unset, bool]):
        required_approvals (Union[Unset, int]):
        status_check_contexts (Union[Unset, List[str]]):
        user_can_merge (Union[Unset, bool]):
        user_can_push (Union[Unset, bool]):
    """

    commit: Union[Unset, "PayloadCommit"] = UNSET
    effective_branch_protection_name: Union[Unset, str] = UNSET
    enable_status_check: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    protected: Union[Unset, bool] = UNSET
    required_approvals: Union[Unset, int] = UNSET
    status_check_contexts: Union[Unset, List[str]] = UNSET
    user_can_merge: Union[Unset, bool] = UNSET
    user_can_push: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        effective_branch_protection_name = self.effective_branch_protection_name
        enable_status_check = self.enable_status_check
        name = self.name
        protected = self.protected
        required_approvals = self.required_approvals
        status_check_contexts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.status_check_contexts, Unset):
            status_check_contexts = self.status_check_contexts

        user_can_merge = self.user_can_merge
        user_can_push = self.user_can_push

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit is not UNSET:
            field_dict["commit"] = commit
        if effective_branch_protection_name is not UNSET:
            field_dict["effective_branch_protection_name"] = effective_branch_protection_name
        if enable_status_check is not UNSET:
            field_dict["enable_status_check"] = enable_status_check
        if name is not UNSET:
            field_dict["name"] = name
        if protected is not UNSET:
            field_dict["protected"] = protected
        if required_approvals is not UNSET:
            field_dict["required_approvals"] = required_approvals
        if status_check_contexts is not UNSET:
            field_dict["status_check_contexts"] = status_check_contexts
        if user_can_merge is not UNSET:
            field_dict["user_can_merge"] = user_can_merge
        if user_can_push is not UNSET:
            field_dict["user_can_push"] = user_can_push

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payload_commit import PayloadCommit

        d = src_dict.copy()
        _commit = d.pop("commit", UNSET)
        commit: Union[Unset, PayloadCommit]
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = PayloadCommit.from_dict(_commit)

        effective_branch_protection_name = d.pop("effective_branch_protection_name", UNSET)

        enable_status_check = d.pop("enable_status_check", UNSET)

        name = d.pop("name", UNSET)

        protected = d.pop("protected", UNSET)

        required_approvals = d.pop("required_approvals", UNSET)

        status_check_contexts = cast(List[str], d.pop("status_check_contexts", UNSET))

        user_can_merge = d.pop("user_can_merge", UNSET)

        user_can_push = d.pop("user_can_push", UNSET)

        branch = cls(
            commit=commit,
            effective_branch_protection_name=effective_branch_protection_name,
            enable_status_check=enable_status_check,
            name=name,
            protected=protected,
            required_approvals=required_approvals,
            status_check_contexts=status_check_contexts,
            user_can_merge=user_can_merge,
            user_can_push=user_can_push,
        )

        branch.additional_properties = d
        return branch

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
