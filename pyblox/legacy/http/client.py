import re

import aiohttp
import asyncio
from typing import Any

from ..errors import *


DEFAULT_ERROR_CODE_EXCEPTIONS = {
    400: {
        1: NotFound,
        2: TooMany
        3: Invalid,
        4: Invalid,
        6: Invalid,
        8: Incorrect
    },
    401: {
        0: AuthenticationDenied
    },
    403: {
        0: TokenValidationFailed,
        2: PinLocked,
        5: Invalid
    },
    404: {
        0: NotFound,
        3: Invalid
    }
    500: {
        0: UnknownError,
        5: Invalid
    },
    503: {
        3: FeatureDisabled
    }
}


class HTTPClient:
    def __init__(self, cookie=None):
        self.__cookie = cookie
        self.__x_csrf_token_cache: str | None = None
        self.__session: aiohttp.ClientSession | None = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self.__session is None:
            self.__session = aiohttp.ClientSession()
        return self.__session
        
    async def __make_request(
        self,
        method: str,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        json: dict | list | None = None,
        file: str | None = None
    ):
        session = await self._get_session()
        async with session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            file=file
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

        # Request Data
        headers: dict | None = None,
        params: dict | None = None,
        json: dict | list | None = None,

        file: str | None = None,

        # Authentications
        use_csrf: bool = False,
        use_cookie: bool = False,

        # Utils
        retry: bool = True
    ):
        headers = headers or {}

        headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "PyBlox/0.3"
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

        error = body.get("errors", [{}])[0]

        # Due to the fact that the API returns a different error format for some endpoints, we need to handle it.
        subcode = error.get("subcode", "None")
        if subcode == "None":
            subcode = error.get("code")
        message = error.get("message")

        # We dont rely on use_csrf option here
        # Because i can see cases of it being False despite the endpoint requiring it
        if status == 403 and subcode == 0:
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
            # Get ratelimit expiration from headers
            retry_after = int(resp_headers.get("Retry-After", 1))
            await asyncio.sleep(retry_after)
            return await self.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json,
                file=file,
                use_cookie=use_cookie,
                use_csrf=use_csrf,
                retry=False
            )

        if status >= 400:
            split_url = url.split("/")
            dirty_endpoint = "/".join(split_url[3:])

            # Replace all {.*?} with {}
            endpoint = re.sub(r"\{.*?\}", "{}", dirty_endpoint)
            
            error = ERROR_MAP.get(endpoint, DEFAULT_ERROR_CODE_EXCEPTIONS).get(status, {}).get(subcode, RBLXException)
            
            raise error(message, status, subcode, url)
            
        return body