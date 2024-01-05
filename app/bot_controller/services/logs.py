import logging

from aiogram import types


def log_bot_incomming_message(message: types.Message):
    logging.info(
        "User[%s|%s:@%s]: %r",
        message.chat.id,
        message.from_user.id,
        message.from_user.username,
        message.text,
    )


def log_bot_outgoing_message(message: types.Message, answer: str):
    logging.info(
        "<<< User[%s|%s:@%s]: %r",
        message.chat.id,
        message.from_user.id,
        message.from_user.username,
        answer,
    )
