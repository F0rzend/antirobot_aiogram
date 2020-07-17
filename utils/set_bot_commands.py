from aiogram import types
from loguru import logger


async def set_default_commands(dp):
    logger.info('Установка комманд бота...')
    await dp.bot.set_my_commands([
        types.BotCommand("developer", "Разработчик"),
    ])
