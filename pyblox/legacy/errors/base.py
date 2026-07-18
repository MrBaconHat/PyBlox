# API Errors that are shared across multiple endpoints

# ============ MAIN ===========
class RBLXException(Exception):
    def __init__(
        self,
        message: str,
        status: int,
        code: int,
        endpoint: str
    ):
        self.message = message
        self.status = status
        self.code = code
        self.endpoint = endpoint

        super().__init__(message)


# ============ 400 ============

class TooShort(RBLXException):
    pass

class TooLong(RBLXException):
    pass

class Moderated(RBLXException):
    pass

class Filtered(RBLXException):
    pass

class InvalidCharacters(RBLXException):
    pass

class InvalidCharactersSet(RBLXException):
    pass

# ============ 404 ============

class NotFound(RBLXException):
    pass

# ============ 401 ============

class AuthenticationDenied(RBLXException):
    pass

# ============ 403 ============

class TokenValidationFailed(RBLXException):
    pass

class PinLocked(RBLXException):
    pass

# ============ 500 ============

class UnknownError(RBLXException):
    pass

# ============ 503 ============

class FeatureDisabled(RBLXException):
    pass