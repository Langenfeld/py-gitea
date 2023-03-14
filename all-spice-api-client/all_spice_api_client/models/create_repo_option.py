from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.create_repo_option_trust_model import CreateRepoOptionTrustModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRepoOption")


@attr.s(auto_attribs=True)
class CreateRepoOption:
    """CreateRepoOption options when creating repository

    Attributes:
        name (str): Name of the repository to create
        auto_init (Union[Unset, bool]): Whether the repository should be auto-initialized?
        create_develop_branch (Union[Unset, bool]): Whether to initialize the repository with a secondary develop branch
        default_branch (Union[Unset, str]): DefaultBranch of the repository (used when initializes and in template)
        description (Union[Unset, str]): Description of the repository to create
        gitignores (Union[Unset, str]): Gitignores to use
        issue_labels (Union[Unset, str]): Label-Set to use
        license_ (Union[Unset, str]): License to use
        private (Union[Unset, bool]): Whether the repository is private
        readme (Union[Unset, str]): Readme of the repository to create
        template (Union[Unset, bool]): Whether the repository is template
        trust_model (Union[Unset, CreateRepoOptionTrustModel]): TrustModel of the repository
    """

    name: str
    auto_init: Union[Unset, bool] = UNSET
    create_develop_branch: Union[Unset, bool] = UNSET
    default_branch: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    gitignores: Union[Unset, str] = UNSET
    issue_labels: Union[Unset, str] = UNSET
    license_: Union[Unset, str] = UNSET
    private: Union[Unset, bool] = UNSET
    readme: Union[Unset, str] = UNSET
    template: Union[Unset, bool] = UNSET
    trust_model: Union[Unset, CreateRepoOptionTrustModel] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        auto_init = self.auto_init
        create_develop_branch = self.create_develop_branch
        default_branch = self.default_branch
        description = self.description
        gitignores = self.gitignores
        issue_labels = self.issue_labels
        license_ = self.license_
        private = self.private
        readme = self.readme
        template = self.template
        trust_model: Union[Unset, str] = UNSET
        if not isinstance(self.trust_model, Unset):
            trust_model = self.trust_model.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if auto_init is not UNSET:
            field_dict["auto_init"] = auto_init
        if create_develop_branch is not UNSET:
            field_dict["create_develop_branch"] = create_develop_branch
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if description is not UNSET:
            field_dict["description"] = description
        if gitignores is not UNSET:
            field_dict["gitignores"] = gitignores
        if issue_labels is not UNSET:
            field_dict["issue_labels"] = issue_labels
        if license_ is not UNSET:
            field_dict["license"] = license_
        if private is not UNSET:
            field_dict["private"] = private
        if readme is not UNSET:
            field_dict["readme"] = readme
        if template is not UNSET:
            field_dict["template"] = template
        if trust_model is not UNSET:
            field_dict["trust_model"] = trust_model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        auto_init = d.pop("auto_init", UNSET)

        create_develop_branch = d.pop("create_develop_branch", UNSET)

        default_branch = d.pop("default_branch", UNSET)

        description = d.pop("description", UNSET)

        gitignores = d.pop("gitignores", UNSET)

        issue_labels = d.pop("issue_labels", UNSET)

        license_ = d.pop("license", UNSET)

        private = d.pop("private", UNSET)

        readme = d.pop("readme", UNSET)

        template = d.pop("template", UNSET)

        _trust_model = d.pop("trust_model", UNSET)
        trust_model: Union[Unset, CreateRepoOptionTrustModel]
        if isinstance(_trust_model, Unset):
            trust_model = UNSET
        else:
            trust_model = CreateRepoOptionTrustModel(_trust_model)

        create_repo_option = cls(
            name=name,
            auto_init=auto_init,
            create_develop_branch=create_develop_branch,
            default_branch=default_branch,
            description=description,
            gitignores=gitignores,
            issue_labels=issue_labels,
            license_=license_,
            private=private,
            readme=readme,
            template=template,
            trust_model=trust_model,
        )

        create_repo_option.additional_properties = d
        return create_repo_option

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
