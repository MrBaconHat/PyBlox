from __future__ import annotations

from typing import TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from ....client import Client


class Group:
    def __init__(self, data):
        self._data = data

        # ----- Group Info -----
        self.id: int = data["id"]
        self.name: str = data.get["name"]
        self.description: str = data.get["description"]
        self.owner: dict = data.get["owner"]

        self.shout: Shout | None = None
        if data.get("shout") is not None:
            self.shout = Shout(data["shout"])

        self.member_count: int = data.get("memberCount")
        self.is_builders_club_only: bool = data.get("isBuildersClubOnly")
        self.public_entry_allowed: bool = data.get("publicEntryAllowed")
        self.is_locked: bool = data.get("isLocked")
        self.has_verified_badge: bool = data.get("hasVerifiedBadge")
        self.has_social_modules: bool = data.get("hasSocialModules")


class Shout:
    def __init__(self, data):
        self._data = data

        self.body: str = data.get("body")

        self.poster = Poster(data["poster"])
        
        self.created: datetime = data.get("created")
        self.updated: datetime =  data.get("updated")


class Poster:
    def __init__(self, data):
        self._data = data

        self.builders_club_membership_type: int = data.get("buildersClubMembershipType")
        self.user = data.get("user")


class Role:
    def __init__(self, data):
        self._data = data

        # ----- Role Info -----
        self.id: int = data.get("id")
        self.name: str = data.get("name")
        self.description: str = data.get("description")
        self.rank: int = data.get("rank")
        self.member_count: int = data.get("memberCount")
        self.is_base: bool =  data.get("isBase")
        self.color = data.get("color")


class FriendsGroups:
    def __init__(self, data):
        self._data = data