from aiogram import executor

from loader import dp
import handlers
from admin_panel.notify_admins import on_startup_notify
from bot_settings.set_bot_commands import set_default_commands
from data.LubiMoePics.PicsAsObj import init_pics


async def on_startup(dispatcher):
    # Устанавливаем команды
    await set_default_commands(dispatcher)

    # Уведомляем админов о запуске бота
    await on_startup_notify(dispatcher)
    # Инициализация картинок меню
    await init_pics()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

