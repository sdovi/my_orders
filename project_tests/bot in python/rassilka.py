import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, PhoneCodeExpiredError

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Определение состояний
API_ID, API_HASH, PHONE, CODE, SOURCE_CHANNEL, TARGET_CHANNEL = range(6)

# Словарь для хранения данных пользователя
user_data = {}

async def start(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Привет! Пожалуйста, введи свой API ID.')
    return API_ID

async def get_api_id(update: Update, context: CallbackContext) -> int:
    user_data['api_id'] = update.message.text
    await update.message.reply_text('Отлично! Теперь введи свой API Hash.')
    return API_HASH

async def get_api_hash(update: Update, context: CallbackContext) -> int:
    user_data['api_hash'] = update.message.text
    await update.message.reply_text('Спасибо! Теперь введи свой номер телефона с кодом страны.')
    return PHONE

async def get_phone(update: Update, context: CallbackContext) -> int:
    user_data['phone'] = update.message.text
    # Создаем клиент Telethon
    client = TelegramClient('anon', user_data['api_id'], user_data['api_hash'])
    user_data['client'] = client

    try:
        await client.connect()
        if not await client.is_user_authorized():
            try:
                await client.send_code_request(user_data['phone'])
            except SessionPasswordNeededError:
                await update.message.reply_text('Пожалуйста, введите ваш пароль двухфакторной аутентификации.')
                return
    except Exception as e:
        logger.error("Ошибка при отправке кода: %s", e)
        await update.message.reply_text('Произошла ошибка при отправке кода. Попробуйте снова.')
        return ConversationHandler.END

    await update.message.reply_text('Код подтверждения был отправлен на ваш номер. Пожалуйста, введите код.')
    return CODE

async def get_code(update: Update, context: CallbackContext) -> int:
    user_data['code'] = update.message.text

    try:
        await user_data['client'].sign_in(user_data['phone'], user_data['code'])
    except PhoneCodeExpiredError:
        await update.message.reply_text('Код подтверждения истек. Пожалуйста, запросите новый код.')
        return PHONE
    except SessionPasswordNeededError:
        await update.message.reply_text('Пожалуйста, введите ваш пароль двухфакторной аутентификации.')
        return
    except Exception as e:
        logger.error("Ошибка при вводе кода: %s", e)
        await update.message.reply_text('Произошла ошибка при вводе кода. Попробуйте снова.')
        return ConversationHandler.END

    await update.message.reply_text('Успешно авторизованы! Теперь введи исходный канал (с @).')
    return SOURCE_CHANNEL

async def get_source_channel(update: Update, context: CallbackContext) -> int:
    user_data['source_channel'] = update.message.text
    await update.message.reply_text('Теперь введи целевой канал (с @).')
    return TARGET_CHANNEL

async def get_target_channel(update: Update, context: CallbackContext) -> int:
    user_data['target_channel'] = update.message.text
    await update.message.reply_text('Настройка завершена. Бот начнет пересылку сообщений.')

    try:
        async for message in user_data['client'].iter_messages(user_data['source_channel']):
            await user_data['client'].send_message(user_data['target_channel'], message)
    except Exception as e:
        logger.error("Ошибка при пересылке сообщений: %s", e)
        await update.message.reply_text('Произошла ошибка при пересылке сообщений. Попробуйте снова.')
        return ConversationHandler.END

    return ConversationHandler.END

async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Отменено. Если хочешь попробовать снова, напиши /start.')
    return ConversationHandler.END

def main():
    application = Application.builder().token("5836893149:AAGwVrLzM9CTQOUXVe2eIPWpC70olIfUG0A").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            API_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_api_id)],
            API_HASH: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_api_hash)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_code)],
            SOURCE_CHANNEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_source_channel)],
            TARGET_CHANNEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_target_channel)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == '__main__':
    main()
