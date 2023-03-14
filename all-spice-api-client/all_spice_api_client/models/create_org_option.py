from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.create_org_option_visibility import CreateOrgOptionVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOrgOption")


@attr.s(auto_attribs=True)
class CreateOrgOption:
    """CreateOrgOption options for creating an organization

    Attributes:
        username (str):
        description (Union[Unset, str]):
        full_name (Union[Unset, str]):
        location (Union[Unset, str]):
        repo_admin_change_team_access (Union[Unset, bool]):
        visibility (Union[Unset, CreateOrgOptionVisibility]): possible values are `public` (default), `limited` or
            `private`
        website (Union[Unset, str]):
    """

    username: str
    description: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    repo_admin_change_team_access: Union[Unset, bool] = UNSET
    visibility: Union[Unset, CreateOrgOptionVisibility] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        description = self.description
        full_name = self.full_name
        location = self.location
        repo_admin_change_team_access = self.repo_admin_change_team_access
        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if location is not UNSET:
            field_dict["location"] = location
        if repo_admin_change_team_access is not UNSET:
            field_dict["repo_admin_change_team_access"] = repo_admin_change_team_access
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        description = d.pop("description", UNSET)

        full_name = d.pop("full_name", UNSET)

        location = d.pop("location", UNSET)

        repo_admin_change_team_access = d.pop("repo_admin_change_team_access", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, CreateOrgOptionVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = CreateOrgOptionVisibility(_visibility)

        website = d.pop("website", UNSET)

        create_org_option = cls(
            username=username,
            description=description,
            full_name=full_name,
            location=location,
            repo_admin_change_team_access=repo_admin_change_team_access,
            visibility=visibility,
            website=website,
        )

        create_org_option.additional_properties = d
        return create_org_option

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
