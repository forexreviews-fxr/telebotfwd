import config
from pyrogram import Client, filters
import logging



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


app = Client(name="account1",api_id=config.API_ID,api_hash=config.API_HASH,session_string=config.SESSION_STRING)


@app.on_message(filters.chat(config.SOURCE_1))
async def handler1(client, message):
    await message.forward(config.DESTINATION_1)
    logging.info("Message Forwarded to Destination 1")

@app.on_message(filters.chat(config.SOURCE_2))
async def handler2(client, message):
    await message.forward(config.DESTINATION_2)
    logging.info("Message Forwarded to Destination 2")


# You can multiple channel and multiple destination like that


app.run()
