from enum import Enum


class RepoUpdatePullRequestStyle(str, Enum):
    MERGE = "merge"
    REBASE = "rebase"

    def __str__(self) -> str:
        return str(self.value)
