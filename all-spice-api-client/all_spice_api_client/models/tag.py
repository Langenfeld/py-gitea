from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_meta_contains_meta_information_of_a_commit_in_terms_of_api import (
        CommitMetaContainsMetaInformationOfACommitInTermsOfAPI,
    )


T = TypeVar("T", bound="Tag")


@attr.s(auto_attribs=True)
class Tag:
    """Tag represents a repository tag

    Attributes:
        commit (Union[Unset, CommitMetaContainsMetaInformationOfACommitInTermsOfAPI]):
        id (Union[Unset, str]):
        message (Union[Unset, str]):
        name (Union[Unset, str]):
        tarball_url (Union[Unset, str]):
        zipball_url (Union[Unset, str]):
    """

    commit: Union[Unset, "CommitMetaContainsMetaInformationOfACommitInTermsOfAPI"] = UNSET
    id: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    tarball_url: Union[Unset, str] = UNSET
    zipball_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        id = self.id
        message = self.message
        name = self.name
        tarball_url = self.tarball_url
        zipball_url = self.zipball_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit is not UNSET:
            field_dict["commit"] = commit
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if tarball_url is not UNSET:
            field_dict["tarball_url"] = tarball_url
        if zipball_url is not UNSET:
            field_dict["zipball_url"] = zipball_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commit_meta_contains_meta_information_of_a_commit_in_terms_of_api import (
            CommitMetaContainsMetaInformationOfACommitInTermsOfAPI,
        )

        d = src_dict.copy()
        _commit = d.pop("commit", UNSET)
        commit: Union[Unset, CommitMetaContainsMetaInformationOfACommitInTermsOfAPI]
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = CommitMetaContainsMetaInformationOfACommitInTermsOfAPI.from_dict(_commit)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        tarball_url = d.pop("tarball_url", UNSET)

        zipball_url = d.pop("zipball_url", UNSET)

        tag = cls(
            commit=commit,
            id=id,
            message=message,
            name=name,
            tarball_url=tarball_url,
            zipball_url=zipball_url,
        )

        tag.additional_properties = d
        return tag

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
