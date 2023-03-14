from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.list_packages_type import ListPackagesType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    owner: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, ListPackagesType] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/packages/{owner}".format(client.base_url, owner=owner)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["limit"] = limit

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    owner: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, ListPackagesType] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Gets all packages of an owner

    Args:
        owner (str):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        type (Union[Unset, None, ListPackagesType]):
        q (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        client=client,
        page=page,
        limit=limit,
        type=type,
        q=q,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    owner: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, ListPackagesType] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Gets all packages of an owner

    Args:
        owner (str):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        type (Union[Unset, None, ListPackagesType]):
        q (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        client=client,
        page=page,
        limit=limit,
        type=type,
        q=q,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
