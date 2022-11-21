from keyboards.inline.review_menu.review_menu import create_review_menu_keyboard
from ..vars_for_handlers.vars import set_message_id_to_delete
from states.states import StatesGroup
from aiogram import types
from loader import bot


reviews_menu_text = """
Наши отзывы можно посмотреть
в нашем instagram или в  2gis.
Вы можете также оставить свой
отзыв.
                    """

async def send_reviews_info_message(chat_id: int):
    message_to_delete_after_reading = await bot.send_message(chat_id=chat_id,text=reviews_menu_text, reply_markup=await create_review_menu_keyboard())
    await set_message_id_to_delete(message_id=message_to_delete_after_reading.message_id)
    await StatesGroup.stateInReviewsMenu.set()