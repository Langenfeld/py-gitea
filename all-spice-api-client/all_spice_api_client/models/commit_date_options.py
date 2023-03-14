import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitDateOptions")


@attr.s(auto_attribs=True)
class CommitDateOptions:
    """CommitDateOptions store dates for GIT_AUTHOR_DATE and GIT_COMMITTER_DATE

    Attributes:
        author (Union[Unset, datetime.datetime]):
        committer (Union[Unset, datetime.datetime]):
    """

    author: Union[Unset, datetime.datetime] = UNSET
    committer: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        author: Union[Unset, str] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.isoformat()

        committer: Union[Unset, str] = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if committer is not UNSET:
            field_dict["committer"] = committer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _author = d.pop("author", UNSET)
        author: Union[Unset, datetime.datetime]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = isoparse(_author)

        _committer = d.pop("committer", UNSET)
        committer: Union[Unset, datetime.datetime]
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = isoparse(_committer)

        commit_date_options = cls(
            author=author,
            committer=committer,
        )

        commit_date_options.additional_properties = d
        return commit_date_options

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
