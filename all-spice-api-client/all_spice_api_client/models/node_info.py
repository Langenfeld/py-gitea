from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_info_metadata import NodeInfoMetadata
    from ..models.node_info_services import NodeInfoServices
    from ..models.node_info_software import NodeInfoSoftware
    from ..models.node_info_usage import NodeInfoUsage


T = TypeVar("T", bound="NodeInfo")


@attr.s(auto_attribs=True)
class NodeInfo:
    """NodeInfo contains standardized way of exposing metadata about a server running one of the distributed social
    networks

        Attributes:
            metadata (Union[Unset, NodeInfoMetadata]):
            open_registrations (Union[Unset, bool]):
            protocols (Union[Unset, List[str]]):
            services (Union[Unset, NodeInfoServices]): NodeInfoServices contains the third party sites this server can
                connect to via their application API
            software (Union[Unset, NodeInfoSoftware]): NodeInfoSoftware contains Metadata about server software in use
            usage (Union[Unset, NodeInfoUsage]): NodeInfoUsage contains usage statistics for this server
            version (Union[Unset, str]):
    """

    metadata: Union[Unset, "NodeInfoMetadata"] = UNSET
    open_registrations: Union[Unset, bool] = UNSET
    protocols: Union[Unset, List[str]] = UNSET
    services: Union[Unset, "NodeInfoServices"] = UNSET
    software: Union[Unset, "NodeInfoSoftware"] = UNSET
    usage: Union[Unset, "NodeInfoUsage"] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        open_registrations = self.open_registrations
        protocols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.protocols, Unset):
            protocols = self.protocols

        services: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.services, Unset):
            services = self.services.to_dict()

        software: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.software, Unset):
            software = self.software.to_dict()

        usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if open_registrations is not UNSET:
            field_dict["openRegistrations"] = open_registrations
        if protocols is not UNSET:
            field_dict["protocols"] = protocols
        if services is not UNSET:
            field_dict["services"] = services
        if software is not UNSET:
            field_dict["software"] = software
        if usage is not UNSET:
            field_dict["usage"] = usage
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.node_info_metadata import NodeInfoMetadata
        from ..models.node_info_services import NodeInfoServices
        from ..models.node_info_software import NodeInfoSoftware
        from ..models.node_info_usage import NodeInfoUsage

        d = src_dict.copy()
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, NodeInfoMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = NodeInfoMetadata.from_dict(_metadata)

        open_registrations = d.pop("openRegistrations", UNSET)

        protocols = cast(List[str], d.pop("protocols", UNSET))

        _services = d.pop("services", UNSET)
        services: Union[Unset, NodeInfoServices]
        if isinstance(_services, Unset):
            services = UNSET
        else:
            services = NodeInfoServices.from_dict(_services)

        _software = d.pop("software", UNSET)
        software: Union[Unset, NodeInfoSoftware]
        if isinstance(_software, Unset):
            software = UNSET
        else:
            software = NodeInfoSoftware.from_dict(_software)

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, NodeInfoUsage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = NodeInfoUsage.from_dict(_usage)

        version = d.pop("version", UNSET)

        node_info = cls(
            metadata=metadata,
            open_registrations=open_registrations,
            protocols=protocols,
            services=services,
            software=software,
            usage=usage,
            version=version,
        )

        node_info.additional_properties = d
        return node_info

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
