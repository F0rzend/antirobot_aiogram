from random import choice

from aiogram.utils.markdown import hbold

from data.phrases import users_entrance


def users_entrance_generator(mention: str, subject: str) -> str:
    return choice(users_entrance).format(mention=mention, subject=hbold(subject))
