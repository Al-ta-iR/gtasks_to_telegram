
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
    secret = os.getenv("secret")
else:
    secret = os.environ.get("secret")  # online ▼
telegram.message_send(secret)

SCOPES = ['https://www.googleapis.com/auth/tasks.readonly']

def authenticate():
    """Аутентификация пользователя и получение учетных данных."""

    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    telegram.message_send(creds)
    return creds

def print_all_tasks():
    """Получение и печать всех задач."""
    # Аутентификация пользователя
    creds = authenticate()

    # Создание объекта сервиса
    service = build('tasks', 'v1', credentials=creds)

    # Получение списка задач
    tasks_message = ''
    tasklists = service.tasklists().list().execute()
    for tasklist in tasklists['items']:
        if 'ToDo' not in tasklist['title']:
            continue
        list_name_line = f"Задачи в списке: {tasklist['title']}"
        # print(list_name_line)
        tasks_message += f'{list_name_line}\n\n'
        tasks = service.tasks().list(tasklist=tasklist['id']).execute()
        n = 1
        if 'items' in tasks and len(tasks['items']) > 0:
            for task in tasks['items']:
                tasks_message += f"{n}. {task['title']}\n"
                n += 1
        else:
            tasks_message = f"В списке: '{tasklist['title']}' нет задач."
    telegram.message_send(tasks_message)


if __name__ == '__main__':
    print_all_tasks()
