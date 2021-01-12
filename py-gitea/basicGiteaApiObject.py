from .exceptions import ObjectIsInvalid


class BasicGiteaApiObject:
    GET_API_OBJECT = "FORMAT/STINING/{argument}"
    PATCH_API_OBJECT = "FORMAT/STINING/{argument}"

    def __init__(self, gitea, id):
        self.__id = id
        self.gitea = gitea
        self.deleted = False  # set if .delete was called, so that an exception is risen
        self.dirty_fields = set()

    def __eq__(self, other):
        return other.id == self.id if isinstance(other, type(self)) else False

    def __str__(self):
        return "GiteaAPIObject (%s) id: %s" % (type(self), self.id)

    def __hash__(self):
        return self.id

    fields_to_parsers = {}

    def commit(self):
        """ TODO: evaluate if there is a generalizable version of this method
        """
        raise NotImplemented()

    def get_dirty_fields(self):
        return {name: getattr(self, name) for name in self.dirty_fields}

    @classmethod
    def parse_response(cls, gitea, result):
        if "id" in result:
            id = int(result["id"])
        else:
            id = hash(result.items)
        # gitea.logger.debug("Found api object of type %s (id: %s)" % (type(cls), id))
        api_object = cls(gitea, id=id)
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
                prop = property(
                    (lambda name: lambda self: self.__get_var(name))(name),
                    (lambda name: lambda self, v: self.__set_var(name, v))(name))
            else:
                prop = property(
                    (lambda name: lambda self: self.__get_var(name))(name))
            setattr(cls, name, prop)
            setattr(api_object, "_" + name, value)
        # add all patchable fields to be watched if changed
        for name in cls.patchable_fields:
            if not hasattr(api_object,name):
                prop = property(
                    (lambda name: lambda self: self.__get_var(name))(name),
                    (lambda name: lambda self, v: self.__set_var(name, v))(name))
                setattr(cls, name, prop)
                setattr(api_object, "_" + name, None)


    def __set_var(self, name, i):
        if self.deleted:
            raise ObjectIsInvalid()
        self.dirty_fields.add(name)
        setattr(self, "_" + name, i)

    def __get_var(self, name):
        if self.deleted:
            raise ObjectIsInvalid()
        return getattr(self, "_" + name)
