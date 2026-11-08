from __future__ import annotations

from typing import TYPE_CHECKING

from .domain import Domain

if TYPE_CHECKING:
    from ..client import Client

class UserDomain(Domain):
    def __init__(self, client: Client):
        super().__init__(client, "https://users.roblox.com")

    # ==============================
    # Accounts
    # ==============================
    async def get_user_birthdate_v1(self) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/birthdate",
            use_cookie=True
        )
        return data

    async def update_user_birthdate_v1(
        self, 
        birth_month: int, 
        birth_day: int, 
        birth_year: int, 
        password: str
    ) -> dict:
        data = await self._client.http.request(
            method="POST",
            url=f"{self._domain}/v1/birthdate",
            json={
                "birthMonth": birth_month,
                "birthDay": birth_day,
                "birthYear": birth_year,
                "password": password
            },
            use_cookie=True
        )
        return data

    async def get_user_gender_v1(self) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/gender",
            use_cookie=True
        )
        return data

    async def update_user_gender_v1(self, gender: int) -> dict:
        data = await self._client.http.request(
            method="POST",
            url=f"{self._domain}/v1/gender",
            json={
                "gender": gender
            },
            use_cookie=True
        )
        return data

    async def get_authenticated_user_v1(self) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/authenticated",
            use_cookie=True
        )
        return data

    async def get_user_age_bracket_v1(self) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/authenticated/age-bracket",
            use_cookie=True
        )
        return data

    async def get_user_country_code_v1(self) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/authenticated/country-code",
            use_cookie=True
        )
        return data

    async def get_user_roles_v1(self) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/authenticated/roles",
            use_cookie=True
        )
        return data

    # ==============================
    # User Profiles
    # ==============================
    async def get_user_description_v1(self) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/description",
            use_cookie=True
        )
        return data

    async def update_user_description_v1(self, description: str | None) -> dict:
        data = await self._client.http.request(
            method="POST",
            url=f"{self._domain}/v1/description",
            json={
                "description": description
            },
            use_cookie=True
        )
        return data

    async def get_user_by_id_v1(
        self, 
        user_id: int,
        use_cookie: bool = False
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/{user_id}",
            use_cookie=use_cookie
        )
        return data

    async def set_user_display_name_v1(self, user_id: int, new_display: str) -> bool:
        data = await self._client.http.request(
            method="PATCH",
            url=f"{self._domain}/v1/users/{user_id}/display-names",
            json={
                "newDisplayName": new_display
            },
            use_cookie=True
        )
        return data

    async def get_user_username_history_v1(
        self,
        user_id: int,
        limit: int,
        sort_order: str,
        cursor: str | None,
        
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/{user_id}/username-history",
            params={
                 "limit": limit,
                 "sortOrder": sort_order,
                 "cursor": cursor
            },
            use_cookie=use_cookie
        )
        return data

    # ==============================
    # Users
    # ==============================
    async def validate_display_name_for_a_new_user_v1(
        self, 
        display_name: str,
        birthdate: "",
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/display-names/validate",
            params={
                "displayName": display_name,
                "birthdate": birthdate.strftime("%Y-%m-%d")
            },
            use_cookie=use_cookie
        )
        return data
        
    async def get_users_by_usernames_v1(
        self,
        usernames: list[str],
        exclude_banned_users: bool = True,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="POST",
            url=f"{self._domain}/v1/usernames/users",
            json={
                "usernames": usernames,
                "excludeBannedUsers": exclude_banned_users
            },
            use_cookie=use_cookie
        )
        return data

    async def get_users_by_ids_v1(
        self,
        user_ids: list[int],
        exclude_banned_users: bool = True,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="POST",
            url=f"{self._domain}/v1/users",
            json={
                "userIds": user_ids,
                "excludeBannedUsers": exclude_banned_users
            },
            use_cookie=use_cookie
        )
        return data

    async def validate_display_name_for_an_existing_user_v1(self, user_id: int, display_name: str):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/{user_id}/display-names/validate",
            params={
                "displayName": display_name
            },
            use_cookie=True
        )
        return data

    async def search_users_v1(
        self,
        keyword: str,
        session_id: str | None = None,
        limit: int = 10,
        cursor: str | None = None,
        use_cookie: bool = False
    ):
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/users/search",
            params={
                "keyword": keyword,
                "sessionId": session_id,
                "limit": limit,
                "cursor": cursor
            },
            use_cookie=use_cookie
        )
        return data