from aiogram import types
from sqlalchemy.ext.asyncio import AsyncSession

from bot_controller.router import Router
from models import User

router = Router(name=__name__)


@router.register(
    command="start",
    description="base command for user registration",
)
@router.register(
    command="help",
    description="view all commands",
)
async def send_welcome(*_) -> str:
    return "\n".join(router.command_list)


@router.register(
    command="hello",
    description="just hello command",
)
async def hello(*_) -> str:
    return "Well, hello!"


@router.register(
    command="user_info",
    description="user info",
)
async def user_info(message: types.Message, session: AsyncSession, user: User) -> str:  # noqa; pylint: disable=unused-argument
    return f"User ID: {user.external_id}\nChat ID: {message.chat.id}\nRegistration date: {user.created_at}"


@router.register()
async def echo(message: types.Message, *_) -> str:
    return message.text
