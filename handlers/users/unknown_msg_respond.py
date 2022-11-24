from states.states import StatesGroup
from aiogram import types
from loader import dp

unknown_command = "Я не понимаю что вы от меня хотите =("
    
@dp.message_handler(state=StatesGroup)
async def unable_to_recognize(message: types.Message):
    await message.answer(text=unknown_command)