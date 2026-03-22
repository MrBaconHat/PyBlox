from __future__ import annotations
from typing import TYPE_CHECKING

from .utils.requests import make_request

from .models import Thumbnail, ThumbnailFormat, ThumbnailSize
from .types import ReturnPolicy

if TYPE_CHECKING:
    from .client import Client

class Thumbnails:
    def __init__(self, client: Client):
        self.__client = client

    async def asset_thumbnail_animated(self, asset_id: int, roblox_place_id: int | None = None) -> Thumbnail:
        data = await make_request(
            "thumbnails",
            "/v1/asset-thumbnail-animated",
            headers=self.__client.headers
        )
        return Thumbnail(data["data"])

    async def assets(
        self, 
        asset_ids: list[int], 
        size: ThumbnailSize = ThumbnailSize.SIZE_30X30, 
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False) -> list[Thumbnail]:
        data = await make_request(
            "thumbnails",
            "/v1/assets",
            params={
                "assetIds": asset_ids,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]

    async def assets_thumbnail_3d(
        self,
        asset_id: int,
        use_gltf: bool = False,
        roblox_place_id: int | None = None
    ) -> Thumbnail:
        data = await make_request(
            "thumbnails",
            "/v1/assets-thumbnail-3d",
            params={
                "assetId": asset_id,
                "useGltf": use_gltf,
                "robloxPlaceId": roblox_place_id
            },
            headers=self.__client.headers
        )
        return Thumbnail(data["data"])

    async def bundles_thumbnails(
        self,
        bundle_ids: list[int],
        size: ThumbnailSize = ThumbnailSize.SIZE_150X150,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await make_request(
            "thumbnails",
            "/v1/bundles/thumbnails",
            params={
                "bundleIds": bundle_ids,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]

    async def users_avatar(
        self,
        user_ids: list[int],
        size: ThumbnailSize = ThumbnailSize.SIZE_30X30,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await make_request(
            "thumbnails",
            "/v1/users/avatar",
            params={
                "userIds": user_ids,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]

    async def user_avatar_3d(
        self,
        user_ids: int
    ) -> Thumbnail:
        data = await make_request(
            "thumbnails",
            "/v1/users/avatar-3d",
            params={
                "userId": user_ids
            },
            headers=self.__client.headers
        )
        return Thumbnail(data["data"])

    async def avatar_bust(
        self,
        user_id: list[int],
        size: ThumbnailSize = ThumbnailSize.SIZE_48X48,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False
    ):
        data = await make_request(
            "thumbnails",
            "/v1/avatar-bust",
            params={
                "userIds": user_id,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]
        
    async def avatar_headshot(
        self,
        user_id: list[int],
        size: ThumbnailSize = ThumbnailSize.SIZE_48X48,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await make_request(
            "thumbnails",
            "/v1/avatar-headshot",
            params={
                "userIds": user_id,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]

    async def badges_icons(
        self,
        badge_ids: list[int],
        size: ThumbnailSize = ThumbnailSize.SIZE_150X150,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await make_request(
            "thumbnails",
            "/v1/badges/icons",
            params={
                "badgeIds": badge_ids,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]

    async def developer_product_icons(
        self,
        developer_product_ids: list[int],
        size: ThumbnailSize = ThumbnailSize.SIZE_150X150,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await make_request(
            "thumbnails",
            "/v1/developer-products/icons",
            params={
                "developerProductIds": developer_product_ids,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]

    async def gamepass_icons(
        self,
        gamepass_ids: list[int],
        size: ThumbnailSize = ThumbnailSize.SIZE_150X150,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await make_request(
            "thumbnails",
            "/v1/gamepasses/icons",
            params={
                "gamePassIds": gamepass_ids,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]

    async def group_icons(
        self,
        group_ids: list[int],
        size: ThumbnailSize = ThumbnailSize.SIZE_150X150,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await make_request(
            "thumbnails",
            "/v1/groups/icons",
            params={
                "groupIds": group_ids,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]

    async def batch_icons(
        self
    ):
        ...

    async def users_outfit_3d(
        self,
        outfitId: int
    ):
        data = await make_request(
            "thumbnails",
            "/v1/outfits/3d",
            params={
                "outfitId": outfitId
            },
            headers=self.__client.headers
        )
        return Thumbnail(data["data"])

    async def users_outfits(
        self,
        user_outfit_ids: list[int],
        size: ThumbnailSize = ThumbnailSize.SIZE_150X150,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await make_request(
            "thumbnails",
            "/v1/users/outfits",
            params={
                "userOutfitIds": user_outfit_ids,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]

    async def games_thumbnails(
        self,
        universe_id: int,
        thumbnailIds: list[int],
        size: ThumbnailSize = ThumbnailSize.SIZE_768X432,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> list[Thumbnail]:
        data = await make_request(
            "thumbnails",
            "/v1/games/thumbnails",
            params={
                "universeId": universe_id,
                "thumbnailIds": thumbnailIds,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]

    async def games_icons(
        self,
        universe_id: list[int],
        return_policy: ReturnPolicy = ReturnPolicy.PlaceHolder,
        size: ThumbnailSize = ThumbnailSize.SIZE_50X50,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False
    ):
        data = await make_request(
            "thumbnails",
            "/v1/games/icons",
            params={
                "universeId": universe_id,
                "returnPolicy": return_policy.value,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]

    async def games_multiget_thumbnails(
        self,
        universe_ids: list[int],
        countPerUniverse: int = 1,
        defaults: bool = False,
        size: ThumbnailSize = ThumbnailSize.SIZE_768X432,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> list[Thumbnail]:
        ...

    async def places_gameicons(
        self,
        place_ids: list[int],
        return_policy: ReturnPolicy = ReturnPolicy.PlaceHolder,
        size: ThumbnailSize = ThumbnailSize.SIZE_50X50,
        format: ThumbnailFormat = ThumbnailFormat.PNG,
        is_circular: bool = True
    ) -> list[Thumbnail]:
        data = await make_request(
            "thumbnails",
            "/v1/places/gameicons",
            params={
                "placeIds": place_ids,
                "returnPolicy": return_policy.value,
                "size": size.value,
                "format": format.value,
                "isCircular": is_circular
            },
            headers=self.__client.headers
        )
        return [Thumbnail(thumbnail) for thumbnail in data["data"]]