from functools import wraps
from typing import Callable, Optional

from aiogram import types


def skip_empty_command(command: str) -> Callable:
    command_len = len(command) + 1
    error_answer = "Empty message? Please, check /help"

    def decorator(handler: Callable) -> Callable:
        @wraps(handler)
        async def wrapper(message: types.Message, *args, **kwargs) -> Optional[str]:
            request_message: str = message.text[command_len:].strip()
            if not request_message:
                return error_answer

            return await handler(message, *args, **kwargs)

        return wrapper

    return decorator
