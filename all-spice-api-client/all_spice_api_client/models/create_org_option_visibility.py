from enum import Enum


class CreateOrgOptionVisibility(str, Enum):
    PUBLIC = "public"
    LIMITED = "limited"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
