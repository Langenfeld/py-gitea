import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.issue_list_issues_state import IssueListIssuesState
from ...models.issue_list_issues_type import IssueListIssuesType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
    state: Union[Unset, None, IssueListIssuesState] = UNSET,
    labels: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, IssueListIssuesType] = UNSET,
    milestones: Union[Unset, None, str] = UNSET,
    since: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    assigned_by: Union[Unset, None, str] = UNSET,
    mentioned_by: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/issues".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params["labels"] = labels

    params["q"] = q

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["milestones"] = milestones

    json_since: Union[Unset, None, str] = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat() if since else None

    params["since"] = json_since

    json_before: Union[Unset, None, str] = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat() if before else None

    params["before"] = json_before

    params["created_by"] = created_by

    params["assigned_by"] = assigned_by

    params["mentioned_by"] = mentioned_by

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
    owner: str,
    repo: str,
    *,
    client: Client,
    state: Union[Unset, None, IssueListIssuesState] = UNSET,
    labels: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, IssueListIssuesType] = UNSET,
    milestones: Union[Unset, None, str] = UNSET,
    since: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    assigned_by: Union[Unset, None, str] = UNSET,
    mentioned_by: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """List a repository's issues

    Args:
        owner (str):
        repo (str):
        state (Union[Unset, None, IssueListIssuesState]):
        labels (Union[Unset, None, str]):
        q (Union[Unset, None, str]):
        type (Union[Unset, None, IssueListIssuesType]):
        milestones (Union[Unset, None, str]):
        since (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        created_by (Union[Unset, None, str]):
        assigned_by (Union[Unset, None, str]):
        mentioned_by (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
        state=state,
        labels=labels,
        q=q,
        type=type,
        milestones=milestones,
        since=since,
        before=before,
        created_by=created_by,
        assigned_by=assigned_by,
        mentioned_by=mentioned_by,
        page=page,
        limit=limit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    owner: str,
    repo: str,
    *,
    client: Client,
    state: Union[Unset, None, IssueListIssuesState] = UNSET,
    labels: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, IssueListIssuesType] = UNSET,
    milestones: Union[Unset, None, str] = UNSET,
    since: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    assigned_by: Union[Unset, None, str] = UNSET,
    mentioned_by: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """List a repository's issues

    Args:
        owner (str):
        repo (str):
        state (Union[Unset, None, IssueListIssuesState]):
        labels (Union[Unset, None, str]):
        q (Union[Unset, None, str]):
        type (Union[Unset, None, IssueListIssuesType]):
        milestones (Union[Unset, None, str]):
        since (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
        created_by (Union[Unset, None, str]):
        assigned_by (Union[Unset, None, str]):
        mentioned_by (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
        state=state,
        labels=labels,
        q=q,
        type=type,
        milestones=milestones,
        since=since,
        before=before,
        created_by=created_by,
        assigned_by=assigned_by,
        mentioned_by=mentioned_by,
        page=page,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
