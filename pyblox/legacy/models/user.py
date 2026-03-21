from datetime import datetime

class User:
    def __init__(self, id: int, username: str, display_name: str, description: str, created: str, is_banned: bool, external_app_display_name: str | None = None, has_verified_badge: bool = False):

        self.id: int = id
        self.name: str = username
        self.display_name: str = display_name
        self.description: str = description
    
        self.created: str = created
        self.is_banned: bool = is_banned
        self.external_app_display_name: str | None = external_app_display_name
        self.verified: bool = has_verified_badge

    def id(self) -> int:
        return self.id

    def name(self) -> str:
        return self.name

    def display_name(self) -> str:
        return self.display_name

    def description(self) -> str:
        return self.description

    def created(self) -> datetime:
        return datetime.utcfromtimestamp(self.created)

    def is_banned(self) -> bool:
        return self.is_banned

    def external_app_display_name(self) -> str | None:
        return self.external_app_display_name

    def verified(self) -> bool:
        return self.verified