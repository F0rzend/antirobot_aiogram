from aiogram import types
from aiogram.utils.markdown import hbold
from loguru import logger

from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate())
async def start(message: types.Message):
    logger.debug("New user")
    admin_markup = types.InlineKeyboardMarkup(row_width=3)
    admin_markup.insert(
        types.InlineKeyboardButton(
            text="Разработчик",
            url="https://t.me/Kyle167"
        ),
    )

    await message.answer(f"Привет, {hbold(message.from_user.full_name)}\n\n"
                         "Я простой антибот\n\n"
                         "Чтобы я мог приступить к работе, добавь меня в чат, "
                         "сделай админом и дай право менять права пользователей и отправлять сообщения\n\n",
                         "Об ошибке вы можете сообщить разработчику",
                         reply_markup=admin_markup
    )
