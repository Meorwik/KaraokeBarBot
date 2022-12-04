from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menu_button_callbacks = ["Book_", "KitchenAndBar_", "Reviews_", "ContactsAndAddresses_"]
back_callbacks = ["back", "back_to_bar_and_kitchen"]


def create_back_button():
    button = InlineKeyboardButton("Назад", callback_data="back")
    return button


def create_main_menu_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton("Забронировать 🔐", callback_data=main_menu_button_callbacks[0]),
        InlineKeyboardButton("Меню 📕", callback_data=main_menu_button_callbacks[1]),
        InlineKeyboardButton("Отзывы 📈", callback_data=main_menu_button_callbacks[2]),
        InlineKeyboardButton("Контакты и адреса 👤", callback_data=main_menu_button_callbacks[3])
    )
    return keyboard


def create_reviews_menu_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton("Перейти в instagram", url="https://www.instagram.com/karaokelubimoe/"),
        InlineKeyboardButton("Перейти в 2gis", url="https://2gis.kz/almaty/branches/70000001019252897"),
        InlineKeyboardButton("Оставить отзыв", url="https://2gis.kz/almaty/branches/70000001019252897"),
        create_back_button()
    )
    return keyboard


def create_kitchen_and_bar_menu_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton("Кухня 🍖", callback_data="kitchen_"),
        InlineKeyboardButton("Бар 🍸", callback_data="bar_"),
        create_back_button()
    )
    return keyboard


def create_eating_menu_keyboard(url: str):
    keyboard = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton("Открыть меню 🪄", url=url),
        InlineKeyboardButton("Назад", callback_data=back_callbacks[1])
    )
    return keyboard


def get_empty_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1).add(create_back_button())
    return keyboard
