from keyboards.inline.start_menu.start_menu import main_menu_button_callbacks
from ..bot_options.In_reviews_menu import send_reviews_info_message
from ..vars_for_handlers.vars import get_message_id_to_delete
from aiogram.dispatcher import FSMContext
from states.states import StatesGroup
from loader import dp, bot
from aiogram import types

@dp.callback_query_handler(text=main_menu_button_callbacks, state=StatesGroup.stateInMainMenu)
async def respond_on_main_menu_buttons(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    if call.data == "Book_":
        await bot.delete_message(message_id=await get_message_id_to_delete(), chat_id=call.from_user.id)
        await StatesGroup.stateInBookingMenu.set()
        await call.answer("В процессе разработки")
        
    elif call.data == "BarOrRestaurant_":
        await bot.delete_message(message_id=await get_message_id_to_delete(), chat_id=call.from_user.id)
        await StatesGroup.stateInEatingMenu.set()
            
    elif call.data == "Reviews_":
        await bot.delete_message(message_id=await get_message_id_to_delete(), chat_id=call.from_user.id)
        await send_reviews_info_message(call.from_user.id)
        
    elif call.data == "ContactsAndAddresses_":
        await bot.delete_message(message_id=await get_message_id_to_delete(), chat_id=call.from_user.id)
        await bot.send_message(chat_id=call.from_user.id, text="*Contacts And Addresses*")
        
    