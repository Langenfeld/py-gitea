import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.notify_get_repo_list_subject_type_item import NotifyGetRepoListSubjectTypeItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
    all_: Union[Unset, None, bool] = UNSET,
    status_types: Union[Unset, None, List[str]] = UNSET,
    subject_type: Union[Unset, None, List[NotifyGetRepoListSubjectTypeItem]] = UNSET,
    since: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/notifications".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["all"] = all_

    json_status_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(status_types, Unset):
        if status_types is None:
            json_status_types = None
        else:
            json_status_types = status_types

    params["status-types"] = json_status_types

    json_subject_type: Union[Unset, None, List[str]] = UNSET
    if not isinstance(subject_type, Unset):
        if subject_type is None:
            json_subject_type = None
        else:
            json_subject_type = []
            for subject_type_item_data in subject_type:
                subject_type_item = subject_type_item_data.value

                json_subject_type.append(subject_type_item)

    params["subject-type"] = json_subject_type

    json_since: Union[Unset, None, str] = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat() if since else None

    params["since"] = json_since

    json_before: Union[Unset, None, str] = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat() if before else None

    params["before"] = json_before

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
    all_: Union[Unset, None, bool] = UNSET,
    status_types: Union[Unset, None, List[str]] = UNSET,
    subject_type: Union[Unset, None, List[NotifyGetRepoListSubjectTypeItem]] = UNSET,
    since: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """List users's notification threads on a specific repo

    Args:
        owner (str):
        repo (str):
        all_ (Union[Unset, None, bool]):
        status_types (Union[Unset, None, List[str]]):
        subject_type (Union[Unset, None, List[NotifyGetRepoListSubjectTypeItem]]):
        since (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
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
        all_=all_,
        status_types=status_types,
        subject_type=subject_type,
        since=since,
        before=before,
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
    all_: Union[Unset, None, bool] = UNSET,
    status_types: Union[Unset, None, List[str]] = UNSET,
    subject_type: Union[Unset, None, List[NotifyGetRepoListSubjectTypeItem]] = UNSET,
    since: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """List users's notification threads on a specific repo

    Args:
        owner (str):
        repo (str):
        all_ (Union[Unset, None, bool]):
        status_types (Union[Unset, None, List[str]]):
        subject_type (Union[Unset, None, List[NotifyGetRepoListSubjectTypeItem]]):
        since (Union[Unset, None, datetime.datetime]):
        before (Union[Unset, None, datetime.datetime]):
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
        all_=all_,
        status_types=status_types,
        subject_type=subject_type,
        since=since,
        before=before,
        page=page,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
