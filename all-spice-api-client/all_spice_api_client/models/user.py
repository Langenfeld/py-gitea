import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """User represents a user

    Attributes:
        active (Union[Unset, bool]): Is user active
        avatar_url (Union[Unset, str]): URL to the user's avatar
        created (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]): the user's description
        email (Union[Unset, str]):
        followers_count (Union[Unset, int]): user counts
        following_count (Union[Unset, int]):
        full_name (Union[Unset, str]): the user's full name
        id (Union[Unset, int]): the user's id
        is_admin (Union[Unset, bool]): Is the user an administrator
        language (Union[Unset, str]): User locale
        last_login (Union[Unset, datetime.datetime]):
        location (Union[Unset, str]): the user's location
        login (Union[Unset, str]): the user's username
        login_name (Union[Unset, str]): the user's authentication sign-in name. Default: 'empty'.
        prohibit_login (Union[Unset, bool]): Is user login prohibited
        restricted (Union[Unset, bool]): Is user restricted
        starred_repos_count (Union[Unset, int]):
        visibility (Union[Unset, str]): User visibility level option: public, limited, private
        website (Union[Unset, str]): the user's website
    """

    active: Union[Unset, bool] = UNSET
    avatar_url: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    followers_count: Union[Unset, int] = UNSET
    following_count: Union[Unset, int] = UNSET
    full_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_admin: Union[Unset, bool] = UNSET
    language: Union[Unset, str] = UNSET
    last_login: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, str] = UNSET
    login: Union[Unset, str] = UNSET
    login_name: Union[Unset, str] = "empty"
    prohibit_login: Union[Unset, bool] = UNSET
    restricted: Union[Unset, bool] = UNSET
    starred_repos_count: Union[Unset, int] = UNSET
    visibility: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        avatar_url = self.avatar_url
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        description = self.description
        email = self.email
        followers_count = self.followers_count
        following_count = self.following_count
        full_name = self.full_name
        id = self.id
        is_admin = self.is_admin
        language = self.language
        last_login: Union[Unset, str] = UNSET
        if not isinstance(self.last_login, Unset):
            last_login = self.last_login.isoformat()

        location = self.location
        login = self.login
        login_name = self.login_name
        prohibit_login = self.prohibit_login
        restricted = self.restricted
        starred_repos_count = self.starred_repos_count
        visibility = self.visibility
        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if created is not UNSET:
            field_dict["created"] = created
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if followers_count is not UNSET:
            field_dict["followers_count"] = followers_count
        if following_count is not UNSET:
            field_dict["following_count"] = following_count
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if id is not UNSET:
            field_dict["id"] = id
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin
        if language is not UNSET:
            field_dict["language"] = language
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if location is not UNSET:
            field_dict["location"] = location
        if login is not UNSET:
            field_dict["login"] = login
        if login_name is not UNSET:
            field_dict["login_name"] = login_name
        if prohibit_login is not UNSET:
            field_dict["prohibit_login"] = prohibit_login
        if restricted is not UNSET:
            field_dict["restricted"] = restricted
        if starred_repos_count is not UNSET:
            field_dict["starred_repos_count"] = starred_repos_count
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active = d.pop("active", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        followers_count = d.pop("followers_count", UNSET)

        following_count = d.pop("following_count", UNSET)

        full_name = d.pop("full_name", UNSET)

        id = d.pop("id", UNSET)

        is_admin = d.pop("is_admin", UNSET)

        language = d.pop("language", UNSET)

        _last_login = d.pop("last_login", UNSET)
        last_login: Union[Unset, datetime.datetime]
        if isinstance(_last_login, Unset):
            last_login = UNSET
        else:
            last_login = isoparse(_last_login)

        location = d.pop("location", UNSET)

        login = d.pop("login", UNSET)

        login_name = d.pop("login_name", UNSET)

        prohibit_login = d.pop("prohibit_login", UNSET)

        restricted = d.pop("restricted", UNSET)

        starred_repos_count = d.pop("starred_repos_count", UNSET)

        visibility = d.pop("visibility", UNSET)

        website = d.pop("website", UNSET)

        user = cls(
            active=active,
            avatar_url=avatar_url,
            created=created,
            description=description,
            email=email,
            followers_count=followers_count,
            following_count=following_count,
            full_name=full_name,
            id=id,
            is_admin=is_admin,
            language=language,
            last_login=last_login,
            location=location,
            login=login,
            login_name=login_name,
            prohibit_login=prohibit_login,
            restricted=restricted,
            starred_repos_count=starred_repos_count,
            visibility=visibility,
            website=website,
        )

        user.additional_properties = d
        return user

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
