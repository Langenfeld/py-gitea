from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_pull_review_comment import CreatePullReviewComment


T = TypeVar("T", bound="CreatePullReviewOptions")


@attr.s(auto_attribs=True)
class CreatePullReviewOptions:
    """CreatePullReviewOptions are options to create a pull review

    Attributes:
        body (Union[Unset, str]):
        comments (Union[Unset, List['CreatePullReviewComment']]):
        commit_id (Union[Unset, str]):
        event (Union[Unset, str]): ReviewStateType review state type
    """

    body: Union[Unset, str] = UNSET
    comments: Union[Unset, List["CreatePullReviewComment"]] = UNSET
    commit_id: Union[Unset, str] = UNSET
    event: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        comments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()

                comments.append(comments_item)

        commit_id = self.commit_id
        event = self.event

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if comments is not UNSET:
            field_dict["comments"] = comments
        if commit_id is not UNSET:
            field_dict["commit_id"] = commit_id
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_pull_review_comment import CreatePullReviewComment

        d = src_dict.copy()
        body = d.pop("body", UNSET)

        comments = []
        _comments = d.pop("comments", UNSET)
        for comments_item_data in _comments or []:
            comments_item = CreatePullReviewComment.from_dict(comments_item_data)

            comments.append(comments_item)

        commit_id = d.pop("commit_id", UNSET)

        event = d.pop("event", UNSET)

        create_pull_review_options = cls(
            body=body,
            comments=comments,
            commit_id=commit_id,
            event=event,
        )

        create_pull_review_options.additional_properties = d
        return create_pull_review_options

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
