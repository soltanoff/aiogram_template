import logging

import sqlalchemy as sa
from aiogram import types
from sqlalchemy.ext.asyncio import AsyncSession

from models import User

# Common prebuilt queries
STMT_USER = sa.select(User)


async def get_or_create_user(session: AsyncSession, message: types.Message) -> User:
    user_id = message.from_user.id
    user = (await session.scalars(STMT_USER.where(User.external_id == user_id))).one_or_none()
    if user is None:
        user = User()
        user.external_id = user_id
        await session.merge(user)
        await session.commit()
        logging.info("[%s] New user added", user.external_id)

    return user
