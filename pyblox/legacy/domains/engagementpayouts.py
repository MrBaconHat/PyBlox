from __future__ import annotations

from typing import TYPE_CHECKING

from .domain import Domain

if TYPE_CHECKING:
    from ..client import Client


class EngagementPayoutsDomain(Domain):
    def __init__(self, client: Client):
        super().__init__(client, "https://engagementpayouts.roblox.com")

    async def get_games_engagement_payout_history(
        self, 
        universe_id: int,
        start_date: str,
        end_date: str
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/games/{universe_id}/engagement-payouts",
            params={
                "startDate": start_date,
                "endDate": end_date
            },
            use_cookie=True
        )
        return data