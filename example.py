import os

from gitea.gitea import *


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
    assert user.username == 'test-user'
    assert user.login == 'test-user'
    assert user.email == 'testmail@example.org'
    assert not user.is_admin


def test_create_org():
    org = gitea.create_org(gitea.get_user(), 'test-org', 'some-desc', 'loc')
    assert org.description == 'some-desc'
    assert org.username == 'test-org'
    assert org.location == 'loc'
    assert not org.website
    assert not org.full_name


def test_create_repo():
    pass


def test_create_team():
    pass


#
# print(org.username)
# org.set_value({"location": "a-place"})
# print([user.username for user in org.get_members()])
# ## try getting an organization that does not exists
# try:
#     org = Organization(gitea, "non-existent-org")
# except:
#     pass
#
# ##get a User that does exist
# user = User(gitea, "a-user")
# print(user.username)
# ##try getting organization that does not exist
# try:
#     user = User(gitea, "non-existent-user")
# except:
#     pass
# user.set_value(user.email, {"location": "an-location"})
# ##get repositories set under a organization
# repos = org.get_repositories()
# print("org " + org.username + " has repositories " + str(repos))
# ##get repositories of a user
# userRepos = user.get_repositories()
# print("user " + user.username + " has repositories " + str(repos))
# ##get branches
# repo = Repository(gitea, org,"playground")
# print([b.name for b in repo.get_branches()])
#
# ##create Repository
# gitea.create_repo(user , "test-repo-api", "this is an api test repo, delete this", True, True)
# gitea.create_repo(org , "test-repo-api-org", "this is an api test repo, delete this", True, True)
#
# ## create user
# newUser = gitea.create_user("test-test", "test@testing.de","Torben der Tester", str(os.urandom(32)), False)
# print(newUser.username)
# newUser.delete()
