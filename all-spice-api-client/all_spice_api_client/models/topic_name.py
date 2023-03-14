from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopicName")


@attr.s(auto_attribs=True)
class TopicName:
    """TopicName a list of repo topic names

    Attributes:
        topics (Union[Unset, List[str]]):
    """

    topics: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        topics: Union[Unset, List[str]] = UNSET
        if not isinstance(self.topics, Unset):
            topics = self.topics

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if topics is not UNSET:
            field_dict["topics"] = topics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        topics = cast(List[str], d.pop("topics", UNSET))

        topic_name = cls(
            topics=topics,
        )

        topic_name.additional_properties = d
        return topic_name

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
