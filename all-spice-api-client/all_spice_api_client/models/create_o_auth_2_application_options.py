from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOAuth2ApplicationOptions")


@attr.s(auto_attribs=True)
class CreateOAuth2ApplicationOptions:
    """CreateOAuth2ApplicationOptions holds options to create an oauth2 application

    Attributes:
        confidential_client (Union[Unset, bool]):
        name (Union[Unset, str]):
        redirect_uris (Union[Unset, List[str]]):
    """

    confidential_client: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    redirect_uris: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        confidential_client = self.confidential_client
        name = self.name
        redirect_uris: Union[Unset, List[str]] = UNSET
        if not isinstance(self.redirect_uris, Unset):
            redirect_uris = self.redirect_uris

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confidential_client is not UNSET:
            field_dict["confidential_client"] = confidential_client
        if name is not UNSET:
            field_dict["name"] = name
        if redirect_uris is not UNSET:
            field_dict["redirect_uris"] = redirect_uris

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        confidential_client = d.pop("confidential_client", UNSET)

        name = d.pop("name", UNSET)

        redirect_uris = cast(List[str], d.pop("redirect_uris", UNSET))

        create_o_auth_2_application_options = cls(
            confidential_client=confidential_client,
            name=name,
            redirect_uris=redirect_uris,
        )

        create_o_auth_2_application_options.additional_properties = d
        return create_o_auth_2_application_options

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
