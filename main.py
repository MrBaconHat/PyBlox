import asyncio
import random

from pyblox.legacy import Client
from pyblox.legacy import types

client = Client()

async def main():
    # search
    user_search = await client.search_users("roblox")
    print(user_search.users)

asyncio.run(main())