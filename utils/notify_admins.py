from loguru import logger

from aiogram import Dispatcher

from data.config import ADMINS_ID


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS_ID:
        try:
            await dp.bot.send_message(admin, "Бот Запущен", disable_notification=True)

        except Exception as err:
            logger.exception(err)
