from data.config import SKIP_UPDATES, NUM_BUTTONS
from loguru import logger


async def on_startup(dispatcher):
    import filters
    import middlewares
    filters.setup(dispatcher)
    middlewares.setup(dispatcher)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dispatcher)
    logger.info(f"The bot is running")


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    if NUM_BUTTONS in range(2, 8):
        logger.level('INFO')
        executor.start_polling(dp, on_startup=on_startup, skip_updates=SKIP_UPDATES)
    else:
        raise AttributeError('количество кнопок не может быть меньше 2х или больше 7и')
