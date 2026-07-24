# telegram-python-bots

Small Python scripts to **send** and **read** Telegram messages, using both the Telegram **Bot API** (via `requests`) and the **Telethon** user client.

## Overview

This repository collects three standalone scripts for automating Telegram from Python. Two paths are demonstrated: the HTTP Bot API (send a message to a bot chat or a group using a bot token) and the Telethon MTProto client (send as / listen as a user account with an `api_id` / `api_hash`). All credentials are read from environment variables, so nothing sensitive is stored in the code. It is a lightweight utility/reference, not a packaged library.

## Requirements

- Python 3
- [`requests`](https://pypi.org/project/requests/) — used by the Bot API scripts
- [`telethon`](https://pypi.org/project/telethon/) — used by the user-client scripts

There is no `requirements.txt` in the repo; install the two third-party packages directly:

```bash
pip install requests telethon
```

(`os` and `argparse` are from the Python standard library.)

### Credentials (environment variables)

The scripts read all credentials from environment variables — export the ones needed by the script you run:

| Variable | Used by | How to obtain it |
| --- | --- | --- |
| `bot_token` | `bot_send_msg.py`, `send_msg.py` | Create a bot with [@BotFather](https://t.me/BotFather) (`/newbot`) and copy the token |
| `bot_chatID` | `bot_send_msg.py` (when `--chat bot`) | The chat ID of the direct bot conversation |
| `group_chatID` | `bot_send_msg.py` (when `--chat group`), `send_msg.py` | The chat ID of a group the bot is in |
| `api_id` | `send_msg.py`, `read_msg.py` | From [my.telegram.org](https://my.telegram.org) |
| `api_hash` | `send_msg.py`, `read_msg.py` | From [my.telegram.org](https://my.telegram.org) |

To find a chat ID, add the bot to the chat, send a message, then call
`https://api.telegram.org/bot<bot_token>/getUpdates` and read the `chat.id` field.

Example (bash):

```bash
export bot_token="123456:ABC-your-bot-token"
export group_chatID="-1001234567890"
export bot_chatID="123456789"
export api_id="1234567"
export api_hash="your_api_hash"
```

> Note: Telethon writes login session files (`anon.session`, `anon2.session`). These are git-ignored via `.gitignore` (`*.session`) — keep them private.

## Usage

### 1. Send a message with the Bot API — `bot_send_msg.py`

The most reusable script. It accepts command-line arguments and sends via the Bot API.

```bash
# Send to the group (default chat target), default message is "Hi"
python bot_send_msg.py --msg "Hello from Python" --chat group

# Send to the direct bot chat
python bot_send_msg.py --msg "Hello from Python" --chat bot
```

Arguments (both optional):

- `--msg` — message text to send (default: `"Hi"`).
- `--chat` — target chat, either `group` (uses `group_chatID`) or `bot` (uses `bot_chatID`); any other value exits with an error. Default: `group`.

Messages are sent with `parse_mode=Markdown`.

### 2. Send as a user with Telethon — `send_msg.py`

This script first sends a fixed test message (`"Testing Telegram bot with environ"`) to `group_chatID` via the Bot API, then logs in as a user through Telethon and sends a message to a destination.

```bash
python send_msg.py
```

Before running, edit the hard-coded destination in `send_msg.py`:

```python
destination_channel_username = '+10000000000'  # replace with a real phone / username
```

Requires `bot_token`, `group_chatID`, `api_id`, and `api_hash`. On first run Telethon will prompt for login and create an `anon2` session.

### 3. Read incoming messages with Telethon — `read_msg.py`

Listens as a user account and prints the raw text of every new message from a given chat.

```bash
python read_msg.py
```

The chat it listens to is hard-coded — edit it in `read_msg.py`:

```python
@client.on(events.NewMessage(chats='noob_bot'))
```

Requires `api_id` and `api_hash`. Runs until disconnected (`client.run_until_disconnected()`). On first run Telethon creates an `anon` session and may prompt for login.

> To read messages sent in groups via a bot, talk to [@BotFather](https://t.me/BotFather) and disable privacy mode for your bot.

## License

Released under the [MIT License](LICENSE) — Copyright (c) 2021 Dipesh Tamboli.
