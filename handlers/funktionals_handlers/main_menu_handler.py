from ..bot_options.In_BarOrKitchen_menu import send_BarAndKitchen_info_message
from keyboards.inline.start_menu.start_menu import main_menu_button_callbacks
from ..bot_options.In_ContactsAndAddresses import get_contacts_and_addresses_menu_text
from ..bot_options.In_reviews_menu import send_reviews_info_message
from ..vars_for_handlers.vars import get_message_id_to_delete
from aiogram.dispatcher import FSMContext
from states.states import StatesGroup
from loader import dp, bot
from aiogram import types

@dp.callback_query_handler(text=main_menu_button_callbacks, state=StatesGroup.stateInMainMenu)
async def respond_on_main_menu_buttons(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.delete_message(message_id=await get_message_id_to_delete(), chat_id=call.from_user.id)
    if call.data == "Book_":
        
        await StatesGroup.stateInBookingMenu.set()
        await call.answer("В процессе разработки")
        
    elif call.data == "BarOrKitchen_":
        await send_BarAndKitchen_info_message(call.from_user.id)
            
    elif call.data == "Reviews_":
        await send_reviews_info_message(call.from_user.id)
        
    elif call.data == "ContactsAndAddresses_":
        await bot.send_message(chat_id=call.from_user.id, text=await get_contacts_and_addresses_menu_text())
        
    