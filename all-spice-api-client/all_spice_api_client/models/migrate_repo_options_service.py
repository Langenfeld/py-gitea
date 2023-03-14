from enum import Enum


class MigrateRepoOptionsService(str, Enum):
    GIT = "git"
    GITHUB = "github"
    GITEA = "gitea"
    GITLAB = "gitlab"

    def __str__(self) -> str:
        return str(self.value)
