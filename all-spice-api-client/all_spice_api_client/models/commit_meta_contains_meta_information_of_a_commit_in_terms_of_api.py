import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitMetaContainsMetaInformationOfACommitInTermsOfAPI")


@attr.s(auto_attribs=True)
class CommitMetaContainsMetaInformationOfACommitInTermsOfAPI:
    """
    Attributes:
        created (Union[Unset, datetime.datetime]):
        sha (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    created: Union[Unset, datetime.datetime] = UNSET
    sha: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        sha = self.sha
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if sha is not UNSET:
            field_dict["sha"] = sha
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        sha = d.pop("sha", UNSET)

        url = d.pop("url", UNSET)

        commit_meta_contains_meta_information_of_a_commit_in_terms_of_api = cls(
            created=created,
            sha=sha,
            url=url,
        )

        commit_meta_contains_meta_information_of_a_commit_in_terms_of_api.additional_properties = d
        return commit_meta_contains_meta_information_of_a_commit_in_terms_of_api

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
