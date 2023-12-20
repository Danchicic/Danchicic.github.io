from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from db import DataBase


class Keyboard:
    def __init__(self):
        pass

    @staticmethod
    def create_main_inline(user_page:int) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        buttons: list[InlineKeyboardButton] = [InlineKeyboardButton(text='Назад', callback_data='back'),

                                               InlineKeyboardButton(text=str(user_page), callback_data='forward'),
                                               InlineKeyboardButton(text='Вперед', callback_data='forward'),
                                               InlineKeyboardButton(text='В начало', callback_data='to first')
                                               ]

        builder.row(*buttons, width=3)

        return builder.as_markup(resize_keyboard=True)

    def create_comics_kb(self) -> ReplyKeyboardMarkup:
        builder = ReplyKeyboardBuilder()
        buttons: list[KeyboardButton] = []
        for comic_name in DataBase:
            buttons.append(KeyboardButton(text=comic_name[0]))
        builder.row(*buttons, width=4)
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


K = Keyboard()
