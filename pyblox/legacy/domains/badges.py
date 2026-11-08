from __future__ import annotations

from .domain import Domain


class BadgesDomain(Domain):
    async def upload_badge_icon_v1(
        self,
        badge_id: int,
        file: str
    ) -> dict:
        data = await self._client.http.request(
            method="POST",
            url=f"{self._domain}/v1/badges/{badge_id}/icon",
            file=file,
            use_cookie=True,
            use_csrf=True
        )
        return data

    async def get_badge_info_v1(
        self,
        badge_id: int,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/badges/{badge_id}/info",
            use_cookie=use_cookie
        )
        return data

    async def remove_badge_from_user_v1(
        self,
        badge_id: int
    ):
        data = await self. _client.http.request(
            method="DELETE",
            url=f"{self._domain}/v1/badges/{badge_id}/user",
            use_cookie=True,
            use_csrf=True
        )
        return data

    async def get_badge_metadata_v1(self):
        data = await self. _client.http.request(
            method="GET",
            url=f"{self._domain}/v1/badges/metadata"
        )
        return data

    async def get_games_badges_v1(
        self,
        universe_id: int,
        sort_by: str,
        limit: int,
        cursor: str | None,
        sort_order: str,
        use_cookie: bool = False
    ):
        data = await self. _client.http.request(
            method="GET",
            url=f"{self._domain}/v1/universes/{universe_id}/badges",
            params={
                "sortBy": sort_by,
                "limit": limit,
                "cursor": cursor,
                "sortOrder": sort_order
            },
            use_cookie=use_cookie
        )
        return data

    async def get_games_free_badges_quota_v1(
        self,
        universe_id: int
    ) -> int:
        data = await self. _client.http.request(
            method="GET",
            url=f"{self._domain}/v1/universes/{universe_id}/badges/free-quota"
        )
        return data