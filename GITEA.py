import json

import requests


class GITEA():
    def __init__(self, url, token):
        self.headers = {"Authorization": "token " + token}
        self.url = url
        self.requests = requests

    def get_url(self, endpoint):
        url = self.url + endpoint
        print(url)
        return url

    def parse_result(self, result):
        if (result.text and len(result.text) > 3):
            return json.loads(result.text)
        return {}

    def requests_get(self, endpoint):
        return self.parse_result(self.requests.get(self.get_url(endpoint), headers=self.headers))

    def requests_post(self, endpoint, data):
        return self.parse_result(self.requests.post(self.get_url(endpoint), headers=self.headers, data=data))

    def get_repos_search(self, q, uid, limit):
        path = '/repos/search'
        return self.requests_get(path)

    def get_users_gpg_keys(self, username):
        path = '/users/' + username + '/gpg_keys'
        return self.requests_get(path)

    def get_orgs_repos(self, orgname):
        path = '/orgs/' + orgname + '/repos'
        return self.requests_get(path)

    def put_user_starred(self, username, reponame):
        path = '/user/starred/' + username + '/' + reponame
        return self.requests.put(path)

    def delete_user_starred(self, username, reponame):
        path = '/user/starred/' + username + '/' + reponame
        return self.requests.delete(path)

    def get_user_starred(self, username, reponame):
        path = '/user/starred/' + username + '/' + reponame
        return self.requests_get(path)

    def get_users_search(self, ):
        path = '/users/search'
        return self.requests_get(path)

    def delete_repos(self, username, reponame):
        path = '/repos/' + username + '/' + reponame
        return self.requests.delete(path)

    def get_repos(self, username, reponame):
        path = '/repos/' + username + '/' + reponame
        return self.requests_get(path)

    def get_users_repos(self, username):
        path = '/users/' + username + '/repos'
        return self.requests_get(path)

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

    def get_user(self, ):
        path = '/user'
        return self.requests_get(path)

    def get_orgs_members_all(self, orgname):
        path = '/orgs/' + orgname + '/members'
        return self.requests_get(path)

    def patch_admin_users(self, source_id, login_name, full_name, email, password, website, location, active, admin,
                          allow_git_hook, allow_import_local, max_repo_creation, username):
        path = '/admin/users/' + username
        return self.requests.patch(path)

    def delete_admin_users(self, username):
        path = '/admin/users/' + username
        return self.requests.delete(path)

    def post_admin_users_keys(self, title, key, username):
        path = '/admin/users/' + username + '/keys'
        return self.requests_post(path, data={'title': title, 'key': key})

    def post_user_keys(self, title, key):
        path = '/user/keys'
        return self.requests_post(path, data={'title': title, 'key': key})

    def get_user_keys_all(self):
        path = '/user/keys'
        return self.requests_get(path)

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

    def post_admin_users(self, source_id, login_name, username, full_name, email, password, send_notify):
        path = '/admin/users'
        return self.requests_post(path, data={'source_id': source_id, 'login_name': login_name, 'username': username,
                                              'full_name': full_name, 'email': email, 'password': password,
                                              'send_notify': send_notify})

    def get_user_starred_all(self):
        path = '/user/starred'
        return self.requests_get(path)

    def get_users_followers(self, username):
        path = '/users/' + username + '/followers'
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

    def get_user_following_all(self, ):
        path = '/user/following'
        return self.requests_get(path)

    def get_user_followers(self, ):
        path = '/user/followers'
        return self.requests_get(path)

    def post_admin_users_repos(self, name, description, private, auto_init, gitignores, license, readme, username):
        path = '/admin/users/' + username + '/repos'
        return self.requests_post(path, data={'name': name, 'description': description, 'private': private,
                                              'auto_init': auto_init, 'gitignores': gitignores, 'license': license,
                                              'readme': readme})

    def patch_orgs_hooks(self, config, events, active, orgname, id):
        path = '/orgs/' + orgname + '/hooks/' + id
        return self.requests.patch(path)

    def delete_orgs_hooks(self, orgname, id):
        path = '/orgs/' + orgname + '/hooks/' + id
        return self.requests.delete(path)

    def get_orgs_hooks(self, orgname, id):
        path = '/orgs/' + orgname + '/hooks/' + id
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

    def get_user_repos(self, ):
        path = '/user/repos'
        return self.requests_get(path)

    def delete_user_gpg_keys(self, id):
        path = '/user/gpg_keys/' + id
        return self.requests.delete(path)

    def get_user_gpg_keys(self, id):
        path = '/user/gpg_keys/' + id
        return self.requests_get(path)

    def get_version(self):
        path = '/version'
        return self.requests_get(path)
