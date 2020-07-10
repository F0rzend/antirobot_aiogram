import datetime
import asyncio

from aiogram.utils.exceptions import CantRestrictSelf

from aiogram import types
from loguru import logger

from data.config import ENTRY_TIME
from data.config import BAN_TIME

from data.permissions import new_user_added
from data.permissions import user_allowed
from filters import IsGroup
from keyboards.inline import generate_confirm_markup
from keyboards.inline import confirming_callback
from loader import bot
from loader import dp
from loader import storage
from states import ConfirmUserState
from utils.misc import users_entrance_generator


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    """
    Обрабатываем вход нового пользователя
    """

    logger.debug(
        f"New chat member: @{message.from_user.username}:{message.from_user.id} -> "
        f"{', '.join([f'@{user.username}:{user.id}' for user in message.new_chat_members])} "
        f'in chat "{message.chat.title}@{message.chat.username}" chat_id:{message.chat.id}'
    )
    # Пропускаем старые запросы
    if message.date < datetime.datetime.now() - datetime.timedelta(minutes=1):
        return logger.debug('Old updates was skipped')

    for new_member in message.new_chat_members:
        try:
            # сразу выдаём ему права, неподтверждённого пользователя
            await bot.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=new_member.id,
                permissions=new_user_added,
            )
            logger.debug(f'User @{new_member.username}:{new_member.id} cannot send messages now')
        except CantRestrictSelf:
            return logger.debug('Can\'t restrict self')

    # Каждому пользователю отсылаем кнопку
    for new_member in message.new_chat_members:
        generated_tuple = generate_confirm_markup(new_member.id)
        markup = generated_tuple[0]
        subject = generated_tuple[1]
        answer = users_entrance_generator(mention=new_member.get_mention(as_html=True), subject=subject)
        service_message: types.Message = await message.reply(
            text=answer,
            reply_markup=markup
        )
        logger.debug(f'User @{new_member.username}:{new_member.id} '
                     f'got message {service_message.message_id} with keyboard')
        await storage.set_state(chat=message.chat.id, user=new_member.id, state=ConfirmUserState.IncomerUser)
        logger.debug(f'User @{new_member.username}:{new_member.id} in state "IncomerUser"')
        state = dp.current_state(user=new_member.id, chat=message.chat.id)
        await state.update_data(user_id=new_member.id)
        logger.debug(f'@{new_member.username}:{new_member.id} user data has been updated')

    logger.debug(f'The bot waits {ENTRY_TIME} seconds '
                 f'for {", ".join([user.username for user in message.new_chat_members])}')
    await asyncio.sleep(ENTRY_TIME)
    for new_member in message.new_chat_members:
        state = dp.current_state(user=new_member.id, chat=message.chat.id)
        data = await state.get_data()
        if data.get('user_id', None):
            logger.debug(f'User @{new_member.username}:{new_member.id} data: {data}')
            until_date = datetime.datetime.now() + datetime.timedelta(seconds=BAN_TIME)
            await bot.kick_chat_member(chat_id=message.chat.id, user_id=new_member.id, until_date=until_date)
            logger.debug(f'User was kicked from chat @{new_member.username}:{new_member.id} on {BAN_TIME} seconds')


@dp.callback_query_handler(confirming_callback.filter())
async def user_confirm(query: types.CallbackQuery, callback_data: dict):
    """
    Хэндлер обрабатывающий нажатие на кнопку
    """

    # сразу получаем все необходимые нам переменные, а именно
    # предмет, на который нажал пользователь
    subject = callback_data.get("subject")
    # предмет на который пользователь должен был нажать
    necessary_subject = callback_data.get('necessary_subject')
    # айди пользователя (приходит строкой, поэтому используем int)
    user_id = int(callback_data.get("user_id"))
    # и айди чата, для последнующей выдачи прав
    chat_id = int(query.message.chat.id)
    logger.debug(f'User {query.from_user.username} clicked on button: {subject}({necessary_subject}) in chat {chat_id}')
    # если на кнопку нажал не только что вошедший пользователь, говорим, чтобы не лез и игнорируем (выходим из функции).
    if query.from_user.id != user_id:
        logger.debug(f'The wrong user clicked on the button @{query.from_user.username}:{query.from_user.id}')
        return await query.answer("Эта кнопочка не для тебя", show_alert=True)

    # не забываем выдать юзеру необходимые права если он нажал на правильную кнопку
    if subject == necessary_subject:
        await bot.restrict_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            permissions=user_allowed,
        )
        logger.debug(f'Rights have been granted to the user @{query.from_user.username}:{query.from_user.id}')
    else:
        until_date = datetime.datetime.now() + datetime.timedelta(seconds=BAN_TIME)
        await bot.kick_chat_member(chat_id=chat_id, user_id=user_id, until_date=until_date)
        logger.debug(f'The user @{query.from_user.username}:{query.from_user.id} clicked on the wrong object '
                     f'and was banned until {until_date}')

    state = dp.current_state(user=query.from_user.id, chat=query.message.chat.id)
    await state.finish()
    logger.debug(f'User @{query.from_user.username}:{query.from_user.id} is out of the state')

    # и убираем часики
    await query.answer()

    # а также удаляем сообщение, чтобы пользователь в RO не мог получить права
    service_message = query.message
    await service_message.delete()
    logger.debug(f'Message {service_message.message_id} was deleted')
