from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboard import K

from lexicon.lexicon import LEXICON_RU, LEXICON_COMMANDS

from FSM import FSMUser

from config import config

if __name__ == '__main__':
    from bot.lexicon.lexicon import LEXICON_COMMANDS, LEXICON_RU
from db import UserBase
from db.create_db import UserRow

"""start bot handler and choosing user"""
start_router = Router()


@start_router.message(F.text == '/start')
async def send_comics(message: Message, state: FSMContext):
    UserBase.write_user(UserRow(message.from_user.id))
    await state.set_state(FSMUser.user)
    await message.answer(text=LEXICON_RU['/start'], reply_markup=K.create_comics_kb())


@start_router.message(F.text == '/switch_user')
async def change_role_to_admin(message: Message, state: FSMContext):
    if message.from_user.id in config.tg_bot.admins:
        await state.set_state(FSMUser.admin)
        await message.answer(text=LEXICON_COMMANDS['switch_user'])
