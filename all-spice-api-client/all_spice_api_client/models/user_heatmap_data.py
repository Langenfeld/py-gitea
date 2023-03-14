from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserHeatmapData")


@attr.s(auto_attribs=True)
class UserHeatmapData:
    """UserHeatmapData represents the data needed to create a heatmap

    Attributes:
        contributions (Union[Unset, int]):
        timestamp (Union[Unset, int]): TimeStamp defines a timestamp
    """

    contributions: Union[Unset, int] = UNSET
    timestamp: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contributions = self.contributions
        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contributions is not UNSET:
            field_dict["contributions"] = contributions
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contributions = d.pop("contributions", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        user_heatmap_data = cls(
            contributions=contributions,
            timestamp=timestamp,
        )

        user_heatmap_data.additional_properties = d
        return user_heatmap_data

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
