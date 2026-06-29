from unittest import TestCase
import pytest
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

    def test_token_owner(self):
        user = self.g.get_user()
        assert user.username == "test", "Token user not 'tests'."
        assert user.is_admin, "Testuser is not Admin - Tests may fail"

    def test_gitea_version(self):
        assert self.g.get_version().startswith("1."), "No Version String returned"

    def test_fail_get_non_existent_user(self):
        with pytest.raises(NotFoundException) as e:
            User.request(self.g, "This does not exist")

    def test_fail_get_non_existent_org(self):
        with pytest.raises(NotFoundException) as e:
            Organization.request(self.g, "This does not exist")

    def test_fail_get_non_existent_repo(self):
        with pytest.raises(NotFoundException) as e:
            Repository.request(self.g, "This does not exist", "This does not exist")

    def test_create_user(self):
        create_test_name = f"create_user_{suid()}"
        email = f"{create_test_name}@example.org"
        user = self.g.create_user(create_test_name, email, "abcdefg1.23AB", send_notify=False)
        assert user.username == create_test_name
        assert user.login == create_test_name
        assert email in user.emails
        assert user.email == email
        assert not user.is_admin
        assert type(user.id) is int
        assert user.is_admin is False

    def test_secundary_email(self):
        SECONDARYMAIL = "secondarytest@test.org"  # set up with real email
        sec_user = self.g.get_user_by_email(SECONDARYMAIL)
        assert SECONDARYMAIL in sec_user.emails
        assert sec_user.username == "test"

    def test_get_user(self):
        user = self.g.get_user_by_name(self.test_user_name)
        assert user is not None
        assert user.username == self.test_user_name

    def test_change_user(self):
        user = self.g.get_user_by_name(self.test_user_name)
        location = "a house"
        user.location = location
        new_fullname = "Other Test Full Name"
        user.full_name = new_fullname
        user.commit(user.username, 0)
        del user
        user = self.g.get_user_by_name(self.test_user_name)
        assert user.full_name == new_fullname
        assert user.location == location

    def test_create_org(self):
        user = self.g.get_user()
        create_test_name = f"create_org_{suid()}"
        org = self.g.create_org(user, create_test_name, "some-desc", "loc")
        assert org.get_members()[0] == user
        assert org.description == "some-desc"
        assert org.username == create_test_name
        assert org.location == "loc"
        assert not org.website
        assert not org.full_name

    def test_org_get_public_members(self):
        org = Organization.request(self.g, self.test_org_name)
        members = org.get_public_members()
        assert members

    def test_edit_org_fields_and_commit(self):
        org = Organization.request(self.g, self.test_org_name)
        org.description = "some thing other man"
        org.location = "somewehre new"
        org.visibility = "public"
        org.website = "http:\\\\testurl.com"
        org.commit()
        org2 = Organization.request(self.g, self.test_org_name)
        assert org2.name == self.test_org_name
        assert org2.description == "some thing other man"
        assert org2.location == "somewehre new"
        # assert org2.visibility == "private" # after commiting, this field just vanishes (Bug?)
        assert org2.website == "http:\\\\testurl.com"

    def test_user_teams(self):
        team = self.g.create_team(self.org, self.test_team_name,"A testing team for testsing teams")
        team.add_user(self.user)
        teams = self.user.get_teams()
        assert team in teams

    def test_delete_team(self):
        test_team = f"test_team_{suid()}"
        self.g.create_team(self.org, test_team)
        team = self.org.get_team(test_team)
        team.delete()
        with pytest.raises(NotFoundException) as e:
            team = self.org.get_team(test_team)

    def test_delete_repos(self):
        repos = self.org.get_repositories()
        for repo in repos:
            repo.delete()
        repos = self.org.get_repositories()
        assert len(repos) == 0

    def test_delete_org(self):
        test_org = f"test_org_{suid()}"
        test_repo = f"test_repo_{suid()}"
        # make org and make it non-empty
        torg = self.g.create_org(self.user, test_org, "Just a non-empty org")
        trepo = torg.create_repo(test_repo)
        assert trepo is not None
        # will delete anyway ...
        self.org.delete()
        with pytest.raises(NotFoundException) as e:
            Organization.request(self.g, self.test_org_name)

    def test_delete_user(self):
        test_user = f"test_user_{suid()}"
        user = self.g.create_user(test_user, f"{test_user}@t.de", "abcdefg1.23AB", send_notify=False)
        assert user is not None
        user.delete()
        with pytest.raises(NotFoundException) as e:
            User.request(self.g, test_user)