from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Organization")


@attr.s(auto_attribs=True)
class Organization:
    """Organization represents an organization

    Attributes:
        avatar_url (Union[Unset, str]):
        description (Union[Unset, str]):
        full_name (Union[Unset, str]):
        id (Union[Unset, int]):
        location (Union[Unset, str]):
        name (Union[Unset, str]):
        repo_admin_change_team_access (Union[Unset, bool]):
        username (Union[Unset, str]): deprecated
        visibility (Union[Unset, str]):
        website (Union[Unset, str]):
    """

    avatar_url: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    repo_admin_change_team_access: Union[Unset, bool] = UNSET
    username: Union[Unset, str] = UNSET
    visibility: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avatar_url = self.avatar_url
        description = self.description
        full_name = self.full_name
        id = self.id
        location = self.location
        name = self.name
        repo_admin_change_team_access = self.repo_admin_change_team_access
        username = self.username
        visibility = self.visibility
        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if description is not UNSET:
            field_dict["description"] = description
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if repo_admin_change_team_access is not UNSET:
            field_dict["repo_admin_change_team_access"] = repo_admin_change_team_access
        if username is not UNSET:
            field_dict["username"] = username
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        avatar_url = d.pop("avatar_url", UNSET)

        description = d.pop("description", UNSET)

        full_name = d.pop("full_name", UNSET)

        id = d.pop("id", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        repo_admin_change_team_access = d.pop("repo_admin_change_team_access", UNSET)

        username = d.pop("username", UNSET)

        visibility = d.pop("visibility", UNSET)

        website = d.pop("website", UNSET)

        organization = cls(
            avatar_url=avatar_url,
            description=description,
            full_name=full_name,
            id=id,
            location=location,
            name=name,
            repo_admin_change_team_access=repo_admin_change_team_access,
            username=username,
            visibility=visibility,
            website=website,
        )

        organization.additional_properties = d
        return organization

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
