from keyboards.inline.bar_and_kitchen_menu.bar_and_kitchen_menu import Bar_And_Kitchen_menu_button_callbacks, OpenMenu_button_callbacks
from handlers.vars_for_handlers.vars import set_barMenu_link, set_kitchenMenu_link
from .kitchen_and_bar_funk import send_sale_info_message, send_bar_and_kitchen_info_message
from data.lubimoe_pics.pics_as_obj import get_bar_Menu_Pic, get_kitchen_Menu_Pic
from handlers.commands.start import main_menu_start
from aiogram.dispatcher import FSMContext
from states.states import StatesGroup
from loader import dp, bot
from aiogram import types

@dp.callback_query_handler(text=Bar_And_Kitchen_menu_button_callbacks, state=StatesGroup.stateInBarAndKitchengMenu)
async def respond_on_BarAndKitchen_menu_buttons(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
    if call.data == "Bar_":
        await set_barMenu_link()
        await send_sale_info_message(chat_id=call.from_user.id, photo=await get_bar_Menu_Pic())
    
    elif call.data == "Kitchen_":
        await set_kitchenMenu_link()
        await send_sale_info_message(chat_id=call.from_user.id, photo=await get_kitchen_Menu_Pic())
        
        
    elif call.data == "back_":
        await main_menu_start(call=call)
    
    
@dp.callback_query_handler(text=OpenMenu_button_callbacks, state=StatesGroup.steteInOpenMenu)
async def respond_on_BarAndKitchen_menu_buttons(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)

    if call.data == "back_":
        await send_bar_and_kitchen_info_message(call.from_user.id)
    