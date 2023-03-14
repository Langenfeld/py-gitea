import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment
    from ..models.user import User


T = TypeVar("T", bound="Release")


@attr.s(auto_attribs=True)
class Release:
    """Release represents a repository release

    Attributes:
        assets (Union[Unset, List['Attachment']]):
        author (Union[Unset, User]): User represents a user
        body (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        draft (Union[Unset, bool]):
        html_url (Union[Unset, str]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        prerelease (Union[Unset, bool]):
        published_at (Union[Unset, datetime.datetime]):
        tag_name (Union[Unset, str]):
        tarball_url (Union[Unset, str]):
        target_commitish (Union[Unset, str]):
        url (Union[Unset, str]):
        zipball_url (Union[Unset, str]):
    """

    assets: Union[Unset, List["Attachment"]] = UNSET
    author: Union[Unset, "User"] = UNSET
    body: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    draft: Union[Unset, bool] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    prerelease: Union[Unset, bool] = UNSET
    published_at: Union[Unset, datetime.datetime] = UNSET
    tag_name: Union[Unset, str] = UNSET
    tarball_url: Union[Unset, str] = UNSET
    target_commitish: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    zipball_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()

                assets.append(assets_item)

        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        body = self.body
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        draft = self.draft
        html_url = self.html_url
        id = self.id
        name = self.name
        prerelease = self.prerelease
        published_at: Union[Unset, str] = UNSET
        if not isinstance(self.published_at, Unset):
            published_at = self.published_at.isoformat()

        tag_name = self.tag_name
        tarball_url = self.tarball_url
        target_commitish = self.target_commitish
        url = self.url
        zipball_url = self.zipball_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets is not UNSET:
            field_dict["assets"] = assets
        if author is not UNSET:
            field_dict["author"] = author
        if body is not UNSET:
            field_dict["body"] = body
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if draft is not UNSET:
            field_dict["draft"] = draft
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if prerelease is not UNSET:
            field_dict["prerelease"] = prerelease
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if tag_name is not UNSET:
            field_dict["tag_name"] = tag_name
        if tarball_url is not UNSET:
            field_dict["tarball_url"] = tarball_url
        if target_commitish is not UNSET:
            field_dict["target_commitish"] = target_commitish
        if url is not UNSET:
            field_dict["url"] = url
        if zipball_url is not UNSET:
            field_dict["zipball_url"] = zipball_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attachment import Attachment
        from ..models.user import User

        d = src_dict.copy()
        assets = []
        _assets = d.pop("assets", UNSET)
        for assets_item_data in _assets or []:
            assets_item = Attachment.from_dict(assets_item_data)

            assets.append(assets_item)

        _author = d.pop("author", UNSET)
        author: Union[Unset, User]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = User.from_dict(_author)

        body = d.pop("body", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        draft = d.pop("draft", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        prerelease = d.pop("prerelease", UNSET)

        _published_at = d.pop("published_at", UNSET)
        published_at: Union[Unset, datetime.datetime]
        if isinstance(_published_at, Unset):
            published_at = UNSET
        else:
            published_at = isoparse(_published_at)

        tag_name = d.pop("tag_name", UNSET)

        tarball_url = d.pop("tarball_url", UNSET)

        target_commitish = d.pop("target_commitish", UNSET)

        url = d.pop("url", UNSET)

        zipball_url = d.pop("zipball_url", UNSET)

        release = cls(
            assets=assets,
            author=author,
            body=body,
            created_at=created_at,
            draft=draft,
            html_url=html_url,
            id=id,
            name=name,
            prerelease=prerelease,
            published_at=published_at,
            tag_name=tag_name,
            tarball_url=tarball_url,
            target_commitish=target_commitish,
            url=url,
            zipball_url=zipball_url,
        )

        release.additional_properties = d
        return release

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
