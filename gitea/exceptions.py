class AlreadyExistsException(Exception):
    pass


class NotFoundException(Exception):
    pass


class ObjectIsInvalid(Exception):
    pass


class ConflictException(Exception):
    pass

class MissiongEqualyImplementation(Exception):
    """
    Each Object obtained from the gitea api must be able to check itself for equality in relation to its
    fields obtained from gitea. Risen if an api object is lacking the proper implementation.
    """
    pass
