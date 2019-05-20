import json
import requests
import logging
from datetime import datetime

logging = logging.getLogger("gitea")
version = "0.4.3"


class AlreadyExistsException(Exception):
    """ Something (User/Repo/Organization/...) already exists.
    """

    pass


class NotFoundException(Exception):
    """ Something (User/Repo/Organization/...) has not been found.
    """

    pass


class Organization:
    """ Represents an Organization in the Gitea-instance.
    Attr:
        id: int
        avatar_url: string
        description: string
        full_name: string
        location: string
        username: string
        website: string
        gitea: Gitea-instance.
    """

    ORG_REQUEST = """/orgs/%s"""  # <org>
    ORG_REPOS_REQUEST = """/orgs/%s/repos"""  # <org>
    ORG_TEAMS_REQUEST = """/orgs/%s/teams"""  # <org>
    ORG_TEAMS_CREATE = """/orgs/%s/teams"""  # <org>
    ORG_PATCH = """/orgs/%s"""  # <org>
    ORG_GET_MEMBERS = """/orgs/%s/members"""  # <org>
    ORG_DELETE = """/orgs/%s"""  # <org>

    def __init__(self, gitea, orgName: str, initJson: json = None):
        """ Initialize Organization-Object. At least a name is required.
        Will get this Organization, and fail if it does not exist.

        Args:
            gitea (Gitea): current instance.
            orgName: Name of Organization.
            initJson (dict): Optional, init information for Organization

        Returns: Organization
            The initialized Organization.

        Throws:
            NotFoundException
        """
        self.gitea = gitea
        self.username = "UNINIT"
        self.__initialize_org(orgName, initJson)

    def __repr__(self):
        """ Representation of an Organization. Consisting of username and id.
        """
        return "Organization: %s (%s)" % (self.username, self.id)

    def __eq__(self, other):
        if not other is None:
            if isinstance(other, Organization):
                return other.id == self.id
        return False

    def get_repositories(self):
        """ Get the Repositories of this Organization.

        Returns: [Repository]
            A list of Repositories this Organization is hosting.
        """
        results = self.gitea.requests_get(
            Organization.ORG_REPOS_REQUEST % self.username
        )
        return [
            Repository(self.gitea, self, result["name"], initJson=result)
            for result in results
        ]

    def get_teams(self):
        """ Get the Teams in this Organization

        Returns: [Team]
            A list of Teams in this Organization.
        """
        results = self.gitea.requests_get(
            Organization.ORG_TEAMS_REQUEST % self.username
        )
        return [Team(self, result["name"], initJson=result) for result in results]

    def get_members(self):
        """ Get all members of this Organization

        Returns: [User]
            A list of Users who are members of this Organization.
        """
        results = self.gitea.requests_get(Organization.ORG_GET_MEMBERS % self.username)
        return [User(self, result["username"], initJson=result) for result in results]

    def __initialize_org(self, orgName: str, result) -> None:
        """ Initialize Organization.

        Args:
            orgName (str): Name of the Organization
            result (dict): Optional, init information for Organization

        Throws:
            Exception, if Organization could not be found.
        """
        if not result:
            result = self.gitea.requests_get(Organization.ORG_REQUEST % orgName)
        logging.debug("Found Organization: %s" % orgName)
        for i, v in result.items():
            setattr(self, i, v)

    def set_value(self, values: dict):
        """ Setting a certain value for an Organization.

        Args:
            values (dict): Which values should be changed
                description: string
                full_name: string
                location: string
                website: string
        """
        result = self.gitea.requests_patch(
            Organization.ORG_PATCH % self.username, data=values
        )
        self.__initialize_org(self.username, result)

    def remove_member(self, username):
        if isinstance(username, User):
            username = username.username
        path = "/orgs/" + self.username + "/members/" + username
        self.gitea.requests_delete(path)

    def delete(self):
        """ Delete this Organization. Invalidates this Objects data.
        Also deletes all Repositories and Teams associated with this
        Organization.
        """
        # TODO: Delete Repos, Teams, Users (except authenticated user)
        for repo in self.get_repositories():
            repo.delete()
        self.gitea.requests_delete(Organization.ORG_DELETE % self.username)


class User:
    """ Represents a User in the Gitea-instance.

    Attr:
        avatar_url: string
        email: string
        full_name: string
        id: int
        is_admin: bool
        language: string
        login: string
    """

    USER_MAIL = """/user/emails?sudo=%s"""  # <name>
    USER_REQUEST = """/users/%s"""  # <org>
    USER_REPOS_REQUEST = """/users/%s/repos"""  # <org>
    USER_PATCH = """/admin/users/%s"""  # <username>
    ADMIN_DELETE_USER = """/admin/users/%s"""  # <username>
    USER_HEATMAP = """/users/%s/heatmap"""  # <username>

    def __init__(self, gitea, userName: str, initJson: json = None):
        """ Initialize a User. At least a username is necessary.

        Warning:
            This will only get a user, not create one.
            `Gitea.create_user` does that.

        Args:
            gitea (Gitea): current instance.
            userName (str): login-name of the User.
            initJson (dict): Optional, init information for User

        Throws:
            NotFoundException, if User does not exist.
        """
        self.gitea = gitea
        self.username = "UNINIT"
        self.__initialize_user(userName, initJson)

    def __repr__(self):
        """ Representation of a User. Consisting of login-name and id.
        """
        return "User: %s (%s)" % (self.login, self.id)

    def get_repositories(self):
        """ Get all Repositories owned by this User.

        Returns: [Repository]
            A list of Repositories this user owns.
        """
        result = self.gitea.requests_get(User.USER_REPOS_REQUEST % self.username)
        return [Repository(self.gitea, self, r["name"]) for r in result]

    def __initialize_user(self, userName: str, result) -> None:
        """ Initialize User.

        Args:
            userName (str): The name of the user.
            result (dict): Optional, init information for User.
        """
        if not result:
            result = self.gitea.requests_get(User.USER_REQUEST % userName)
        for i, v in result.items():
            setattr(self, i, v)

    def __eq__(self, other):
        if other is not None:
            if isinstance(other, User):
                return other.id == self.id
        return False

    def update_mail(self):
        """ Update the mail of this user instance to one that is \
        actually correct.
        """
        prev = self.email
        result = self.gitea.requests_get(User.USER_MAIL % self.login)
        for mail in result:
            if mail["primary"]:
                self.email = mail["email"]
                break
        logging.info(
            "User %s updated Mail: <%s> to <%s>" % (self.login, prev, self.email)
        )

    def set_value(self, email: str, values: dict):
        """ Set certain values of this user.

        Args:
            email (str): The actual email of the User.
            values (dict): The (updated) values.

        Warning:
            The email you get from the API might not be sufficient.
            It needs to be the actual mail in the database.
        """
        # the request requires email to be set...
        values["email"] = email
        result = self.gitea.requests_patch(User.USER_PATCH % self.username, data=values)
        self.__initialize_user(self.username, result)

    def delete(self):
        """ Deletes this User. Also deletes all Repositories he owns.

        Warning:
            Invalidates this Objects Data.
        """
        # TODO: Delete all Repositories of this user.
        # Might not be deleteable otherwise.
        self.gitea.requests_delete(User.ADMIN_DELETE_USER % self.username)

    def get_heatmap(self):
        results = self.gitea.requests_get(User.USER_HEATMAP % self.username)
        results = [
            (datetime.fromtimestamp(result["timestamp"]), result["contributions"])
            for result in results
        ]
        return results


class Repository:
    """ Represents a Repository in the Gitea-instance.

    Attr:
        archived: bool
        clone_url: string
        default_branch: string
        id: int
        empty: bool
        owner: User/Organization
        private: bool
        ...
    """

    REPO_REQUEST = """/repos/%s/%s"""  # <owner>, <reponame>
    REPO_SEARCH = """/repos/search/%s"""  # <reponame>
    REPO_BRANCHES = """/repos/%s/%s/branches"""  # <owner>, <reponame>
    REPO_ISSUES = """/repos/%s/%s/issues"""  # <owner, reponame>
    REPO_DELETE = """/repos/%s/%s"""  # <owner>, <reponame>
    REPO_USER_TIME = """/repos/%s/%s/times/%s"""  # <owner>, <reponame>, <username>

    def __init__(self, gitea, repoOwner, repoName: str, initJson: json = None):
        """ Initializing a Repository.

        Args:
            gitea (Gitea): current instance.
            repoOwner (User/Organization): Owner of the Repository.
            repoName (str): Name of the Repository
            initJson (dict): Optional, init information for Repository.

        Warning:
            This does not Create a Repository. `gitea.create_repo` does.

        Throws:
            NotFoundException, if Repository has not been found.
        """
        self.gitea = gitea
        self.name = "UNINIT"
        self.__initialize_repo(repoOwner, repoName, initJson)

    def __initialize_repo(self, repoOwner, repoName: str, result):
        """ Initializing a Repository.

        Args:
            repoOwner (User/Organization): Owner of the Repository
            repoName (str): Name of the Repository
            result (dict): Optional, init information for Repository.

        Throws:
            NotFoundException, if Repository has not been found.
        """
        if not result:
            result = self.gitea.requests_get(
                Repository.REPO_REQUEST % (repoOwner.username, repoName)
            )
        logging.debug("Found Repository: %s/%s" % (repoOwner.username, repoName))
        for i, v in result.items():
            setattr(self, i, v)
        self.owner = repoOwner

    def __eq__(self, other):
        if not other is None:
            if isinstance(other, Repository):
                return other.id == self.id
        return False

    def __repr__(self):
        """ Representation of a Repository. Consisting of path and id.
        """
        return "Repository: %s/%s (%s)" % (self.owner.username, self.name, self.id)

    def get_branches(self):
        """Get all the Branches of this Repository.

        Returns: [Branch]
            A list of Branches of this Repository.
        """
        results = self.gitea.requests_get(
            Repository.REPO_BRANCHES % (self.owner.username, self.name)
        )
        return [Branch(self, result["name"], result) for result in results]

    def get_issues(self):
        """Get all Issues of this Repository.

        Returns: [Issue]
            A list of Issues of this Repository.
        """
        return self.get_issues_state("open") + self.get_issues_state("closed")

    def get_issues_state(self, state):
        """Get either open or closed Issues of this Repository.

        Returns: [Issue]
            A list of Issues of this Repository.
        """
        assert state in ["open", "closed"]
        index = 1
        issues = []
        while True:
            # q=&type=all&sort=&state=open&milestone=0&assignee=0
            results = self.gitea.requests_get(
                Repository.REPO_ISSUES % (self.owner.username, self.name),
                params={"page": index, "state": state},
            )
            if len(results) <= 0:
                break
            index += 1
            issues += [Issue(self, result["id"], result) for result in results]
        return issues

    def get_user_time(self, username, ignore_above=8):
        """Get the time a user spent working on this Repository.

        Args:
            username (str): Username of the user
            ignore_above (int): above what amount this number should be taken as invalid (in hours)

        Returns: int
            Accumulated time the user worked in this Repository.
        """
        if isinstance(username, User):
            username = username.username
        results = self.gitea.requests_get(
            Repository.REPO_USER_TIME % (self.owner.username, self.name, username)
        )
        time = (
            sum(
                filter(
                    lambda t: t < ignore_above * 3600, map(lambda d: d["time"], results)
                )
            )
            // 60
        ) / 60
        return time

    def delete(self):
        """ Deletes this Repository.

        Warning:
            Invalidates this objects Data.
        """
        self.gitea.requests_delete(
            Repository.REPO_DELETE % (self.owner.username, self.name)
        )

class Milestone:
    """Reperesents a Milestone in Gitea.
    """
    GET = """/repos/%s/%s/milestones/%s"""  # <owner, repo, id>

    def __init__(self, repo: Repository, id: int, initJson: json = None):
        """ Initializes a Milestone.

        Args:
            repo (Repository): The Repository of this Milestone.
            id (int): The id of the Milestone.
            initJson (dict): Optional, init information for Milestone.

        Warning:
            This does not create a Milestone. <sth> does.

        Throws:
            NotFoundException, if the Milestone could not be found.
        """
        self.gitea = repo.gitea
        self.__initialize_milestone(repo, id, initJson)

    def __initialize_milestone(self, repository, id, result):
        """ Initializes a Milestone.

        Args:
            repo (Repository): The Repository of this Milestone.
            id (int): The id of the Milestone.
            initJson (dict): Optional, init information for Milestone.

        Throws:
            NotFoundException, if the Milestone could not be found.
        """
        if not result:
            result = self.gitea.requests_get(
                Milestone.GET % (repository.owner.username, repository.name, id)
            )
        logging.debug(
            "Milestone found: %s/%s/%s: %s"
            % (repository.owner.username, repository.name, id, result["title"])
        )
        for i, v in result.items():
            setattr(self, i, v)
        self.repository = repository

    def __repr__(self):
        return "Milestone: '%s'" % self.title

    def full_print(self):
        return str(vars(self))


class Issue:
    """Reperestents an Issue in Gitea.
    """

    GET = """/repos/%s/%s/issues/%s"""  # <owner, repo, index>
    GET_TIME = """/repos/%s/%s/issues/%s/times"""  # <owner, repo, index>

    def __init__(self, repo: Repository, id: int, initJson: json = None):
        """ Initializes a Issue.

        Args:
            repo (Repository): The Repository of this Issue.
            id (int): The id of the Issue.
            initJson (dict): Optional, init information for Issue.

        Warning:
            This does not create an Issue. <sth> does.

        Throws:
            NotFoundException, if the Issue could not be found.
        """
        self.gitea = repo.gitea
        self.__initialize_issue(repo, id, initJson)

    def __initialize_issue(self, repository, id, result):
        """ Initializing an Issue.

        Args:
            repo (Repository): The Repository of this Issue.
            id (int): The id of the Issue.
            initJson (dict): Optional, init information for Issue.

        Throws:
            NotFoundException, if the Issue could not be found.
        """
        if not result:
            result = self.gitea.requests_get(
                Issue.GET % (repository.owner.username, repository.name, id)
            )
        logging.debug(
            "Issue found: %s/%s/%s: %s"
            % (repository.owner.username, repository.name, id, result["title"])
        )
        for i, v in result.items():
            setattr(self, i, v)
        self.repository = repository
        self.milestone = Milestone(repository, self.milestone["id"], self.milestone) if self.milestone else self.milestone

    def __eq__(self, other):
        if other is not None:
            if isinstance(other, Milestone):
                return other.id == self.id
        return False

    def __repr__(self):
        return "#%i %s" % (self.id, self.title)

    def get_estimate_sum(self):
        """Returns the summed estimate-labeled values"""
        return sum(
            map(
                lambda l: float(l["name"][10:]),
                filter(lambda l: l["name"][:10] == "estimate: ", self.labels),
            )
        )

    def get_time(self, user_id = None):
        """ Returns the summed time on this issue for this user."""
        return sum((t["time"] // 60) / 60 for t in self.gitea.requests_get(Issue.GET_TIME % (repository.owner.username, repository.name, id)) if user_id and t["user_id"] == user_id)


class Branch:
    """ Represents a Branch in the Gitea-instance.

    Attr:
        name: string
        commit: Commit
    """

    REPO_BRANCH = """/repos/%s/%s/branches/%s"""  # <owner>, <repo>, <ref>

    def __init__(self, repo: Repository, name: str, initJson: json = None):
        """ Initializes a Branch.

        Args:
            repo (Repository): The Repository of this Branch.
            name (str): The name of this Branch.
            initJson (dict): Optional, init information for Branch.

        Warning:
            This does not create a Branch. <sth> does.

        Throws:
            NotFoundException, if Branch could not be found.
        """
        self.gitea = repo.gitea
        self.__initialize_branch(repo, name, initJson)

    def __initialize_branch(self, repository, name, result):
        """ Initializing a Branch.

        Args:
            repository (Repository): The Repository of this Branch.
            name (str): The name of this Branch.
            result (dict): Optional, init information for Branch.

        Throws:
            NotFoundException, if Branch could not be found.
        """
        if not result:
            result = self.gitea.requests_get(
                Branch.REPO_BRANCH % (repository.owner.username, repository.name, name)
            )
        logging.debug(
            "Branch found: %s/%s/%s"
            % (repository.owner.username, repository.name, name)
        )
        for i, v in result.items():
            setattr(self, i, v)
        self.repository = repository


class Team:
    """ Represents a Team in the Gitea-instance.
    """

    # GET_TEAM = """/orgs/%s/teams"""
    GET_TEAM = """/teams/%s"""  # <id>
    ADD_USER = """/teams/%s/members/%s"""  # <id, username to add>
    ADD_REPO = """/teams/%s/repos/%s/%s"""  # <id, org, repo>
    TEAM_DELETE = """/teams/%s"""  # <id>
    GET_MEMBERS = """/teams/%s/members"""  # <id>
    GET_REPOS = """/teams/%s/repos"""  # <id>

    def __init__(self, org: Organization, name: str, initJson: json = None):
        """ Initializes Team.

        Args:
            org (Organization): Organization this team is part of.
            name (str): Name of the Team.
            initJson (dict): Optional, init information for Team.

        Warning:
            This does not create a Team. `gitea.create_team` does.

        Throws:
            NotFoundException, if Team could not be found.
        """
        self.gitea = org.gitea
        self.__initialize_team(org, name, initJson)

    def __initialize_team(self, org, name, result):
        """ Initializes Team.

        Args:
            org (Organization): Organization this team is part of.
            name (str): Name of the Team.
            result (dict): Optional, init information for Team.

        Throws:
            NotFoundException, if Team could not be found.
        """
        if not result:
            for team in org.get_teams():
                if team.name == name:
                    result = self.gitea.requests_get(Team.GET_TEAM % team.id)
                    logging.debug("Team found: %s/%s" % (org.username, name))
        if not result:
            logging.warning("Failed to find Team: %s/%s" % (org.username, name))
            raise NotFoundException("Team could not be Found")
        for i, v in result.items():
            setattr(self, i, v)
        self.organization = org

    def __repr__(self):
        """ Representation of a Team. Consisting of name and id.
        """
        return "Team: %s/%s (%s)" % (self.organization.username, self.name, self.id)

    def __eq__(self, other):
        if other is not None:
            if isinstance(other, Team):
                return other.id == self.id
        return False

    def add(self, toAdd):
        """ Adding User or Repository to Team.

        Args:
            toAdd (Repository/User): the object to add to this Team
        """
        if isinstance(toAdd, Repository):
            self.add_repo(toAdd)
            return
        if isinstance(toAdd, User):
            self.add_user(toAdd)
            return
        logging.error("Could not add %s" % str(toAdd))
        raise Exception("Could not add" + str(type(toAdd)))

    def add_user(self, user: User):
        """ Adding a User to this Team.

        Args:
            user (User): User to be added.
        """
        self.gitea.requests_put(Team.ADD_USER % (self.id, user.login))

    def add_repo(self, repo: Repository):
        """ Adding a Repository to this Team.

        Args:
            repo (Repository): Repository to be added.
        """
        self.gitea.requests_put(
            Team.ADD_REPO % (self.id, self.organization.username, repo.name)
        )

    def get_members(self):
        """ Get all members of this Team.

        Returns: [User]
            A list of Users in this Team.
        """
        results = self.gitea.requests_get(Team.GET_MEMBERS % self.id)
        return [
            User(self.gitea, result["username"], initJson=result) for result in results
        ]

    def get_repos(self):
        """ Get all repos of this Team.

        Returns: [Repository]
            A list of Repositories of this Team
        """
        results = self.gitea.requests_get(Team.GET_REPOS % self.id)
        return [
            Repository(self.gitea, self.organization, result["name"], initJson=result)
            for result in results
        ]

    def delete(self):
        """ Delete this Team.
        """
        self.gitea.requests_delete(Team.TEAM_DELETE % self.id)


class Gitea:
    """ Has Gitea-authenticated session. Can Create Users/Organizations/Teams/...

    Attr:
        A few. Look at them.
    """

    ADMIN_CREATE_USER = """/admin/users"""
    ADMIN_REPO_CREATE = """/admin/users/%s/repos"""  # <ownername>
    GITEA_VERSION = """/version"""
    GET_USER = """/user"""
    CREATE_ORG = """/admin/users/%s/orgs"""  # <username>
    CREATE_TEAM = """/orgs/%s/teams"""  # <orgname>

    def __init__(self, url, token):
        """ Initializing Gitea-instance.

        Args:
            url (str): URL of Gitea-server.
            token (str): Token of acting User.
        """
        self.headers = {
            "Authorization": "token " + token,
            "Content-type": "application/json",
        }
        self.url = url
        self.requests = requests

    def get_url(self, endpoint):
        """ Returns the full API-URL.

        Args:
            endpoint (str): Path to be added on API-Path.

        Returns: str
            Combined total API endpoint.
        """
        url = self.url + "/api/v1" + endpoint
        logging.debug("Url: %s" % url)
        return url

    @staticmethod
    def parse_result(result):
        """ Parses the result-JSON to a dict.

        Args:
            result (str): Result-Object from requests (library).

        Returns: dict
            Parsed from JSON
        """
        if result.text and len(result.text) > 3:
            return json.loads(result.text)
        return {}

    def requests_get(self, endpoint, params={}):
        """ Get parsed result from API-endpoint.

        Args:
            endpoint (str): Endpoint to request from.

        Returns: (dict)
            Parsed JSON-answer from the API.

        Throws:
            Exception, if answer status code is not ok.
        """
        request = self.requests.get(
            self.get_url(endpoint), headers=self.headers, params=params
        )
        if request.status_code not in [200, 201]:
            if request.status_code in [404]:
                raise NotFoundException()
            logging.error(
                "Received status code: %s (%s)" % (request.status_code, request.url)
            )
            if request.status_code in [403]:
                raise Exception(
                    "Unauthorized: %s - Check your permissions and try again!" % request.url
                )
            raise Exception(
                "Received status code: %s (%s)" % (request.status_code, request.url)
            )
        return self.parse_result(request)

    def requests_put(self, endpoint):
        """ Get parsed result from API-endpoint.

        Args:
            endpoint (str): Endpoint to request from.

        Throws:
            Exception, if answer status code is not ok.
        """
        request = self.requests.put(self.get_url(endpoint), headers=self.headers)
        if request.status_code not in [204]:
            logging.error(
                "Received status code: %s (%s) %s"
                % (request.status_code, request.url, request.text)
            )
            raise Exception(
                "Received status code: %s (%s) %s"
                % (request.status_code, request.url, request.text)
            )

    def requests_delete(self, endpoint):
        """ Get parsed result from API-endpoint.

        Args:
            endpoint (str): Endpoint to request from.

        Throws:
            Exception, if answer status code is not ok.
        """
        request = self.requests.delete(self.get_url(endpoint), headers=self.headers)
        if request.status_code not in [204]:
            logging.error(
                "Received status code: %s (%s)" % (request.status_code, request.url)
            )
            raise Exception(
                "Received status code: %s (%s) %s"
                % (request.status_code, request.url, vars(request))
            )

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
            self.get_url(endpoint), headers=self.headers, data=json.dumps(data)
        )
        if request.status_code not in [200, 201]:
            if (
                "already exists" in request.text
                or "e-mail already in use" in request.text
            ):
                logging.warning(request.text)
                raise AlreadyExistsException()
            logging.error(
                "Received status code: %s (%s)" % (request.status_code, request.url)
            )
            logging.error("With info: %s (%s)" % (data, self.headers))
            logging.error("Answer: %s" % request.text)
            raise Exception(
                "Received status code: %s (%s), %s"
                % (request.status_code, request.url, request.text)
            )

        return self.parse_result(request)

    def requests_patch(self, endpoint, data):
        """ Patch data to API-endpoint.

        Args:
            endpoint (str): endpoint of API to send data to
            data (dict): Data to patch.

        Returns: (dict)
            Parsed JSON-answer from the API. Usually it is empty.

        Throws:
            Exception, if status code not ok.
        """
        request = self.requests.patch(
            self.get_url(endpoint), headers=self.headers, data=json.dumps(data)
        )
        if request.status_code not in [200, 201]:
            logging.error(
                "Received status code: %s (%s) %s"
                % (request.status_code, request.url, data)
            )
            raise Exception(
                "Received status code: %s (%s) %s"
                % (request.status_code, request.url, request.text)
            )
        return self.parse_result(request)

    def get_users_search(self):
        path = "/users/search"
        return self.requests_get(path)

    def delete_repos(self, username, reponame):
        path = "/repos/" + username + "/" + reponame
        return self.requests.delete(path)

    def get_orgs_public_members_all(self, orgname):
        path = "/orgs/" + orgname + "/public_members"
        return self.requests_get(path)

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

    def get_user(self) -> User:
        result = self.requests_get(Gitea.GET_USER)
        return User(self, "UNINIT", initJson=result)

    def get_version(self) -> str:
        result = self.requests_get(Gitea.GITEA_VERSION)
        return result["version"]

    def create_user(
        self,
        userName: str,
        email: str,
        password: str,
        change_pw=True,
        sendNotify=True,
        sourceId=0,
    ) -> User:
        """ Create User.

        Args:
            userName (str): Name of the User that should be created.
            email (str): Email of the User that should be created.
            password (str): Password of the User that should be created.
            change_pw (bool): Optional, True, if the User should change his Password
            sendNotify (bool): Optional, True, if the User should be notified by Mail.
            sourceId (int): Optional, 0, source by which the User can authentificate himself against.

        Returns: User
            The newly created User.

        Throws:
            AlreadyExistsException, if the User exists already
            Exception, if something else went wrong.
        """
        result = self.requests_post(
            Gitea.ADMIN_CREATE_USER,
            data={
                "source_id": sourceId,
                "login_name": userName,
                "username": userName,
                "email": email,
                "password": password,
                "send_notify": sendNotify,
                "must_change_password": change_pw,
            },
        )
        if "id" in result:
            logging.info(
                "Successfully created User %s <%s> (id %s)"
                % (result["login"], result["email"], result["id"])
            )
        else:
            logging.error(result["message"])
            raise Exception("User not created... (gitea: %s)" % result["message"])
        return User(self, userName, result)

    def create_repo(
        self,
        repoOwner,
        repoName: str,
        description: str = "",
        private: bool = False,
        autoInit=True,
        gitignores=None,
        license=None,
        readme="Default",
    ) -> Repository:
        """ Create a Repository.

        Args:
            repoOwner (User/Organization): The owner of this Repository.
            repoName (str): The name of this Repository.
            description (str): Optional, None, short description of this Repository.
            private (bool): Optional, False, if this Repository should be private.
            autoInit (bool): Optional, True, if this Repository should auto-initialize.
            gitignores ([str]): Optional, None, list of gitignores to add.
            license (str): Optional, None, what sort of License to add.
            readme (str): Optional, 'Default', which Readme to initialize with.

        Returns: Repository
            The newly created Repository

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
                "readme": readme,
            },
        )
        if "id" in result:
            logging.info("Successfully created Repository %s " % result["name"])
        else:
            logging.error(result["message"])
            raise Exception("Repository not created... (gitea: %s)" % result["message"])
        return Repository(self, repoOwner, repoName, result)

    def create_org(
        self,
        owner: User,
        orgName: str,
        description: str,
        location="",
        website="",
        full_name="",
    ) -> Organization:
        """ Creates Organization.

        Args:
            owner (User): The User that will own this Organization.
            orgName (str): The name of the new Organization.
            description (str): Short description of the Organization.
            location (str): Optional, where the Organization is located.
            website (str): Optional, a website of this Organization.
            full_name (str): Optional, the full name of the Organization.

        Returns: Organization
            The newly created Organization.

        Throws:
            AlreadyExistsException, if this Organization already exists.
            Exception, if something else went wrong.
        """
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
            logging.info("Successfully created Organization %s" % result["username"])
        else:
            logging.error("Organization not created... (gitea: %s)" % result["message"])
            logging.error(result["message"])
            raise Exception(
                "Organization not created... (gitea: %s)" % result["message"]
            )
        return Organization(self, orgName, initJson=result)

    def create_team(
        self,
        org: Organization,
        name: str,
        description: str = "",
        permission: str = "read",
        units=[
            "repo.code",
            "repo.issues",
            "repo.ext_issues",
            "repo.wiki",
            "repo.pulls",
            "repo.releases",
            "repo.ext_wiki",
        ],
    ) -> Team:
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
            logging.info("Successfully created Team %s" % result["name"])
        else:
            logging.error("Team not created... (gitea: %s)" % result["message"])
            logging.error(result["message"])
            raise Exception("Team not created... (gitea: %s)" % result["message"])
        return Team(org, name, initJson=result)
