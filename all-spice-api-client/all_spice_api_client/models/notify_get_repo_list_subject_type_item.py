from enum import Enum


class NotifyGetRepoListSubjectTypeItem(str, Enum):
    ISSUE = "issue"
    PULL = "pull"
    COMMIT = "commit"
    REPOSITORY = "repository"

    def __str__(self) -> str:
        return str(self.value)
