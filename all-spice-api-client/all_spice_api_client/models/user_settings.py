from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSettings")


@attr.s(auto_attribs=True)
class UserSettings:
    """UserSettings represents user settings

    Attributes:
        description (Union[Unset, str]):
        diff_view_style (Union[Unset, str]):
        full_name (Union[Unset, str]):
        hide_activity (Union[Unset, bool]):
        hide_email (Union[Unset, bool]): Privacy
        language (Union[Unset, str]):
        location (Union[Unset, str]):
        theme (Union[Unset, str]):
        website (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    diff_view_style: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    hide_activity: Union[Unset, bool] = UNSET
    hide_email: Union[Unset, bool] = UNSET
    language: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    theme: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        diff_view_style = self.diff_view_style
        full_name = self.full_name
        hide_activity = self.hide_activity
        hide_email = self.hide_email
        language = self.language
        location = self.location
        theme = self.theme
        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if diff_view_style is not UNSET:
            field_dict["diff_view_style"] = diff_view_style
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if hide_activity is not UNSET:
            field_dict["hide_activity"] = hide_activity
        if hide_email is not UNSET:
            field_dict["hide_email"] = hide_email
        if language is not UNSET:
            field_dict["language"] = language
        if location is not UNSET:
            field_dict["location"] = location
        if theme is not UNSET:
            field_dict["theme"] = theme
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        diff_view_style = d.pop("diff_view_style", UNSET)

        full_name = d.pop("full_name", UNSET)

        hide_activity = d.pop("hide_activity", UNSET)

        hide_email = d.pop("hide_email", UNSET)

        language = d.pop("language", UNSET)

        location = d.pop("location", UNSET)

        theme = d.pop("theme", UNSET)

        website = d.pop("website", UNSET)

        user_settings = cls(
            description=description,
            diff_view_style=diff_view_style,
            full_name=full_name,
            hide_activity=hide_activity,
            hide_email=hide_email,
            language=language,
            location=location,
            theme=theme,
            website=website,
        )

        user_settings.additional_properties = d
        return user_settings

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
