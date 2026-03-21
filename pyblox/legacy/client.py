from .utils.requests import make_request
from .models.user import User
from .models.authenticateduser import AuthenticatedUser

class Client:
    def __init__(self, cookie: str | None = None):
        self.__cookie = cookie

    async def get_user(self, user_id: int) -> User:
        data = await make_request(
            "users",
            f"/v1/users/{user_id}"
        )
        return User(data=data)

    async def get_users(self, user_ids: list[int], excludeBannedUsers: bool = True) -> list[User] | list:
        data = await make_request(
            "users",
            "/v1/users",
            params={
                "userIds": ",".join(map(str, user_ids)),
                "excludeBannedUsers": excludeBannedUsers
            }
        )
        return [await self.get_user(user) for user in data["data"]]

    async def get_users_by_usernames(self, usernames: list[str], excludeBannedUsers=True) -> list[User]:
        data = await make_request(
            "users",
            "/v1/usernames/users",
            json={
                "usernames": usernames,
                "excludeBannedUsers": excludeBannedUsers
            },
            method="POST"
        )
        print("data:", data)
        return [await self.get_user(user) for user in data["data"]]

    async def get_authenticated_user(self) -> AuthenticatedUser:
        if not self.__cookie:
            raise Exception("No cookie provided")

        data = await make_request(
            "users",
            "/v1/authenticated-user",
            headers={
                "Cookie": f".ROBLOSECURITY={self.__cookie}"
            }
        )
        return  AuthenticatedUser(self.__cookie, User(data=data))
        