from unittest import TestCase
from utils import suid

from gitea import (
    Gitea,
    Repository,
    MigrationServices,
)


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

    def test_migrate_repo_gitea(self):
        test_repo = f"test_repo_{suid()}"
        repo = Repository.migrate_repo(
            self.g,
            MigrationServices.GITEA,
            "https://gitea.com/gitea/awesome-gitea.git",
            test_repo,
            "user owned repo",
        )
        assert repo.name == test_repo
        assert repo.description == "user owned repo"
        assert not repo.private
        assert repo.owner.username == "test"
        assert "README.md" in [f.name for f in repo.get_git_content()]
        repo = Repository.request(self.g, "test", test_repo)
        repo.delete()

    def test_migrate_repo_github(self):
        test_repo = f"test_repo_{suid()}"
        repo = Repository.migrate_repo(
            self.g,
            MigrationServices.GITHUB,
            "https://github.com/Langenfeld/py-gitea",
            test_repo,
            "cloning py-gitea to test py-gitea",
        )
        assert repo.name == test_repo
        assert repo.description == "cloning py-gitea to test py-gitea"
        assert not repo.private
        assert repo.owner.username == "test"
        assert "README.md" in [f.name for f in repo.get_git_content()]
        repo = Repository.request(self.g, "test", test_repo)
        repo.delete()
