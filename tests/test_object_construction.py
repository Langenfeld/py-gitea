from unittest import TestCase
import pytest
from utils import suid

from gitea import (
    Gitea,
    Organization,
)


class PyGiteaInternaTests(TestCase):
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
        self.team = g.create_team(self.org, self.test_team_name, "some-desc", "loc")

    def test_non_changable_field(self):
        org = Organization.request(self.g, self.test_org_name)
        with pytest.raises(AttributeError) as e:
            org.id = 55

    def test_hashing(self):
        # just call the hash function of each object to see if something bad happens
        # TODO test for milestones (Todo: add milestone adding)
        repo = self.org.get_repositories()[0]
        milestone = repo.create_milestone("mystone", "this is only a teststone")
        issue = repo.create_issue("Testissue", set(), "this is a testing issue")
        branch = repo.get_branches()[0]
        commit = repo.get_commits()[0]
        items = set()
        items.add(self.org)
        items.add(self.team)
        items.add(self.repo)
        items.add(issue)
        items.add(branch)
        items.add(commit)
        items.add(milestone)
