from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payload_user import PayloadUser


T = TypeVar("T", bound="PayloadCommitVerification")


@attr.s(auto_attribs=True)
class PayloadCommitVerification:
    """PayloadCommitVerification represents the GPG verification of a commit

    Attributes:
        payload (Union[Unset, str]):
        reason (Union[Unset, str]):
        signature (Union[Unset, str]):
        signer (Union[Unset, PayloadUser]): PayloadUser represents the author or committer of a commit
        verified (Union[Unset, bool]):
    """

    payload: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    signature: Union[Unset, str] = UNSET
    signer: Union[Unset, "PayloadUser"] = UNSET
    verified: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payload = self.payload
        reason = self.reason
        signature = self.signature
        signer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.signer, Unset):
            signer = self.signer.to_dict()

        verified = self.verified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payload is not UNSET:
            field_dict["payload"] = payload
        if reason is not UNSET:
            field_dict["reason"] = reason
        if signature is not UNSET:
            field_dict["signature"] = signature
        if signer is not UNSET:
            field_dict["signer"] = signer
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payload_user import PayloadUser

        d = src_dict.copy()
        payload = d.pop("payload", UNSET)

        reason = d.pop("reason", UNSET)

        signature = d.pop("signature", UNSET)

        _signer = d.pop("signer", UNSET)
        signer: Union[Unset, PayloadUser]
        if isinstance(_signer, Unset):
            signer = UNSET
        else:
            signer = PayloadUser.from_dict(_signer)

        verified = d.pop("verified", UNSET)

        payload_commit_verification = cls(
            payload=payload,
            reason=reason,
            signature=signature,
            signer=signer,
            verified=verified,
        )

        payload_commit_verification.additional_properties = d
        return payload_commit_verification

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
