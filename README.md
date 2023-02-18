# py-allspice

A very simple API client for AllSpice Hub

Note that not the full Swagger-API is accessible. The whole implementation is focused 
on making access and working with Organizations, Teams, Repositories and Users as pain
free as possible.

Forked from https://github.com/Langenfeld/py-gitea.

## Usage

First get an `allspice` object wrapping access and authentication (via an api token) for your gitea instance:

```python
from gitea import *

allspice = Gitea(URL, TOKEN)
```

Operations like requesting the Allspice version or authentication user can be requested directly from the `allspice` object:

```python
print("AllSpice Version: " + allspice.get_version())
print("API-Token belongs to user: " + allspice.get_user().username)
```

Adding entities like Users, Organizations, ...  also is done via the allspice object.

```python
user = allspice.create_user("Test Testson", "test@test.test", "password")
```

All operations on entities in allspice are then accomplished via the according wrapper objects for those entities.
Each of those objects has a `.request` method that creates an entity according to your allspice instance. 

```python
other_user = User.request(allspice, "OtherUserName")
print(other_user.username)
```

Note that the fields of the User, Organization,... classes are dynamically created at runtime, and thus not visible during divelopment. Refer to the AllSpice-API documentation for the fields names. 


Fields that can not be altered via allspice-api, are read only. After altering a field, the `.commit` method of the according object must be called to synchronize the changed fields with your allspice instance.

```python
org = Organization.request(allspice, test_org)
org.description = "some new description"
org.location = "some new location"
org.commit()
```

An entity in allspice can be deleted by calling delete.
```python
org.delete()
```

All entity objects do have methods to execute some of the requests possible though the allspice-api:
```python
org = Organization.request(allspice, ORGNAME)
teams = org.get_teams()
for team in teams:
	repos = team.get_repos()
	for repo in repos:
		print(repo.name)
```


## Installation

Use ``pip install py-allspice`` to install.

## Tests

Tests can be run with: 

```python3 -m pytest test_api.py```

Make sure to have a allspice-instance running on `http://localhost:3000`, and an admin-user token at `.token`. 
The admin user must be named ``test``, with email ``secondarytest@test.org``.
