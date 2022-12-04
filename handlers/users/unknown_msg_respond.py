from data.texts import texts
from aiogram import types
from loader import dp


@dp.message_handler()
async def unable_to_recognize(message: types.Message):
    await message.answer(text=texts.get("unknown"))
