import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2ApplicationRepresentsAnOAuth2Application")


@attr.s(auto_attribs=True)
class OAuth2ApplicationRepresentsAnOAuth2Application:
    """
    Attributes:
        client_id (Union[Unset, str]):
        client_secret (Union[Unset, str]):
        confidential_client (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        redirect_uris (Union[Unset, List[str]]):
    """

    client_id: Union[Unset, str] = UNSET
    client_secret: Union[Unset, str] = UNSET
    confidential_client: Union[Unset, bool] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    redirect_uris: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id
        client_secret = self.client_secret
        confidential_client = self.confidential_client
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        id = self.id
        name = self.name
        redirect_uris: Union[Unset, List[str]] = UNSET
        if not isinstance(self.redirect_uris, Unset):
            redirect_uris = self.redirect_uris

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if confidential_client is not UNSET:
            field_dict["confidential_client"] = confidential_client
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if redirect_uris is not UNSET:
            field_dict["redirect_uris"] = redirect_uris

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        confidential_client = d.pop("confidential_client", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        redirect_uris = cast(List[str], d.pop("redirect_uris", UNSET))

        o_auth_2_application_represents_an_o_auth_2_application = cls(
            client_id=client_id,
            client_secret=client_secret,
            confidential_client=confidential_client,
            created=created,
            id=id,
            name=name,
            redirect_uris=redirect_uris,
        )

        o_auth_2_application_represents_an_o_auth_2_application.additional_properties = d
        return o_auth_2_application_represents_an_o_auth_2_application

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
