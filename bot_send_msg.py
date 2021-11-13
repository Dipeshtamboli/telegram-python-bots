import os
import requests
import argparse


parser = argparse.ArgumentParser(description='Send a message on Telegram')
parser.add_argument('--msg', default="Hi", required=False,
                    help='Message string to send')

parser.add_argument('--chat', default="group", required=False, 
                    help='Chat channel: \'group\' or the \'bot\'')
                    
args = parser.parse_args()

def telegram_bot_sendtext(bot_message, chat):
    bot_token = os.environ["bot_token"]
    if chat=="bot": 
        bot_chatID = os.environ["bot_chatID"]
    elif chat=="group":
        bot_chatID = os.environ["group_chatID"]
    else:
        print(f"Chat ID can be \'group\' or \'bot\' and not {chat}")
        exit()

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext(args.msg, args.chat)
# test = telegram_bot_sendtext("Testing Telegram bot with environ")