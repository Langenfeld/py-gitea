from enum import Enum


class RepoListPullRequestsState(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
