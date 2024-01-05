from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, types

import db_helper
from bot_controller.services import logs
from models import async_session


class DbTransactionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[types.TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: types.TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        async with async_session() as session:
            data["session"] = session
            return await handler(event, data)


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[types.TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: types.TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        session = data["session"]
        data["user"] = await db_helper.get_or_create_user(session, event.message)
        return await handler(event, data)


class AutoReplyMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[types.TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: types.TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        message = event.message
        logs.log_bot_incomming_message(message)
        result = await handler(event, data)
        logs.log_bot_outgoing_message(message, result)

        if result is not None:
            await message.reply(text=result, disable_web_page_preview=False)
