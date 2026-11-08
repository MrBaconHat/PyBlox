from __future__ import annotations

from typing import TYPE_CHECKING

from .domain import Domain

if TYPE_CHECKING:
    from ..client import Client


class PublishDomain(Domain):
    def __init__(self, client: Client):
        super().__init__(client, "https://publish.roblox.com")

    async def list_assets_quotas_v1(
        self, 
        resource_type: str, 
        asset_type: str, 
        use_dummy_data: bool = False
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/assets/quotas",
            params={
                "resourceType": resource_type,
                "assetType": asset_type,
                "useDummyData": use_dummy_data
            },
            use_cookie=True
        )
        return data

    async def publish_audio_v1(
        self,
        name: str,
        file: str,
        group_id: int,
        payment_source: str,
        estimated_file_size: int,
        estimated_duration: int,
        asset_privacy: int
    ) -> dict:
        data = await self._client.http.request(
            method="POST",
            url=f"{self._domain}/v1/audio",
            json={
                "name": name,
                "file": file,
                "groupId": group_id,
                "paymentSource": payment_source,
                "estimatedFileSize": estimated_file_size,
                "estimatedDuration": estimated_duration,
                "assetPrivacy": asset_privacy
            },
            use_cookie=True
        )
        return data

    async def verify_audio_v1(
        self,
        name: str,
        file: str,
        group_id: int,
        payment_source: str,
        file_size: int,
        duration: int
    ) -> dict:
        data = await self._client.http.request(
            method="POST",
            url=f"{self._domain}/v1/audio/verify",
            json={
                "name": name,
                "file": file,
                "groupId": group_id,
                "paymentSource": payment_source,
                "fileSize": file_size,
                "duration": duration
            },
            use_cookie=True
        )
        return data

    async def publish_a_new_plugin_icon_v1(
        self,
        plugin_id: int,
        file: str
    ) -> dict:
        data = await self._client.http.request(
            method="POST",
            url=f"{self._domain}/v1/plugins/{plugin_id}/icon",
            json={
                "file": file
            },
            use_cookie=True
        )
        return data

    async def upload_a_game_thumbnail(
        self,
        universe_id: int,
        file: str
    ) -> dict:
        data = await self._client.http.request(
            method="POST",
            url=f"{self._domain}/v1/universes/{universe_id}/thumbnails",
            json={
                "file": file
            },
            use_cookie=True
        )
        return data