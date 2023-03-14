from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_tracker import ExternalTracker
    from ..models.external_wiki import ExternalWiki
    from ..models.internal_tracker import InternalTracker


T = TypeVar("T", bound="EditRepoOption")


@attr.s(auto_attribs=True)
class EditRepoOption:
    """EditRepoOption options when editing a repository's properties

    Attributes:
        allow_manual_merge (Union[Unset, bool]): either `true` to allow mark pr as merged manually, or `false` to
            prevent it.
        allow_merge_commits (Union[Unset, bool]): either `true` to allow merging pull requests with a merge commit, or
            `false` to prevent merging pull requests with merge commits.
        allow_rebase (Union[Unset, bool]): either `true` to allow rebase-merging pull requests, or `false` to prevent
            rebase-merging.
        allow_rebase_explicit (Union[Unset, bool]): either `true` to allow rebase with explicit merge commits (--no-ff),
            or `false` to prevent rebase with explicit merge commits.
        allow_rebase_update (Union[Unset, bool]): either `true` to allow updating pull request branch by rebase, or
            `false` to prevent it.
        allow_squash_merge (Union[Unset, bool]): either `true` to allow squash-merging pull requests, or `false` to
            prevent squash-merging.
        archived (Union[Unset, bool]): set to `true` to archive this repository.
        autodetect_manual_merge (Union[Unset, bool]): either `true` to enable AutodetectManualMerge, or `false` to
            prevent it. Note: In some special cases, misjudgments can occur.
        default_branch (Union[Unset, str]): sets the default branch for this repository.
        default_delete_branch_after_merge (Union[Unset, bool]): set to `true` to delete pr branch after merge by default
        default_merge_style (Union[Unset, str]): set to a merge style to be used by this repository: "merge", "rebase",
            "rebase-merge", or "squash".
        description (Union[Unset, str]): a short description of the repository.
        enable_prune (Union[Unset, bool]): enable prune - remove obsolete remote-tracking references
        external_tracker (Union[Unset, ExternalTracker]): ExternalTracker represents settings for external tracker
        external_wiki (Union[Unset, ExternalWiki]): ExternalWiki represents setting for external wiki
        has_issues (Union[Unset, bool]): either `true` to enable issues for this repository or `false` to disable them.
        has_projects (Union[Unset, bool]): either `true` to enable project unit, or `false` to disable them.
        has_pull_requests (Union[Unset, bool]): either `true` to allow pull requests, or `false` to prevent pull
            request.
        has_wiki (Union[Unset, bool]): either `true` to enable the wiki for this repository or `false` to disable it.
        ignore_whitespace_conflicts (Union[Unset, bool]): either `true` to ignore whitespace for conflicts, or `false`
            to not ignore whitespace.
        internal_tracker (Union[Unset, InternalTracker]): InternalTracker represents settings for internal tracker
        mirror_interval (Union[Unset, str]): set to a string like `8h30m0s` to set the mirror interval time
        name (Union[Unset, str]): name of the repository
        private (Union[Unset, bool]): either `true` to make the repository private or `false` to make it public.
            Note: you will get a 422 error if the organization restricts changing repository visibility to organization
            owners and a non-owner tries to change the value of private.
        template (Union[Unset, bool]): either `true` to make this repository a template or `false` to make it a normal
            repository
        website (Union[Unset, str]): a URL with more information about the repository.
    """

    allow_manual_merge: Union[Unset, bool] = UNSET
    allow_merge_commits: Union[Unset, bool] = UNSET
    allow_rebase: Union[Unset, bool] = UNSET
    allow_rebase_explicit: Union[Unset, bool] = UNSET
    allow_rebase_update: Union[Unset, bool] = UNSET
    allow_squash_merge: Union[Unset, bool] = UNSET
    archived: Union[Unset, bool] = UNSET
    autodetect_manual_merge: Union[Unset, bool] = UNSET
    default_branch: Union[Unset, str] = UNSET
    default_delete_branch_after_merge: Union[Unset, bool] = UNSET
    default_merge_style: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enable_prune: Union[Unset, bool] = UNSET
    external_tracker: Union[Unset, "ExternalTracker"] = UNSET
    external_wiki: Union[Unset, "ExternalWiki"] = UNSET
    has_issues: Union[Unset, bool] = UNSET
    has_projects: Union[Unset, bool] = UNSET
    has_pull_requests: Union[Unset, bool] = UNSET
    has_wiki: Union[Unset, bool] = UNSET
    ignore_whitespace_conflicts: Union[Unset, bool] = UNSET
    internal_tracker: Union[Unset, "InternalTracker"] = UNSET
    mirror_interval: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    private: Union[Unset, bool] = UNSET
    template: Union[Unset, bool] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_manual_merge = self.allow_manual_merge
        allow_merge_commits = self.allow_merge_commits
        allow_rebase = self.allow_rebase
        allow_rebase_explicit = self.allow_rebase_explicit
        allow_rebase_update = self.allow_rebase_update
        allow_squash_merge = self.allow_squash_merge
        archived = self.archived
        autodetect_manual_merge = self.autodetect_manual_merge
        default_branch = self.default_branch
        default_delete_branch_after_merge = self.default_delete_branch_after_merge
        default_merge_style = self.default_merge_style
        description = self.description
        enable_prune = self.enable_prune
        external_tracker: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_tracker, Unset):
            external_tracker = self.external_tracker.to_dict()

        external_wiki: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_wiki, Unset):
            external_wiki = self.external_wiki.to_dict()

        has_issues = self.has_issues
        has_projects = self.has_projects
        has_pull_requests = self.has_pull_requests
        has_wiki = self.has_wiki
        ignore_whitespace_conflicts = self.ignore_whitespace_conflicts
        internal_tracker: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.internal_tracker, Unset):
            internal_tracker = self.internal_tracker.to_dict()

        mirror_interval = self.mirror_interval
        name = self.name
        private = self.private
        template = self.template
        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_manual_merge is not UNSET:
            field_dict["allow_manual_merge"] = allow_manual_merge
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
        if autodetect_manual_merge is not UNSET:
            field_dict["autodetect_manual_merge"] = autodetect_manual_merge
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if default_delete_branch_after_merge is not UNSET:
            field_dict["default_delete_branch_after_merge"] = default_delete_branch_after_merge
        if default_merge_style is not UNSET:
            field_dict["default_merge_style"] = default_merge_style
        if description is not UNSET:
            field_dict["description"] = description
        if enable_prune is not UNSET:
            field_dict["enable_prune"] = enable_prune
        if external_tracker is not UNSET:
            field_dict["external_tracker"] = external_tracker
        if external_wiki is not UNSET:
            field_dict["external_wiki"] = external_wiki
        if has_issues is not UNSET:
            field_dict["has_issues"] = has_issues
        if has_projects is not UNSET:
            field_dict["has_projects"] = has_projects
        if has_pull_requests is not UNSET:
            field_dict["has_pull_requests"] = has_pull_requests
        if has_wiki is not UNSET:
            field_dict["has_wiki"] = has_wiki
        if ignore_whitespace_conflicts is not UNSET:
            field_dict["ignore_whitespace_conflicts"] = ignore_whitespace_conflicts
        if internal_tracker is not UNSET:
            field_dict["internal_tracker"] = internal_tracker
        if mirror_interval is not UNSET:
            field_dict["mirror_interval"] = mirror_interval
        if name is not UNSET:
            field_dict["name"] = name
        if private is not UNSET:
            field_dict["private"] = private
        if template is not UNSET:
            field_dict["template"] = template
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.external_tracker import ExternalTracker
        from ..models.external_wiki import ExternalWiki
        from ..models.internal_tracker import InternalTracker

        d = src_dict.copy()
        allow_manual_merge = d.pop("allow_manual_merge", UNSET)

        allow_merge_commits = d.pop("allow_merge_commits", UNSET)

        allow_rebase = d.pop("allow_rebase", UNSET)

        allow_rebase_explicit = d.pop("allow_rebase_explicit", UNSET)

        allow_rebase_update = d.pop("allow_rebase_update", UNSET)

        allow_squash_merge = d.pop("allow_squash_merge", UNSET)

        archived = d.pop("archived", UNSET)

        autodetect_manual_merge = d.pop("autodetect_manual_merge", UNSET)

        default_branch = d.pop("default_branch", UNSET)

        default_delete_branch_after_merge = d.pop("default_delete_branch_after_merge", UNSET)

        default_merge_style = d.pop("default_merge_style", UNSET)

        description = d.pop("description", UNSET)

        enable_prune = d.pop("enable_prune", UNSET)

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

        has_issues = d.pop("has_issues", UNSET)

        has_projects = d.pop("has_projects", UNSET)

        has_pull_requests = d.pop("has_pull_requests", UNSET)

        has_wiki = d.pop("has_wiki", UNSET)

        ignore_whitespace_conflicts = d.pop("ignore_whitespace_conflicts", UNSET)

        _internal_tracker = d.pop("internal_tracker", UNSET)
        internal_tracker: Union[Unset, InternalTracker]
        if isinstance(_internal_tracker, Unset):
            internal_tracker = UNSET
        else:
            internal_tracker = InternalTracker.from_dict(_internal_tracker)

        mirror_interval = d.pop("mirror_interval", UNSET)

        name = d.pop("name", UNSET)

        private = d.pop("private", UNSET)

        template = d.pop("template", UNSET)

        website = d.pop("website", UNSET)

        edit_repo_option = cls(
            allow_manual_merge=allow_manual_merge,
            allow_merge_commits=allow_merge_commits,
            allow_rebase=allow_rebase,
            allow_rebase_explicit=allow_rebase_explicit,
            allow_rebase_update=allow_rebase_update,
            allow_squash_merge=allow_squash_merge,
            archived=archived,
            autodetect_manual_merge=autodetect_manual_merge,
            default_branch=default_branch,
            default_delete_branch_after_merge=default_delete_branch_after_merge,
            default_merge_style=default_merge_style,
            description=description,
            enable_prune=enable_prune,
            external_tracker=external_tracker,
            external_wiki=external_wiki,
            has_issues=has_issues,
            has_projects=has_projects,
            has_pull_requests=has_pull_requests,
            has_wiki=has_wiki,
            ignore_whitespace_conflicts=ignore_whitespace_conflicts,
            internal_tracker=internal_tracker,
            mirror_interval=mirror_interval,
            name=name,
            private=private,
            template=template,
            website=website,
        )

        edit_repo_option.additional_properties = d
        return edit_repo_option

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
