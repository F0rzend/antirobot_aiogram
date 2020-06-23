from aiogram import Dispatcher


from .chat_filters import IsGroup, IsPrivate


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
