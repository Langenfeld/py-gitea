import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
    all_: Union[Unset, None, str] = UNSET,
    status_types: Union[Unset, None, List[str]] = UNSET,
    to_status: Union[Unset, None, str] = UNSET,
    last_read_at: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/notifications".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["all"] = all_

    json_status_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(status_types, Unset):
        if status_types is None:
            json_status_types = None
        else:
            json_status_types = status_types

    params["status-types"] = json_status_types

    params["to-status"] = to_status

    json_last_read_at: Union[Unset, None, str] = UNSET
    if not isinstance(last_read_at, Unset):
        json_last_read_at = last_read_at.isoformat() if last_read_at else None

    params["last_read_at"] = json_last_read_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.RESET_CONTENT:
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
    repo: str,
    *,
    client: Client,
    all_: Union[Unset, None, str] = UNSET,
    status_types: Union[Unset, None, List[str]] = UNSET,
    to_status: Union[Unset, None, str] = UNSET,
    last_read_at: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Any]:
    """Mark notification threads as read, pinned or unread on a specific repo

    Args:
        owner (str):
        repo (str):
        all_ (Union[Unset, None, str]):
        status_types (Union[Unset, None, List[str]]):
        to_status (Union[Unset, None, str]):
        last_read_at (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
        all_=all_,
        status_types=status_types,
        to_status=to_status,
        last_read_at=last_read_at,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    owner: str,
    repo: str,
    *,
    client: Client,
    all_: Union[Unset, None, str] = UNSET,
    status_types: Union[Unset, None, List[str]] = UNSET,
    to_status: Union[Unset, None, str] = UNSET,
    last_read_at: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Any]:
    """Mark notification threads as read, pinned or unread on a specific repo

    Args:
        owner (str):
        repo (str):
        all_ (Union[Unset, None, str]):
        status_types (Union[Unset, None, List[str]]):
        to_status (Union[Unset, None, str]):
        last_read_at (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
        all_=all_,
        status_types=status_types,
        to_status=to_status,
        last_read_at=last_read_at,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
