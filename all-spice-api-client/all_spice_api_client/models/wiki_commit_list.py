from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wiki_commit import WikiCommit


T = TypeVar("T", bound="WikiCommitList")


@attr.s(auto_attribs=True)
class WikiCommitList:
    """WikiCommitList commit/revision list

    Attributes:
        commits (Union[Unset, List['WikiCommit']]):
        count (Union[Unset, int]):
    """

    commits: Union[Unset, List["WikiCommit"]] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commits: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.commits, Unset):
            commits = []
            for commits_item_data in self.commits:
                commits_item = commits_item_data.to_dict()

                commits.append(commits_item)

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commits is not UNSET:
            field_dict["commits"] = commits
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wiki_commit import WikiCommit

        d = src_dict.copy()
        commits = []
        _commits = d.pop("commits", UNSET)
        for commits_item_data in _commits or []:
            commits_item = WikiCommit.from_dict(commits_item_data)

            commits.append(commits_item)

        count = d.pop("count", UNSET)

        wiki_commit_list = cls(
            commits=commits,
            count=count,
        )

        wiki_commit_list.additional_properties = d
        return wiki_commit_list

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
