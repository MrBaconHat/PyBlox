from __future__ import annotations

from .model import Thumbnail, ThumbnailMetadata, ThumbnailBatch

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .....client import Client


class ThumbnailService:
    def __init__(self, client: Client):
        self.__client = client

        self.__API_URL = "https://thumbnails.roblox.com/v1"

    def _parse_thumbnails(self, data):
        return [
            Thumbnail(t) 
            for t in data.get("data", [])
        ]

    # ---------- ASSETS ----------
    async def thumbnails_asset_animated(
        self,
        asset_id: int,
        place_id: int | None = None
    ) -> Thumbnail:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/asset-thumbnail-animated",
            params={
                "assetId": asset_id,
                "placeId": place_id
            }
        )
        return Thumbnail(data)

    async def thumbnail_asset(
        self,
        asset_ids: list[int],
        return_policy: str = "PlaceHolder",
        size: str = "30x30",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/assets",
            params={
                "assetIds": asset_ids,
                "returnPolicy": return_policy,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=True
        )
        return self._parse_thumbnails(data)

    async def assets_thumbnail_3d(
        self,
        asset_id: int,
        use_gltf: bool = False,
        place_id: int | None = None
    ) -> Thumbnail:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/assets-thumbnail-3d",
            params={
                "assetId": asset_id,
                "useGltf": use_gltf,
                "placeId": place_id
            },
            use_cookie=True
        )
        return Thumbnail(data)

    # ---------- AVATARS ----------
    async def bundles_thumbnails(
        self,
        bundle_ids: list[int],
        size: str = "150x150",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/bundles/thumbnails",
            params={
                "bundleIds": bundle_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=True
        )
        return self._parse_thumbnails(data)

    async def user_avatar(
        self,
        user_ids: list[int],
        size: str = "30x30",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/avatar",
            params={
                "userIds": user_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=True
        )
        return self._parse_thumbnails(data)

    async def user_avatar_3d(
        self,
        user_id: int
    ) -> Thumbnail:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/avatar-3d",
            params={
                "userId": user_id
            },
            use_cookie=True
        )
        return Thumbnail(data)

    async def user_avatar_bust(
        self,
        user_ids: list[int],
        size: str = "48x48",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/avatar-bust",
            params={
                "userIds": user_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=True
        )
        return self._parse_thumbnails(data)

    async def user_avatar_headshot(
        self,
        user_ids: list[int],
        size: str = "48x48",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/avatar-headshot",
            params={
                "userIds": user_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=True
        )
        return self._parse_thumbnails(data)

    # ---------- BADGES ----------
    async def badges_icon(
        self,
        badge_ids: list[int],
        size: str = "150x150",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/badges/icons",
            params={
                "badgeIds": badge_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            }
        )
        return self._parse_thumbnails(data)

    #  ---------- DEVELOPER PRODUCTS ----------
    async def developer_products_icon(
        self,
        developer_product_ids: list[int],
        size: str = "150x150",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/developer-products/icons",
            params={
                "developerProductIds": developer_product_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=True
        )
        return self._parse_thumbnails(data)

    # ---------- GAME PASS ----------
    async def game_passes_icon(
        self,
        game_pass_ids: list[int],
        size: str = "150x150",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/game-passes/icons",
            params={
                "gamePassIds": game_pass_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            }
        )
        return self._parse_thumbnails(data)

    # ---------- GROUPS ----------
    async def groups_icon(
        self,
        group_ids: list[int],
        size: str = "150x150",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/groups/icons",
            params={
                "groupIds": group_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            }
        )
        return self._parse_thumbnails(data)

    #  ---------- THUMBNAILS ----------
    async def batch(
        self,
        batch: list[ThumbnailBatch]
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="POST",
            url=f"{self.__API_URL}/batches",
            json={
                "batch": batch
            }
        )
        return self._parse_thumbnails(data)

    async def metadata(self):
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/metadata"
        )
        return ThumbnailMetadata(data)

    async def user_outfit_3d(
        self,
        outfit_id: int
    ) -> Thumbnail:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/outfit-3d",
            params={
                "outfitId": outfit_id
            },
            use_cookie=True
        )
        return Thumbnail(data)

    async def user_outfits(
        self,
        user_outfit_ids: list[int],
        size: str = "150x150",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/users/outfits",
            params={
                "userOutfitIds": user_outfit_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=True
        )
        return self._parse_thumbnails(data)

    # ---------- UNIVERSES ----------
    async def universe_thumbnail(
        self,
        universe_id: int,
        thumbnail_ids: list[int],
        size: str = "150x150",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/universes/{universe_id}/thumbnails",
            params={
                "thumbnailIds": thumbnail_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=True
        )
        return self._parse_thumbnails(data)

    async def universe_icon(
        self,
        universe_ids: list[int],
        return_policy: str = "PlaceHolder",
        size: str = "50x50",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/games/icon",
            params={
                "universeIds": universe_ids,
                "returnPolicy": return_policy,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=True
        )
        return self._parse_thumbnails(data)

    async def universe_multiget_thumbnails(
        self,
        universe_ids: list[int],
        count_per_universe: int = 1,
        defaults: bool = True,
        size: str = "768x432",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/games/multiget/thumbnails",
            params={
                "universeIds": universe_ids,
                "countPerUniverse": count_per_universe,
                "defaults": defaults,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=True
        )
        thumbnails = []
        for universe in data["data"]:
            if universe.get("error") is not None:
                raise Exception(universe["error"])
                
            for thumbnail in universe["thumbnails"]:
                thumbnails.append(Thumbnail(thumbnail))

        return thumbnails

    async def universes_gameicon(
        self,
        place_ids: list[int],
        return_policy: str = "PlaceHolder",
        size: str = "50x50",
        format: str = "Png",
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await self.__client.http.request(
            method="GET",
            url=f"{self.__API_URL}/games/gameicon",
            params={
                "placeIds": place_ids,
                "returnPolicy": return_policy,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=True
        )
        return self._parse_thumbnails(data)