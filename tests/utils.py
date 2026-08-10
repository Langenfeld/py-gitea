from unittest import TestCase
from typing import Any, get_type_hints, get_args, get_origin, Annotated
import uuid


def generate_random_color():
    import random

    return "{:06x}".format(random.randint(0, 0xFFFFFF))


def suid() -> str:
    return str(uuid.uuid4().hex[:8])


class FieldCheckingTestCase:

    def __init__(self):
        self.version = "FAIL"

    def _check_fields(self, cls, object):
        """Check if all the fields listed in the object were in deed added to the object.
        If Gitea returned more than None as a content, also check if the content type is right.
        Note: this is a copy from field population tests, but don't what to have the git stuff there"""
        for field, t in cls.__annotations__.items():
            # Ignore this field if it has an annotation with the right gitea version
            if get_origin(t) is Annotated:
                _, *metadata = get_args(t)
                if True in [self.version.startswith(v[7:]) for v in metadata if v.startswith("ignore:")]:
                    continue
            # There should be a field in the object
            self.assertTrue(hasattr(object, field), f"Field '{field}' in '{object}' should be existing.")
            if t is Any:
                # don't care further if there is no useful type given
                continue
            if isinstance(t, type) and (v := getattr(object, field)):
                if v is None:
                    # don't care further if Gitea did not provide a value for the field (but the field is there, yey)
                    continue
                # Check if the field has the correct type _if_ a value was given that is not None
                self.assertIsInstance(
                    v, t, f"Field {field} in {object} has a value of wrong type assigned ({type(v)})."
                )
