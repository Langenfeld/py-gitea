from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.migrate_repo_options_service import MigrateRepoOptionsService
from ..types import UNSET, Unset

T = TypeVar("T", bound="MigrateRepoOptions")


@attr.s(auto_attribs=True)
class MigrateRepoOptions:
    """MigrateRepoOptions options for migrating repository's
    this is used to interact with api v1

        Attributes:
            clone_addr (str):
            repo_name (str):
            auth_password (Union[Unset, str]):
            auth_token (Union[Unset, str]):
            auth_username (Union[Unset, str]):
            description (Union[Unset, str]):
            issues (Union[Unset, bool]):
            labels (Union[Unset, bool]):
            lfs (Union[Unset, bool]):
            lfs_endpoint (Union[Unset, str]):
            milestones (Union[Unset, bool]):
            mirror (Union[Unset, bool]):
            mirror_interval (Union[Unset, str]):
            private (Union[Unset, bool]):
            pull_requests (Union[Unset, bool]):
            releases (Union[Unset, bool]):
            repo_owner (Union[Unset, str]): Name of User or Organisation who will own Repo after migration
            service (Union[Unset, MigrateRepoOptionsService]):
            uid (Union[Unset, int]): deprecated (only for backwards compatibility)
            wiki (Union[Unset, bool]):
    """

    clone_addr: str
    repo_name: str
    auth_password: Union[Unset, str] = UNSET
    auth_token: Union[Unset, str] = UNSET
    auth_username: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    issues: Union[Unset, bool] = UNSET
    labels: Union[Unset, bool] = UNSET
    lfs: Union[Unset, bool] = UNSET
    lfs_endpoint: Union[Unset, str] = UNSET
    milestones: Union[Unset, bool] = UNSET
    mirror: Union[Unset, bool] = UNSET
    mirror_interval: Union[Unset, str] = UNSET
    private: Union[Unset, bool] = UNSET
    pull_requests: Union[Unset, bool] = UNSET
    releases: Union[Unset, bool] = UNSET
    repo_owner: Union[Unset, str] = UNSET
    service: Union[Unset, MigrateRepoOptionsService] = UNSET
    uid: Union[Unset, int] = UNSET
    wiki: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clone_addr = self.clone_addr
        repo_name = self.repo_name
        auth_password = self.auth_password
        auth_token = self.auth_token
        auth_username = self.auth_username
        description = self.description
        issues = self.issues
        labels = self.labels
        lfs = self.lfs
        lfs_endpoint = self.lfs_endpoint
        milestones = self.milestones
        mirror = self.mirror
        mirror_interval = self.mirror_interval
        private = self.private
        pull_requests = self.pull_requests
        releases = self.releases
        repo_owner = self.repo_owner
        service: Union[Unset, str] = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.value

        uid = self.uid
        wiki = self.wiki

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clone_addr": clone_addr,
                "repo_name": repo_name,
            }
        )
        if auth_password is not UNSET:
            field_dict["auth_password"] = auth_password
        if auth_token is not UNSET:
            field_dict["auth_token"] = auth_token
        if auth_username is not UNSET:
            field_dict["auth_username"] = auth_username
        if description is not UNSET:
            field_dict["description"] = description
        if issues is not UNSET:
            field_dict["issues"] = issues
        if labels is not UNSET:
            field_dict["labels"] = labels
        if lfs is not UNSET:
            field_dict["lfs"] = lfs
        if lfs_endpoint is not UNSET:
            field_dict["lfs_endpoint"] = lfs_endpoint
        if milestones is not UNSET:
            field_dict["milestones"] = milestones
        if mirror is not UNSET:
            field_dict["mirror"] = mirror
        if mirror_interval is not UNSET:
            field_dict["mirror_interval"] = mirror_interval
        if private is not UNSET:
            field_dict["private"] = private
        if pull_requests is not UNSET:
            field_dict["pull_requests"] = pull_requests
        if releases is not UNSET:
            field_dict["releases"] = releases
        if repo_owner is not UNSET:
            field_dict["repo_owner"] = repo_owner
        if service is not UNSET:
            field_dict["service"] = service
        if uid is not UNSET:
            field_dict["uid"] = uid
        if wiki is not UNSET:
            field_dict["wiki"] = wiki

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        clone_addr = d.pop("clone_addr")

        repo_name = d.pop("repo_name")

        auth_password = d.pop("auth_password", UNSET)

        auth_token = d.pop("auth_token", UNSET)

        auth_username = d.pop("auth_username", UNSET)

        description = d.pop("description", UNSET)

        issues = d.pop("issues", UNSET)

        labels = d.pop("labels", UNSET)

        lfs = d.pop("lfs", UNSET)

        lfs_endpoint = d.pop("lfs_endpoint", UNSET)

        milestones = d.pop("milestones", UNSET)

        mirror = d.pop("mirror", UNSET)

        mirror_interval = d.pop("mirror_interval", UNSET)

        private = d.pop("private", UNSET)

        pull_requests = d.pop("pull_requests", UNSET)

        releases = d.pop("releases", UNSET)

        repo_owner = d.pop("repo_owner", UNSET)

        _service = d.pop("service", UNSET)
        service: Union[Unset, MigrateRepoOptionsService]
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = MigrateRepoOptionsService(_service)

        uid = d.pop("uid", UNSET)

        wiki = d.pop("wiki", UNSET)

        migrate_repo_options = cls(
            clone_addr=clone_addr,
            repo_name=repo_name,
            auth_password=auth_password,
            auth_token=auth_token,
            auth_username=auth_username,
            description=description,
            issues=issues,
            labels=labels,
            lfs=lfs,
            lfs_endpoint=lfs_endpoint,
            milestones=milestones,
            mirror=mirror,
            mirror_interval=mirror_interval,
            private=private,
            pull_requests=pull_requests,
            releases=releases,
            repo_owner=repo_owner,
            service=service,
            uid=uid,
            wiki=wiki,
        )

        migrate_repo_options.additional_properties = d
        return migrate_repo_options

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
