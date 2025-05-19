from telethon.sync import TelegramClient

api_id = 27029779    # Replace with your API ID
api_hash = 'ae52e445711e8865e6520109dabbbd96'

client = TelegramClient('keyword_finder_session', api_id, api_hash)

async def main():
    await client.start()
    print("Logged in successfully!")

with client:
    client.loop.run_until_complete(main())
