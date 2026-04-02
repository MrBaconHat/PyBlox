from __future__ import annotations

from .utils import HTTPClient

class Client:
    def __init__(self, cookie=None):
        self.__cookie = cookie

        self.http = HTTPClient(cookie=self.__cookie)