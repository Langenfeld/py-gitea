class AlreadyExistsException(Exception):
    pass


class NotFoundException(Exception):
    pass


class ObjectIsInvalid(Exception):
    pass


class ConflictException(Exception):
    pass


class RawRequestEndpointMissing(Exception):
    """This ApiObject can only be obtained through other api objects and does not have
    diret .request method."""

    pass


class MissiongEqualyImplementation(Exception):
    """
    Each Object obtained from the gitea api must be able to check itself for equality in relation to its
    fields obtained from gitea. Risen if an api object is lacking the proper implementation.
    """

    pass
