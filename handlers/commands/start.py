from handlers.users.main_menu_menu.main_menu_funk import main_menu_start
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types
from loader import dp

    
@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    await main_menu_start(message)