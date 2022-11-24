from keyboards.inline.bar_and_kitchen_menu.bar_and_kitchen_menu import create_bar_and_kitchen_menu_keyboard, create_open_menu_keyboard
from states.states import StatesGroup
from aiogram import types
from loader import bot

BarAndKitchen_menu_text = """Выберите какое меню Вы хотите 
посмотреть"""


BarAndKitchen_selected_menu_text = """На всё меню скидки после 21.00"""

async def send_bar_and_kitchen_info_message(chat_id: int):
    await bot.send_message(chat_id=chat_id,text=BarAndKitchen_menu_text, reply_markup=await create_bar_and_kitchen_menu_keyboard())
    await StatesGroup.stateInBarAndKitchengMenu.set()
    
async def send_sale_info_message(chat_id: int, photo):
    await bot.send_photo(photo=photo,chat_id=chat_id,caption=BarAndKitchen_selected_menu_text, reply_markup=await create_open_menu_keyboard())
    await StatesGroup.steteInOpenMenu.set()
    
    
