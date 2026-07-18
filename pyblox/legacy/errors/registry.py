from . import *

# Exceptions registry pattern for roblox API errors

ERROR_RP = {
    "/v1/birthdate": {
        400: {
            1: NotFound,
            4: InvalidBirthdate,
            8: InvalidPassword
        },
        401: {
            0: AuthenticationDenied
        },
        403: {
            0: TokenValidationFailed,
            2: PinLocked,
            5: InvalidBirthdate
        },
        500: {
            0: UnknownError,
            5: InvalidBirthdate
        }
    },
    "/v1/gender": {
        400: {
            1: NotFound,
            6: InvalidGender
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
            3: InvalidCharacters,
            4: Moderated,
            8: InvalidCharactersSet
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
            3: InvalidCharacters,
            4: Moderated,
            6: MissingBirthdate,
            8: InvalidCharactersSet
        }
    },
    "/v1/usernames/users": {
        400: {
            2: TooManyUsernames
        }
    },
    "/v1/users": {
        400: {
            1: TooManyIds
        }
    },
    "/v1/users/{}/display-names/validate": {
        400: {
            1: TooShort,
            2: TooLong,
            3: InvalidCharacters,
            4: Moderated,
            8: InvalidCharactersSet
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