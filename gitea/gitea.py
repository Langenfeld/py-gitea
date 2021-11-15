import json
import logging
from typing import List, Dict

import requests
from httpcache import CachingHTTPAdapter

from .exceptions import NotFoundException, ConflictException, AlreadyExistsException
from .apiobject import User, Organization, Repository, Team

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
