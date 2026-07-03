from typing import Any
from unittest import TestCase

from utils import suid, generate_random_color
from datetime import datetime

from gitea import Gitea, User, Organization, Repository, Branch, Milestone, Issue, Team, Label, Commit, Content

CURRENT_VERSION = "1.26"


class ApiObjectsPopulationTest(TestCase):

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
            assert False, "Gitea could not load. \
                    - Instance running at http://localhost:3000 \
                    - Token at .token   \
                        ?"
        self.g = g
        self.user = g.create_user(
            self.test_user_name, f"{self.test_user_name}@example.org", "asdas.passwd", send_notify=False
        )
        self.org = g.create_org(self.user, self.test_org_name, "some-desc", "loc")
        self.repo = g.create_repo(self.org, self.test_repo_name, "user owned repo")

    def __check_fields(self, cls, object):
        """Check if all the fields listed in the object were in deed added to the object.
        If Gitea returned more than None as a content, also check if the content type is right."""
        for field, t in cls.__annotations__.items():
            # There should be a field in the object
            self.assertTrue(hasattr(object, field), f"Field {field} in {object} should have been accessible.")
            if t is Any:
                # dont care further if there is no useful type given
                continue
            if isinstance(t, type) and (v := getattr(object, field)):
                if v is None:
                    # dont care further if Gitea did not provide a value for the field (but the field is there, yey)
                    continue
                # Check if the field has the correct type _if_ a value was given that is not None
                self.assertIsInstance(
                    v, t, f"Field {field} in {object} has a value of wrong type assigned ({type(v)})."
                )

    def test_user_field_population(self):
        if not self.g.get_version().startswith(CURRENT_VERSION):
            return
        user = self.g.get_user_by_name(self.test_user_name)
        self.__check_fields(User, user)

    def test_org_field_population(self):
        if not self.g.get_version().startswith(CURRENT_VERSION):
            return
        user = self.g.get_user()
        create_test_name = f"create_org_{suid()}"
        org = self.g.create_org(user, create_test_name, "some-desc", "loc")
        self.__check_fields(Organization, org)

    def test_branch_field_population(self):
        if not self.g.get_version().startswith(CURRENT_VERSION):
            return
        branches = self.repo.get_branches()
        self.__check_fields(Branch, branches[0])
        # TODO: check fields in tags in commits

    def test_repo_field_population(self):
        if not self.g.get_version().startswith(CURRENT_VERSION):
            return
        repo = self.org.get_repository(self.test_repo_name)
        self.__check_fields(Repository, repo)

    def test_issue_field_population(self):
        if not self.g.get_version().startswith(CURRENT_VERSION):
            return
        issue = Issue.create_issue(self.g, self.repo, "TestIssue", "Body text with this issue")
        self.__check_fields(Issue, issue)

    def test_teams_field_population(self):
        if not self.g.get_version().startswith(CURRENT_VERSION):
            return
        team = self.g.create_team(self.org, self.test_team_name, "A testing team for testsing teams")
        self.__check_fields(Team, team)

    def test_labels_field_population(self):
        self.org.create_label(f"label-1", generate_random_color())
        orgt = Organization.request(self.g, self.test_org_name)
        labels = orgt.get_labels()
        assert labels
        self.__check_fields(Label, labels[0])

    def test_milestone_field_population(self):
        if not self.g.get_version().startswith(CURRENT_VERSION):
            return
        self.repo.create_milestone("Testing Milestone", "The Bla of Blue")
        mss = self.repo.get_milestones()
        assert mss
        ms = mss[0]
        ms.state = "closed"
        ms.due_on = datetime.now()
        ms.commit()
        mss = self.repo.get_milestones(state="all")
        assert mss
        ms = mss[0]
        self.__check_fields(Milestone, ms)

    def test_commit_field_population(self):
        if not self.g.get_version().startswith(CURRENT_VERSION):
            return
        repo = self.org.get_repository(self.test_repo_name)
        c = repo.get_commits(1)
        assert c
        self.__check_fields(Commit, c[0])

    def test_content_field_population(self):
        if not self.g.get_version().startswith(CURRENT_VERSION):
            return
        content = self.repo.get_git_content()
        # Readme file should exist in any new repo
        #  content is the description given during creation
        readmes = [c for c in content if c.name == "README.md"]
        assert len(readmes) > 0
        self.__check_fields(Content, readmes[0])
