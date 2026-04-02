from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....client import Client

class User:
    def __init__(self, client: Client, data: dict):
        self.__client = client
        self.__dict = data

        self.name = data.get("name")
        self.id = data.get("id")
        self.display_name = data.get("displayName")
        self.description = data.get("description")
        self.created = data.get("created")
        self.is_banned = data.get("isBanned")
        self.external_app_display_name = data.get("externalAppDisplayName")
        self.has_verified_badge = data.get("hasVerifiedBadge")


class PartialUser:
    def __init__(self, client: Client, data: dict):
        self.__client = client
        self.__dict = data

        self.name = data.get("name")
        self.id = data.get("id")

    async def fetch(self) -> User:
        return await self.__client.user.get_user(self.id)