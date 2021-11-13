import os
import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = os.environ["bot_token"]
    bot_chatID = os.environ["bot_chatID"]
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext("Testing Telegram bot with environ")
# print(test)

from telethon import TelegramClient, events, sync
api_id = os.environ["api_id"]
api_hash = os.environ["api_hash"]

client = TelegramClient('anon2',
                    api_id,
                    api_hash
                    )
client.start()

destination_channel_username='+917397925455'
entity=client.get_entity(destination_channel_username)
client.send_message(entity=entity,message=f"Hi {destination_channel_username}")