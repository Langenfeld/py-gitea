from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.team_search_response_200 import TeamSearchResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org: str,
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    include_desc: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/teams/search".format(client.base_url, org=org)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["q"] = q

    params["include_desc"] = include_desc

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[TeamSearchResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TeamSearchResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[TeamSearchResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org: str,
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    include_desc: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[TeamSearchResponse200]:
    """Search for teams within an organization

    Args:
        org (str):
        q (Union[Unset, None, str]):
        include_desc (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamSearchResponse200]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
        q=q,
        include_desc=include_desc,
        page=page,
        limit=limit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org: str,
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    include_desc: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[TeamSearchResponse200]:
    """Search for teams within an organization

    Args:
        org (str):
        q (Union[Unset, None, str]):
        include_desc (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamSearchResponse200]
    """

    return sync_detailed(
        org=org,
        client=client,
        q=q,
        include_desc=include_desc,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    org: str,
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    include_desc: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[TeamSearchResponse200]:
    """Search for teams within an organization

    Args:
        org (str):
        q (Union[Unset, None, str]):
        include_desc (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamSearchResponse200]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
        q=q,
        include_desc=include_desc,
        page=page,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org: str,
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    include_desc: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[TeamSearchResponse200]:
    """Search for teams within an organization

    Args:
        org (str):
        q (Union[Unset, None, str]):
        include_desc (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamSearchResponse200]
    """

    return (
        await asyncio_detailed(
            org=org,
            client=client,
            q=q,
            include_desc=include_desc,
            page=page,
            limit=limit,
        )
    ).parsed
