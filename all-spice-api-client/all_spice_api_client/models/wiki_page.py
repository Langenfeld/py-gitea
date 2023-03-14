from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wiki_commit import WikiCommit


T = TypeVar("T", bound="WikiPage")


@attr.s(auto_attribs=True)
class WikiPage:
    """WikiPage a wiki page

    Attributes:
        commit_count (Union[Unset, int]):
        content_base64 (Union[Unset, str]): Page content, base64 encoded
        footer (Union[Unset, str]):
        html_url (Union[Unset, str]):
        last_commit (Union[Unset, WikiCommit]): WikiCommit page commit/revision
        sidebar (Union[Unset, str]):
        sub_url (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    commit_count: Union[Unset, int] = UNSET
    content_base64: Union[Unset, str] = UNSET
    footer: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    last_commit: Union[Unset, "WikiCommit"] = UNSET
    sidebar: Union[Unset, str] = UNSET
    sub_url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commit_count = self.commit_count
        content_base64 = self.content_base64
        footer = self.footer
        html_url = self.html_url
        last_commit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_commit, Unset):
            last_commit = self.last_commit.to_dict()

        sidebar = self.sidebar
        sub_url = self.sub_url
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit_count is not UNSET:
            field_dict["commit_count"] = commit_count
        if content_base64 is not UNSET:
            field_dict["content_base64"] = content_base64
        if footer is not UNSET:
            field_dict["footer"] = footer
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if last_commit is not UNSET:
            field_dict["last_commit"] = last_commit
        if sidebar is not UNSET:
            field_dict["sidebar"] = sidebar
        if sub_url is not UNSET:
            field_dict["sub_url"] = sub_url
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wiki_commit import WikiCommit

        d = src_dict.copy()
        commit_count = d.pop("commit_count", UNSET)

        content_base64 = d.pop("content_base64", UNSET)

        footer = d.pop("footer", UNSET)

        html_url = d.pop("html_url", UNSET)

        _last_commit = d.pop("last_commit", UNSET)
        last_commit: Union[Unset, WikiCommit]
        if isinstance(_last_commit, Unset):
            last_commit = UNSET
        else:
            last_commit = WikiCommit.from_dict(_last_commit)

        sidebar = d.pop("sidebar", UNSET)

        sub_url = d.pop("sub_url", UNSET)

        title = d.pop("title", UNSET)

        wiki_page = cls(
            commit_count=commit_count,
            content_base64=content_base64,
            footer=footer,
            html_url=html_url,
            last_commit=last_commit,
            sidebar=sidebar,
            sub_url=sub_url,
            title=title,
        )

        wiki_page.additional_properties = d
        return wiki_page

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
