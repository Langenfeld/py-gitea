from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DismissPullReviewOptions")


@attr.s(auto_attribs=True)
class DismissPullReviewOptions:
    """DismissPullReviewOptions are options to dismiss a pull review

    Attributes:
        message (Union[Unset, str]):
        priors (Union[Unset, bool]):
    """

    message: Union[Unset, str] = UNSET
    priors: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        priors = self.priors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if priors is not UNSET:
            field_dict["priors"] = priors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        priors = d.pop("priors", UNSET)

        dismiss_pull_review_options = cls(
            message=message,
            priors=priors,
        )

        dismiss_pull_review_options.additional_properties = d
        return dismiss_pull_review_options

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
