from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitBlobResponse")


@attr.s(auto_attribs=True)
class GitBlobResponse:
    """GitBlobResponse represents a git blob

    Attributes:
        content (Union[Unset, str]):
        encoding (Union[Unset, str]):
        sha (Union[Unset, str]):
        size (Union[Unset, int]):
        url (Union[Unset, str]):
    """

    content: Union[Unset, str] = UNSET
    encoding: Union[Unset, str] = UNSET
    sha: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content
        encoding = self.encoding
        sha = self.sha
        size = self.size
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if sha is not UNSET:
            field_dict["sha"] = sha
        if size is not UNSET:
            field_dict["size"] = size
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content", UNSET)

        encoding = d.pop("encoding", UNSET)

        sha = d.pop("sha", UNSET)

        size = d.pop("size", UNSET)

        url = d.pop("url", UNSET)

        git_blob_response = cls(
            content=content,
            encoding=encoding,
            sha=sha,
            size=size,
            url=url,
        )

        git_blob_response.additional_properties = d
        return git_blob_response

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
