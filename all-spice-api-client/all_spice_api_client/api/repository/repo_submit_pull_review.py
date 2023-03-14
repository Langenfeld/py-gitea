from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.submit_pull_review_options import SubmitPullReviewOptions
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    index: int,
    id: int,
    *,
    client: Client,
    json_body: SubmitPullReviewOptions,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/pulls/{index}/reviews/{id}".format(
        client.base_url, owner=owner, repo=repo, index=index, id=id
    )

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
    index: int,
    id: int,
    *,
    client: Client,
    json_body: SubmitPullReviewOptions,
) -> Response[Any]:
    """Submit a pending review to an pull request

    Args:
        owner (str):
        repo (str):
        index (int):
        id (int):
        json_body (SubmitPullReviewOptions): SubmitPullReviewOptions are options to submit a
            pending pull review

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
    owner: str,
    repo: str,
    index: int,
    id: int,
    *,
    client: Client,
    json_body: SubmitPullReviewOptions,
) -> Response[Any]:
    """Submit a pending review to an pull request

    Args:
        owner (str):
        repo (str):
        index (int):
        id (int):
        json_body (SubmitPullReviewOptions): SubmitPullReviewOptions are options to submit a
            pending pull review

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
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
