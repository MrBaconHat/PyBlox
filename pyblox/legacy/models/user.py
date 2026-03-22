from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime

from .usernamehistory import UsernameHistory

from ..utils.requests import make_request
from .. import types
from .. import models

from ..thumbnails import Thumbnails

if TYPE_CHECKING:
    from ..client import Client

class User:
    def __init__(self, client: "Client", data: dict):
        self.__client = client
        self.thumbnails = Thumbnails(self.__client)
        
        self.id: int = data.get("id")
        self.name: str = data.get("name")
        self.display_name: str = data.get("displayName")
        
        self.description: str | None = data.get("description")

        created: str | datetime | None = data.get("created")
        if created and not isinstance(created, datetime):
            self.created: datetime | None = datetime.fromisoformat(created.replace("Z", "+00:00"))
        elif created and isinstance(created, datetime):
            self.created = created
        else:
            self.created = None

        self.is_banned: bool | None = data.get("isBanned")
        self.verified: bool | None = data.get("hasVerifiedBadge")
        self.external_app_display_name: str | None = data.get("externalAppDisplayName")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "displayName": self.display_name,
            "description": self.description,
            "created": self.created,
            "isBanned": self.is_banned,
            "hasVerifiedBadge": self.verified,
            "externalAppDisplayName": self.external_app_display_name
        }

    def __repr__(self):
        return f"<User id={self.id} name={self.name} display_name={self.display_name} created={self.created} is_banned={self.is_banned} external_app_display_name={self.external_app_display_name} verified={self.verified} description={self.description}>"

    async def refresh(self):
        """
        Refreshes the user data. Only use this if you need the full user data.
        """
        data = await make_request(
            "users",
            f"/v1/users/{self.id}",
            headers=self.__client.__headers
        )
        self.__init__(self.__client, data)

    async def username_history(
        self, limit: int = 10, 
        cursor: str | None = None,
        sort_order: types.SortOrder = types.SortOrder.Asc
    ) -> UsernameHistory:
        return await self.__client.get_username_history(
            self.id,
            limit,
            cursor,
            sort_order
        )

    async def avatar_thumbnail(
        self,
        size: models.ThumbnailSize = models.ThumbnailSize.SIZE_30X30,
        format: models.ThumbnailFormat = models.ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> models.ThumbnailResponse:
        thumbnail_data: list[models.ThumbnailResponse] = await self.thumbnails.users_avatar([self.id])
        return thumbnail_data[0]

    async def avatar_thumbnail_3d(self) -> models.ThumbnailResponse:
        return await self.thumbnails.user_avatar_3d(self.id)

    async def  avatar_bust_thumbnail(
        self,
        size: models.ThumbnailSize = models.ThumbnailSize.SIZE_48X48,
        format: models.ThumbnailFormat = models.ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> models.ThumbnailResponse:
        thumbnail_data: list[models.ThumbnailResponse] = await self.thumbnails.avatar_bust([self.id])
        return thumbnail_data[0]

    async def  avatar_headshot_thumbnail(
        self,
        size: models.ThumbnailSize = models.ThumbnailSize.SIZE_48X48,
        format: models.ThumbnailFormat = models.ThumbnailFormat.PNG,
        is_circular: bool = False
    ) -> models.ThumbnailResponse:
        thumbnail_data: list[models.ThumbnailResponse] = await self.thumbnails.avatar_headshot([self.id])
        return thumbnail_data[0]