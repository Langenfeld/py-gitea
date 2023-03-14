from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePushMirrorOptionRepresentsNeedInformationToCreateAPushMirrorOfARepository")


@attr.s(auto_attribs=True)
class CreatePushMirrorOptionRepresentsNeedInformationToCreateAPushMirrorOfARepository:
    """
    Attributes:
        interval (Union[Unset, str]):
        remote_address (Union[Unset, str]):
        remote_password (Union[Unset, str]):
        remote_username (Union[Unset, str]):
        sync_on_commit (Union[Unset, bool]):
    """

    interval: Union[Unset, str] = UNSET
    remote_address: Union[Unset, str] = UNSET
    remote_password: Union[Unset, str] = UNSET
    remote_username: Union[Unset, str] = UNSET
    sync_on_commit: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interval = self.interval
        remote_address = self.remote_address
        remote_password = self.remote_password
        remote_username = self.remote_username
        sync_on_commit = self.sync_on_commit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interval is not UNSET:
            field_dict["interval"] = interval
        if remote_address is not UNSET:
            field_dict["remote_address"] = remote_address
        if remote_password is not UNSET:
            field_dict["remote_password"] = remote_password
        if remote_username is not UNSET:
            field_dict["remote_username"] = remote_username
        if sync_on_commit is not UNSET:
            field_dict["sync_on_commit"] = sync_on_commit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interval = d.pop("interval", UNSET)

        remote_address = d.pop("remote_address", UNSET)

        remote_password = d.pop("remote_password", UNSET)

        remote_username = d.pop("remote_username", UNSET)

        sync_on_commit = d.pop("sync_on_commit", UNSET)

        create_push_mirror_option_represents_need_information_to_create_a_push_mirror_of_a_repository = cls(
            interval=interval,
            remote_address=remote_address,
            remote_password=remote_password,
            remote_username=remote_username,
            sync_on_commit=sync_on_commit,
        )

        create_push_mirror_option_represents_need_information_to_create_a_push_mirror_of_a_repository.additional_properties = (
            d
        )
        return create_push_mirror_option_represents_need_information_to_create_a_push_mirror_of_a_repository

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
