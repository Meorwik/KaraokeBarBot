from keyboards.keyboards import (create_reviews_menu_keyboard,
                                 create_kitchen_and_bar_menu_keyboard,
                                 create_eating_menu_keyboard)
from keyboards.keyboards import main_menu_button_callbacks, back_callbacks
from data.texts import texts
from data.urls import get_bar_menu, get_kitchen_menu
from ..commands.start import main_menu_start
from loader import dp, bot
from aiogram import types


@dp.callback_query_handler(text=main_menu_button_callbacks)
async def respond_on_main_menu_buttons(call: types.CallbackQuery):
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
    if call.data == "Book_":
        await call.message.answer("IN PROGRESS")

    elif call.data == "KitchenAndBar_":
        await call.message.answer(text=texts.get("bar_and_kitchen_1"), reply_markup=create_kitchen_and_bar_menu_keyboard())

    elif call.data == "Reviews_":
        await call.message.answer(text=texts.get("reviews"), reply_markup=create_reviews_menu_keyboard())

    elif call.data == "ContactsAndAddresses_":
        await call.message.answer(text=texts.get("contacts_and_addresses"))


@dp.callback_query_handler(text=back_callbacks)
async def return_one_level_lower(call: types.CallbackQuery):
    if call.data == "back":
        await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
        await main_menu_start(call)

    elif call.data == "back_to_bar_and_kitchen":
        await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
        await call.message.answer(text=texts.get("bar_and_kitchen_1"), reply_markup=create_kitchen_and_bar_menu_keyboard())


@dp.callback_query_handler(text=["kitchen_", "bar_"])
async def bar_and_kitchen_callback_handler(call: types.CallbackQuery):
    if call.data == "kitchen_":
        await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
        await call.message.answer(text=texts.get("bar_and_kitchen_2"),
                                  reply_markup=create_eating_menu_keyboard(url=await get_bar_menu()))

    elif call.data == "bar_":
        await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
        await call.message.answer(text=texts.get("bar_and_kitchen_2"),
                                  reply_markup=create_eating_menu_keyboard(url=await get_bar_menu()))
