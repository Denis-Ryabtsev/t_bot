from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


command_router = Router()
text_router = Router()


@command_router.message(Command("start"))
async def start_command_handler(message: Message):
    await message.answer(f"Привет. Это бот. Для того, чтобы узнать "\
                         "полный функционал, перейдите на /help")

@command_router.message(Command("help"))
async def help_command_handler(message: Message):
    await message.answer(f"Имеется много чего, но пока ничего нет")

@text_router.message()
async def echo_message_handler(message: Message):
    await message.answer(f"Вы отправили: {message.text}")