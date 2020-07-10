from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hlink

from loader import dp


@dp.message_handler(Command('developer'))
async def developer(message: types.Message):
    await message.answer(f'Меня создал {hlink(title="Forzend", url="tg://user?id=525340304")}')
