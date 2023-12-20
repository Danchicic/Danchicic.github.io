from aiogram.filters.state import State, StatesGroup


# user state model
class FSMUser(StatesGroup):
    user = State()
    admin = State()
