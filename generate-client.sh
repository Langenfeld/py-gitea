#!/bin/sh

# this code generates data models and api clients for using the allspice API
# this is an alternative to hand writting each api call but presummes the openapi / swagger step is complete

# in order to do this i updated the swagger api to an openapi like so
#
# curl -X 'GET' \
#  'https://converter.swagger.io/api/convert?url=https%3A%2F%2Fhub.allspice.io%2Fswagger.v1.json' \
#  -H 'accept: application/json' > allspice.openapi.json
#
# This only has to be done when the API changes. I also run a json formatter on it.

# Then I run it through the code generators
#
# each is slightly different but i will try to summarize
#
# datamodel-codegen -> generates models for the API but no HTTP stuff 
#
# fastapi-codegen -> uses datamodel-codegen to generate both the models and some HTTP stuff (server)
#
# openapi-python-client -> generates its own models (not datamodel-codegen) and HTTP stuff (client)

datamodel-codegen --input ./allspice.openapi.json --output datamodel-codegen/model.py

fastapi-codegen --input ./allspice.openapi.json --output fastapi

openapi-python-client generate --path ./allspice.openapi.json

# openapi-python-client is probably what we want for now, but a perfect solution would be something
# like the fastapi-codegen but for a client