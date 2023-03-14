from enum import Enum


class RepoGetPullRequestFilesWhitespace(str, Enum):
    IGNORE_ALL = "ignore-all"
    IGNORE_CHANGE = "ignore-change"
    IGNORE_EOL = "ignore-eol"
    SHOW_ALL = "show-all"

    def __str__(self) -> str:
        return str(self.value)
