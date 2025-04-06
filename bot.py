import asyncio
import logging
from aiogram import F, Bot, Dispatcher
from config import TOKEN_BOT
from handlers.for_bot import router

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN_BOT)
dp = Dispatcher()
 
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except  KeyboardInterrapt:
        print('Exit')

