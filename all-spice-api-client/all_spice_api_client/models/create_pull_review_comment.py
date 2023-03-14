from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePullReviewComment")


@attr.s(auto_attribs=True)
class CreatePullReviewComment:
    """CreatePullReviewComment represent a review comment for creation api

    Attributes:
        body (Union[Unset, str]):
        new_position (Union[Unset, int]): if comment to new file line or 0
        old_position (Union[Unset, int]): if comment to old file line or 0
        path (Union[Unset, str]): the tree path
    """

    body: Union[Unset, str] = UNSET
    new_position: Union[Unset, int] = UNSET
    old_position: Union[Unset, int] = UNSET
    path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        new_position = self.new_position
        old_position = self.old_position
        path = self.path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if new_position is not UNSET:
            field_dict["new_position"] = new_position
        if old_position is not UNSET:
            field_dict["old_position"] = old_position
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        body = d.pop("body", UNSET)

        new_position = d.pop("new_position", UNSET)

        old_position = d.pop("old_position", UNSET)

        path = d.pop("path", UNSET)

        create_pull_review_comment = cls(
            body=body,
            new_position=new_position,
            old_position=old_position,
            path=path,
        )

        create_pull_review_comment.additional_properties = d
        return create_pull_review_comment

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
