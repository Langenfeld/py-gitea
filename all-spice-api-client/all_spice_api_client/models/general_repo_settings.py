from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeneralRepoSettings")


@attr.s(auto_attribs=True)
class GeneralRepoSettings:
    """GeneralRepoSettings contains global repository settings exposed by API

    Attributes:
        http_git_disabled (Union[Unset, bool]):
        lfs_disabled (Union[Unset, bool]):
        migrations_disabled (Union[Unset, bool]):
        mirrors_disabled (Union[Unset, bool]):
        stars_disabled (Union[Unset, bool]):
        time_tracking_disabled (Union[Unset, bool]):
    """

    http_git_disabled: Union[Unset, bool] = UNSET
    lfs_disabled: Union[Unset, bool] = UNSET
    migrations_disabled: Union[Unset, bool] = UNSET
    mirrors_disabled: Union[Unset, bool] = UNSET
    stars_disabled: Union[Unset, bool] = UNSET
    time_tracking_disabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        http_git_disabled = self.http_git_disabled
        lfs_disabled = self.lfs_disabled
        migrations_disabled = self.migrations_disabled
        mirrors_disabled = self.mirrors_disabled
        stars_disabled = self.stars_disabled
        time_tracking_disabled = self.time_tracking_disabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if http_git_disabled is not UNSET:
            field_dict["http_git_disabled"] = http_git_disabled
        if lfs_disabled is not UNSET:
            field_dict["lfs_disabled"] = lfs_disabled
        if migrations_disabled is not UNSET:
            field_dict["migrations_disabled"] = migrations_disabled
        if mirrors_disabled is not UNSET:
            field_dict["mirrors_disabled"] = mirrors_disabled
        if stars_disabled is not UNSET:
            field_dict["stars_disabled"] = stars_disabled
        if time_tracking_disabled is not UNSET:
            field_dict["time_tracking_disabled"] = time_tracking_disabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        http_git_disabled = d.pop("http_git_disabled", UNSET)

        lfs_disabled = d.pop("lfs_disabled", UNSET)

        migrations_disabled = d.pop("migrations_disabled", UNSET)

        mirrors_disabled = d.pop("mirrors_disabled", UNSET)

        stars_disabled = d.pop("stars_disabled", UNSET)

        time_tracking_disabled = d.pop("time_tracking_disabled", UNSET)

        general_repo_settings = cls(
            http_git_disabled=http_git_disabled,
            lfs_disabled=lfs_disabled,
            migrations_disabled=migrations_disabled,
            mirrors_disabled=mirrors_disabled,
            stars_disabled=stars_disabled,
            time_tracking_disabled=time_tracking_disabled,
        )

        general_repo_settings.additional_properties = d
        return general_repo_settings

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
