from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.repo_create_release_attachment_multipart_data import RepoCreateReleaseAttachmentMultipartData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    owner: str,
    repo: str,
    id: int,
    *,
    client: Client,
    multipart_data: RepoCreateReleaseAttachmentMultipartData,
    name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/releases/{id}/assets".format(client.base_url, owner=owner, repo=repo, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.CREATED:
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
    id: int,
    *,
    client: Client,
    multipart_data: RepoCreateReleaseAttachmentMultipartData,
    name: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Create a release attachment

    Args:
        owner (str):
        repo (str):
        id (int):
        name (Union[Unset, None, str]):
        multipart_data (RepoCreateReleaseAttachmentMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        id=id,
        client=client,
        multipart_data=multipart_data,
        name=name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    owner: str,
    repo: str,
    id: int,
    *,
    client: Client,
    multipart_data: RepoCreateReleaseAttachmentMultipartData,
    name: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Create a release attachment

    Args:
        owner (str):
        repo (str):
        id (int):
        name (Union[Unset, None, str]):
        multipart_data (RepoCreateReleaseAttachmentMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        id=id,
        client=client,
        multipart_data=multipart_data,
        name=name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
