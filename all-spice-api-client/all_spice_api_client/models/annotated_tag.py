from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotated_tag_object import AnnotatedTagObject
    from ..models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit import (
        CommitUserContainsInformationOfAUserInTheContextOfACommit,
    )
    from ..models.payload_commit_verification import PayloadCommitVerification


T = TypeVar("T", bound="AnnotatedTag")


@attr.s(auto_attribs=True)
class AnnotatedTag:
    """AnnotatedTag represents an annotated tag

    Attributes:
        message (Union[Unset, str]):
        object_ (Union[Unset, AnnotatedTagObject]): AnnotatedTagObject contains meta information of the tag object
        sha (Union[Unset, str]):
        tag (Union[Unset, str]):
        tagger (Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]):
        url (Union[Unset, str]):
        verification (Union[Unset, PayloadCommitVerification]): PayloadCommitVerification represents the GPG
            verification of a commit
    """

    message: Union[Unset, str] = UNSET
    object_: Union[Unset, "AnnotatedTagObject"] = UNSET
    sha: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    tagger: Union[Unset, "CommitUserContainsInformationOfAUserInTheContextOfACommit"] = UNSET
    url: Union[Unset, str] = UNSET
    verification: Union[Unset, "PayloadCommitVerification"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        object_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.to_dict()

        sha = self.sha
        tag = self.tag
        tagger: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tagger, Unset):
            tagger = self.tagger.to_dict()

        url = self.url
        verification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if object_ is not UNSET:
            field_dict["object"] = object_
        if sha is not UNSET:
            field_dict["sha"] = sha
        if tag is not UNSET:
            field_dict["tag"] = tag
        if tagger is not UNSET:
            field_dict["tagger"] = tagger
        if url is not UNSET:
            field_dict["url"] = url
        if verification is not UNSET:
            field_dict["verification"] = verification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.annotated_tag_object import AnnotatedTagObject
        from ..models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit import (
            CommitUserContainsInformationOfAUserInTheContextOfACommit,
        )
        from ..models.payload_commit_verification import PayloadCommitVerification

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _object_ = d.pop("object", UNSET)
        object_: Union[Unset, AnnotatedTagObject]
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = AnnotatedTagObject.from_dict(_object_)

        sha = d.pop("sha", UNSET)

        tag = d.pop("tag", UNSET)

        _tagger = d.pop("tagger", UNSET)
        tagger: Union[Unset, CommitUserContainsInformationOfAUserInTheContextOfACommit]
        if isinstance(_tagger, Unset):
            tagger = UNSET
        else:
            tagger = CommitUserContainsInformationOfAUserInTheContextOfACommit.from_dict(_tagger)

        url = d.pop("url", UNSET)

        _verification = d.pop("verification", UNSET)
        verification: Union[Unset, PayloadCommitVerification]
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = PayloadCommitVerification.from_dict(_verification)

        annotated_tag = cls(
            message=message,
            object_=object_,
            sha=sha,
            tag=tag,
            tagger=tagger,
            url=url,
            verification=verification,
        )

        annotated_tag.additional_properties = d
        return annotated_tag

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
