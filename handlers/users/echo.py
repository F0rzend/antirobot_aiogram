from aiogram import types
from bot import dp


@dp.message_handler()
async def bot_start(message: types.Message):
    await message.answer(message.text)
