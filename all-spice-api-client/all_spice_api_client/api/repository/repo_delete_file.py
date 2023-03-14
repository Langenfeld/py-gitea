from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.delete_file_options import DeleteFileOptions
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    filepath: str,
    *,
    client: Client,
    json_body: DeleteFileOptions,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/contents/{filepath}".format(
        client.base_url, owner=owner, repo=repo, filepath=filepath
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
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
    filepath: str,
    *,
    client: Client,
    json_body: DeleteFileOptions,
) -> Response[Any]:
    """Delete a file in a repository

    Args:
        owner (str):
        repo (str):
        filepath (str):
        json_body (DeleteFileOptions): DeleteFileOptions options for deleting files (used for
            other File structs below)
            Note: `author` and `committer` are optional (if only one is given, it will be used for the
            other, otherwise the authenticated user will be used)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        filepath=filepath,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    owner: str,
    repo: str,
    filepath: str,
    *,
    client: Client,
    json_body: DeleteFileOptions,
) -> Response[Any]:
    """Delete a file in a repository

    Args:
        owner (str):
        repo (str):
        filepath (str):
        json_body (DeleteFileOptions): DeleteFileOptions options for deleting files (used for
            other File structs below)
            Note: `author` and `committer` are optional (if only one is given, it will be used for the
            other, otherwise the authenticated user will be used)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        filepath=filepath,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
