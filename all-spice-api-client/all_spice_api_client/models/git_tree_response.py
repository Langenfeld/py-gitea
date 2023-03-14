from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_entry import GitEntry


T = TypeVar("T", bound="GitTreeResponse")


@attr.s(auto_attribs=True)
class GitTreeResponse:
    """GitTreeResponse returns a git tree

    Attributes:
        page (Union[Unset, int]):
        sha (Union[Unset, str]):
        total_count (Union[Unset, int]):
        tree (Union[Unset, List['GitEntry']]):
        truncated (Union[Unset, bool]):
        url (Union[Unset, str]):
    """

    page: Union[Unset, int] = UNSET
    sha: Union[Unset, str] = UNSET
    total_count: Union[Unset, int] = UNSET
    tree: Union[Unset, List["GitEntry"]] = UNSET
    truncated: Union[Unset, bool] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page = self.page
        sha = self.sha
        total_count = self.total_count
        tree: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tree, Unset):
            tree = []
            for tree_item_data in self.tree:
                tree_item = tree_item_data.to_dict()

                tree.append(tree_item)

        truncated = self.truncated
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if sha is not UNSET:
            field_dict["sha"] = sha
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if tree is not UNSET:
            field_dict["tree"] = tree
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.git_entry import GitEntry

        d = src_dict.copy()
        page = d.pop("page", UNSET)

        sha = d.pop("sha", UNSET)

        total_count = d.pop("total_count", UNSET)

        tree = []
        _tree = d.pop("tree", UNSET)
        for tree_item_data in _tree or []:
            tree_item = GitEntry.from_dict(tree_item_data)

            tree.append(tree_item)

        truncated = d.pop("truncated", UNSET)

        url = d.pop("url", UNSET)

        git_tree_response = cls(
            page=page,
            sha=sha,
            total_count=total_count,
            tree=tree,
            truncated=truncated,
            url=url,
        )

        git_tree_response.additional_properties = d
        return git_tree_response

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
