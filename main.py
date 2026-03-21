import asyncio
from pyblox.legacy import Client

client = Client()

async def main():
    user = await client.get_users_by_usernames(["Mr_Hat360"])
    user = user[0]

    print(user.name)
    print(user.id)
    print(user.display_name)
    print(user.description)
    print(user.created)
    print(user.is_banned)
    print(user.external_app_display_name)

asyncio.run(main())