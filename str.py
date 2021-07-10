import asyncio

from pyrogram import Client

print("Enter your App Info from my.telegram.org/apps Below.")


async def main():
    async with Client(
        ":memory:", api_id=int(input("Enter API ID:")), api_hash=input("Enter API HASH:")
    ) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
