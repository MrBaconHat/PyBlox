from __future__ import annotations 
from typing import TYPE_CHECKING

from datetime import datetime

from .utils.requests import make_request
from .models import User

if TYPE_CHECKING:
    from .client import Client

class FriendContact:
    def __init__(self, success: bool, captcha_required: bool):
        self.success = success
        self.captcha_required = captcha_required

class FriendRequest(User):
    def __init__(self, client: Client, data: dict):
        self.__client = client

        # =======================
        # Friend request object
        # =======================
        friend_request = data["friendRequest"]

        self.sent_at = datetime.fromisoformat(friend_request["sentAt"].replace("Z", "+00:00"))
        self.sender_id = friend_request["senderId"]
        self.source_universe_id = friend_request["sourceUniverseId"]
        self.origin_source_type = friend_request["originSourceType"]
        self.contact_name = friend_request["contactName"]
        self.sender_nickname = friend_request["senderNickname"]

        # =======================
        # Mutual Friends
        # =======================
        self.mutual_friends_list = data["mutualFriendsList"]

        # =======================
        # User Object
        # =======================
        user_data = {
            "hasVerifiedBadge": data["hasVerifiedBadge"],
            "description": data["description"],
            "created": data["created"],
            "isBanned": data["isBanned"],
            "externalAppDisplayName": data["externalAppDisplayName"],
            "id": data["id"],
            "name": data["name"],
            "displayName": data["displayName"]
        }
        super().__init__(self.__client, user_data)

class FriendRequestPagination:
    def __init__(self, client: Client, data: dict, friend_request: list[FriendRequest]):
        self.__client = client
        self.next_page_cursor = data["nextPageCursor"]
        self.previous_page_cursor = data["previousPageCursor"]

        self.friend_requests: list[FriendRequest] = friend_request

    async def next_page(self) -> FriendRequestPagination | None:
        if not self.next_page_cursor:
            return None
            
        return await self.__client.friend.my_friend_requests(
            cursor=self.next_page_cursor
        )

    async def previous_page(self) -> FriendRequestPagination | None:
        if not self.previous_page_cursor:
            return None

        return await self.__client.friend.my_friend_requests(
            cursor=self.previous_page_cursor
        )

class Friend:
    def __init__(self, client: Client):
        self.__client = client

    async def send_contact_friend_request(
        self,
        target_contact_id: int
    ) -> FriendContact:
        """
        [AUTHENTICATION]
        Send a contact friend request to target user.

        Returns: FriendContact
        """
        if not self.__client.headers:
            raise Exception("No cookie provided")
        data = await make_request(
            "friends",
            f"/v1/contacts/{target_contact_id}/request-friendship",
            method="POST",
            headers=self.__client.headers
        )
        return FriendContact(data["success"], data["captchaRequired"])

    async def my_check_qr_session(
        self,
        user_id: int
    ) -> bool:
        """
        [AUTHENTICATION]
        Check if the user has a QR session.

        Returns: bool
        """
        if not self.__client.headers:
            raise Exception("No cookie provided")
            
        data = await make_request(
            "friends",
            f"/v1/my/friends/{user_id}/check-qr-session",
            headers=self.__client.headers
        )
        return data

    async def my_refresh_qr_session(self) -> bool:
        """
        [AUTHENTICATION]
        Refresh QR Session for the authenticated user

        Returns: bool
        """
        if not self.__client.headers:
            raise Exception("No cookie provided")

        data = await make_request(
            "friends",
            "/v1/my/friends/refresh-qr-session",
            method="POST",
            headers=self.__client.headers
        )
        return data["Success"]

    async def my_friends_count(self) -> int:
        """
        [AUTHENTICATION]
        Get the number of friends a user has.

        Returns: int
        """
        if not self.__client.headers:
            raise Exception("No cookie provided")

        data = await make_request(
            "friends",
            "/v1/my/friends/count",
            headers=self.__client.headers
        )
        return data["count"]

    async def my_friend_requests(
        self,
        limit: int = 10,
        cursor: str | None = None,
        session_id: str | None = None,
        sort_order: int = 1
    ) -> FriendRequestPagination:
        """
        [AUTHENTICATION]
        Get all users that friend request with the authenticated user using exclusive start paging
        """
        if not self.__client.headers:
            raise Exception("No cookie provided")

        params = {
            "limit": limit,
            "friendRequestSort": SortOrder
        }
        if cursor:
            params["cursor"] = cursor

        if session_id:
            params["sessionId"] = session_id

        data = await make_request(
            "friends",
            "/v1/my/friends/requests",
            headers=self.__client.headers,
            param={
                
            }
        )
        requests = []
        for friend_request in data["data"]:
            requests.append(
                FriendRequest(self.__client, friend_request)
            )

        return FriendRequestPagination(
            self.__client,
            data,
            requests
        )