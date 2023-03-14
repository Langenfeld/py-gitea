import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    state: Union[Unset, None, str] = UNSET,
    labels: Union[Unset, None, str] = UNSET,
    milestones: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    priority_repo_id: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    since: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    assigned: Union[Unset, None, bool] = UNSET,
    created: Union[Unset, None, bool] = UNSET,
    mentioned: Union[Unset, None, bool] = UNSET,
    review_requested: Union[Unset, None, bool] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    team: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repos/issues/search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["state"] = state

    params["labels"] = labels

    params["milestones"] = milestones

    params["q"] = q

    params["priority_repo_id"] = priority_repo_id

    params["type"] = type

    json_since: Union[Unset, None, str] = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat() if since else None

    params["since"] = json_since

    json_before: Union[Unset, None, str] = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat() if before else None

    params["before"] = json_before

    params["assigned"] = assigned

    params["created"] = created

    params["mentioned"] = mentioned

    params["review_requested"] = review_requested

    params["owner"] = owner

    params["team"] = team

    params["page"] = page

    params["limit"] = limit

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
    *,
    client: Client,
    state: Union[Unset, None, str] = UNSET,
    labels: Union[Unset, None, str] = UNSET,
    milestones: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    priority_repo_id: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    since: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    assigned: Union[Unset, None, bool] = UNSET,
    created: Union[Unset, None, bool] = UNSET,
    mentioned: Union[Unset, None, bool] = UNSET,
    review_requested: Union[Unset, None, bool] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    team: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """Search for issues across the repositories that the user has access to

    Args:
        state (Union[Unset, None, str]):
        labels (Union[Unset, None, str]):
        milestones (Union[Unset, None, str]):
        q (Union[Unset, None, str]):
        priority_repo_id (Union[Unset, None, int]):
        type (Union[Unset, None, str]):
        since (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        assigned (Union[Unset, None, bool]):
        created (Union[Unset, None, bool]):
        mentioned (Union[Unset, None, bool]):
        review_requested (Union[Unset, None, bool]):
        owner (Union[Unset, None, str]):
        team (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        state=state,
        labels=labels,
        milestones=milestones,
        q=q,
        priority_repo_id=priority_repo_id,
        type=type,
        since=since,
        before=before,
        assigned=assigned,
        created=created,
        mentioned=mentioned,
        review_requested=review_requested,
        owner=owner,
        team=team,
        page=page,
        limit=limit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    state: Union[Unset, None, str] = UNSET,
    labels: Union[Unset, None, str] = UNSET,
    milestones: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    priority_repo_id: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    since: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    assigned: Union[Unset, None, bool] = UNSET,
    created: Union[Unset, None, bool] = UNSET,
    mentioned: Union[Unset, None, bool] = UNSET,
    review_requested: Union[Unset, None, bool] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    team: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """Search for issues across the repositories that the user has access to

    Args:
        state (Union[Unset, None, str]):
        labels (Union[Unset, None, str]):
        milestones (Union[Unset, None, str]):
        q (Union[Unset, None, str]):
        priority_repo_id (Union[Unset, None, int]):
        type (Union[Unset, None, str]):
        since (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        assigned (Union[Unset, None, bool]):
        created (Union[Unset, None, bool]):
        mentioned (Union[Unset, None, bool]):
        review_requested (Union[Unset, None, bool]):
        owner (Union[Unset, None, str]):
        team (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        state=state,
        labels=labels,
        milestones=milestones,
        q=q,
        priority_repo_id=priority_repo_id,
        type=type,
        since=since,
        before=before,
        assigned=assigned,
        created=created,
        mentioned=mentioned,
        review_requested=review_requested,
        owner=owner,
        team=team,
        page=page,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
