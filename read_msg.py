from telethon import TelegramClient, events, sync
import os
# Remember to use your own values from my.telegram.org!
api_id = os.environ["api_id"]
api_hash = os.environ["api_hash"]
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats='noob_bot'))
async def my_event_handler(event):
    print(event.raw_text)

client.start()
client.run_until_disconnected()