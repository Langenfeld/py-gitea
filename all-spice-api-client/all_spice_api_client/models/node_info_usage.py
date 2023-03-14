from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_info_usage_users import NodeInfoUsageUsers


T = TypeVar("T", bound="NodeInfoUsage")


@attr.s(auto_attribs=True)
class NodeInfoUsage:
    """NodeInfoUsage contains usage statistics for this server

    Attributes:
        local_comments (Union[Unset, int]):
        local_posts (Union[Unset, int]):
        users (Union[Unset, NodeInfoUsageUsers]): NodeInfoUsageUsers contains statistics about the users of this server
    """

    local_comments: Union[Unset, int] = UNSET
    local_posts: Union[Unset, int] = UNSET
    users: Union[Unset, "NodeInfoUsageUsers"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        local_comments = self.local_comments
        local_posts = self.local_posts
        users: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_comments is not UNSET:
            field_dict["localComments"] = local_comments
        if local_posts is not UNSET:
            field_dict["localPosts"] = local_posts
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.node_info_usage_users import NodeInfoUsageUsers

        d = src_dict.copy()
        local_comments = d.pop("localComments", UNSET)

        local_posts = d.pop("localPosts", UNSET)

        _users = d.pop("users", UNSET)
        users: Union[Unset, NodeInfoUsageUsers]
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = NodeInfoUsageUsers.from_dict(_users)

        node_info_usage = cls(
            local_comments=local_comments,
            local_posts=local_posts,
            users=users,
        )

        node_info_usage.additional_properties = d
        return node_info_usage

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
