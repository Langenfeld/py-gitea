from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.repo_download_pull_diff_or_patch_diff_type import RepoDownloadPullDiffOrPatchDiffType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    owner: str,
    repo: str,
    index: int,
    diff_type: RepoDownloadPullDiffOrPatchDiffType,
    *,
    client: Client,
    binary: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/pulls/{index}.{diffType}".format(
        client.base_url, owner=owner, repo=repo, index=index, diffType=diff_type
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["binary"] = binary

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
    if response.status_code == HTTPStatus.NOT_FOUND:
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
    index: int,
    diff_type: RepoDownloadPullDiffOrPatchDiffType,
    *,
    client: Client,
    binary: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """Get a pull request diff or patch

    Args:
        owner (str):
        repo (str):
        index (int):
        diff_type (RepoDownloadPullDiffOrPatchDiffType):
        binary (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        index=index,
        diff_type=diff_type,
        client=client,
        binary=binary,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    owner: str,
    repo: str,
    index: int,
    diff_type: RepoDownloadPullDiffOrPatchDiffType,
    *,
    client: Client,
    binary: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """Get a pull request diff or patch

    Args:
        owner (str):
        repo (str):
        index (int):
        diff_type (RepoDownloadPullDiffOrPatchDiffType):
        binary (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        index=index,
        diff_type=diff_type,
        client=client,
        binary=binary,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
