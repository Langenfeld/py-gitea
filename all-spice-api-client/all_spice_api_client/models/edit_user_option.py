from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditUserOption")


@attr.s(auto_attribs=True)
class EditUserOption:
    """EditUserOption edit user options

    Attributes:
        login_name (str):
        source_id (int):
        active (Union[Unset, bool]):
        admin (Union[Unset, bool]):
        allow_create_organization (Union[Unset, bool]):
        allow_git_hook (Union[Unset, bool]):
        allow_import_local (Union[Unset, bool]):
        description (Union[Unset, str]):
        email (Union[Unset, str]):
        full_name (Union[Unset, str]):
        location (Union[Unset, str]):
        max_repo_creation (Union[Unset, int]):
        must_change_password (Union[Unset, bool]):
        password (Union[Unset, str]):
        prohibit_login (Union[Unset, bool]):
        restricted (Union[Unset, bool]):
        visibility (Union[Unset, str]):
        website (Union[Unset, str]):
    """

    login_name: str
    source_id: int
    active: Union[Unset, bool] = UNSET
    admin: Union[Unset, bool] = UNSET
    allow_create_organization: Union[Unset, bool] = UNSET
    allow_git_hook: Union[Unset, bool] = UNSET
    allow_import_local: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    max_repo_creation: Union[Unset, int] = UNSET
    must_change_password: Union[Unset, bool] = UNSET
    password: Union[Unset, str] = UNSET
    prohibit_login: Union[Unset, bool] = UNSET
    restricted: Union[Unset, bool] = UNSET
    visibility: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login_name = self.login_name
        source_id = self.source_id
        active = self.active
        admin = self.admin
        allow_create_organization = self.allow_create_organization
        allow_git_hook = self.allow_git_hook
        allow_import_local = self.allow_import_local
        description = self.description
        email = self.email
        full_name = self.full_name
        location = self.location
        max_repo_creation = self.max_repo_creation
        must_change_password = self.must_change_password
        password = self.password
        prohibit_login = self.prohibit_login
        restricted = self.restricted
        visibility = self.visibility
        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login_name": login_name,
                "source_id": source_id,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if admin is not UNSET:
            field_dict["admin"] = admin
        if allow_create_organization is not UNSET:
            field_dict["allow_create_organization"] = allow_create_organization
        if allow_git_hook is not UNSET:
            field_dict["allow_git_hook"] = allow_git_hook
        if allow_import_local is not UNSET:
            field_dict["allow_import_local"] = allow_import_local
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if location is not UNSET:
            field_dict["location"] = location
        if max_repo_creation is not UNSET:
            field_dict["max_repo_creation"] = max_repo_creation
        if must_change_password is not UNSET:
            field_dict["must_change_password"] = must_change_password
        if password is not UNSET:
            field_dict["password"] = password
        if prohibit_login is not UNSET:
            field_dict["prohibit_login"] = prohibit_login
        if restricted is not UNSET:
            field_dict["restricted"] = restricted
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login_name = d.pop("login_name")

        source_id = d.pop("source_id")

        active = d.pop("active", UNSET)

        admin = d.pop("admin", UNSET)

        allow_create_organization = d.pop("allow_create_organization", UNSET)

        allow_git_hook = d.pop("allow_git_hook", UNSET)

        allow_import_local = d.pop("allow_import_local", UNSET)

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        full_name = d.pop("full_name", UNSET)

        location = d.pop("location", UNSET)

        max_repo_creation = d.pop("max_repo_creation", UNSET)

        must_change_password = d.pop("must_change_password", UNSET)

        password = d.pop("password", UNSET)

        prohibit_login = d.pop("prohibit_login", UNSET)

        restricted = d.pop("restricted", UNSET)

        visibility = d.pop("visibility", UNSET)

        website = d.pop("website", UNSET)

        edit_user_option = cls(
            login_name=login_name,
            source_id=source_id,
            active=active,
            admin=admin,
            allow_create_organization=allow_create_organization,
            allow_git_hook=allow_git_hook,
            allow_import_local=allow_import_local,
            description=description,
            email=email,
            full_name=full_name,
            location=location,
            max_repo_creation=max_repo_creation,
            must_change_password=must_change_password,
            password=password,
            prohibit_login=prohibit_login,
            restricted=restricted,
            visibility=visibility,
            website=website,
        )

        edit_user_option.additional_properties = d
        return edit_user_option

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
