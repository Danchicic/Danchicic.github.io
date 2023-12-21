from aiogram import Router, F
from aiogram.filters import StateFilter

from FSM import FSMUser
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from lexicon.lexicon import LEXICON_ADMIN

"""admins handlers"""
admin_router = Router()
admin_router.message.filter(StateFilter(FSMUser.admin))


@admin_router.message(F.text == '/q')
async def left_admin_panel(message: Message, state: FSMContext):
    await state.set_state(FSMUser.user)
    await message.answer(text=LEXICON_ADMIN['/q'])


@admin_router.message()
async def start_admin_panel(message: Message):
    await message.answer(text='Вы в панели админа')
