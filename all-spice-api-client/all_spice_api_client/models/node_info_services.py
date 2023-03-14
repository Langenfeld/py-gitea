from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeInfoServices")


@attr.s(auto_attribs=True)
class NodeInfoServices:
    """NodeInfoServices contains the third party sites this server can connect to via their application API

    Attributes:
        inbound (Union[Unset, List[str]]):
        outbound (Union[Unset, List[str]]):
    """

    inbound: Union[Unset, List[str]] = UNSET
    outbound: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inbound: Union[Unset, List[str]] = UNSET
        if not isinstance(self.inbound, Unset):
            inbound = self.inbound

        outbound: Union[Unset, List[str]] = UNSET
        if not isinstance(self.outbound, Unset):
            outbound = self.outbound

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbound is not UNSET:
            field_dict["inbound"] = inbound
        if outbound is not UNSET:
            field_dict["outbound"] = outbound

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        inbound = cast(List[str], d.pop("inbound", UNSET))

        outbound = cast(List[str], d.pop("outbound", UNSET))

        node_info_services = cls(
            inbound=inbound,
            outbound=outbound,
        )

        node_info_services.additional_properties = d
        return node_info_services

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
