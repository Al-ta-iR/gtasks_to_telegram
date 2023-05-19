import telebot
# import datetime as dt
import os
import platform
import json
import os.path

from dotenv import load_dotenv


is_os_windows = platform.system() == "Windows"

if is_os_windows:
    env_path = os.path.join("secrets.env")  # ◄local ▼
    load_dotenv(env_path)
    BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
else:
    BOT_API_TOKEN = os.environ.get("BOT_API_TOKEN")  # online ▼
    CHAT_ID = os.environ.get("CHAT_ID")  # online ▼




bot = telebot.TeleBot(BOT_API_TOKEN)

def message_send(answer):
    if len(answer) > 1500:
        message_parts = []
        while len(answer) > 1500:
            message_parts.append(answer[:1501])
            answer = answer[1501:]
        for part in message_parts:
            bot.send_message(CHAT_ID, str(part), parse_mode='Markdown')
    else:
        bot.send_message(CHAT_ID, answer, parse_mode='Markdown')
