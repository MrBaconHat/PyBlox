import asyncio
from pyblox.legacy import Client

client = Client()

async def main():
    user = await client.get_user(1)

    print(user.name)

asyncio.run(main())