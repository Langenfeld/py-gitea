from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.edit_branch_protection_option import EditBranchProtectionOption
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    name: str,
    *,
    client: Client,
    json_body: EditBranchProtectionOption,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/branch_protections/{name}".format(client.base_url, owner=owner, repo=repo, name=name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
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
    name: str,
    *,
    client: Client,
    json_body: EditBranchProtectionOption,
) -> Response[Any]:
    """Edit a branch protections for a repository. Only fields that are set will be changed

    Args:
        owner (str):
        repo (str):
        name (str):
        json_body (EditBranchProtectionOption): EditBranchProtectionOption options for editing a
            branch protection

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        name=name,
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
    name: str,
    *,
    client: Client,
    json_body: EditBranchProtectionOption,
) -> Response[Any]:
    """Edit a branch protections for a repository. Only fields that are set will be changed

    Args:
        owner (str):
        repo (str):
        name (str):
        json_body (EditBranchProtectionOption): EditBranchProtectionOption options for editing a
            branch protection

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        name=name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
