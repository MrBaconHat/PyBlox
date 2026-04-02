from __future__ import annotations
from typing import TYPE_CHECKING

from .model import User, PartialUser

if TYPE_CHECKING:
    from ....client import Client

class UserService:
    def __init__(self, client: Client):
        self.__client = client

    async def get_user(self, user_id: int) -> User:
        status, data = await self.__client.http.request(
            method="GET",
            url=f"https://users.roblox.com/v1/users/{user_id}",
            cookie=True
        )
        if status != 200:
            raise Exception(f"Failed to get user: {data}({status})")
            
        return User(self.__client, data)