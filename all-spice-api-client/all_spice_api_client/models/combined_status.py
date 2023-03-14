from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_status import CommitStatus
    from ..models.repository import Repository


T = TypeVar("T", bound="CombinedStatus")


@attr.s(auto_attribs=True)
class CombinedStatus:
    """CombinedStatus holds the combined state of several statuses for a single commit

    Attributes:
        commit_url (Union[Unset, str]):
        repository (Union[Unset, Repository]): Repository represents a repository
        sha (Union[Unset, str]):
        state (Union[Unset, str]): CommitStatusState holds the state of a CommitStatus
            It can be "pending", "success", "error", "failure", and "warning"
        statuses (Union[Unset, List['CommitStatus']]):
        total_count (Union[Unset, int]):
        url (Union[Unset, str]):
    """

    commit_url: Union[Unset, str] = UNSET
    repository: Union[Unset, "Repository"] = UNSET
    sha: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    statuses: Union[Unset, List["CommitStatus"]] = UNSET
    total_count: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commit_url = self.commit_url
        repository: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        sha = self.sha
        state = self.state
        statuses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.to_dict()

                statuses.append(statuses_item)

        total_count = self.total_count
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit_url is not UNSET:
            field_dict["commit_url"] = commit_url
        if repository is not UNSET:
            field_dict["repository"] = repository
        if sha is not UNSET:
            field_dict["sha"] = sha
        if state is not UNSET:
            field_dict["state"] = state
        if statuses is not UNSET:
            field_dict["statuses"] = statuses
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commit_status import CommitStatus
        from ..models.repository import Repository

        d = src_dict.copy()
        commit_url = d.pop("commit_url", UNSET)

        _repository = d.pop("repository", UNSET)
        repository: Union[Unset, Repository]
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        sha = d.pop("sha", UNSET)

        state = d.pop("state", UNSET)

        statuses = []
        _statuses = d.pop("statuses", UNSET)
        for statuses_item_data in _statuses or []:
            statuses_item = CommitStatus.from_dict(statuses_item_data)

            statuses.append(statuses_item)

        total_count = d.pop("total_count", UNSET)

        url = d.pop("url", UNSET)

        combined_status = cls(
            commit_url=commit_url,
            repository=repository,
            sha=sha,
            state=state,
            statuses=statuses,
            total_count=total_count,
            url=url,
        )

        combined_status.additional_properties = d
        return combined_status

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
