from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalTracker")


@attr.s(auto_attribs=True)
class InternalTracker:
    """InternalTracker represents settings for internal tracker

    Attributes:
        allow_only_contributors_to_track_time (Union[Unset, bool]): Let only contributors track time (Built-in issue
            tracker)
        enable_issue_dependencies (Union[Unset, bool]): Enable dependencies for issues and pull requests (Built-in issue
            tracker)
        enable_time_tracker (Union[Unset, bool]): Enable time tracking (Built-in issue tracker)
    """

    allow_only_contributors_to_track_time: Union[Unset, bool] = UNSET
    enable_issue_dependencies: Union[Unset, bool] = UNSET
    enable_time_tracker: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_only_contributors_to_track_time = self.allow_only_contributors_to_track_time
        enable_issue_dependencies = self.enable_issue_dependencies
        enable_time_tracker = self.enable_time_tracker

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_only_contributors_to_track_time is not UNSET:
            field_dict["allow_only_contributors_to_track_time"] = allow_only_contributors_to_track_time
        if enable_issue_dependencies is not UNSET:
            field_dict["enable_issue_dependencies"] = enable_issue_dependencies
        if enable_time_tracker is not UNSET:
            field_dict["enable_time_tracker"] = enable_time_tracker

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allow_only_contributors_to_track_time = d.pop("allow_only_contributors_to_track_time", UNSET)

        enable_issue_dependencies = d.pop("enable_issue_dependencies", UNSET)

        enable_time_tracker = d.pop("enable_time_tracker", UNSET)

        internal_tracker = cls(
            allow_only_contributors_to_track_time=allow_only_contributors_to_track_time,
            enable_issue_dependencies=enable_issue_dependencies,
            enable_time_tracker=enable_time_tracker,
        )

        internal_tracker.additional_properties = d
        return internal_tracker

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
