import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1734272666:AAHjHVM5GITeOp7FJRrj67wt_I4lj7WTCkM'
    bot_chatID = '1685677293'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

# test = telegram_bot_sendtext("Testing Telegram bot")
# print(test)

from telethon import TelegramClient, events, sync

api_id = "7186968"
api_hash = 'ab0b161427f3dd23f6845f8614b7b928'

client = TelegramClient('anon2',
                    api_id,
                    api_hash
                    )
client.start()

destination_channel_username='+917397925455'
entity=client.get_entity(destination_channel_username)
client.send_message(entity=entity,message="Hi")