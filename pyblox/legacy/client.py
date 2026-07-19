# pyblox/client.py
from __future__ import annotations

from .http.client import HTTPClient

# --------- SERVICES ----------
from .user import UserService
from .thumbnail import ThumbnailService
from .thumbnailresizer import ThumbnailResizerService


class Client:
    def __init__(self, cookie=None):
        self.__cookie = cookie

        self.http = HTTPClient(cookie=self.__cookie)

        # services
        self.user = UserService(self)
        self.thumbnail =  ThumbnailService(self)
        self.thumbnail_resizer = ThumbnailResizerService(self)