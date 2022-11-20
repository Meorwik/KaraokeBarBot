from ..vars_for_handlers.vars import set_message_id_to_delete, get_message_id_to_delete
from keyboards.inline.review_menu.review_menu import review_menu_button_callbacks
from handlers.commands.start import main_menu_start
from aiogram.dispatcher import FSMContext
from states.states import StatesGroup
from loader import dp, bot
from aiogram import types

@dp.callback_query_handler(text=review_menu_button_callbacks, state=StatesGroup.stateInReviewsMenu)
async def respond_on_main_menu_buttons(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    if call.data == "instsgram_":
        await bot.delete_message(message_id=await get_message_id_to_delete(), chat_id=call.from_user.id)
        pass
    elif call.data == "2gis_":
        await bot.delete_message(message_id=await get_message_id_to_delete(), chat_id=call.from_user.id)
        pass
    elif call.data == "leave_review_":
        await bot.delete_message(message_id=await get_message_id_to_delete(), chat_id=call.from_user.id)
        pass
    elif call.data == "back_":
        await bot.delete_message(message_id=await get_message_id_to_delete(), chat_id=call.from_user.id)
        await main_menu_start(call=call)
    