import asyncio
import logging
import os

from bot_controller import BotController


async def main() -> None:
    bot_controller = BotController(os.getenv("TELEGRAM_API_KEY"))
    await bot_controller.start()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)9s | %(asctime)s | %(name)30s | %(filename)20s | %(lineno)6s | %(message)s",
        force=True,
    )
    asyncio.run(main())
