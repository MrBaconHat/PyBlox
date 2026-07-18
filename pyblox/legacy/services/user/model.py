from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import date

if TYPE_CHECKING:
    from ....client import Client

    # ------ Models ------
    from ..thumbnail.model import Thumbnail

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

    async def avatar(
        self,
        size: str = "420x420",
        format: str = "Png",
        is_circular: bool = False
    ) -> Thumbnail:
        thumbnails = await self.__client.thumbnail.user_avatar(
            user_ids=[self.id],
            size=size,
            format=format,
            is_circular=is_circular
        )
        return thumbnails[0]

    async def avatar_headshot(
            self,
            size: str = "420x420",
            format: str = "Png",
            is_circular: bool = False
        ) -> Thumbnail:
        thumbnails = await self.__client.thumbnail.user_avatar_headshot(
            user_ids=[self.id],
            size=size,
            format=format,
            is_circular=is_circular
        )
        return thumbnails[0]

    async def avatar_bust(
        self,
        size: str = "420x420",
        format: str = "Png",
        is_circular: bool = False
    ) -> Thumbnail:
        thumbnails = await self.__client.thumbnail.user_avatar_bust(
            user_ids=[self.id],
            size=size,
            format=format,
            is_circular=is_circular
        )
        return thumbnails[0]

    async def username_history(
        self,
        limit: int = 10,
        sort_order: str = "Asc",
        cursor: str | None = None
    ) -> UsernameHistoryResult:
        return await self.__client.user.username_history(
            self.id,
            limit=limit,
            sort_order=sort_order,
            cursor=cursor
        )


class AuthenticatedUser(User):
    def __init__(self, client: Client, data):
        super().__init__(client, data)

    async def birthdate(self) -> date:
        return await self.__client.user.birthdate()

    async def birthdate_update(self, birth_month: int, birth_day: int, birth_year: int, password: str):
        return await self.__client.user.birthdate_update(birth_month, birth_day, birth_year, password)

    async def gender(self) -> int:
        return await self.__client.user.gender()

    async def gender_update(self, gender: int) -> bool:
        return await self.__client.user.gender_update(gender)

    async def age_bracket(self) -> int:
        return await self.__client.user.age_bracket()

    async def country_code(self) -> str | None:
        return await self.__client.user.country_code()

    async def roles(self) -> list[str]:
        return await self.__client.user.roles()

    async def description(self) -> str | None:
        return await self.__client.user.description()

    async def description_update(self, description: str) -> str | None:
        return await self.__client.user.description_update(description)

    async def set_display(self, new_display: str) -> bool:
        return await self.__client.user.set_display(self.id, new_display)

    async def display_name_validate(self, display_name: str) -> bool:
        return await self.__client.user.display_name_validate(self.id, display_name)
        
    async def avatar_3d(self) -> Thumbnail:
        return await self.__client.thumbnail.user_avatar_3d(self.id)

    async def outfit_3d(self, outfit_id: int) -> Thumbnail:
        return await self.__client.thumbnail.user_outfit_3d(outfit_id)


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

        return await self.__client.user.get_username_history(
            self.__user_id,
            limit=self.__limit,
            sort_order=self.__sort_order,
            cursor=self.previous_page_cursor
        )