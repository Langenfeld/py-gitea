from enum import Enum


class TeamPermission(str, Enum):
    NONE = "none"
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
