from aiogram.types.input_file import InputFile

Bar_file = None
Kitchen_file = None

async def get_barMenuPic():
    global Bar_file
    return Bar_file

async def get_kitchenMenuPic():
    global Kitchen_file
    return Kitchen_file

async def init_pics():
    global Bar_file, Kitchen_file
    Bar_file = InputFile("data\LubiMoePics\BarMenu.png")
    Kitchen_file = InputFile("data\LubiMoePics\KitchenMenu.png")