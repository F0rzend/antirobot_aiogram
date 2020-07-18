from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hlink
from loguru import logger

from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=60)
@dp.message_handler(Command('developer'))
async def developer(message: types.Message):
    logger.debug(f'User @{message.from_user.username}:{message.from_user.id} looking for a developer')
    await message.answer(f'Меня создал {hlink(title="Forzend", url="tg://user?id=525340304")}')
