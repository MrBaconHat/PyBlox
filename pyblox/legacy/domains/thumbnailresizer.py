from __future__ import annotations

from typing import TYPE_CHECKING

from .domain import Domain

if TYPE_CHECKING:
    from ..client import Client


class ThumbnailResizerDomain(Domain):
    def __init__(self, client: Client):
        super().__init__(client, "https://thumbnailsresizer.roblox.com")


    async def resize_thumbnails_v1(
        self,
        hash: str,
        width: int,
        height: int,
        type: str,
        format: str,
        filter_type: str
    ) -> bool:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/resize/{hash}/{width}/{height}/{type}/{format}/{filter_type}"
        )
        return True  # success (no exception)

    async def resize_secure_v1(
        self,
        hash: str,
        width: int,
        height: int,
        type: str,
        format: str = "Png",
        filter_type: str = "default"
    ) -> bool:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/secureresize/{hash}/{width}/{height}/{type}/{format}/"
        )
        return True  # success (no exception)