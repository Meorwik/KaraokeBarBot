from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def init_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    return keyboard

async def create_back_button():
    back_button = InlineKeyboardButton(text="Назад", callback_data="back_")
    return back_button