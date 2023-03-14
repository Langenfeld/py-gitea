from enum import Enum


class IssueListIssuesState(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
