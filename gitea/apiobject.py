import logging
from datetime import datetime
from typing import List, Tuple, Dict, Sequence, Optional, Union, Set

from .baseapiobject import ReadonlyApiObject, ApiObject
from .exceptions import *


class Organization(ApiObject):
    """see https://try.gitea.io/api/swagger#/organization/orgGetAll"""

    API_OBJECT = """/orgs/{name}"""  # <org>
    ORG_REPOS_REQUEST = """/orgs/%s/repos"""  # <org>
    ORG_TEAMS_REQUEST = """/orgs/%s/teams"""  # <org>
    ORG_TEAMS_CREATE = """/orgs/%s/teams"""  # <org>
    ORG_GET_MEMBERS = """/orgs/%s/members"""  # <org>
    ORG_IS_MEMBER = """/orgs/%s/members/%s"""  # <org>, <username>
    ORG_HEATMAP = """/users/%s/heatmap"""  # <username>

    def __init__(self, gitea):
        super().__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Organization):
            return False
        return self.gitea == other.gitea and self.name == other.name

    def __hash__(self):
        return hash(self.gitea) ^ hash(self.name)

    @classmethod
    def request(cls, gitea: "Gitea", name: str) -> "Organization":
        return cls._request(gitea, {"name": name})

    @classmethod
    def parse_response(cls, gitea, result) -> "Organization":
        api_object = super().parse_response(gitea, result)
        # add "name" field to make this behave similar to users for gitea < 1.18
        # also necessary for repository-owner when org is repo owner
        if not hasattr(api_object, "name"):
            Organization._add_read_property("name", result["username"], api_object)
        return api_object

    _patchable_fields = {
        "description",
        "full_name",
        "location",
        "visibility",
        "website",
    }

    def commit(self):
        values = self.get_dirty_fields()
        args = {"name": self.name}
        self.gitea.requests_patch(Organization.API_OBJECT.format(**args), data=values)
        self.dirty_fields = {}

    def create_repo(
        self,
        repoName: str,
        description: str = "",
        private: bool = False,
        autoInit=True,
        gitignores: str = None,
        license: str = None,
        readme: str = "Default",
        issue_labels: str = None,
        default_branch="master",
    ):
        """Create an organization Repository

        Throws:
            AlreadyExistsException: If the Repository exists already.
            Exception: If something else went wrong.
        """
        result = self.gitea.requests_post(
            f"/orgs/{self.name}/repos",
            data={
                "name": repoName,
                "description": description,
                "private": private,
                "auto_init": autoInit,
                "gitignores": gitignores,
                "license": license,
                "issue_labels": issue_labels,
                "readme": readme,
                "default_branch": default_branch,
            },
        )
        if "id" in result:
            self.gitea.logger.info(
                "Successfully created Repository %s " % result["name"]
            )
        else:
            self.gitea.logger.error(result["message"])
            raise Exception("Repository not created... (gitea: %s)" % result["message"])
        return Repository.parse_response(self, result)

    def get_repositories(self) -> List["Repository"]:
        results = self.gitea.requests_get_paginated(
            Organization.ORG_REPOS_REQUEST % self.username
        )
        return [Repository.parse_response(self.gitea, result) for result in results]

    def get_repository(self, name) -> "Repository":
        repos = self.get_repositories()
        for repo in repos:
            if repo.name == name:
                return repo
        raise NotFoundException("Repository %s not existent in organization." % name)

    def get_teams(self) -> List["Team"]:
        results = self.gitea.requests_get(
            Organization.ORG_TEAMS_REQUEST % self.username
        )
        teams = [Team.parse_response(self.gitea, result) for result in results]
        # organisation seems to be missing using this request, so we add org manually
        for t in teams:
            setattr(t, "_organization", self)
        return teams

    def get_team(self, name) -> "Team":
        teams = self.get_teams()
        for team in teams:
            if team.name == name:
                return team
        raise NotFoundException("Team not existent in organization.")

    def get_members(self) -> List["User"]:
        results = self.gitea.requests_get(Organization.ORG_GET_MEMBERS % self.username)
        return [User.parse_response(self.gitea, result) for result in results]

    def is_member(self, username) -> bool:
        if isinstance(username, User):
            username = username.username
        try:
            # returns 204 if its ok, 404 if its not
            self.gitea.requests_get(
                Organization.ORG_IS_MEMBER % (self.username, username)
            )
            return True
        except:
            return False

    def remove_member(self, user: "User"):
        path = f"/orgs/{self.username}/members/{user.username}"
        self.gitea.requests_delete(path)

    def delete(self):
        """Delete this Organization. Invalidates this Objects data. Also deletes all Repositories owned by the User"""
        for repo in self.get_repositories():
            repo.delete()
        self.gitea.requests_delete(Organization.API_OBJECT.format(name=self.username))
        self.deleted = True

    def get_heatmap(self) -> List[Tuple[datetime, int]]:
        results = self.gitea.requests_get(User.USER_HEATMAP % self.username)
        results = [
            (datetime.fromtimestamp(result["timestamp"]), result["contributions"])
            for result in results
        ]
        return results


class User(ApiObject):
    API_OBJECT = """/users/{name}"""  # <org>
    USER_MAIL = """/user/emails?sudo=%s"""  # <name>
    USER_PATCH = """/admin/users/%s"""  # <username>
    ADMIN_DELETE_USER = """/admin/users/%s"""  # <username>
    ADMIN_EDIT_USER = """/admin/users/{username}"""  # <username>
    USER_HEATMAP = """/users/%s/heatmap"""  # <username>

    def __init__(self, gitea):
        super().__init__(gitea)
        self._emails = []

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.gitea == other.gitea and self.id == other.id

    def __hash__(self):
        return hash(self.gitea) ^ hash(self.id)

    @property
    def emails(self):
        self.__request_emails()
        return self._emails

    @classmethod
    def request(cls, gitea: "Gitea", name: str) -> "User":
        api_object = cls._request(gitea, {"name": name})
        return api_object

    _patchable_fields = {
        "active",
        "admin",
        "allow_create_organization",
        "allow_git_hook",
        "allow_import_local",
        "email",
        "full_name",
        "location",
        "login_name",
        "max_repo_creation",
        "must_change_password",
        "password",
        "prohibit_login",
        "website",
    }

    def commit(self, login_name: str, source_id: int = 0):
        """
        Unfortunately it is necessary to require the login name
        as well as the login source (that is not supplied when getting a user) for
        changing a user.
        Usually source_id is 0 and the login_name is equal to the username.
        """
        values = self.get_dirty_fields()
        values.update(
            # api-doc says that the "source_id" is necessary; works without though
            {"login_name": login_name, "source_id": source_id}
        )
        args = {"username": self.username}
        self.gitea.requests_patch(User.ADMIN_EDIT_USER.format(**args), data=values)
        self.dirty_fields = {}

    def create_repo(
        self,
        repoName: str,
        description: str = "",
        private: bool = False,
        autoInit=True,
        gitignores: str = None,
        license: str = None,
        readme: str = "Default",
        issue_labels: str = None,
        default_branch="master",
    ):
        """Create a user Repository

        Throws:
            AlreadyExistsException: If the Repository exists already.
            Exception: If something else went wrong.
        """
        result = self.gitea.requests_post(
            "/user/repos",
            data={
                "name": repoName,
                "description": description,
                "private": private,
                "auto_init": autoInit,
                "gitignores": gitignores,
                "license": license,
                "issue_labels": issue_labels,
                "readme": readme,
                "default_branch": default_branch,
            },
        )
        if "id" in result:
            self.gitea.logger.info(
                "Successfully created Repository %s " % result["name"]
            )
        else:
            self.gitea.logger.error(result["message"])
            raise Exception("Repository not created... (gitea: %s)" % result["message"])
        return Repository.parse_response(self, result)

    def get_repositories(self) -> List["Repository"]:
        """Get all Repositories owned by this User."""
        url = f"/users/{self.username}/repos"
        results = self.gitea.requests_get_paginated(url)
        return [Repository.parse_response(self.gitea, result) for result in results]

    def get_orgs(self) -> List[Organization]:
        """Get all Organizations this user is a member of."""
        url = f"/users/{self.username}/orgs"
        results = self.gitea.requests_get_paginated(url)
        return [Organization.parse_response(self.gitea, result) for result in results]

    def get_teams(self) -> List["Team"]:
        url = f"/user/teams"
        results = self.gitea.requests_get_paginated(url, sudo=self)
        return [Team.parse_response(self.gitea, result) for result in results]

    def get_accessible_repos(self) -> List["Repository"]:
        """Get all Repositories accessible by the logged in User."""
        results = self.gitea.requests_get("/user/repos", sudo=self)
        return [Repository.parse_response(self, result) for result in results]

    def __request_emails(self):
        result = self.gitea.requests_get(User.USER_MAIL % self.login)
        # report if the adress changed by this
        for mail in result:
            self._emails.append(mail["email"])
            if mail["primary"]:
                self._email = mail["email"]

    def delete(self):
        """Deletes this User. Also deletes all Repositories he owns."""
        self.gitea.requests_delete(User.ADMIN_DELETE_USER % self.username)
        self.deleted = True

    def get_heatmap(self) -> List[Tuple[datetime, int]]:
        results = self.gitea.requests_get(User.USER_HEATMAP % self.username)
        results = [
            (datetime.fromtimestamp(result["timestamp"]), result["contributions"])
            for result in results
        ]
        return results


class Branch(ReadonlyApiObject):
    def __init__(self, gitea):
        super().__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Branch):
            return False
        return self.commit == other.commit and self.name == other.name

    def __hash__(self):
        return hash(self.commit["id"]) ^ hash(self.name)

    _fields_to_parsers = {
        # This is not a commit object
        # "commit": lambda gitea, c: Commit.parse_response(gitea, c)
    }

    @classmethod
    def request(cls, gitea: "Gitea", owner: str, repo: str, ref: str):
        return cls._request(gitea, {"owner": owner, "repo": repo, "ref": ref})


class Repository(ApiObject):
    API_OBJECT = """/repos/{owner}/{name}"""  # <owner>, <reponame>
    REPO_MIGRATE = """/repos/migrate"""
    REPO_IS_COLLABORATOR = (
        """/repos/%s/%s/collaborators/%s"""  # <owner>, <reponame>, <username>
    )
    REPO_SEARCH = """/repos/search/%s"""  # <reponame>
    REPO_BRANCHES = """/repos/%s/%s/branches"""  # <owner>, <reponame>
    REPO_ISSUES = """/repos/{owner}/{repo}/issues"""  # <owner, reponame>
    REPO_DELETE = """/repos/%s/%s"""  # <owner>, <reponame>
    REPO_TIMES = """/repos/%s/%s/times"""  # <owner>, <reponame>
    REPO_USER_TIME = """/repos/%s/%s/times/%s"""  # <owner>, <reponame>, <username>
    REPO_COMMITS = "/repos/%s/%s/commits"  # <owner>, <reponame>
    REPO_TRANSFER = "/repos/{owner}/{repo}/transfer"
    REPO_MILESTONES = """/repos/{owner}/{repo}/milestones"""

    def __init__(self, gitea):
        super().__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Repository):
            return False
        return self.owner == other.owner and self.name == other.name

    def __hash__(self):
        return hash(self.owner) ^ hash(self.name)

    _fields_to_parsers = {
        # dont know how to tell apart user and org as owner except form email being empty.
        "owner": lambda gitea, r: Organization.parse_response(gitea, r)
        if r["email"] == ""
        else User.parse_response(gitea, r),
        "updated_at": lambda gitea, t: Util.convert_time(t),
    }

    @classmethod
    def request(cls, gitea: "Gitea", owner: str, name: str):
        return cls._request(gitea, {"owner": owner, "name": name})

    _patchable_fields = {
        "allow_manual_merge",
        "allow_merge_commits",
        "allow_rebase",
        "allow_rebase_explicit",
        "allow_rebase_update",
        "allow_squash_merge",
        "archived",
        "autodetect_manual_merge",
        "default_branch",
        "default_delete_branch_after_merge",
        "default_merge_style",
        "description",
        "enable_prune",
        "external_tracker",
        "external_wiki",
        "has_issues",
        "has_projects",
        "has_pull_requests",
        "has_wiki",
        "ignore_whitespace_conflicts",
        "internal_tracker",
        "mirror_interval",
        "name",
        "private",
        "template",
        "website",
    }

    def commit(self):
        values = self.get_dirty_fields()
        args = {"owner": self.owner.username, "name": self.name}
        self.gitea.requests_patch(self.API_OBJECT.format(**args), data=values)
        self.dirty_fields = {}

    def get_branches(self) -> List["Branch"]:
        """Get all the Branches of this Repository."""
        results = self.gitea.requests_get(
            Repository.REPO_BRANCHES % (self.owner.username, self.name)
        )
        return [Branch.parse_response(self.gitea, result) for result in results]

    def add_branch(self, create_from: Branch, newname: str) -> "Branch":
        """Add a branch to the repository"""
        # Note: will only work with gitea 1.13 or higher!
        data = {"new_branch_name": newname, "old_branch_name": create_from.name}
        result = self.gitea.requests_post(
            Repository.REPO_BRANCHES % (self.owner.username, self.name), data=data
        )
        return Branch.parse_response(self.gitea, result)

    def get_issues(self) -> List["Issue"]:
        """Get all Issues of this Repository (open and closed)"""
        return self.get_issues_state(Issue.OPENED) + self.get_issues_state(Issue.CLOSED)

    def get_commits(self, page_limit: int = 0) -> List["Commit"]:
        """Get all the Commits of this Repository."""
        try:
            results = self.gitea.requests_get_paginated(
                Repository.REPO_COMMITS % (self.owner.username, self.name),
                page_limit= page_limit
            )
        except ConflictException as err:
            logging.warning(err)
            logging.warning(
                "Repository %s/%s is Empty" % (self.owner.username, self.name)
            )
            results = []
        return [Commit.parse_response(self.gitea, result) for result in results]

    def get_issues_state(self, state) -> List["Issue"]:
        """Get issues of state Issue.open or Issue.closed of a repository."""
        assert state in [Issue.OPENED, Issue.CLOSED]
        issues = []
        data = {"state": state}
        results = self.gitea.requests_get_paginated(
            Repository.REPO_ISSUES.format(owner=self.owner.username, repo=self.name),
            params=data,
        )
        for result in results:
            issue = Issue.parse_response(self.gitea, result)
            # adding data not contained in the issue answer
            Issue._add_read_property("repo", self, issue)
            Issue._add_read_property("owner", self.owner, issue)
            issues.append(issue)
        return issues

    def get_times(self):
        results = self.gitea.requests_get(
            Repository.REPO_TIMES % (self.owner.username, self.name)
        )
        return results

    def get_user_time(self, username) -> float:
        if isinstance(username, User):
            username = username.username
        results = self.gitea.requests_get(
            Repository.REPO_USER_TIME % (self.owner.username, self.name, username)
        )
        time = sum(r["time"] for r in results)
        return time

    def get_full_name(self) -> str:
        return self.owner.username + "/" + self.name

    def create_issue(self, title, assignees=frozenset(), description="") -> ApiObject:
        data = {
            "assignees": assignees,
            "body": description,
            "closed": False,
            "title": title,
        }
        result = self.gitea.requests_post(
            Repository.REPO_ISSUES.format(owner=self.owner.username, repo=self.name),
            data=data,
        )
        return Issue.parse_response(self.gitea, result)

    def create_milestone(
        self, title: str, description: str, due_date: str = None, state: str = "open"
    ) -> "Milestone":
        url = Repository.REPO_MILESTONES.format(
            owner=self.owner.username, repo=self.name
        )
        data = {"title": title, "description": description, "state": state}
        if due_date:
            data["due_date"] = due_date
        result = self.gitea.requests_post(url, data=data)
        return Milestone.parse_response(self.gitea, result)

    def create_gitea_hook(self, hook_url: str, events: List[str]):
        url = f"/repos/{self.owner.username}/{self.name}/hooks"
        data = {
            "type": "gitea",
            "config": {"content_type": "json", "url": hook_url},
            "events": events,
            "active": True,
        }
        return self.gitea.requests_post(url, data=data)

    def list_hooks(self):
        url = f"/repos/{self.owner.username}/{self.name}/hooks"
        return self.gitea.requests_get(url)

    def delete_hook(self, id: str):
        url = f"/repos/{self.owner.username}/{self.name}/hooks/{id}"
        self.gitea.requests_delete(url)

    def is_collaborator(self, username) -> bool:
        if isinstance(username, User):
            username = username.username
        try:
            # returns 204 if its ok, 404 if its not
            self.gitea.requests_get(
                Repository.REPO_IS_COLLABORATOR
                % (self.owner.username, self.name, username)
            )
            return True
        except:
            return False

    def get_users_with_access(self) -> Sequence[User]:
        url = f"/repos/{self.owner.username}/{self.name}/collaborators"
        response = self.gitea.requests_get(url)
        collabs = [User.parse_response(self.gitea, user) for user in response]
        if isinstance(self.owner, User):
            return collabs + [self.owner]
        else:
            # owner must be org
            teams = self.owner.get_teams()
            for team in teams:
                team_repos = team.get_repos()
                if self.name in [n.name for n in team_repos]:
                    collabs += team.get_members()
            return collabs

    def remove_collaborator(self, user_name: str):
        url = f"/repos/{self.owner.username}/{self.name}/collaborators/{user_name}"
        self.gitea.requests_delete(url)

    def transfer_ownership(
        self,
        new_owner: Union["User", "Organization"],
        new_teams: Set["Team"] = frozenset(),
    ):
        url = Repository.REPO_TRANSFER.format(owner=self.owner.username, repo=self.name)
        data = {"new_owner": new_owner.username}
        if isinstance(new_owner, Organization):
            new_team_ids = [
                team.id for team in new_teams if team in new_owner.get_teams()
            ]
            data["team_ids"] = new_team_ids
        self.gitea.requests_post(url, data=data)
        # TODO: make sure this instance is either updated or discarded

    def get_git_content(self, commit: "Commit" = None) -> List["Content"]:
        """https://try.gitea.io/api/swagger#/repository/repoGetContentsList"""
        url = f"/repos/{self.owner.username}/{self.name}/contents"
        data = {"ref": commit.sha} if commit else {}
        result = [
            Content.parse_response(self.gitea, f)
            for f in self.gitea.requests_get(url, data)
        ]
        return result

    def get_file_content(
        self, content: "Content", commit: "Commit" = None
    ) -> Union[str, List["Content"]]:
        """https://try.gitea.io/api/swagger#/repository/repoGetContents"""
        url = f"/repos/{self.owner.username}/{self.name}/contents/{content.path}"
        data = {"ref": commit.sha} if commit else {}
        if content.type == Content.FILE:
            return self.gitea.requests_get(url, data)["content"]
        else:
            return [
                Content.parse_response(self.gitea, f)
                for f in self.gitea.requests_get(url, data)
            ]

    def create_file(self, file_path: str, content: str, data: dict = None):
        """https://try.gitea.io/api/swagger#/repository/repoCreateFile"""
        if not data:
            data = {}
        url = f"/repos/{self.owner.username}/{self.name}/contents/{file_path}"
        data.update({"content": content})
        return self.gitea.requests_post(url, data)

    def change_file(
        self, file_path: str, file_sha: str, content: str, data: dict = None
    ):
        """https://try.gitea.io/api/swagger#/repository/repoCreateFile"""
        if not data:
            data = {}
        url = f"/repos/{self.owner.username}/{self.name}/contents/{file_path}"
        data.update({"sha": file_sha, "content": content})
        return self.gitea.requests_put(url, data)

    def delete(self):
        self.gitea.requests_delete(
            Repository.REPO_DELETE % (self.owner.username, self.name)
        )
        self.deleted = True

    @classmethod
    def migrate_repo(
        cls,
        gitea: "Gitea",
        service: str,
        clone_addr: str,
        repo_name: str,
        description: str = "",
        private: bool = False,
        auth_token: str = None,
        auth_username: str = None,
        auth_password: str = None,
        mirror: bool = False,
        mirror_interval: str = None,
        lfs: bool = False,
        lfs_endpoint: str = "",
        wiki: bool = False,
        labels: bool = False,
        issues: bool = False,
        pull_requests: bool = False,
        releases: bool = False,
        milestones: bool = False,
        repo_owner: str = None,
    ):
        """Migrate a Repository from another service.

        Throws:
            AlreadyExistsException: If the Repository exists already.
            Exception: If something else went wrong.
        """
        result = gitea.requests_post(
            cls.REPO_MIGRATE,
            data={
                "auth_password": auth_password,
                "auth_token": auth_token,
                "auth_username": auth_username,
                "clone_addr": clone_addr,
                "description": description,
                "issues": issues,
                "labels": labels,
                "lfs": lfs,
                "lfs_endpoint": lfs_endpoint,
                "milestones": milestones,
                "mirror": mirror,
                "mirror_interval": mirror_interval,
                "private": private,
                "pull_requests": pull_requests,
                "releases": releases,
                "repo_name": repo_name,
                "repo_owner": repo_owner,
                "service": service,
                "wiki": wiki,
            },
        )
        if "id" in result:
            gitea.logger.info(
                "Successfully created Job to Migrate Repository %s " % result["name"]
            )
        else:
            gitea.logger.error(result["message"])
            raise Exception(
                "Repository not Migrated... (gitea: %s)" % result["message"]
            )
        return Repository.parse_response(gitea, result)


class Milestone(ApiObject):
    API_OBJECT = """/repos/{owner}/{repo}/milestones/{number}"""  # <owner, repo>

    def __init__(self, gitea):
        super().__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Milestone):
            return False
        return self.gitea == other.gitea and self.id == other.id

    def __hash__(self):
        return hash(self.gitea) ^ hash(self.id)

    _fields_to_parsers = {
        "closed_at": lambda gitea, t: Util.convert_time(t),
        "due_on": lambda gitea, t: Util.convert_time(t),
    }

    _patchable_fields = {
        "allow_merge_commits",
        "allow_rebase",
        "allow_rebase_explicit",
        "allow_squash_merge",
        "archived",
        "default_branch",
        "description",
        "has_issues",
        "has_pull_requests",
        "has_wiki",
        "ignore_whitespace_conflicts",
        "name",
        "private",
        "website",
    }

    @classmethod
    def request(cls, gitea: "Gitea", owner: str, repo: str, number: str):
        return cls._request(gitea, {"owner": owner, "repo": repo, "number": number})


class Comment(ApiObject):
    def __init__(self, gitea):
        super().__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Comment):
            return False
        return self.repo == other.repo and self.id == other.id

    def __hash__(self):
        return hash(self.repo) ^ hash(self.id)

    _fields_to_parsers = {
        "user": lambda gitea, r: User.parse_response(gitea, r),
        "created_at": lambda gitea, t: Util.convert_time(t),
        "updated_at": lambda gitea, t: Util.convert_time(t),
    }


class Commit(ReadonlyApiObject):
    def __init__(self, gitea):
        super().__init__(gitea)

    _fields_to_parsers = {
        # NOTE: api may return None for commiters that are no gitea users
        "author": lambda gitea, u: User.parse_response(gitea, u)
        if u
        else None
    }

    def __eq__(self, other):
        if not isinstance(other, Commit):
            return False
        return self.sha == other.sha

    def __hash__(self):
        return hash(self.sha)

    @classmethod
    def parse_response(cls, gitea, result) -> "Commit":
        commit_cache = result["commit"]
        api_object = cls(gitea)
        cls._initialize(gitea, api_object, result)
        # inner_commit for legacy reasons
        Commit._add_read_property("inner_commit", commit_cache, api_object)
        return api_object


class Issue(ApiObject):
    API_OBJECT = """/repos/{owner}/{repo}/issues/{index}"""  # <owner, repo, index>
    GET_TIME = """/repos/%s/%s/issues/%s/times"""  # <owner, repo, index>
    GET_COMMENTS = """/repos/%s/%s/issues/comments"""
    CREATE_ISSUE = """/repos/{owner}/{repo}/issues"""

    OPENED = "open"
    CLOSED = "closed"

    def __init__(self, gitea):
        super().__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Issue):
            return False
        return self.repo == other.repo and self.id == other.id

    def __hash__(self):
        return hash(self.repo) ^ hash(self.id)

    _fields_to_parsers = {
        "milestone": lambda gitea, m: Milestone.parse_response(gitea, m),
        "user": lambda gitea, u: User.parse_response(gitea, u),
        "assignee": lambda gitea, u: User.parse_response(gitea, u),
        "assignees": lambda gitea, us: [User.parse_response(gitea, u) for u in us],
        "state": lambda gitea, s: Issue.CLOSED if s == "closed" else Issue.OPENED,
        # Repository in this request is just a "RepositoryMeta" record, thus request whole object
        "repository": lambda gitea, r: Repository.request(gitea, r["owner"], r["name"]),
    }

    _parsers_to_fields = {
        "milestone": lambda m: m.id,
    }

    _patchable_fields = {
        "assignee",
        "assignees",
        "body",
        "due_date",
        "milestone",
        "state",
        "title",
    }

    def commit(self):
        values = self.get_dirty_fields()
        args = {
            "owner": self.repository.owner.username,
            "repo": self.repository.name,
            "index": self.number,
        }
        self.gitea.requests_patch(Issue.API_OBJECT.format(**args), data=values)
        self.dirty_fields = {}

    @classmethod
    def request(cls, gitea: "Gitea", owner: str, repo: str, number: str):
        api_object = cls._request(
            gitea, {"owner": owner, "repo": repo, "index": number}
        )
        return api_object

    @classmethod
    def create_issue(cls, gitea, repo: Repository, title: str, body: str = ""):
        args = {"owner": repo.owner.username, "repo": repo.name}
        data = {"title": title, "body": body}
        result = gitea.requests_post(Issue.CREATE_ISSUE.format(**args), data=data)
        return Issue.parse_response(gitea, result)

    def get_time_sum(self, user: User) -> int:
        results = self.gitea.requests_get(
            Issue.GET_TIME % (self.owner.username, self.repo.name, self.number)
        )
        return sum(
            result["time"]
            for result in results
            if result and result["user_id"] == user.id
        )

    def get_times(self) -> Optional[Dict]:
        return self.gitea.requests_get(
            Issue.GET_TIME % (self.owner.username, self.repository.name, self.number)
        )

    def delete_time(self, time_id: str):
        path = f"/repos/{self.owner.username}/{self.repository.name}/issues/{self.number}/times/{time_id}"
        self.gitea.requests_delete(path)

    def add_time(self, time: int, created: str = None, user_name: User = None):
        path = f"/repos/{self.owner.username}/{self.repository.name}/issues/{self.number}/times"
        self.gitea.requests_post(
            path, data={"created": created, "time": int(time), "user_name": user_name}
        )

    def get_comments(self) -> List[ApiObject]:
        results = self.gitea.requests_get(
            Issue.GET_COMMENTS % (self.owner.username, self.repo.name)
        )
        allProjectComments = [
            Comment.parse_response(self.gitea, result) for result in results
        ]
        # Comparing the issue id with the URL seems to be the only (!) way to get to the comments of one issue
        return [
            comment
            for comment in allProjectComments
            if comment.issue_url.endswith("/" + str(self.number))
        ]


class Team(ApiObject):
    API_OBJECT = """/teams/{id}"""  # <id>
    ADD_REPO = """/teams/%s/repos/%s/%s"""  # <id, org, repo>
    TEAM_DELETE = """/teams/%s"""  # <id>
    GET_MEMBERS = """/teams/%s/members"""  # <id>
    GET_REPOS = """/teams/%s/repos"""  # <id>

    def __init__(self, gitea):
        super().__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Team):
            return False
        return self.organization == other.organization and self.id == other.id

    def __hash__(self):
        return hash(self.organization) ^ hash(self.id)

    _fields_to_parsers = {
        "organization": lambda gitea, o: Organization.parse_response(gitea, o)
    }

    _patchable_fields = {
        "can_create_org_repo",
        "description",
        "includes_all_repositories",
        "name",
        "permission",
        "units",
        "units_map",
    }

    @classmethod
    def request(cls, gitea: "Gitea", id: int):
        return cls._request(gitea, {"id": id})

    def commit(self):
        values = self.get_dirty_fields()
        args = {"id": self.id}
        self.gitea.requests_patch(self.API_OBJECT.format(**args), data=values)
        self.dirty_fields = {}

    def add_user(self, user: User):
        """https://try.gitea.io/api/swagger#/organization/orgAddTeamMember"""
        url = f"/teams/{self.id}/members/{user.login}"
        self.gitea.requests_put(url)

    def add_repo(self, org: Organization, repo: Repository):
        self.gitea.requests_put(Team.ADD_REPO % (self.id, org, repo.name))

    def get_members(self):
        """Get all users assigned to the team."""
        results = self.gitea.requests_get(Team.GET_MEMBERS % self.id)
        return [User.parse_response(self.gitea, result) for result in results]

    def get_repos(self):
        """Get all repos of this Team."""
        results = self.gitea.requests_get(Team.GET_REPOS % self.id)
        return [Repository.parse_response(self.gitea, result) for result in results]

    def delete(self):
        self.gitea.requests_delete(Team.TEAM_DELETE % self.id)
        self.deleted = True

    def remove_team_member(self, user_name: str):
        url = f"/teams/{self.id}/members/{user_name}"
        self.gitea.requests_delete(url)


class Content(ReadonlyApiObject):
    FILE = "file"

    def __init__(self, gitea):
        super().__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Team):
            return False
        return (
            self.repo == self.repo and self.sha == other.sha and self.name == other.name
        )

    def __hash__(self):
        return hash(self.repo) ^ hash(self.sha) ^ hash(self.name)


class Util:
    @staticmethod
    def convert_time(time: str) -> datetime:
        """Parsing of strange Gitea time format ("%Y-%m-%dT%H:%M:%S:%z" but with ":" in time zone notation)"""
        try:
            return datetime.strptime(time[:-3] + "00", "%Y-%m-%dT%H:%M:%S%z")
        except ValueError:
            return datetime.strptime(time[:-3] + "00", "%Y-%m-%dT%H:%M:%S")


class MigrationServices:
    GIT = "1"
    GITHUB = "2"
    GITEA = "3"
    GITLAB = "4"
    GOGS = "5"
    ONEDEV = "6"
    GITBUCKET = "7"
    CODEBASE = "8"
