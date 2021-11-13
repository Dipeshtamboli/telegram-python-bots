from telethon import TelegramClient, events, sync

# Remember to use your own values from my.telegram.org!
api_id = "7186968"
api_hash = 'ab0b161427f3dd23f6845f8614b7b928'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats='noob_bot'))
async def my_event_handler(event):
    print(event.raw_text)

client.start()
client.run_until_disconnected()