from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalTracker")


@attr.s(auto_attribs=True)
class ExternalTracker:
    """ExternalTracker represents settings for external tracker

    Attributes:
        external_tracker_format (Union[Unset, str]): External Issue Tracker URL Format. Use the placeholders {user},
            {repo} and {index} for the username, repository name and issue index.
        external_tracker_regexp_pattern (Union[Unset, str]): External Issue Tracker issue regular expression
        external_tracker_style (Union[Unset, str]): External Issue Tracker Number Format, either `numeric`,
            `alphanumeric`, or `regexp`
        external_tracker_url (Union[Unset, str]): URL of external issue tracker.
    """

    external_tracker_format: Union[Unset, str] = UNSET
    external_tracker_regexp_pattern: Union[Unset, str] = UNSET
    external_tracker_style: Union[Unset, str] = UNSET
    external_tracker_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_tracker_format = self.external_tracker_format
        external_tracker_regexp_pattern = self.external_tracker_regexp_pattern
        external_tracker_style = self.external_tracker_style
        external_tracker_url = self.external_tracker_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_tracker_format is not UNSET:
            field_dict["external_tracker_format"] = external_tracker_format
        if external_tracker_regexp_pattern is not UNSET:
            field_dict["external_tracker_regexp_pattern"] = external_tracker_regexp_pattern
        if external_tracker_style is not UNSET:
            field_dict["external_tracker_style"] = external_tracker_style
        if external_tracker_url is not UNSET:
            field_dict["external_tracker_url"] = external_tracker_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_tracker_format = d.pop("external_tracker_format", UNSET)

        external_tracker_regexp_pattern = d.pop("external_tracker_regexp_pattern", UNSET)

        external_tracker_style = d.pop("external_tracker_style", UNSET)

        external_tracker_url = d.pop("external_tracker_url", UNSET)

        external_tracker = cls(
            external_tracker_format=external_tracker_format,
            external_tracker_regexp_pattern=external_tracker_regexp_pattern,
            external_tracker_style=external_tracker_style,
            external_tracker_url=external_tracker_url,
        )

        external_tracker.additional_properties = d
        return external_tracker

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
