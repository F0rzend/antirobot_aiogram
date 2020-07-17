from aiogram import Dispatcher
from aiogram import executor

from data.config import SKIP_UPDATES, NUM_BUTTONS
from loguru import logger
from loader import dp

from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.logger_config import setup_logger
from filters import setup_filters
from middlewares import setup_middlewares


async def on_startup(dispatcher: Dispatcher):
    setup_logger()
    setup_filters(dispatcher)
    logger.info("Установка обработчиков...")
    # Установка обработчиков производится посредством декораторов. Для этого достаточно просто импортировать модуль
    import handlers
    setup_middlewares(dispatcher)

    await on_startup_notify(dispatcher)
    await set_default_commands(dispatcher)
    logger.info(f"Бот успешно запущен...")


if __name__ == '__main__':
    if NUM_BUTTONS in range(2, 8):
        executor.start_polling(dp, on_startup=on_startup, skip_updates=SKIP_UPDATES)
    else:
        raise AttributeError('количество кнопок не может быть меньше 2х или больше 7и')
