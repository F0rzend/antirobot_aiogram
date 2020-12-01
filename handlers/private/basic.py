from aiogram import types
from aiogram.utils.markdown import hbold
from loguru import logger

from loader import dp


@dp.message_handler(chat_type='private')
async def default(message: types.Message):
    logger.debug(f"@{message.from_user.username}:{message.from_user.id} in default handler")
    admin_markup = types.InlineKeyboardMarkup(row_width=3)
    admin_markup.insert(
        types.InlineKeyboardButton(
            text="Написать разработчику",
            url="https://t.me/Forzend"
        )
    )

    await message.answer(
        text=''.join(
            (
                f"Привет, {hbold(message.from_user.full_name)}\n\n",
                "Я простой антибот\n",
                "Я могу помочь тебе с установкой бота, для этого отправь мне /quick_guide\n\n",
                "Об ошибке вы можете сообщить разработчику"
            )
        ),
        reply_markup=admin_markup
    )
