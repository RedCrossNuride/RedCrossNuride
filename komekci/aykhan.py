
from telethon import TelegramClient

# Config məlumatları

# Telegram Client (Telethon)
API_ID = 22044573
API_HASH = "b6212c1e666ed3898df1e59cdc053e98"
bot_token = "5730897799:AAFH-aie5evF4ZsqZprqr5ADDg32_1weiVk"

# Nermin
Nermin = TelegramClient('Nermin', API_ID, API_HASH).start(bot_token=bot_token)
