from aiogram.dispatcher.filters.builtin import CommandStart
from data.texts import texts
from keyboards.keyboards import create_main_menu_keyboard
from loader import dp,  bot
from time import strftime
from aiogram import types


async def get_greetings_based_on_time():
    user_time = strftime("%H:%M:%S")
    current_time = int(user_time[:2])
    if 6 <= current_time <= 12:
        return "Доброго утра вам"
    elif 12 <= current_time <= 17:
        return "Добрый день"
    elif current_time >= 18:
        return "Добрый вечер"
    elif 0 <= current_time <= 6:
        return "Доброй ночи"


async def main_menu_start(message: types.Message or types.CallbackQuery):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"{await get_greetings_based_on_time()}, "
                            f"{message.from_user.full_name}!{texts.get('greetings')}",
                            reply_markup=create_main_menu_keyboard())


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    await main_menu_start(message)
