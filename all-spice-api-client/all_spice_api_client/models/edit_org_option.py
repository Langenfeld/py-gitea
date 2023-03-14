from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.edit_org_option_visibility import EditOrgOptionVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditOrgOption")


@attr.s(auto_attribs=True)
class EditOrgOption:
    """EditOrgOption options for editing an organization

    Attributes:
        description (Union[Unset, str]):
        full_name (Union[Unset, str]):
        location (Union[Unset, str]):
        repo_admin_change_team_access (Union[Unset, bool]):
        visibility (Union[Unset, EditOrgOptionVisibility]): possible values are `public`, `limited` or `private`
        website (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    repo_admin_change_team_access: Union[Unset, bool] = UNSET
    visibility: Union[Unset, EditOrgOptionVisibility] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        field_dict.update({})
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
        description = d.pop("description", UNSET)

        full_name = d.pop("full_name", UNSET)

        location = d.pop("location", UNSET)

        repo_admin_change_team_access = d.pop("repo_admin_change_team_access", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, EditOrgOptionVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = EditOrgOptionVisibility(_visibility)

        website = d.pop("website", UNSET)

        edit_org_option = cls(
            description=description,
            full_name=full_name,
            location=location,
            repo_admin_change_team_access=repo_admin_change_team_access,
            visibility=visibility,
            website=website,
        )

        edit_org_option.additional_properties = d
        return edit_org_option

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
