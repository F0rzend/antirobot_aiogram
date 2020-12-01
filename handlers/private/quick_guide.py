from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ChatType

from loguru import logger

from loader import dp


@dp.message_handler(Command('quick_guide'), chat_type='private')
async def quick_guide(message: types.Message):
    logger.debug(f'User @{message.from_user.username}:{message.from_user.id} needs help')
    answer = '\n'.join([
        'Окей, давай по порядку. Для начала, тебе нужно добавить меня в группу. Я думаю с этим ты разберёшься сам',
        'Потом, чтобы я мог кикать спамящих мудаков, мне нужны некоторые права администратора:\n',
        '1) В первую очередь возможность отправлять сообщения, это само собой\n',
        '2) Далее, я думаю ты понимаешь, что у меня должна быть возможность банить пользователя ' 
        'и это право мне тоже необходимо\n',
        '3) Не будем забывать о лишних сообщениях, которые по-хорошему б удалять, чтобы не было спама. ' 
        'Так сказать затирать следы. И для этого мне нужна возможность удалять сообщения. ' 
        'Я думаю ты понимаешь, что делать\n',
        'Завершив это, я смогу кикать тех, кто не способен нажать на кнопку, и в твоём чате не будет ботов'
    ])
    await message.answer(text=answer)
