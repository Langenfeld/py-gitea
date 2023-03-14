from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
    include_desc: Union[Unset, None, bool] = UNSET,
    uid: Union[Unset, None, int] = UNSET,
    priority_owner_id: Union[Unset, None, int] = UNSET,
    team_id: Union[Unset, None, int] = UNSET,
    starred_by: Union[Unset, None, int] = UNSET,
    private: Union[Unset, None, bool] = UNSET,
    is_private: Union[Unset, None, bool] = UNSET,
    template: Union[Unset, None, bool] = UNSET,
    archived: Union[Unset, None, bool] = UNSET,
    mode: Union[Unset, None, str] = UNSET,
    exclusive: Union[Unset, None, bool] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    order: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repos/search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["q"] = q

    params["topic"] = topic

    params["includeDesc"] = include_desc

    params["uid"] = uid

    params["priority_owner_id"] = priority_owner_id

    params["team_id"] = team_id

    params["starredBy"] = starred_by

    params["private"] = private

    params["is_private"] = is_private

    params["template"] = template

    params["archived"] = archived

    params["mode"] = mode

    params["exclusive"] = exclusive

    params["sort"] = sort

    params["order"] = order

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
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
    include_desc: Union[Unset, None, bool] = UNSET,
    uid: Union[Unset, None, int] = UNSET,
    priority_owner_id: Union[Unset, None, int] = UNSET,
    team_id: Union[Unset, None, int] = UNSET,
    starred_by: Union[Unset, None, int] = UNSET,
    private: Union[Unset, None, bool] = UNSET,
    is_private: Union[Unset, None, bool] = UNSET,
    template: Union[Unset, None, bool] = UNSET,
    archived: Union[Unset, None, bool] = UNSET,
    mode: Union[Unset, None, str] = UNSET,
    exclusive: Union[Unset, None, bool] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    order: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """Search for repositories

    Args:
        q (Union[Unset, None, str]):
        topic (Union[Unset, None, bool]):
        include_desc (Union[Unset, None, bool]):
        uid (Union[Unset, None, int]):
        priority_owner_id (Union[Unset, None, int]):
        team_id (Union[Unset, None, int]):
        starred_by (Union[Unset, None, int]):
        private (Union[Unset, None, bool]):
        is_private (Union[Unset, None, bool]):
        template (Union[Unset, None, bool]):
        archived (Union[Unset, None, bool]):
        mode (Union[Unset, None, str]):
        exclusive (Union[Unset, None, bool]):
        sort (Union[Unset, None, str]):
        order (Union[Unset, None, str]):
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
        q=q,
        topic=topic,
        include_desc=include_desc,
        uid=uid,
        priority_owner_id=priority_owner_id,
        team_id=team_id,
        starred_by=starred_by,
        private=private,
        is_private=is_private,
        template=template,
        archived=archived,
        mode=mode,
        exclusive=exclusive,
        sort=sort,
        order=order,
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
    q: Union[Unset, None, str] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
    include_desc: Union[Unset, None, bool] = UNSET,
    uid: Union[Unset, None, int] = UNSET,
    priority_owner_id: Union[Unset, None, int] = UNSET,
    team_id: Union[Unset, None, int] = UNSET,
    starred_by: Union[Unset, None, int] = UNSET,
    private: Union[Unset, None, bool] = UNSET,
    is_private: Union[Unset, None, bool] = UNSET,
    template: Union[Unset, None, bool] = UNSET,
    archived: Union[Unset, None, bool] = UNSET,
    mode: Union[Unset, None, str] = UNSET,
    exclusive: Union[Unset, None, bool] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
    order: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """Search for repositories

    Args:
        q (Union[Unset, None, str]):
        topic (Union[Unset, None, bool]):
        include_desc (Union[Unset, None, bool]):
        uid (Union[Unset, None, int]):
        priority_owner_id (Union[Unset, None, int]):
        team_id (Union[Unset, None, int]):
        starred_by (Union[Unset, None, int]):
        private (Union[Unset, None, bool]):
        is_private (Union[Unset, None, bool]):
        template (Union[Unset, None, bool]):
        archived (Union[Unset, None, bool]):
        mode (Union[Unset, None, str]):
        exclusive (Union[Unset, None, bool]):
        sort (Union[Unset, None, str]):
        order (Union[Unset, None, str]):
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
        q=q,
        topic=topic,
        include_desc=include_desc,
        uid=uid,
        priority_owner_id=priority_owner_id,
        team_id=team_id,
        starred_by=starred_by,
        private=private,
        is_private=is_private,
        template=template,
        archived=archived,
        mode=mode,
        exclusive=exclusive,
        sort=sort,
        order=order,
        page=page,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
