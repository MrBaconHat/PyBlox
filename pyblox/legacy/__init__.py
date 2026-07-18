from .client import Client

# ============ Models ============
from .types import (
    # User
    User,
    AuthenticatedUser,
    PartialUser,
    SearchUser,
    UserSearchResult,
    UsernameHistoryResult,

    # Thumbnail
    Thumbnail,
    ThumbnailMetadata,
    ThumbnailBatch,
    ThumbnailBatchTypes,
)

from .errors import (
    # Main Exception
    RBLXException,

    # Base Exceptions
    TooShort,
    TooLong,
    Moderated,
    Filtered,
    InvalidCharacters,
    InvalidCharactersSet,
    NotFound,
    AuthenticationDenied,
    TokenValidationFailed,
    PinLocked,
    UnknownError,
    FeatureDisabled,

    # Users API Exceptions
    InvalidBirthdate,
    InvalidPassword,
    InvalidGender,
    MissingBirthdate,
    TooManyUsernames,
    TooManyIds
)

__all__ = [
    "Client",
    
    # User
    "User",
    "AuthenticatedUser",
    "PartialUser",
    "SearchUser",
    "UserSearchResult",
    "UsernameHistoryResult",
    
    # Thumbnail
    "Thumbnail",
    "ThumbnailMetadata",
    "ThumbnailBatch",
    "ThumbnailBatchTypes",

    # Errors
    "RBLXException",
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
    "TooManyIds"
]
