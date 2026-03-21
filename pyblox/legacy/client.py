from .utils.requests import make_request
from .models.user import User

class Client:
    def __init__(self, cookie: str | None = None):
        self.cookie = cookie

    async def get_user(self, user_id: int) -> User:
        data = await make_request(
            "users",
            f"/v1/users/{user_id}"
        )
        return User(
            id=data["id"],
            username=data["name"],
            display_name=data["displayName"],
            description=data["description"],
            created=data["created"],
            is_banned=data["isBanned"],
            external_app_display_name=data["externalAppDisplayName"],
            has_verified_badge=data["hasVerifiedBadge"]
        )

    async def get_authenticated_user(self):
        if not self.cookie:
            raise Exception("No cookie provided")

        data = await make_request(
            "users",
            "/v1/authenticated-user",
            headers={
                "Cookie": f".ROBLOSECURITY={self.cookie}"
            }
        )