from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from keyboard import K

from db import DataBase, UserBase
from db.create_db import UserRow

comics_router = Router()


@comics_router.message(F.text.in_({str(name[0]) for name in DataBase}))
async def send_comics(message: Message):
    path = DataBase.get_comics_by_name(message.text)
    UserBase.write_user(UserRow(message.from_user.id, comics=message.text))
    await message.answer_photo(photo=FSInputFile(path), reply_markup=K.create_main_inline(1))
