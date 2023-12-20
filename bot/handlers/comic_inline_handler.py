from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto

from keyboard import K
from db import UserBase, DataBase
from db.create_db import UserRow
from lexicon.lexicon import LEXICON_RU
"""reading handlers"""
reading_router = Router()


@reading_router.callback_query(F.data == 'forward')
async def send_next_page(callback: CallbackQuery):
    user_id = callback.from_user.id
    new_page = UserBase.get_page(user_id)[0][0] + 1

    user_comics = UserBase.get_comics(user_id)[0][0]

    last_page = DataBase.get_last_page(table_name=user_comics)
    if new_page > last_page:
        await callback.answer(text=LEXICON_RU['last_page'])
        return

    comic_path: str = DataBase.get_comics_by_name(user_comics, new_page)
    UserBase.write_user(UserRow(telegram_id=callback.from_user.id, page=new_page, comics=user_comics))
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile(comic_path)),
        reply_markup=K.create_main_inline(new_page),
    )
    await callback.answer()


@reading_router.callback_query(F.data == 'backward')
async def send_prev_page(callback: CallbackQuery):
    user_id = callback.from_user.id
    new_page = UserBase.get_page(user_id)[0][0] - 1

    user_comics = UserBase.get_comics(user_id)[0][0]

    if new_page < 1:
        await callback.answer(text=LEXICON_RU['first_page'])
        return

    comic_path: str = DataBase.get_comics_by_name(user_comics, new_page)
    UserBase.write_user(UserRow(telegram_id=callback.from_user.id, page=new_page, comics=user_comics))

    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile(comic_path)),
        reply_markup=K.create_main_inline(new_page),
    )
    await callback.answer()


@reading_router.callback_query(F.data == 'inline_first_page')
async def send_first_page(callback: CallbackQuery):
    user_id = callback.from_user.id
    new_page = 1

    user_comics = UserBase.get_comics(user_id)[0][0]

    comic_path: str = DataBase.get_comics_by_name(user_comics, new_page)
    UserBase.write_user(UserRow(telegram_id=callback.from_user.id, page=new_page, comics=user_comics))
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=FSInputFile(comic_path)),
            reply_markup=K.create_main_inline(new_page),
        )
    except TelegramBadRequest:
        await callback.answer(text=LEXICON_RU['stupid_user'])

    await callback.answer()

    pass
