import os

from gitea import Gitea, User, Organization, Team, Repository, version
from gitea import NotFoundException, AlreadyExistsException

assert version >= '0.4.0'


# Testing a localhost instance for API-functionality.
#


# testing includes:
# - reading in token
# - creation of organization
# - creation of repository
# - creation of team
# - creation of user
# - assigning team to repository
# - assigning user to team
# - deleting created user
# - deleting repository
# - deleting team
# - deleting organization


def expect_not_exist(fn, expect) -> bool:
    try:
        fn()
        return False
    except expect:
        return True


gitea = None

# put a ".token" file into your directory containg only the token for gitea
try:
    gitea = Gitea("http://localhost:3000", open(".token", "r").read().strip())
    print("Gitea Version: " + gitea.get_version())
    print("API-Token belongs to user: " + gitea.get_user().username)
except:
    assert (
        False
    ), "Gitea could not load. \
            - Instance running at http://localhost:3000 \
            - Token at .token   \
                ?"


def test_token():
    assert gitea.get_user().username == "test", "Token user not 'test'."


def test_version():
    assert gitea.get_version() == "1.8.0-rc2", "Version changed. Updated?"


def test_before_user():
    # This should not work currently
    assert expect_not_exist(
        lambda: User(gitea, "test-user"), (NotFoundException)
    ), "User test-user should not exist"


def test_before_org():
    assert expect_not_exist(
        lambda: Organization(gitea, "test-org"), (NotFoundException)
    ), "Organization test-org should not exist"


def test_before_repo():
    assert expect_not_exist(
        lambda: Repository(gitea, User(gitea, "test-user"), "test-repo"),
        (NotFoundException),
    ), "Repository test-repo should not exist"


def test_before_team():
    assert expect_not_exist(
        lambda: Team(gitea, Organization(gitea, "test-org"), "test-team"),
        (NotFoundException),
    ), "Team test-team should not exist"


def test_create_user():
    user = gitea.create_user('test-user', 'testmail@example.org', 'pw1234')
    user.update_mail()
    assert user.username == 'test-user'
    assert user.login == 'test-user'
    assert user.email == 'testmail@example.org'
    assert not user.is_admin


def test_create_org():
    user = gitea.get_user()
    org = gitea.create_org(user, 'test-org', 'some-desc', 'loc')
    assert org.get_members() == [user]
    assert org.description == 'some-desc'
    assert org.username == 'test-org'
    assert org.location == 'loc'
    assert not org.website
    assert not org.full_name


def test_create_repo():
    org = Organization(gitea, 'test-org')
    repo = gitea.create_repo(org, 'test-repo', 'descr')
    assert repo.description == 'descr'
    assert repo.owner == org
    assert repo.name == 'test-repo'
    assert not repo.private


def test_create_team():
    org = Organization(gitea, 'test-org')
    team = gitea.create_team(org, 'test-team', 'descr')
    assert team.name == 'test-team'
    assert team.description == 'descr'
    assert team.organization == org

def test_full():
    user = User(gitea, 'test-user')
    user.update_mail()
    org = Organization(gitea, 'test-org')
    team = Team(org, 'test-team')
    assert team.get_members() == []
    team.add(user)
    assert team.get_members() == [user]
    repo = Repository(gitea, org, 'test-repo')
    assert team.get_repos() == []
    team.add(repo)
    assert team.get_repos() == [repo]


def test_delete_repo():
    org = Organization(gitea, 'test-org')
    repo = Repository(gitea, org, 'test-repo')
    repo.delete()
    assert expect_not_exist(
        lambda: Repository(gitea, User(gitea, "test-user"), "test-repo"),
        (NotFoundException),
    ), "Repository test-repo should not exist"

def test_delete_team():
    org = Organization(gitea, 'test-org')
    team = Team(org, 'test-team')
    team.delete()
    assert expect_not_exist(
        lambda: Team(org, "test-team"),
        (NotFoundException),
    ), "Team test-team should not exist"

def test_delete_org():
    org = Organization(gitea, 'test-org')
    org.delete()
    assert expect_not_exist(
        lambda: Organization(gitea, "test-org"), (NotFoundException)
    ), "Organization test-org should not exist"


def test_delete_user():
    user = User(gitea, 'test-user')
    user.delete()
    assert expect_not_exist(
        lambda: User(gitea, "test-user"), (NotFoundException)
    ), "User test-user should not exist"


