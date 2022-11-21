from keyboards.inline.BarAndKitchen_menu.BarAndKitchen_menu import create_BarAndKitchen_menu_keyboard, create_OpenMenu_keyboard
from ..vars_for_handlers.vars import set_message_id_to_delete
from states.states import StatesGroup
from aiogram import types
from loader import bot

BarAndKitchen_menu_text = """Выберите какое меню Вы хотите 
посмотреть"""


BarAndKitchen_selected_menu_text = """На всё меню скидки после 21.00"""

async def send_BarAndKitchen_info_message(chat_id: int):
    message_to_delete_after_reading = await bot.send_message(chat_id=chat_id,text=BarAndKitchen_menu_text, reply_markup=await create_BarAndKitchen_menu_keyboard())
    await set_message_id_to_delete(message_id=message_to_delete_after_reading.message_id)
    await StatesGroup.stateInBarAndKitchengMenu.set()
    
async def send_sale_info_message(chat_id: int, photo):
    message_to_delete_after_reading = await bot.send_photo(photo=photo,chat_id=chat_id,caption=BarAndKitchen_selected_menu_text, reply_markup=await create_OpenMenu_keyboard())
    await set_message_id_to_delete(message_id=message_to_delete_after_reading.message_id)
    await StatesGroup.steteInOpenMenu.set()
    
    
