from __future__ import annotations

import datetime

# ------ Service Models ------
from .model import (
    User,
    AuthenticatedUser,
    PartialUser,
    SearchUser,
    UserSearchResult,
    UsernameHistoryResult
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....client import Client

    # ------- External Models -------
    from ..services.thumbnail.model import Thumbnail

class UserService:
    def __init__(self, client: Client):
        self.__client = client

        self.__API_URL = "https://users.roblox.com/v1"

    # ==============================
    # Accounts
    # ==============================
    
    async def birthdate(self) -> datetime.date:
        """
        [COOKIE]
        Get the user's birthdate
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/birthdate",
            use_cookie=True
        )
        return datetime.date(
            data["birthYear"],
            data["birthMonth"],
            data["birthDay"]
        )

    async def birthdate_update(
        self,
        birth_month: int,
        birth_day: int,
        birth_year: int,
        password: str
    ) -> bool:
        """
        [COOKIE]
        Update the user's birthdate
        """
        data = await self.__client.http.request(
            method="POST",
            url=f"{self.__API_URL}/birthdate",
            json={
                "birthMonth": birth_month,
                "birthDay": birth_day,
                "birthYear": birth_year,
                "password": password
            },
            use_cookie=True
        )
        return True  # success (no exception

    async def gender(self) -> int:
        """
        [COOKIE]
        Get the user's gender
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/gender",
            use_cookie=True
        )
        return data.get("gender")

    async def gender_update(self, gender: int) -> bool:
        """
        [COOKIE]
        Update the user's gender
        """
        data = await self.__client.http.request(
            method="POST",
            url=f"{self.__API_URL}/gender",
            json={
                "gender": gender
            },
            use_cookie=True
        )
        return True

    async def get_authenticated_user(self) -> AuthenticatedUser | None:
        """
        [COOKIE]
        Gets the minimal authenticated user.
        """
        status, data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/authenticated",
            use_cookie=True
        )
            
        user: User = await self.get(data["id"])
        return AuthenticatedUser(self.__client, user.to_dict())

    async def age_bracket(self) -> int:
        """
        [COOKIE]
        Gets the age bracket of the authenticated user.
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/authenticated/age-bracket",
            use_cookie=True
        )
        return data.get("ageBracket")

    async def country_code(self) -> str | None:
        """
        [COOKIE]
        Gets the country code of the authenticated user.
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/authenticated/country-code",
            use_cookie=True
        )
        return data.get("countryCode")

    async def roles(self) -> list[str]:
        """
        [COOKIE]
        Gets the roles of the authenticated user.
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/authenticated/roles",
            use_cookie=True
        )
        return data.get("roles", [])

    # ==============================
    # User Profiles
    # ==============================
    
    async def description(self) -> str | None:
        """
        [COOKIE]
        Gets the description of the authenticated user.
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/description",
            use_cookie=True
        )
        return data.get("description")

    async def description_update(self, description: str) -> str | None:
        """
        [COOKIE]
        Updates the description of the authenticated user.
        """
        data = await self.__client.http.request(
            method="POST",
            url=f"{self.__API_URL}/description",
            json={
                "description": description
            },
            use_cookie=True
        )
        return data.get("description")

    async def get(self, user_id: int) -> User:
        """
        Gets the user by the user id.
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/{user_id}"
        )
        return User(self.__client, data)

    async def set_display(self, user_id: int, new_display: str) -> bool:
        """
        [COOKIE]
        Sets the display name of the user.
        """
        data = await self.__client.http.request(
            method="PATCH",
            url=f"{self.__API_URL}/users/{user_id}/display-names",
            json={
                "newDisplayName": new_display
            },
            use_cookie=True
        )
        return True  # success (no exception)

    async def username_history(
        self,
        user_id: int,
        limit: int = 10,
        sort_order: str = "Asc",
        cursor: str | None = None
    ) -> UsernameHistoryResult:
        """
        Gets the username history of the user.
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/{user_id}/username-history",
            params={
                "limit": limit,
                "sortOrder": sort_order,
                "cursor": cursor
            }
        )
        return UsernameHistoryResult(
            client=self.__client,
            user_id=user_id,
            data=data,
            limit=limit,
            sort_order=sort_order
        )

    # ==============================
    # Users
    # ==============================

    async def by_usernames(
        self,
        usernames: list[str],
        exclude_banned_users: bool = True
    ) -> list[PartialUser]:
        """
        Gets the users by the usernames.
        """
        data = await self.__client.http.request(
            method="POST",
            url=f"{self.__API_URL}/usernames/users",
            json={
                "usernames": usernames,
                "excludeBannedUsers": exclude_banned_users
            }
        )
        return [SearchUser(self.__client, user) for user in data["data"]]

    async def by_ids(
        self,
        user_ids: list[int],
        exclude_banned_users: bool = True
    ) -> list[PartialUser]:
        """
        Gets the users by the user ids.
        """
        data = await self.__client.http.request(
            method="POST",
            url=f"{self.__API_URL}/users",
            json={
                "userIds": user_ids,
                "excludeBannedUsers": exclude_banned_users
            }
        )
        return [PartialUser(self.__client, user) for user in data["data"]]

    async def display_name_validate(
        self,
        user_id: int,
        display_name: str
    ) -> bool:
        """
        [COOKIE]
        Validates the display name of the user.
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/{user_id}/display-names/validate",
            params={
                "displayName": display_name
            },
            use_cookie=True
        )
        return True

    async def search(
        self,
        keyword: str,
        session_id: str | None = None,
        limit: int = 10,
        cursor: str | None = None
    ) -> UserSearchResult:
        """
        Searches for users by the keyword.
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/search",
            params={
                "keyword": keyword,
                "sessionId": session_id,
                "limit": limit,
                "cursor": cursor
            }
        )
        return UserSearchResult(
            self.__client,
            input_data={
                "keyword": keyword,
                "session_id": session_id,
                "limit": limit,
                "cursor": cursor
            },
            data=data
        )