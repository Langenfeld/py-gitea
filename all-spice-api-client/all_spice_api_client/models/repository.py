import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_tracker import ExternalTracker
    from ..models.external_wiki import ExternalWiki
    from ..models.internal_tracker import InternalTracker
    from ..models.permission import Permission
    from ..models.repo_transfer import RepoTransfer
    from ..models.user import User


T = TypeVar("T", bound="Repository")


@attr.s(auto_attribs=True)
class Repository:
    """Repository represents a repository

    Attributes:
        allow_merge_commits (Union[Unset, bool]):
        allow_rebase (Union[Unset, bool]):
        allow_rebase_explicit (Union[Unset, bool]):
        allow_rebase_update (Union[Unset, bool]):
        allow_squash_merge (Union[Unset, bool]):
        archived (Union[Unset, bool]):
        avatar_url (Union[Unset, str]):
        clone_url (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        default_branch (Union[Unset, str]):
        default_delete_branch_after_merge (Union[Unset, bool]):
        default_merge_style (Union[Unset, str]):
        description (Union[Unset, str]):
        empty (Union[Unset, bool]):
        external_tracker (Union[Unset, ExternalTracker]): ExternalTracker represents settings for external tracker
        external_wiki (Union[Unset, ExternalWiki]): ExternalWiki represents setting for external wiki
        fork (Union[Unset, bool]):
        forks_count (Union[Unset, int]):
        full_name (Union[Unset, str]):
        has_issues (Union[Unset, bool]):
        has_projects (Union[Unset, bool]):
        has_pull_requests (Union[Unset, bool]):
        has_wiki (Union[Unset, bool]):
        html_url (Union[Unset, str]):
        id (Union[Unset, int]):
        ignore_whitespace_conflicts (Union[Unset, bool]):
        internal (Union[Unset, bool]):
        internal_tracker (Union[Unset, InternalTracker]): InternalTracker represents settings for internal tracker
        language (Union[Unset, str]):
        languages_url (Union[Unset, str]):
        mirror (Union[Unset, bool]):
        mirror_interval (Union[Unset, str]):
        mirror_updated (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        open_issues_count (Union[Unset, int]):
        open_pr_counter (Union[Unset, int]):
        original_url (Union[Unset, str]):
        owner (Union[Unset, User]): User represents a user
        parent (Union[Unset, Repository]): Repository represents a repository
        permissions (Union[Unset, Permission]): Permission represents a set of permissions
        private (Union[Unset, bool]):
        release_counter (Union[Unset, int]):
        repo_transfer (Union[Unset, RepoTransfer]): RepoTransfer represents a pending repo transfer
        size (Union[Unset, int]):
        ssh_url (Union[Unset, str]):
        stars_count (Union[Unset, int]):
        template (Union[Unset, bool]):
        updated_at (Union[Unset, datetime.datetime]):
        watchers_count (Union[Unset, int]):
        website (Union[Unset, str]):
    """

    allow_merge_commits: Union[Unset, bool] = UNSET
    allow_rebase: Union[Unset, bool] = UNSET
    allow_rebase_explicit: Union[Unset, bool] = UNSET
    allow_rebase_update: Union[Unset, bool] = UNSET
    allow_squash_merge: Union[Unset, bool] = UNSET
    archived: Union[Unset, bool] = UNSET
    avatar_url: Union[Unset, str] = UNSET
    clone_url: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    default_branch: Union[Unset, str] = UNSET
    default_delete_branch_after_merge: Union[Unset, bool] = UNSET
    default_merge_style: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    empty: Union[Unset, bool] = UNSET
    external_tracker: Union[Unset, "ExternalTracker"] = UNSET
    external_wiki: Union[Unset, "ExternalWiki"] = UNSET
    fork: Union[Unset, bool] = UNSET
    forks_count: Union[Unset, int] = UNSET
    full_name: Union[Unset, str] = UNSET
    has_issues: Union[Unset, bool] = UNSET
    has_projects: Union[Unset, bool] = UNSET
    has_pull_requests: Union[Unset, bool] = UNSET
    has_wiki: Union[Unset, bool] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    ignore_whitespace_conflicts: Union[Unset, bool] = UNSET
    internal: Union[Unset, bool] = UNSET
    internal_tracker: Union[Unset, "InternalTracker"] = UNSET
    language: Union[Unset, str] = UNSET
    languages_url: Union[Unset, str] = UNSET
    mirror: Union[Unset, bool] = UNSET
    mirror_interval: Union[Unset, str] = UNSET
    mirror_updated: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    open_issues_count: Union[Unset, int] = UNSET
    open_pr_counter: Union[Unset, int] = UNSET
    original_url: Union[Unset, str] = UNSET
    owner: Union[Unset, "User"] = UNSET
    parent: Union[Unset, "Repository"] = UNSET
    permissions: Union[Unset, "Permission"] = UNSET
    private: Union[Unset, bool] = UNSET
    release_counter: Union[Unset, int] = UNSET
    repo_transfer: Union[Unset, "RepoTransfer"] = UNSET
    size: Union[Unset, int] = UNSET
    ssh_url: Union[Unset, str] = UNSET
    stars_count: Union[Unset, int] = UNSET
    template: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    watchers_count: Union[Unset, int] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_merge_commits = self.allow_merge_commits
        allow_rebase = self.allow_rebase
        allow_rebase_explicit = self.allow_rebase_explicit
        allow_rebase_update = self.allow_rebase_update
        allow_squash_merge = self.allow_squash_merge
        archived = self.archived
        avatar_url = self.avatar_url
        clone_url = self.clone_url
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        default_branch = self.default_branch
        default_delete_branch_after_merge = self.default_delete_branch_after_merge
        default_merge_style = self.default_merge_style
        description = self.description
        empty = self.empty
        external_tracker: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_tracker, Unset):
            external_tracker = self.external_tracker.to_dict()

        external_wiki: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_wiki, Unset):
            external_wiki = self.external_wiki.to_dict()

        fork = self.fork
        forks_count = self.forks_count
        full_name = self.full_name
        has_issues = self.has_issues
        has_projects = self.has_projects
        has_pull_requests = self.has_pull_requests
        has_wiki = self.has_wiki
        html_url = self.html_url
        id = self.id
        ignore_whitespace_conflicts = self.ignore_whitespace_conflicts
        internal = self.internal
        internal_tracker: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.internal_tracker, Unset):
            internal_tracker = self.internal_tracker.to_dict()

        language = self.language
        languages_url = self.languages_url
        mirror = self.mirror
        mirror_interval = self.mirror_interval
        mirror_updated: Union[Unset, str] = UNSET
        if not isinstance(self.mirror_updated, Unset):
            mirror_updated = self.mirror_updated.isoformat()

        name = self.name
        open_issues_count = self.open_issues_count
        open_pr_counter = self.open_pr_counter
        original_url = self.original_url
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        private = self.private
        release_counter = self.release_counter
        repo_transfer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repo_transfer, Unset):
            repo_transfer = self.repo_transfer.to_dict()

        size = self.size
        ssh_url = self.ssh_url
        stars_count = self.stars_count
        template = self.template
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        watchers_count = self.watchers_count
        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_merge_commits is not UNSET:
            field_dict["allow_merge_commits"] = allow_merge_commits
        if allow_rebase is not UNSET:
            field_dict["allow_rebase"] = allow_rebase
        if allow_rebase_explicit is not UNSET:
            field_dict["allow_rebase_explicit"] = allow_rebase_explicit
        if allow_rebase_update is not UNSET:
            field_dict["allow_rebase_update"] = allow_rebase_update
        if allow_squash_merge is not UNSET:
            field_dict["allow_squash_merge"] = allow_squash_merge
        if archived is not UNSET:
            field_dict["archived"] = archived
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if clone_url is not UNSET:
            field_dict["clone_url"] = clone_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if default_delete_branch_after_merge is not UNSET:
            field_dict["default_delete_branch_after_merge"] = default_delete_branch_after_merge
        if default_merge_style is not UNSET:
            field_dict["default_merge_style"] = default_merge_style
        if description is not UNSET:
            field_dict["description"] = description
        if empty is not UNSET:
            field_dict["empty"] = empty
        if external_tracker is not UNSET:
            field_dict["external_tracker"] = external_tracker
        if external_wiki is not UNSET:
            field_dict["external_wiki"] = external_wiki
        if fork is not UNSET:
            field_dict["fork"] = fork
        if forks_count is not UNSET:
            field_dict["forks_count"] = forks_count
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if has_issues is not UNSET:
            field_dict["has_issues"] = has_issues
        if has_projects is not UNSET:
            field_dict["has_projects"] = has_projects
        if has_pull_requests is not UNSET:
            field_dict["has_pull_requests"] = has_pull_requests
        if has_wiki is not UNSET:
            field_dict["has_wiki"] = has_wiki
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if ignore_whitespace_conflicts is not UNSET:
            field_dict["ignore_whitespace_conflicts"] = ignore_whitespace_conflicts
        if internal is not UNSET:
            field_dict["internal"] = internal
        if internal_tracker is not UNSET:
            field_dict["internal_tracker"] = internal_tracker
        if language is not UNSET:
            field_dict["language"] = language
        if languages_url is not UNSET:
            field_dict["languages_url"] = languages_url
        if mirror is not UNSET:
            field_dict["mirror"] = mirror
        if mirror_interval is not UNSET:
            field_dict["mirror_interval"] = mirror_interval
        if mirror_updated is not UNSET:
            field_dict["mirror_updated"] = mirror_updated
        if name is not UNSET:
            field_dict["name"] = name
        if open_issues_count is not UNSET:
            field_dict["open_issues_count"] = open_issues_count
        if open_pr_counter is not UNSET:
            field_dict["open_pr_counter"] = open_pr_counter
        if original_url is not UNSET:
            field_dict["original_url"] = original_url
        if owner is not UNSET:
            field_dict["owner"] = owner
        if parent is not UNSET:
            field_dict["parent"] = parent
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if private is not UNSET:
            field_dict["private"] = private
        if release_counter is not UNSET:
            field_dict["release_counter"] = release_counter
        if repo_transfer is not UNSET:
            field_dict["repo_transfer"] = repo_transfer
        if size is not UNSET:
            field_dict["size"] = size
        if ssh_url is not UNSET:
            field_dict["ssh_url"] = ssh_url
        if stars_count is not UNSET:
            field_dict["stars_count"] = stars_count
        if template is not UNSET:
            field_dict["template"] = template
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if watchers_count is not UNSET:
            field_dict["watchers_count"] = watchers_count
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.external_tracker import ExternalTracker
        from ..models.external_wiki import ExternalWiki
        from ..models.internal_tracker import InternalTracker
        from ..models.permission import Permission
        from ..models.repo_transfer import RepoTransfer
        from ..models.user import User

        d = src_dict.copy()
        allow_merge_commits = d.pop("allow_merge_commits", UNSET)

        allow_rebase = d.pop("allow_rebase", UNSET)

        allow_rebase_explicit = d.pop("allow_rebase_explicit", UNSET)

        allow_rebase_update = d.pop("allow_rebase_update", UNSET)

        allow_squash_merge = d.pop("allow_squash_merge", UNSET)

        archived = d.pop("archived", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        clone_url = d.pop("clone_url", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        default_branch = d.pop("default_branch", UNSET)

        default_delete_branch_after_merge = d.pop("default_delete_branch_after_merge", UNSET)

        default_merge_style = d.pop("default_merge_style", UNSET)

        description = d.pop("description", UNSET)

        empty = d.pop("empty", UNSET)

        _external_tracker = d.pop("external_tracker", UNSET)
        external_tracker: Union[Unset, ExternalTracker]
        if isinstance(_external_tracker, Unset):
            external_tracker = UNSET
        else:
            external_tracker = ExternalTracker.from_dict(_external_tracker)

        _external_wiki = d.pop("external_wiki", UNSET)
        external_wiki: Union[Unset, ExternalWiki]
        if isinstance(_external_wiki, Unset):
            external_wiki = UNSET
        else:
            external_wiki = ExternalWiki.from_dict(_external_wiki)

        fork = d.pop("fork", UNSET)

        forks_count = d.pop("forks_count", UNSET)

        full_name = d.pop("full_name", UNSET)

        has_issues = d.pop("has_issues", UNSET)

        has_projects = d.pop("has_projects", UNSET)

        has_pull_requests = d.pop("has_pull_requests", UNSET)

        has_wiki = d.pop("has_wiki", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        ignore_whitespace_conflicts = d.pop("ignore_whitespace_conflicts", UNSET)

        internal = d.pop("internal", UNSET)

        _internal_tracker = d.pop("internal_tracker", UNSET)
        internal_tracker: Union[Unset, InternalTracker]
        if isinstance(_internal_tracker, Unset):
            internal_tracker = UNSET
        else:
            internal_tracker = InternalTracker.from_dict(_internal_tracker)

        language = d.pop("language", UNSET)

        languages_url = d.pop("languages_url", UNSET)

        mirror = d.pop("mirror", UNSET)

        mirror_interval = d.pop("mirror_interval", UNSET)

        _mirror_updated = d.pop("mirror_updated", UNSET)
        mirror_updated: Union[Unset, datetime.datetime]
        if isinstance(_mirror_updated, Unset):
            mirror_updated = UNSET
        else:
            mirror_updated = isoparse(_mirror_updated)

        name = d.pop("name", UNSET)

        open_issues_count = d.pop("open_issues_count", UNSET)

        open_pr_counter = d.pop("open_pr_counter", UNSET)

        original_url = d.pop("original_url", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, User]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = User.from_dict(_owner)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, Repository]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = Repository.from_dict(_parent)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, Permission]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = Permission.from_dict(_permissions)

        private = d.pop("private", UNSET)

        release_counter = d.pop("release_counter", UNSET)

        _repo_transfer = d.pop("repo_transfer", UNSET)
        repo_transfer: Union[Unset, RepoTransfer]
        if isinstance(_repo_transfer, Unset):
            repo_transfer = UNSET
        else:
            repo_transfer = RepoTransfer.from_dict(_repo_transfer)

        size = d.pop("size", UNSET)

        ssh_url = d.pop("ssh_url", UNSET)

        stars_count = d.pop("stars_count", UNSET)

        template = d.pop("template", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        watchers_count = d.pop("watchers_count", UNSET)

        website = d.pop("website", UNSET)

        repository = cls(
            allow_merge_commits=allow_merge_commits,
            allow_rebase=allow_rebase,
            allow_rebase_explicit=allow_rebase_explicit,
            allow_rebase_update=allow_rebase_update,
            allow_squash_merge=allow_squash_merge,
            archived=archived,
            avatar_url=avatar_url,
            clone_url=clone_url,
            created_at=created_at,
            default_branch=default_branch,
            default_delete_branch_after_merge=default_delete_branch_after_merge,
            default_merge_style=default_merge_style,
            description=description,
            empty=empty,
            external_tracker=external_tracker,
            external_wiki=external_wiki,
            fork=fork,
            forks_count=forks_count,
            full_name=full_name,
            has_issues=has_issues,
            has_projects=has_projects,
            has_pull_requests=has_pull_requests,
            has_wiki=has_wiki,
            html_url=html_url,
            id=id,
            ignore_whitespace_conflicts=ignore_whitespace_conflicts,
            internal=internal,
            internal_tracker=internal_tracker,
            language=language,
            languages_url=languages_url,
            mirror=mirror,
            mirror_interval=mirror_interval,
            mirror_updated=mirror_updated,
            name=name,
            open_issues_count=open_issues_count,
            open_pr_counter=open_pr_counter,
            original_url=original_url,
            owner=owner,
            parent=parent,
            permissions=permissions,
            private=private,
            release_counter=release_counter,
            repo_transfer=repo_transfer,
            size=size,
            ssh_url=ssh_url,
            stars_count=stars_count,
            template=template,
            updated_at=updated_at,
            watchers_count=watchers_count,
            website=website,
        )

        repository.additional_properties = d
        return repository

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
