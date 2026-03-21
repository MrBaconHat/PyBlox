import asyncio
from typing import TYPE_CHECKING
from .utils.requests import make_request

from .models import User
from .models import AuthenticatedUser
from .models import UsernameHistory
from .models import UserSearch

from .types import SortOrder

class Client:
    def __init__(self, cookie: str | None = None):
        self.__cookie = cookie
        self.__headers = None
        if cookie:
            self.__headers = {"cookie": f".ROBLOSECURITY={cookie}"}

    @property
    def headers(self):
        return self.__headers

    async def _get_full_users(self, user_ids: list[int]) -> list["User"]:
        return await asyncio.gather(
            *[self.get_user(uid) for uid in user_ids]
        )

    async def get_user(self, user_id: int) -> "User":
        data = await make_request(
            "users",
            f"/v1/users/{user_id}",
            headers=self.__headers
        )
        return User(
            client=self,
            data=data
        )

    async def get_users(self, user_ids: list[int], excludeBannedUsers: bool = True) -> list["User"]:
        data = await make_request(
            "users",
            "/v1/users",
            json={
                "userIds": user_ids,
                "excludeBannedUsers": excludeBannedUsers
            },
            method="POST",
            headers=self.__headers
        )
        return await self._get_full_users([user["id"] for user in data["data"]])

    async def get_users_by_usernames(self, usernames: list[str], excludeBannedUsers=True) -> list["User"]:
        data = await make_request(
            "users",
            "/v1/usernames/users",
            json={
                "usernames": usernames,
                "excludeBannedUsers": str(excludeBannedUsers).lower()
            },
            method="POST",
            headers=self.__headers
        )
        return await self._get_full_users([user["id"] for user in data["data"]])

    async def get_authenticated_user(self) -> "AuthenticatedUser":
        if not self.__cookie:
            raise Exception("No cookie provided")

        data = await make_request(
            "users",
            "/v1/authenticated-user",
            headers=self.__headers
        )
        return AuthenticatedUser(self, data)

    async def get_username_history(self, user_id: int, limit: int = 10, cursor: str | None = None, sort_order: SortOrder = SortOrder.Asc) -> "UsernameHistory":
        params = {
            "limit": limit,
            "sortOrder": sort_order.value
        }
        if cursor:
            params["cursor"] = cursor
            
        data = await make_request(
            "users",
            f"/v1/users/{user_id}/username-history",
            params=params,
            headers=self.__headers
        )
        return UsernameHistory(
            client=self,
            user_id=user_id,
            limit=limit,
            sort_order=sort_order,
            nextCursor=data.get("nextPageCursor"),
            previousCursor=data.get("previousPageCursor"),
            data=data.get("data", [])
        )

    async def search_users(
        self,
        keyword: str,
        session_id: str | None = None,
        limit: int = 10,
        cursor: str | None = None
    ) -> UserSearch:
        data = await make_request(
            "users",
            "/v1/users/search",
            params={
                "keyword": keyword,
                "limit": 10
            },
            headers=self.headers
        )
        users_list = []
        for user in data["data"]:
            u = User(self, user)
            u.previous_usernames =  user.get("previousUsernames", [])
            users_list.append(u)

        return UserSearch(
            client=self,
            input_data={
                "keyword": keyword,
                "session_id": session_id,
                "limit": limit,
                "cursor": cursor
            },
            users=users_list,
            next_cursor=data.get("nextPageCursor"),
            previous_cursor=data.get("previousPageCursor")
        )