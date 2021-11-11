import json
import logging
from datetime import datetime
from typing import List, Tuple, Dict, Sequence, Optional, Union, Set

import requests
from httpcache import CachingHTTPAdapter

from .basicGiteaApiObject import BasicGiteaApiObject
from .exceptions import *
from .giteaApiObject import GiteaApiObject


class Organization(GiteaApiObject):
    """see https://try.gitea.io/api/swagger#/organization/orgGetAll"""

    GET_API_OBJECT = """/orgs/{name}"""  # <org>
    PATCH_API_OBJECT = """/orgs/{name}"""  # <org>
    ORG_REPOS_REQUEST = """/orgs/%s/repos"""  # <org>
    ORG_TEAMS_REQUEST = """/orgs/%s/teams"""  # <org>
    ORG_TEAMS_CREATE = """/orgs/%s/teams"""  # <org>
    ORG_GET_MEMBERS = """/orgs/%s/members"""  # <org>
    ORG_IS_MEMBER = """/orgs/%s/members/%s"""  # <org>, <username>
    ORG_DELETE = """/orgs/%s"""  # <org>
    ORG_HEATMAP = """/users/%s/heatmap"""  # <username>

    def __init__(self, gitea):
        super(Organization, self).__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Organization): return False
        return self.gitea == other.gitea and self.name == other.name

    def __hash__(self):
        return hash(self.gitea) ^ hash(self.name)

    @classmethod
    def request(cls, gitea, name):
        return cls._request(gitea, {"name": name})

    @classmethod
    def parse_response(cls, gitea, result):
        api_object = super().parse_response(gitea, result)
        # add "name" field to make this behave similar to users
        Organization._add_readonly_property("name", result["username"], api_object)
        return api_object

    patchable_fields = {"description", "full_name", "location", "visibility", "website"}

    def commit(self):
        values = self.get_dirty_fields()
        args = {"name": self.name}
        self.gitea.requests_patch(
            Organization.PATCH_API_OBJECT.format(**args), data=values
        )
        self.dirty_fields = {}

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
        for t in teams: setattr(t, "_organization", self)
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

    def remove_member(self, user: GiteaApiObject):
        path = f"/orgs/{self.username}/members/{user.username}"
        self.gitea.requests_delete(path)

    def delete(self):
        """ Delete this Organization. Invalidates this Objects data. Also deletes all Repositories owned by the User"""
        for repo in self.get_repositories():
            repo.delete()
        self.gitea.requests_delete(Organization.ORG_DELETE % self.username)
        self.deleted = True

    def get_heatmap(self) -> List[Tuple[datetime, int]]:
        results = self.gitea.requests_get(User.USER_HEATMAP % self.username)
        results = [
            (datetime.fromtimestamp(result["timestamp"]), result["contributions"])
            for result in results
        ]
        return results


class User(GiteaApiObject):
    GET_API_OBJECT = """/users/{name}"""  # <org>
    USER_MAIL = """/user/emails?sudo=%s"""  # <name>
    USER_PATCH = """/admin/users/%s"""  # <username>
    ADMIN_DELETE_USER = """/admin/users/%s"""  # <username>
    ADMIN_EDIT_USER = """/admin/users/{username}"""  # <username>
    USER_HEATMAP = """/users/%s/heatmap"""  # <username>

    def __init__(self, gitea):
        super(User, self).__init__(gitea)
        self._emails = []

    def __eq__(self, other):
        if not isinstance(other, User): return False
        return self.gitea == other.gitea and self.id == other.id

    def __hash__(self):
        return hash(self.gitea) ^ hash(self.id)

    @property
    def emails(self):
        self.__request_emails()
        return self._emails

    @classmethod
    def request(cls, gitea, name) -> "User":
        api_object = cls._request(gitea, {"name": name})
        return api_object

    patchable_fields = {
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

    def get_repositories(self) -> List["Repository"]:
        """ Get all Repositories owned by this User."""
        url = f"/users/{self.username}/repos"
        results = self.gitea.requests_get(url)
        return [Repository.parse_response(self.gitea, result) for result in results]

    def get_orgs(self) -> List[Organization]:
        """ Get all Organizations this user is a member of."""
        url = f"/users/{self.username}/orgs"
        results = self.gitea.requests_get(url)
        return [Organization.parse_response(self.gitea, result) for result in results]

    def get_teams(self) -> List['Team']:
        url = f"/user/teams"
        results = self.gitea.requests_get(url, sudo=self)
        return [Team.parse_response(self.gitea, result) for result in results]

    def get_accessible_repos(self) -> List['Repository']:
        """ Get all Repositories accessible by the logged in User."""
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
        """ Deletes this User. Also deletes all Repositories he owns."""
        self.gitea.requests_delete(User.ADMIN_DELETE_USER % self.username)
        self.deleted = True

    def get_heatmap(self) -> List[Tuple[datetime, int]]:
        results = self.gitea.requests_get(User.USER_HEATMAP % self.username)
        results = [
            (datetime.fromtimestamp(result["timestamp"]), result["contributions"])
            for result in results
        ]
        return results


class Branch(GiteaApiObject):
    GET_API_OBJECT = """/repos/%s/%s/branches/%s"""  # <owner>, <repo>, <ref>

    def __init__(self, gitea):
        super(Branch, self).__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Branch): return False
        return self.repo == other.repo and self.name == other.name

    def __hash__(self):
        return hash(self.repo) ^ hash(self.name)

    fields_to_parsers = {
        "commit": lambda gitea, c: Commit.parse_response(gitea, c)
    }

    @classmethod
    def request(cls, gitea, owner, repo, ref):
        return cls._request(gitea, {"owner": owner, "repo": repo, "ref": ref})


class Repository(GiteaApiObject):
    REPO_IS_COLLABORATOR = (
        """/repos/%s/%s/collaborators/%s"""  # <owner>, <reponame>, <username>
    )
    GET_API_OBJECT = """/repos/{owner}/{name}"""  # <owner>, <reponame>
    REPO_SEARCH = """/repos/search/%s"""  # <reponame>
    REPO_BRANCHES = """/repos/%s/%s/branches"""  # <owner>, <reponame>
    REPO_ISSUES = """/repos/%s/%s/issues"""  # <owner, reponame>
    REPO_DELETE = """/repos/%s/%s"""  # <owner>, <reponame>
    REPO_TIMES = """/repos/%s/%s/times"""  # <owner>, <reponame>
    REPO_USER_TIME = """/repos/%s/%s/times/%s"""  # <owner>, <reponame>, <username>
    REPO_COMMITS = "/repos/%s/%s/commits"  # <owner>, <reponame>
    REPO_TRANSFER = "/repos/{owner}/{repo}/transfer"
    REPO_CONTENTS = "/repos/{owner}/{repo}/contents"
    REPO_CONTENT = """/repos/{owner}/{repo}/contents/{filepath}"""

    def __init__(self, gitea):
        super(Repository, self).__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Repository): return False
        return self.owner == other.owner and self.name == other.name

    def __hash__(self):
        return hash(self.owner) ^ hash(self.name)

    fields_to_parsers = {
        # dont know how to tell apart user and org as owner except form email being empty.
        "owner": lambda gitea, r: Organization.parse_response(gitea, r)
        if r["email"] == ""
        else User.parse_response(gitea, r),
        "updated_at": lambda gitea, t: Util.convert_time(t),
    }

    @classmethod
    def request(cls, gitea, owner, name):
        return cls._request(gitea, {"owner": owner, "name": name})

    patchable_fields = {
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

    def get_branches(self) -> List['Branch']:
        """Get all the Branches of this Repository."""
        results = self.gitea.requests_get(
            Repository.REPO_BRANCHES % (self.owner.username, self.name)
        )
        return [Branch.parse_response(self.gitea, result) for result in results]

    def add_branch(self, create_from: Branch, newname: str) -> "Commit":
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

    def get_commits(self) -> List["Commit"]:
        """Get all the Commits of this Repository."""
        try:
            results = self.gitea.requests_get_commits(
                Repository.REPO_COMMITS % (self.owner.username, self.name)
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
        # "page": -1 is returning _all_ issues instead of pages. Hopefully this is intended behaviour.
        data = {"page": -1, "state": state}
        results = self.gitea.requests_get(
            Repository.REPO_ISSUES % (self.owner.username, self.name), params=data
        )
        for result in results:
            issue = Issue.parse_response(self.gitea, result)
            # adding data not contained in the issue answer
            setattr(issue, "repo", self.name)
            setattr(issue, "owner", self.owner)
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

    def create_issue(self, title, assignees=[], description="") -> GiteaApiObject:
        data = {
            "assignees": assignees,
            "body": description,
            "closed": False,
            "title": title,
        }
        result = self.gitea.requests_post(
            Repository.REPO_ISSUES % (self.owner.username, self.name), data=data
        )
        return Issue.parse_response(self.gitea, result)

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

    def transfer_ownership(self, new_owner: Union["User", "Organization"], new_teams: Set["Team"] = frozenset()):
        url = Repository.REPO_TRANSFER.format(owner=self.owner.username, repo=self.name)
        data = {"new_owner": new_owner.username}
        if isinstance(new_owner, Organization):
            new_team_ids = [team.id for team in new_teams if team in new_owner.get_teams()]
            data["team_ids"] = new_team_ids
        self.gitea.requests_post(url, data=data)
        # TODO: make sure this instance is either updated or discarded

    def get_git_content(self, file_path: str = None, commit : "Commit" = None) -> List["Content"]:
        """https://git.sopranium.de/api/swagger#/repository/repoGetContentsList"""
        url = Repository.REPO_CONTENTS.format(owner=self.owner.username, repo=self.name)
        data = {"ref": "HEAD" if commit is None else commit.sha}
        if file_path: data["filepath"] = file_path
        result = [Content.parse_response(self.gitea, f) for f in self.gitea.requests_get(url, data)]
        return result

    def get_file_content(self, content: "Content", commit : "Commit" = None) -> Union[str, List["Content"]]:
        """https://git.sopranium.de/api/swagger#/repository/repoGetContents"""
        if content.type == Content.FILE:
            url = Repository.REPO_CONTENT.format(owner=self.owner.username,
                                                 repo=self.name, filepath=content.path)
            data = {"ref": "HEAD" if commit is None else commit.sha}
            return self.gitea.requests_get(url, data)["content"]
        else:
            return self.get_git_content(self.owner.name, self.name, content.path)

    def delete(self):
        self.gitea.requests_delete(
                Repository.REPO_DELETE % (self.owner.username, self.name)
        )
        self.deleted = True

class Milestone(GiteaApiObject):
    GET_API_OBJECT = (
        """/repos/{owner}/{repo}/milestones/{number}"""  # <owner, repo>
    )

    def __init__(self, gitea):
        super(Milestone, self).__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Milestone): return False
        return self.repo == other.repo and self.id == other.id

    def __hash__(self):
        return hash(self.repo) ^ hash(self.id)

    fields_to_parsers = {
        "closed_at": lambda gitea, t: Util.convert_time(t),
        "due_on": lambda gitea, t: Util.convert_time(t),
    }

    patchable_fields = {
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
    def request(cls, gitea, owner, repo, number):
        return cls._request(gitea, {"owner": owner, "repo": repo, "number": number})


class Comment(BasicGiteaApiObject):
    PATCH_API_OBJECT = "/repos/{owner}/{repo}/issues/comments/{id}"

    def __init__(self, gitea):
        super(Comment, self).__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Comment): return False
        return self.repo == other.repo and self.id == other.id

    def __hash__(self):
        return hash(self.repo) ^ hash(self.id)

    fields_to_parsers = {
        "user": lambda gitea, r: User.parse_response(gitea, r),
        "created_at": lambda gitea, t: Util.convert_time(t),
        "updated_at": lambda gitea, t: Util.convert_time(t),
    }

    patchable_fields = {"body"}


class Commit(GiteaApiObject):
    def __init__(self, gitea):
        super(Commit, self).__init__(gitea)

    fields_to_parsers = {
        # NOTE: do not try to parse gitea-users from git-committers/authors, as
        # they are not necessarily users of gitea as well
    }

    def __eq__(self, other):
        if not isinstance(other, Commit): return False
        return self.repo == other.repo and self.ref == other.ref

    def __hash__(self):
        return hash(self.repo) ^ hash(self.ref)

    @classmethod
    def request(cls, gitea, owner, repo):
        api_object = cls._request(gitea, {"owner": owner, "repo": repo})
        return api_object

    @classmethod
    def parse_response(cls, gitea, result):
        api_object = cls(gitea)
        cls._initialize(gitea, api_object, result)
        return api_object


class Issue(GiteaApiObject):
    GET_API_OBJECT = """/repos/{owner}/{repo}/issues/{number}"""  # <owner, repo, index>
    GET_TIME = """/repos/%s/%s/issues/%s/times"""  # <owner, repo, index>
    GET_COMMENTS = """/repos/%s/%s/issues/comments"""
    CREATE_ISSUE = """/repos/{owner}/{repo}/issues"""

    OPENED = "open"
    CLOSED = "closed"

    def __init__(self, gitea):
        super(Issue, self).__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Issue): return False
        return self.repo == other.repo and self.id == other.id

    def __hash__(self):
        return hash(self.repo) ^ hash(self.id)

    fields_to_parsers = {
        "milestone": lambda gitea, m: Milestone.parse_response(gitea, m),
        "user": lambda gitea, u: User.parse_response(gitea, u),
        "assignee": lambda gitea, u: User.parse_response(gitea, u),
        "assignees": lambda gitea, us: [User.parse_response(gitea, u) for u in us],
        "state": lambda gitea, s: Issue.CLOSED if s == "closed" else Issue.OPENED,
    }

    patchable_fields = {
        "assignee",
        "assignees",
        "body",
        "due_date",
        "milestone",
        "state",
        "title",
    }

    @classmethod
    def request(cls, gitea, owner, repo, number):
        api_object = cls._request(
            gitea, {"owner": owner, "repo": repo, "number": number}
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
            Issue.GET_TIME % (self.owner.username, self.repo, self.number)
        )
        return sum(
            result["time"]
            for result in results
            if result and result["user_id"] == user.id
        )

    def get_times(self) -> Optional[Dict]:
        return self.gitea.requests_get(
            Issue.GET_TIME % (self.owner.username, self.repo, self.number)
        )

    def delete_time(self, time_id: str):
        path = f"/repos/{self.owner.username}/{self.repo}/issues/{self.number}/times/{time_id}"
        self.gitea.requests_delete(path)

    def add_time(self, time: int, created: str = None, user_name: str = None):
        path = f"/repos/{self.owner.username}/{self.repo}/issues/{self.number}/times"
        self.gitea.requests_post(
            path, data={"created": created, "time": int(time), "user_name": user_name}
        )

    def get_comments(self) -> List[GiteaApiObject]:
        results = self.gitea.requests_get(
            Issue.GET_COMMENTS % (self.owner.username, self.repo)
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


class Team(GiteaApiObject):
    GET_API_OBJECT = """/teams/{id}"""  # <id>
    ADD_USER = """/teams/%s/members/%s"""  # <id, username to add>
    ADD_REPO = """/teams/%s/repos/%s/%s"""  # <id, org, repo>
    TEAM_DELETE = """/teams/%s"""  # <id>
    GET_MEMBERS = """/teams/%s/members"""  # <id>
    GET_REPOS = """/teams/%s/repos"""  # <id>

    def __init__(self, gitea):
        super(Team, self).__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Team): return False
        return self.organization == other.organization and self.id == other.id

    def __hash__(self):
        return hash(self.organization) ^ hash(self.id)

    fields_to_parsers = {
        "organization": lambda gitea, o: Organization.parse_response(gitea, o)
    }

    @classmethod
    def request(cls, gitea, organization, team):
        return cls._request(gitea, {"id": id})

    patchable_fields = {"description", "name", "permission", "units"}

    def add_user(self, user: User):
        self.gitea.requests_put(Team.ADD_USER % (self.id, user.login))

    def add_repo(self, org: Organization, repo: Repository):
        self.gitea.requests_put(Team.ADD_REPO % (self.id, org, repo.name))

    def get_members(self):
        """ Get all users assigned to the team. """
        results = self.gitea.requests_get(Team.GET_MEMBERS % self.id)
        return [User.parse_response(self.gitea, result) for result in results]

    def get_repos(self):
        """ Get all repos of this Team."""
        results = self.gitea.requests_get(Team.GET_REPOS % self.id)
        return [Repository.parse_response(self.gitea, result) for result in results]

    def delete(self):
        self.gitea.requests_delete(Team.TEAM_DELETE % self.id)
        self.deleted = True

    def remove_team_member(self, user_name: str):
        url = f"/teams/{self.id}/members/{user_name}"
        self.gitea.requests_delete(url)

class Content(GiteaApiObject):
    GET_API_OBJECT = """/repos/{owner}/{repo}/contents/{filepath}"""

    FILE = "file"

    def __init__(self, gitea):
        super(Content, self).__init__(gitea)

    def __eq__(self, other):
        if not isinstance(other, Team): return False
        return self.repo == self.repo and self.sha == other.sha and self.name == other.name

    def __hash__(self):
        return hash(self.repo) ^ hash(self.sha) ^ hash(self.name)


class Util:
    @staticmethod
    def convert_time(time: str) -> datetime:
        """ Parsing of strange Gitea time format ("%Y-%m-%dT%H:%M:%S:%z" but with ":" in time zone notation)"""
        try:
            return datetime.strptime(time[:-3] + "00", "%Y-%m-%dT%H:%M:%S%z")
        except ValueError:
            return datetime.strptime(time[:-3] + "00", "%Y-%m-%dT%H:%M:%S")


class Gitea:
    """ Object to establish a session with Gitea. """

    ADMIN_CREATE_USER = """/admin/users"""
    GET_USERS_ADMIN = """/admin/users"""
    ADMIN_REPO_CREATE = """/admin/users/%s/repos"""  # <ownername>
    GITEA_VERSION = """/version"""
    GET_USER = """/user"""
    CREATE_ORG = """/admin/users/%s/orgs"""  # <username>
    CREATE_TEAM = """/orgs/%s/teams"""  # <orgname>

    def __init__(self, gitea_url: str, token_text: str, cached=False, log_level="INFO"):
        """ Initializing Gitea-instance."""
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.headers = {
            "Authorization": "token " + token_text,
            "Content-type": "application/json",
        }
        self.url = gitea_url
        self.requests = requests.Session()
        if cached:
            self.requests.mount("http://", CachingHTTPAdapter())
            self.requests.mount("https://", CachingHTTPAdapter())

    def __get_url(self, endpoint):
        url = self.url + "/api/v1" + endpoint
        self.logger.debug("Url: %s" % url)
        return url

    @staticmethod
    def parse_result(result) -> Dict:
        """ Parses the result-JSON to a dict. """
        if result.text and len(result.text) > 3:
            return json.loads(result.text)
        return {}

    def requests_get_paginated(self, endpoint, params ={}, requests=None, sudo=None, page_key: str = "page"):
        page = 1
        combined_params = {}
        combined_params.update(params)
        aggregated_result = []
        while True:
            combined_params[page_key] = page
            result = self.requests_get(endpoint, combined_params, requests, sudo)
            aggregated_result.extend(result)
            page += 1
            if len(result) == 0:
                return aggregated_result

    def requests_get(self, endpoint, params={}, requests=None, sudo=None):
        combined_params = {}
        combined_params.update(params)
        if sudo:
            combined_params["sudo"] = sudo.username
        if not requests:
            request = self.requests.get(
                self.__get_url(endpoint), headers=self.headers, params=combined_params
            )
        else:
            request = requests.get(
                self.__get_url(endpoint), headers=self.headers, params=combined_params
            )
        if request.status_code == 204:
            return None
        if request.status_code not in [200, 201]:
            message = "Received status code: %s (%s)" % (
                request.status_code,
                request.url,
            )
            if request.status_code in [404]:
                raise NotFoundException(message)
            if request.status_code in [403]:
                raise Exception(
                    "Unauthorized: %s - Check your permissions and try again! (%s)"
                    % (request.url, message)
                )
            if request.status_code in [409]:
                raise ConflictException(message)
            raise Exception(message)
        return self.parse_result(request)

    def requests_get_commits(self, endpoint, page=1, params={}, requests=None):
        results = []
        page_endpoint = endpoint + f"?page={page}"
        if not requests:
            request = self.requests.get(
                self.__get_url(page_endpoint), headers=self.headers, params=params
            )
        else:
            request = requests.get(
                self.__get_url(page_endpoint), headers=self.headers, params=params
            )
        results += self.parse_result(request)
        if request.headers.get("x-hasmore") == "true":
            page += 1
            results += self.requests_get_commits(endpoint, page)
        elif request.status_code not in [200, 201]:
            message = "Received status code: %s (%s)" % (
                request.status_code,
                request.url,
            )
            if request.status_code in [404]:
                raise NotFoundException(message)
            if request.status_code in [403]:
                raise Exception(
                    "Unauthorized: %s - Check your permissions and try again! (%s)"
                    % (request.url, message)
                )
            if request.status_code in [409]:
                raise ConflictException(message)
            raise Exception(message)
        return results

    def requests_put(self, endpoint):
        request = self.requests.put(self.__get_url(endpoint), headers=self.headers)
        if request.status_code not in [204]:
            message = "Received status code: %s (%s) %s" % (
                request.status_code,
                request.url,
                request.text,
            )
            self.logger.error(message)
            raise Exception(message)

    def requests_delete(self, endpoint):
        request = self.requests.delete(self.__get_url(endpoint), headers=self.headers)
        if request.status_code not in [204]:
            message = "Received status code: %s (%s)" % (
                request.status_code,
                request.url,
            )
            self.logger.error(message)
            raise Exception(message)

    def requests_post(self, endpoint, data):
        """ Post data to API-endpoint.

        Args:
            endpoint (str): endpoint of API to send data to
            data (dict): Data to send.

        Returns: (dict)
            Parsed JSON-answer from the API.

        Throws:
            AlreadyExistsException, if 'already exists' in answer
            Exception, if status code not ok
        """
        request = self.requests.post(
            self.__get_url(endpoint), headers=self.headers, data=json.dumps(data)
        )
        if request.status_code not in [200, 201, 202]:
            if (
                "already exists" in request.text
                or "e-mail already in use" in request.text
            ):
                self.logger.warning(request.text)
                raise AlreadyExistsException()
            self.logger.error(
                "Received status code: %s (%s)" % (request.status_code, request.url)
            )
            self.logger.error("With info: %s (%s)" % (data, self.headers))
            self.logger.error("Answer: %s" % request.text)
            raise Exception(
                "Received status code: %s (%s), %s"
                % (request.status_code, request.url, request.text)
            )

        return self.parse_result(request)

    def requests_patch(self, endpoint, data):
        request = self.requests.patch(
            self.__get_url(endpoint), headers=self.headers, data=json.dumps(data)
        )
        if request.status_code not in [200, 201]:
            error_message = "Received status code: %s (%s) %s" % (
                request.status_code,
                request.url,
                data,
            )
            self.logger.error(error_message)
            raise Exception(error_message)
        return self.parse_result(request)

    def get_users_search(self):
        path = "/users/search"
        return self.requests_get(path)

    def get_orgs_public_members_all(self, orgname):
        path = "/orgs/" + orgname + "/public_members"
        return self.requests_get(path)

    def get_orgs(self):
        path = "/admin/orgs"
        results = self.requests_get(path)
        return [Organization.parse_response(self, result) for result in results]

    def post_repos__forks(self, organization, repo, owner):
        path = "/repos/" + owner + "/" + repo + "/forks"
        return self.requests_post(path, data={"organization": organization})

    def get_repos_forks(self, repo, owner):
        path = "/repos/" + owner + "/" + repo + "/forks"
        return self.requests_get(path)

    def put_repos__subscription(self, username, reponame):
        path = "/repos/" + username + "/" + reponame + "/subscription"
        return self.requests.put(path)

    def delete_repos_subscription(self, username, reponame):
        path = "/repos/" + username + "/" + reponame + "/subscription"
        return self.requests.delete(path)

    def get_repos_subscription(self, username, reponame):
        path = "/repos/" + username + "/" + reponame + "/subscription"
        return self.requests_get(path)

    def get_users_following(self, username):
        path = "/users/" + username + "/following"
        return self.requests_get(path)

    def get_users_starred(self, username):
        path = "/users/" + username + "/starred"
        return self.requests_get(path)

    def put_orgs_public_members(self, username, orgname):
        path = "/orgs/" + orgname + "/public_members/" + username
        return self.requests.put(path)

    def delete_orgs_public_members(self, username, orgname):
        path = "/orgs/" + orgname + "/public_members/" + username
        return self.requests.delete(path)

    def get_orgs_public_members(self, username, orgname):
        path = "/orgs/" + orgname + "/public_members/" + username
        return self.requests_get(path)

    def post_org_repos(
        self, name, description, private, auto_init, gitignores, license, readme, org
    ):
        path = "/org/" + org + "/repos"
        return self.requests_post(
            path,
            data={
                "name": name,
                "description": description,
                "private": private,
                "auto_init": auto_init,
                "gitignores": gitignores,
                "license": license,
                "readme": readme,
            },
        )

    def delete_orgs_members(self, orgname, username):
        path = "/orgs/" + orgname + "/members/" + username
        return self.requests.delete(path)

    def post_repos__hooks(self, type, config, events, active, reponame, username):
        path = "/repos/" + username + "/" + reponame + "/hooks"
        return self.requests_post(
            path,
            data={"type": type, "config": config, "events": events, "active": active},
        )

    def get_repos_hooks(self, reponame, username):
        path = "/repos/" + username + "/" + reponame + "/hooks"
        return self.requests_get(path)

    def post_repos_migrate(
        self,
        clone_addr,
        auth_username,
        auth_password,
        uid,
        repo_name,
        mirror,
        private,
        description,
    ):
        path = "/repos/migrate"
        return self.requests_post(
            path,
            data={
                "clone_addr": clone_addr,
                "auth_username": auth_username,
                "auth_password": auth_password,
                "uid": uid,
                "repo_name": repo_name,
                "mirror": mirror,
                "private": private,
                "description": description,
            },
        )

    def post_user_repos(
        self, name, description, private, auto_init, gitignores, license, readme
    ):
        path = "/user/repos"
        return self.requests_post(
            path,
            data={
                "name": name,
                "description": description,
                "private": private,
                "auto_init": auto_init,
                "gitignores": gitignores,
                "license": license,
                "readme": readme,
            },
        )

    # # #

    def get_user(self):
        result = self.requests_get(Gitea.GET_USER)
        return User.parse_response(self, result)

    def get_version(self) -> str:
        result = self.requests_get(Gitea.GITEA_VERSION)
        return result["version"]

    def get_users(self) -> List[User]:
        results = self.requests_get(Gitea.GET_USERS_ADMIN)
        return [User.parse_response(self, result) for result in results]

    def get_user_by_email(self, email: str) -> User:
        users = self.get_users()
        for user in users:
            if user.email == email or email in user.emails:
                return user
        return None

    def get_user_by_name(self, username: str) -> User:
        users = self.get_users()
        for user in users:
            if user.username == username:
                return user
        return None

    def create_user(
        self,
        user_name: str,
        email: str,
        password: str,
        login_name: str = None,
        change_pw=True,
        send_notify=True,
        source_id=0,
    ):
        """ Create User.
        Throws:
            AlreadyExistsException, if the User exists already
            Exception, if something else went wrong.
        """
        if not login_name:
            login_name = user_name
        request_data = {
            "source_id": source_id,
            "login_name": login_name,
            "username": user_name,
            "email": email,
            "password": password,
            "send_notify": send_notify,
            "must_change_password": change_pw,
        }

        self.logger.debug("Gitea post payload: %s", request_data)
        result = self.requests_post(Gitea.ADMIN_CREATE_USER, data=request_data)
        if "id" in result:
            self.logger.info(
                "Successfully created User %s <%s> (id %s)",
                result["login"],
                result["email"],
                result["id"],
            )
            self.logger.debug("Gitea response: %s", result)
        else:
            self.logger.error(result["message"])
            raise Exception("User not created... (gitea: %s)" % result["message"])
        user = User.parse_response(self, result)
        return user

    def create_repo(
        self,
        repoOwner,
        repoName: str,
        description: str = "",
        private: bool = False,
        autoInit=True,
        gitignores: str = None,
        license: str = None,
        readme: str = "Default",
        issue_labels: str = None,
    ):
        """ Create a Repository.
        Throws:
            AlreadyExistsException, if Repository exists already.
            Exception, if something else went wrong.

        """
        # although this only says user in the api, this also works for
        # organizations
        assert isinstance(repoOwner, User) or isinstance(repoOwner, Organization)
        result = self.requests_post(
            Gitea.ADMIN_REPO_CREATE % repoOwner.username,
            data={
                "name": repoName,
                "description": description,
                "private": private,
                "auto_init": autoInit,
                "gitignores": gitignores,
                "license": license,
                "issue_labels": issue_labels,
                "readme": readme,
            },
        )
        if "id" in result:
            self.logger.info("Successfully created Repository %s " % result["name"])
        else:
            self.logger.error(result["message"])
            raise Exception("Repository not created... (gitea: %s)" % result["message"])
        return Repository.parse_response(self, result)

    def create_org(
        self,
        owner: User,
        orgName: str,
        description: str,
        location="",
        website="",
        full_name="",
    ):
        assert isinstance(owner, User)
        result = self.requests_post(
            Gitea.CREATE_ORG % owner.username,
            data={
                "username": orgName,
                "description": description,
                "location": location,
                "website": website,
                "full_name": full_name,
            },
        )
        if "id" in result:
            self.logger.info(
                "Successfully created Organization %s" % result["username"]
            )
        else:
            self.logger.error(
                "Organization not created... (gitea: %s)" % result["message"]
            )
            self.logger.error(result["message"])
            raise Exception(
                "Organization not created... (gitea: %s)" % result["message"]
            )
        return Organization.parse_response(self, result)

    def create_team(
        self,
        org: Organization,
        name: str,
        description: str = "",
        permission: str = "read",
        units=(
            "repo.code",
            "repo.issues",
            "repo.ext_issues",
            "repo.wiki",
            "repo.pulls",
            "repo.releases",
            "repo.ext_wiki",
        ),
    ):
        """ Creates a Team.

        Args:
            org (Organization): Organization the Team will be part of.
            name (str): The Name of the Team to be created.
            description (str): Optional, None, short description of the new Team.
            permission (str): Optional, 'read', What permissions the members
        """
        result = self.requests_post(
            Gitea.CREATE_TEAM % org.username,
            data={
                "name": name,
                "description": description,
                "permission": permission,
                "units": units,
            },
        )
        if "id" in result:
            self.logger.info("Successfully created Team %s" % result["name"])
        else:
            self.logger.error("Team not created... (gitea: %s)" % result["message"])
            self.logger.error(result["message"])
            raise Exception("Team not created... (gitea: %s)" % result["message"])
        api_object = Team.parse_response(self, result)
        setattr(
            api_object, "_organization", org
        )  # fixes strange behaviour of gitea not returning a valid organization here.
        return api_object
