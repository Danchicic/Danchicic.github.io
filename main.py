import random

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent, \
    WebAppInfo, Message

API_TOKEN = '6929981160:AAFyRy8CJQpLhaqqxrm6fsX247gfgMADd_Y'

bot = telebot.TeleBot(API_TOKEN)


def create_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    mireaWebApp = WebAppInfo('https://www.mirea.ru/')
    my_site_webapp = WebAppInfo('https://danchicic.github.io/')

    button = InlineKeyboardButton(text='Мирэа', web_app=mireaWebApp)
    button1 = InlineKeyboardButton(text='Интернет магазин', web_app=my_site_webapp)
    kb.add(button, button1)
    return kb


@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(message.chat.id, text='Перейди на один из сайтов', reply_markup=create_kb())


@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    bot.send_message(message.chat.id, text='Перейди на один из сайтов', reply_markup=create_kb())


bot.infinity_polling()
