from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_object_represents_a_git_object import GitObjectRepresentsAGitObject


T = TypeVar("T", bound="ReferenceRepresentsAGitReference")


@attr.s(auto_attribs=True)
class ReferenceRepresentsAGitReference:
    """
    Attributes:
        object_ (Union[Unset, GitObjectRepresentsAGitObject]):
        ref (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    object_: Union[Unset, "GitObjectRepresentsAGitObject"] = UNSET
    ref: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.to_dict()

        ref = self.ref
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if ref is not UNSET:
            field_dict["ref"] = ref
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.git_object_represents_a_git_object import GitObjectRepresentsAGitObject

        d = src_dict.copy()
        _object_ = d.pop("object", UNSET)
        object_: Union[Unset, GitObjectRepresentsAGitObject]
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = GitObjectRepresentsAGitObject.from_dict(_object_)

        ref = d.pop("ref", UNSET)

        url = d.pop("url", UNSET)

        reference_represents_a_git_reference = cls(
            object_=object_,
            ref=ref,
            url=url,
        )

        reference_represents_a_git_reference.additional_properties = d
        return reference_represents_a_git_reference

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
