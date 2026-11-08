from __future__ import annotations

from typing import TYPE_CHECKING

from .domain import Domain

if TYPE_CHECKING:
    from ..client import Client


class PresenceDomain(Domain):
    def __init__(self, client: Client):
        super().__init__(client, "https://presence.roblox.com")

    async def get_user_presence_v1(self, user_ids: list[int]) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/presence/users",
            params={
                "userIds": user_ids
            }
        )
        return data