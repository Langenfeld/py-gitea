#!/usr/bin/env python
"""Fixtures for testing py-gitea

Instructions
------------
put a ".token" file into your directory containg only the token for gitea

"""

import os

import pytest

from gitea import Gitea

@pytest.fixture
def instance(scope="module"):
    try:
        url = os.getenv("PY_GITEA_URL")
        token = os.getenv("PY_GITEA_TOKEN")
        auth = os.getenv("PY_GITEA_AUTH")
        if not url:
            raise ValueError("No Gitea URL was provided")
        if token and auth:
            raise ValueError("Please provide auth or token_text, but not both")
        g = Gitea(url, token_text=token, auth=auth, verify=False)
        print("Gitea Version: " + g.get_version())
        print("API-Token belongs to user: " + g.get_user().username)
        return g
    except:
        assert (
            False
        ), "Gitea could not load. \
                - Instance running at http://localhost:3000 \
                - Token at .token   \
                    ?"
