import random
from typing import Tuple

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

# создём CallbackData для удобного парсинга калбеков
confirming_callback = CallbackData("confirm", "subject", "user_id")


def generate_confirm_markup(user_id: int) -> Tuple[InlineKeyboardMarkup, str]:
    """
    Функция, создающая клавиатуру для подтверждения, что пользователь не является ботом
    """
    # создаём инлайн клавиатуру
    confirm_user_markup = InlineKeyboardMarkup(row_width=5)
    all_buttons = [
        InlineKeyboardButton(u'\U0001F48D', callback_data=confirming_callback.new(subject="ring", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F460', callback_data=confirming_callback.new(subject="shoe", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F451', callback_data=confirming_callback.new(subject="crown", user_id=user_id)),
        InlineKeyboardButton(u'\U00002702', callback_data=confirming_callback.new(subject="scissors", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F941', callback_data=confirming_callback.new(subject="drum", user_id=user_id)),

        InlineKeyboardButton(u'\U0001F48A', callback_data=confirming_callback.new(subject="pill", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F338', callback_data=confirming_callback.new(subject="blossom", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F9C0', callback_data=confirming_callback.new(subject="cheese", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F3A7', callback_data=confirming_callback.new(subject="headphone", user_id=user_id)),
        InlineKeyboardButton(u'\U000023F0', callback_data=confirming_callback.new(subject="clock", user_id=user_id)),

        InlineKeyboardButton(u'\U0001F951', callback_data=confirming_callback.new(subject="avocado", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F334', callback_data=confirming_callback.new(subject="palm", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F45C', callback_data=confirming_callback.new(subject="handbag", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F9E6', callback_data=confirming_callback.new(subject="socks", user_id=user_id)),
        InlineKeyboardButton(u'\U0001FA93', callback_data=confirming_callback.new(subject="axe", user_id=user_id)),

        InlineKeyboardButton(u'\U0001F308', callback_data=confirming_callback.new(subject="rainbow", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F4A7', callback_data=confirming_callback.new(subject="droplet", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F525', callback_data=confirming_callback.new(subject="fire", user_id=user_id)),
        InlineKeyboardButton(u'\U000026C4', callback_data=confirming_callback.new(subject="snowman", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F9F2', callback_data=confirming_callback.new(subject="magnet", user_id=user_id)),

        InlineKeyboardButton(u'\U0001F389', callback_data=confirming_callback.new(subject="popper", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F339', callback_data=confirming_callback.new(subject="rose", user_id=user_id)),
        InlineKeyboardButton(u'\U0000270E', callback_data=confirming_callback.new(subject="pencil", user_id=user_id)),
        InlineKeyboardButton(u'\U00002709', callback_data=confirming_callback.new(subject="envelope", user_id=user_id)),
        InlineKeyboardButton(u'\U0001F680', callback_data=confirming_callback.new(subject="rocket", user_id=user_id)),
    ]

    subjects = list()
    for button in random.sample(all_buttons, 5):
        subjects.append(button.callback_data)
        confirm_user_markup.insert(button)

    # отдаём клавиатуру после создания
    return confirm_user_markup, random.choice(subjects)
