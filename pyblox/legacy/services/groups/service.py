from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....client import Client


class GroupService:
    def __init__(self, client: Client):
        self.__client = client

        self.__API_URL = "https://groups.roblox.com"
        self._v1 = "/v1"
        self._v2 = "/v2"

    # ==============================
    #        BANS AND BLOCKS
    # ==============================
    
    async def bans_list(
        self, 
        group_id: int, 
        limit: int = 10, 
        cursor: str | None = None,
        sort_order: str = "Asc"
    ):
        """
        [COOKIE]
        Gets the bans for the group.
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}{self._v1}/groups/{group_id}/bans",
            params={
                "limit": limit,
                "cursor": cursor,
                "sortOrder": sort_order
            },
            use_cookie=True
        )

    async def is_banned(
        self,
        group_id: int,
        user_id: int
    ):
        """
        [COOKIE]
        Fetch the ban for the user in the group.
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}{self._v1}/groups/{group_id}/bans/{user_id}",
            use_cookie=True
        )

    async def ban(
        self,
        group_id: int,
        user_id: int
    ):
        """
        [COOKIE]
        Ban the user from the group.
        """
        data = await self.__client.http.request(
            method="POST",
            url=f"{self.__API_URL}{self._v1}/groups/{group_id}/bans{user_id}",
            use_cookie=True
        )

    async def unban(
        self,
        group_id: int,
        user_id: int
    ) -> bool:
        """
        [COOKIE]
        Unban the user from the group.
        """
        data = await self.__client.http.request(
            method="DELETE",
            url=f"{self.__API_URL}{self._v1}/groups/{group_id}/bans{user_id}",
            use_cookie=True
        )
        return True  # success (no exception)

    async def blocked_keywords(
        self,
        group_id: int,
        limit: int = 10,
        cursor: str | None = None,
        sort_order: str = "Asc"
    ):
        """
        [COOKIE]
        Gets the blocked keywords for the group.
        """
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}{self._v1}/groups/{group_id}/blocked-keywords",
            params={
                "limit": limit,
                "cursor": cursor,
                "sortOrder": sort_order
            },
            use_cookie=True
        )

    async def add_blocked_keyword(
        self,
        group_id: int,
        keyword: str,
        is_private: bool
    ):
        """
        [COOKIE]
        Adds a blocked keyword to the group.
        """
        data = await self.__client.http.request(
            method="POST",
            url=f"{self.__API_URL}{self._v1}/groups/{group_id}/blocked-keywords",
            json={
                "keyword": keyword,
                "isPrivate": is_private
            },
            use_cookie=True
        )

    async def update_blocked_keyword(
        self,
        group_id: int,
        keyword_id: int,
        keyword: str,
        is_private: bool
    ):
        """
        [COOKIE]
        Updates a blocked keyword in the group.
        """
        data = await self.__client.http.request(
            method="PATCH",
            url=f"{self.__API_URL}{self._v1}/groups/{group_id}/blocked-keywords/{keyword_id}",
            json={
                "keyword": keyword,
                "isPrivate": is_private
            },
            use_cookie=True
        )

    async def delete_blocked_keyword(
        self,
        group_id: int,
        keyword_id: str
    ) -> bool:
        """
        [COOKIE]
        Deletes a blocked keyword from the group.
        """
        data = await self.__client.http.request(
            method="DELETE",
            url=f"{self.__API_URL}{self._v1}/groups/{group_id}/blocked-keywords/{keyword_id}",
            use_cookie=True
        )
        return True  # success (no exception)

    async def users_friends_groups(
        self,
        user_id: int
    )