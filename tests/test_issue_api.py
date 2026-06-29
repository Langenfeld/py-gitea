from unittest import TestCase

import pytest

import base64
from typing import Final

import pytest
import uuid
from utils import suid

from gitea import (
    Gitea,
    User,
    Organization,
    Team,
    Repository,
    Issue,
    Milestone,
    MigrationServices,
)
from gitea import NotFoundException, AlreadyExistsException
from utils import generate_random_color


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

    def test_create_repo_labels(self):
        for i in range(0, 3):
            self.repo.create_label(f"label-{i}", generate_random_color())
        repot = self.org.get_repository(self.test_repo_name)
        labels = repot.get_labels()
        label_names = [l.name for l in labels]
        for i in range(0, 3):
            assert f"label-{i}" in label_names
        title: Final[str] = "Label Test"
        issue = Issue.create_issue(self.g, self.repo, title , "Dis is a label test")
        issue.set_labels([labels[1]])
        issuet = {i.title: i for i in self.repo.get_issues()}
        assert title in issuet
        assert labels[1] in issuet[title].labels

    def test_create_org_labels(self):
        for i in range(0, 3):
            self.org.create_label(f"label-{i}", generate_random_color())
        orgt = Organization.request(self.g, self.test_org_name)
        labels = orgt.get_labels()
        label_names = [l.name for l in labels]
        for i in range(0, 3):
            assert f"label-{i}" in label_names