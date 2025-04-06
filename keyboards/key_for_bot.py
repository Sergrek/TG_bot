from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Catalog', callback_data='catalog')],
        [InlineKeyboardButton(text='Basket', callback_data='basket'), 
         InlineKeyboardButton(text='Help', callback_data='help')] 
        ] )

settings = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Youtube', url='https://youtube.com')]
            ]
        )

products = ['tovar1', 'tovar2', 'tovar3']

async def key_RB():
    key_build = InlineKeyboardBuilder()
    for product in products:
        key_build.add(InlineKeyboardButton(text=product, url='https://ya.ru'))
    return key_build.adjust(2).as_markup() 



