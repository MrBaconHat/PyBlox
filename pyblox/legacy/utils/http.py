import aiohttp
from typing import Any

X_CSFR_TOKEN_CACHE: str | None = None

class HTTPClient:
    def __init__(self, cookie=None):
        self.__cookie = cookie

    async def __make_request(
        self,
        method: str,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        json: dict | None = None
    ):
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json
            ) as response:
                return response

    async def __get_x_csfr_token(self) -> str:
        response = await self.__make_request(
            method="GET",
            url="https://users.roblox.com/v1/users/authenticated",
            headers={
                "Cookie": f".ROBLOSECURITY={self.__cookie}"
            }
        )
        return response.headers.get("x-csfr-token")

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
            if X_CSFR_TOKEN_CACHE is None:
                X_CSFR_TOKEN_CACHE = await self.__get_x_csfr_token()

            headers["X-CSFR-TOKEN"] =  X_CSFR_TOKEN_CACHE

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