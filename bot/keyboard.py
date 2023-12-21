from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from lexicon.lexicon import LEXICON_RU
from db import DataBase


class Keyboard:
    """
    class with keyboard builders
    """

    @staticmethod
    def create_main_inline(user_page: int) -> InlineKeyboardMarkup:
        """
        creating << {page} >> keyboard
        :param user_page: user page
        :return:
        """
        buttons: list[InlineKeyboardButton] = []
        builder = InlineKeyboardBuilder()
        button_list = ['backward', str(user_page), 'forward', 'inline_first_page']
        for button_name in button_list:
            buttons.append(
                InlineKeyboardButton(text=LEXICON_RU.get(button_name, button_name),
                                     callback_data=button_name,
                                     )
            )

        builder.row(*buttons, width=3)

        return builder.as_markup(resize_keyboard=True)

    @staticmethod
    def create_comics_kb() -> ReplyKeyboardMarkup:
        """
        create comics keyboard
        :return:
        """
        builder = ReplyKeyboardBuilder()
        buttons: list[KeyboardButton] = []
        for comic_name in DataBase:
            buttons.append(KeyboardButton(text=comic_name[0]))
        builder.row(*buttons, width=4)
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


K = Keyboard()
