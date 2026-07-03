# py-gitea

A simple API client for Gitea > 1.24 based on the idea that passing around 
dictionaries and strings is disgusting and needs to be wrapped in something safe.
So, the whole implementation is focused
on making access and working with Organizations, Teams, Repositories and Users as pain
free as possible.

Most functions should be covered by tests or should be in use (somewhere) so things should work as expected. 
Note that not the full Swagger-API is accessible. 

Originally forked from https://github.com/m301/py-gitea.

## Usage

First get a `gitea` object wrapping access and authentication (via an api token) for your gitea instance:

```python
from gitea import *

gitea = Gitea(URL, TOKEN)
```

Operations like requesting the Gitea version or authentication user can be done directly from the `gitea` object:

```python
print("Gitea Version: " + gitea.get_version())
print("API-Token belongs to user: " + gitea.get_user().username)
```

Adding entities like Users, Organizations, ... also is done via the gitea object.

```python
user = gitea.create_user("Test Testson", "test@test.test", "password")
```

All operations on entities in gitea are then accomplished via the according wrapper objects for those entities.
Each of those objects has a `.request` method that creates an 
entity according to your gitea instance

```python
other_user = User.request(gitea, "OtherUserName")
print(other_user.username)
```
or can be requested from other entities.

```python
orgs = user.get_orgs()
print(f"{user.name} is in orgarnisations {orgs}")
```

Note that the fields of the User, Organization,... classes are dynamically created at runtime, and thus not visible
during divelopment. Refer to the Gitea-API documentation for the fields names.

Fields that can not be altered via gitea-api, are read only. After altering a field, the `.commit` method of the
according object must be called to synchronize the changed fields with your gitea instance.

```python
org = Organization.request(gitea, test_org)
org.description = "some new description"
org.location = "some new location"
org.commit()
```

An entity in gitea can be deleted by calling delete.

```python
org.delete()
```

All entity objects do have methods to execute some of the requests possible though the gitea-api:

```python
org = Organization.request(gitea, ORGNAME)
teams = org.get_teams()
for team in teams:
    repos = team.get_repos()
    for repo in repos:
        print(repo.name)
```

If something is missing, feel free to add it :).

## Installation

Use ``pip install py-gitea`` to install.

## Tests

Tests can be run with:

```python3 -m pytest test_api.py```

Make sure to have a gitea-instance running on `http://localhost:3000`, and an admin-user token at `.token`.
The admin user must be named ``test``, with email ``secondarytest@test.org``.
