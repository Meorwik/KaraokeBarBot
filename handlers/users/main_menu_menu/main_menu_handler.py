from ..kithcen_and_bar_menu.kitchen_and_bar_funk import send_bar_and_kitchen_info_message
from keyboards.inline.start_menu.start_menu import main_menu_button_callbacks
from ..contacts_and_addresses_menu.contacts_and_addresses_funk import get_contacts_and_addresses_menu_text
from ..reviews_menu.reviews_funk import send_reviews_info_message
from aiogram.dispatcher import FSMContext
from states.states import StatesGroup
from loader import dp, bot
from aiogram import types

@dp.callback_query_handler(text=main_menu_button_callbacks, state=StatesGroup.stateInMainMenu)
async def respond_on_main_menu_buttons(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
    if call.data == "Book_":
        # await StatesGroup.stateInBookingMenu.set()
        await call.answer("В процессе разработки")
        
    elif call.data == "BarOrKitchen_":
        await send_bar_and_kitchen_info_message(call.from_user.id)
            
    elif call.data == "Reviews_":
        await send_reviews_info_message(call.from_user.id)
        
    elif call.data == "ContactsAndAddresses_":
        await bot.send_message(chat_id=call.from_user.id, text=await get_contacts_and_addresses_menu_text())
        
    