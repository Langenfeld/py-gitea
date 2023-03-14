from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationSubject")


@attr.s(auto_attribs=True)
class NotificationSubject:
    """NotificationSubject contains the notification subject (Issue/Pull/Commit)

    Attributes:
        html_url (Union[Unset, str]):
        latest_comment_html_url (Union[Unset, str]):
        latest_comment_url (Union[Unset, str]):
        state (Union[Unset, str]): StateType issue state type
        title (Union[Unset, str]):
        type (Union[Unset, str]): NotifySubjectType represent type of notification subject
        url (Union[Unset, str]):
    """

    html_url: Union[Unset, str] = UNSET
    latest_comment_html_url: Union[Unset, str] = UNSET
    latest_comment_url: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        html_url = self.html_url
        latest_comment_html_url = self.latest_comment_html_url
        latest_comment_url = self.latest_comment_url
        state = self.state
        title = self.title
        type = self.type
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if latest_comment_html_url is not UNSET:
            field_dict["latest_comment_html_url"] = latest_comment_html_url
        if latest_comment_url is not UNSET:
            field_dict["latest_comment_url"] = latest_comment_url
        if state is not UNSET:
            field_dict["state"] = state
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        html_url = d.pop("html_url", UNSET)

        latest_comment_html_url = d.pop("latest_comment_html_url", UNSET)

        latest_comment_url = d.pop("latest_comment_url", UNSET)

        state = d.pop("state", UNSET)

        title = d.pop("title", UNSET)

        type = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        notification_subject = cls(
            html_url=html_url,
            latest_comment_html_url=latest_comment_html_url,
            latest_comment_url=latest_comment_url,
            state=state,
            title=title,
            type=type,
            url=url,
        )

        notification_subject.additional_properties = d
        return notification_subject

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
