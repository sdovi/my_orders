from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext

# Определение состояний
SOURCE_CHANNEL, TARGET_CHANNEL, PARSE_TYPE, WITH_SIGNATURE, WITHOUT_SIGNATURE = range(5)

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
    keyboard = [['С подписью', 'Без подписи']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text('Выберите тип парсинга:', reply_markup=reply_markup)
    return PARSE_TYPE

async def parse_type(update: Update, context: CallbackContext) -> int:
    parse_type = update.message.text
    context.user_data['parse_type'] = parse_type

    if parse_type == 'С подписью':
        await update.message.reply_text(f'Выбран тип парсинга: {parse_type}. Запуск пересылки последних 10 сообщений с подписью.')
        return WITH_SIGNATURE
    elif parse_type == 'Без подписи':
        await update.message.reply_text(f'Выбран тип парсинга: {parse_type}. Запуск пересылки последних 10 сообщений без подписи.')
        return WITHOUT_SIGNATURE
    else:
        await update.message.reply_text('Выберите один из предложенных вариантов.')
        return PARSE_TYPE

async def with_signature(update: Update, context: CallbackContext) -> int:
    # Добавьте логику для пересылки сообщений с подписью
    return ConversationHandler.END

async def without_signature(update: Update, context: CallbackContext) -> int:
    # Добавьте логику для пересылки сообщений без подписи
    return ConversationHandler.END

def main():
    application = Application.builder().token("5836893149:AAGwVrLzM9CTQOUXVe2eIPWpC70olIfUG0A").build()

    conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        SOURCE_CHANNEL: [MessageHandler(filters.Text() & (~filters.Command()), get_source_channel)],
        TARGET_CHANNEL: [MessageHandler(filters.Text() & (~filters.Command()), get_target_channel)],
        PARSE_TYPE: [MessageHandler(filters.Text() & (~filters.Command()), parse_type)],
        WITH_SIGNATURE: [MessageHandler(filters.Text() & (~filters.Command()), with_signature)],
        WITHOUT_SIGNATURE: [MessageHandler(filters.Text() & (~filters.Command()), without_signature)],
    },
    fallbacks=[],
)



    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == '__main__':
    main()
