from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_status_option import CreateStatusOption
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    sha: str,
    *,
    client: Client,
    json_body: CreateStatusOption,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/statuses/{sha}".format(client.base_url, owner=owner, repo=repo, sha=sha)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    sha: str,
    *,
    client: Client,
    json_body: CreateStatusOption,
) -> Response[Any]:
    """Create a commit status

    Args:
        owner (str):
        repo (str):
        sha (str):
        json_body (CreateStatusOption): CreateStatusOption holds the information needed to create
            a new CommitStatus for a Commit

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
    sha: str,
    *,
    client: Client,
    json_body: CreateStatusOption,
) -> Response[Any]:
    """Create a commit status

    Args:
        owner (str):
        repo (str):
        sha (str):
        json_body (CreateStatusOption): CreateStatusOption holds the information needed to create
            a new CommitStatus for a Commit

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
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
