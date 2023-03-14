from enum import Enum


class CreateRepoOptionTrustModel(str, Enum):
    DEFAULT = "default"
    COLLABORATOR = "collaborator"
    COMMITTER = "committer"
    COLLABORATORCOMMITTER = "collaboratorcommitter"

    def __str__(self) -> str:
        return str(self.value)
