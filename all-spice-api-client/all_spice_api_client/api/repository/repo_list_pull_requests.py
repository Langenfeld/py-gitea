from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.repo_list_pull_requests_sort import RepoListPullRequestsSort
from ...models.repo_list_pull_requests_state import RepoListPullRequestsState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
    state: Union[Unset, None, RepoListPullRequestsState] = UNSET,
    sort: Union[Unset, None, RepoListPullRequestsSort] = UNSET,
    milestone: Union[Unset, None, int] = UNSET,
    labels: Union[Unset, None, List[int]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/pulls".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    params["milestone"] = milestone

    json_labels: Union[Unset, None, List[int]] = UNSET
    if not isinstance(labels, Unset):
        if labels is None:
            json_labels = None
        else:
            json_labels = labels

    params["labels"] = json_labels

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
    state: Union[Unset, None, RepoListPullRequestsState] = UNSET,
    sort: Union[Unset, None, RepoListPullRequestsSort] = UNSET,
    milestone: Union[Unset, None, int] = UNSET,
    labels: Union[Unset, None, List[int]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """List a repo's pull requests

    Args:
        owner (str):
        repo (str):
        state (Union[Unset, None, RepoListPullRequestsState]):
        sort (Union[Unset, None, RepoListPullRequestsSort]):
        milestone (Union[Unset, None, int]):
        labels (Union[Unset, None, List[int]]):
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
        sort=sort,
        milestone=milestone,
        labels=labels,
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
    state: Union[Unset, None, RepoListPullRequestsState] = UNSET,
    sort: Union[Unset, None, RepoListPullRequestsSort] = UNSET,
    milestone: Union[Unset, None, int] = UNSET,
    labels: Union[Unset, None, List[int]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """List a repo's pull requests

    Args:
        owner (str):
        repo (str):
        state (Union[Unset, None, RepoListPullRequestsState]):
        sort (Union[Unset, None, RepoListPullRequestsSort]):
        milestone (Union[Unset, None, int]):
        labels (Union[Unset, None, List[int]]):
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
        sort=sort,
        milestone=milestone,
        labels=labels,
        page=page,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
