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


def test_list_repos(instance):
    user = instance.create_user(test_user, test_user + "@example.org", "abcdefg1.23AB", send_notify=False)
    org = instance.create_org(user, test_org, "some Description for longtests")
    repos = org.get_repositories()
    assert len(repos) == 0
    # test a number of repository listings larger than the pagination number (default 50)
    for i in range(1, 54):
        instance.create_repo(org, test_repo + "_" + str(i), str(i))
    repos = org.get_repositories()
    assert len(repos) >= 53


def test_list_issue(instance):
    org = Organization.request(instance, test_org)
    repo = instance.create_repo(org, test_repo, "Testing a huge number of Issues and how they are listed")
    for x in range(0, 100):
        Issue.create_issue(instance, repo, "TestIssue" + str(x), "We will be too many to be listed on one page")
    issues = repo.get_issues()
    assert len(issues) > 98
