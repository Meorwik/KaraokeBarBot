from keyboards.inline.BarAndKitchen_menu.BarAndKitchen_menu import BarAndKitchen_menu_button_callbacks, OpenMenu_button_callbacks
from handlers.vars_for_handlers.vars import set_barMenu_link, set_kitchenMenu_link
from ..bot_options.In_BarOrKitchen_menu import send_sale_info_message, send_BarAndKitchen_info_message
from data.LubiMoePics.PicsAsObj import get_barMenuPic, get_kitchenMenuPic
from ..vars_for_handlers.vars import get_message_id_to_delete
from handlers.commands.start import main_menu_start
from aiogram.dispatcher import FSMContext
from states.states import StatesGroup
from loader import dp, bot
from aiogram import types

@dp.callback_query_handler(text=BarAndKitchen_menu_button_callbacks, state=StatesGroup.stateInBarAndKitchengMenu)
async def respond_on_BarAndKitchen_menu_buttons(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.delete_message(message_id=await get_message_id_to_delete(), chat_id=call.from_user.id)
    if call.data == "Bar_":
        await set_barMenu_link()
        await send_sale_info_message(chat_id=call.from_user.id, photo=await get_barMenuPic())
    
    elif call.data == "Kitchen_":
        await set_kitchenMenu_link()
        await send_sale_info_message(chat_id=call.from_user.id, photo=await get_kitchenMenuPic())
        
        
    elif call.data == "back_":
        await main_menu_start(call=call)
    
    
@dp.callback_query_handler(text=OpenMenu_button_callbacks, state=StatesGroup.steteInOpenMenu)
async def respond_on_BarAndKitchen_menu_buttons(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.delete_message(message_id=await get_message_id_to_delete(), chat_id=call.from_user.id)

    if call.data == "back_":
        await send_BarAndKitchen_info_message(call.from_user.id)
    