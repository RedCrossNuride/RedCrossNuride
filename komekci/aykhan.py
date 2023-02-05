
from telethon import TelegramClient

# Config məlumatları

# Telegram Client (Telethon)
API_ID = 24343756
API_HASH = "22a85c57bbe604ce4930f5e479cc3bcc"
bot_token = "6183404530:AAGLcH7EP0BOfBiuUY1R2zNgxtGg7sJHQsY"

# Nermin
Nermin = TelegramClient('Nermin', API_ID, API_HASH).start(bot_token=bot_token)
