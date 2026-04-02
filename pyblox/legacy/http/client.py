import aiohttp
from typing import Any


class HTTPClient:
    def __init__(self, cookie=None):
        self.__cookie = cookie
        self.__x_csfr_token_cache: str | None = None
        self.__session: aiohttp.ClientSession | None = None

    async def __make_request(
        self,
        method: str,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        json: dict | None = None
    ):
        if self.__session is None:
            self.__session = aiohttp.ClientSession()
        async with self.__session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json
        ) as response:
            return response

    async def __get_x_csfr_token(self) -> str | None:
        response = await self.__make_request(
            method="GET",
            url="https://users.roblox.com/v1/users/authenticated",
            headers={
                "Cookie": f".ROBLOSECURITY={self.__cookie}"
            }
        )
        if response.status == 403:
            return response.headers.get("x-csfr-token")
        return None

    async def request(
        self,
        method: str,
        url: str, 

        # Request Data
        headers: dict | None = None, 
        params: dict | None = None, 
        json: dict | None = None,

        # Authentications
        x_csfr_token: bool = False,
        cookie: bool = False
    ):
        headers = headers or {}

        headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "PyBlox/0.1"
        })

        if cookie and self.__cookie:
            headers["Cookie"] = f".ROBLOSECURITY={self.__cookie}"

        if x_csfr_token and self.__cookie:
            if self.__x_csfr_token_cache is None:
                self.__x_csfr_token_cache = await self.__get_x_csfr_token()

            headers["X-CSFR-TOKEN"] = self.__x_csfr_token_cache

        response = await self.__make_request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json
        )
        if response.status == 200:
            return 200, await response.json()

        return response.status, await response.text()