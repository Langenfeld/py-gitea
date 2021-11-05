import pytest
import uuid

from gitea import Gitea, User, Organization, Team, Repository, Issue
from gitea import NotFoundException, AlreadyExistsException

# put a ".token" file into your directory containg only the token for gitea
@pytest.fixture
def instance(scope="module"):
    try:
        g = Gitea("http://localhost:3000", open(".token", "r").read().strip())
        print("Gitea Version: " + g.get_version())
        print("API-Token belongs to user: " + g.get_user().username)
        return g
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


def test_token_owner(instance):
    user = instance.get_user()
    assert user.username == "test", "Token user not 'tests'."
    assert user.is_admin, "Testuser is not Admin - Tests may fail"


def test_gitea_version(instance):
    assert instance.get_version().startswith("1."), "No Version String returned"


def test_fail_get_non_existent_user(instance):
    with pytest.raises(NotFoundException) as e:
        User.request(instance, test_user)


def test_fail_get_non_existent_org(instance):
    with pytest.raises(NotFoundException) as e:
        Organization.request(instance, test_org)


def test_fail_get_non_existent_repo(instance):
    with pytest.raises(NotFoundException) as e:
        Repository.request(instance, test_user, test_repo)


def test_create_user(instance):
    email = test_user + "@example.org"
    user = instance.create_user(test_user, email, "abcdefg1.23AB", send_notify=False)
    assert user.username == test_user
    assert user.login == test_user
    assert email in user.emails
    assert user.email == email
    assert not user.is_admin
    assert type(user.id) is int
    assert user.is_admin is False

def test_change_user(instance):
    user = instance.get_user_by_name(test_user)
    location = "a house"
    user.location = location
    new_fullname = "Other Test Full Name"
    user.full_name = new_fullname
    user.commit(user.username, 0)
    del(user)
    user = instance.get_user_by_name(test_user)
    assert user.full_name == new_fullname
    assert user.location == location


def test_create_org(instance):
    user = instance.get_user()
    org = instance.create_org(user, test_org, "some-desc", "loc")
    assert org.get_members() == [user]
    assert org.description == "some-desc"
    assert org.username == test_org
    assert org.location == "loc"
    assert not org.website
    assert not org.full_name


def test_non_changable_field(instance):
    org = Organization.request(instance, test_org)
    with pytest.raises(AttributeError) as e:
        org.id = 55


def test_create_repo_userowned(instance):
    org = User.request(instance, test_user)
    repo = instance.create_repo(org, test_repo, "user owned repo")
    assert repo.description == "user owned repo"
    assert repo.owner == org
    assert repo.name == test_repo
    assert not repo.private


def test_edit_org_fields_and_commit(instance):
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


def test_create_repo_orgowned(instance):
    org = Organization.request(instance, test_org)
    repo = instance.create_repo(org, test_repo, "descr")
    assert repo.description == "descr"
    assert repo.owner == org
    assert repo.name == test_repo
    assert not repo.private

def test_list_branches(instance):
    org = Organization.request(instance, test_org)
    repo = org.get_repository(test_repo)
    branches = repo.get_branches()
    assert len(branches) > 0
    master = [b for b in branches if b.name == "master"]
    assert len(master) > 0

def test_create_branch(instance):
    org = Organization.request(instance, test_org)
    repo = org.get_repository(test_repo)
    branches = repo.get_branches()
    master = [b for b in branches if b.name == "master"]
    assert len(master) > 0
    repo.add_branch(master[0], "test_branch")

def test_create_team(instance):
    org = Organization.request(instance, test_org)
    team = instance.create_team(org, test_team, "descr")
    assert team.name == test_team
    assert team.description == "descr"
    assert team.organization == org

def test_user_teams(instance):
    org = Organization.request(instance, test_org)
    team = org.get_team(test_team)
    user = instance.get_user_by_name(test_user)
    team.add_user(user)
    teams = user.get_teams()
    assert team in teams

def test_get_accessible_repositories(instance):
    user = instance.get_user_by_name(test_user)
    repos = user.get_accessible_repos()
    assert len(repos) > 0

def test_create_issue(instance):
    org = Organization.request(instance, test_org)
    repo = Repository.request(instance, org.username, test_repo)
    issue = Issue.create_issue(instance, repo, "TestIssue", "Body text with this issue")
    assert issue.state == Issue.OPENED
    assert issue.title == "TestIssue"
    assert issue.body == "Body text with this issue"

def test_team_get_org(instance):
    org = Organization.request(instance, test_org)
    user = instance.get_user_by_name(test_user)
    teams = user.get_teams()
    assert org.username == teams[0].organization.name

def test_delete_repo_userowned(instance):
    user = User.request(instance, test_user)
    repo = Repository.request(instance, user.username, test_repo)
    repo.delete()
    with pytest.raises(NotFoundException) as e:
        Repository.request(instance, test_user, test_repo)

def test_secundary_email(instance):
    SECONDARYMAIL = "secondarytest@test.org"  # set up with real email
    sec_user = instance.get_user_by_email(SECONDARYMAIL)
    assert SECONDARYMAIL in sec_user.emails
    assert sec_user.username == "test"


def test_delete_repo_orgowned(instance):
    org = Organization.request(instance, test_org)
    repo = Repository.request(instance, org.username, test_repo)
    repo.delete()
    with pytest.raises(NotFoundException) as e:
        Repository.request(instance, test_user, test_repo)


def test_change_repo_ownership_org(instance):
    old_org = Organization.request(instance, test_org)
    user = User.request(instance, test_user)
    new_org = instance.create_org(user,test_org+"_repomove", "Org for testing moving repositories")
    new_team = instance.create_team(new_org, test_team + "_repomove", "descr")
    repo_name = test_repo+"_repomove"
    repo = instance.create_repo(old_org, repo_name , "descr")
    repo.transfer_ownership(new_org, set([new_team]))
    assert repo_name not in [repo.name for repo in old_org.get_repositories()]
    assert repo_name in [repo.name for repo in new_org.get_repositories()]

def test_change_repo_ownership_user(instance):
    old_org = Organization.request(instance, test_org)
    user = User.request(instance, test_user)
    repo_name = test_repo+"_repomove"
    repo = instance.create_repo(old_org, repo_name, "descr")
    repo.transfer_ownership(user)
    assert repo_name not in [repo.name for repo in old_org.get_repositories()]
    assert repo_name in [repo.name for repo in user.get_repositories()]


def test_delete_team(instance):
    org = Organization.request(instance, test_org)
    team = org.get_team(test_team)
    team.delete()
    with pytest.raises(NotFoundException) as e:
        team = org.get_team(test_team)

def test_delete_teams(instance):
    org = Organization.request(instance, test_org)
    repos = org.get_repositories()
    for repo in repos:
        repo.delete()
    repos = org.get_repositories()
    assert len(repos) == 0

def test_delete_org(instance):
    org = Organization.request(instance, test_org)
    org.delete()
    with pytest.raises(NotFoundException) as e:
        Organization.request(instance, test_org)


def test_delete_user(instance):
    user = User.request(instance, test_user)
    user.delete()
    with pytest.raises(NotFoundException) as e:
        User.request(instance, test_user)
