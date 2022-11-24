from keyboards.inline.review_menu.review_menu import review_menu_button_callbacks
from handlers.users.main_menu_menu.main_menu_funk import main_menu_start
from aiogram.dispatcher import FSMContext
from states.states import StatesGroup
from loader import dp, bot
from aiogram import types

@dp.callback_query_handler(text=review_menu_button_callbacks, state=StatesGroup.stateInReviewsMenu)
async def respond_on_rewievs_menu_buttons(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
    
    if call.data == "back_":
        await main_menu_start(call=call)
    