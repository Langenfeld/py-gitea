from unittest import TestCase
from utils import suid

from gitea import (
    Gitea,
    Issue,
)


class PublicApiTest(TestCase):
    def setUp(self):
        """Set up a user, repo and TODO TOD"""
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
        self.user = g.get_user()
        self.org = g.create_org(self.user, self.test_org_name, "some-desc", "loc")
        self.repo = g.create_repo(self.org, self.test_repo_name, "user owned repo")


    def test_list_repos(self):
        repos = self.org.get_repositories()
        assert len(repos) == 1
        # test a number of repository listings larger than the pagination number (default 50)
        for i in range(1, 54):
            self.g.create_repo(self.org, self.test_repo_name + "_" + str(i), str(i))
        repos = self.org.get_repositories()
        assert len(repos) >= 53


    def test_list_issue(self):
        for x in range(0, 100):
            Issue.create_issue(
                self.g,
                self.repo,
                "TestIssue" + str(x),
                "We will be too many to be listed on one page",
            )
        issues = self.repo.get_issues()
        assert len(issues) > 98


    def test_list_branches(self):
        branches = self.repo.get_branches()
        master = [b for b in branches if b.name == "master"]
        assert len(master) > 0

        for x in range(0, 54):
            self.repo.add_branch(master[0], "test_branch_" + str(x) + "_" + suid())

        branches = self.repo.get_branches()
        assert len(branches) >= 53

    def test_list_tags(self):
        branches = self.repo.get_branches()
        master = [b for b in branches if b.name == "master"]
        assert len(master) > 0

        # Add all tags on last 'master' branch commit
        for x in range(0, 54):
            self.repo.add_tag("test_tag_" + str(x) + "_" + suid(), master[0].commit["id"], "test tag")

        tags = self.repo.get_tags()
        assert len(tags) >= 53

