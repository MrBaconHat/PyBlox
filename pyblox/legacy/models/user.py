from datetime import datetime
from typing import TYPE_CHECKING

from .usernamehistory import UsernameHistory

from ..utils.requests import make_request
from .. import types

if TYPE_CHECKING:
    from ..client import Client

class User:
    def __init__(self, client: "Client", data: dict):
        self.__client = client
        
        self.id: int = data.get("id")
        self.name: str = data.get("name")
        self.display_name: str = data.get("displayName")
        self.description: str = data.get("description")

        created = data.get("created")
        self.created = datetime.fromisoformat(created.replace("Z", "+00:00")) if created else None

        self.is_banned: bool = data.get("isBanned")
        self.verified: bool = data.get("hasVerifiedBadge")
        self.external_app_display_name: str | None = data.get("externalAppDisplayName")

    def __repr__(self):
        return f"<User id={self.id} name={self.name} display_name={self.display_name} created={self.created} is_banned={self.is_banned} external_app_display_name={self.external_app_display_name} verified={self.verified} description={self.description}>"

    async def username_history(
        self, limit: int = 10, 
        cursor: str | None = None,
        sort_order: types.SortOrder = types.SortOrder.Asc
    ) -> "UsernameHistory":
        return await self.__client.get_username_history(
            self.id,
            limit,
            cursor,
            sort_order
        )
