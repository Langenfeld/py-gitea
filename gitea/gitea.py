import logging
import json
from typing import List, Dict, Union

from frozendict import frozendict
import requests
import urllib3

from .apiobject import User, Organization, Repository, Team
from .exceptions import NotFoundException, ConflictException, AlreadyExistsException


class Gitea:
    """ Object to establish a session with Gitea. """
    ADMIN_CREATE_USER = """/admin/users"""
    GET_USERS_ADMIN = """/admin/users"""
    ADMIN_REPO_CREATE = """/admin/users/%s/repos"""  # <ownername>
    GITEA_VERSION = """/version"""
    GET_USER = """/user"""
    CREATE_ORG = """/admin/users/%s/orgs"""  # <username>
    CREATE_TEAM = """/orgs/%s/teams"""  # <orgname>

    def __init__(
            self,
            gitea_url: str,
            token_text=None,
            auth=None,
            verify=True,
            log_level="INFO"
        ):
        """ Initializing Gitea-instance

        Args:
            gitea_url (str): The Gitea instance URL.
            token_text (str, None): The access token, by default None.
            auth (tuple, None): The user credentials
                `(username, password)`, by default None.
            verify (bool): If True, allow insecure server connections
                when using SSL.
            log_level (str): The log level, by default `INFO`.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.headers = {
            "Content-type": "application/json",
        }
        self.url = gitea_url
        self.requests = requests.Session()

        # Manage authentification
        if not token_text and not auth:
            raise ValueError("Please provide auth or token_text, but not both")
        if token_text:
            self.headers["Authorization"] = "token " + token_text
        if auth:
            self.requests.auth = auth

        # Manage SSL certification verification
        self.requests.verify = verify
        if not verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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

    def requests_get(self, endpoint: str, params=frozendict(), sudo=None):
        combined_params = {}
        combined_params.update(params)
        if sudo:
            combined_params["sudo"] = sudo.username
        request = self.requests.get(self.__get_url(endpoint), headers=self.headers, params=combined_params)
        if request.status_code not in [200, 201]:
            message = f"Received status code: {request.status_code} ({request.url})"
            if request.status_code in [404]:
                raise NotFoundException(message)
            if request.status_code in [403]:
                raise Exception(f"Unauthorized: {request.url} - Check your permissions and try again! ({message})")
            if request.status_code in [409]:
                raise ConflictException(message)
            raise Exception(message)
        return self.parse_result(request)

    def requests_get_paginated(self, endpoint: str, params=frozendict(), sudo=None, page_key: str = "page"):
        page = 1
        combined_params = {}
        combined_params.update(params)
        aggregated_result = []
        while True:
            combined_params[page_key] = page
            result = self.requests_get(endpoint, combined_params, sudo)
            if not result:
                return aggregated_result
            aggregated_result.extend(result)
            page += 1

    def requests_put(self, endpoint: str, data: dict = None):
        if not data:
            data = {}
        request = self.requests.put(self.__get_url(endpoint), headers=self.headers, data=json.dumps(data))
        if request.status_code not in [200, 204]:
            message = f"Received status code: {request.status_code} ({request.url}) {request.text}"
            self.logger.error(message)
            raise Exception(message)

    def requests_delete(self, endpoint: str):
        request = self.requests.delete(self.__get_url(endpoint), headers=self.headers)
        if request.status_code not in [204]:
            message = f"Received status code: {request.status_code} ({request.url})"
            self.logger.error(message)
            raise Exception(message)

    def requests_post(self, endpoint: str, data: dict):
        request = self.requests.post(self.__get_url(endpoint), headers=self.headers, data=json.dumps(data))
        if request.status_code not in [200, 201, 202]:
            if ("already exists" in request.text or "e-mail already in use" in request.text):
                self.logger.warning(request.text)
                raise AlreadyExistsException()
            self.logger.error(f"Received status code: {request.status_code} ({request.url})")
            self.logger.error(f"With info: {data} ({self.headers})")
            self.logger.error(f"Answer: {request.text}")
            raise Exception(f"Received status code: {request.status_code} ({request.url}), {request.text}")
        return self.parse_result(request)

    def requests_patch(self, endpoint: str, data: dict):
        request = self.requests.patch(self.__get_url(endpoint), headers=self.headers, data=json.dumps(data))
        if request.status_code not in [200, 201]:
            error_message = f"Received status code: {request.status_code} ({request.url}) {data}"
            self.logger.error(error_message)
            raise Exception(error_message)
        return self.parse_result(request)

    def get_orgs_public_members_all(self, orgname):
        path = "/orgs/" + orgname + "/public_members"
        return self.requests_get(path)

    def get_orgs(self):
        path = "/admin/orgs"
        results = self.requests_get(path)
        return [Organization.parse_response(self, result) for result in results]

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
            full_name: str = None,
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
        if not full_name:
            full_name = user_name
        request_data = {
            "source_id": source_id,
            "login_name": login_name,
            "full_name": full_name,
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
            repoOwner: Union[User, Organization],
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
        """ Create a Repository as the administrator

        Throws:
            AlreadyExistsException: If the Repository exists already.
            Exception: If something else went wrong.

        Note:
            Non-admin users can not use this method. Please use instead
            `gitea.User.create_repo` or `gitea.Organization.create_repo`.
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
                "default_branch": default_branch,
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
            can_create_org_repo: bool = False,
            includes_all_repositories: bool = False,
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
                "can_create_org_repo": can_create_org_repo,
                "includes_all_repositories": includes_all_repositories,
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
