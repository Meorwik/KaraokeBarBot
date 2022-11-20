from keyboards.inline.start_menu.start_menu import create_main_menu_keyboard
from aiogram.dispatcher.filters.builtin import CommandStart
from ..vars_for_handlers.vars import set_message_id_to_delete
from states.states import StatesGroup
from time import strftime
from loader import dp, bot
from aiogram import types

async def get_greetings_based_on_time():
    user_time = strftime("%H:%M:%S")
    current_time = int(user_time[:2]) 
    if current_time >= 6 and current_time <= 12:
        return "Доброго утра вам"
    elif current_time >= 12 and current_time <= 18:
        return "Добрый день"
    elif current_time >= 18:
        return "Добрый вечер"
    elif current_time <= 6 and current_time >= 0:
        return "Доброй ночи"
    
greeting_text = "\nРады приветствовать вас!\nВыберите, чем я могу вам помочь:"

async def main_menu_start(call):
    message_to_delete_after_reading = await bot.send_message(chat_id=call.from_user.id, text=f"{await get_greetings_based_on_time()}, {call.from_user.full_name}!{greeting_text}", reply_markup=await create_main_menu_keyboard())
    await set_message_id_to_delete(message_id=message_to_delete_after_reading.message_id)
    await StatesGroup.stateInMainMenu.set()
    
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await main_menu_start(message)