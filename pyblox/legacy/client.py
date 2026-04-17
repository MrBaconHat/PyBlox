from __future__ import annotations

from .http.client import HTTPClient

# --------- SERVICES ----------
from .services.user.service import UserService
from .services.thumbnail.service import ThumbnailService

class Client:
    def __init__(self, cookie=None):
        self.__cookie = cookie

        self.http = HTTPClient(cookie=self.__cookie)

        # services
        self.user = UserService(self)
        self.thumbnail =  ThumbnailService(self)