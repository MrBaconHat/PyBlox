# API Errors that are shared across multiple endpoints

# ============ MAIN ===========
class RBLXException(Exception):
    """
    This is the base exception. All exceptions inherit from this.
    """
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
    """
    This exception is raised when the input is too short.
    """
    pass

class TooLong(RBLXException):
    """
    This exception is raised when the input is too long.
    """
    pass

class TooMany(RBLXException):
    """
    This exception is raised when the input is too many.
    """
    pass

class Moderated(RBLXException):
    """
    This exception is raised when the input is moderated.
    """
    pass

class Filtered(RBLXException):
    """
    This exception is raised when the input is filtered.
    """
    pass

class Invalid(RBLXException):
    """
    This exception is raised when the input is invalid.
    """
    pass

class MissingRequirement(RBLXException):
    """
    This exception is raised when a constructor is missing a required input.
    """
    pass

# ============ 401 ============

class AuthenticationDenied(RBLXException):
    """
    This exception is raised when the authentication is denied. Mainly raised when the cookie is invalid or has expired.
    """
    pass

# ============ 403 ============

class TokenValidationFailed(RBLXException):
    """
    This exception is raised when the token validation fails. Mainly raised when the CSRF token is invalid or has expired.
    """
    pass

class PinLocked(RBLXException):
    """
    This exception is raised when the account's pin is locked.
    """
    pass

# ============ 404 ============

class NotFound(RBLXException):
    """
    This exception is raised when the resource is not found.
    """
    pass

# ============ 500 ============

class UnknownError(RBLXException):
    """
    This exception is raised when the server returns an unknown error.
    """
    pass

# ============ 503 ============

class FeatureDisabled(RBLXException):
    """
    This exception is raised when the feature is disabled.
    """
    pass



# ============ REGISTRY PATTERN ============

# Exceptions registry pattern for roblox API errors

ERROR_RP = {
    "/v1/birthdate": {
        400: {
            1: NotFound,
            4: Invalid,
            8: Invalid
        },
        401: {
            0: AuthenticationDenied
        },
        403: {
            0: TokenValidationFailed,
            2: PinLocked,
            5: Invalid
        },
        500: {
            0: UnknownError,
            5: Invalid
        }
    },
    "/v1/gender": {
        400: {
            1: NotFound,
            6: Invalid
        },
        401: {
            0: AuthenticationDenied
        },
        403: {
            0: TokenValidationFailed,
            2: PinLocked
        },
        500: {
            0: UnknownError
        }
    },
    "/v1/users/authenticated": {
        401: {
            0: AuthenticationDenied
        }
    },
    "/v1/users/authenticated/age-bracket": {
        401: {
            0: AuthenticationDenied
        }
    },
    "/v1/users/authenticated/country-code": {
        401: {
            0: AuthenticationDenied
        }
    },
    "/v1/users/authenticated/roles": {
        401: {
            0: AuthenticationDenied
        }
    },
    "/v1/description": {
        400: {
            1: NotFound
        },
        401: {
            0: AuthenticationDenied
        },
        403: {
            0: TokenValidationFailed,
            2: PinLocked
        },
        500: {
            0: UnknownError
        },
        503: {
            3: FeatureDisabled
        }
    },
    "/v1/users/": {
        404: {
            3: NotFound
        }
    },
    "/v1/users/{}/display-names": {
        400: {
            1: TooShort,
            2: TooLong,
            3: Invalid,
            4: Moderated,
            8: Invalid
        },
        401: {
            0: AuthenticationDenied
        },
        403: {
            0: TokenValidationFailed,
            2: NotFound
        }
    },
    "/v1/users/{}/username-history": {
        400: {
            3: NotFound
        }
    },
    "/v1/display-names/validate": {
        400: {
            1: TooShort,
            2: TooLong,
            3: Invalid,
            4: Moderated,
            6: MissingRequirement,
            8: Invalid
        }
    },
    "/v1/usernames/users": {
        400: {
            2: TooMany
        }
    },
    "/v1/users": {
        400: {
            1: TooMany
        }
    },
    "/v1/users/{}/display-names/validate": {
        400: {
            1: TooShort,
            2: TooLong,
            3: Invalid,
            4: Moderated,
            8: Invalid
        },
        401: {
            0: AuthenticationDenied
        },
        403: {
            7: NotFound
        }
    },
    "/v1/users/search": {
        400: {
            5: Filtered,
            6: TooShort
        }
    }
}