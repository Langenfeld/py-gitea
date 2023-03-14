from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerateRepoOption")


@attr.s(auto_attribs=True)
class GenerateRepoOption:
    """GenerateRepoOption options when creating repository using a template

    Attributes:
        name (str): Name of the repository to create
        owner (str): The organization or person who will own the new repository
        avatar (Union[Unset, bool]): include avatar of the template repo
        default_branch (Union[Unset, str]): Default branch of the new repository
        description (Union[Unset, str]): Description of the repository to create
        git_content (Union[Unset, bool]): include git content of default branch in template repo
        git_hooks (Union[Unset, bool]): include git hooks in template repo
        labels (Union[Unset, bool]): include labels in template repo
        private (Union[Unset, bool]): Whether the repository is private
        topics (Union[Unset, bool]): include topics in template repo
        webhooks (Union[Unset, bool]): include webhooks in template repo
    """

    name: str
    owner: str
    avatar: Union[Unset, bool] = UNSET
    default_branch: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    git_content: Union[Unset, bool] = UNSET
    git_hooks: Union[Unset, bool] = UNSET
    labels: Union[Unset, bool] = UNSET
    private: Union[Unset, bool] = UNSET
    topics: Union[Unset, bool] = UNSET
    webhooks: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        owner = self.owner
        avatar = self.avatar
        default_branch = self.default_branch
        description = self.description
        git_content = self.git_content
        git_hooks = self.git_hooks
        labels = self.labels
        private = self.private
        topics = self.topics
        webhooks = self.webhooks

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "owner": owner,
            }
        )
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if description is not UNSET:
            field_dict["description"] = description
        if git_content is not UNSET:
            field_dict["git_content"] = git_content
        if git_hooks is not UNSET:
            field_dict["git_hooks"] = git_hooks
        if labels is not UNSET:
            field_dict["labels"] = labels
        if private is not UNSET:
            field_dict["private"] = private
        if topics is not UNSET:
            field_dict["topics"] = topics
        if webhooks is not UNSET:
            field_dict["webhooks"] = webhooks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        owner = d.pop("owner")

        avatar = d.pop("avatar", UNSET)

        default_branch = d.pop("default_branch", UNSET)

        description = d.pop("description", UNSET)

        git_content = d.pop("git_content", UNSET)

        git_hooks = d.pop("git_hooks", UNSET)

        labels = d.pop("labels", UNSET)

        private = d.pop("private", UNSET)

        topics = d.pop("topics", UNSET)

        webhooks = d.pop("webhooks", UNSET)

        generate_repo_option = cls(
            name=name,
            owner=owner,
            avatar=avatar,
            default_branch=default_branch,
            description=description,
            git_content=git_content,
            git_hooks=git_hooks,
            labels=labels,
            private=private,
            topics=topics,
            webhooks=webhooks,
        )

        generate_repo_option.additional_properties = d
        return generate_repo_option

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
