import base64

import pytest
import uuid

from gitea import Gitea, User, Organization, Team, Repository, Issue, Milestone
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
    assert org.get_members()[0] == user
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


def test_patch_repo(instance):
    fields = {
        "allow_rebase": False,
        "description": "new description",
        "has_projects": True,
        "private": True,
    }
    org = Organization.request(instance, test_org)
    repo = org.get_repository(test_repo)
    for field, value in fields.items():
        setattr(repo, field, value)
    repo.commit()
    repo = org.get_repository(test_repo)
    for field, value in fields.items():
        assert getattr(repo, field) == value


def test_list_branches(instance):
    org = Organization.request(instance, test_org)
    repo = org.get_repository(test_repo)
    branches = repo.get_branches()
    assert len(branches) > 0
    master = [b for b in branches if b.name == "master"]
    assert len(master) > 0

def test_list_files_and_content(instance):
    org = Organization.request(instance, test_org)
    repo = org.get_repository(test_repo)
    content = repo.get_git_content()
    # Readme file should exist in any new repo
    #  content is the description given during creation
    readmes = [c for c in content if c.name == "README.md"]
    assert len(readmes) > 0
    readme_content = repo.get_file_content(readmes[0])
    assert len(readme_content) > 0
    assert "descr" in str(base64.b64decode(readme_content))

def test_create_file(instance):
    TESTFILE_CONENTE = "TestStringFileContent"
    TESTFILE_CONENTE_B64 = base64.b64encode(bytes(TESTFILE_CONENTE, 'utf-8'))
    org = Organization.request(instance, test_org)
    repo = org.get_repository(test_repo)
    repo.create_file("testfile.md",
        content = TESTFILE_CONENTE_B64.decode("ascii"))
    # test if putting was successful
    content = repo.get_git_content()
    readmes = [c for c in content if c.name == "testfile.md"]
    assert len(readmes) > 0
    readme_content = repo.get_file_content(readmes[0])
    assert len(readme_content) > 0
    assert TESTFILE_CONENTE in str(base64.b64decode(readme_content))

def test_change_file(instance):
    TESTFILE_CONENTE = "TestStringFileContent with changed content now"
    TESTFILE_CONENTE_B64 = base64.b64encode(bytes(TESTFILE_CONENTE, 'utf-8'))
    org = Organization.request(instance, test_org)
    repo = org.get_repository(test_repo)
    #figure out the sha of the file to change
    content = repo.get_git_content()
    readmes = [c for c in content if c.name == "testfile.md"]
    # change
    repo.change_file("testfile.md", readmes[0].sha,
                     content = TESTFILE_CONENTE_B64.decode("ascii"))
    # test if putting was successful
    content = repo.get_git_content()
    readmes = [c for c in content if c.name == "testfile.md"]
    assert len(readmes) > 0
    readme_content = repo.get_file_content(readmes[0])
    assert len(readme_content) > 0
    assert TESTFILE_CONENTE in str(base64.b64decode(readme_content))

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

def test_patch_team(instance):
    fields = {
        "can_create_org_repo": True,
        "description": "patched description",
        "includes_all_repositories": True,
        "name": "newname",
        "permission": "write",
    }
    org = Organization.request(instance, test_org)
    team = instance.create_team(org, test_team[:1], "descr")
    for field, value in fields.items():
        setattr(team, field, value)
    team.commit()
    team = Team.request(instance, team.id)
    for field, value in fields.items():
        assert getattr(team, field) == value


def test_request_team(instance):
    org = Organization.request(instance, test_org)
    team = org.get_team(test_team)
    team2 = Team.request(instance, team.id)
    assert team.name == team2.name

def test_create_milestone(instance):
        org = Organization.request(instance, test_org)
        repo = org.get_repository(test_repo)
        ms = repo.create_milestone("I love this Milestone", "Find an otter to adopt this milestone")
        assert isinstance(ms, Milestone)
        assert ms.title == "I love this Milestone"

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

def test_hashing(instance):
    #just call the hash function of each object to see if something bad happens
    org = Organization.request(instance, test_org)
    team = org.get_team(test_team)
    user = instance.get_user_by_name(test_user)
    #TODO test for milestones (Todo: add milestone adding)
    repo = org.get_repositories()[0]
    milestone = repo.create_milestone("mystone", "this is only a teststone")
    issue = repo.get_issues()[0]
    branch = repo.get_branches()[0]
    commit = repo.get_commits()[0]
    assert len(set([org, team, user, repo, issue, branch, commit, milestone]))


def test_change_issue(instance):
    org = Organization.request(instance, test_org)
    repo = org.get_repositories()[0]
    ms_title = "othermilestone"
    issue = Issue.create_issue(instance, repo, "IssueTestissue with Testinput", "asdf2332")
    new_body = "some new description with some more of that char stuff :)"
    issue.body = new_body
    issue.commit()
    number = issue.number
    del issue
    issue2 = Issue.request(instance, org.username, repo.name, number)
    assert issue2.body == new_body
    milestone = repo.create_milestone(ms_title, "this is only a teststone2")
    issue2.milestone = milestone
    issue2.commit()
    del issue2
    issue3 = Issue.request(instance, org.username, repo.name, number)
    assert issue3.milestone is not None
    assert issue3.milestone.description == "this is only a teststone2"
    issues = repo.get_issues()
    assert len([issue for issue in issues
                if issue.milestone is not None and issue.milestone.title == ms_title]) > 0

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
    for repo in user.get_repositories():
        repo.transfer_ownership(old_org)
        assert repo_name in [repo.name for repo in old_org.get_repositories()]
        assert repo_name not in [repo.name for repo in user.get_repositories()]


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
    user_name = test_user + "delte_test"
    email = user_name + "@example.org"
    user = instance.create_user(user_name, email, "abcdefg1.23AB", send_notify=False)
    assert user.username == user_name
    user.delete()
    with pytest.raises(NotFoundException) as e:
        User.request(instance, user_name)
