import json
import requests
import logging


class Organization:

    ORG_REQUEST = """/orgs/%s""" #<org>
    ORG_REPOS_REQUEST = """/orgs/%s/repos""" #<org>
    ORG_TEAMS_REQUEST = """/orgs/%s/teams""" #<org>
    ORG_PATCH = """/orgs/%s""" #<org>

    def __init__(self, gitea, orgName : str, initJson: json = None):
        self.gitea = gitea
        self.username = "UNINIT"
        self.__initialize_org(orgName, initJson)

    def get_repositories(self):
        results = self.gitea.requests_get(Organization.ORG_TEAMS_REQUEST%self.username)
        return [Repository(self.gitea, self, result["name"], initJson=result) for result in results]

    def get_teams(self):
        results = self.gitea.requests_get(Organization.ORG_TEAMS_REQUEST % self.username)
        return [Team(self, result["name"], initJson=result) for result in results]

    def __initialize_org(self, orgName: str, result) -> None:
        if not result:
            result = self.gitea.requests_get(Organization.ORG_REQUEST%orgName)
        logging.info("Found Orgranization: %s"%orgName)
        for i,v in result.items(): setattr(self, i, v)

    def set_value(self, values: dict):
        result = self.gitea.requests_patch(Organization.ORG_PATCH%self.username, data=values)
        self.__initialize_org(self.username, result)

class User:

    USER_REQUEST = """/users/%s""" #<org>
    USER_REPOS_REQUEST = """/users/%s/repos""" #<org>
    USER_PATCH = """/admin/users/%s""" # <username>
    ADMIN_DELETE_USER = """/admin/users/%s""" # <username>

    def __init__(self, gitea, userName : str, initJson: json = None):
        self.gitea = gitea
        self.username = "UNINIT"
        self.__initialize_user(userName, initJson)

    def get_repositories(self):
        result = self.gitea.requests_get(User.USER_REPOS_REQUEST%self.username)
        return [Repository(self.gitea, self.username, r["name"]) for r in result]

    def __initialize_user(self, userName: str, result) -> None:
        if not result:
            result = self.gitea.requests_get(User.USER_REQUEST % userName)
        logging.info("Found User: %s"%userName)
        for i, v in result.items(): setattr(self, i, v)

    def set_value(self, email: str, values: dict):
        #the request requires email to be set...
        values["email"] = email
        result = self.gitea.requests_patch(User.USER_PATCH%self.username, data=values)
        self.__initialize_user(self.username, result)

    def delete(self):
        result = self.gitea.requests_delete(User.ADMIN_DELETE_USER%self.username)


class Repository:

    REPO_REQUEST = """/repos/%s/%s"""   #<ownername>,<reponame>
    REPO_SEARCH ="""/repos/search/%s""" # <reponame>
    REPO_BRANCHES = """/repos/%s/%s/branches""" #<owner>, <reponame>

    def __init__(self, gitea, repoOwner, repoName: str, initJson: json = None):
        self.gitea = gitea
        self.name = "UNINIT"
        self.__initialize_repo(repoOwner, repoName, initJson)

    def __initialize_repo(self, repoOwner, repoName: str, result):
        if not result:
            result = self.gitea.requests_get(Repository.REPO_REQUEST % (repoOwner.username,repoName))
        logging.info("Found Repository: %s/%s" % (repoOwner.username, repoName))
        for i, v in result.items(): setattr(self, i, v)
        self.owner = repoOwner

    def get_branches(self):
        results = self.gitea.requests_get(Repository.REPO_BRANCHES%(self.owner.username, self.name))
        return [Branch(self, result["name"], result) for result in results]


class Branch:

    REPO_BRANCH = """/repos/%s/%s/branches/%s""" # <owner>, <repo>, <ref>

    def __init__(self, repo: Repository, name: str, initJson: json = None):
        self.gitea = repo.gitea
        self.__initialize_branch(repo, name, initJson)

    def __initialize_branch(self, repository, name, result):
        if not result:
            result = self.gitea.requests_get(Branch.REPO_BRANCH %
                                             (repository.owner.username, repository.name, name))
        logging.info("Branch found: %s/%s/%s" % (repository.owner.username, repository.name, name))
        for i, v in result.items(): setattr(self, i, v)
        self.repository = repository

class Team:

    def __init__(self, org: Organization, name: str, initJson: json = None):
        self.gitea = org.gitea
        self.__initialize_repo(org, name, initJson)

    def __initialize_repo(self, org, name, result):
        if not result:
            raise NotImplementedError("TODO")
        logging.info("Team found: %s/%s" % (org.username, name))
        for i, v in result.items(): setattr(self, i, v)
        self.organization = org


class Gitea():

    ADMIN_CREATE_USER = """/admin/users"""
    ADMIN_REPO_CREATE = """/admin/users/%s/repos""" # <ownername>
    GITEA_VERSION = """/version"""
    GET_USER = """/user"""

    """
    @:param url: url of Gitea server without  .../api/<version>
    """
    def __init__(self, url, token):
        self.headers = {"Authorization": "token " + token}
        self.url = url
        self.requests = requests

    def get_url(self, endpoint):
        url = self.url + "/api/v1" + endpoint
        logging.info(url)
        return url

    def parse_result(self, result):
        if (result.text and len(result.text) > 3):
            return json.loads(result.text)
        return {}

    def requests_get(self, endpoint):
        request = self.requests.get(self.get_url(endpoint), headers=self.headers)
        if request.status_code not in [200,201]:
            logging.error("Received status code: %s (%s)"%(request.status_code, request.url))
            raise Exception(("Received status code: %s (%s)"%(request.status_code, request.url)))
        return self.parse_result(request)

    def requests_delete(self, endpoint):
        request = self.requests.delete(self.get_url(endpoint), headers=self.headers)
        if request.status_code not in [204]:
            logging.error("Received status code: %s (%s)"%(request.status_code, request.url))
            raise Exception(("Received status code: %s (%s)"%(request.status_code, request.url)))

    def requests_post(self, endpoint, data):
        request = self.requests.post(self.get_url(endpoint), headers=self.headers, data=data)
        if request.status_code not in [200, 201]:
            logging.error("Received status code: %s (%s)"%(request.status_code, request.url))
            raise Exception(("Received status code: %s (%s)"%(request.status_code, request.url)))
        return self.parse_result(request)

    def requests_patch(self, endpoint, data):
        request = self.requests.patch(self.get_url(endpoint), headers=self.headers, data=data)
        if request.status_code not in [200, 201]:
            logging.error("Received status code: %s (%s)"%(request.status_code, request.url))
            raise Exception(("Received status code: %s (%s)"%(request.status_code, request.url)))
        return self.parse_result(request)

    def get_users_gpg_keys(self, username):
        path = '/users/' + username + '/gpg_keys'
        return self.requests_get(path)

    def get_users_search(self, ):
        path = '/users/search'
        return self.requests_get(path)

    def delete_repos(self, username, reponame):
        path = '/repos/' + username + '/' + reponame
        return self.requests.delete(path)

    def post_repos__mirror_sync(self, username, reponame):
        path = '/repos/' + username + '/' + reponame + '/mirror-sync'
        return self.requests_post(path, data={})

    def post_admin_users_orgs(self, username, full_name, description, website, location):
        path = '/admin/users/' + username + '/orgs'
        return self.requests_post(path, data={'username': username, 'full_name': full_name, 'description': description,
                                              'website': website, 'location': location})

    def post_user_gpg_keys(self, armored_public_key):
        path = '/user/gpg_keys'
        return self.requests_post(path, data={'armored_public_key': armored_public_key})

    def get_user_gpg_keys_all(self):
        path = '/user/gpg_keys'
        return self.requests_get(path)

    def get_user_subscriptions(self, ):
        path = '/user/subscriptions'
        return self.requests_get(path)

    def post_markdown(self, Text, Mode, Context, Wiki):
        path = '/markdown'
        return self.requests_post(path, data={'Text': Text, 'Mode': Mode, 'Context': Context, 'Wiki': Wiki})

    def patch_repos__hooks(self, config, events, active, username, reponame, id):
        path = '/repos/' + username + '/' + reponame + '/hooks/' + id
        return self.requests.patch(path)

    def delete_repos_hooks(self, username, reponame, id):
        path = '/repos/' + username + '/' + reponame + '/hooks/' + id
        return self.requests.delete(path)


    def get_users_keys(self, username):
        path = '/users/' + username + '/keys'
        return self.requests_get(path)

    def put_user_following(self, username):
        path = '/user/following/' + username
        return self.requests.put(path)

    def delete_user_following(self, username):
        path = '/user/following/' + username
        return self.requests.delete(path)

    def get_user_following(self, username):
        path = '/user/following/' + username
        return self.requests_get(path)

    def post_markdown_raw(self, ):
        path = '/markdown/raw'
        return self.requests_post(path, data={})

    def get_users_subscriptions(self, username):
        path = '/users/' + username + '/subscriptions'
        return self.requests_get(path)

    def delete_user_keys(self, id):
        path = '/user/keys/' + id
        return self.requests.delete(path)

    def get_user_keys(self, id):
        path = '/user/keys/' + id
        return self.requests_get(path)

    def post_orgs_hooks(self, type, config, events, active, orgname):
        path = '/orgs/' + orgname + '/hooks/'
        return self.requests_post(path, data={'type': type, 'config': config, 'events': events, 'active': active})

    def get_orgs_members_all(self, orgname):
        path = '/orgs/' + orgname + '/members'
        return self.requests_get(path)

    def post_admin_users_keys(self, title, key, username):
        path = '/admin/users/' + username + '/keys'
        return self.requests_post(path, data={'title': title, 'key': key})

    def get_users_tokens(self, username):
        path = '/users/' + username + '/tokens'
        return self.requests_get(path)

    def get_orgs_hooks_all(self, orgname):
        path = '/orgs/' + orgname + '/hooks'
        return self.requests_get(path)

    def get_users(self, username):
        path = '/users/' + username
        return self.requests_get(path)

    def get_orgs_public_members_all(self, orgname):
        path = '/orgs/' + orgname + '/public_members'
        return self.requests_get(path)

    def post_repos__forks(self, organization, repo, owner):
        path = '/repos/' + owner + '/' + repo + '/forks'
        return self.requests_post(path, data={'organization': organization})

    def get_repos_forks(self, repo, owner):
        path = '/repos/' + owner + '/' + repo + '/forks'
        return self.requests_get(path)

    def get_repositories(self, id):
        path = '/repositories/' + id
        return self.requests_get(path)

    def put_repos__subscription(self, username, reponame):
        path = '/repos/' + username + '/' + reponame + '/subscription'
        return self.requests.put(path)

    def delete_repos_subscription(self, username, reponame):
        path = '/repos/' + username + '/' + reponame + '/subscription'
        return self.requests.delete(path)

    def get_repos_subscription(self, username, reponame):
        path = '/repos/' + username + '/' + reponame + '/subscription'
        return self.requests_get(path)

    def get_users_following(self, username):
        path = '/users/' + username + '/following'
        return self.requests_get(path)

    def get_users_starred(self, username):
        path = '/users/' + username + '/starred'
        return self.requests_get(path)

    def put_orgs_public_members(self, username, orgname):
        path = '/orgs/' + orgname + '/public_members/' + username
        return self.requests.put(path)

    def delete_orgs_public_members(self, username, orgname):
        path = '/orgs/' + orgname + '/public_members/' + username
        return self.requests.delete(path)

    def get_orgs_public_members(self, username, orgname):
        path = '/orgs/' + orgname + '/public_members/' + username
        return self.requests_get(path)

    def post_org_repos(self, name, description, private, auto_init, gitignores, license, readme, org):
        path = '/org/' + org + '/repos'
        return self.requests_post(path, data={'name': name, 'description': description, 'private': private,
                                              'auto_init': auto_init, 'gitignores': gitignores, 'license': license,
                                              'readme': readme})

    def delete_orgs_members(self, orgname, username):
        path = '/orgs/' + orgname + '/members/' + username
        return self.requests.delete(path)

    def get_orgs_members(self, orgname, username):
        path = '/orgs/' + orgname + '/members/' + username
        return self.requests_get(path)

    def post_repos__hooks(self, type, config, events, active, reponame, username):
        path = '/repos/' + username + '/' + reponame + '/hooks'
        return self.requests_post(path, data={'type': type, 'config': config, 'events': events, 'active': active})

    def get_repos_hooks(self, reponame, username):
        path = '/repos/' + username + '/' + reponame + '/hooks'
        return self.requests_get(path)

    def post_repos_migrate(self, clone_addr, auth_username, auth_password, uid, repo_name, mirror, private,
                           description):
        path = '/repos/migrate'
        return self.requests_post(path, data={'clone_addr': clone_addr, 'auth_username': auth_username,
                                              'auth_password': auth_password, 'uid': uid, 'repo_name': repo_name,
                                              'mirror': mirror, 'private': private, 'description': description})

    def post_user_repos(self, name, description, private, auto_init, gitignores, license, readme):
        path = '/user/repos'
        return self.requests_post(path, data={'name': name, 'description': description, 'private': private,
                                              'auto_init': auto_init, 'gitignores': gitignores, 'license': license,
                                              'readme': readme})

    def delete_user_gpg_keys(self, id):
        path = '/user/gpg_keys/' + id
        return self.requests.delete(path)

    def get_user_gpg_keys(self, id):
        path = '/user/gpg_keys/' + id
        return self.requests_get(path)

    # # #

    def get_user(self, ):
        result = self.requests_get(Gitea.GET_USER)
        return User(self, "UNINIT", initJson=result)

    def get_version(self):
        result = self.requests_get(Gitea.GITEA_VERSION)
        return result["version"]

    def create_user(self, userName: str, email: str, fullName: str, password: str, sendNotify = True, sourceId = 0):
        result = self.requests_post(Gitea.ADMIN_CREATE_USER,
            data={'source_id': sourceId, 'login_name': userName, 'username': userName, 'full_name': fullName,
            'email': email, 'password': password, 'send_notify': sendNotify})
        if "id" in result:
            logging.info("Successfully created User %s (id %s)"%(result["login"], result["id"]))
        else:
            logging.error(result["message"])
            raise Exception("User not created... (gitea: %s)"%result["message"])
        return User(self, userName, result)

    def create_repo(self, repoOwner, repoName: str, description: str, private: bool, autoInit = True, gitignores = None, license= None, readme = "Default"):
        assert(isinstance(repoOwner, User) or isinstance(repoOwner, Organization)) # although this only says user in the api, this also works for organizations
        result = self.requests_post(Gitea.ADMIN_REPO_CREATE%repoOwner.username,
            data={'name': repoName, 'description': description, 'private': private,
                                              'auto_init': autoInit, 'gitignores': gitignores, 'license': license, 'readme': readme})
        if "id" in result:
            logging.info("Successfully created Repository %s "%(result["name"]))
        else:
            logging.error(result["message"])
            raise Exception("Repository not created... (gitea: %s)"%(result["message"]))
        return Repository(self, repoOwner, repoName, result)
