from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_links_response import FileLinksResponse


T = TypeVar("T", bound="ContentsResponse")


@attr.s(auto_attribs=True)
class ContentsResponse:
    """ContentsResponse contains information about a repo's entry's (dir, file, symlink, submodule) metadata and content

    Attributes:
        field_links (Union[Unset, FileLinksResponse]): FileLinksResponse contains the links for a repo's file
        content (Union[Unset, str]): `content` is populated when `type` is `file`, otherwise null
        download_url (Union[Unset, str]):
        encoding (Union[Unset, str]): `encoding` is populated when `type` is `file`, otherwise null
        git_url (Union[Unset, str]):
        html_url (Union[Unset, str]):
        last_commit_sha (Union[Unset, str]):
        name (Union[Unset, str]):
        path (Union[Unset, str]):
        sha (Union[Unset, str]):
        size (Union[Unset, int]):
        submodule_git_url (Union[Unset, str]): `submodule_git_url` is populated when `type` is `submodule`, otherwise
            null
        target (Union[Unset, str]): `target` is populated when `type` is `symlink`, otherwise null
        type (Union[Unset, str]): `type` will be `file`, `dir`, `symlink`, or `submodule`
        url (Union[Unset, str]):
    """

    field_links: Union[Unset, "FileLinksResponse"] = UNSET
    content: Union[Unset, str] = UNSET
    download_url: Union[Unset, str] = UNSET
    encoding: Union[Unset, str] = UNSET
    git_url: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    last_commit_sha: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    sha: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    submodule_git_url: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        content = self.content
        download_url = self.download_url
        encoding = self.encoding
        git_url = self.git_url
        html_url = self.html_url
        last_commit_sha = self.last_commit_sha
        name = self.name
        path = self.path
        sha = self.sha
        size = self.size
        submodule_git_url = self.submodule_git_url
        target = self.target
        type = self.type
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if content is not UNSET:
            field_dict["content"] = content
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if git_url is not UNSET:
            field_dict["git_url"] = git_url
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if last_commit_sha is not UNSET:
            field_dict["last_commit_sha"] = last_commit_sha
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if sha is not UNSET:
            field_dict["sha"] = sha
        if size is not UNSET:
            field_dict["size"] = size
        if submodule_git_url is not UNSET:
            field_dict["submodule_git_url"] = submodule_git_url
        if target is not UNSET:
            field_dict["target"] = target
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_links_response import FileLinksResponse

        d = src_dict.copy()
        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, FileLinksResponse]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = FileLinksResponse.from_dict(_field_links)

        content = d.pop("content", UNSET)

        download_url = d.pop("download_url", UNSET)

        encoding = d.pop("encoding", UNSET)

        git_url = d.pop("git_url", UNSET)

        html_url = d.pop("html_url", UNSET)

        last_commit_sha = d.pop("last_commit_sha", UNSET)

        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        sha = d.pop("sha", UNSET)

        size = d.pop("size", UNSET)

        submodule_git_url = d.pop("submodule_git_url", UNSET)

        target = d.pop("target", UNSET)

        type = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        contents_response = cls(
            field_links=field_links,
            content=content,
            download_url=download_url,
            encoding=encoding,
            git_url=git_url,
            html_url=html_url,
            last_commit_sha=last_commit_sha,
            name=name,
            path=path,
            sha=sha,
            size=size,
            submodule_git_url=submodule_git_url,
            target=target,
            type=type,
            url=url,
        )

        contents_response.additional_properties = d
        return contents_response

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
