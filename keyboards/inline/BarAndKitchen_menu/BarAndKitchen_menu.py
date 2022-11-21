from aiogram.types import InlineKeyboardButton
from handlers.vars_for_handlers.vars import get_needed_menu
from ..settings_for_all_keyboards import init_keyboard, create_back_button

BarAndKitchen_menu_button_callbacks = ["Bar_", "Kitchen_", "back_"]
OpenMenu_button_callbacks = ["back_"]

async def create_bar_button():
    bar_button = InlineKeyboardButton(text="Бар", callback_data=BarAndKitchen_menu_button_callbacks[0])
    return bar_button
    
async def create_kitchen_button():
    kitchen_button = InlineKeyboardButton(text="Кухня", callback_data=BarAndKitchen_menu_button_callbacks[1])
    return kitchen_button   

async def combine_BarAndKitchen_menu_keyboard():
    bar_button = await create_bar_button()
    kitchen_button = await create_kitchen_button()
    back_button = await create_back_button()
    return [bar_button, kitchen_button, back_button]

async def create_BarAndKitchen_menu_keyboard():
    keyboard = await init_keyboard()
    list_with_buttons = await combine_BarAndKitchen_menu_keyboard()
    keyboard.add(*list_with_buttons)
    return keyboard

async def create_OpenMenu_button():
    OpenMenu_button = InlineKeyboardButton(text="Открыть меню", url=await get_needed_menu())
    return OpenMenu_button

async def combine_OpenMenu_keyboard():
    OpenMenu_button = await create_OpenMenu_button()
    back_button = await create_back_button()
    return [OpenMenu_button, back_button]

async def create_OpenMenu_keyboard():
    keyboard = await init_keyboard()
    list_with_buttons = await combine_OpenMenu_keyboard()
    keyboard.add(*list_with_buttons)
    return keyboard
