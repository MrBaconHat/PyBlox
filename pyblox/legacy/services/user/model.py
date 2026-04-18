from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import date

from proxies import FetchProxy

if TYPE_CHECKING:
    from ....client import Client

    # ------ Models ------
    from ..services.thumbnail.model import Thumbnail

class User:
    def __init__(self, client: Client, data: dict):
        self.__client = client
        self.__dict = data

        self.name = data.get("name")
        self.id = data.get("id")
        self.display_name = data.get("displayName")
        self.description = data.get("description")
        self.created = data.get("created")
        self.is_banned = data.get("isBanned")
        self.external_app_display_name = data.get("externalAppDisplayName")
        self.has_verified_badge = data.get("hasVerifiedBadge")

        self.__proxy = FetchProxy

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "display_name": self.display_name,
            "description": self.description,
            "created": self.created,
            "is_banned": self.is_banned,
             "external_app_display_name": self.external_app_display_name,
            "has_verified_badge": self.has_verified_badge
        }

    @property
    def birthdate(self) -> date:
        return self.__proxy(self.__client.user.birthdate())

    @property
    async def gender(self) -> int:
        return await self.__client.user.gender()

    @property
    async def age_bracket(self) -> int:
        return await self.__client.user.age_bracket()

    @property
    async def country_code(self) -> str | None:
        return await self.__client.user.country_code()

    @property
    async def roles(self) -> list[str]:
        return await self.__client.user.roles()

    @property
    def avatar(self) -> Thumbnail:
        return self.__proxy(self.__client.user.user_avatar, self.id)

    @property
    async def avatar_headshot(self) -> Thumbnail:
        return await self.__client.user.user_avatar_headshot(self.id)

    @property
    async def avatar_bust(self) -> Thumbnail:
        return await self.__client.user.user_avatar_bust(self.id)

    @property
    async def username_history(self) -> Thumbnail:
        return await self.__client.user.username_history(self.id)


class AuthenticatedUser(User):
    def __init__(self, client: Client, data):
        super().__init__(client, data)


class PartialUser:
    def __init__(self, client: Client, data: dict):
        self.__client = client
        self.__dict = data

        self.name = data.get("name")
        self.id = data.get("id")

    async def fetch(self) -> User:
        return await self.__client.user.get_user(self.id)
        

class SearchUser(PartialUser):
    def __init__(self, client: Client, data):
        super().__init__(client, data)
        self.previous_usernames: list[str] = data.get("previousUsernames", [])


class UserSearchResult:
    def __init__(self, client: Client, input_data: dict, data: dict):
        self.__client = client

        # inputs
        self.__keyword: str = input_data.get("keyword")
        self.__session_id: str = input_data.get("sessionId")
        self.__limit: int = input_data.get("limit")
        self.__cursor: str = input_data.get("cursor")

        # data
        self.previous_page_cursor: str | None = data.get("previousPageCursor")
        self.next_page_cursor: str | None = data.get("nextPageCursor")

        self.users: list[SearchUser] = [
            SearchUser(client, user) for user in data.get("data", [])
        ]

    async def next_page(self) -> UserSearchResult:
        if self.next_page_cursor is None:
            raise Exception("No next page cursor")

        return await self.__client.user.search_users(
            keyword=self.__keyword,
            session_id=self.__session_id,
            limit=self.__limit,
            cursor=self.next_page_cursor
        )

    async def previous_page(self) -> UserSearchResult:
        if self.previous_page_cursor is None:
            raise Exception("No previous page cursor")

        return await self.__client.user.search_users(
            keyword=self.__keyword,
            session_id=self.__session_id,
            limit=self.__limit,
            cursor=self.__cursor
        )

class UsernameHistoryResult:
    def __init__(
        self, 
        client, 
        user_id: int, 
        data: dict,
        # --- User Input Data ---
        limit: int,
        sort_order: str
    ):
        self.__client = client
        self.__user_id = user_id

        self.__limit = limit
        self.__sort_order = sort_order

        self.previous_page_cursor: str | None = data.get("previousPageCursor")
        self.next_page_cursor: str | None = data.get("nextPageCursor")

        self.names: list[str] = [
            entry.get("name") for entry in data.get("data", [])
        ]

    async def next_page(self) -> UsernameHistoryResult:
        if self.next_page_cursor is None:
            raise Exception("No next page cursor")

        return await self.__client.user.get_username_history(
            self.__user_id,
            limit=self.__limit,
            sort_order=self.__sort_order,
            cursor=self.next_page_cursor
        )

    async def previous_page(self) -> UsernameHistoryResult:
        if self.previous_page_cursor is None:
            raise Exception("No previous page cursor")

        return await self.__client.user. get_username_history(
            self.__user_id,
            limit=self.__limit,
            sort_order=self.__sort_order,
            cursor=self.previous_page_cursor
        )