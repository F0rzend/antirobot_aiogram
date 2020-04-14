from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_start(message: types.Message):
    await message.answer(message.text)
