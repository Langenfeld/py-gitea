from gitea import *

gitea = Gitea("https://test-gitea.something", "api-token")

##create Organization that does exist
org = Organization(gitea, "existing-organization")
print(org.name)
##create organization that does not exist
try:
    org = Organization(gitea, "non-existing-organization")
except:
    pass

##create a User that does exist
user = User(gitea, "existing-username")
print(user.name)
##create organization that does not exist
try:
    org = User(gitea, "non-existing-username")
except:
    pass

##get repositories set under a organization
repos = org.get_repositories()
print("org " + org.name + " has repositories " + str(repos))
##get repositories of a user
userRepos = user.get_repositories()
print("user " + user.name + " has repositories " + str(repos))

##create User
user2 = User.create_user(gitea, "torben-teststudent", "email@e-mail.de", "Torben der Teststudent", "testABCDEF",sendNotify=False)
print(user2.name)

##create Repository
Repository.create_repo(gitea, user , "test-repo-api", "this is an api test repo, delete this", True, True)
Repository.create_repo(gitea, org , "test-repo-api-org", "this is an api test repo, delete this", True, True)

