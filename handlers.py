from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os


load_dotenv()
command_router = Router()
text_router = Router()
ALLOWED_USERS = os.getenv('USERS')

def check_user(id: int) -> bool:
    return str(id) in ALLOWED_USERS

@command_router.message(Command("start"))
async def start_command_handler(message: Message):
    if check_user(message.from_user.id):
        await message.answer(f"Привет. Это бот. Для того, чтобы узнать "\
                            "полный функционал, перейдите на /help")
    else:
        await message.answer("Нет доступа, щенок ебаный")

@command_router.message(Command("help"))
async def help_command_handler(message: Message):
    if check_user(message.from_user.id):
        await message.answer(f"Имеется много чего, но пока ничего нет")
    else:
        await message.answer("Нет доступа, щенок ебаный")

@text_router.message()
async def echo_message_handler(message: Message):
    if check_user(message.from_user.id):
        await message.answer(f"Вы отправили: {message.text}")
    else:
        await message.answer("Нет доступа, щенок ебаный")