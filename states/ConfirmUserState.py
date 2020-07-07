from aiogram.dispatcher.filters.state import StatesGroup, State


class ConfirmUserState(StatesGroup):
    IncomerUser = State()
