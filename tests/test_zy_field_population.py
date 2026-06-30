from typing import Any, Type
from unittest import TestCase
import pytest
from mypyc.ir.ops import Branch

from utils import suid

from gitea import (
    Gitea,
    User,
    Organization,
    Repository,
)
from gitea import NotFoundException


class BasicGiteaFunctions(TestCase):
    def setUp(self):
        self.test_org_name = "org_public_" + suid()
        self.test_user_name = "user_" + suid()
        self.test_team_name = "team_" + suid()  # team names seem to have a rather low max lenght
        self.test_repo_name = "repo_" + suid()
        # get admin gitea instance to set up tests
        try:
            g = Gitea("http://localhost:3000", open(".token", "r").read().strip())
            print("Gitea Version: " + g.get_version())
            print("API-Token belongs to user: " + g.get_user().username)
        except:
            assert (
                False
            ), "Gitea could not load. \
                    - Instance running at http://localhost:3000 \
                    - Token at .token   \
                        ?"
        self.g = g
        self.user = g.create_user(
            self.test_user_name,f"{self.test_user_name}@example.org", "asdas.passwd", send_notify=False)
        self.org = g.create_org(self.user, self.test_org_name, "some-desc", "loc")
        self.repo = g.create_repo(self.org, self.test_repo_name, "user owned repo")

    def __check_fields(self, cls, object):
        for field, t in cls.__annotations__.items():
            v = getattr(object, field)
            assert v is not None
            print(f"{field} as {t}: {getattr(object, field)}")
            if t is Any:
                continue
            if isinstance(t, type):
                assert isinstance(v, t)

    def test_user_field_population(self):
        user = self.g.get_user_by_name(self.test_user_name)
        self.__check_fields(User, user)

    def test_org_field_population(self):
        user = self.g.get_user()
        create_test_name = f"create_org_{suid()}"
        org = self.g.create_org(user, create_test_name, "some-desc", "loc")
        self.__check_fields(Organization, org)

    def test_branch_field_population(self):
        branches = self.repo.get_branches()
        self.__check_fields(Branch, branches[0])
        # TODO: check fields in tags in commits

    def test_repo_field_population(self):
        repo = self.org.get_repository(self.test_repo_name)
        self.__check_fields(Repository, repo)