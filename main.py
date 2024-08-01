import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher
import handlers
import asyncio

load_dotenv()
logging.basicConfig(level=logging.INFO)
# logging in file .log
# logging.basicConfig(
#     filename='bot.log', 
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dispatch = Dispatcher()
dispatch.include_router(handlers.command_router)
dispatch.include_router(handlers.text_router)

async def main():
    await dispatch.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())