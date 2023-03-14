import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gpg_key_email import GPGKeyEmail


T = TypeVar("T", bound="GPGKey")


@attr.s(auto_attribs=True)
class GPGKey:
    """GPGKey a user GPG key to sign commit and tag in repository

    Attributes:
        can_certify (Union[Unset, bool]):
        can_encrypt_comms (Union[Unset, bool]):
        can_encrypt_storage (Union[Unset, bool]):
        can_sign (Union[Unset, bool]):
        created_at (Union[Unset, datetime.datetime]):
        emails (Union[Unset, List['GPGKeyEmail']]):
        expires_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, int]):
        key_id (Union[Unset, str]):
        primary_key_id (Union[Unset, str]):
        public_key (Union[Unset, str]):
        subkeys (Union[Unset, List['GPGKey']]):
        verified (Union[Unset, bool]):
    """

    can_certify: Union[Unset, bool] = UNSET
    can_encrypt_comms: Union[Unset, bool] = UNSET
    can_encrypt_storage: Union[Unset, bool] = UNSET
    can_sign: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    emails: Union[Unset, List["GPGKeyEmail"]] = UNSET
    expires_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    key_id: Union[Unset, str] = UNSET
    primary_key_id: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    subkeys: Union[Unset, List["GPGKey"]] = UNSET
    verified: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_certify = self.can_certify
        can_encrypt_comms = self.can_encrypt_comms
        can_encrypt_storage = self.can_encrypt_storage
        can_sign = self.can_sign
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        emails: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()

                emails.append(emails_item)

        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        id = self.id
        key_id = self.key_id
        primary_key_id = self.primary_key_id
        public_key = self.public_key
        subkeys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subkeys, Unset):
            subkeys = []
            for subkeys_item_data in self.subkeys:
                subkeys_item = subkeys_item_data.to_dict()

                subkeys.append(subkeys_item)

        verified = self.verified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_certify is not UNSET:
            field_dict["can_certify"] = can_certify
        if can_encrypt_comms is not UNSET:
            field_dict["can_encrypt_comms"] = can_encrypt_comms
        if can_encrypt_storage is not UNSET:
            field_dict["can_encrypt_storage"] = can_encrypt_storage
        if can_sign is not UNSET:
            field_dict["can_sign"] = can_sign
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if emails is not UNSET:
            field_dict["emails"] = emails
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if key_id is not UNSET:
            field_dict["key_id"] = key_id
        if primary_key_id is not UNSET:
            field_dict["primary_key_id"] = primary_key_id
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if subkeys is not UNSET:
            field_dict["subkeys"] = subkeys
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gpg_key_email import GPGKeyEmail

        d = src_dict.copy()
        can_certify = d.pop("can_certify", UNSET)

        can_encrypt_comms = d.pop("can_encrypt_comms", UNSET)

        can_encrypt_storage = d.pop("can_encrypt_storage", UNSET)

        can_sign = d.pop("can_sign", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        emails = []
        _emails = d.pop("emails", UNSET)
        for emails_item_data in _emails or []:
            emails_item = GPGKeyEmail.from_dict(emails_item_data)

            emails.append(emails_item)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: Union[Unset, datetime.datetime]
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        id = d.pop("id", UNSET)

        key_id = d.pop("key_id", UNSET)

        primary_key_id = d.pop("primary_key_id", UNSET)

        public_key = d.pop("public_key", UNSET)

        subkeys = []
        _subkeys = d.pop("subkeys", UNSET)
        for subkeys_item_data in _subkeys or []:
            subkeys_item = GPGKey.from_dict(subkeys_item_data)

            subkeys.append(subkeys_item)

        verified = d.pop("verified", UNSET)

        gpg_key = cls(
            can_certify=can_certify,
            can_encrypt_comms=can_encrypt_comms,
            can_encrypt_storage=can_encrypt_storage,
            can_sign=can_sign,
            created_at=created_at,
            emails=emails,
            expires_at=expires_at,
            id=id,
            key_id=key_id,
            primary_key_id=primary_key_id,
            public_key=public_key,
            subkeys=subkeys,
            verified=verified,
        )

        gpg_key.additional_properties = d
        return gpg_key

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
