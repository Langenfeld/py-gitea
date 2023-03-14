from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_form_field import IssueFormField


T = TypeVar("T", bound="IssueTemplate")


@attr.s(auto_attribs=True)
class IssueTemplate:
    """IssueTemplate represents an issue template for a repository

    Attributes:
        about (Union[Unset, str]):
        body (Union[Unset, List['IssueFormField']]):
        content (Union[Unset, str]):
        file_name (Union[Unset, str]):
        labels (Union[Unset, List[str]]):
        name (Union[Unset, str]):
        ref (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    about: Union[Unset, str] = UNSET
    body: Union[Unset, List["IssueFormField"]] = UNSET
    content: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    labels: Union[Unset, List[str]] = UNSET
    name: Union[Unset, str] = UNSET
    ref: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        about = self.about
        body: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.body, Unset):
            body = []
            for body_item_data in self.body:
                body_item = body_item_data.to_dict()

                body.append(body_item)

        content = self.content
        file_name = self.file_name
        labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        name = self.name
        ref = self.ref
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if about is not UNSET:
            field_dict["about"] = about
        if body is not UNSET:
            field_dict["body"] = body
        if content is not UNSET:
            field_dict["content"] = content
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if ref is not UNSET:
            field_dict["ref"] = ref
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.issue_form_field import IssueFormField

        d = src_dict.copy()
        about = d.pop("about", UNSET)

        body = []
        _body = d.pop("body", UNSET)
        for body_item_data in _body or []:
            body_item = IssueFormField.from_dict(body_item_data)

            body.append(body_item)

        content = d.pop("content", UNSET)

        file_name = d.pop("file_name", UNSET)

        labels = cast(List[str], d.pop("labels", UNSET))

        name = d.pop("name", UNSET)

        ref = d.pop("ref", UNSET)

        title = d.pop("title", UNSET)

        issue_template = cls(
            about=about,
            body=body,
            content=content,
            file_name=file_name,
            labels=labels,
            name=name,
            ref=ref,
            title=title,
        )

        issue_template.additional_properties = d
        return issue_template

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
