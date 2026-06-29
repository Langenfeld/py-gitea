from unittest import TestCase
import pytest
from utils import suid

from gitea import (
    Gitea,
    Team,
    Repository,
    Issue,
    Milestone,
)
from gitea import NotFoundException


class RepoFunctions(TestCase):
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


    def test_create_repo_userowned(self):
        test_repo_name = f"test_repo_{suid()}"
        repo = self.g.create_repo(self.user,test_repo_name , "user owned repo")
        assert repo.description == "user owned repo"
        assert repo.owner == self.user
        assert repo.name == test_repo_name
        assert not repo.private

    def test_create_repo_orgowned(self):
        test_repo_name = f"test_repo_{suid()}"
        repo = self.g.create_repo(self.org, test_repo_name, "descr")
        assert repo.description == "descr"
        assert repo.owner == self.org
        assert repo.name == test_repo_name
        assert not repo.private

    def test_patch_repo(self):
        fields = {
            "allow_rebase": False,
            "allow_rebase_explicit": False,
            "allow_rebase_update": False,
            "description": "new description",
            "has_projects": True,
            "private": True,
        }
        for field, value in fields.items():
            setattr(self.repo, field, value)
        self.repo.commit()
        repod = self.org.get_repository(self.test_repo_name)
        for field, value in fields.items():
            assert getattr(repod, field) == value

    def test_create_team(self):
        team = self.g.create_team(self.org, self.test_team_name, "descr")
        assert team.name == self.test_team_name
        assert team.description == "descr"
        assert team.organization == self.org

    def test_patch_team(self):
        # TODO: fix this test when automatic testing works
        fields = {
            "can_create_org_repo": True,
            "description": "patched description",
            "includes_all_repositories": True,
            "name": "newname",
            "permission": "write",
        }
        test_team_name = f"team_{suid()}"
        team = self.g.create_team(self.org, test_team_name, "descr")
        for field, value in fields.items():
            setattr(team, field, value)
        team.commit()
        team = Team.request(self.g, team.id)
        assert team is not None

    def test_request_team(self):
        test_team_name = f"team_{suid()}"
        self.g.create_team(self.org, test_team_name, "descr")
        team = self.org.get_team(test_team_name)
        team2 = Team.request(self.g, team.id)
        assert team2.name == team.name

    def test_create_milestone(self):
        ms = self.repo.create_milestone("I love this Milestone", "Find an otter to adopt this milestone")
        assert isinstance(ms, Milestone)
        assert ms.title == "I love this Milestone"

    def test_change_issue(self):
        repo = self.org.get_repositories()[0]
        ms_title = "othermilestone"
        issue = Issue.create_issue(self.g, repo, "IssueTestissue with Testinput", "asdf2332")
        new_body = "some new description with some more of that char stuff :)"
        issue.body = new_body
        issue.commit()
        number = issue.number
        del issue
        issue2 = Issue.request(self.g, self.org.username, repo.name, number)
        assert issue2.body == new_body
        milestone = repo.create_milestone(ms_title, "this is only a teststone2")
        issue2.milestone = milestone
        issue2.commit()
        del issue2
        issue3 = Issue.request(self.g, self.org.username, repo.name, number)
        assert issue3.milestone is not None
        assert issue3.milestone.description == "this is only a teststone2"
        issues = repo.get_issues()
        assert len([issue for issue in issues if issue.milestone is not None and issue.milestone.title == ms_title]) > 0

    def test_create_issue(self):
        issue = Issue.create_issue(self.g, self.repo, "TestIssue", "Body text with this issue")
        assert issue.state == Issue.OPENED
        assert issue.title == "TestIssue"
        assert issue.body == "Body text with this issue"

    def test_team_get_org(self):
        teams = self.user.get_teams()
        assert self.org.username == teams[0].organization.name

    def test_topic_functions(self):
        self.repo.add_topic("rings")
        self.repo.add_topic("swords")
        self.repo.add_topic("dragons")
        assert "swords" in self.repo.get_topics()
        self.repo.del_topic("swords")
        assert "swords" not in self.repo.get_topics()
        assert "dragons" in self.repo.get_topics()
        assert "rings" in self.repo.get_topics()

    def test_delete_repo_userowned(self):
        test_repo = f"repo_{suid()}"
        repo = self.org.create_repo(test_repo, "")
        assert repo.name == test_repo
        repo.delete()
        with pytest.raises(NotFoundException) as e:
            Repository.request(self.g, self.org, test_repo)

    def test_delete_repo_orgowned(self):
        test_repo = f"repo_{suid()}"
        repo = self.org.create_repo(test_repo, "")
        assert repo.name == test_repo
        repo.delete()
        with pytest.raises(NotFoundException) as e:
            Repository.request(self.g, self.user, test_repo)

    def test_change_repo_ownership_org(self):
        test_org = f"org_{suid()}"
        new_org = self.g.create_org(self.user, test_org + "_repomove", "Org for testing moving repositories")
        new_team = self.g.create_team(new_org, self.test_team_name + "_repomove", "descr")
        repo_name = self.test_repo_name + "_repomove"
        repo = self.g.create_repo(self.org, repo_name, "descr")
        assert repo is not None
        repo.transfer_ownership(new_org, set([new_team]))
        assert repo_name not in [repo.name for repo in self.org.get_repositories()]
        assert repo_name in [repo.name for repo in new_org.get_repositories()]

    def test_change_repo_ownership_user(self):
        test_repo = f"repo_{suid()}"
        repo_name = test_repo + "_repomove"
        repo = self.g.create_repo(self.org, repo_name, "descr")
        assert repo is not None
        repo.transfer_ownership(self.user)
        assert repo_name not in [repo.name for repo in self.org.get_repositories()]
        assert repo_name in [repo.name for repo in self.user.get_repositories()]
        for repo in self.user.get_repositories():
            repo.transfer_ownership(self.org)
            assert repo_name in [repo.name for repo in self.org.get_repositories()]
            assert repo_name not in [repo.name for repo in self.user.get_repositories()]
