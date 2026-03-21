from ..utils.requests import make_request
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import Client

class UserBirthdate:
    def __init__(self, client: "Client", data: dict):
        self.__client = client

        self.birthMonth: int = data.get("birthMonth")
        self.birthDay: int = data.get("birthDay")
        self.birthYear: int = data.get("birthYear")

    async def update_birthdate(
        self, 
        birthMonth: int, 
        birthDay: int, 
        birthYear: int,
        password: str
    ) -> "UserBirthdate":

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

        return UserBirthdate(self.__client, data)