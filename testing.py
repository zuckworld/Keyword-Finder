from telethon.sync import TelegramClient

api_id = API-ID    # Replace with your API ID
api_hash = 'Your_Hash'

client = TelegramClient('keyword_finder_session', api_id, api_hash)

async def main():
    await client.start()
    print("Logged in successfully!")

with client:
    client.loop.run_until_complete(main())
