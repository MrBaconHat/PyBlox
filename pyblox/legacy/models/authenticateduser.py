from .user import User
from .birthdate import UserBirthdate

from ..utils.requests import make_request

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..client import Client

class AuthenticatedUser(User):
    def __init__(self, client: "Client", data: dict):
        super().__init__(client, data)
        self.__client = client

    def __repr__(self):
        return f"<AuthenticatedUser ID={self.id} user={self.name}>"

    async def get_birthdate(self) -> UserBirthdate:
        data = await make_request(
            "users",
            "/v1/birthdate",
            headers=self.__client.__headers
        )
        return UserBirthdate(self.__client, data)

    async def update_birthdate(
        self,
        birthMonth: int,
        birthDay: int,
        birthYear: int,
        password: str
    ) -> UserBirthdate:
        data = await make_request(
            "users",
            "/v1/birthdate",
            method="POST",
            headers=self.__client.headers,
            json={
                "birthMonth": birthMonth,
                "birthDay": birthDay,
                "birthYear": birthYear,
                "password": password
            }
        )
        return  UserBirthdate(self.__client, data)

    async def get_gender(self) -> int:
        data = await make_request(
            "users",
            "/v1/gender",
            headers=self.__client.__headers
        )
        return data.get("gender")

    async def update_gender(
        self, gender: int, 
        password: str
    ):
        data = await make_request(
            "users",
            "/v1/gender",
            method="POST",
            headers=self.__client.headers,
            json={
                "gender": gender,
                "password": password
            }
        )
        return data.get("gender")

    async def get_age_bracket(self) -> int:
        data = await make_request(
            "users",
            "/v1/users/authenticated/age-bracket",
            headers=self.__client.headers
        )
        return data.get("ageBracket")

    async def get_country_code(self):
        data = await make_request(
            "users",
            "/v1/users/authenticated/country-code",
            headers=self.__client.headers
        )
        return data.get("countryCode")

    async def get_roles(self) -> list[str | None]:
        data = await make_request(
            "users",
            "/v1/users/authenticated/roles",
            headers=self.__client.headers
        )
        return data.get("roles")

    async def get_description(self) -> str | None:
        data = await make_request(
            "users",
            "/v1/description",
            headers=self.__client.headers
        )
        return data.get("description")

    async def update_description(self, description: str) -> str | None:
        data = await make_request(
            "users",
            "/v1/description",
            method="POST",
            headers=self.__client.headers,
            json={
                "description": description
            }
        )
        return data.get("description")

    async def validate_display_name(
        self,
        display_name: str
    ) -> bool:
        data = await make_request(
            "users",
            f"/v1/users/{self.id}/display-names/validate",
            method="GET",
            headers=self.__client.headers,
            params={
                "displayName": display_name
            }
        )
        return len(data) == 0

    async def update_display_name(
        self, 
        new_display_name: str
    ) -> str | None:
        data = await make_request(
            "users",
            f"/v1/users/{self.id}/display-names",
            method="PATCH",
            headers=self.__client.headers,
            json={
                "newDisplayName": new_display_name
            }
        )
        return  data.get("newDisplayName")