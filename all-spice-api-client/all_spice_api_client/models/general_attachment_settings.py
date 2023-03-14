from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeneralAttachmentSettings")


@attr.s(auto_attribs=True)
class GeneralAttachmentSettings:
    """GeneralAttachmentSettings contains global Attachment settings exposed by API

    Attributes:
        allowed_types (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        max_files (Union[Unset, int]):
        max_size (Union[Unset, int]):
    """

    allowed_types: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    max_files: Union[Unset, int] = UNSET
    max_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowed_types = self.allowed_types
        enabled = self.enabled
        max_files = self.max_files
        max_size = self.max_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_types is not UNSET:
            field_dict["allowed_types"] = allowed_types
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if max_files is not UNSET:
            field_dict["max_files"] = max_files
        if max_size is not UNSET:
            field_dict["max_size"] = max_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allowed_types = d.pop("allowed_types", UNSET)

        enabled = d.pop("enabled", UNSET)

        max_files = d.pop("max_files", UNSET)

        max_size = d.pop("max_size", UNSET)

        general_attachment_settings = cls(
            allowed_types=allowed_types,
            enabled=enabled,
            max_files=max_files,
            max_size=max_size,
        )

        general_attachment_settings.additional_properties = d
        return general_attachment_settings

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
