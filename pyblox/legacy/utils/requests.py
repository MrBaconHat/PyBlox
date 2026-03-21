import aiohttp

BASE_URL = ".roblox.com"

async def make_request(
    prefix,
    endpoint,
    method="GET",
    headers=None,
    params=None
):
    url = f"https://{prefix}{BASE_URL}{endpoint}"

    async with aiohttp.ClientSession() as session:
        async with session.request(
            method,
            url,
            headers=headers,
            params=params
        ) as response:
            if response.status != 200:
                text = await response.text()
                raise Exception(f"Request failed with status {response.status}: {text}")
            return await response.json()