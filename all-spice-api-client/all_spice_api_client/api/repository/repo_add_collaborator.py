from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.add_collaborator_option import AddCollaboratorOption
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    collaborator: str,
    *,
    client: Client,
    json_body: AddCollaboratorOption,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/collaborators/{collaborator}".format(
        client.base_url, owner=owner, repo=repo, collaborator=collaborator
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
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
    collaborator: str,
    *,
    client: Client,
    json_body: AddCollaboratorOption,
) -> Response[Any]:
    """Add a collaborator to a repository

    Args:
        owner (str):
        repo (str):
        collaborator (str):
        json_body (AddCollaboratorOption): AddCollaboratorOption options when adding a user as a
            collaborator of a repository

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        collaborator=collaborator,
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
    collaborator: str,
    *,
    client: Client,
    json_body: AddCollaboratorOption,
) -> Response[Any]:
    """Add a collaborator to a repository

    Args:
        owner (str):
        repo (str):
        collaborator (str):
        json_body (AddCollaboratorOption): AddCollaboratorOption options when adding a user as a
            collaborator of a repository

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        collaborator=collaborator,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
