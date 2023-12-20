from aiogram import Router, F
from aiogram.types import Message
from keyboard import K
from aiogram.filters import CommandStart

from db import UserBase
from db.create_db import UserRow

start_router = Router()


@start_router.message(F.text == '/start')
async def send_comics(message: Message):
    UserBase.write_user(UserRow(message.from_user.id))
    print(message.chat.id)
    await message.answer(text='Выбери подходящий комикс', reply_markup=K.create_comics_kb())
