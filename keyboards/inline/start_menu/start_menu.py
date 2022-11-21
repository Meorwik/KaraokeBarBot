from aiogram.types import InlineKeyboardButton
from ..settings_for_all_keyboards import init_keyboard

main_menu_button_callbacks = ["Book_", "BarOrKitchen_", "Reviews_", "ContactsAndAddresses_"]

async def create_book_button():
    book_button = InlineKeyboardButton(text="Забронировать", callback_data=main_menu_button_callbacks[0])
    return book_button
    
async def create_menu_button():
    menu_button = InlineKeyboardButton(text="Меню", callback_data=main_menu_button_callbacks[1])
    return menu_button

async def create_review_button():
    review_button = InlineKeyboardButton(text="Отзывы", callback_data=main_menu_button_callbacks[2])
    return review_button

async def create_ContactsAndAddresses_button():
    ContactsAndAddresses_button = InlineKeyboardButton(text="Контакты и адреса", callback_data=main_menu_button_callbacks[3])
    return ContactsAndAddresses_button

async def combine_main_menu_keyboard():
    book_button = await create_book_button()
    menu_button = await create_menu_button()
    review_button = await create_review_button()
    ContactsAndAddresses_button = await create_ContactsAndAddresses_button()
    return [book_button, menu_button, review_button, ContactsAndAddresses_button]

async  def create_main_menu_keyboard():
    keyboard = await init_keyboard()
    list_with_buttons = await combine_main_menu_keyboard()
    keyboard.add(*list_with_buttons)
    return keyboard

