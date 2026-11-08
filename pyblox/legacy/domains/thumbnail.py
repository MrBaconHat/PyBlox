from __future__ import annotations

from typing import TYPE_CHECKING

from .domain import Domain

if TYPE_CHECKING:
    from ..client import Client


class ThumbnailDomain(Domain):
    def __init__(self, client: Client):
        super().__init__(client, "https://thumbnails.roblox.com")

    async def get_thumbnails_asset_animated_v1(
        self,
        asset_id: int,
        place_id: int | None = None
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/asset-thumbnail-animated",
            params={
                "assetId": asset_id,
                "placeId": place_id
            }
        )
        return data

    async def get_thumbnails_asset_v1(
        self,
        asset_ids: list[int],
        return_policy: str,
        size: str,
        format: str,
        is_circular: bool,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/assets",
            params={
                "assetIds": asset_ids,
                "returnPolicy": return_policy,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=use_cookie
        )
        return data

    async def get_thumbnails_asset_3d_v1(
        self,
        asset_id: int,
        use_gltf: bool,
        place_id: int | None
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/assets-thumbnail-3d",
            params={
                "assetId": asset_id,
                "useGltf": use_gltf,
                "placeId": place_id
            },
            use_cookie=True
        )
        return data

    async def get_thumbnails_bundles_thumbnails_v1(
        self,
        bundle_ids: list[int],
        size: str,
        format: str,
        is_circular: bool,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/bundles/thumbnails",
            params={
                "bundleIds": bundle_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=use_cookie
        )
        return data

    async def get_thumbnails_user_avatar_v1(
        self,
        user_ids: list[int],
        includeBackground: bool,
        size: str,
        format: str,
        is_circular: bool,
        use_cookie: bool = False
    ):
        data = await self._client. http.request(
            method="GET",
            url=f"{self._domain}/v1/users/avatar",
            params={
                "userIds": user_ids,
                "includeBackground": includeBackground,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=use_cookie
        )
        return data

    async def get_thumbnails_user_avatar_3d_v1(self, user_id: int):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/avatar-3d",
            params={
                "userId": user_id
            },
            use_cookie=True
        )
        return data

    async def get_thumbnails_user_avatar_bust_v1(
        self,
        user_ids: list[int],
        include_background: bool,
        size: str,
        format: str,
        is_circular: bool,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/avatar-bust",
            params={
                "userIds": user_ids,
                "includeBackground": include_background,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=use_cookie
        )
        return data

    async def get_thumbnails_user_avatar_headshot_v1(
        self,
        user_ids: list[int],
        include_background: bool,
        size: str,
        format: str,
        is_circular: bool,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/avatar-headshot",
            params={
                "userIds": user_ids,
                "includeBackground": include_background,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=use_cookie
        )
        return data

    async def get_thumbnails_badges_icon_v1(
        self,
        badge_ids: list[int],
        size: str,
        format: str,
        is_circular: bool
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/badges/icons",
            params={
                "badgeIds": badge_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            }
        )

    async def get_thumbnails_developer_products_icon_v1(
        self,
        developer_product_ids: list[int],
        size: str,
        format: str,
        is_circular: bool,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/developer-products/icons",
            params={
                "developerProductIds": developer_product_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=use_cookie
        )

    async def get_thumbnails_game_passes_icon_v1(
        self,
        game_pass_ids: list[int],
        size: str,
        format: str,
        is_circular: bool
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/game-passes/icons",
            params={
                "gamePassIds": game_pass_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            }
        )
        return data

    async def get_thumbnails_groups_icon_v1(
        self,
        group_ids: list[int],
        size: str,
        format: str,
        is_circular: bool
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/groups/icons",
            params={
                "groupIds": group_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            }
        )
        return data

    async def post_thumbnails_batch_v1(self, batch: list[dict], use_cookie: bool = False):
        data = await self._client.http.request(
            method="POST",
            url=f"{self._domain}/v1/batch",
            json=batch,
            use_cookie=use_cookie
        )
        return data

    async def get_users_outfit_3d_object_v1(self, outfit_id: int):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/outfit-3d",
            params={
                "outfitId": outfit_id
            },
            use_cookie=True
        )
        return data

    async def get_thumbnails_user_outfits_v1(
        self,
        user_outfit_ids: list[int],
        size: str,
        format: str,
        is_circular: bool,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/outfits",
            params={
                "userOutfitIds": user_outfit_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=use_cookie
        )
        return data

    async def get_thumbnails_universe_thumbnails_v1(
        self,
        universe_id: int,
        thumbnail_ids: list[int],
        size: str,
        format: str,
        is_circular: bool,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/universes/{universe_id}/thumbnails",
            params={
                "thumbnailIds": thumbnail_ids,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=use_cookie
        )
        return data

    async def get_thumbnails_universe_icon_v1(
        self,
        universe_ids: list[int],
        return_policy: str,
        size: str,
        format: str,
        is_circular: bool,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/games/icon",
            params={
                "universeIds": universe_ids,
                "returnPolicy": return_policy,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=use_cookie
        )
        return data

    async def get_thumbnails_universes_multiget_thumbnails_v1(
        self,
        universe_ids: list[int],
        count_per_universe: int,
        defaults: bool,
        size: str,
        format: str,
        is_circular: bool,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/games/multiget/thumbnails",
            params={
                "universeIds": universe_ids,
                "countPerUniverse": count_per_universe,
                "defaults": defaults,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=use_cookie
        )
        return data

    async def get_thumbnails_universes_gameicon_v1(
        self,
        place_ids: list[int],
        return_policy: str,
        size: str,
        format: str,
        is_circular: bool,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/games/gameicon",
            params={
                "placeIds": place_ids,
                "returnPolicy": return_policy,
                "size": size,
                "format": format,
                "isCircular": is_circular
            },
            use_cookie=use_cookie
        )
        return data