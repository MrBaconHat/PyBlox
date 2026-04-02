from __future__ import annotations

from .http.client import HTTPClient
from .services.user.service import UserService

class Client:
    def __init__(self, cookie=None):
        self.__cookie = cookie

        self.http = HTTPClient(cookie=self.__cookie)

        # services
        self.user = UserService(self)