from __future__ import annotations
from .user import User

class UserSearch:
    def __init__(self, client, previous_cursor, next_cursor, users: list[User], input_data: dict):
        
        self.__client = client

        self.keyword: str = input_data.get("keyword")
        self.session_id: str | None = input_data.get("session_id")
        self.limit: int = input_data.get("limit")
        self.cursor: str | None = input_data.get("cursor")
        
        self.previous_cursor: str | None = previous_cursor
        self.next_cursor: str | None = next_cursor

        self.users: list[User] = users

    async def next_page(self) -> "UserSearch" | None:
        if not self.next_cursor:
            return None
            
        return await self.__client.search_users(
            keyword=self.keyword,
            session_id=self.session_id,
            limit=self.limit,
            cursor=self.next_cursor
        )

    async def previous_page(self) -> "UserSearch" | None:
        if not self.previous_cursor:
            return None

        return await  self.__client.search_users(
            keyword=self.keyword,
            session_id=self.session_id,
            limit=self.limit,
            cursor=self.previous_cursor
        )