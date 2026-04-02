import aiohttp
from typing import Any


class HTTPClient:
    def __init__(self, cookie=None):
        self.__cookie = cookie
        self.__x_csfr_token_cache: str | None = None

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
                status = response.status
                resp_headers = response.headers
                try:
                    body = await response.json()
                    return status, resp_headers, body, "json"
                except Exception:
                    body = await response.text()
                    return status, resp_headers, body, "text"

    async def __get_x_csfr_token(self) -> str | None:
        status, headers, _, __ = await self.__make_request(
            method="GET",
            url="https://users.roblox.com/v1/users/authenticated",
            headers={
                "Cookie": f".ROBLOSECURITY={self.__cookie}"
            }
        )
        if status == 403:
            return headers.get("x-csfr-token")
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

        status, _, body, __ = await self.__make_request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json
        )
        return status, body