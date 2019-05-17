# py-gitea

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)


A very simple API client for Gitea (`1.8.0-rc2`)

This has been somewhat tested (and used!), so most things should work as expected.

Note that not the full Swagger-API is accessible. The implemented part is
focused on Organization/Team/Repository/User-creation, also putting users in
Teams in Organizations and adding Repositories to Teams. Sadly the API does not
do all of what I wanted to use. Still, it should be pretty easy to add almost
all API-calls.


# tests
Can be run like this:

```python3 -m pytest tests.py```

Make sure to have a gitea-instance running on `http://localhost:3000`, and an admin-user token at `.token`.
