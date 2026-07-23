from typing import Any
from unittest import TestCase

import base64
from utils import suid

from gitea import (
    Gitea,
    Commit,
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
            assert False, "Gitea could not load. \
                    - Instance running at http://localhost:3000 \
                    - Token at .token   \
                        ?"
        self.g = g
        self.user = g.create_user(
            self.test_user_name, f"{self.test_user_name}@example.org", "asdas.passwd", send_notify=False
        )
        self.org = g.create_org(self.user, self.test_org_name, "some-desc", "loc")
        self.repo = g.create_repo(self.org, self.test_repo_name, "user owned repo with a descr")

    def test_list_branches(self):
        repo = self.org.get_repository(self.test_repo_name)
        branches = repo.get_branches()
        assert len(branches) > 0
        master = [b for b in branches if b.name == "master"]
        assert len(master) > 0

    def test_create_branch(self):
        branches = self.repo.get_branches()
        master = [b for b in branches if b.name == "master"]
        assert len(master) > 0
        self.repo.add_branch(master[0], "test_branch")

    def test_get_accessible_repositories(self):
        user = self.g.get_user_by_name(self.test_user_name)
        repos = user.get_accessible_repos()
        assert len(repos) > 0

    def test_list_files_and_content(self):
        content = self.repo.get_git_content()
        # Readme file should exist in any new repo
        #  content is the description given during creation
        readmes = [c for c in content if c.name == "README.md"]
        assert len(readmes) > 0
        readme_content = self.repo.get_file_content(readmes[0])
        assert len(readme_content) > 0
        assert "descr" in str(base64.b64decode(readme_content))

    def test_create_file(self):
        TESTFILE_CONENTE = "TestStringFileContent"
        TESTFILE_CONENTE_B64 = base64.b64encode(bytes(TESTFILE_CONENTE, "utf-8"))
        self.repo.create_file("testfile.md", content=TESTFILE_CONENTE_B64.decode("ascii"))
        # test if putting was successful
        content = self.repo.get_git_content()
        readmes = [c for c in content if c.name == "testfile.md"]
        assert len(readmes) > 0
        readme_content = self.repo.get_file_content(readmes[0])
        assert len(readme_content) > 0
        assert TESTFILE_CONENTE in str(base64.b64decode(readme_content))

    def test_change_file(self):
        TESTFILE_CONENTE = "TestStringFileContent with changed content now"
        TESTFILE_CONENTE_B64 = base64.b64encode(bytes(TESTFILE_CONENTE, "utf-8"))
        self.repo.create_file("testfile2.md", content=TESTFILE_CONENTE_B64.decode("ascii"))
        # figure out the sha of the file to change
        content = self.repo.get_git_content()
        readmes = [c for c in content if c.name == "testfile2.md"]
        # change
        self.repo.change_file("testfile2.md", readmes[0].sha, content=TESTFILE_CONENTE_B64.decode("ascii"))
        # test if putting was successful
        content = self.repo.get_git_content()
        readmes = [c for c in content if c.name == "testfile2.md"]
        assert len(readmes) > 0
        readme_content = self.repo.get_file_content(readmes[0])
        assert len(readme_content) > 0
        assert TESTFILE_CONENTE in str(base64.b64decode(readme_content))

    def test_delete_file(self):
        TESTFILE_CONENTE = "TestStringFileContent2"
        TESTFILE_CONENTE_B64 = base64.b64encode(bytes(TESTFILE_CONENTE, "utf-8"))
        self.repo.create_file("testfile3.md", content=TESTFILE_CONENTE_B64.decode("ascii"))
        # test if putting was successful
        content = self.repo.get_git_content()
        readmes = [c for c in content if c.name == "testfile3.md"]
        assert len(readmes) > 0
        # test if deleting was successful
        self.repo.delete_file("testfile3.md", readmes[0].sha)
        content = self.repo.get_git_content()
        readmes = [c for c in content if c.name == "testfile3.md"]
        assert len(readmes) == 0

    def test_list_commits(self):
        count = 4
        self.__create_random_commit(count)
        # test if putting was successful
        commits = self.repo.get_commits()
        assert len(commits) > count
        head = commits[-1]
        # TODO: add some author tests here
        # assert head.author == self.user
        # assert head.committer == self.user # no, this is gitea!
        # TODO: commit typing is thin, add concete types
        self.__check_fields(Commit, head)

    def __create_random_commit(self, count: int):
        TESTFILE_CONENTE = f"TestStringFileContent with some content, will add {count} commits"
        TESTFILE_CONENTE_B64 = base64.b64encode(bytes(TESTFILE_CONENTE, "utf-8"))
        self.repo.create_file(f"randomcommits.md", content=TESTFILE_CONENTE_B64.decode("ascii"))
        for x in range(count):
            content = self.repo.get_git_content()
            readmes = [c for c in content if c.name == "randomcommits.md"]
            # change
            TESTFILE_CONENTE = TESTFILE_CONENTE + f"\nThis is change number {x}"
            TESTFILE_CONENTE_B64 = base64.b64encode(bytes(TESTFILE_CONENTE, "utf-8"))
            self.repo.change_file("randomcommits.md", readmes[0].sha, content=TESTFILE_CONENTE_B64.decode("ascii"))

    def __check_fields(self, cls, object):
        """Check if all the fields listed in the object were in deed added to the object.
        If Gitea returned more than None as a content, also check if the content type is right.
        Note: this is a copy from field population tests, but don't what to have the git stuff there"""
        for field, t in cls.__annotations__.items():
            # There should be a field in the object
            self.assertTrue(hasattr(object, field), f"Field {field} in {object} should have been accessible.")
            if t is Any:
                # don't care further if there is no useful type given
                continue
            if isinstance(t, type) and (v := getattr(object, field)):
                if v is None:
                    # don't care further if Gitea did not provide a value for the field (but the field is there, yey)
                    continue
                # Check if the field has the correct type _if_ a value was given that is not None
                self.assertIsInstance(
                    v, t, f"Field {field} in {object} has a value of wrong type assigned ({type(v)})."
                )
