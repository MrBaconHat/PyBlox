from __future__ import annotations

from typing import TYPE_CHECKING

from .domain import Domain

if TYPE_CHECKING:
    from ..client import Client


class EconomyCreatorStatsDomain(Domain):
    def __init__(self, client: Client):
        super().__init__(client, "https://economycreatorstats.roblox.com")

    async def get_game_statistics_data_v1(
        self,
        universe_id: int,
        type: str,
        start_time: str,
        end_time: str
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/universes/{universe_id}/stats",
            params={
                "type": type,
                "startTime": start_time,
                "endTime": end_time
            },
            use_cookie=True
        )
        return data