from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto

from keyboard import K
from db import UserBase, DataBase
from db.create_db import UserRow

reading_router = Router()


@reading_router.callback_query(F.data == 'forward')
async def send_next_page(callback: CallbackQuery):
    user_id = callback.from_user.id
    new_page = UserBase.get_page(user_id)[0][0] + 1

    user_comics = UserBase.get_comics(user_id)[0][0]

    last_page = DataBase.get_last_page(table_name=user_comics)
    if new_page == last_page:
        pass
    comic_path: str = DataBase.get_comics_by_name(user_comics, new_page)

    UserBase.write_user(UserRow(telegram_id=callback.from_user.id, page=new_page, comics=user_comics))
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile(comic_path)),
        reply_markup=K.create_main_inline(new_page),
    )


@reading_router.callback_query(F.data == 'back')
async def send_prev_page(callback: CallbackQuery):
    pass


@reading_router.callback_query(F.data == 'to first')
async def send_first_page(callback: CallbackQuery):
    pass
