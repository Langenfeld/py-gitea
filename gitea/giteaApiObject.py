from .basicGiteaApiObject import BasicGiteaApiObject
import logging

class GiteaApiObject(BasicGiteaApiObject):

    GET_API_OBJECT = "FORMAT/STINING/{argument}"
    PATCH_API_OBJECT = "FORMAT/STINING/{argument}"

    def __init__(self, gitea, id):
        super(GiteaApiObject, self).__init__(gitea, id)

    @classmethod
    def request(cls, gitea, id):
        """Use for ginving a nice e.g. 'request(gita, orgname, repo, ticket)'.
        All args are put into an args tuple for passing around"""
        return cls._request(gitea, {"id": id})

    @classmethod
    def _request(cls, gitea, args):
        result = cls._get_gitea_api_object(gitea, args)
        api_object = cls.parse_response(gitea, result)
        for key, value in args.items(): # hack: not all necessary request args in api result (e.g. repo name in issue)
            if not hasattr(api_object, key):
                setattr(api_object, key, value)
        return api_object