from .exceptions import (
    ObjectIsInvalid,
    MissiongEqualyImplementation,
    RawRequestEndpointMissing,
)


class ReadonlyApiObject:
    def __init__(self, gitea):
        self.gitea = gitea
        self.deleted = False  # set if .delete was called, so that an exception is risen

    def __str__(self):
        return "GiteaAPIObject (%s):" % (type(self))

    def __eq__(self, other):
        """Compare only fields that are part of the gitea-data identity"""
        raise MissiongEqualyImplementation()

    def __hash__(self):
        """Hash only fields that are part of the gitea-data identity"""
        raise MissiongEqualyImplementation()

    _fields_to_parsers = {}

    @classmethod
    def request(cls, gitea):
        if hasattr("API_OBJECT", cls):
            return cls._request(gitea)
        else:
            raise RawRequestEndpointMissing()

    @classmethod
    def _request(cls, gitea, args):
        result = cls._get_gitea_api_object(gitea, args)
        api_object = cls.parse_response(gitea, result)
        return api_object

    @classmethod
    def _get_gitea_api_object(cls, gitea, args):
        """Retrieving an object always as GET_API_OBJECT"""
        return gitea.requests_get(cls.API_OBJECT.format(**args))

    @classmethod
    def parse_response(cls, gitea, result) -> "ReadonlyApiObject":
        # gitea.logger.debug("Found api object of type %s (id: %s)" % (type(cls), id))
        api_object = cls(gitea)
        cls._initialize(gitea, api_object, result)
        return api_object

    @classmethod
    def _initialize(cls, gitea, api_object, result):
        for name, value in result.items():
            if name in cls._fields_to_parsers and value is not None:
                parse_func = cls._fields_to_parsers[name]
                value = parse_func(gitea, value)
            cls._add_read_property(name, value, api_object)
        # add all patchable fields missing in the request to be writable
        for name in cls._fields_to_parsers.keys():
            if not hasattr(api_object, name):
                cls._add_read_property(name, None, api_object)

    @classmethod
    def _add_read_property(cls, name, value, api_object):
        if not hasattr(api_object, name):
            setattr(api_object, "_" + name, value)
            prop = property((lambda n: lambda self: self._get_var(n))(name))
            setattr(cls, name, prop)
        else:
            raise AttributeError(f"Attribute {name} already exists on api object.")

    def _get_var(self, name):
        if self.deleted:
            raise ObjectIsInvalid()
        return getattr(self, "_" + name)


class ApiObject(ReadonlyApiObject):
    _patchable_fields = set()

    def __init__(self, gitea):
        super().__init__(gitea)
        self._dirty_fields = set()

    def commit(self):
        raise NotImplemented()

    _parsers_to_fields = {}

    def get_dirty_fields(self):
        dirty_fields_values = {}
        for field in self._dirty_fields:
            value = getattr(self, field)
            if field in self._parsers_to_fields:
                dirty_fields_values[field] = self._parsers_to_fields[field](value)
            else:
                dirty_fields_values[field] = value
        return dirty_fields_values

    @classmethod
    def _initialize(cls, gitea, api_object, result):
        super()._initialize(gitea, api_object, result)
        for name in cls._patchable_fields:
            cls._add_write_property(name, None, api_object)

    @classmethod
    def _add_write_property(cls, name, value, api_object):
        if not hasattr(api_object, "_" + name):
            setattr(api_object, "_" + name, value)
        prop = property(
            (lambda n: lambda self: self._get_var(n))(name),
            (lambda n: lambda self, v: self.__set_var(n, v))(name),
        )
        setattr(cls, name, prop)

    def __set_var(self, name, i):
        if self.deleted:
            raise ObjectIsInvalid()
        self._dirty_fields.add(name)
        setattr(self, "_" + name, i)
