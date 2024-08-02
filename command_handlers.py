from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


from protect import check_user


command_router = Router()

@command_router.message(Command("buttons"))
async def delete_message(message: Message):
    if check_user(message.from_user.id):    
        keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Кнопка 2", 
                                            callback_data="button_2"),]]
                                            )
        await message.answer(f"Вот кнопка. После нажатия следующее "\
                            "сообщение удалится через 5 секунд", 
                            reply_markup=keyboard
                            )
    else:
        await message.answer(f"Нет доступа, щенок ебаный")

@command_router.message(Command("start"))
async def start_command(message: Message):
    if check_user(message.from_user.id):
        keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Нажми меня", 
                                               callback_data="button_1"),]]
                                               )
        await message.answer(f"Привет. Это бот. Для того, чтобы узнать "\
                             "полный функционал, перейдите на /help", 
                             reply_markup=keyboard)
    else:
        await message.answer(f"Нет доступа, щенок ебаный")

@command_router.message(Command("help"))
async def help_command(message: Message):
    if check_user(message.from_user.id):
        await message.answer(f"Имеется много чего, но пока ничего нет")
    else:
        await message.answer(f"Нет доступа, щенок ебаный")