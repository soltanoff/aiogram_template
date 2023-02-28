import logging
import os
import time
from datetime import timedelta

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('TELEGRAM_API_KEY'))
dp = Dispatcher(bot)
SLEEP_AFTER_EXCEPTION = timedelta(minutes=1).seconds


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    chat_id: int = message.chat.id
    user_id: str = message.from_user.id
    username: str = message.from_user.username
    request_message: str = message.text

    await message.answer_chat_action('typing')
    logging.info('>>> User[%s|%s:@%s]: %r', chat_id, user_id, username, request_message)
    await message.reply('Well, hello!')


@dp.message_handler()
async def echo(message: types.Message):
    chat_id: int = message.chat.id
    user_id: str = message.from_user.id
    username: str = message.from_user.username
    request_message: str = message.text

    await message.answer_chat_action('typing')
    logging.info('>>> User[%s|%s:@%s]: %r', chat_id, user_id, username, request_message)
    logging.info('<<< User[%s|%s:@%s]: %r', chat_id, user_id, username, request_message)
    await message.answer(request_message)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.getLevelName(os.getenv('LOG_LEVEL')),
        format='%(levelname)9s | %(asctime)s | %(name)30s | %(filename)20s | %(lineno)6s | %(message)s',
    )

    while True:
        try:
            executor.start_polling(dp, skip_updates=True)
        except Exception as ex:
            logging.error('Error found: %r. Restarting...', ex)
            time.sleep(SLEEP_AFTER_EXCEPTION)
