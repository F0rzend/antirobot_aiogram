import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import CantRestrictSelf

from data.permissions import new_user_added, user_allowed
from filters import IsGroup
from keyboards.inline import generate_confirm_markup, confirming_callback
from loader import bot
from loader import dp
from states import ConfirmUserState


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message, state: FSMContext):
    """
    Обрабатываем вход нового пользователя
    """
    # Пропускаем старые запросы
    if message.date < datetime.datetime.now() - datetime.timedelta(minutes=1):
        return

    try:
        # сразу выдаём ему права, неподтверждённого пользователя
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.new_chat_members[0].id,
            permissions=new_user_added,
        )
    except CantRestrictSelf:
        return
    # Каждому пользователю отсылаем кнопку
    for i, new_member in enumerate(message.new_chat_members):
        confirm_markup = generate_confirm_markup(message.new_chat_members[i].id)
        await message.reply(
            (
                f"{new_member.get_mention(as_html=True)}, добро пожаловать в чат!\n"
                f"Подтверди, что ты не бот и нажми на {confirm_markup[1]}"
            ),
            reply_markup=confirm_markup[0]
        )
        await state.update_data(subject=confirm_markup[1])
        await ConfirmUserState.ConfirmUser.set()


@dp.callback_query_handler(confirming_callback.filter(), state=ConfirmUserState.IncomerUser)
async def user_confirm(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    print(1231)
    """
    Хэндлер обрабатывающий нажатие на кнопку
    """

    # сразу получаем все необходимые нам переменные,а именно
    # существо (человек или бот)
    subject = callback_data.get("subject")
    # айди пользователя (приходит строкой, поэтому используем int)
    user_id = int(callback_data.get("user_id"))

    data = await state.get_data()
    needed_subject = data.get("subject")
    print(subject)
    print(needed_subject)
    # и айди чата, для последнующей выдачи прав
    chat_id = int(query.message.chat.id)

    # если на кнопку нажал не только что вошедший пользователь, говорим, чтобы не лез и игнорируем (выходим из функции).
    if query.from_user.id != user_id:
        await query.answer("Эта кнопочка не для тебя", show_alert=True)
        return

    # не забываем выдать юзеру необходимые права
    if subject == needed_subject:
        await bot.restrict_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            permissions=user_allowed,
        )

    # и убираем часики
    await query.answer('123')

    # а также удаляем сообщение, чтобы пользователь в RO не мог получить права
    await query.message.delete()
    await state.finish()
