from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangedFile")


@attr.s(auto_attribs=True)
class ChangedFile:
    """ChangedFile store information about files affected by the pull request

    Attributes:
        additions (Union[Unset, int]):
        changes (Union[Unset, int]):
        contents_url (Union[Unset, str]):
        deletions (Union[Unset, int]):
        filename (Union[Unset, str]):
        html_url (Union[Unset, str]):
        previous_filename (Union[Unset, str]):
        raw_url (Union[Unset, str]):
        status (Union[Unset, str]):
    """

    additions: Union[Unset, int] = UNSET
    changes: Union[Unset, int] = UNSET
    contents_url: Union[Unset, str] = UNSET
    deletions: Union[Unset, int] = UNSET
    filename: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    previous_filename: Union[Unset, str] = UNSET
    raw_url: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        additions = self.additions
        changes = self.changes
        contents_url = self.contents_url
        deletions = self.deletions
        filename = self.filename
        html_url = self.html_url
        previous_filename = self.previous_filename
        raw_url = self.raw_url
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additions is not UNSET:
            field_dict["additions"] = additions
        if changes is not UNSET:
            field_dict["changes"] = changes
        if contents_url is not UNSET:
            field_dict["contents_url"] = contents_url
        if deletions is not UNSET:
            field_dict["deletions"] = deletions
        if filename is not UNSET:
            field_dict["filename"] = filename
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if previous_filename is not UNSET:
            field_dict["previous_filename"] = previous_filename
        if raw_url is not UNSET:
            field_dict["raw_url"] = raw_url
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        additions = d.pop("additions", UNSET)

        changes = d.pop("changes", UNSET)

        contents_url = d.pop("contents_url", UNSET)

        deletions = d.pop("deletions", UNSET)

        filename = d.pop("filename", UNSET)

        html_url = d.pop("html_url", UNSET)

        previous_filename = d.pop("previous_filename", UNSET)

        raw_url = d.pop("raw_url", UNSET)

        status = d.pop("status", UNSET)

        changed_file = cls(
            additions=additions,
            changes=changes,
            contents_url=contents_url,
            deletions=deletions,
            filename=filename,
            html_url=html_url,
            previous_filename=previous_filename,
            raw_url=raw_url,
            status=status,
        )

        changed_file.additional_properties = d
        return changed_file

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
