from typing import TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from gitea import User, Organization


def get_username(user: "str | User | Organization", allow_orgs: bool = True) -> str:
    from gitea import User

    if isinstance(user, str):
        return user
    elif isinstance(user, User):
        return user.login
    elif allow_orgs:
        return user.username
    raise TypeError(f"Object of type {type(user)} is not a valid owner of anything")


def encode_timestamp(t: datetime) -> str:
    """Encode timestamp in gitea-api compatible format"""
    return t.strftime("%Y-%m-%dT%H:%M:%S.000Z") if not isinstance(t, str) else t


def decode_timestamp(time: str) -> datetime:
    """Parsing of strange Gitea time format ("%Y-%m-%dT%H:%M:%S:%z" but with ":" in time zone notation)"""
    try:
        return datetime.strptime(time[:-3] + "00", "%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        return datetime.strptime(time[:-3] + "00", "%Y-%m-%dT%H:%M:%S")
