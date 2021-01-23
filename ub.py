from telethon import TelegramClient, events
import traceback
import logging
import asyncio


import core
import db as dbmod


import text
import python
import arts
import fl


logging.basicConfig(level=logging.WARNING)
cf = open("config", "r")
cd = cf.readlines()
api_id = int(cd[0])
api_hash = cd[1].strip('\n')
db_id = int(cd[2])
db = dbmod.db(db_id)
client = TelegramClient('anon', api_id, api_hash)


commands = {
    "stop": core.stop,
    "help": core.help,
    "activate": core.activate,
    "deactivate": core.deactivate,
    "ping": core.ping,
    "sovet": core.sovet,
    "titles": core.titles,
}


@client.on(events.NewMessage)
async def cmd(event):
    message = event.message
    if event.message.sender_id == (await client.get_me()).id:
        if message.raw_text.startswith('.'):
            try:
                await commands[message.raw_text[1:].split()[0]](message)
            except KeyError:
                pass

client.start()
loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(core._activate_from_db())
client.run_until_disconnected()
