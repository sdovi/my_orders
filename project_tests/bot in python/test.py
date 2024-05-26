from telethon.sync import TelegramClient
from datetime import datetime, timedelta, timezone
import re

api_id = '21939961'
api_hash = 'af19f9947ea913111917a013632d8949'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Подключение к аккаунту
    await client.start()
    
    # название канала, который нужно парсить
    channel_username = 'vykup2'
    # vykup2
    # Определяем дату, 3 месяца назад
    three_months_ago = datetime.now(timezone.utc) - timedelta(days=90)
    
    # Создаем регулярное выражение для поиска упоминаний пользователей в тексте сообщения
    username_pattern = re.compile(r'@[\w\d_]+')
    
    # Получаем все сообщения из канала
    async for message in client.iter_messages(channel_username):
        if message.date > three_months_ago and message.text:
            # Ищем упоминания пользователей в тексте сообщения
            matches = username_pattern.findall(message.text)
            # Записываем найденные упоминания в файл
            if matches:
                with open(f"{channel_username}.txt", "a", encoding="utf-8") as file:
                    file.write(' '.join(matches) + "\n")
    
    print(f"Упоминания пользователей из канала {channel_username}, найденные за последние 3 месяца, записаны в файл {channel_username}.txt")

# Запускаем асинхронную функцию main()
with client:
    client.loop.run_until_complete(main())
