from aiogram.types import InlineKeyboardButton
from ..settings_for_all_keyboards import init_keyboard, create_back_button

review_menu_button_callbacks = ["back_"]

async def create_instagram_button():
    instagram_button = InlineKeyboardButton(text="Перейти в Instagram", url="https://www.instagram.com/karaokelubimoe/")
    return instagram_button
    
async def create_TwoGis_button():
    Twogis_button = InlineKeyboardButton(text="Перейти в 2Gis", url="https://2gis.kz/almaty/branches/70000001019252897")
    return Twogis_button   

async def create_leaveReview_button():
    leaveReview_button = InlineKeyboardButton(text="Оставить отзыв", callback_data=review_menu_button_callbacks[2])
    return leaveReview_button

async def combine_review_menu_keyboard():
    instagram_button = await create_instagram_button()
    TwoGis_button = await create_TwoGis_button()
    leaveReview_button = await create_leaveReview_button()
    back_button = await create_back_button()
    return [instagram_button, TwoGis_button, leaveReview_button, back_button]

async def create_review_menu_keyboard():
    keyboard = await init_keyboard()
    list_with_buttons = await combine_review_menu_keyboard()
    keyboard.add(*list_with_buttons)
    return keyboard
