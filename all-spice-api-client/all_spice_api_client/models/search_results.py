from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository import Repository


T = TypeVar("T", bound="SearchResults")


@attr.s(auto_attribs=True)
class SearchResults:
    """SearchResults results of a successful search

    Attributes:
        data (Union[Unset, List['Repository']]):
        ok (Union[Unset, bool]):
    """

    data: Union[Unset, List["Repository"]] = UNSET
    ok: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        ok = self.ok

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if ok is not UNSET:
            field_dict["ok"] = ok

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.repository import Repository

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = Repository.from_dict(data_item_data)

            data.append(data_item)

        ok = d.pop("ok", UNSET)

        search_results = cls(
            data=data,
            ok=ok,
        )

        search_results.additional_properties = d
        return search_results

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
