from unittest import TestCase
import uuid

from gitea import (
    Gitea,
    User,
    Organization,
    Team,
    Repository,
    Issue,
    Milestone,
    MigrationServices,
)
from gitea import NotFoundException, AlreadyExistsException


class PublicApiTest(TestCase):
    def setUp(self):
        self.test_org = "org_public_" + uuid.uuid4().hex[:8]
        self.test_user = "user_" + uuid.uuid4().hex[:8]
        self.test_team = (
            "team_" + uuid.uuid4().hex[:8]
        )  # team names seem to have a rather low max lenght
        self.test_repo = "repo_" + uuid.uuid4().hex[:8]
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
        self.org = g.create_org(self.user, self.test_org, "some-desc", "loc")
        self.repo = self.g.create_repo(self.org, self.test_repo, "user owned repo")
        self.pinstance = Gitea("http://localhost:3000")

    def test_list_public_org_list(self):
        p_orgs = self.pinstance.get_orgs()
        assert self.test_org in [o.name for o in p_orgs]

    def test_list_public_org(self):
        owner = Organization.request(self.pinstance, self.test_org)
        assert self.test_org == owner.name
        repos = owner.get_repositories()
        assert self.test_repo in [r.name for r in repos]
