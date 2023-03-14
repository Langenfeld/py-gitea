from enum import Enum


class EditTeamOptionPermission(str, Enum):
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"

    def __str__(self) -> str:
        return str(self.value)
