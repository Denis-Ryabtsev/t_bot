import asyncio


from aiogram import Router, types


callback_router = Router()

@callback_router.callback_query(lambda c: c.data == 'button_1')
async def button_1(callback_query: types.CallbackQuery):
    await callback_query.answer(f'Вы совершили действие!')
    await callback_query.message.answer(f'Кнопка была нажата')

@callback_router.callback_query(lambda c: c.data == 'button_2')
async def button_2(callback_query: types.CallbackQuery):
    await callback_query.answer(f'БА БА БАМ!')
    del_mess = await callback_query.message.answer(f'Кнопка 2 тыкнута')
    await asyncio.sleep(5)
    await callback_query.bot.delete_message(chat_id=del_mess.chat.id, 
                                            message_id=del_mess.message_id)