class GiteaApiException(Exception):
    """Something in contact with the GiteaApi failed.
    Note: Just use as fallback if no more specific Exception is available."""

    pass


class AlreadyExistsException(GiteaApiException):
    pass


class NotFoundException(GiteaApiException):
    pass


class ObjectIsInvalid(GiteaApiException):
    pass


class Unauthorized(GiteaApiException):
    pass


class Unprocessable(GiteaApiException):
    pass


class Forbidden(GiteaApiException):
    pass


class ConflictException(GiteaApiException):
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
