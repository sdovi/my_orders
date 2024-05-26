from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext
from telethon.sync import TelegramClient, events

# Определение состояний
SOURCE_CHANNEL, TARGET_CHANNEL = range(2)

# Ваши учетные данные для доступа к Telegram API
api_id = '21939961'
api_hash = 'af19f9947ea913111917a013632d8949'

async def start(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Привет! Пожалуйста, введи SOURCE_CHANNEL (имя канала, из которого хотите копировать сообщения).')
    return SOURCE_CHANNEL

async def get_source_channel(update: Update, context: CallbackContext) -> int:
    context.user_data['source_channel'] = update.message.text
    await update.message.reply_text('Теперь введи TARGET_CHANNEL (имя канала, в который хотите пересылать сообщения).')
    return TARGET_CHANNEL

async def get_last_10_posts(client, channel_name):
    try:
        # Получаем входную сущность канала по его имени
        channel_entity = await client.get_entity(channel_name)
        # Получаем последние 10 сообщений из канала
        messages = await client.get_messages(channel_entity, limit=5)
        return messages
    except Exception as e:
        print(f'Ошибка при получении сообщений из канала: {e}')
        return []

async def get_target_channel(update: Update, context: CallbackContext) -> int:
    context.user_data['target_channel'] = update.message.text
    await update.message.reply_text('Настройка завершена. Бот начнет пересылку последних 10 сообщений.')

    # Авторизация в Telegram с использованием ваших учетных данных
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()

    try:
        # Получаем последние 10 сообщений из исходного канала
        source_messages = await get_last_10_posts(client, context.user_data['source_channel'])
        target_entity = await client.get_input_entity(context.user_data['target_channel'])
    except Exception as e:
        await update.message.reply_text(f'Произошла ошибка: {e}')
        return ConversationHandler.END

    # Пересылаем каждое сообщение в целевой канал
    for message in source_messages:
        await client.forward_messages(target_entity, message)

    # Запуск клиента Telegram
    await client.run_until_disconnected()

    return ConversationHandler.END

def main():
    application = Application.builder().token("5836893149:AAGwVrLzM9CTQOUXVe2eIPWpC70olIfUG0A").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SOURCE_CHANNEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_source_channel)],
            TARGET_CHANNEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_target_channel)],
        },
        fallbacks=[],
    )

    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == '__main__':
    main()
