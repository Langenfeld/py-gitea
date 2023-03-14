import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payload_commit_verification import PayloadCommitVerification
    from ..models.payload_user import PayloadUser


T = TypeVar("T", bound="PayloadCommit")


@attr.s(auto_attribs=True)
class PayloadCommit:
    """PayloadCommit represents a commit

    Attributes:
        added (Union[Unset, List[str]]):
        author (Union[Unset, PayloadUser]): PayloadUser represents the author or committer of a commit
        committer (Union[Unset, PayloadUser]): PayloadUser represents the author or committer of a commit
        id (Union[Unset, str]): sha1 hash of the commit
        message (Union[Unset, str]):
        modified (Union[Unset, List[str]]):
        removed (Union[Unset, List[str]]):
        timestamp (Union[Unset, datetime.datetime]):
        url (Union[Unset, str]):
        verification (Union[Unset, PayloadCommitVerification]): PayloadCommitVerification represents the GPG
            verification of a commit
    """

    added: Union[Unset, List[str]] = UNSET
    author: Union[Unset, "PayloadUser"] = UNSET
    committer: Union[Unset, "PayloadUser"] = UNSET
    id: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    modified: Union[Unset, List[str]] = UNSET
    removed: Union[Unset, List[str]] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    url: Union[Unset, str] = UNSET
    verification: Union[Unset, "PayloadCommitVerification"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        added: Union[Unset, List[str]] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added

        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        committer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.to_dict()

        id = self.id
        message = self.message
        modified: Union[Unset, List[str]] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified

        removed: Union[Unset, List[str]] = UNSET
        if not isinstance(self.removed, Unset):
            removed = self.removed

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        url = self.url
        verification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added is not UNSET:
            field_dict["added"] = added
        if author is not UNSET:
            field_dict["author"] = author
        if committer is not UNSET:
            field_dict["committer"] = committer
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if modified is not UNSET:
            field_dict["modified"] = modified
        if removed is not UNSET:
            field_dict["removed"] = removed
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if url is not UNSET:
            field_dict["url"] = url
        if verification is not UNSET:
            field_dict["verification"] = verification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payload_commit_verification import PayloadCommitVerification
        from ..models.payload_user import PayloadUser

        d = src_dict.copy()
        added = cast(List[str], d.pop("added", UNSET))

        _author = d.pop("author", UNSET)
        author: Union[Unset, PayloadUser]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = PayloadUser.from_dict(_author)

        _committer = d.pop("committer", UNSET)
        committer: Union[Unset, PayloadUser]
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = PayloadUser.from_dict(_committer)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        modified = cast(List[str], d.pop("modified", UNSET))

        removed = cast(List[str], d.pop("removed", UNSET))

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        url = d.pop("url", UNSET)

        _verification = d.pop("verification", UNSET)
        verification: Union[Unset, PayloadCommitVerification]
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = PayloadCommitVerification.from_dict(_verification)

        payload_commit = cls(
            added=added,
            author=author,
            committer=committer,
            id=id,
            message=message,
            modified=modified,
            removed=removed,
            timestamp=timestamp,
            url=url,
            verification=verification,
        )

        payload_commit.additional_properties = d
        return payload_commit

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
