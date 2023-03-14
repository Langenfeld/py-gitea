from enum import Enum


class RepoListStatusesByRefSort(str, Enum):
    OLDEST = "oldest"
    RECENTUPDATE = "recentupdate"
    LEASTUPDATE = "leastupdate"
    LEASTINDEX = "leastindex"
    HIGHESTINDEX = "highestindex"

    def __str__(self) -> str:
        return str(self.value)
