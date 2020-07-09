from aiogram import types
from aiogram.utils.markdown import bold
from loguru import logger

from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate())
async def start(message: types.Message):
    logger.debug(f"@{message.from_user.username}:{message.from_user.id} in Start handler")
    admin_markup = types.InlineKeyboardMarkup(row_width=3)
    admin_markup.insert(
        types.InlineKeyboardButton(
            text="Разработчик",
            url="https://t.me/Forzend"
        )
    )

    await message.answer(
        text=''.join(
            (
                f"Привет, {bold(message.from_user.full_name)}\n\n",
                "Я простой антибот\n",
                "Чтобы я мог приступить к работе, добавь меня в чат, ",
                "сделай админом и дай право менять права пользователей и отправлять сообщения\n\n",
                "Об ошибке вы можете сообщить разработчику"
            )
        ),
        parse_mode='MARKDOWN',
        reply_markup=admin_markup
    )
