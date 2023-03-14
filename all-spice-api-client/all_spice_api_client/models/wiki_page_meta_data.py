from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wiki_commit import WikiCommit


T = TypeVar("T", bound="WikiPageMetaData")


@attr.s(auto_attribs=True)
class WikiPageMetaData:
    """WikiPageMetaData wiki page meta information

    Attributes:
        html_url (Union[Unset, str]):
        last_commit (Union[Unset, WikiCommit]): WikiCommit page commit/revision
        sub_url (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    html_url: Union[Unset, str] = UNSET
    last_commit: Union[Unset, "WikiCommit"] = UNSET
    sub_url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        html_url = self.html_url
        last_commit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_commit, Unset):
            last_commit = self.last_commit.to_dict()

        sub_url = self.sub_url
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if last_commit is not UNSET:
            field_dict["last_commit"] = last_commit
        if sub_url is not UNSET:
            field_dict["sub_url"] = sub_url
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wiki_commit import WikiCommit

        d = src_dict.copy()
        html_url = d.pop("html_url", UNSET)

        _last_commit = d.pop("last_commit", UNSET)
        last_commit: Union[Unset, WikiCommit]
        if isinstance(_last_commit, Unset):
            last_commit = UNSET
        else:
            last_commit = WikiCommit.from_dict(_last_commit)

        sub_url = d.pop("sub_url", UNSET)

        title = d.pop("title", UNSET)

        wiki_page_meta_data = cls(
            html_url=html_url,
            last_commit=last_commit,
            sub_url=sub_url,
            title=title,
        )

        wiki_page_meta_data.additional_properties = d
        return wiki_page_meta_data

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
