from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...client import Client


class ThumbnailResizerService:
    def __init__(self, client: Client):
        self._client = client
        self._API_URL = "https://thumbnailsresizer.roblox.com/v1"


    async def resize(
        self,
        hash: str,
        width: int,
        height: int,
        type: str,
        format: str = "Png",
        filter_type: str = "default"
    ) -> bool:
        """
        [COOKIE]
        Resizes a thumbnail.
        """
        data = await self._client.http.request(
            method="GET",
            url=f"{self._API_URL}/resize/{hash}/{width}/{height}/{type}/{format}/{filter_type}"
        )
        return True  # success (no exception)

    async def resize_secure(
        self,
        hash: str,
        width: int,
        height: int,
        type: str,
        format: str = "Png",
        filter_type: str = "default"
    ) -> bool:
        """
        [COOKIE]
        Resizes a thumbnail.
        """
        data = await self._client.http.request(
            method="GET",
            url=f"{self._API_URL}/secureresize/{hash}/{width}/{height}/{type}/{format}/"
        )
        return True  # success (no exception)