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
    ) -> "UsernameHistory":
        return await self.__client.get_username_history(
            self.id,
            limit,
            cursor,
            sort_order
        )
