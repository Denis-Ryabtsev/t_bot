from aiogram import Router
from aiogram.types import Message


from protect import check_user


text_router = Router()

@text_router.message()
async def echo_message(message: Message):
    if check_user(message.from_user.id):
        await message.answer(f"Вы отправили: {message.text}")
    else:
        await message.answer(f"Нет доступа, щенок ебаный")