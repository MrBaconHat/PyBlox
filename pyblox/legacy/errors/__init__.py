from .base import *

# Services Exceptions
from ..services.user.errors import *

from .registry import ERROR_RP


__all__ = [
    # Main
    "RBLXException",

    # Base
    "TooShort",
    "TooLong",
    "Moderated",
    "Filtered",
    "InvalidCharacters",
    "InvalidCharactersSet",
    "NotFound",
    "AuthenticationDenied",
    "TokenValidationFailed",
    "PinLocked",
    "UnknownError",
    "FeatureDisabled",
    "InvalidBirthdate",
    "InvalidPassword",
    "InvalidGender",
    "MissingBirthdate",
    "TooManyUsernames",
    "TooManyIds",

    # User
    "InvalidBirthdate",
    "InvalidPassword",
    "InvalidGender",
    "MissingBirthdate",
    "TooManyUsernames",
    "TooManyIds"
    
    "ERROR_RP"
]