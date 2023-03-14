from enum import Enum


class RepoListStatusesState(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    ERROR = "error"
    FAILURE = "failure"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
