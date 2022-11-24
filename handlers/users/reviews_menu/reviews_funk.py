from keyboards.inline.review_menu.review_menu import create_review_menu_keyboard
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
    await bot.send_message(chat_id=chat_id,text=reviews_menu_text, reply_markup=await create_review_menu_keyboard())
    await StatesGroup.stateInReviewsMenu.set()