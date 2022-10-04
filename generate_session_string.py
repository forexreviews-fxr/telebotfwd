import config
import asyncio
from os import remove
from pyrogram import Client


app = Client(name="session_gen",api_id=config.API_ID,api_hash=config.API_HASH)

async def main():
    global s
    await app.start()
    s = await app.export_session_string()
    await app.send_message("me",s)





asyncio.run(main())
print("String Session Generated \nCheck Saved Message on Telegram")
remove("session_gen.session")