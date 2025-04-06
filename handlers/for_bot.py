import asyncio
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import keyboards.key_for_bot as kb

router = Router()
@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.reply(f'Hello!\nYour ID is: {message.from_user.id}', reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply('This is a test bot')

@router.message(F.text == 'How are you?')
async def answer_how(message: Message):
    await message.answer('I am OK')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID photo {message.photo[-1].file_id}')

@router.callback_query(F.data=='catalog')
async def callback_catalog(callback: CallbackQuery):
    await callback.answer('You choose catalog.')
    await callback.message.edit_text('Hello!', reply_markup=await kb.key_RB())
