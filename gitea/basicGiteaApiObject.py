from .exceptions import ObjectIsInvalid, MissiongEqualyImplementation


class BasicGiteaApiObject:
    GET_API_OBJECT = "FORMAT/STINING/{argument}"
    PATCH_API_OBJECT = "FORMAT/STINING/{argument}"

    def __init__(self, gitea):
        self.gitea = gitea
        self.deleted = False  # set if .delete was called, so that an exception is risen
        self.dirty_fields = set()

    def __str__(self):
        return "GiteaAPIObject (%s):" % (type(self))

    def __eq__(self, other):
        """Compare only fields that are part of the gitea-data"""
        raise MissiongEqualyImplementation()


    fields_to_parsers = {}

    def commit(self):
        raise NotImplemented()

    def get_dirty_fields(self):
        return {name: getattr(self, name) for name in self.dirty_fields}

    @classmethod
    def parse_response(cls, gitea, result) -> "BasicGiteaApiObject":
        # gitea.logger.debug("Found api object of type %s (id: %s)" % (type(cls), id))
        api_object = cls(gitea)
        cls._initialize(gitea, api_object, result)
        return api_object

    @classmethod
    def _get_gitea_api_object(cls, gitea, args):
        """Retrieving an object always as GET_API_OBJECT """
        return gitea.requests_get(cls.GET_API_OBJECT.format(**args))

    patchable_fields = set()

    @classmethod
    def _initialize(cls, gitea, api_object, result):
        for name, value in result.items():
            if name in cls.fields_to_parsers and value is not None:
                parse_func = cls.fields_to_parsers[name]
                value = parse_func(gitea, value)
            if name in cls.patchable_fields:
               cls._add_property(name, value, api_object)
            else:
                cls._add_readonly_property(name,value,api_object)
        # add all patchable fields missing in the request to be writable
        for name in cls.patchable_fields:
            if not hasattr(api_object,name):
                cls._add_property(name, None, api_object)
        for name in cls.fields_to_parsers.keys():
            if not hasattr(api_object,name):
                cls._add_readonly_property(name, None, api_object)

    @classmethod
    def _add_property(cls, name, value, api_object):
        if not hasattr(api_object, name):
            prop = property(
                (lambda name: lambda self: self.__get_var(name))(name),
                (lambda name: lambda self, v: self.__set_var(name, v))(name))
            setattr(cls, name, prop)
            setattr(api_object, "_" + name, value)

    @classmethod
    def _add_readonly_property(cls, name, value, api_object):
        if not hasattr(api_object, name):
            prop = property(
                (lambda name: lambda self: self.__get_var(name))(name))
            setattr(cls, name, prop)
            setattr(api_object, "_" + name, value)

    def __set_var(self, name, i):
        if self.deleted:
            raise ObjectIsInvalid()
        self.dirty_fields.add(name)
        setattr(self, "_" + name, i)

    def __get_var(self, name):
        if self.deleted:
            raise ObjectIsInvalid()
        return getattr(self, "_" + name)
