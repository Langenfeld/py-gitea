from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserOption")


@attr.s(auto_attribs=True)
class CreateUserOption:
    """CreateUserOption create user options

    Attributes:
        email (str):
        password (str):
        username (str):
        full_name (Union[Unset, str]):
        login_name (Union[Unset, str]):
        must_change_password (Union[Unset, bool]):
        restricted (Union[Unset, bool]):
        send_notify (Union[Unset, bool]):
        source_id (Union[Unset, int]):
        visibility (Union[Unset, str]):
    """

    email: str
    password: str
    username: str
    full_name: Union[Unset, str] = UNSET
    login_name: Union[Unset, str] = UNSET
    must_change_password: Union[Unset, bool] = UNSET
    restricted: Union[Unset, bool] = UNSET
    send_notify: Union[Unset, bool] = UNSET
    source_id: Union[Unset, int] = UNSET
    visibility: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        password = self.password
        username = self.username
        full_name = self.full_name
        login_name = self.login_name
        must_change_password = self.must_change_password
        restricted = self.restricted
        send_notify = self.send_notify
        source_id = self.source_id
        visibility = self.visibility

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password": password,
                "username": username,
            }
        )
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if login_name is not UNSET:
            field_dict["login_name"] = login_name
        if must_change_password is not UNSET:
            field_dict["must_change_password"] = must_change_password
        if restricted is not UNSET:
            field_dict["restricted"] = restricted
        if send_notify is not UNSET:
            field_dict["send_notify"] = send_notify
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        password = d.pop("password")

        username = d.pop("username")

        full_name = d.pop("full_name", UNSET)

        login_name = d.pop("login_name", UNSET)

        must_change_password = d.pop("must_change_password", UNSET)

        restricted = d.pop("restricted", UNSET)

        send_notify = d.pop("send_notify", UNSET)

        source_id = d.pop("source_id", UNSET)

        visibility = d.pop("visibility", UNSET)

        create_user_option = cls(
            email=email,
            password=password,
            username=username,
            full_name=full_name,
            login_name=login_name,
            must_change_password=must_change_password,
            restricted=restricted,
            send_notify=send_notify,
            source_id=source_id,
            visibility=visibility,
        )

        create_user_option.additional_properties = d
        return create_user_option

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
