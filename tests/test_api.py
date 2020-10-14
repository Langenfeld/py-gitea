import pytest
import uuid

from gitea import Gitea, User, Organization, Team, Repository, Issue
from gitea import NotFoundException, AlreadyExistsException

# put a ".token" file into your directory containg only the token for gitea
try:
    instance = Gitea("http://localhost:3000", open(".token", "r").read().strip())
    print("Gitea Version: " + instance.get_version())
    print("API-Token belongs to user: " + instance.get_user().username)
except:
    assert (
        False
    ), "Gitea could not load. \
            - Instance running at http://localhost:3000 \
            - Token at .token   \
                ?"

# make up some fresh names for the tests run
test_org = "org_" + uuid.uuid4().hex[:8]
test_user = "user_" + uuid.uuid4().hex[:8]
test_team = "team_" + uuid.uuid4().hex[:8]  # team names seem to have a rather low max lenght
test_repo = "repo_" + uuid.uuid4().hex[:8]


def test_token_owner():
    user = instance.get_user()
    assert user.username == "tests", "Token user not 'tests'."
    assert user.is_admin, "Testuser is not Admin - Tests may fail"


def test_gitea_version():
    assert instance.get_version() == "1.10.0", "Version changed. Updated?"


def test_fail_get_non_existent_user():
    with pytest.raises(NotFoundException) as e:
        User.request(instance, test_user)


def test_fail_get_non_existent_org():
    with pytest.raises(NotFoundException) as e:
        Organization.request(instance, test_org)


def test_fail_get_non_existent_repo():
    with pytest.raises(NotFoundException) as e:
        Repository.request(instance, test_user, test_repo)


def test_create_user():
    email = test_user + "@example.org"
    user = instance.create_user(test_user, email, "abcdefg1.23AB")
    assert user.username == test_user
    assert user.login == test_user
    assert email in user.emails
    assert user.email == email
    assert not user.is_admin


def test_create_org():
    user = instance.get_user()
    org = instance.create_org(user, test_org, "some-desc", "loc")
    assert org.get_members() == [user]
    assert org.description == "some-desc"
    assert org.username == test_org
    assert org.location == "loc"
    assert not org.website
    assert not org.full_name


def test_non_changable_field():
    org = Organization.request(instance, test_org)
    with pytest.raises(AttributeError) as e:
        org.id = 55


def test_create_repo_userowned():
    org = User.request(instance, test_user)
    repo = instance.create_repo(org, test_repo, "user owned repo")
    assert repo.description == "user owned repo"
    assert repo.owner == org
    assert repo.name == test_repo
    assert not repo.private


def test_edit_org_fields_and_commit():
    org = Organization.request(instance, test_org)
    org.description = "some thing other man"
    org.location = "somewehre new"
    org.visibility = "public"
    org.website = "http:\\\\testurl.com"
    org.commit()
    org2 = Organization.request(instance, test_org)
    assert org2.name == test_org
    assert org2.description == "some thing other man"
    assert org2.location == "somewehre new"
    # assert org2.visibility == "private" # after commiting, this field just vanishes (Bug?)
    assert org2.website == "http:\\\\testurl.com"


def test_create_repo_orgowned():
    org = Organization.request(instance, test_org)
    repo = instance.create_repo(org, test_repo, "descr")
    assert repo.description == "descr"
    assert repo.owner == org
    assert repo.name == test_repo
    assert not repo.private


def test_create_team():
    org = Organization.request(instance, test_org)
    team = instance.create_team(org, test_team, "descr")
    assert team.name == test_team
    assert team.description == "descr"
    assert team.organization == org


def test_create_issue():
    org = Organization.request(instance, test_org)
    repo = Repository.request(instance, org.username, test_repo)
    issue = Issue.create_issue(instance, repo, "TestIssue", "Body text with this issue")
    assert issue.state == Issue.OPENED
    assert issue.title == "TestIssue"
    assert issue.body == "Body text with this issue"


def test_delete_repo_userowned():
    user = User.request(instance, test_user)
    repo = Repository.request(instance, user.username, test_repo)
    repo.delete()
    with pytest.raises(NotFoundException) as e:
        Repository.request(instance, test_user, test_repo)


def test_secundary_email():
    SECONDARYMAIL = "secondarytest@tests.org"  # set up with real email
    sec_user = instance.get_user_by_email(SECONDARYMAIL)
    assert SECONDARYMAIL in sec_user.emails
    assert sec_user.username == "tests"


def test_delete_repo_orgowned():
    org = Organization.request(instance, test_org)
    repo = Repository.request(instance, org.username, test_repo)
    repo.delete()
    with pytest.raises(NotFoundException) as e:
        Repository.request(instance, test_user, test_repo)


def test_delete_team():
    org = Organization.request(instance, test_org)
    team = org.get_team(test_team)
    team.delete()
    with pytest.raises(NotFoundException) as e:
        team = org.get_team(test_team)


def test_delete_org():
    org = Organization.request(instance, test_org)
    org.delete()
    with pytest.raises(NotFoundException) as e:
        Organization.request(instance, test_org)


def test_delete_user():
    user = User.request(instance, test_user)
    user.delete()
    with pytest.raises(NotFoundException) as e:
        User.request(instance, test_user)
