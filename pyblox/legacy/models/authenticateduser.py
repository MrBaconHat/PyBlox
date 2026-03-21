from .user import User
from .birthdate import UserBirthdate

from ..utils.requests import make_request

class AuthenticatedUser:
    def __init__(self, cookie: str, user: User):
        self.__cookie = cookie
        self.user = user

    def __repr__(self):
        return f"<AuthenticatedUser user={self.user}>"

    async def get_birthday(self) -> UserBirthdate:
        data = await make_request(
            "users",
            "/v1/birthdate",
            headers=f".ROBLOSECURITY={self.__cookie}"
        )
        return UserBirthdate(self.__cookie, data)
        