
import json
import os
import platform
import os.path
import telegram

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from dotenv import load_dotenv


is_os_windows = platform.system() == "Windows"

if is_os_windows:
    env_path = os.path.join("secrets.env")  # ◄local ▼
    load_dotenv(env_path)
    SECRET = os.getenv("SECRET")

with open('data.json', 'w') as file:
    json.dump(SECRET, file)

# Считывание данных из файла .json в новую переменную
with open('data.json', 'r') as file:
    y = json.load(file)

print(y)  # Вывод содержимого переменной y
print(y)  # Вывод содержимого переменной y