from ...errors.base import RBLXException

# ================= ACCOUNTS =================

# ------- Birthdate -------
class InvalidBirthdate(RBLXException):
    pass

class InvalidPassword(RBLXException):
    pass


# ------- Gender ----------
class InvalidGender(RBLXException):
    pass


# ================= USER =============

# ------- Display Name Validate -------
class MissingBirthdate(RBLXException):
    pass

# ------- Get Users by Usernames -------
class TooManyUsernames(RBLXException):
    pass

# ------- Get Users by Ids -------
class TooManyIds(RBLXException):
    pass