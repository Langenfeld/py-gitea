from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TeamUnitsMap")


@attr.s(auto_attribs=True)
class TeamUnitsMap:
    """
    Example:
        {'repo.code': 'read', 'repo.ext_issues': 'none', 'repo.ext_wiki': 'none', 'repo.issues': 'write',
            'repo.projects': 'none', 'repo.pulls': 'owner', 'repo.releases': 'none', 'repo.wiki': 'admin'}

    """

    additional_properties: Dict[str, str] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        team_units_map = cls()

        team_units_map.additional_properties = d
        return team_units_map

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
