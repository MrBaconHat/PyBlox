import aiohttp
import asyncio
from typing import Any


class HTTPClient:
    def __init__(self, cookie=None):
        self.__cookie = cookie
        self.__x_csrf_token_cache: str | None = None
        self.__session: aiohttp.ClientSession | None = None

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

    async def __get_x_csrf_token(self) -> str | None:
        status, headers, _ = await self.__make_request(
            method="GET",
            url="https://users.roblox.com/v1/users/authenticated",
            headers={
                "Cookie": f".ROBLOSECURITY={self.__cookie}"
            }
        )
        if status == 403:
            return headers.get("x-csrf-token")
        return None

    async def request(
        self,
        method: str,
        url: str,

        # ---- Request Data ----
        headers: dict | None = None,
        params: dict | None = None,
        json: dict | None = None,

        # ---- Authentications ----
        use_csrf: bool = False,
        use_cookie: bool = False,

        # ---- Utils ----
        retry: bool = True,
        exception: bool = True
    ):
        headers = headers or {}

        headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "PyBlox/0.1.1"
        })

        if use_cookie and self.__cookie:
            headers["Cookie"] = f".ROBLOSECURITY={self.__cookie}"

        if use_csrf and self.__cookie:
            if self.__x_csrf_token_cache is None:
                self.__x_csrf_token_cache = await self.__get_x_csrf_token()

            headers["X-CSRF-TOKEN"] = self.__x_csrf_token_cache

        status, resp_headers, body = await self.__make_request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json
        )
        if status == 403 and use_csrf:
            self.__x_csrf_token_cache = resp_headers.get("x-csrf-token")
            return await self.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json,
                use_csrf=use_csrf,
                use_cookie=use_cookie 
            )

        if status == 429 and retry:
            await asyncio.sleep(1)
            return await self.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json,
                use_cookie=use_cookie,
                use_csrf=use_csrf,
                retry=False,
                exception=exception
            )

        if status >= 400 and exception:
            message = None

            if isinstance(body, dict) and "errors" in body:
                if body["errors"]:
                    message = body["errors"][0].get("message")

            raise Exception(f"{status}: {message or body}")

        elif status >= 400 and not exception:
            return status, body
            
        return body