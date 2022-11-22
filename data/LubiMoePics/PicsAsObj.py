from aiogram.types.input_file import InputFile



async def get_barMenuPic():
    Bar_file = InputFile("data\LubiMoePics\BarMenu.png")
    return Bar_file

async def get_kitchenMenuPic():
    Kitchen_file = InputFile("data\LubiMoePics\KitchenMenu.png")
    return Kitchen_file

