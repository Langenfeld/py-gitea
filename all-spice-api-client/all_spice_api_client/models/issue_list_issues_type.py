from enum import Enum


class IssueListIssuesType(str, Enum):
    ISSUES = "issues"
    PULLS = "pulls"

    def __str__(self) -> str:
        return str(self.value)
