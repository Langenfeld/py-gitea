import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository import Repository
    from ..models.user import User


T = TypeVar("T", bound="Package")


@attr.s(auto_attribs=True)
class Package:
    """Package represents a package

    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        creator (Union[Unset, User]): User represents a user
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        owner (Union[Unset, User]): User represents a user
        repository (Union[Unset, Repository]): Repository represents a repository
        type (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    creator: Union[Unset, "User"] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    owner: Union[Unset, "User"] = UNSET
    repository: Union[Unset, "Repository"] = UNSET
    type: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        creator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        id = self.id
        name = self.name
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        repository: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        type = self.type
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if creator is not UNSET:
            field_dict["creator"] = creator
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if repository is not UNSET:
            field_dict["repository"] = repository
        if type is not UNSET:
            field_dict["type"] = type
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.repository import Repository
        from ..models.user import User

        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _creator = d.pop("creator", UNSET)
        creator: Union[Unset, User]
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = User.from_dict(_creator)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, User]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = User.from_dict(_owner)

        _repository = d.pop("repository", UNSET)
        repository: Union[Unset, Repository]
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        type = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        package = cls(
            created_at=created_at,
            creator=creator,
            id=id,
            name=name,
            owner=owner,
            repository=repository,
            type=type,
            version=version,
        )

        package.additional_properties = d
        return package

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
