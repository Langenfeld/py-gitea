from enum import Enum


class MergePullRequestOptionDo(str, Enum):
    MERGE = "merge"
    REBASE = "rebase"
    REBASE_MERGE = "rebase-merge"
    SQUASH = "squash"
    MANUALLY_MERGED = "manually-merged"

    def __str__(self) -> str:
        return str(self.value)
