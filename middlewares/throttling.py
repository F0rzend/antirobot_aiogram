import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled
from loguru import logger

from utils.misc.phrase_generator import throttled_answers_generator


class ThrottlingMiddleware(BaseMiddleware):
    """
    Стандартный middleware для предотвращение спама через throttling
    """

    def __init__(self, limit: int = DEFAULT_RATE_LIMIT, key_prefix: str = 'antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    # noinspection PyUnusedLocal
    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await self.message_throttled(message, t)
            raise CancelHandler()

    async def message_throttled(self, message: types.Message, throttled: Throttled):
        handler = current_handler.get()
        logger.debug(f'@{message.from_user.username}:{message.from_user.id} спамит командой {message.text}')
        limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)
        delta = throttled.rate - throttled.delta
        if throttled.exceeded_count <= 2:

            await message.reply(text=throttled_answers_generator(limit=limit))
        await asyncio.sleep(delta)
