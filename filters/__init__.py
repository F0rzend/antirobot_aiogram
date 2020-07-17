from aiogram import Dispatcher
from loguru import logger

from .chat_filters import IsGroup, IsPrivate


def setup_filters(dp: Dispatcher):
    logger.info("Установка фильтров")
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
