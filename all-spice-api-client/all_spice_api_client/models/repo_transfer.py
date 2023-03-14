from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team import Team
    from ..models.user import User


T = TypeVar("T", bound="RepoTransfer")


@attr.s(auto_attribs=True)
class RepoTransfer:
    """RepoTransfer represents a pending repo transfer

    Attributes:
        doer (Union[Unset, User]): User represents a user
        recipient (Union[Unset, User]): User represents a user
        teams (Union[Unset, List['Team']]):
    """

    doer: Union[Unset, "User"] = UNSET
    recipient: Union[Unset, "User"] = UNSET
    teams: Union[Unset, List["Team"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doer, Unset):
            doer = self.doer.to_dict()

        recipient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.to_dict()

        teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()

                teams.append(teams_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doer is not UNSET:
            field_dict["doer"] = doer
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team import Team
        from ..models.user import User

        d = src_dict.copy()
        _doer = d.pop("doer", UNSET)
        doer: Union[Unset, User]
        if isinstance(_doer, Unset):
            doer = UNSET
        else:
            doer = User.from_dict(_doer)

        _recipient = d.pop("recipient", UNSET)
        recipient: Union[Unset, User]
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = User.from_dict(_recipient)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = Team.from_dict(teams_item_data)

            teams.append(teams_item)

        repo_transfer = cls(
            doer=doer,
            recipient=recipient,
            teams=teams,
        )

        repo_transfer.additional_properties = d
        return repo_transfer

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
