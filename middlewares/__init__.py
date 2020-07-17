from aiogram import Dispatcher
from loguru import logger

from .throttling import ThrottlingMiddleware


def setup_middlewares(dp: Dispatcher):
    logger.info("Установка middlewares...")
    dp.middleware.setup(ThrottlingMiddleware())
