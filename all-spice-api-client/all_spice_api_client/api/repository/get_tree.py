from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    owner: str,
    repo: str,
    sha: str,
    *,
    client: Client,
    recursive: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/git/trees/{sha}".format(client.base_url, owner=owner, repo=repo, sha=sha)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["recursive"] = recursive

    params["page"] = page

    params["per_page"] = per_page

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
    if response.status_code == HTTPStatus.BAD_REQUEST:
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
    sha: str,
    *,
    client: Client,
    recursive: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """Gets the tree of a repository.

    Args:
        owner (str):
        repo (str):
        sha (str):
        recursive (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        sha=sha,
        client=client,
        recursive=recursive,
        page=page,
        per_page=per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    owner: str,
    repo: str,
    sha: str,
    *,
    client: Client,
    recursive: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """Gets the tree of a repository.

    Args:
        owner (str):
        repo (str):
        sha (str):
        recursive (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        sha=sha,
        client=client,
        recursive=recursive,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
