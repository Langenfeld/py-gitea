from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_form_field_attributes import IssueFormFieldAttributes
    from ..models.issue_form_field_validations import IssueFormFieldValidations


T = TypeVar("T", bound="IssueFormField")


@attr.s(auto_attribs=True)
class IssueFormField:
    """IssueFormField represents a form field

    Attributes:
        attributes (Union[Unset, IssueFormFieldAttributes]):
        id (Union[Unset, str]):
        type (Union[Unset, str]):
        validations (Union[Unset, IssueFormFieldValidations]):
    """

    attributes: Union[Unset, "IssueFormFieldAttributes"] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    validations: Union[Unset, "IssueFormFieldValidations"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        id = self.id
        type = self.type
        validations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.validations, Unset):
            validations = self.validations.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if validations is not UNSET:
            field_dict["validations"] = validations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.issue_form_field_attributes import IssueFormFieldAttributes
        from ..models.issue_form_field_validations import IssueFormFieldValidations

        d = src_dict.copy()
        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, IssueFormFieldAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = IssueFormFieldAttributes.from_dict(_attributes)

        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        _validations = d.pop("validations", UNSET)
        validations: Union[Unset, IssueFormFieldValidations]
        if isinstance(_validations, Unset):
            validations = UNSET
        else:
            validations = IssueFormFieldValidations.from_dict(_validations)

        issue_form_field = cls(
            attributes=attributes,
            id=id,
            type=type,
            validations=validations,
        )

        issue_form_field.additional_properties = d
        return issue_form_field

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
