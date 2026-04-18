import aiohttp
import asyncio
from typing import Any


class HTTPClient:
    def __init__(self, cookie=None):
        self.__cookie = cookie
        self.__x_csfr_token_cache: str | None = None
        self.__session: str | None = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self.__session is None:
            self.__session = aiohttp.ClientSession()
        return self.__session
        
    @staticmethod
    def __sanitize_params(params: dict | None) -> dict | None:
        if params is None:
            return None
        return {
            k: str(v).lower() if isinstance(v, bool) else v
            for k, v in params.items()
            if v is not None
        }

    async def __make_request(
        self,
        method: str,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        json: dict | None = None
    ):
        session = await self._get_session()
        async with session.request(
            method=method,
            url=url,
            headers=headers,
            params=self.__sanitize_params(params),
            json=json
        ) as response:
            status = response.status
            resp_headers = response.headers
            try:
                body = await response.json()
            except Exception:
                body = await response.text()
            return status, resp_headers, body

    async def __get_x_csfr_token(self) -> str | None:
        status, headers, _ = await self.__make_request(
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
        use_csfr: bool = False,
        use_cookie: bool = False,

        # Utils
        retry: bool = True
    ):
        headers = headers or {}

        headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "PyBlox/0.1"
        })

        if use_cookie and self.__cookie:
            headers["Cookie"] = f".ROBLOSECURITY={self.__cookie}"

        if use_csfr and self.__cookie:
            if self.__x_csfr_token_cache is None:
                self.__x_csfr_token_cache = await self.__get_x_csfr_token()

            headers["X-CSFR-TOKEN"] = self.__x_csfr_token_cache

        status, resp_headers, body = await self.__make_request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json
        )
        if status == 403 and use_csfr:
            self.__x_csfr_token_cache = resp_headers.get("x-csfr-token")
            return await self.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json,
                use_csfr=use_csfr,
                use_cookie=use_cookie
            )

        if status == 429 and retry:
            await asyncio.sleep(1)
            return await self.request(
                method,
                url,
                headers,
                params,
                json,
                use_cookie,
                use_csfr,
                retry=False
            )

        if status >= 400:
            message = None

            if isinstance(body, dict) and "errors" in body:
                if body["errors"]:
                    message = body["errors"][0].get("message")

            raise Exception(f"{status}: {message or body}")
            
        return body