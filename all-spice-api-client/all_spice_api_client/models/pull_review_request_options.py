from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullReviewRequestOptions")


@attr.s(auto_attribs=True)
class PullReviewRequestOptions:
    """PullReviewRequestOptions are options to add or remove pull review requests

    Attributes:
        reviewers (Union[Unset, List[str]]):
        team_reviewers (Union[Unset, List[str]]):
    """

    reviewers: Union[Unset, List[str]] = UNSET
    team_reviewers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reviewers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.reviewers, Unset):
            reviewers = self.reviewers

        team_reviewers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.team_reviewers, Unset):
            team_reviewers = self.team_reviewers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if team_reviewers is not UNSET:
            field_dict["team_reviewers"] = team_reviewers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reviewers = cast(List[str], d.pop("reviewers", UNSET))

        team_reviewers = cast(List[str], d.pop("team_reviewers", UNSET))

        pull_review_request_options = cls(
            reviewers=reviewers,
            team_reviewers=team_reviewers,
        )

        pull_review_request_options.additional_properties = d
        return pull_review_request_options

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
