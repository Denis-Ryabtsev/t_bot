from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import asyncio
from datetime import datetime, timedelta

from protect import check_user
from weather import get_weather
from gifs import get_gif

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class Form(StatesGroup):
    waiting = State()

command_router = Router()
user_time = ""

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

@command_router.message(Command("notify"))
async def notify_command(message: Message):
    await message.answer(f"Введи время. Формат ЧЧ:ММ")
    @command_router.message(lambda message: True)
    async def get_usertime(message: Message):
        try:
            msg_time = datetime.strptime(message.text, "%H:%M").time()
            user_time = msg_time
            await message.answer(f"Уведомление установлено на {user_time}")
            #command_router.message.remove(get_usertime)
            asyncio.create_task(send_notify(message.from_user.id, 
                                            user_time, 
                                            message.bot))
        except:
            await message.answer(f"Неверный формат времени")

async def send_notify(user_id: str, time: str, bot: object):
    now_time = datetime.now()
    target = datetime.combine(now_time.date(), time)
    if target < now_time:
        target += timedelta(days=1)
    wait_time = (target - now_time).total_seconds()
    await asyncio.sleep(wait_time)
    await bot.send_message(user_id, f"Просыпайся, дура, уже {time}")

@command_router.message(Command("weather"))
async def weather_command(message: Message):
    location = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отправить геолокацию", request_location=True)]
    ],
    resize_keyboard=True
)
    await message.answer(f"Нажми, чтобы отправить геолокацию", 
                         reply_markup=location)

@command_router.message(F.location)
async def handle_location(message: types.Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    del_mess = await message.answer("Геолокация отправлена, ждите", 
                                    reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(1)
    await message.bot.delete_message(chat_id=del_mess.chat.id, 
                                     message_id=del_mess.message_id)
    data = await get_weather(latitude, longitude)
    await message.answer(f"Готово, получай данные:\n\n{data}")

# @command_router.message(Command("gif"))
# async def gif_command(message: Message):
#     await message.answer(f"Введите тематику")

# @command_router.message()
# async def send_gif(message: Message):
#     print(message.text)
#     await message.bot.send_animation(message.chat.id, 
#                                      await get_gif(message.text))
    
@command_router.message(Command("gif"))
async def gif_command(message: Message, state: FSMContext):
    await message.answer(f"Введите тематику")
    await state.set_state(Form.waiting)

@command_router.message(Form.waiting)
async def senf_gif(message: Message, state: FSMContext):
    await message.bot.send_animation(message.chat.id, 
                                     await get_gif(message.text))
    await state.clear()