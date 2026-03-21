import asyncio
import random

from pyblox.legacy import Client
from pyblox.legacy import types

client = Client()

async def main():
    user = await client.get_user(953381216)

    username_history = await user.username_history(
        limit=100,
        sort_order=types.SortOrder.Asc
    )
    print(username_history.usernames)
    await asyncio.sleep(5)
    username_history2 = await username_history.next()
    print(username_history2.usernames)

asyncio.run(main())