from enum import Enum


class RepoListPullRequestsSort(str, Enum):
    OLDEST = "oldest"
    RECENTUPDATE = "recentupdate"
    LEASTUPDATE = "leastupdate"
    MOSTCOMMENT = "mostcomment"
    LEASTCOMMENT = "leastcomment"
    PRIORITY = "priority"

    def __str__(self) -> str:
        return str(self.value)
