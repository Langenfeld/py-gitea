from enum import Enum


class RepoDownloadCommitDiffOrPatchDiffType(str, Enum):
    DIFF = "diff"
    PATCH = "patch"

    def __str__(self) -> str:
        return str(self.value)
