from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmitPullReviewOptions")


@attr.s(auto_attribs=True)
class SubmitPullReviewOptions:
    """SubmitPullReviewOptions are options to submit a pending pull review

    Attributes:
        body (Union[Unset, str]):
        event (Union[Unset, str]): ReviewStateType review state type
    """

    body: Union[Unset, str] = UNSET
    event: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        event = self.event

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        body = d.pop("body", UNSET)

        event = d.pop("event", UNSET)

        submit_pull_review_options = cls(
            body=body,
            event=event,
        )

        submit_pull_review_options.additional_properties = d
        return submit_pull_review_options

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
