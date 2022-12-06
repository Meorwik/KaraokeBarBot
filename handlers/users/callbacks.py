from keyboards.keyboards import (create_reviews_menu_keyboard,
                                 create_kitchen_and_bar_menu_keyboard,
                                 create_eating_menu_keyboard, get_empty_keyboard)
from keyboards.keyboards import main_menu_button_callbacks, back_callbacks
from data.urls import get_bar_menu, get_kitchen_menu
from ..commands.start import main_menu_start
from data.texts import texts
from loader import dp, bot
from aiogram import types


@dp.callback_query_handler()
async def respond_on_callbacks(call: types.CallbackQuery):
    await call.message.delete()
    # -------------------------------------MAIN MENU-----------------------
    if call.data == "Book_":
        await call.message.answer("IN PROGRESS")

    if call.data == "KitchenAndBar_":
        await call.message.answer(text=texts.get("bar_and_kitchen_1"),
                                  reply_markup=create_kitchen_and_bar_menu_keyboard())

    if call.data == "Reviews_":
        await call.message.answer(text=texts.get("reviews"), reply_markup=create_reviews_menu_keyboard())

    if call.data == "ContactsAndAddresses_":
        await call.message.answer(text=texts.get("contacts_and_addresses"), reply_markup=get_empty_keyboard())

    # -------------------------------------BACK BUTTONS-----------------------
    if call.data == "back":
        await main_menu_start(call)

    if call.data == "back_to_bar_and_kitchen":
        await call.message.answer(text=texts.get("bar_and_kitchen_1"),
                                  reply_markup=create_kitchen_and_bar_menu_keyboard())

    # -------------------------------------KITCHEN AND BAR MENU-----------------------
    if call.data == "bar_":
        bar_file = open("data/lubimoe_pics/BarMenu.png", "rb")
        await call.message.answer_photo(photo=bar_file,
                                        caption=texts.get("bar_and_kitchen_2"),
                                        reply_markup=create_eating_menu_keyboard(url=await get_bar_menu()))
        bar_file.close()

    if call.data == "kitchen_":
        kitchen_file = open("data/lubimoe_pics/KitchenMenu.png", "rb")
        await call.message.answer_photo(photo=kitchen_file,
                                        caption=texts.get("bar_and_kitchen_2"),
                                        reply_markup=create_eating_menu_keyboard(url=await get_kitchen_menu()))
        kitchen_file.close()
