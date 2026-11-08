from __future__ import annotations

from typing import TYPE_CHECKING

from .domain import Domain

if TYPE_CHECKING:
    from ..client import Client


class TranslationRolesDomain(Domain):
    def __init__(self, client: Client):
        super().__init__(client, "https://translationroles.roblox.com")

    async def assign_or_revoke_a_role_v1(
        self,
        user_id: int,

        assignee_id: int,
        assingee_type: str,
        role: str,
        revoke: bool
    ):
        data = await self._client.http.request(
            method="POST",
            url=f"{self._domain}/v1/users/{user_id}/roles",
            json={
                "assigneeId": assignee_id,
                "assigneeType": assingee_type,
                "role": role,
                "revoke": revoke
            },
            use_cookie=True
        )
        return data

    async def get_current_logged_in_user_roles_in_a_game_v1(
        self,
        game_id: int
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/game-localization-roles/games/{game_id}/current-user/roles",
            use_cookie=True
        )
        return data

    async def get_game_user_role_assignment_info_v1(
        self,
        role: str,
        exclusive_start_key: str | None,
        page_size: int,
        group_id: int | None
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/game-localization-roles/{role}/current_user",
            params={
                "role": role,
                "exclusiveStartKey": exclusive_start_key,
                "pageSize": page_size,
                "groupId": group_id
            },
            use_cookie=True
        )
        return data

    async def get_list_of_users_assigned_a_role_in_a_game_v1(
        self,
        game_id: int,
        role: str
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/game-localization-roles/games/{game_id}/roles/{role}/assignees",
            use_cookie=True
        )
        return data