from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_o_auth_2_application_options import CreateOAuth2ApplicationOptions
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: Client,
    json_body: CreateOAuth2ApplicationOptions,
) -> Dict[str, Any]:
    url = "{}/user/applications/oauth2/{id}".format(client.base_url, id=id)

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
    id: int,
    *,
    client: Client,
    json_body: CreateOAuth2ApplicationOptions,
) -> Response[Any]:
    """update an OAuth2 Application, this includes regenerating the client secret

    Args:
        id (int):
        json_body (CreateOAuth2ApplicationOptions): CreateOAuth2ApplicationOptions holds options
            to create an oauth2 application

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    json_body: CreateOAuth2ApplicationOptions,
) -> Response[Any]:
    """update an OAuth2 Application, this includes regenerating the client secret

    Args:
        id (int):
        json_body (CreateOAuth2ApplicationOptions): CreateOAuth2ApplicationOptions holds options
            to create an oauth2 application

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
