import asyncio

from aiogram import Bot, types, Router, F
from aiogram.types import Message, InputFile, FSInputFile
import os
import os.path

from db import create_db

rout = Router()

from db import DataBase

bot = Bot(token='6929981160:AAFyRy8CJQpLhaqqxrm6fsX247gfgMADd_Y')


async def upload_and_get_photo_id():
    path_zero = '/Users/danya/CodeProjects/site_for_tz/comics_files'
    for dr in os.listdir(path_zero):
        print(dr)
        DataBase.create_new_comic(dr)
        if os.path.isdir(dr):
            for file in os.listdir(dr):
                print(dr + '/' + file)

                # photo = open(, 'rb')
                message = await bot.send_photo(chat_id=676923918, photo=FSInputFile(dr + '/' + file))
                photo_id = message.photo[-1].file_id
                print(message.photo)

                DataBase.write_data(dr, create_db.ComicRow(comics_photo_url=photo_id))


s = [PhotoSize(file_id='AgACAgIAAxkDAAIBP2WBRglCjsh1vVFRNH3zsg6G_IXuAAKN0DEbLRQISNhc-OMV1CcDAQADAgADcwADMwQ',
               file_unique_id='AQADjdAxGy0UCEh4', width=30, height=90, file_size=988),
     PhotoSize(file_id='AgACAgIAAxkDAAIBP2WBRglCjsh1vVFRNH3zsg6G_IXuAAKN0DEbLRQISNhc-OMV1CcDAQADAgADbQADMwQ',
               file_unique_id='AQADjdAxGy0UCEhy', width=106, height=320, file_size=11727),
     PhotoSize(file_id='AgACAgIAAxkDAAIBP2WBRglCjsh1vVFRNH3zsg6G_IXuAAKN0DEbLRQISNhc-OMV1CcDAQADAgADeAADMwQ',
               file_unique_id='AQADjdAxGy0UCEh9', width=266, height=800, file_size=50529),
     PhotoSize(file_id='AgACAgIAAxkDAAIBP2WBRglCjsh1vVFRNH3zsg6G_IXuAAKN0DEbLRQISNhc-OMV1CcDAQADAgADeQADMwQ',
               file_unique_id='AQADjdAxGy0UCEh-', width=426, height=1280, file_size=107839),
     PhotoSize(file_id='AgACAgIAAxkDAAIBP2WBRglCjsh1vVFRNH3zsg6G_IXuAAKN0DEbLRQISNhc-OMV1CcDAQADAgADdwADMwQ',
               file_unique_id='AQADjdAxGy0UCEh8', width=682, height=2048, file_size=201484)]

lst = []

if __name__ == '__main__':
    asyncio.run(upload_and_get_photo_id())
