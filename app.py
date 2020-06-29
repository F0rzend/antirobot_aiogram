from loader import bot, storage
from data.config import SKIP_UPDATES, NUM_BUTTONS


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    if NUM_BUTTONS in range(2, 8):
        executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=SKIP_UPDATES)
    else:
        raise AttributeError('количество кнопок не может быть меньше 2х или больше 7и')
