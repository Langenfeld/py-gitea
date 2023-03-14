from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferRepoOption")


@attr.s(auto_attribs=True)
class TransferRepoOption:
    """TransferRepoOption options when transfer a repository's ownership

    Attributes:
        new_owner (str):
        team_ids (Union[Unset, List[int]]): ID of the team or teams to add to the repository. Teams can only be added to
            organization-owned repositories.
    """

    new_owner: str
    team_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_owner = self.new_owner
        team_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new_owner": new_owner,
            }
        )
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_owner = d.pop("new_owner")

        team_ids = cast(List[int], d.pop("team_ids", UNSET))

        transfer_repo_option = cls(
            new_owner=new_owner,
            team_ids=team_ids,
        )

        transfer_repo_option.additional_properties = d
        return transfer_repo_option

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
