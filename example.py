import os

from gitea import *

gitea = Gitea("https://test-gitea.something", "api-token")
print("Gitea Version: " + gitea.get_version())
print("API-Token belongs to user: " + gitea.get_user().username)

##get an organization that does exist
org = Organization(gitea, "an-org")
print(org.username)
org.set_value({"location": "a-place"})
print([user.username for user in org.get_members()])
## try getting an organization that does not exists
try:
    org = Organization(gitea, "non-existent-org")
except:
    pass

##get a User that does exist
user = User(gitea, "a-user")
print(user.username)
##try getting organization that does not exist
try:
    user = User(gitea, "non-existent-user")
except:
    pass
user.set_value(user.email, {"location": "an-location"})
##get repositories set under a organization
repos = org.get_repositories()
print("org " + org.username + " has repositories " + str(repos))
##get repositories of a user
userRepos = user.get_repositories()
print("user " + user.username + " has repositories " + str(repos))
##get branches
repo = Repository(gitea, org,"playground")
print([b.name for b in repo.get_branches()])

##create Repository
gitea.create_repo(user , "test-repo-api", "this is an api test repo, delete this", True, True)
gitea.create_repo(org , "test-repo-api-org", "this is an api test repo, delete this", True, True)

## create user
newUser = gitea.create_user("test-test", "test@testing.de","Torben der Tester", str(os.urandom(32)), False)
print(newUser.username)
newUser.delete()

