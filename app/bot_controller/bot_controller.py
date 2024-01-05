import logging
from asyncio import CancelledError

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiohttp.web_runner import GracefulExit

from bot_controller import middlewares, services


class BotController:
    MIDDLEWARES = [
        middlewares.DbTransactionMiddleware,
        middlewares.UserMiddleware,
        middlewares.AutoReplyMiddleware,
    ]
    ROUTERS = [
        services.subscriptions_router,
    ]

    def __init__(self, telegram_api_key: str):
        self._bot = Bot(token=telegram_api_key)
        self._dispatcher = Dispatcher()

        self._register_middlewares()
        self._register_routers()

    async def start(self):
        try:
            await self._dispatcher.start_polling(self._bot)
        except Exception as error:
            logging.exception("Unexpected error: %r", error, exc_info=error)
        except (GracefulExit, KeyboardInterrupt, CancelledError):
            logging.info("Bot graceful shutdown...")

    async def send_message(self, user_external_id: int, answer: str, parse_mode=ParseMode.HTML):
        await self._bot.send_message(user_external_id, answer, parse_mode=parse_mode)

    def _register_middlewares(self):
        for middleware in self.MIDDLEWARES:
            self._dispatcher.update.outer_middleware.register(middleware())

    def _register_routers(self):
        self._dispatcher.include_routers(*self.ROUTERS)
