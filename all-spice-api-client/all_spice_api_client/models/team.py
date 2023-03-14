from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.team_permission import TeamPermission
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization import Organization
    from ..models.team_units_map import TeamUnitsMap


T = TypeVar("T", bound="Team")


@attr.s(auto_attribs=True)
class Team:
    """Team represents a team in an organization

    Attributes:
        can_create_org_repo (Union[Unset, bool]):
        description (Union[Unset, str]):
        id (Union[Unset, int]):
        includes_all_repositories (Union[Unset, bool]):
        name (Union[Unset, str]):
        organization (Union[Unset, Organization]): Organization represents an organization
        permission (Union[Unset, TeamPermission]):
        units (Union[Unset, List[str]]):  Example: ['repo.code', 'repo.issues', 'repo.ext_issues', 'repo.wiki',
            'repo.pulls', 'repo.releases', 'repo.projects', 'repo.ext_wiki'].
        units_map (Union[Unset, TeamUnitsMap]):  Example: {'repo.code': 'read', 'repo.ext_issues': 'none',
            'repo.ext_wiki': 'none', 'repo.issues': 'write', 'repo.projects': 'none', 'repo.pulls': 'owner',
            'repo.releases': 'none', 'repo.wiki': 'admin'}.
    """

    can_create_org_repo: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    includes_all_repositories: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    organization: Union[Unset, "Organization"] = UNSET
    permission: Union[Unset, TeamPermission] = UNSET
    units: Union[Unset, List[str]] = UNSET
    units_map: Union[Unset, "TeamUnitsMap"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_create_org_repo = self.can_create_org_repo
        description = self.description
        id = self.id
        includes_all_repositories = self.includes_all_repositories
        name = self.name
        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        permission: Union[Unset, str] = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        units: Union[Unset, List[str]] = UNSET
        if not isinstance(self.units, Unset):
            units = self.units

        units_map: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.units_map, Unset):
            units_map = self.units_map.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_create_org_repo is not UNSET:
            field_dict["can_create_org_repo"] = can_create_org_repo
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if includes_all_repositories is not UNSET:
            field_dict["includes_all_repositories"] = includes_all_repositories
        if name is not UNSET:
            field_dict["name"] = name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if permission is not UNSET:
            field_dict["permission"] = permission
        if units is not UNSET:
            field_dict["units"] = units
        if units_map is not UNSET:
            field_dict["units_map"] = units_map

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization import Organization
        from ..models.team_units_map import TeamUnitsMap

        d = src_dict.copy()
        can_create_org_repo = d.pop("can_create_org_repo", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        includes_all_repositories = d.pop("includes_all_repositories", UNSET)

        name = d.pop("name", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, Organization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = Organization.from_dict(_organization)

        _permission = d.pop("permission", UNSET)
        permission: Union[Unset, TeamPermission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = TeamPermission(_permission)

        units = cast(List[str], d.pop("units", UNSET))

        _units_map = d.pop("units_map", UNSET)
        units_map: Union[Unset, TeamUnitsMap]
        if isinstance(_units_map, Unset):
            units_map = UNSET
        else:
            units_map = TeamUnitsMap.from_dict(_units_map)

        team = cls(
            can_create_org_repo=can_create_org_repo,
            description=description,
            id=id,
            includes_all_repositories=includes_all_repositories,
            name=name,
            organization=organization,
            permission=permission,
            units=units,
            units_map=units_map,
        )

        team.additional_properties = d
        return team

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
