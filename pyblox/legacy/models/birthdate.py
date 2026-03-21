from ..utils.requests import make_request

class UserBirthdate:
    def __init__(self, cookie: str, data: dict):
        self.__cookie = cookie

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
            headers={
                "Cookie": f".ROBLOSECURITY={self.__cookie}"
            },
            json={
                "birthMonth": birthMonth,
                "birthDay": birthDay,
                "birthYear": birthYear,
                "password": password
            }
        )

        return UserBirthdate(self.__cookie, data)