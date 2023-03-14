from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PushMirror")


@attr.s(auto_attribs=True)
class PushMirror:
    """PushMirror represents information of a push mirror

    Attributes:
        created (Union[Unset, str]):
        interval (Union[Unset, str]):
        last_error (Union[Unset, str]):
        last_update (Union[Unset, str]):
        remote_address (Union[Unset, str]):
        remote_name (Union[Unset, str]):
        repo_name (Union[Unset, str]):
        sync_on_commit (Union[Unset, bool]):
    """

    created: Union[Unset, str] = UNSET
    interval: Union[Unset, str] = UNSET
    last_error: Union[Unset, str] = UNSET
    last_update: Union[Unset, str] = UNSET
    remote_address: Union[Unset, str] = UNSET
    remote_name: Union[Unset, str] = UNSET
    repo_name: Union[Unset, str] = UNSET
    sync_on_commit: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created = self.created
        interval = self.interval
        last_error = self.last_error
        last_update = self.last_update
        remote_address = self.remote_address
        remote_name = self.remote_name
        repo_name = self.repo_name
        sync_on_commit = self.sync_on_commit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if interval is not UNSET:
            field_dict["interval"] = interval
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if last_update is not UNSET:
            field_dict["last_update"] = last_update
        if remote_address is not UNSET:
            field_dict["remote_address"] = remote_address
        if remote_name is not UNSET:
            field_dict["remote_name"] = remote_name
        if repo_name is not UNSET:
            field_dict["repo_name"] = repo_name
        if sync_on_commit is not UNSET:
            field_dict["sync_on_commit"] = sync_on_commit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = d.pop("created", UNSET)

        interval = d.pop("interval", UNSET)

        last_error = d.pop("last_error", UNSET)

        last_update = d.pop("last_update", UNSET)

        remote_address = d.pop("remote_address", UNSET)

        remote_name = d.pop("remote_name", UNSET)

        repo_name = d.pop("repo_name", UNSET)

        sync_on_commit = d.pop("sync_on_commit", UNSET)

        push_mirror = cls(
            created=created,
            interval=interval,
            last_error=last_error,
            last_update=last_update,
            remote_address=remote_address,
            remote_name=remote_name,
            repo_name=repo_name,
            sync_on_commit=sync_on_commit,
        )

        push_mirror.additional_properties = d
        return push_mirror

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
