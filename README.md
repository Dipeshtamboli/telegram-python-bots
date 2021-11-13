<!-- # telegram-python-bots -->

A repository for sending and reading messages using python scripts from Telegram.

# Sending and receiveing messages using Telegram bot
## Creating a Telegram bot - get token
- Start the conversation with BotFather (@BotFather).
- Create bot by `/newbot` command
- Set display and user name
- Get the token 

## Getting chat ID (group or bot)
- Create a group and add telegram bot to the group
- Get the list of updates for your bot from here:
 `https://api.telegram.org/bot<YourBOTToken>/getUpdates`
- Look for the `chat` object and get the group chat's id or bot's id

## Python script for sending a message
Python code `bot_send_message.py` is quite flexible and you can change it however you want. Right now,
- it requires `bot_token` and `bot_chatID` variables
- store variables `bot_token` and `bot_chatID` in bash (keep it secure) and load it in the code
- `bot_send_message.py` takes `message` and `chat` as input arguments.

## Receiving a message
- Talk to `@botfather` and disable the privacy mode for reading group messages